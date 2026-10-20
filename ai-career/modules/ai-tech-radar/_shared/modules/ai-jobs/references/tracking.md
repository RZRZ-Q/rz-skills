# 岗位记录、比较与持续追踪

## 数据目录与身份

先按[共用数据目录](../../../references/storage.md)运行存储助手 `resolve`，已有根目录显式传入 `--root`；需要初始化或登记时在该根目录执行 `init`。读取 `paths.jobs_watchlist` 与 `paths.jobs_db` 后再规划采集，先查已有岗位键与成功观察，不因换会话、公司标题变化或工作目录变化另建库。

下文的 `data/`、`reports/` 和记录中的相对证据路径均相对于选定数据根目录，技能脚本路径相对于技能安装位置。默认使用 `data/observations/` 放各次规范化 JSONL、`data/imports/` 放原始材料、`data/jobs.sqlite3` 放本地账本、`reports/` 放交付报告；实际账本与基线使用助手返回路径。个人画像放独立私有文件，不写进 JD 或公开仓库。

新轮次将正式观察所引用的必要正文、状态证据和访问记录保存到 `data/evidence/<run-id>/`；临时下载与解析中间件仍放 `tmp/<run-id>/`。先确定证据路径，再入库。已有不可变观察若引用 `tmp/`，保留对应文件，不为搬目录重写历史观察；迁移时另存路径映射并保留原有定位。备份须包含账本、JSONL、watchlist 与被引用的证据，复制技能包不等于备份数据。

优先主键 `招聘站域名:岗位ID`；站点 ID 在不同招聘渠道／届别下复用时，主键再加入已确认的渠道／届别命名空间。无 ID 时用保留岗位定位参数的规范详情 URL，去除已确认的跟踪参数。不要删除 `positionId`、`jobId` 等身份参数。转载指向同一官方 ID 的，复用身份并保留出处；未能确认同岗关系的先分开，不凭标题强合并。首次保存后沿用键；标题变化不生成新岗位。

## JSONL 观察记录

每行一个完整观察对象。必填：

| 字段 | 含义 |
|---|---|
| `job_key`, `company`, `title` | 稳定身份、公司名称、来源标题 |
| `recruitment_type` | `internship` / `campus` / `experienced` / `unknown`，指招聘渠道 |
| `source_url`, `source_kind` | HTTP(S) 来源链接；`official` / `third_party` / `user_document`，指本次实际读到的来源 |
| `observed_at` | 来源观察时间：带时区 ISO8601 或只有日期的 `YYYY-MM-DD` |
| `verification`, `status` | `live` / `historical`；`open` / `closed` / `unknown` |
| `requirements` | 数组，条目含原句 `text`、`kind`、`skill_tags` 字符串数组 |

`kind` 为 `must` / `preferred` / `responsibility` / `unspecified`。条目可增加 `source_ref`、原始逻辑说明等字段。不要删掉无法分类的原句。

按来源增加门户身份 `source_id`、`source_job_id`、`locations`、`hiring_cycle`、`candidate_stage_raw`、`education_raw`、`experience_raw`、`application_deadline`、`company_tier`、`company_tier_basis`、`role_family`、`salary`、`source_published_at`、`source_updated_at`、`source_ref`、`source_refs`、`raw_text`、`notes`。`company_tier` 使用 `large/mid/small/unknown`；地区、规模、届别没有证据时不补造。`role_family` 是分析分类，可说明依据。已有观察没有 `source_id` 时可在运行记录或 watchlist 关联，不为补字段改写历史。

附件包含官方链接时，`source_url` 可存该岗位链接，但 `source_kind` 仍是 `user_document`，`source_ref` 指向真正读取的本地附件与位置。纯文本附件没有链接时，在扩展字段保存文件出处，先作为待补来源材料，**不要编造 HTTP 链接满足账本字段**；可直接分析，找到真实链接后再进入本账本。

