# B 站视频面经与学习材料

按[首次引导](onboarding.md)准备官方 OpenCLI、Chrome 和 Browser Bridge，复用用户指定的 `BROWSER_PROFILE`。本文接口已对照官方 OpenCLI `1.8.8` 源码，不要求安装定制 Bridge。连接成功不证明平台登录或字幕可读，不自动登录、导出 Cookie 或安装其他采集工具。

## 范围、预算与身份

B 站仅在用户选择时加入，默认全部串行。沿用[采集子流程](find-interviews.md)所有平台合计 3 批搜索、5 篇详情的预算；每次搜索翻页另计一批，**每个分 P 计一次详情**，同一 P 的元数据和字幕属于这次详情。先判断候选再读字幕，不自动遍历全集；视频数、已读分 P 数和符合条件的经历数分别报告。

搜索、元数据和字幕命令都遵守本轮约定的访问间隔，包括同一 P 内的两条命令。下一条执行前，按上一条平台命令的实际完成时间核对间隔，等待不足的部分；不能只凭已做过本地整理就假定间隔已满足。

BVID 只取用户输入或本轮真实视频链接。核对最终主机为 `www.bilibili.com`、`bilibili.com` 或 `m.bilibili.com`，路径为 `/video/BV…`，BV 身份保持原大小写；不凭标题猜 ID。`b23.tv` 短链先正常打开一次，核实最终主机、视频身份与 `p`，立即排重；实际打开占详情预算。

按“视频＋分 P”排重：P1 规范链接为 `https://www.bilibili.com/video/BVID`，其他 P 为 `https://www.bilibili.com/video/BVID?p=N`，不把不同 P 合并。访问链接里的 `p=N` 必须显式传给下面两个 `--page`；未指定 P 时只读 P1。传入原视频 URL 并不会让命令自动采用其中的 `p`。

## 搜索候选

```bash
opencli --profile "$BROWSER_PROFILE" bilibili search "$QUERY" \
  --type video --page 1 --limit 20 --window background --site-session ephemeral -f json
```

