# 基模公司、研究组与实验室招聘入口

2026-10-14 系统补充见[逐公司研究与工程团队清单](../../../references/team-inventory.md)：逐一排查83个主体，包含最新新增入口、公司级缺口和读取边界；下表保留原批次核验范围。

2026-10-16组织补证见[事实清单](../../../references/organization-lineage.md)：197条实体均已完成对应关系的核查尝试，未解决项逐条保留。新增事实包括MSRA通用人工智能组旧名、MSR Americas及Spatial AI父级、商汤1+X重组，以及面壁项目的分别署名；本次未重新核验岗位开放状态或招聘渠道。

核验日期：2026-10-14。21 个已确认入口、2 个候选；覆盖 15 家至少有一个已确认入口的公司及 2 家独立研究机构。同公司多入口不重复计公司。

招聘来源按所属公司／机构去重，团队单列，不把 Seed、混元、MiMo、dots 分别算成新公司。ATF／通义沿用主清单的 `jobs-alibaba-tongyi`。本表兼收公司门户、团队招聘 hub 和独立研究机构；全球目录只作为地区待筛的补充来源。

渠道“已核”指入口／项目有依据，不代表已采到该渠道完整 JD 或岗位目前开放。候选不计入官方覆盖；“未核”不等于没有。当前启用状态以用户 watchlist 为准。

## 已确认入口