历史材料 `verification=historical` 必须 `status=unknown`。`observed_at` 使用材料的历史整理／观察日期，在 `notes` 说明时间精度；没有可知历史日期时先留在导入材料区，不将今天伪装为历史观察日。导入时间可另存扩展字段。日期仅用于排序，不意味着那天零点实际核验过。

`open/closed` 需要 `status_evidence` 原文或明确页面行为。重新访问失败写本轮运行记录，不能用空正文覆盖旧 JD。最新状态与最近一次成功观察分开叙述；很久没复查的 `open` 不能称今天仍在招。

## 标准库账本命令

将下面的技能路径替换成实际安装路径，`/absolute/selected-root` 替换为助手返回的数据根目录，`--db` 使用返回的 `paths.jobs_db`。脚本接收绝对路径，不依赖调用时的当前目录。

```bash
python3 /path/to/ai-jobs/scripts/job_ledger.py ingest --db /absolute/selected-root/data/jobs.sqlite3 --input /absolute/selected-root/data/observations/batch.jsonl
python3 /path/to/ai-jobs/scripts/job_ledger.py list --db /absolute/selected-root/data/jobs.sqlite3
python3 /path/to/ai-jobs/scripts/job_ledger.py list --db /absolute/selected-root/data/jobs.sqlite3 --as-of 2026-09-07
python3 /path/to/ai-jobs/scripts/job_ledger.py diff --db /absolute/selected-root/data/jobs.sqlite3 --before 2026-09-07 --after 2026-10-13
```

脚本只做存储与比较，不联网。观察按 `job_key + UTC 观察时间` 幂等；同一键／时间的不同内容会报冲突并回滚整批。新增版本使用真实的新观察时间，纠错不能伪造后续观察或删除旧证据。原始材料读错需要纠正时另存纠错说明，明确统计采用哪份记录。

`list` 取各岗位截至指定时刻的最近观察；日期截止包含 UTC 整天，精确时点用带时区 ISO8601。乱序导入不会覆盖更新的观察。`diff` 比较标题、地点、招聘渠道、届别、候选阶段、学历／经验、截止日期、方向、要求、薪资、状态；要求条目比较原句、类别和技能标签，原文位置和采集时间变化不算需求变化。集合中没有再次出现的岗位保留旧状态，不自动关闭。

`added_to_sample` 只表示第一次进入所选样本，不等于最近新发布或新增 HC。要求增删仍需读取差异上下文，判断是措辞变化、真正能力变化还是提取格式变化；脚本不是语义裁判。

## 来源清单与扩充

[官方入口清单](source-list.md)随技能分发，只保存公共入口及核验边界。助手返回的 `paths.jobs_watchlist`（默认 `data/jobs-watchlist.json`）保存本人的范围、启用来源和跟踪岗位；技能升级不覆盖它。新用户初始化的来源为空，按本轮目标选用公共 list，不自动启用全部入口。招聘门户或有实际招募内容的独立团队入口使用稳定 `source_id`，公司别名合并到同一主体；校园与社招门户可有不同 ID，具体职位仍使用 `job_key`。

watchlist 的 `sources` 每项保存 `source_id/company/url/channels/state/ownership_evidence/selection_reason`；渠道使用 `internship/campus/experienced/unknown`。`state` 为 `candidate/active/paused/retired`，是用户清单中的选用状态，不能与岗位的 `open/closed/unknown` 混用。固定清单中未选用的入口无需全部复制。已有 `tracked_jobs` 继续保存具体岗位，不能代替来源列表。

扩充中小厂、创业公司时，可用 `source_group` 标明本轮的业务分组；它不代替有依据的 `company_tier`。例如专注数据库或 Agent 产品的公司不自动等于人数少，公司被收购或招聘主体变化时保留新旧主体与官方依据。招聘 SaaS 的域名不能单独证明归属，应由官网招聘链接、认证主体或官方互链确认。

