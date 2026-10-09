# 小红书图文读取

按[首次引导](onboarding.md)补齐环境，复用用户指定且已登录的 GUI Chrome profile 和 OpenCLI Browser Bridge。`opencli profile list` 只证明连接，实际搜索或详情可读才是本轮登录证据。采集中不安装或升级工具，不读 Cookie、不自动登录，不访问收藏、私信或创作者后台。

## 搜索或给定链接

条件、预算和排重沿用[采集子流程](find-interviews.md)。先读当前搜索页最多 20 个候选，不足才滚动加载，只打开可能匹配的帖子。搜索、导航、滚动、翻图与截图串行，遵守约定间隔；已开页面只读提取可小批并行，范围见下文。

OpenCLI 通用浏览器可直接打开搜索页面：把简短关键词用标准 URL 编码放入 `https://www.xiaohongshu.com/search_result?keyword=ENCODED_QUERY&source=web_search_result_notes`。用独立搜索 session 保存返回的 `page`，通过 `state` 和 `find` 检查页面及实际卡片，再读取可见卡片的标题、片段和笔记链接。保留从页面取得的完整访问链接，不猜 note ID 或 `xsec_token`。搜索卡片只用于选候选，不能充当正文。

用户指定排序、笔记类型、发布时间、搜索范围或位置时，在当前页的筛选面板设置；通过 `state`／`find` 确认实际控件及选中状态，不猜筛选 URL 参数。页面没有对应选项或无法确认生效时说明限制，不把未筛选结果当作已满足条件。页面的相对时间筛选仍须逐帖核对日期。