| source_id | 公司／团队与入口 | 渠道／待核线索 | 官方归属依据 | 实际读取与边界 |
|---|---|---|---|---|
| `jobs-modelbest-social` | [面壁智能 / 基础模型 / Agent / 端侧 / 具身](https://modelbest.jobs.feishu.cn/career/) | 社招 | [依据1](https://modelbest.cn/) [依据2](https://modelbest.jobs.feishu.cn/career/) 实际点击官网顶部加入我们，新标签打开同站career；与campus官方互链。 | Chrome已读社招列表及大模型评测算法工程师完整JD；Jina仅品牌介绍、web空正文；92为目录瞬时数量，不计入岗位账本。 地区：中国大陆岗位；具体城市和资格逐岗核验 |
| `jobs-modelbest-campus` | [面壁智能 / 基础模型 / Agent / 端侧 / 具身](https://modelbest.jobs.feishu.cn/campus/) | 校招、实习 | [依据1](https://modelbest.jobs.feishu.cn/career/) [依据2](https://modelbest.jobs.feishu.cn/campus/) 官网直达的社招站反链校园门户，校园导航又回链社招；已读2027/2026校园项目及实习岗位列表。 | Chrome读到校园目录、60项瞬时计数及多个明确实习职位；本轮未读校园详情资格全文；校园栏目不等于全部为应届全职。 地区：中国大陆岗位；具体城市和资格逐岗核验 |
| `jobs-baichuan` | [百川智能](https://careers.baichuan-inc.com/) | 校招、实习、社招 | [依据1](https://careers.baichuan-inc.com/) 百川官方子域名招聘页明确源点计划含应届/实习、社会招聘、日常实习，并链接飞书。 | 首页及三渠道说明可读，飞书目录读取受动态加载和Jina限流影响，未取得完整JD。 地区：中国大陆岗位；具体城市和资格逐岗核验 |
| `jobs-01ai` | [零一万物](https://01ai.jobs.feishu.cn/index/) | 实习 | [依据1](https://www.01.ai/cn1) [依据2](https://01ai.jobs.feishu.cn/index/) 公司官网HTML页脚加入我们直接链接此飞书站；Chrome成功读取职位列表。 | 实际列表有知识算法、AI全栈产品工程、FDE实习岗位，以及标全职的AI测试/平台岗位；未确认独立校招渠道，全职标签不直接映射experienced，未读详情要求。 地区：中国大陆岗位；具体城市和资格逐岗核验 组织补证：2025年联合实验室与部分训练／Infra人员转入阿里按原始采访记录，非零一公司合并。 [事实表](../../../references/organization-lineage.md) |
| `jobs-sensetime` | [商汤科技](https://hr.sensetime.com/) | 社招、校招、实习 | [依据1](https://www.sensetime.com/cn/join-us) [依据2](https://hr.sensetime.com/campus/?c=1) 商汤官网简历投递明确社招、校招、实习入口；2027校园页注明应届和实习对象及官方ATS跳转。 | 公司页与2027校园项目正文可读；招聘根页Jina限流。已核目录用途，未完整读取具体JD。 地区：中国大陆岗位；具体城市和资格逐岗核验 |
| `jobs-bytedance-seed` | [字节跳动 / Seed](https://seed.bytedance.com/zh/career) | 社招、校招、实习 | [依据1](https://seed.bytedance.com/zh/career) 字节官方 Seed 子域名，招聘页明确社招和校招，并链接2027人才专项 | 字节官方 Seed 子域名，招聘页明确社招和校招，并链接2027人才专项；专项明确应届生及实习生毕业窗口。已读岗位标题、团队方向和资格窗口，未点击动态投递按钮读完整JD，不作为独立ATS。 地区：中国大陆为主 组织补证：豆包大模型团队与Seed名称对应已核；AI Lab吸收为2025年4月原始报道事实。 [事实表](../../../references/organization-lineage.md) |
| `jobs-tencent-qingyun` | [腾讯 / 青云计划（含混元、ARC Lab、Robotics X等）](https://join.qq.com/qingyun.html) | 校招 | [依据1](https://join.qq.com/qingyun.html) 腾讯官方校招域名的技术人才专项，正文展示混元基础模型/AI Infra、ARC Lab、Robotics X等导师及课题介绍 | 腾讯官方校招域名的技术人才专项，正文展示混元基础模型/AI Infra、ARC Lab、Robotics X等导师及课题介绍；本次正文能读专项和团队关系，岗位卡片未渲染。搜索索引提及实习生但不将摘要视作渠道已核实，因此暂仅标校园专项。 地区：中国大陆为主 |
| `jobs-tencent-jarvis` | [腾讯 / 天衍研究中心 Jarvis](https://jarvislab.tencent.com/join-us.html) | 实习 | [依据1](https://jarvislab.tencent.com/join-us.html) 腾讯官方研究中心子域名，招聘正文明确研究型实习生面向本科/硕士/博士在读，并给出官方邮箱 | 腾讯官方研究中心子域名，招聘正文明确研究型实习生面向本科/硕士/博士在读，并给出官方邮箱；研究员只见招募表述，未读到独立完整JD或社招类别。该页是团队邮件招聘入口，不是ATS。 地区：中国大陆为主 组织补证：官网2023—2024年署为优图实验室天衍研究中心，主要方向医疗AI；2026完整汇报链未核。 [事实表](../../../references/organization-lineage.md) |
| `jobs-alibaba-damo` | [阿里巴巴 / 达摩院 DAMO Academy](https://joindamo.alibaba.com/) | 待核 | [依据1](https://joindamo.alibaba.com/) 阿里官方子域名，实际HTML title为达摩院招聘官网、meta邀请加入达摩院、内嵌circle归属为DAMO Academy | 阿里官方子域名，实际HTML title为达摩院招聘官网、meta邀请加入达摩院、内嵌circle归属为DAMO Academy；页面为JS壳，Jina只有标题/提示，未读到当前岗位。代码中的旧毕业时间与关闭开关不作为当前渠道依据，渠道保留unknown。 地区：中国大陆为主 组织补证：通义由达摩院孵化是历史沿革，无证据表明达摩院整体并入ATF。 [事实表](../../../references/organization-lineage.md) |
| `jobs-meituan-longcat` | [美团 / LongCat](https://zhaopin.meituan.com/longcatprogram) | 社招、校招、实习 | [依据1](https://zhaopin.meituan.com/longcatprogram) 美团官方招聘域名下的LongCat专页，正文有社会招聘和校园招聘链接，FAQ明确LongCat校招实习生招聘 | 美团官方招聘域名下的LongCat专页，正文有社会招聘和校园招聘链接，FAQ明确LongCat校招实习生招聘；本次读取团队介绍、模型方向及入口，校招职位页动态空正文，未采完整JD。 地区：中国大陆为主 组织补证：美团2023年8月完成收购光年之外；Tabbit官方明确GN06（光年之外）开发主体，美团官网刊载报道记载Tabbit内置LongCat等模型；未证实光年整体更名或合并为LongCat。 [事实表](../../../references/organization-lineage.md) |
| `jobs-microsoft-msra` | [微软 / Microsoft Research Asia](https://www.microsoft.com/en-us/research/careers/open-positions/?facet%5Btax%5D%5Bassociated_msr_research_lab%5D%5B0%5D=199560) | 实习 | [依据1](https://www.microsoft.com/en-us/research/careers/open-positions/?facet%5Btax%5D%5Bassociated_msr_research_lab%5D%5B0%5D=199560) 微软官方研究网站的Asia筛选目录，实际显示37项Internship和3项Researcher（目录瞬时计数，未逐条核验在招） | 微软官方研究网站的Asia筛选目录，实际显示37项Internship和3项Researcher（目录瞬时计数，未逐条核验在招）；读取了北京FDE实习生完整职责、条件、三个月全职要求和邮箱申请说明。只确认internship；Researcher不自动映射experienced。岗位目录包含中国大陆及海外地区，应逐岗位判断。 地区：中国大陆及亚洲/全球部分岗位 |
| `jobs-google-deepmind` | [Google / Google DeepMind](https://deepmind.google/careers/) | 待核 | [依据1](https://deepmind.google/careers/) DeepMind官方careers页面明确其Google归属，列出Research Engineer/Research Scientist等职业介绍并链接Google Careers中DeepMind筛选 | DeepMind官方careers页面明确其Google归属，列出Research Engineer/Research Scientist等职业介绍并链接Google Careers中DeepMind筛选；只读团队招聘介绍及跳转，不把职业介绍当完整JD。Student Researcher项目仅见入口，国内三渠道尚未逐项核实。 地区：全球；中国大陆机会未确认 组织补证：2023-04-20公告由原DeepMind和Google Research的Brain团队合并；Google Research继续存在。 [事实表](../../../references/organization-lineage.md) |
| `jobs-openai` | [OpenAI / Research / Agents / Engineering](https://openai.com/careers/search/) | 待核 | [依据1](https://openai.com/careers/) [依据2](https://openai.com/careers/search/) OpenAI官方岗位目录实际列出工作地点、团队与Ashby投递链接 | OpenAI官方岗位目录实际列出工作地点、团队与Ashby投递链接；已读取Agent Post-Training, Frontier Evals and Environments Research完整职责与资格。公开研究岗位和实践经验要求不证明中国社招或校招，channels保留unknown，未读取到明确聘用形式则employment_type_raw为null。 地区：全球；本次完整JD为San Francisco |
| `jobs-anthropic` | [Anthropic / AI Research & Engineering](https://www.anthropic.com/careers/jobs) | 待核 | [依据1](https://www.anthropic.com/careers) [依据2](https://www.anthropic.com/careers/jobs) [依据3](https://job-boards.greenhouse.io/anthropic/jobs/5198255008) Anthropic官方岗位目录直接链接Greenhouse | Anthropic官方岗位目录直接链接Greenhouse；实际读完Research Engineer, Post-Training Model Evaluations职责、资格和地点。JD未给确定工作年限，不映射国内experienced，channels为unknown；careers FAQ明确目前不提供internships，Fellows不能当作实习或中国校招。 地区：全球；本次完整JD为San Francisco/Seattle |
| `jobs-shanghai-ai-lab` | [上海人工智能实验室 / 人才招聘](https://www.shlab.org.cn/joinus/social) | 社招、校招 | [依据1](https://www.shlab.org.cn/joinus/social) 上海人工智能实验室官网的人才招聘页明确社招和校招，并给出机构名称/版权 | 上海人工智能实验室官网的人才招聘页明确社招和校招，并给出机构名称/版权；实际读取只到筛选和模板占位符，未见职位内容。联合培养招生与招聘分开，不将招生视作岗位；实习未在当前成功正文中确认。 地区：中国大陆为主 |
| `jobs-shanghai-ai-lab-robotics` | [上海人工智能实验室 / 具身智能中心 / Intern Robotics](https://internrobotics.shlab.org.cn/aboutus.html) | 待核 | [依据1](https://internrobotics.shlab.org.cn/aboutus.html) 上海AI实验室官方子域名列出具身生成、具身大模型、人形机器人、世界模型、感知、物理仿真等招聘方向，并提供pjlab.org.cn联系邮箱 | 上海AI实验室官方子域名列出具身生成、具身大模型、人形机器人、世界模型、感知、物理仿真等招聘方向，并提供pjlab.org.cn联系邮箱；未细分社招/校招/实习，不将团队名称中的Intern理解为实习。 地区：中国大陆为主 |
| `jobs-baai` | [北京智源人工智能研究院 / BAAI](https://app.mokahr.com/social-recruitment/baai/42173) | 社招、校招、实习 | [依据1](https://www.baai.ac.cn/en/) [依据2](https://app.mokahr.com/social-recruitment/baai/42173) [依据3](https://app.mokahr.com/campus-recruitment/baai/42174) BAAI官方网站的Career直接链接Moka社招42173和校招42174，ATS又链接回baai.ac.cn，形成双向官方链路 | BAAI官方网站的Career直接链接Moka社招42173和校招42174，ATS又链接回baai.ac.cn，形成双向官方链路；校招目录显示2027届及实习生栏目，社招显示科学家/研究员/工程专家栏目，未逐条采JD。 地区：中国大陆为主 |
| `jobs-xiaomi-mimo` | [小米 / MiMo](https://mimo.xiaomi.com/zh) | 待核 | [依据1](https://mimo.xiaomi.com/zh) 小米官方子域名正文明确小米MiMo团队 | 小米官方子域名正文明确小米MiMo团队；加入我们展示预训练、后训练、AI Infra、语音、多模态、数据等六类岗位和官方联系邮箱。实际读取招聘区，但未读取动态岗位跳转、完整JD及明确社招/校招/实习类别，渠道unknown。 地区：中国大陆为主 |

| `jobs-xiaohongshu-dots` | [小红书 / dots studio](https://studio.dots.ai/) | 待核 | 官网与[GitHub组织](https://github.com/studio-dots-ai)、HF互链；[项目许可](https://github.com/studio-dots-ai/dots.vlm1/blob/main/LICENSE)写明Xingyin发布主体及Xiaohongshu商标；模型README标小红书版权。 | Join Us展示预训练、后训练岗位及职责；完整资格、招聘渠道、可投状态未核。Business inquiries邮箱不当投递邮箱。2026-10-14补证后由candidate转active。 组织补证：官网说明2025年初由小红书内部大模型团队演进；2026年4月宣布成立Dots一级部门、10月宣布与核心infra打通按原始报道单列，内部信原件未取得；与AllSpark的上下级／合并关系仍未闭合。 [事实表](../../../references/organization-lineage.md) |
| `jobs-xiaohongshu-allspark` | [小红书 / AllSpark 招募区](https://github.com/AllSpark-Research#to-join-us) | 实习、社招；团队校招未核 | 公司[完整社招JD](https://job.xiaohongshu.com/social/position/19257)使用AllSpark团队名；GitHub/HF互链及公司域招募邮箱、HR投递链接；论文团队署名补充印证。 | 全年研究实习招募可读，未读实习完整资格；Chrome读到1份完整社招JD。作为团队招聘hub关联jobs-xiaohongshu，不新计公司或ATS；不把AllSpark与dots合并。 |
| `jobs-netease-fuxi` | [网易 / 网易伏羲实验室](https://fuxi.netease.com/recruitment) | internship | 网易域名的实验室正文、招聘栏目、公司页脚互证。 | 当前2条列表职位，分别为游戏AI实习与全职工程师；仅实习渠道确认，不将全职等同社招。未读取单岗详情。 组织补证：2024公司招聘简章归雷火事业群；互娱AI Lab于2025-08-11官方否认与伏羲合并。 [事实表](../../../references/organization-lineage.md) |

## 待核候选

| source_id | 公司／团队与入口 | 渠道／待核线索 | 官方归属依据 | 实际读取与边界 |
|---|---|---|---|---|
| `jobs-iflytek-candidate` | [科大讯飞](https://iflytek.zhiye.com/) | 校招、社招、实习 | [依据1](https://iflytek.zhiye.com/) 招聘站品牌、联系方式和回链iflytek.com可读；本轮未取得公司官网到该ATS的反向链接或认证主体，旧join子域TLS失败。 | Chrome读到校招/社招/实习导航与星火X计划、AI研究院介绍；渠道为目录自述，官方归属待补证，暂不启用。 地区：中国大陆岗位；具体城市和资格逐岗核验 |
| `jobs-tencent-ailab` | [腾讯 / AI Lab](https://ailab.tencent.com/ailab/zh/recruit/) | 待核 | [依据1](https://ailab.tencent.com/ailab/zh/recruit/) 搜索发现腾讯官方AI Lab招聘地址 | 搜索发现腾讯官方AI Lab招聘地址；本次直接读取Web为502、Jina为403、直连TLS失败。只有搜索摘要显示研究员与实习生，缺少成功正文读取，保留候选，不据此确认当前渠道或在招。 地区：中国大陆为主 组织补证：2026-03-20撤销及两路人员分流有原始报道；本行保留历史候选入口，不代表当前独立AI Lab仍在招聘。 [事实表](../../../references/organization-lineage.md) |

## 三渠道覆盖

| 公司／机构 | 实习 | 校招 | 社招 |
|---|---|---|---|
| 面壁智能 | 入口已核 | 入口已核 | 入口已核 |
| 百川智能 | 入口已核 | 入口已核 | 入口已核 |
| 零一万物 | 入口已核 | 未核 | 未核 |
| 商汤科技 | 入口已核 | 入口已核 | 入口已核 |
| 科大讯飞 | 仅候选线索 | 仅候选线索 | 仅候选线索 |
| 字节跳动 | 入口已核 | 入口已核 | 入口已核 |
| 腾讯 | 入口已核 | 入口已核 | 未核 |
| 阿里巴巴 | 未核 | 未核 | 未核 |
| 美团 | 入口已核 | 入口已核 | 入口已核 |
| 微软 | 入口已核 | 未核 | 未核 |
| Google | 未核 | 未核 | 未核 |
| OpenAI | 未核 | 未核 | 未核 |
| Anthropic | 未核 | 未核 | 未核 |
| 上海人工智能实验室 | 未核 | 入口已核 | 入口已核 |
| 北京智源人工智能研究院 | 入口已核 | 入口已核 | 入口已核 |
| 小米 | 未核 | 未核 | 未核 |
| 小红书 | AllSpark招募已核 | 团队专属未核 | AllSpark JD已核 |
| 网易／伏羲 | 入口已核 | 未核 | 未核 |

## 已确认团队，通过既有公司入口跟踪

没有独立团队招聘站，不影响团队入表。此处通过父来源的 `team_queries` 跟踪，不另增来源数量或公司数量。

| 公司／团队 | 招聘入口与查询 | 归属与研究入口 | 当前可读性／渠道 |
|---|---|---|---|
| BOSS直聘 / 南北阁 / Nanbeige LLM Lab | 社招沿用 `jobs-boss-zhipin-social` 的[公司自招页](https://www.zhipin.com/gongsi/fa2f92669c66eee31Hc~.html)；校园沿用 `jobs-boss-zhipin-campus` 的[公司校园页](https://www.zhipin.com/campus/pc/)。查询南北阁、Nanbeige、Nanbeige LLM Lab。 | [公司业绩材料](https://ir.zhipin.com/static-files/ea54044d-acb0-4fa4-9ab4-8c0e82453e7e)、[论文作者机构](https://arxiv.org/html/2607.22083v2)、[HF组织](https://huggingface.co/Nanbeige)与[GitHub](https://github.com/Nanbeige)互证；公司归属已确认。 | [具体JD](https://www.zhipin.com/job_detail/c29316112f7adcdf0nR_2t66ElBX.html)于2026-10-14读到“招聘中”、页面更新2026-10-13，正文公司北京华品博睿。标题混称实习生/工程师，完整正文需登录；不拆成两岗、不自动继承父源三渠道。2025实习帖只保留历史线索。 |

以上三个团队的研究／代码URL均保存在招聘团队记录中，可交给 ai-tech-radar 继续发现论文和工程材料；本轮不等同已完成论文采集。dots与AllSpark分别保留团队标识，当前证据未说明两者改名、合并或上下级关系。

## 继续核查与衔接

蚂蚁研究院／百灵／inclusionAI：本轮读到研究和模型介绍，未确认独立招聘区，回退既有 `jobs-ant`。腾讯混元、ARC Lab、Robotics X 本轮由青云专项承接，未各造一个招聘门户。网易伏羲现行团队招聘页已核，沿用原source_id更新URL并保留旧专题别名；实习已核，全职类别不自动归社招。研究网站、arXiv、HF Papers 与论文模板归属仍由 ai-tech-radar 跟进，本轮没有把招聘页数量当作论文覆盖。

新增、暂停、迁移与幂等合并按[清单维护](tracking.md#来源清单与扩充)执行；总目录见[固定来源清单](source-list.md)。