公司官网反链不是团队归属的唯一证明。公司官方JD中的团队名、团队官网与开源组织／模型页互链、项目版权与发布主体、论文作者机构、公司正式公告等，可结合起来确认团队关系；单独邮箱、同名页面或第三方转载不足时，写清尚缺的证据。分别记录团队归属、招聘入口用途、正文可读性、具体岗位在招状态，不因缺少独立招聘站而漏掉已确认的研究团队，也不因论文署名已核就声称当前有招聘。

团队与行业扩充另保留这些关系：

- `company` 沿用所属组织的统一名称，`team` 记录 Seed、混元、研究院等团队；独立研究机构用 `organization_type=research_institute`，公司用 `company`。团队数量、企业数量和来源数量分别统计。
- `entry_kind` 区分 `recruiting_portal`、`team_recruiting_hub` 和 `research_recruiting_hub`。有实际招聘说明、岗位导航或投递联系方式的团队页可以纳入；单纯论文／产品介绍页保留为发现线索或交给技术雷达，不当作招聘来源。已有集团门户可用 `parent_source_id` 关联；同一门户的项目、城市、部门筛选保存在 `related_channel_urls` 或查询提示，不按筛选条件增加来源。已有分别编号的校园／社招门户不为统一格式重编号。
- 已确认团队没有独立招聘入口时，在现有父来源的 `team_queries` 中保存团队名／别名、归属依据、查询词、研究／代码入口及招聘待核项。团队仍纳入跟踪，但不为同一父门户重复建来源ID。团队招聘页有自己的招募说明时可另建hub并关联父源；团队之间的别名、改名或隶属关系需要依据，不能仅凭研究方向或职责相似就合并。
- `sector`／`role_keywords` 是采集分组和检索提示，不能当作已证实的 JD 要求。具身模型、仿真评测、控制算法、嵌入式和机械电气岗位分别看；芯片公司中的 AI 软件、编译器／Kernel、RTL／验证、物理设计、模拟电路也分别看。
- 全球研究团队和芯片招聘站记录 `region_scope`：全球目录不能自动计作中国大陆机会。Researcher、Fellow、Resident、Student Researcher 与国内校招／实习不机械等同；没有明确渠道时保留 `unknown` 和来源原词。已核实的官网历史招聘页仍可作为来源，但旧 JD 日期不能证明当前在招。

- **新增**：用户说“加入某公司／方向”时，直接在已授权范围内核实官方归属、目录用途和可访问渠道；核实完成即加入 `active`，无需再确认。未知归属的入口先记 `candidate`，附发现线索与待核实项；搜索摘要不算核实完成。记录官方互链或认证主体的证据 URL，以及入口实际读取的时间／结果。动态目录只能确认归属时，明确记录正文读取限制，不声称 JD 已采到。
- **去重与替换**：先按公司别名、门户及规范 URL 查重，保留岗位定位参数。官方迁移入口时沿用来源 ID 并保留旧 URL、变更日期及原因；新增独立门户用新 ID。
- **暂停与恢复**：用户暂停用 `paused`，恢复后继续同一来源；确认已退役才用 `retired`，保存官方证据和替代入口。访问失败只更新访问记录，不自动暂停来源、删除岗位或宣告关闭。
- **范围内发现**：按本轮范围与总预算安排新来源核验，费用和读取量计入总预算；固定公司请求只补该公司的遗漏门户／渠道。超出用户范围的公司可留候选线索，不自行启用。日常新增写用户清单；只有用户要求维护公共固定 list 时才修改技能内清单。新增来源引起的样本扩大不能解释为招聘增长。

批量扩充按本轮范围逐项核验。写入前按 ID／别名／门户去重，增量合并并保留已有暂停项和偏好；写入后回读确认，重复合并相同条目不新增来源。运行记录列出新增、补充、仍待核候选与未变更项。记录入口实际可读层级；任务包含岗位采集或详情可读性核验时，再读取真实 JD。只有完整正文才进入岗位账本，不能把新入口计成新增岗位。

