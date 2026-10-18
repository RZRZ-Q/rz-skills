# 材料目录与重复追踪

先按[共用数据目录](../../ai-career/references/storage.md)运行存储助手 `resolve`，已有根目录显式传入 `--root`；需要初始化或登记时在该根目录执行 `init`。读取 `paths.radar_watchlist` 与 `baselines.radar_catalog` 后规划采集，先对照已有材料 ID、工作 ID 和来源，不因换会话或当前目录变化另建目录。

每轮规范材料用 JSONL 保存到选定数据根目录，如 `data/radar/runs/<run-id>/engineering.jsonl` 与 `research.jsonl`。下文的相对路径及记录中的 `source_ref` 都从该根目录解析。保留每轮原输入、正文证据和目录快照，生成新快照时不覆盖旧快照；最新目录只保留每份材料的最新视图，不能单靠它保存全部历史版本。

## 单条材料

必需字段：

| 字段 | 用途 |
|---|---|
| `material_id`, `work_id` | 稳定材料身份与独立工作身份；跨语言／载体版本保留同工作关系，固定论文版本或代码 commit 的材料可用带版本的 ID |
| `title`, `url`, `source_type` | 原始标题、规范 HTTP(S) 来源与类型：`engineering_blog/research_blog/paper/repository` |
| `company`, `team`, `authors` | 原文可支持的组织与作者；未知 team 用 null，未知作者用空数组 |
| `published_at`, `retrieved_at` | 来源发布日期（未知用 null）与本轮实际获取时间（带时区 ISO8601） |
| `topics`, `modes` | 主题标签和 `engineering/research` 分析模式，可同时包含两种 |
| `content_scope`, `source_ref` | `full_text/partial/abstract` 与本地正文证据路径；另用 `read_scope` 写实际读过的章节 |
| `summary`, `evidence` | 自己的总结；证据数组中的 `claim/excerpt/locator/kind`，kind 区分 `method/reported_result/constraint/limitation` |
| `related_urls`, `job_links` | 原文关联论文／代码；可选岗位关系数组含 `job_key/requirement_excerpt/source_ref/relationship` |

没有岗位关联时 `job_links=[]`，独立学习不要求 JD。可以扩展 `source_id`（发现入口）、`affiliation_evidence`、`reading_notes` 等字段。定位指章节、段落、表或源码位置，短引文只支持对应结论，不用全文替代分析。`full_text` 表示可用正文范围；真正读过的部分由 `read_scope` 说明，不把下载全文写成全文精读。

材料引用了本轮已核验的代码时，在 `code_checks` 数组中传回每个入口的 `repo/ref/path/source_ref/checked_at/scope`，可附 `symbol/lines/purpose`；`source_ref` 指向实际读取的本地源码。只读了 README 就把 scope 写清楚，未运行不写成已跑通。仅发现仓库链接时保留在 `related_urls`，不填写已核验记录。代码本身已作为独立材料且携带固定版本与源码路径时，不要求重复记录。

## 生成可比较目录

将技能路径替换成实际安装位置，输入和输出使用数据根目录下的绝对路径。首次没有基线时：

```bash
python3 /path/to/ai-tech-radar/scripts/catalog.py \
  --input /absolute/selected-root/data/radar/runs/current/engineering.jsonl /absolute/selected-root/data/radar/runs/current/research.jsonl \
  --output /absolute/selected-root/data/radar/runs/current/catalog.json
```

后续轮次使用新的运行目录，并把助手返回的 `baselines.radar_catalog` 绝对路径传入 `--previous`；已有基线时不能省略它，否则无法保留先前未在本轮输入中的材料。脚本保留之前材料，只更新较新的观察，并输出本次新发现材料、首次进入目录的独立工作、元数据变化与本轮未复查项。同一工作多载体按 `work_id` 聚合。重复导入不增加材料数，身份冲突明确报错。只有比上次 `last_seen_at` 更新的真实观察才算复查，重放旧文件仍列为未复查。

脚本只汇总已经读到的材料，不联网，不判断论文创新或团队热度；“新发现”是首次进入本目录，不等于刚发表。“本轮未复查”不等于撤稿或删除。原文改动与分析标签变化需查看原始材料后判断，不能从目录差异推断科研方向转变。

## 来源清单与扩充

[固定来源清单](source-list.md)随技能分发，保存公共入口与核验边界；助手返回的 `paths.radar_watchlist`（默认 `data/radar/watchlist.json`）保存用户实际关注范围，升级技能不覆盖用户选择。新用户初始化的来源为空，按本轮目标选用公共 list，不自动启用全部入口。一个独立目录／订阅／仓库一个稳定 `source_id`；同公司可有多个团队来源，英文／中文镜像若属同一目录则保存为别名。材料仍用 `material_id/work_id`，不能拿来源数量代替独立工作数。

watchlist 的 `sources` 每项保存 `source_id/company/team/url/modes/role/state/ownership_evidence/selection_reason`。`role` 区分 `directory/repository/discovery/work_anchor/account`，`state` 为 `candidate/active/paused/retired`。不清楚归属的团队用 null；订阅地址仅在官方实际提供时填写，不猜 `/rss.xml`。

公众号使用 `role=account`，另保存 `account_identity`（已核实的账号名、微信号或 `__biz`）、`identity_status` 与归属证据；平台认证主体没读到就留未知，官方互链不能表述为已见到平台认证。仅有示例文章时标明 `entry_kind=article_anchor`，历史目录 `history_url` 留空，不把短链当作账号完整历史入口。微信号、`__biz` 和内部 `source_id` 各自保留，不凭显示名合并同名账号。

