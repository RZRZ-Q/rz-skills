# RZ Skills

一个持续更新的 Agent Skills 集合，收录可复用的任务流程与工具能力。

目前主要提供 **AI Career** 套件，覆盖 AI 方向探索、学习与项目实践、岗位选择和面试准备；后续会陆续加入其他领域的 Skill。

## Skill 目录

| Skill | 用来做什么 | 直接这样说 |
|---|---|---|
| [ai-career · 职业发展总入口](ai-career/SKILL.md) | 根据目标和能力证据安排项目，梳理成果主张，并续接真实进展 | “先看我的代码和运行结果，判断下一步；哪些成果能用于面试？” |
| [ai-jobs · 岗位与 JD](ai-career/modules/ai-jobs/SKILL.md) | 查找实习／校招／社招，核对资格与状态，保留岗位观察历史 | “找 Agent 与评测岗位，比较不同公司的要求。” |
| [ai-tech-radar · 工程与研究追踪](ai-career/modules/ai-tech-radar/SKILL.md) | 跟进技术文章、公众号、论文与代码，分析工程方法和研究问题 | “跟进 Seed、混元、千问近期 Agent 研究，区分复现与科研候选。” |
| [interview-collection · 面经采集与整理](ai-career/modules/interview-collection/SKILL.md) | 搜索或读取面经，整理原题，追加飞书，生成岗位题库与本地学习页 | “找腾讯大模型算法面经，最多 5 篇，整理进飞书。”／“把已有题库做成按知识点学习的本地刷题页。” |

## 安装

