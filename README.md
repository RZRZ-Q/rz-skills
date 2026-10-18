# RZ Skills

从 AI 方向探索、学习与项目实践，到岗位选择和面试准备的 Agent Skills。

`ai-career` 是总体入口，按目标组合 `ai-jobs` 的招聘事实、`ai-tech-radar` 的工程与研究资料，以及可选的 `interview-collection` 面经和练习流程。也可以直接调用子技能处理单项任务。

**AI Career v0.1 Beta** 分发可复用流程、公共来源清单和本地存储脚本。个人画像、采集正文、历史库、测试材料、账号与认证信息不随包分发。

## Skill 目录

| Skill | 用来做什么 | 直接这样说 |
|---|---|---|
| [ai-career · 职业发展总入口](ai-career/SKILL.md) | 根据目标、能力和资源，整合方向选择、学习、项目与求职准备 | “我会 Python 和基础机器学习，未来 10 周怎么准备 Agent 方向？” |
| [ai-jobs · 岗位与 JD](ai-jobs/SKILL.md) | 查找实习／校招／社招，核对资格与状态，保留岗位观察历史 | “找 Agent 与评测岗位，比较不同公司的要求。” |
| [ai-tech-radar · 工程与研究追踪](ai-tech-radar/SKILL.md) | 跟进技术文章、公众号、论文与代码，分析工程方法和研究问题 | “跟进 Seed、混元、千问近期 Agent 研究，区分复现与科研候选。” |
| [interview-collection · 面经采集与整理](interview-collection/SKILL.md) | 搜索或读取面经，整理原题，追加飞书，生成岗位题库与本地学习页 | “找腾讯大模型算法面经，最多 5 篇，整理进飞书。”／“把已有题库做成按知识点学习的本地刷题页。” |

## 安装

在支持 Agent Skills 的工具里，把仓库链接与所需范围交给 Agent：

```text
从 https://github.com/RZRZ-Q/rz-skills 的 v0.1.0-beta.1 安装
ai-career、ai-jobs、ai-tech-radar，放在同一个 Skill 父目录；
如果我要面经采集和刷题，再安装 interview-collection。
```

**职业套件的三个目录需要一起安装**：它们共享存储助手和来源引用。安装后可以单独调用任何一个，不必每次执行全部流程。`interview-collection` 可以单独安装，也可作为套件的可选面试环节。

