# 牛客搜索与正文读取

使用本 Skill 的[标准库脚本](../scripts/search_nowcoder.py)，需要 Python 3.9+。`SKILL_DIR` 是 Skill 目录；每次使用独立、尚不存在的输出目录，父目录须已存在，不自动重试。

## 搜索

```bash
python3 "$SKILL_DIR/scripts/search_nowcoder.py" \
  --query "大模型 秋招 面经" --pages 1 \
  --output-dir ./tmp/interview-search-01
```

每页最多 20 条，一次最多 3 页。脚本请求 `order=create`，按帖子公开链接去重，保存 `results.json`。`text_scope=search_excerpt` 只是搜索片段，可能被平台省略或重排；`body_truncated=false` 不证明原帖已完整返回。`fetched_at` 是采集时间。

需要页面上的“面经”分类、“默认／最新”或其他筛选时使用已有浏览器，按[采集子流程](find-interviews.md) 的定位与选中状态核对规则操作；脚本没有这些可选参数，不猜接口参数模拟按钮，不对同一条件再跑一遍脚本搜索。

## 读取详情

讨论帖 `https://www.nowcoder.com/discuss/数字ID` 与动态帖 `https://www.nowcoder.com/feed/main/detail/32位小写UUID` 都用 `--url`：

```bash
python3 "$SKILL_DIR/scripts/search_nowcoder.py" \
  --url "$POST_URL" --output-dir ./tmp/interview-post-01
```

脚本分别使用 `content-data/detail` 与 `moment-data/detail` 的匿名 JSON 接口；动态响应核对 UUID。每篇只请求一次，保存全部返回正文为 `text_scope=post_body`，未返回内容不算已读。

`created_at` 来自原始 `createdAt`（Unix 毫秒），`edited_at` 来自 `editTime`，缺失留空；补年只用原始时间，不用修改或采集时间。`has_images` 同时检查正文图片和独立 `imgMoment` 附件，附件原样保存为 `image_attachments`。此路线只读文字，未读图片明确说明；有文字不等于已读全帖图文。

独立请求与输出可小批并行，默认值、验证范围和用户选择见[引导说明](onboarding.md#3-说明默认并行度再让用户选择)，全部占本轮详情预算。失败后停止新请求、收齐在途调用；不以搜索摘要补失败详情，不在网络／登录／访问限制后切浏览器重试。

## 已有浏览器路线

用户指定浏览器或需要页面内容时，按[首次引导](onboarding.md)补齐环境，`opencli profile list` 确认用户指定的现有 profile，不切换身份或采集中安装工具。每篇用独立 session，返回的 `page` 保存为 `TAB_ID`，后续始终指定该 tab：

```bash
opencli --profile "$BROWSER_PROFILE" browser "$POST_SESSION" --window background tab new "$POST_URL"
opencli --profile "$BROWSER_PROFILE" browser "$POST_SESSION" --window background state --tab "$TAB_ID"
```

核对 URL、标题和作者正文容器，再只读该容器 `innerText`，标记 `browser_visible_body`。`.feed-content-text` 是动态帖可检查的候选，不盲用选择器。正常展开／滚动读正文，排除评论和推荐；发布时间省略年份时可只读同帖已加载时间元数据，核对帖子身份，区分创建和编辑。不要把 OpenCLI `nowcoder detail` 的文本截断输出当完整原文。

## 输出与失败

退出 `0` 表示读取完成（搜索可为空）；`1` 为平台／响应失败，立即停止平台访问并保留已取得材料；`2` 为参数或本地写入错误，不能算成功。成功响应中的空正文或纯图片帖属于单帖缺口，保留标题、来源、时间及图片标记，不计入有效面经、不重复请求，可在原预算内继续其他候选。其余停止规则见[采集子流程](find-interviews.md)，不以匿名 HTML 提示断定帖子永久不存在。