当前版本：[v0.1.0-beta.5](https://github.com/RZRZ-Q/rz-skills/releases/tag/v0.1.0-beta.5)。可以安装整套 AI Career，也可以只装需要的模块：

| 安装范围 | 仓库路径 | 安装后的入口 |
|---|---|---|
| 整套职业能力 | `ai-career` | `ai-career/SKILL.md`，按需读取内含三个模块 |
| 仅岗位／JD | `ai-career/modules/ai-jobs` | `ai-jobs/SKILL.md` |
| 仅工程实践／研究追踪 | `ai-career/modules/ai-tech-radar` | `ai-tech-radar/SKILL.md` |
| 仅面经／题库／练习 | `ai-career/modules/interview-collection` | `interview-collection/SKILL.md` |

把下面任一请求交给支持 Agent Skills 的工具：

```text
从 https://github.com/RZRZ-Q/rz-skills 的 v0.1.0-beta.5 安装 ai-career 整个目录。
```

```text
只从 https://github.com/RZRZ-Q/rz-skills 的 v0.1.0-beta.5 安装
ai-career/modules/ai-tech-radar，不安装整个套件。
```

也可从 [Releases](https://github.com/RZRZ-Q/rz-skills/releases/tag/v0.1.0-beta.5) 下载 ZIP 与 SHA256SUMS。使用 Codex 的 skill-installer 时，选择 `--ref v0.1.0-beta.5`；整套使用 `--path ai-career`，单装使用上表中的子路径。

已有源码副本时，也可以复制整个目标目录，以项目级安装为例：

```bash
mkdir -p /path/to/your-project/.agents/skills
# 整套安装
cp -R ai-career /path/to/your-project/.agents/skills/
# 或只装一个模块；两种方式选择其一
cp -R ai-career/modules/ai-tech-radar /path/to/your-project/.agents/skills/
```

请复制完整目录，保留其中的引用、脚本和资源文件，包括存在的 `_shared/`。安装后在目标项目开启新会话。

### 从旧版升级

旧版将几个 Skill 分别安装。改装整套时，确认原目录来自本项目并备份，再替换 `ai-career`，移出原来单装的本套件模块，避免重复注册；保留其他作者的 Skill。整套与同名单模块选择其一。

升级只替换源码目录，数据登记表和历史库留在原位置；从单模块改装整套也可继续使用同一个库。面经的飞书表和学习页进度沿用原保存方式。

## 推荐模型

Skill 不绑定模型。使用 Codex 时，可选择以下配置：

| 模型 | 推理强度 | Fast |
|---|---|---|
| `gpt-6-luna` | `high` | 可开启 |
| `gpt-6.1-sol` | `medium` | 可开启 |

## AI 职业套件：从资料到个人行动

告诉 `ai-career` 你的目标、基础、时间和预算，它会按需组合岗位、技术研究和面试资料，给出方向与行动计划。科研或项目学习可以直接开始，需要招聘匹配时再关联 JD；单项任务也可以直接调用对应模块。

```text
用 ai-jobs 找近期 Agent 实习和校招岗位，先限定字节、腾讯、阿里，每家最多两个可读 JD。
用 ai-tech-radar 跟进近一年的 Agent 评测论文和技术文章，说明实际读到了哪些部分。
用 ai-career 帮我选项目：会 Python、了解基础机器学习、没有完整 LLM 项目，
10 周、每周 10 小时、普通电脑与有限 API 预算。给出优先级、最小交付与验收标准。
用 ai-career 根据我的项目结果和面试反馈调整下一阶段计划。
用 ai-career 先核对我现有代码、运行日志和解释，找出影响当前项目的前置能力缺口。
用 ai-career 把我的实际改动、版本和结果对应到面试里能说的贡献，列出还缺的证据。
用 ai-career 继续历史库里的项目，结合这次反馈更新下一步。
```

项目建议包含要做的改动、前置能力和验收标准；已有代码与运行结果可用于诊断差距、梳理个人贡献和面试主张。科研候选会进一步核查相近论文、直接对照和实验预算，区分学习复现、工程实践与待验证的研究贡献。

### 数据保存与续接

第一次实际保存资料时，存储助手初始化空库并登记位置：

| 内容 | 默认位置 |
|---|---|
| 数据根目录登记表 | `${XDG_CONFIG_HOME:-~/.config}/ai-career/storage.json` |
| 用户资料根目录 | `${XDG_DATA_HOME:-~/.local/share}/ai-career` |
| 岗位、watchlist、原文与各轮快照 | 根目录下的 `data/` |
| 用户报告与建议 | 根目录下的 `reports/` |
| 个人目标、项目与行动索引（按需） | 根目录下的 `data/career/state.json` |
| 个人计划与逐轮复盘（按需） | 根目录下的 `reports/career/<run-id>.md` |

新会话会自动找回已有库。定位顺序为显式 `--root` → `AI_CAREER_DATA_ROOT` → 当前工作目录已有项目库 → 登记表 → 新用户默认目录。切换工作目录仍可复用登记库；多个库不会自动合并。

岗位和技术材料先查重，再增量保存内容与变化，保留历史记录。数据默认保存在本机，不提供自动跨设备同步；备份时同时保留数据根目录和登记表。详见[共用存储](ai-career/references/storage.md)、[岗位追踪](ai-career/modules/ai-jobs/references/tracking.md)、[技术追踪](ai-career/modules/ai-tech-radar/references/tracking.md)。

个人计划可在后续会话中继续：结合新代码、运行结果或面试反馈更新下一步，分别记录行动完成情况与实际核验结果。重复反馈不会重复记完成，普通资料查询也不要求建立个人档案。详见[个人进展续接](ai-career/references/progress.md)。

### 固定来源与后续扩充

| 清单 | 已核实快照与口径 |
|---|---|
| [公司内团队清单](ai-career/references/team-inventory.md) | 2026-10-14：83 个主体、197 条分型实体；包含团队、项目、生态等类型，不全是实验室 |
| [岗位来源](ai-career/modules/ai-jobs/references/source-list.md)及行业分表 | 2026-10-14：79 家公司、2 家独立研究机构；156 个已确认入口、10 个候选入口 |
| [技术公众号](ai-career/modules/ai-tech-radar/references/wechat-sources.md) | 2026-10-16：43 条来源，40 条有官方关联或入口依据（含历史关系）、3 条候选；认证名称与当前可读性另列 |
| [工程与研究来源](ai-career/modules/ai-tech-radar/references/source-list.md) | 官方博客、团队目录、代码、arXiv 与 Hugging Face Papers 等入口，逐条保留归属与阅读边界 |

清单列的是来源入口，数量不代表当前在招岗位或已采集文章。你可以按需启用来源，关注项保存在自己的 watchlist 中；也可以说“加入这家公司”“增加这个 Lab 的论文入口”“暂停这个来源并保留历史”。新增入口会先核实归属和可读性，证据不足保留候选。新增来源不会自动触发正文采集；定期追踪需另外配置宿主调度。

## 面经采集

给公司、岗位或技术方向，它会寻找实际面试经历，并核对正文中的岗位、日期和提问。也可以直接给帖子链接，跳过搜索。

```text
找字节跳动 Agent 算法岗面经，最多 5 个来源，不限时间。
只在知乎找腾讯推荐算法面经，最多 3 篇。
只在B站找算法岗实际面经，读取可用字幕，保留每题时间段。
读取这几个小红书链接，整理正文和图片里的实际问题。
```

未指定平台时默认牛客＋小红书；也可指定知乎或 B站。数量按来源帖子计算，一个合集拆成多份经历时会另报面经记录数。

只找面经时，输出链接、匹配依据和少量代表题；要求整理时，提取全部有依据的提问。招聘广告、求助帖、教程和准备题单不会当作实际面经。

→ [运行说明](ai-career/modules/interview-collection/references/find-interviews.md) · [牛客](ai-career/modules/interview-collection/references/nowcoder.md) · [小红书](ai-career/modules/interview-collection/references/xiaohongshu.md) · [知乎](ai-career/modules/interview-collection/references/zhihu.md) · [B站](ai-career/modules/interview-collection/references/bilibili.md)

## 原题整理与岗位题库

输入已有面经文字、已读取的图文材料，或帖子链接。问题保留原句、轮次和出处；候选人反问、学习建议及问方不明的片段单独说明。

```text
把这段面经整理成 Markdown，保留原句和轮次，不补答案。
把这些面经追加到这个飞书多维表格：<目标链接>
用已有面经表生成大模型算法题库，同义题合并，保留来源公司和帖子。
更新已有推荐算法题库，只补新题和新来源。
```

输出分两层：

- **原始面经与题目**：按经历和轮次保留原题、公司、岗位与出处；飞书使用面经和原题两张关联表，方便筛选与追溯。
- **岗位题库**：按岗位和主题组织标准问题、变体与追问，合并同义问法，同时保留原题及其来源。来源岗位缺失时保留“未知”，复习分类结合上下文判断；Agent 算法、应用开发和评测分别整理。

可以继续积累面经、更新岗位题库，或生成学习包与本地刷题页。追加资料前按来源链接查重，已有帖子不重复采集。

→ [运行说明](ai-career/modules/interview-collection/references/organize-interviews.md) · [公司与岗位归一](ai-career/modules/interview-collection/references/company-role.md) · [飞书两表](ai-career/modules/interview-collection/references/feishu-base.md) · [岗位题库](ai-career/modules/interview-collection/references/role-question-bank.md)

## 学习包与本地刷题

输入 CSV、XLSX、JSON、NDJSON，或读取已有飞书题库，按知识点编排学习目标、实践任务和自查标准，生成 `pack.json`、`题目.csv`、`学习包.md` 与 `index.html`。Markdown、PDF 和图片先由 Agent 审读，再整理成题目输入；只读到的材料才作为依据。飞书路线只读导出已有题目及关联原题，不新建表，也不回写练习进度。

```text
把这个 CSV 题库按知识点编排，生成能在本地打开的刷题页。
读取这个 XLSX 的“算法题”工作表，保留已有答案，没有答案的题留空。
用这个飞书岗位题库生成学习包，保留每道题的关联原题和来源依据。
用更新后的题目重新生成学习页，保留原学习包 ID 和题目 ID，让旧笔记能恢复。
```

“面经练习簿”页面支持专题、搜索与难度筛选、收藏、复习状态、作答和笔记；参考默认收起，也可选择“直接看参考”。缺少答案时可以正常练习，不自动补答案或扩题。题目显示原句、来源位置、链接和核验状态，多条来源分别保留。

更新时沿用稳定的学习包 ID 和题目 ID，保留旧作答与笔记；新增题从未练开始，移出题库的旧记录仍保留并可导出。题面或参考变化会将已掌握题目改为需复习，仅增加来源不触发降级。进度可导出／导入 JSON；同 ID 导入记录覆盖本题当前进度，未提供的题目保持不变。更换浏览器或移动 HTML 文件可能隔离本地存储，更新前先导出备份。

→ [学习流程、输入字段与更新说明](ai-career/modules/interview-collection/references/study-pack.md)

## 环境准备

| 你要做的事 | 需要的环境 |
|---|---|
| 保存岗位、技术资料和个人计划 | Python 3.9+；存储脚本使用标准库 |
| 搜索岗位、技术文章和论文 | 宿主提供搜索与网页读取能力；部分来源需要登录 |
| 导出公众号正文 | Node.js、[OpenCLI](https://github.com/jackwener/OpenCLI)、Browser Bridge 和已授权的 Chrome 会话 |
| 整理已有文字 | 宿主可以读取文本；涉及图片时需要读图能力 |
| 生成本地学习包 | Python 3.9+；CSV／JSON／NDJSON 使用标准库，XLSX 导入需可选 `openpyxl`；成品 HTML 只需浏览器 |
| 读取牛客文本 | Python 3.9+，随包脚本只使用标准库 |
| 读取小红书、知乎或B站字幕 | 已配置的 [OpenCLI](https://github.com/jackwener/OpenCLI) 与 Browser Bridge，以及用户已登录的 Chrome 会话；小红书图片下载另需 Python 3.9+ |
| 读取或写入飞书 | 已配置的 [lark-cli](https://github.com/larksuite/cli)、`lark-base` 和 `lark-shared` Skill，以及本轮目标的读取或写入权限 |

安装 Skill 后，按实际任务配置所需工具和登录态即可。本地题库学习不需要平台登录，普通 Markdown 输出不需要飞书。面经模块附带环境检查脚本，可检查依赖并指导安装，详见[环境准备](ai-career/modules/interview-collection/references/environment.md)。

第一次使用可以直接说：“我想收集一些面经并整理到飞书，请引导我完成配置。”流程会检查环境，再补齐公司、岗位、数量和输出目标等信息。详见[首次引导](ai-career/modules/interview-collection/references/onboarding.md)。

公众号采集使用 OpenCLI 的浏览器与微信正文读取能力，缺少浏览器条件时可先用可读的官方博客或论文。详见[技术材料采集](ai-career/modules/ai-tech-radar/references/collection.md)。

## 使用边界

- **网页访问**：来源是否可读，取决于网站、登录态和网络环境。浏览器采集以 OpenCLI `1.8.8` 为接口基线，实际读取能力需按平台确认；遇到登录要求、验证码或访问限制时会暂停，等待用户处理。
- **B站材料**：读取简介与可用字幕，保留分 P 和时间戳，不代表已审看视频画面；没有字幕时不会自动下载或转写。部分导航问题仍需兼容处理，见[B站说明](ai-career/modules/interview-collection/references/bilibili.md)。
- **学习页进度**：保存在当前浏览器中，跨浏览器或设备需导出／导入。已验证通过本地 HTTP 访问，直接双击 HTML 尚未验证。
- **面经图片**：原文复核和飞书入库回读完成后，默认删除本批临时图片及截图，保留来源链接与文字；用户原文件和明确要求保留的图片除外。

版本变化和已完成的验证见[发行说明](https://github.com/RZRZ-Q/rz-skills/releases/tag/v0.1.0-beta.5)。反馈问题时请提供去除个人信息和认证参数的最小示例。

## 仓库结构与维护

```text
ai-career/
  SKILL.md                       # 职业发展总入口
  references/                    # 综合建议、共享事实与进展续接
  scripts/storage.py             # 定位与复用已有历史库
  modules/
    ai-jobs/                     # 可独立安装的岗位模块
    ai-tech-radar/                # 可独立安装的工程／研究模块
    interview-collection/        # 可独立安装的面经与学习模块
scripts/build_suite.py            # 维护用构建器，不装进 Skill
README.md
LICENSE
```

业务规则维护在总入口或对应模块的原文件中，`_shared/` 与子包的 `storage.py`、雷达包的 `job_ledger.py` 为构建副本，不逐份手改。修改维护源后，用以下命令输出到一个新目录，再核对变更并替换安装包：

```bash
python3 scripts/build_suite.py --output tmp/rebuild/ai-career
```

构建器将独立模块所需的引用和脚本复制到输出目录，并重定位链接。

## 许可

源码采用 [Apache-2.0](LICENSE)。平台、外部工具、岗位正文、技术文章、论文和原始面经内容的授权不由本仓库许可证覆盖。公共来源清单只提供入口及事实说明，不随包再分发采集原文。
