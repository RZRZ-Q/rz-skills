#!/usr/bin/env node
// 将 stdin 链接交给同进程的原生 OpenCLI；原生输出／日志仍可能含完整 URL。
import { readSync, readFileSync, realpathSync, statSync } from 'node:fs';
import { isAbsolute, relative, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const names = ['--opencli-package', '--profile', '--session'];
const values = new Map();
const args = process.argv.slice(2);
for (let index = 0; index < args.length; index += 2) {
  const [name, value] = args.slice(index, index + 2);
  if (!names.includes(name) || values.has(name) || !value?.trim() || value.startsWith('--')) {
    throw new Error('参数必须各提供一次：--opencli-package ABSOLUTE_PATH --profile PROFILE --session SESSION');
  }
  values.set(name, value);
}
if (values.size !== names.length || !isAbsolute(values.get('--opencli-package'))) {
  throw new Error('必须提供 npm 包根绝对路径、profile 和独立 session。');
}
const packageRoot = realpathSync(values.get('--opencli-package'));
const metadata = JSON.parse(readFileSync(resolve(packageRoot, 'package.json'), 'utf8'));
if (metadata.name !== '@jackwener/opencli' || typeof metadata.bin?.opencli !== 'string') {
  throw new Error('指定目录必须是具有 bin.opencli 的 @jackwener/opencli npm 包。');
}
const entry = realpathSync(resolve(packageRoot, metadata.bin.opencli));
const entryRelative = relative(packageRoot, entry);
if (isAbsolute(entryRelative) || entryRelative === '..' || entryRelative.startsWith('../')
    || entryRelative.startsWith('..\\') || !statSync(entry).isFile()) {
  throw new Error('OpenCLI 入口必须是包目录内的现有文件。');
}

const maximumBytes = 16 * 1024;
const buffer = Buffer.alloc(maximumBytes + 1);
let size = 0;
while (size <= maximumBytes) {
  const count = readSync(0, buffer, size, buffer.length - size, null);
  if (count === 0) break;
  size += count;
}
if (size > maximumBytes) throw new Error('stdin URL 超过 16 KiB。');
const input = new TextDecoder('utf-8', { fatal: true }).decode(buffer.subarray(0, size)).trim();
if (!input || /\s/u.test(input)) throw new Error('stdin URL 不能为空或包含内部空白。');
let url;
try {
  url = new URL(input);
} catch {
  throw new Error('stdin URL 格式无效。');
}
const authority = input.match(/^https:\/\/([^/?#]+)/i)?.[1];
const detail = url.hostname === 'www.xiaohongshu.com'
  && /^\/(?:explore|search_result)\/[a-f0-9]{6,80}\/?$/i.test(url.pathname);
const shortLink = url.hostname === 'xhslink.com' && url.pathname !== '/';
if (!authority || authority.includes('@') || url.protocol !== 'https:'
    || url.username || url.password || (url.port && url.port !== '443')
    || (!detail && !shortLink)) {
  throw new Error('仅支持无认证、HTTPS 默认端口的小红书详情链接或 xhslink.com 短链。');
}

process.argv = [process.execPath, entry, '--profile', values.get('--profile'),
  'browser', values.get('--session'), '--window', 'background', 'tab', 'new', input];
await import(pathToFileURL(entry).href);
