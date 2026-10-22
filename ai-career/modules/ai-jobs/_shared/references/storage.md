# 共用数据目录、初始化与历史复用

三个技能共用一个数据根目录。根目录包含 `data/` 与 `reports/`，不是仅指 `data/` 子目录。安装包保存指令、公共来源清单与脚本；用户的关注范围、采集证据、历史观察和报告保存在数据根目录。整套安装时使用 `ai-career` 总包；单独安装的岗位与雷达模块随包携带相同存储助手，使用同一登记位置，无需先执行总入口。

## 每次调用先定位

涉及已有资料的分析、来源维护或采集保存时，先运行当前所用技能目录中的 `scripts/storage.py`：

```bash
python3 /path/to/installed-skill/scripts/storage.py resolve --workspace /absolute/current-workspace
```

`resolve` 只读，按以下顺序选择数据根目录：

1. 本次显式传入的 `--root`。
2. 环境变量 `AI_CAREER_DATA_ROOT`。
3. 当前 `--workspace` 已有的 `data/jobs.sqlite3`、`data/jobs-watchlist.json` 或 `data/radar/watchlist.json`；仅检查该目录，不向祖先目录或全盘搜索。
4. `${XDG_CONFIG_HOME:-~/.config}/ai-career/storage.json` 中登记的 `default_root`。
5. 新用户默认目录 `${XDG_DATA_HOME:-~/.local/share}/ai-career`。

`--workspace` 缺省为当前工作目录；`--config` 可显式指定配置文件。只解释技能用法且没有需要读取的历史库时，不为回答问题初始化空库。配置损坏或已登记根目录消失时，处理报告的具体问题，不静默创建另一份空库代替历史。

读取返回的 `root`、`selected_by`、`initialized`、`registered`，以及绝对路径字段：

- `paths`：`jobs_db`、`jobs_watchlist`、`jobs_observations`、`radar_watchlist`、`radar_runs`、`evidence`、`reports`。
- `baselines`：`jobs_observations`、`radar_catalog`、`radar_input`、`career_handoff`、`jobs_report`、`radar_report`；没有历史基线时为空，不补造上一轮路径。

后续使用返回路径，不从本轮聊天的工作目录猜测数据位置。给子技能或另一执行上下文传入已确定的绝对 `root`，子流程使用 `resolve --root /absolute/selected-root`，避免不同工作目录选中不同库。首次使用或选定目录改变时，向用户说明实际保存位置。

## 首次使用与接入已有库

任务需要建立或复用持久化资料，且选定目录尚未初始化或登记时，使用同一根目录执行：

```bash
python3 /path/to/installed-skill/scripts/storage.py init --root /absolute/selected-root
```

使用自定义配置路径时，`resolve` 和 `init` 传入同一个 `--config`。初始化只补缺失目录、账本与工作清单，并登记 `default_root`；再次运行不会清空已有记录、覆盖 watchlist 或推进采集基线。已有项目库原位接入，不复制到默认目录，也不重写旧观察及其证据引用。初始化成功后读取返回路径，确认使用的是预期数据根目录。

新用户的来源清单为空。按本轮目标从技能自带的公共 list 中选择来源，核实后增量启用；初始化不自动选择所有公司、抓取正文或建立定时任务。没有采集结果时，空账本和空清单只表示初始化完成。

默认结构如下；已有 watchlist 指定的账本与基线路径继续使用，以助手返回值为准：

```text
<root>/
├── data/
│   ├── jobs-watchlist.json
│   ├── jobs.sqlite3
│   ├── observations/
│   ├── job-runs/<run-id>/
│   ├── radar/
│   │   ├── watchlist.json
│   │   └── runs/<run-id>/
│   ├── career/state.json       # 需要保存个人进展时创建
│   └── evidence/<run-id>/
└── reports/
    └── career/<run-id>.md      # 个人计划与逐轮复盘
```

## 新会话如何复用

新会话重新执行 `resolve`。在没有已有项目库的工作目录中，读取登记的 `default_root` 即可找回之前的库；不依赖对话记忆或上次 shell 的当前目录。若当前项目已有库，按上述顺序使用项目库；需要指定另一份库时显式传入 `--root`。不同库不会自动合并。

定位后按本轮目标读取相关资料：

- 工作清单的 `last_run` 若引用提取纠错和纠正后的分析输入／目录，分析时一并读取并按稳定 ID 与原观察时间应用；原始账本或采集目录仍用于历史比较。读取更正结果不表示重新抓取来源，具体保存方式沿用对应模块的追踪文档。
- `ai-jobs`：读取 `paths.jobs_watchlist` 的范围、偏好和来源，使用 `paths.jobs_db` 查询岗位及历史。`baselines.jobs_observations` 是最近一批输入，不等于整个岗位历史。
- `ai-tech-radar`：读取 `paths.radar_watchlist`，以 `baselines.radar_catalog` 作为后续目录命令的 `--previous`。目录含之前保留的材料，不表示本轮全部重新读取；按任务需要读取原输入和证据。
- `ai-career`：读取所需分支的工作清单、基线与运行记录，沿稳定 ID 查证据；`career_handoff` 是雷达到总入口的交接产物，不是个人进度索引。保存计划或续接个人进展时，再读 `<root>/data/career/state.json` 及其相关计划／复盘引用，按[进展续接](progress.md)处理。只使用与本轮目标相关的资料，JD 关联仍按需进行。

个人索引和 `reports/career/` 由 Agent 在已解析的根目录下按需创建，存储助手的返回字段、初始化条件及原有历史路径保持原约定。旧库缺少索引不代表没有历史；采用用户明确关联的旧计划和产物，保留原文，不按修改时间自动选取报告，也不将历史中的示例画像当作当前用户。没有保存个人计划的任务不创建空索引。

存储助手负责定位、补缺和登记，不采集、不分析，也不推进基线。历史调用与数据读写分别遵循[岗位追踪](../../references/tracking.md)和[材料追踪](../modules/ai-tech-radar/references/tracking.md)。

## 路径与历史保留

传给脚本的账本、输入、输出与上一轮目录使用返回的绝对路径。保存到记录中的相对证据路径、watchlist 路径和报告路径一律相对于数据根目录；读取时也从该根目录解析，不相对于技能安装目录或本轮聊天目录。

每轮新建独立运行目录，保留原始 JSONL、必要正文和目录快照。岗位的新观察追加到同一账本；雷达用旧目录合并新观察并生成新快照。成功写入并回读后才更新 watchlist 的基线指针；失败、未复查或只扩充来源不会清空历史，也不冒充新观察。

推进 `last_run` 时，新运行记录继续引用仍匹配稳定 ID 与原观察时间的既有纠错；当前分析输入／视图基于本轮账本或目录应用这些纠错，不直接用旧分析快照替代新增结果。新来源观察不自动继承旧纠错。

备份或迁移须同时保留配置所指的整个库及记录引用的文件。旧观察引用 `tmp/` 或库外绝对路径时，继续保留相应证据；仅复制技能包不包含这些个人数据。改变默认根目录只是选择库，不会自动搬迁或合并已有历史。
