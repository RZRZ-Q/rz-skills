# RZ Skills

一个仓库，多个可以独立安装、组合使用的 Agent Skills。

目前收录 `interview-collection`：一次安装，完成找面经、读取原文、整理问题、写入飞书、生成岗位题库，以及从现有题目生成专题学习包和本地刷题页。它内部包含采集、整理、学习与刷题三个流程，由统一入口按任务调用。以后新增其他 Skill 时，在仓库根目录并列添加独立目录。

包含采集、整理、学习页与按需环境准备的完整源码。用户资料、题库数据、账号和认证信息不随源码分发。

## Skill 目录

| Skill | 用来做什么 | 直接这样说 |
|---|---|---|
| [interview-collection · 面经采集与整理](interview-collection/SKILL.md) | 搜索或读取面经，整理原题，追加飞书，生成岗位题库与本地学习页 | “找腾讯大模型算法面经，最多 5 篇，整理进飞书。”／“把已有题库做成按知识点学习的本地刷题页。” |

## 安装

在支持 Agent Skills 的工具里，把本仓库链接交给 Agent：

```text
帮我安装这个仓库里的 interview-collection：https://github.com/RZRZ-Q/rz-skills
```

只需安装 `interview-collection` 一个目录。三个流程都在包内，不需要分别安装，也不需要用户手动切换。

也可以下载仓库后手动复制。以支持项目级 `.agents/skills/` 的宿主为例，从本仓库根目录执行以下命令，把目标路径换成自己的项目：

```bash
mkdir -p /path/to/your-project/.agents/skills
cp -R interview-collection /path/to/your-project/.agents/skills/
```

已有同名目录时先保留旧副本。复制整个 Skill 目录，包括 `references/`、`scripts/` 和 `assets/`，不要只拿 `SKILL.md`。在目标项目开启新会话，确认宿主已识别 Skill；其他宿主按其 Skill 目录配置安装。Skill 本身不绑定模型。

## 推荐模型

使用 Codex 时，推荐以下两组配置：

| 模型 | 推理强度 | Fast |
|---|---|---|
| `gpt-6-luna` | `high` | 可开启 |
| `gpt-6.1-sol` | `medium` | 可开启 |

在 Codex 的模型设置中选择对应模型和推理强度，按需开启 Fast。本项目目前主要使用 `gpt-6.1-sol` + `medium` 进行实测；上述配置是使用建议，不是 Skill 的运行要求。

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
- **岗位题库**：用户选择后，每个岗位一张表，包含标准问题、主题、变体与追问、来源公司、原题和面经关联。只在派生题库合并同义问法，保留原始题目记录。

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

源码采用 [Apache-2.0](LICENSE)。平台、外部工具和原始面经内容的授权不由本仓库许可证覆盖。