`search` 只请求指定的一页，没有自动翻页或滚动；`--limit` 截取该页结果，不会补足数量。输出包含标题、作者、播放量和视频链接，缺少发布日期与完整内容，只作候选依据；没有排序或时间筛选参数，不能声称“最新”。该版本未检查搜索 API 的业务错误码，错误响应也可能变成空列表，因此**空列表不能单独证明没有结果**；保留原始输出，记录状态未核实，不自动重复搜索或换工具。接口见[官方 search.js](https://github.com/jackwener/OpenCLI/blob/v1.8.8/clis/bilibili/search.js)。

## 详情与带时间轴的字幕

确认本次读取的 `BVID` 与 `PART`（从 1 开始）后，依次执行：

```bash
opencli --profile "$BROWSER_PROFILE" bilibili video "$BVID" \
  --page "$PART" --window background --site-session ephemeral -f json
```

核对返回的 `bvid`、`page`、`cid`，保留分集标题、`series_title`、作者、简介、时长与发布时间。`description` 是整视频共享简介；只有明确标注了所选 P 的对应内容，才能归入该 P，否则仅作视频背景并注明归属未确认，不能在多个 P 重复计题。`publish_time` 由 UTC 时间格式化而来，输出未带时区标记，保存时注明 UTC；视频发布日期不等于面试发生日期。详情命令会导航到视频页，但元数据和简介不是完整视频内容。接口见[官方 video.js](https://github.com/jackwener/OpenCLI/blob/v1.8.8/clis/bilibili/video.js)。

```bash
opencli --profile "$BROWSER_PROFILE" bilibili subtitle "$BVID" \
  --page "$PART" --window background --site-session ephemeral -f json
```

保存原始字幕的 `index`、`from`、`to` 和 `content` 原句，问题出处写成“规范视频链接＋P＋字幕起止秒／序号”，与前一步 `cid` 对应。字幕时间是该 P 内的相对时间，不是发布日期。长输出须完整读取已保存材料，工具展示截断不等于字幕完整。

默认选第一条字幕轨；可用 `--lang` 指定语言，但找不到时仍会回退第一轨，输出也不包含实际轨道语言或人工／ASR 标记。不能据请求参数声称语言匹配，不能把类型未知的字幕写成人工转录；保留“实际语言／字幕类型未核实”，明显识别错误或残句列为待核实，不猜原题。命令无时间范围或条数参数，会取所选 P 的整条字幕，见[官方 subtitle.js](https://github.com/jackwener/OpenCLI/blob/v1.8.8/clis/bilibili/subtitle.js)。

这三条命令需要浏览器会话，接口请求复用该会话；搜索和详情没有强制登录检查，不能预先保证匿名可用。真实登录、验证码或账号／平台级访问限制立即停止；单视频收费／权限按[采集子流程](find-interviews.md#取得并保存材料)跳过。网络／执行错误保留原错，仅下文明确的导航拒绝可恢复。明确表示无字幕的 `EMPTY_RESULT` 属于本视频内容缺口，可在剩余预算内处理其他候选。原生浏览器层有有界的连接／页面瞬态恢复，不能宣称底层“零重试”；Skill 不重放失败命令。[原生执行层](https://github.com/jackwener/OpenCLI/blob/v1.8.8/src/execution.ts)、[浏览器传输](https://github.com/jackwener/OpenCLI/blob/v1.8.8/src/browser/daemon-client.ts)。

## 已确认导航故障的临时 trace 模式

适用已诊断的官方 OpenCLI `1.8.8`／Bridge `1.0.24`／Chrome 154 环境：搜索或字幕返回精确 `COMMAND_EXEC: Pre-navigation to https://www.bilibili.com failed: Navigation rejected.`，或详情返回精确 `UNKNOWN: Navigation rejected.`，且已确认 trace 模式可读。用户已同意临时兼容方案时，在已授权的 `bilibili search`、`bilibili video` 和 `bilibili subtitle` 首次执行时直接追加 `--trace retain-on-failure`；沿用原 profile、关键词或 BVID／P、后台模式及剩余预算，不为触发条件重复制造普通模式失败。失败访问仍计入预算，换批次或 CLI 不重置；其他环境仍使用正常命令。

trace 启用网络捕获，改变导航前的调试连接 detach 行为，相关问题见上游 [#2487](https://github.com/jackwener/OpenCLI/issues/2487)。这是临时兼容方式，不代表根因修复或长期稳定。`retain-on-failure` 只在失败时导出日志；日志留在本地私有目录，不放入 Skill 或公开材料。保留官方 CLI／扩展，不将 trace 设为全局或其他平台的默认。

这不是额外重试额度；trace 命令出现导航、网络或执行错误时保留原错并停止本轮 B站访问，不叠加下文页面恢复、重启或其他渠道。明确无字幕的 `EMPTY_RESULT`、单视频收费／权限仍按单帖缺口处理；真实登录、验证码或账号／平台级限制仍停止。已有授权直接沿用。升级后是否仍需要该参数，应按新的有界验证结果判断。

## 导航拒绝后的单次页面核验

仅限官方 `1.8.8` 的只读 `bilibili video` 返回精确 `UNKNOWN: Navigation rejected.`，且输入 BV ID／P 与原始来源链接已知。该实现先导航详情页，再读取视频 API；此错误能定位到导航调用，不能证明页面未打开，也不能确定 Chrome 拒绝原因。其他命令、超时、HTTP 401／403／429、登录或访问限制不凭 `Navigation` 子串进入此分支。

1. 保留失败日志，只读核对 daemon 与原 profile。已有本轮身份正确的页面时先复用其 session／tab；不要改全局配置、换 profile 或重启浏览器。
2. 无可复用页面且连接正常时，从失败及在途命令完成的较晚时间起至少等 35 秒，沿用原来源 URL，在独立后台 session 打开一次；这只是给本地会话回收留时间，不是平台安全频率保证：

   ```bash
   opencli --profile "$BROWSER_PROFILE" browser "$RECOVERY_SESSION" --window background tab new "$SOURCE_URL"
   ```

3. 保存返回的 `TAB_ID`，用同一 session、`--tab "$TAB_ID"` 和 `--window background` 的 `state`／只读 DOM 核对 URL、BV 身份、所选 P、标题与门禁。可读时，从页面已加载的视频状态读取 `bvid`、`pages` 中对应 P 的 `cid`、标题和简介；与可见页面核对，只返回必要字段，不序列化整份状态。元数据缺失或身份不符时说明缺口，不猜值或补发 API。
4. 元数据恢复成功、没有门禁且预算仍允许时，继续上文原生 `subtitle`，明确同一 BVID／P；已有明确诊断和授权时按临时 trace 模式执行，不再调用失败的 `video`。字幕成功才可整理其中的原题；后续再次导航失败时停止，门禁按上述限制范围处理。

整个逻辑采集阶段共用一次恢复打开额度，换来源、session、子批次或 CLI 不重置。未单列访问次数时，失败详情占 1 次详情额度，额外恢复打开再占 1 次；同一 BV／P 的来源数不增加，正常元数据与字幕仍归这份详情。恢复使用新日志路径。已确认的单视频限制／内容缺口按上述范围跳过；其余打开失败、身份不符或仍不可读时停止平台访问，不再尝试其他分支或追加 trace。仅要求诊断、没有剩余访问预算或缺少原始来源 URL 时只报告阻塞。页面核验成功只证明本次页面可读，不能据此宣称原生详情命令已修复。

## 判断与交付

只有简介或已读字幕明确描述实际面试经历及其真实提问，才按采集子流程判断公司、岗位、招聘类型与时间。标题叫“面经”不足以入选。模拟面试、知识讲解、备考题单单独标明性质，仅在用户选择学习材料时进入[学习与刷题](study-pack.md)，不混入实际经历的原题数量。

没有字幕时可保留已读简介；简介没有实际提问就不计原题，不把无字幕等同于无内容。默认不运行 `bilibili download`，不下载音视频、不调用外部 ASR，也不换工具绕过门禁。原生下载命令会调用 yt-dlp 并读取浏览器 Cookie，属于另一条流程；`bilibili summary` 是平台 AI 总结，也不能替代原始字幕或证明真实提问。[下载源码](https://github.com/jackwener/OpenCLI/blob/v1.8.8/clis/bilibili/download.js)、[总结源码](https://github.com/jackwener/OpenCLI/blob/v1.8.8/clis/bilibili/summary.js)。

只读部分 P、字幕缺失、只取得简介、画面内容未读或字幕有识别疑点时，明确覆盖范围。字幕可读不代表画面里的板书、代码或题目已读；未核实的内容不补入原题。取得材料后沿用[整理子流程](organize-interviews.md)完成原题与来源交付，学习材料按其独立用途标注。