也可以下载 [Releases 发行包](https://github.com/RZRZ-Q/rz-skills/releases)，从解压后的仓库根目录执行。以支持项目级 `.agents/skills/` 的宿主为例，先把目标路径改为自己的项目：

```bash
mkdir -p /path/to/your-project/.agents/skills
cp -R ai-career ai-jobs ai-tech-radar /path/to/your-project/.agents/skills/
# 可选面经与刷题能力
cp -R interview-collection /path/to/your-project/.agents/skills/
```

安装前检查目标目录：已有同名 Skill 时先核对来源并备份，不直接覆盖其他作者的包。升级本仓库的旧版本时替换完整 Skill 目录，保留目录外的用户数据；不要把新文件叠加到来源不明的旧目录。复制整个目录，包括 `references/`、`scripts/` 和存在的 `agents/`、`assets/`，不要只拿 `SKILL.md`。其他宿主使用其实际配置的 Skill 目录。

安装后在目标项目开启新会话，确认宿主识别了这些 Skill。安装源码不会自动安装搜索工具、建立登录态或启动定时采集。Skill 本身不绑定模型。

## 推荐模型

使用 Codex 时，推荐以下两组配置：

| 模型 | 推理强度 | Fast |
|---|---|---|
| `gpt-6-luna` | `high` | 可开启 |
| `gpt-6.1-sol` | `medium` | 可开启 |

在 Codex 的模型设置中选择对应模型和推理强度，按需开启 Fast。本项目目前主要使用 `gpt-6.1-sol` + `medium` 进行实测；上述配置是使用建议，不是 Skill 的运行要求。

## AI 职业套件：从资料到个人行动

`ai-career` 按本轮目标选择流程：岗位需求由 `ai-jobs` 提供；工程实践和研究方向由 `ai-tech-radar` 提供；面试原题与练习由已安装的 `interview-collection` 提供。科研或项目学习可以直接开始，只有需要招聘匹配时才关联 JD。

```text
用 ai-jobs 找近期 Agent 实习和校招岗位，先限定字节、腾讯、阿里，每家最多两个可读 JD。
用 ai-tech-radar 跟进近一年的 Agent 评测论文和技术文章，说明实际读到了哪些部分。
用 ai-career 帮我选项目：会 Python、了解基础机器学习、没有完整 LLM 项目，
10 周、每周 10 小时、普通电脑与有限 API 预算。给出优先级、最小交付与验收标准。
用 ai-career 根据我的项目结果和面试反馈调整下一阶段计划。
```

岗位事实、作者报告的结果、分析判断和待实施建议分开记录。项目建议说明自己要做的改动、代码依据与能力证明；科研候选额外核查近邻、对照和实验预算。学习复现、工程项目和有待验证的科研贡献分开标明，不预测录用率或论文录用概率。

### 首次使用与数据保存

核心存储脚本使用 Python 3.9+ 标准库。联网采集需要宿主可用的搜索与网页读取能力；公开文本路线不要求账号。公众号正文导出是可选路线，需要 Node.js、[OpenCLI](https://github.com/jackwener/OpenCLI)、Browser Bridge 和已授权的 Chrome 会话；当前接口基线为 OpenCLI `1.8.8`。该脚本依赖 OpenCLI 的页面与微信读取模块，换版本后需检查接口及实际正文读取。缺少浏览器能力时可使用可读的官方博客或论文入口，并说明覆盖缺口。

第一次实际保存资料时，存储助手初始化空库并登记位置：

| 内容 | 默认位置 |
|---|---|
| 数据根目录登记表 | `${XDG_CONFIG_HOME:-~/.config}/ai-career/storage.json` |
| 用户资料根目录 | `${XDG_DATA_HOME:-~/.local/share}/ai-career` |
| 岗位、watchlist、原文与各轮快照 | 根目录下的 `data/` |
| 用户报告与建议 | 根目录下的 `reports/` |

新会话先定位库，再读取历史和基线。定位顺序为显式 `--root` → `AI_CAREER_DATA_ROOT` → 当前工作目录已有项目库 → 登记表 → 新用户默认目录。切换工作目录仍可复用登记库；已有项目库原位接入，不自动合并多个库。只解释用法且没有库时不创建数据。

岗位按稳定键保存观察历史；技术材料按稳定 ID 去重，同一工作的文章、论文、代码相互关联，保存各轮快照。成功写入并回读后才更新基线。升级 Skill 不覆盖用户库；备份时同时保留数据根目录和登记表。详见[共用存储](ai-career/references/storage.md)、[岗位追踪](ai-jobs/references/tracking.md)、[技术追踪](ai-tech-radar/references/tracking.md)。

### 固定来源与后续扩充

| 清单 | 已核实快照与口径 |
|---|---|
| [公司内团队清单](ai-career/references/team-inventory.md) | 2026-10-14：83 个主体、197 条分型实体；包含团队、项目、生态等类型，不全是实验室 |
| [岗位来源](ai-jobs/references/source-list.md)及行业分表 | 2026-10-14：79 家公司、2 家独立研究机构；156 个已确认入口、10 个候选入口 |
| [技术公众号](ai-tech-radar/references/wechat-sources.md) | 2026-10-16：43 条来源，40 条有官方关联或入口依据（含历史关系）、3 条候选；认证名称与当前可读性另列 |
| [工程与研究来源](ai-tech-radar/references/source-list.md) | 官方博客、团队目录、代码、arXiv 与 Hugging Face Papers 等入口，逐条保留归属与阅读边界 |

这些是可选择的公共来源，不是已采集正文数量、当前在招统计或默认全量监控。用户启用项单独保存在自己的 watchlist。可以说“把这家公司加入岗位来源”“增加这个 Lab 的论文入口”“暂停这个来源并保留历史”；按清单维护流程核实归属、入口和可读性、去重后更新，证据不足保留候选。新增来源不默认读取全部正文。定期执行由宿主调度，只有明确要求并实际创建成功才会启动。

Beta 的验证范围以[发行说明](https://github.com/RZRZ-Q/rz-skills/releases/tag/v0.1.0-beta.1)为准。已有真实材料验证不等于所有平台、账号和网络环境都可访问；默认库在当前设备本地，不提供跨设备同步。以下面经流程保留各自的环境与验证说明。

## 采集子流程：找到有依据的面经

给公司、岗位或技术方向，它会寻找实际面试经历，并核对正文中的岗位、日期和提问。也可以直接给帖子链接，跳过搜索。

```text
找字节跳动 Agent 算法岗面经，最多 5 个来源，不限时间。
只在知乎找腾讯推荐算法面经，最多 3 篇。
只在B站找算法岗实际面经，读取可用字幕，保留每题时间段。
读取这几个小红书链接，整理正文和图片里的实际问题。
```

未指定平台时默认牛客＋小红书；知乎和B站在明确指定时加入。“小红书公司”与“小红书来源平台”分别判断。数量按来源帖子计算，一个合集拆成多份经历时会另报面经记录数。

只找面经时，输出链接、匹配依据和少量代表题；要求整理时，继续进入内部整理流程，提取全部有依据的提问。招聘广告、求助帖、教程和准备题单不会当作实际面经。

→ [运行说明](interview-collection/references/find-interviews.md) · [牛客](interview-collection/references/nowcoder.md) · [小红书](interview-collection/references/xiaohongshu.md) · [知乎](interview-collection/references/zhihu.md) · [B站](interview-collection/references/bilibili.md)

## 整理子流程：保留原题，按岗位复习

输入已有面经文字、已读取的图文材料，或帖子链接。问题保留原句、轮次和出处；候选人反问、学习建议及问方不明的片段单独说明。

```text
把这段面经整理成 Markdown，保留原句和轮次，不补答案。
把这些面经追加到这个飞书多维表格：<目标链接>
用已有面经表生成大模型算法题库，同义题合并，保留来源公司和帖子。
更新已有推荐算法题库，只补新题和新来源。
```

输出分两层：

- **原始面经与题目**：Markdown 按经历和轮次整理；飞书用两张关联表，一份可辨认经历一条主记录，原题逐条关联。公司和岗位可筛选，原始称呼另存，外号、emoji 和同义岗位结合上下文归一。
- **岗位题库**：用户选择后，按已确认的岗位类别复用题库，细分岗位保留在“来源岗位”字段和视图中，避免按别名重复建表；Agent算法、应用开发、评测分别保留。题库包含标准问题、主题、变体与追问、来源公司、原题和面经关联，只在派生层合并同义问法，保留原始题目记录。

原题整理或入表完成后，会提示选择继续积累、生成／更新岗位题库，或生成学习包与本地刷题页；已有明确选择时直接执行。普通追加先按来源链接排重，不重复采集已入库帖子。

→ [运行说明](interview-collection/references/organize-interviews.md) · [公司与岗位归一](interview-collection/references/company-role.md) · [飞书两表](interview-collection/references/feishu-base.md) · [岗位题库](interview-collection/references/role-question-bank.md)

## 学习与刷题：把现有题目编排成学习包

输入 CSV、XLSX、JSON、NDJSON，或读取已有飞书题库，按知识点编排学习目标、实践任务和自查标准，生成 `pack.json`、`题目.csv`、`学习包.md` 与 `index.html`。Markdown、PDF 和图片先由 Agent 审读，再整理成题目输入；只读到的材料才作为依据。飞书路线只读导出已有题目及关联原题，不新建表，也不回写练习进度。

```text
把这个 CSV 题库按知识点编排，生成能在本地打开的刷题页。
读取这个 XLSX 的“算法题”工作表，保留已有答案，没有答案的题留空。
用这个飞书岗位题库生成学习包，保留每道题的关联原题和来源依据。
用更新后的题目重新生成学习页，保留原学习包 ID 和题目 ID，让旧笔记能恢复。
```

页面支持专题、搜索与难度筛选、收藏、复习状态、作答和笔记；参考默认收起，也可选择“暂不会，查看参考”。缺少答案时可以正常练习，不自动补答案或扩题。题目显示原句、来源位置、链接和核验状态，多条来源分别保留。

更新时沿用稳定的学习包 ID 和题目 ID，保留旧作答与笔记；新增题从未练开始，移出题库的旧记录仍保留并可导出。题面或参考变化会将已掌握题目改为需复习，仅增加来源不触发降级。进度可导出／导入 JSON；同 ID 导入记录覆盖本题当前进度，未提供的题目保持不变。更换浏览器或移动 HTML 文件可能隔离本地存储，更新前先导出备份。

→ [学习流程、输入字段与更新说明](interview-collection/references/study-pack.md)

## 首次使用与环境准备

| 你要做的事 | 需要的环境 |
|---|---|
| 整理已有文字 | 宿主可以读取文本；涉及图片时需要读图能力 |
| 生成本地学习包 | Python 3.9+；CSV／JSON／NDJSON 使用标准库，XLSX 导入需可选 `openpyxl`；成品 HTML 只需浏览器 |
| 读取牛客文本 | Python 3.9+，随包脚本只使用标准库 |
| 读取小红书、知乎或B站字幕 | 已配置的 [OpenCLI](https://github.com/jackwener/OpenCLI) 与 Browser Bridge，以及用户已登录的 Chrome 会话；小红书图片下载另需 Python 3.9+ |
| 读取或写入飞书 | 已配置的 [lark-cli](https://github.com/larksuite/cli)、`lark-base` 和 `lark-shared` Skill，以及本轮目标的读取或写入权限 |

随包 `scripts/setup_environment.py` 默认运行只读 `check`，按 `local`、`nowcoder`、`browser`、`feishu`、`excel`、`pdf` 选择本轮依赖。明确选择并授权安装后，`install --features ... --runtime ...` 只向指定项目目录补齐缺失的 OpenCLI 或 Python 可选包，复用可用的已有工具，不升级全局环境。Python、Node.js、Chrome／Bridge、飞书交互安装和账号授权按报告中的步骤完成，详见[环境准备](interview-collection/references/environment.md)。本地文件学习不要求平台登录。

首次使用会先检查本轮所需环境，指导缺失工具的安装、浏览器连接与飞书授权，完成后复检；不会假定安装 Skill 就等于依赖已齐全。随后集中询问缺失的公司／岗位、平台、数量、输出目标等条件，说明各平台当前并行度与验证范围，让用户选择是否调整，并在确认方案后开始。已明确的条件与授权不重复询问，具体见[首次引导](interview-collection/references/onboarding.md)。

飞书是可选输出，普通 Markdown 整理不需要飞书工具；已选择飞书时指导补齐依赖，不擅自改成交付 Markdown。外部工具的安装与登录按官方说明完成，本仓库不包含认证信息或浏览器安装包。

初次试用可以只说：“我第一次使用这个 Skill，想收集一些面经并整理到飞书，请引导我开始。”

浏览器路线以官方 OpenCLI `1.8.8` 为当前接口基线，不依赖定制 CLI 或 Bridge。执行前核对本轮工具参数和实际读取能力；版本与连接检查不能代替平台访问验证。

B站默认串行，读取简介及可用字幕，按分 P 保留来源与时间戳。特定导航拒绝的临时 trace 兼容方式及单次页面核验见[B站说明](interview-collection/references/bilibili.md)。没有字幕时明确缺口，不默认下载音视频或调用外部转写；可读字幕也不等于已经审看视频画面。

## 来源与临时材料

每题保留来源链接、原句和已核对的位置。缺失岗位、日期或未读图片按实际情况说明，不补猜。OpenCLI 浏览器命令默认后台；真实登录要求、验证码或明确访问限制出现时停止，具体有界恢复条件见各平台说明。

完成原文复核、飞书入库与回读后，默认删除本批采集的图片、截图和图片副本，保留来源链接与文字摘录。后续复审重新打开来源链接；未完成批次暂存所需图片，用户原始文件或明确要求保留的图片不自动删除。

带访问参数的链接、账号配置、私人飞书表格、采集正文与图片不提交到代码仓库。提交问题或改进建议时，提供去除身份信息的最小示例即可。

## 验证范围

牛客文本、小红书图文、知乎文章和 B站视频 P1 均有搜索、读取、原题整理、飞书追加及回读的真实证据；知乎具体回答也有读取与整理入表证据。平台验证来自不同工具版本，小红书／知乎旧版本结果不替代官方新版的完整验收。B站当前使用上述临时兼容方式，不能视为导航问题已根治或长期稳定。

首次引导、新建飞书两表、岗位题库创建及追加已有交互验证；新来源与旧题的语义合并、来源关联与写后回读已完成业务验证。从文件或飞书题库生成学习包、CSV 往返、浏览器交互和更新后的进度恢复已验证。学习页浏览器检查使用本地 HTTP，直接双击 HTML 尚未验收。

全新机器配置、更高并发与长期访问、人工编辑冲突恢复仍待验证。原文审读与必要纠正是交付流程的一部分；生成器测试不替代参考答案的技术核验。

## 仓库结构

```text
ai-career/                      # 总入口、共享存储、公司与团队事实表
ai-jobs/                        # JD 采集与岗位账本
ai-tech-radar/                  # 工程／研究追踪与材料目录
interview-collection/
  SKILL.md                       # 唯一安装入口
  references/
    find-interviews.md           # 采集子流程
    organize-interviews.md       # 整理子流程
    study-pack.md                # 学习与刷题流程
    environment.md               # 按功能检查与局部安装
    ...                          # 平台、飞书和题库说明
  scripts/
    setup_environment.py
    study_pack.py
    ...
  assets/
    study.html                   # 无题目数据的本地页面模板
README.md
LICENSE
```

新增 Skill 按相同方式使用独立目录，并在首页目录中添加用途和安装入口。各 Skill 的运行规则维护在自己的 `SKILL.md` 和引用文件中。

## 许可

源码采用 [Apache-2.0](LICENSE)。平台、外部工具、岗位正文、技术文章、论文和原始面经内容的授权不由本仓库许可证覆盖。公共来源清单只提供入口及事实说明，不随包再分发采集原文。