已确认同号的旧名称或索引名称保存在 `aliases`，并用 `account_identity.name_observations` 区分当前显示、历史官方名称与搜索索引名称，附对应证据和观察日期。未确认的名称关系放 `pending_identity_relations`，不混入已核 aliases；不同账号保留独立 ID。历史官方关联、当前页面标识和平台认证各自记录，更名生效日期没有证据就留未知。

身份核验结果按 `source_id` 分别生成 `identity_page_result`，保存该入口的 `source_ref/checked_at/result/scope`。账号名称、归属与日期从对应证据填写，批量更新时只复用字段结构，不共用包含账号事实的说明。写回后逐项对照“来源 ID → 身份入口 → 证据 → 说明”；旧说明与本次证据不符时据实更正，未核实的事实不从其他来源补齐。

公众号原文的 `article_probes` 与官方替代目录的访问记录分别保存 URL／时间／读取方式／结果／证据；替代目录作为独立来源，通过 `official_mirror_source_id` 关联，也可补 `mirror_probes`。该关系不保证每篇文章相同。原链受阻时仍可启用已确认官方归属的来源，但显示访问限制；替代目录读取成功不更新微信原链的成功时间。确认同篇作品需有官方互链或明确原文关系，仅标题相似不足以合并 `work_id`。只读官方社区的材料 `url/source_ref` 指向实际读取页，已发现的原链作为线索保存。

- 用户指定新公司、公众号、Lab 或仓库时，核实官方／作者归属、入口用途和实际可读范围后加入 `active`，不重复要求批准。无法核实的来源作为 `candidate`，保留线索与缺口；记录入口检查时间、方式和结果，入口可用不等于全部内容已读。
- 新增前按组织、团队、规范 URL 与官方互链去重。官方换入口保留同一 ID、旧 URL、变更日期与依据。`paused` 用于用户暂停；有官方退役依据才设 `retired`。一次失败只记访问结果，不删来源和历史作品。
- 按本轮范围与总预算安排新来源核验；固定团队任务只发现其新目录或合作线索，跨团队候选不自行启用。日常扩充写工作目录；用户要求更新公共固定 list 时才修改技能包。BlogrXiv 等发现入口返回原站核验，不整体导入后宣称已阅读。

批量扩充按本轮范围逐项核验。将核实后的新来源增量合并到 watchlist，保留旧状态／偏好；回读并核对 ID，重复合并不产生第二份来源。保留候选到启用的证据和仍待核实的原因，记录入口实际可读层级；任务包含材料采集或正文可读性核验时，再读取真实文章，有足够正文才加入材料目录。来源扩充报告分别计算账号确认数、原链可读数、镜像可读数与实际新增材料数。

系统盘点时，以本轮公司／行业清单逐家查团队目录、研究站、官方代码／模型组织和论文机构；已有公司博客不能替代公司内专项研究组发现。保留公司级缺口，区分真实团队、联合 Lab、研究项目与工程生态；一个项目名不自动证明独立组织。招聘入口交给 ai-jobs 承接，研究身份不因缺少独立招聘站而排除。

运行预算分别考虑旧来源检查、新作品深读和新来源核实；“新增最多 N 篇”不是可以不计时间地检查所有历史材料。优先用户目标、最久未检查的相关来源及上轮缺口，其他来源轮换；本轮跳过的来源明确列出。新增团队或扩大关键词引起的作品数变化，不能直接写成团队研究热度上升。

只做公司／来源盘点时，分别记录工程目录、研究目录、Lab 简介与公众号身份。未找到也保留公司缺口；网站周刊不冒充公众号，Lab 简介不冒充论文目录。没有新材料时只推进 `last_source_expansion` 与 `source_inventory_report`，保持材料 `baseline`、`last_run` 和采集报告不变。

## 每轮基线与交接

在 `data/radar/runs/<run-id>/run.json` 或已有正式目录保存本轮主题／时间窗口、前一基线、实际访问的 `source_id`／URL／时间／方式／结果／证据路径、阅读边界、输出位置和未检查范围。空结果、失败、预算未检查分别记录；来源保留 `last_attempt_at/last_success_at/last_result`，未知成功时间不补造。

材料采集轮次按以下顺序交接：

1. 先确定本轮实际使用的 JD 输入，在运行记录中写 `job_context`；未使用 JD 则明确为 `[]`，不沿用上一轮输入。已有快照中的历史岗位关联保留。
2. 用 watchlist 的最新有效目录作为 `--previous`，生成新快照并核对材料数、工作数、本轮变化与 `not_rechecked`。失败不推进指针；部分来源失败可形成包含旧材料的新目录，但须明确缺口。
3. 成功后重读 watchlist，增量合并并一起写回本轮 `baseline`、`baseline_input`、`last_run`、报告路径和 `job_context`，保留未受影响的范围与来源。上下文使用运行记录的本轮值，不能因空数组而跳过写入。来源维护沿用上述按 `source_id` 的更新与证据回读。
4. 回读已保存的 watchlist：目录／输入／报告指向同一轮，`job_context` 与本轮实际使用的输入一致，受影响来源的身份说明、访问结果与成功时间各有对应证据；未检查来源保留原状态。向 `ai-career` 传递同一数据根目录绝对路径、材料目录、运行记录及交接文件。

旧快照不覆盖、不丢弃，重放旧材料不更新检索时间。仅来源扩充仍按上一节保留材料基线与本轮材料上下文，不借来源维护重写历史采集记录。

watchlist 保存主题、来源、时间范围、数量／时间预算、输出路径与上述基线，供下轮 Agent 读取；它不是常驻抓取器配置。

用户要求定期运行时，通过宿主已有调度工具安排来源复查与目录比较；由 `ai-career` 发起时由总入口统一安排。只在相关新工作、值得行动的方法变化或需要处理的故障时通知，无变化保持安静。未实际建立调度时明确为手动可重复流程。
