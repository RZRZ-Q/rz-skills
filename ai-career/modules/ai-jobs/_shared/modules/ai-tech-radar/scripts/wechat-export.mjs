#!/usr/bin/env node
// 在已有可读会话中复用 OpenCLI 原版微信下载适配器，不改导航或验证逻辑。
import { access, mkdir, readFile, realpath, stat, writeFile } from 'node:fs/promises';
import { constants } from 'node:fs';
import { dirname, delimiter, join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { parseArgs } from 'node:util';
import { createHash } from 'node:crypto';

const help = `用法：node wechat-export.mjs --session NAME --url URL --output DIR --receipt FILE [--publisher NAME] [--opencli-root DIR]

读取已由本轮浏览器会话打开的微信文章，复用已安装的 OpenCLI weixin/download。
--session       opencli browser 使用的独立会话名；调用期间不要并行导航
--url           本轮实际取得的微信文章地址；支持短链、文章标识长链及搜狗签名地址
--output        本篇文章独立的输出目录
--receipt       保存元数据、结果状态和文件哈希的 JSON 路径
--publisher     可选：核对页面公众号显示名；不代替官方归属证明
--opencli-root  可选：OpenCLI 包根目录；默认沿 PATH 中 opencli 的真实路径定位

需要现有 Node.js 和 OpenCLI。不会安装工具、登录、处理验证页或关闭会话。
返回码 0 表示导出及回读成功；其他结果返回非零并保留收据。`;

function articleKey(value) {
  const url = new URL(value);
  if (url.protocol !== 'https:' || url.hostname !== 'mp.weixin.qq.com') {
    throw new Error('需要 https://mp.weixin.qq.com 的实际文章地址');
  }
  if (/^\/s\/[^/]+$/.test(url.pathname)) return url.origin + url.pathname;
  const fields = ['__biz', 'mid', 'idx', 'sn'];
  if (url.pathname === '/s' && fields.every(key => url.searchParams.get(key))) {
    return url.origin + '/s?' + new URLSearchParams(fields.map(key => [key, url.searchParams.get(key)]));
  }
  // 搜狗可直接落到只有 src/timestamp/ver/signature 的可读原文，不凭空补文章标识。
  if (url.pathname === '/s' && url.searchParams.get('src') === '11' && url.searchParams.get('signature')) {
    url.hash = '';
    url.searchParams.delete('poc_token');
    url.searchParams.sort();
    return url.href;
  }
  throw new Error('无法识别微信文章地址；请使用本轮页面实际 URL');
}

function scrub(value) {
  return JSON.stringify(value, null, 2).replace(/(poc_token=)[A-Za-z0-9_-]+/g, '$1REDACTED');
}

async function opencliRoot(explicit) {
  if (explicit) return resolve(explicit);
  for (const directory of (process.env.PATH || '').split(delimiter)) {
    const executable = join(directory, 'opencli');
    try { await access(executable, constants.X_OK); }
    catch (error) {
      if (['ENOENT', 'EACCES', 'ENOTDIR'].includes(error.code)) continue;
      throw error;
    }
    let current = dirname(await realpath(executable));
    while (true) {
      try {
        const pkg = JSON.parse(await readFile(join(current, 'package.json'), 'utf8'));
        if (pkg.name === '@jackwener/opencli') return current;
      } catch (error) {
        if (error.code !== 'ENOENT') throw error;
      }
      if (dirname(current) === current) break;
      current = dirname(current);
    }
    throw new Error('PATH 中的 opencli 不是可定位的包入口；请显式提供 --opencli-root');
  }
  throw new Error('PATH 中未找到已安装的 opencli；请提供 --opencli-root');
}

let receiptPath;
const receipt = { method: 'opencli_weixin_download_loaded_session', started_at: new Date().toISOString(), status: 'failed' };
try {
  const { values } = parseArgs({ options: Object.fromEntries([
    'session', 'url', 'output', 'receipt', 'publisher', 'opencli-root',
  ].map(name => [name, { type: 'string' }]).concat([['help', { type: 'boolean' }]])) });
  if (values.help) {
    console.log(help);
    process.exit(0);
  }
  receiptPath = values.receipt && resolve(values.receipt);
  for (const key of ['session', 'url', 'output', 'receipt']) {
    if (!values[key]?.trim()) throw new Error(`缺少 --${key}；用 --help 查看用法`);
  }
  const expected = articleKey(values.url);
  receipt.session = values.session;
  receipt.article_url = expected;
  const root = await opencliRoot(values['opencli-root']);
  const pkg = JSON.parse(await readFile(join(root, 'package.json'), 'utf8'));
  if (pkg.name !== '@jackwener/opencli') throw new Error('--opencli-root 不是 @jackwener/opencli 包');
  receipt.opencli_version = pkg.version;
  const load = relative => import(pathToFileURL(join(root, relative)).href);
  const { Page } = await load('dist/src/browser/page.js');
  const { getRegistry } = await load('dist/src/registry.js');
  const { buildDetectWechatAccessIssueJs } = await load('clis/weixin/download.js');
  const adapter = getRegistry().get('weixin/download');
  if (typeof adapter?.func !== 'function' || typeof buildDetectWechatAccessIssueJs !== 'function') {
    throw new Error('当前 OpenCLI 内部接口不兼容；停止，不修改安装或替换验证逻辑');
  }
  const snapshotJs = `(() => {
    const first = (...selectors) => selectors.map(s => document.querySelector(s)?.textContent?.replace(/\\s+/g, ' ').trim()).find(text => text && text !== 'Name cleared') || '';
    const text = document.querySelector('#js_content')?.innerText || '';
    return { url: location.href, title: first('#activity-name', '#js_text_title', '.rich_media_title'),
      publisher: first('#js_name', '.wx_follow_nickname', '#profileBt .profile_nickname', '.rich_media_meta_nickname'),
      published_at: first('#publish_time'), body_chars: text.length, body_start: text.slice(0, 300), body_end: text.slice(-400),
      access_issue: (${buildDetectWechatAccessIssueJs()})(document.body?.innerText || '', document.documentElement.innerHTML) };
  })()`;
  const page = new Page(values.session);
  const before = await page.evaluate(snapshotJs);
  receipt.before = { ...before, url: before.url.replace(/(poc_token=)[A-Za-z0-9_-]+/g, '$1REDACTED') };
  if (before.access_issue) throw new Error(`当前会话不可读：${before.access_issue}`);
  if (articleKey(before.url) !== expected) throw new Error('当前会话不是指定文章；停止导出');
  if (!before.body_chars || !before.title || !before.publisher) throw new Error('当前会话没有可核对的文章正文、标题或公众号');
  if (values.publisher && before.publisher !== values.publisher) throw new Error('当前公众号显示名与 --publisher 不一致');

  // 传当前真实 URL，保留原版 goto 和验证检查；不重新创建下载会话。
  receipt.result = await adapter.func(page, { url: before.url, output: values.output, 'download-images': false });
  if (!Array.isArray(receipt.result) || receipt.result.length !== 1 || receipt.result[0].status !== 'success') {
    throw new Error('OpenCLI 未返回正文导出 success；见 result，不能仅凭进程状态判断');
  }
  const row = receipt.result[0];
  const after = await page.evaluate(snapshotJs);
  receipt.after = after;
  if (after.access_issue || articleKey(after.url) !== expected || after.title !== before.title || after.publisher !== before.publisher || !after.body_chars) {
    throw new Error('导出后页面身份或可读状态变化；本次不计成功');
  }
  const saved = resolve(row.saved);
  let content = await readFile(saved, 'utf8');
  if (!content.includes(before.title) || !content.includes(before.publisher)) throw new Error('导出文件未包含对应标题或公众号');
  // 原版导出保留当前 URL；仅遮盖浏览器自动附加的临时参数。
  receipt.downloaded_bytes = (await stat(saved)).size;
  const sanitized = content.replace(/(poc_token=)[A-Za-z0-9_-]+/g, '$1REDACTED');
  if (sanitized !== content) await writeFile(saved, sanitized);
  receipt.file = { path: saved, bytes: Buffer.byteLength(sanitized), sha256: createHash('sha256').update(sanitized).digest('hex'), transient_url_redacted: sanitized !== content };
  receipt.published_at = row.publish_time;
  receipt.status = 'success';
} catch (error) {
  receipt.error = { message: error.message, ...(error.code && { code: error.code }) };
  process.exitCode = 1;
} finally {
  receipt.completed_at = new Date().toISOString();
  const serialized = scrub(receipt) + '\n';
  if (receiptPath) {
    await mkdir(dirname(receiptPath), { recursive: true });
    await writeFile(receiptPath, serialized);
  }
  if (receiptPath || process.exitCode) console.log(serialized);
}