系统盘点时，按本轮公司／行业范围建立逐公司覆盖表，再沿官方研究目录、公司 JD、团队站、GitHub／HF 和论文机构发现团队。每个主体保留本轮查询、发现团队、已核入口、访问失败与待补项；“未找到”只能描述本轮覆盖，不能写成不存在。模型／产品／工程项目使用明确的 `entity_kind`，不冒充独立 Lab；联合实验室保留合作方与归属边界。已有集团官网不等于该公司的团队发现已经完成。

用户授权新增公司或行业时，若清单另有 `scope.companies`，同时增量补入本次新启用的公司；独立研究机构使用 `scope.research_institutes`，团队不另加公司。仅候选或暂停项不自动扩入启用范围。保留旧成员以及未被本次请求改变的地区、方向、预算与调度偏好。回读时核对本轮新启用主体与范围一致，重复执行不增加重复名称。

若本轮只要求公司／来源盘点，逐公司保留三渠道的已核、候选与未核项；不为凑完整覆盖而用 ATS 模板枚举推断渠道开放。来源清单更新只推进 `last_source_expansion` 与 `source_inventory_report`，没有新岗位观察时保持原 `baseline_observations`、`last_run` 和采集报告不变。

读取结果至少区分目录、职位列表与详情，保存实际方式。阅读器报加载失败但已授权浏览器成功时，保留两次结果，采用最新成功正文；不删失败证据，也不反过来称阅读器已跑通。没有独立详情 URL 的抽屉岗位，保存观察到的稳定区分参数或官方投递链接及定位方式，不凭空构造 ID。

还可在 watchlist 保存 `scope`（地区、主题／查询词、公司分组依据）、预算、输出路径、基线与调度状态。它是 Agent 每轮读取的任务配置，不是爬虫配置接口。

## 每轮复查与交接

定位数据根目录后读取最新 watchlist 与账本，沿用来源 ID、岗位键、暂停项和偏好。`baselines.jobs_observations` 只指最近一批观察；去重、历史比较和已有岗位查询使用完整账本。根据本轮目标和已有工作清单预算分配复查与新岗位发现名额，记录实际覆盖和未完成项。复查优先本轮准备投递、临近截止、状态待确认及最久未成功检查的岗位，其他岗位轮换；原 `open` 只表示最后核验日状态，实际投递前重新确认。

每轮在 `data/job-runs/<run-id>/run.json` 或已有正式运行目录记录：本轮范围／预算、前一基线、实际尝试的 `source_id`／URL／时间／读取方式／结果／证据路径、成功获取的 `job_key`、失败与未检查的公司×渠道、输出位置。空结果、读取失败、预算未检查分别记录。每个来源保留 `last_attempt_at/last_success_at/last_result`，没有成功访问就保持成功时间未知。

有效观察入库并回读确认后，才将 watchlist 的 `last_run`、`baseline_observations` 和报告路径指向本轮；入库失败不推进基线。写回前重读 watchlist，增量合并本轮变更，保留未受影响的范围和来源。部分来源失败时可保存其他成功观察，但运行记录标明不完整，未复查岗位保持上次成功观察。基线仅用于衔接本轮，历史比较仍读取完整账本。交接同时传递数据根目录绝对路径、账本路径、本轮输入和报告位置。比较优先相同来源／渠道／查询规则的范围，单列新来源贡献和覆盖缺口。

用户要求定期自动追踪时，使用当前宿主实际支持的自动化工具，保存 watchlist 路径、技能与账本路径、执行频率、采集预算和变更摘要要求。默认仅在有相关新机会、关键要求变化、明确关闭或需要用户处理的故障时通知；无变化保持安静。避免重复建相同任务。缺少执行器则说明目前支持手动复查，不能把保存配置说成自动运行；缺少必需周期等信息时只询问该缺口。
