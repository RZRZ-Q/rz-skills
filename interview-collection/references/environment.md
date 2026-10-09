# 按功能检查与安装环境

随 Skill 提供 `scripts/setup_environment.py`，只装本轮需要的依赖。默认执行只读 `check`；不会搜索平台、启动 Chrome、读取认证或修改宿主配置。脚本本身只用标准库，需要 Python 3.9+。若没有 Python，由 Agent 按 [Python 官方说明](https://www.python.org/downloads/)指导安装，脚本不能安装自己的解释器。

## 先选择本轮功能

| `--features` | 检查什么 | 仍需完成什么 |
|---|---|---|
| `local` | Python，可用于文本／CSV／JSON 与本地页面生成 | Agent 宿主、模型和文件能力；成品 HTML 仅需浏览器 |
| `nowcoder` | Python；牛客脚本仅用标准库 | 首个预算内真实读取验证网络与内容 |
| `browser` | OpenCLI、Node.js 版本，npm 是否可用于安装 | Chrome、Bridge、指定 profile；本轮命令参数和真实平台登录 |
| `feishu` | `lark-cli --version` | `lark-base`、`lark-shared`、用户认证、身份和目标权限 |
| `excel` | 可导入 `openpyxl.load_workbook` 及版本 | 使用题包生成器直接读取 XLSX 时需要；宿主已能读取时也可先整理成 CSV／JSON |
| `pdf` | 可导入 `pypdf.PdfReader` 及版本 | 文本 PDF；扫描页、图像和公式另用宿主读图，安装不等于正确提取 |

功能可用逗号组合。以下示例在**用户项目根目录**运行，先将 `SKILL_DIR` 设置为本机实际安装的 `interview-collection` Skill 绝对路径；路径带空格时保留引号。局部依赖放在项目的 `interview-results/runtime/`，可将该路径加入项目 `.gitignore`，不在 Skill 包内创建 runtime：

```bash
SKILL_DIR="/实际安装路径/interview-collection"
python3 "$SKILL_DIR/scripts/setup_environment.py" --features local
python3 "$SKILL_DIR/scripts/setup_environment.py" check --features nowcoder,browser,feishu --runtime "$PWD/interview-results/runtime"
```

JSON 报告包含工具路径、版本、`missing`、`pending` 与 `next_steps`。`tools_ready=true` 和退出码 `0` 仅表示所选本机工具检查通过；`pending` 不因此消失。缺少必需工具退出 `1`；参数错误或安装失败退出 `2`。检查不创建 runtime 目录。npm 仅用于安装，已有工具可运行时，缺少 npm 不影响检查通过。

OpenCLI 的 `--help` 会进入初始化、插件发现及更新检查，可能写用户配置目录。因此此工具只运行其 `--version`，不自动运行帮助、`doctor` 或 `profile list`。版本检查不证明 `--profile`、`browser <session>` 或 `--window background` 满足本轮需要；按[首次引导](onboarding.md)及所选平台说明核对。Bridge 连通也不证明平台登录。已有工具能运行时先保留；若本轮参数确实不支持，明确报告差异，再决定局部安装或用户升级。

## 按需安装到明确目录

用户选定功能并授权安装后运行：

```bash
python3 "$SKILL_DIR/scripts/setup_environment.py" install --features browser --runtime "$PWD/interview-results/runtime"
python3 "$SKILL_DIR/scripts/setup_environment.py" install --features excel,pdf --runtime "$PWD/interview-results/runtime"
```

`install` 必须显式提供功能和目录。先复用可运行的已有工具／具备读取入口的 Python 包，只补缺失项，不自动升级全局。OpenCLI 安装到 `interview-results/runtime/npm`，npm 缓存也在所选 runtime；使用 `--ignore-scripts` 防止包安装钩子触发宿主配置。Python 可选包安装到独立 `interview-results/runtime/python` venv，失败保留原始错误和现场。版本由脚本常量统一维护，按 [npm 版本 API](https://registry.npmjs.org/@jackwener/opencli/1.8.8)、[openpyxl PyPI API](https://pypi.org/pypi/openpyxl/json)、[pypdf PyPI API](https://pypi.org/pypi/pypdf/json)核对；新增安装固定直接依赖，npm 在 runtime 保存 lockfile，未声称锁定所有 Python 传递依赖。

若缺少 Node.js/npm，按 [Node.js 官方安装入口](https://nodejs.org/en/download)补齐后复检，脚本不安装 Node.js。OpenCLI 所选公开包的最低 Node.js 要求由脚本检查。不要将作者机器的预发布版、`.venv`、`node_modules` 或 Chrome profile 当作可移植环境分发。

后续使用报告给出的确切工具／Python 路径。局部安装后的常见路径为：

```bash
"$PWD/interview-results/runtime/npm/node_modules/.bin/opencli" --version
"$PWD/interview-results/runtime/python/bin/python" -c 'import openpyxl, pypdf; print(openpyxl.__version__, pypdf.__version__)'
```

Windows 对应 `interview-results\runtime\npm\node_modules\.bin\opencli.cmd` 与 `interview-results\runtime\python\Scripts\python.exe`。如使用其他采集说明中的 `opencli` 命令，可在**当前进程** PATH 加入报告中的局部 `.bin` 路径；不修改 shell 启动文件或系统 PATH。

## OpenCLI 能力与本地补充

2026-10-09 核对官方 `1.8.8` 与当日主分支：搜索筛选 [PR #2276](https://github.com/jackwener/OpenCLI/pull/2276) 已于 2026-08-24 合并，包含排序、笔记类型、发布时间、搜索范围及位置；无需分发旧预发布版本或重打筛选补丁。Skill 仍按[小红书流程](xiaohongshu.md)控制页面加载次数，不能把原生搜索的条数限制当作滚动／重开预算。

随包只保留本流程需要的补充：`open_xhs.mjs` 从 stdin 接收完整访问链接并在同进程调用已安装 OpenCLI；`capture_xhs.js` 在已开页面一次提取有换行的正文、日期与图片并检查页面身份；`download_xhs_images.py` 按数量和总字节预算下载原始图片地址，不携带 Cookie、不自动重试。官方 `1.8.8` 尚无上述 stdin 打开入口，其通用下载命令也不提供这些预算参数，且会去除图片查询参数，因此暂不替换本地脚本。

`open_xhs.mjs` 使用 Node.js，须指定环境检查确认的 npm 包根目录（含 `package.json` 和 `bin.opencli`）。它不安装或修改 OpenCLI，原生初始化、Bridge 与输出行为保持不变；此入口已做离线参数和进程检查，尚未完成 `1.8.8` 的真实平台验收。升级依赖时核对实际功能和行为，已被上游等效覆盖的补充优先移除，不按旧 PR 状态长期携带补丁。

## 飞书与人工步骤

`install --features feishu` 只报告状态和官方步骤，不自动运行飞书安装器。缺少 `lark-cli` 时，由用户按 [官方安装流程](https://github.com/larksuite/cli#installation--quick-start)执行：

```bash
npx @larksuite/cli@latest install
```

该交互过程可能安装 CLI、Skills 并配置 Agent 宿主；它与仅在 runtime 安装依赖不同。需要 Node.js/npm，安装完成后再次 `check --features feishu`，并由 Agent 确认相关 Skill 可用；认证与目标核对按[飞书说明](feishu-base.md)执行。没有完成上述步骤时，报告“待用户完成”，不声称已安装或已授权。

Chrome、Browser Bridge 的启用、账号登录以及 Agent 宿主／模型不能打包。按 [OpenCLI 官方步骤](https://github.com/jackwener/OpenCLI#quick-start)准备用户所选 profile；本工具不连接用户 Chrome。默认不安装 OCR、GPU 依赖、模型权重、Docker、数据库或浏览器。环境检查和安装完成后，仍须按本轮方案进行有预算的真实读取及输出核验，才能说明业务可用。
