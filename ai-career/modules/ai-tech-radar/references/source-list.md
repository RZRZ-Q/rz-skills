# 技术雷达固定来源清单

2026-10-14 系统补充见[逐公司研究与工程团队清单](../_shared/references/team-inventory.md)：逐一排查83个主体，包含最新新增入口、公司级缺口和读取边界；下表保留原批次核验范围。

2026-10-16组织补证见[事实清单](../_shared/references/organization-lineage.md)：剩余133条实体已分四批核查，补团队旧名、父级和合作主体。Mooncake官方仓库入口修正为[kvcache-ai/Mooncake](https://github.com/kvcache-ai/Mooncake)；NVIDIA AIE入口迁至[当前团队页](https://research.nvidia.com/labs/aie/)，其与GenAIR、GEAR的LPR父级已核。工程文章和论文采集基线保持原范围。

这是随技能分发的入口种子表，供首次选源与补充来源使用。用户工作目录中的 `watchlist.json` 决定实际启用范围；已有关注项、排除项和预算优先。表中入口不自动全部启用，也不代表已读完其文章、论文或代码。

核验日：**2026-10-13**。本轮核对目录／仓库首页、归属线索与可访问性，未逐条抓取目录、遍历分页或运行模型。后续使用时按本轮访问结果更新状态，不把这个日期当作永久有效证明。`engineering` 和 `research` 是分析模式；公司、团队和项目分别识别，具体材料仍以发表时的作者归属为准。

2026-10-15 公众号主动盘点覆盖现有 26 家互联网公司；2026-10-16 最新复核剩余 7 个候选，百度Geek说、搜狐技术产品、大淘宝技术、京东零售技术升级，唯品技术、金山办公、腾讯AlloyTeam 继续待核。当前 **43 个公众号来源（40 个官方关联或官方入口、3 个候选）**。阿里云开发者（当前页面名：千问AI平台）继续显式展示与同号检索。名称、身份层级与待核关系见[公众号固定表](wechat-sources.md#2026-10-16-七项候选复核)。

## 核心公司与团队

| `source_id` | 公司 / 团队 | `modes` | 固定入口 | 归属证据与使用边界 |
|---|---|---|---|---|
| `bytedance-seed-research` | 字节跳动 / Seed | `engineering,research` | [Seed 博客与论文](https://seed.bytedance.com/zh/research) | 页面含 ByteDance Seed 页脚与博客、精选论文、AI Infra 分类。精选列表不等于团队全部论文。 |
| `tencent-hunyuan-research` | 腾讯 / 混元；子团队按文章确认 | `research` | [混元研究目录](https://hunyuan.tencent.com/research) | 腾讯官方域名；目录显示 RL Team、Pretrain Team 等署名。普通网页读取超时，Jina 本轮取得目录正文；不把失败当作没有更新。 组织补证：2026年AI Lab分流与混元基础模型部合并分开记录，非简单品牌改名。 [事实表](../_shared/references/organization-lineage.md) |
| `tencent-cloudbase-blog` | 腾讯 / 腾讯云 CloudBase | `engineering` | [CloudBase 官方博客](https://tcb.cloud.tencent.com/blog) | 页面自述腾讯云开发官方博客，列有 CloudBase Team 署名、技术实践与社区故事。收录时分别核对作者，不能把社区故事全部归为腾讯内部研发。 |
| `alibaba-qwen-research` | 阿里巴巴 / ATF 下的 Qwen 研发线 | `engineering,research` | [Qwen Research](https://qwen.ai/research) | [旧官方博客](https://qwenlm.github.io/blog/)明确指向新站；新站有 Research Index，站点标注 Alibaba Cloud。保留旧址为 alias，不新增第二个团队；旧博客用于历史补充。2026-06-08 通义大模型事业部与原淘天未来生活实验室合并为 Token Foundry；通义→通义大模型事业部→ATF及ATH父级的证据见[阿里巴巴组织沿革](../_shared/references/organization-lineage.md#阿里巴巴)。 |
| `meituan-tech-blog` | 美团 / 技术团队；子团队按文章确认 | `engineering,research` | [美团技术团队](https://tech.meituan.com/) | 官方技术站含团队介绍与文章目录。按当前目标主题筛选，不能把同站所有业务文章归为 LongCat 研究。 |
| `meituan-longcat-code` | 美团 / LongCat | `engineering,research` | [LongCat 官方仓库组织](https://github.com/meituan-longcat) | 组织页显示美团邮箱；[美团 VitaBench 文章](https://tech.meituan.com/2025/11/02/LongCat-VitaBench-Agent.html)链接该组织的仓库。组织首页只用于发现，各项目需另查论文、许可及代码范围。组织补证：光年之外／GN06开发Tabbit、Tabbit接入LongCat已核；未证实两团队整体更名或合并。[事实表](../_shared/references/organization-lineage.md) |
| `openai-research` | OpenAI / 具体团队按材料确认 | `research` | [OpenAI Research Index](https://openai.com/research/index/) | [OpenAI 研究主页](https://openai.com/research/)直接链接该目录。目录混有发布与安全等类别，按问题筛选，不能以单篇 BrowseComp 作为全公司追踪入口。 |
| `anthropic-engineering` | Anthropic / 具体工程团队按材料确认 | `engineering` | [Anthropic Engineering](https://www.anthropic.com/engineering) | 公司官方工程目录；适合查 Agent、Harness、上下文与评测方法。标题只用于筛选，方法结论仍需读正文。 |
| `anthropic-research` | Anthropic / 各研究团队 | `research` | [Anthropic Research](https://www.anthropic.com/research) | 官方页明确列研究团队与近期工作。与 Alignment 子站重叠的同一工作按 `work_id` 关联。 |
| `anthropic-alignment` | Anthropic / Alignment Science | `research` | [Alignment Science Blog](https://alignment.anthropic.com/) | About 明确自述为 Anthropic Alignment Science 团队并链接公司研究页。关注评测、监督与审计；不代表公司全部研究。 组织补证：About直接对应公司Alignment条目；内部父子层级未核。 [事实表](../_shared/references/organization-lineage.md) |

## 可选扩展与开源实践入口

以下 **5 个入口** 已完成同日入口核验，按用户方向加入关注范围；“可选”表示是否启用，不表示归属未确认。

| `source_id` | 公司 / 团队或项目 | `modes` | 固定入口 | 归属证据与使用边界 |
|---|---|---|---|---|
| `deepseek-code` | DeepSeek / 具体团队未知 | `engineering,research` | [DeepSeek 官方组织](https://github.com/deepseek-ai) | [公司官网](https://www.deepseek.com/)直接链接该组织，组织页反链官网。按项目发现技术报告和实现；仓库更新数不是论文数。 |
| `moonshot-research` | 月之暗面 / Kimi；子团队按材料确认 | `research` | [Kimi Research & Tech Blog](https://www.kimi.ai/blog/) | [Moonshot 官网](https://www.moonshot.ai/)的 Latest Research 指向此页；本轮读到模型与 benchmark 条目。研究目录不能代替各论文的作者归属。 |
| `qwen-agent-code` | 阿里巴巴 / Qwen-Agent 项目 | `engineering` | [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | QwenLM 仓库 README 链接 Qwen 博客和产品，说明项目关系。用于应用、工具调用、RAG、MCP 与评测代码发现；本清单未重验所有模块。 |
| `openai-evals-code` | OpenAI / Evals 项目 | `engineering,research` | [OpenAI Evals](https://github.com/openai/evals) | OpenAI 组织内仓库，README 链接官方评测文档。含社区贡献的 benchmark；不能把每个条目都算为 OpenAI 研究成果。 |
| `vllm-code` | `company=null` / vLLM 开源项目 | `engineering` | [vLLM](https://github.com/vllm-project/vllm) | 项目 README 与文档互链。用于推理服务和性能评测实现；不归属任一招聘公司，具体建议须固定 commit、路径与资源条件。 |

## 补充发现与待核候选

- 研究补充入口包括 arXiv 与 Hugging Face Papers，不只检查公司博客。按[论文平台与团队归属](research.md#从论文平台补齐团队研究)组合团队别名／主题搜索，核论文作者单位或模板中的明确品牌标识；HF 与 arXiv 同一论文按同一 `work_id` 关联。Daily Papers、热门榜单与团队所有产出不等价。

- [主要互联网平台扩展清单](large-internet-sources.md)新增百度、京东、快手、小米及 18 家平台的工程、研究、公众号来源，包含已核入口与待核候选。按[公司覆盖表](../_shared/references/company-coverage.md)检查遗漏，不能把某个团队来源当作整家公司覆盖完成。

- `blogrxiv-discovery`：[BlogrXiv](https://github.com/OpenEnvision/BlogrXiv)，维护者 OpenEnvision，模式 `engineering,research`。本轮核验 README 的精选索引定位及原站链接；用于发现线索，回到原始来源后才收录材料。它不是公司官方来源，不以收录数比较 Lab 论文产量或活跃度。
- [大厂技术公众号固定清单](wechat-sources.md)与互联网平台扩展清单记录账号、名称关系和替代目录。2026-10-15 已补“阿里云开发者／阿里开发者／当前千问AI平台”的同号证据与携程当前原文入口；2026-10-16 已确认大淘宝技术历史官方运营、京东零售技术官方互链。不同名称的证据类型及待核关系见分表。2026-10-13 的原链访问失败保留为历史观察，不代表当前不可读；其他相近账号不继承身份结论。
- [Alibaba Cloud Community](https://www.alibabacloud.com/blog)是官方域名上的混合作者平台。可作为候选发现入口，需逐篇核对作者和团队，不将整站等同于阿里内部工程输出。

## 新增与维护

新增来源按[清单维护](tracking.md#来源清单与扩充)处理；任务包含材料采集或分析时再使用[采集流程](collection.md)。新增公司、Lab、公众号或仓库时，先查现有 `source_id` 与 aliases；同团队不同目录可以各有来源 ID，同一工作仍合并到同一 `work_id`。新条目至少补齐本表列出的组织、模式、规范入口、归属证据、核验日期和实际访问边界，再写入用户的关注清单。

迁站时保留 `source_id`，记录旧 URL 为 alias；换运营主体或换团队时另建条目。临时不可访问保留该源及失败记录，不删除历史材料。来源清单的扩充、一次目录核验、某篇文章精读和定期运行是四种不同结果，报告时分别说明。