官方 OpenCLI `1.8.8` 已包含上述五类搜索筛选，但 `xiaohongshu search` 会自动滚动收集，页面渲染收缩时还可能重开一次；`--limit` 不是页面操作预算。因此本流程仍在当前搜索页按预算读取，不另跑该命令重复搜索。其 `published_at` 来自 note ID 推算，不能用于补年或时间筛选。上游能力及保留的本地补充见[环境说明](environment.md#opencli-能力与本地补充)。

每篇从首次打开起使用独立 session，返回的 `page` 保存为该篇 `TAB_ID`。把用户或本轮页面提供的完整访问链接直接解析到本轮私有 `access-url.txt`，不手工重写 URL 或 `xsec_token`；调用前设置 `umask 077`，打开前与来源完整字符串核对。用随包入口从 stdin 读取链接；`OPENCLI_PACKAGE` 为环境检查确认的已安装 `@jackwener/opencli` npm 包根绝对路径，局部安装通常在 `interview-results/runtime/npm/node_modules/@jackwener/opencli`：

```bash
node "$SKILL_DIR/scripts/open_xhs.mjs" \
  --opencli-package "$OPENCLI_PACKAGE" --profile "$BROWSER_PROFILE" --session "$POST_SESSION" \
  < ./tmp/post-01/access-url.txt
opencli --profile "$BROWSER_PROFILE" browser "$POST_SESSION" --window background state --tab "$TAB_ID"
```

入口只在同一 Node 进程转交给原生 OpenCLI，不额外导航、不重试，不将链接放入启动参数或环境变量；原生输出／日志仍可能包含完整 URL，须留在私有目录。链接限 HTTPS 小红书详情页或 `xhslink.com` 短链；短链按采集子流程确认最终身份并立即排重。包路径不明时先根据环境报告的可执行文件／安装目录定位，不复制旧补丁包或静默换工具。

读取并行数及验证范围按[首次引导](onboarding.md#3-说明默认并行度再让用户选择)确认，按此大小逐个打开并核对页面，再并行提取正文、日期及图片链接，各帖独立保存。并行仅限已加载 DOM 和日期／媒体信息，不导航、刷新、滚动、翻图、截图或执行 fetch；每条结果核对 note ID，失败后停止新增批次、收齐在途调用。不使用 `xiaohongshu note` 后重开补图：该命令会压平正文空白，且缺少图片和原始发布时间。

## 正文与日期

确认目标页面可读后，优先使用随 Skill 提供的 [提取表达式](../scripts/capture_xhs.js)，一次返回可见正文、原始／修改时间和完整图片地址，无网络请求或页面修改：

```bash
opencli --profile "$BROWSER_PROFILE" browser "$POST_SESSION" --window background eval \
  "$(cat "$SKILL_DIR/scripts/capture_xhs.js")" --tab "$TAB_ID"
```

表达式检查实际 HTTPS／域名、详情路径及元数据 ID；标题、正文和图片全空时失败，纯图片帖仍可提取。返回的 JSON 字符串解析为对象，保存为本帖 `snapshot.json`，不保存 OpenCLI 响应外壳。下载或入库前，将返回的 `note_id` 与本轮目标核对；`image_count` 仅在取得完整 `imageList` 时给出，DOM 回退不证明图片齐全。结合该字段、可见图数和下载清单的 `unique_count`／`downloaded_count` 判断覆盖，不把达到图片预算称为完整读取。页面结构不符时按下文检查容器，不逐篇重写 `eval` 或以空材料充成功。

先确认最终 URL、主帖标题、正文容器和图文区域，排除搜索卡片、评论及推荐内容。通过已确认容器的 `innerText` 保留换行和原句；`#detail-title`、`#detail-desc` 是可检查的候选选择器，页面没有时先查看实际 DOM，不返回空字符串冒充成功。正常展开或滚动读至正文末尾。

发布日期优先取明确的页面原始发布时间；仅有月日、相对时间或“编辑于”时，可以只读同一已打开页面的时间元数据。必须把元数据中的 note ID 与目标核对，区分原始 `time` 和修改 `lastUpdateTime`；不能用编辑时间、采集时间或 note ID 解码代替发帖年。无法核实时保留未知，按 [整理子流程](organize-interviews.md) 的日期规则整理，不重复打开帖子补字段。

页面状态可能包含 Vue ref／computed 对象。不要直接序列化 `currentNoteId`、整份 state 或笔记对象，会遇到循环引用；先确认字段路径，遇到 `__v_isRef === true` 时取 `.value`，最终只返回笔记 ID、`time`、`lastUpdateTime` 的字符串／数值。字段仍是对象或没有明确含义时保留缺失，不展开整个对象图。正文仍取 DOM，不以状态里的文案代替可见正文。

交付和排重使用采集子流程中的规范公开链接；带 `xsec_token` 的访问链接及原始记录仅存本轮私有材料，不放入文档、飞书或 Git。后续访问仍取用户或当前页面提供的完整链接，不生成参数或假定规范链接可再次读取。

## 图片中的问题

按采集子流程先保存本批材料、后本地统一转录；采集时只核对经历相关性、清晰度和覆盖范围。

### 优先保存当前帖的 CDN 图片

从主帖媒体容器取得完整 `currentSrc`／`src`，或同 note ID 已加载 `imageList` 中的 `urlDefault` 等地址；正文仍取可见 DOM。排除头像、评论和推荐图，不删参数、改路径或猜图片 ID。脚本仅将限定小红书 CDN 主机的 HTTP 改为 HTTPS，同时保留原始及请求地址，其余部分不变。可与正文、日期合并一次 `eval --tab`，不为下载重开帖子。

保存私有 JSON，至少包含规范帖子 `url` 和去重前的 `image_urls` 字符串列表；正文、标题和日期依据可在同份材料中保留。用本 Skill 的 [图片下载脚本](../scripts/download_xhs_images.py) 串行下载：

```bash
python3 "$SKILL_DIR/scripts/download_xhs_images.py" \
  --input ./tmp/post-01/snapshot.json \
  --output-dir ./tmp/post-01/images \
  --max-images 6 --max-bytes 20971520
```

输出目录必须尚不存在；默认每帖最多6张、总量20 MiB，用户较小预算优先。跨帖下载也串行；脚本不接触浏览器或 Cookie，只请求材料里实际取得的 HTTPS 小红书 CDN 地址，不重定向、不重试。保留 `images.json` 中来源链接与本地文件的对应关系，逐张用宿主视觉能力确认可读性；下载完成不等于读图完成。网络、HTTP、格式或超限错误时停止，不再改用截图重试访问。

**下载顺序无需等于轮播顺序。** 出处写“本地图片编号＋图内题号／原句”，原图位置未知时不以文件编号代替。按题号、轮次标题和明确上下文整理，跨图归属不明时不猜接续，也不为恢复顺序额外翻图或重下。

### 无可用下载地址时截图

当前页正常，但无法取得主帖图片地址，或本地图片文字确实不清晰时，可在已有页面按下列方法截图。不得用此分支绕过网络失败、登录、验证码或访问限制。

先确认当前帖是文字、图文还是视频及实际图片容器，不假定每篇都有轮播或直接读取可能不存在的 `swiper` 对象。用页面显示的轮播数量确认图数，在同一帖子内正常点击下一张或展开图片，每张保存独立截图：

```bash
opencli --profile "$BROWSER_PROFILE" browser "$POST_SESSION" --window background screenshot "$IMAGE_PATH" --tab "$TAB_ID"
```

截图后用宿主视觉确认图序、文字清晰且目标未截断，再翻页，暂不逐题转录。箭头遮字时在当前图展开大图，确认遮挡消失后截图，不猜字或离开后补图。展开后重新用 `state`／`find` 定位含图序的翻页组，排除同类缩放控件；不凭 `:first-child` 猜位置，使用 `--nth` 前先核对实际顺序及唯一目标。点击后核对图序，失败不能继续截图冒充已翻页。

`IMAGE_PATH` 是本轮新文件；保存时记录已确认的原帖图号及对应文件，分段截图同时记录段序。长图按正常滚动分段，仍归于同一张图。只截到一部分、文字看不清或宿主不能看图时，明确缺口，不把截图存在当作读图完成。不调用外部 OCR 服务，不要求新 Agent。

每个来源帖默认最多读 6 张图，下载与截图共用预算，合集拆篇不重置；用户指定其他上限时沿用。未收齐就说明部分读取，只标注明确的经历／轮次和原图位置，不把乱序下载称为“前6张”。视频暂不转录。本地整理仅保留看清且有经历依据的完整提问，不猜残题；正文、图片重复题不重复计数，出处保留本地编号、图内位置及已核实原图号。完整／部分读取分别标记，飞书缺口按[整理子流程](organize-interviews.md)写入对应主记录。

## 保存与停止条件

保存规范公开链接、标题、可见正文、发布时间依据、下载图片／截图与转录，以及本地图片标识、已确认的原图位置和未读范围；文本标记 `browser_visible_body`，图片文字注明视觉转录。材料只服务于来源核对，不要求用户处理固定 JSON。调用前设置 `umask 077`，含访问参数的日志与材料只进入本轮私有目录。

遇登录页、验证码、安全限制、网络错误或 Bridge 关闭，立即停止本轮平台访问并保留原始错误，不重试、换账号或渠道。单帖内容缺口、经历判断及后续交付按[采集子流程](find-interviews.md)执行。
