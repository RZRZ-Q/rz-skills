# AI 创业公司与专项技术企业招聘入口

核验日：2026-10-13。**8 家企业、11 个已确认官方归属的入口，另保留 2 个候选入口。**这是[固定招聘清单](source-list.md)的创业与专项企业分表；互联网公司随后单独扩展为[26 家盘点范围](../../../references/company-coverage.md)，当前总计见主清单，避免沿用初版 16 家的小计。

2026-10-14扩充：面壁智能（社招及校园／实习）、百川智能、零一万物、商汤另列[基模与实验室分表](foundation-lab-sources.md)；科大讯飞保留待核候选。上方8家是首批分组小计，全部来源以[主清单](source-list.md)为准。

“AI 创业公司”“专项／成长型技术企业”是本轮采集分组，不是员工人数或融资阶段结论。本轮没有足够规模证据，`company_tier` 均保留 `unknown`。渠道表示入口支持的范围，不能替代具体岗位资格或在招核验；Zilliz 是全球补充来源，本轮未确认中国岗位。

## 已确认的入口

| source_id | 公司与官方入口 | 渠道 | 官方归属依据 | 实际读取范围 |
|---|---|---|---|---|
| `jobs-deepseek` | [DeepSeek](https://talent.deepseek.com/) | 社招、实习 | [官方证据](https://www.deepseek.com/)：官网 Join Us / Careers 直接链接 talent.deepseek.com；招聘目录将 Agent Harness 团队链接至 Moka high-flyer/140576 的同一 UUID。 | 官网归属、招聘目录与一个 Harness 多方向联合 JD 正文；未操作投递。 |
| `jobs-moonshot` | [月之暗面（Kimi）](https://careers.kimi.com/) | 社招、校招、实习 | [官方证据](https://www.kimi.com/news/kimi-global-hiring)：Kimi 官方招聘公告页脚直接链接 careers.kimi.com；招聘站“加入我们”链接 Moka moonshot/148506；页面标题为 Kimi社会招聘。 | 官网招聘公告、招聘主页、Moka 目录与一个 Agentic Commerce Engineer 完整职责和资格正文。 |
| `jobs-minimax` | [MiniMax](https://vrfi1sk8a0.jobs.feishu.cn/index/) | 社招、校招、实习 | [官方证据](https://minimax.cn/careers)：MiniMax 官网 careers 页面直接链接该飞书招聘域名，分别列 Top Talent、2027届校招、2028届实习与日常实习、社招。 | 官网项目入口、招聘目录与“大模型效率研究员-模型结构方向”的完整职责和资格正文。 |
| `jobs-zhipu-social` | [智谱](https://app.mokahr.com/social-recruitment/zphz/148983?locale=zh-CN#/) | 社招 | [官方证据](https://www.zhipuai.cn/zh/joinus)：官网 joinus 页面引用的公开 JS 中，“社会招聘”按钮 window.open 指向 zphz/148983；目标门户标题为北京智谱华章科技股份有限公司。 | 当前官网按钮目的地、招聘门户介绍及地点目录；社招具体 JD 未读。 |
| `jobs-zhipu-campus` | [智谱](https://app.mokahr.com/campus-recruitment/zphz/148984#/home) | 校招、实习 | [官方证据](https://www.zhipuai.cn/zh/joinus)：官网 joinus 页面公开 JS 的“校园招聘”按钮指向 zphz/148984；目标门户为同一公司校园招聘，目录含校招及实习。 | 官网归属、校园目录与“27届校招 GLM-Code Agent算法工程师”完整职责和资格；该岗位是本轮两条规范化 JD 之一。 |
| `jobs-stepfun-social` | [阶跃星辰（StepFun）](https://app.mokahr.com/social-recruitment/step/94904#/) | 社招 | [官方证据](https://www.stepfun.com/)：官网 HTML 引用的公开前端 JS 定义社会招聘链接 step/94904；目标页页脚为上海阶跃星辰智能科技股份有限公司，并链接校园门户。 | 官网入口、社招热招目录及 AI Safety 研究员完整职责和任职要求。 |
| `jobs-stepfun-campus` | [阶跃星辰（StepFun）](https://app.mokahr.com/campus-recruitment/step/94905) | 校招、实习 | [官方证据](https://www.stepfun.com/)：官网公开前端 JS 定义校园招聘链接 step/94905；目标页页脚为同一公司，导航含校园招聘、日常实习和 StepStar 项目。 | 官网入口与校园项目页；具体校园 JD 尚未读取。 |
| `jobs-dify` | [Dify / LangGenius](https://join.dify.ai/roles) | 实习 | [官方证据](https://dify.ai/about-us)：Dify 官网 Company→Join Us 直接指向 join.dify.ai；招聘页反链官网并标 LangGenius, Inc.。 | 官网→招聘站归属已核；Chrome 实读4岗目录与后端开发实习生完整JD。Jina roles 报 Unable to load roles，web 静态空列表，不代表关闭。 组织补证：官方条款明确LangGenius, Inc.以Dify品牌开展业务，非两家公司合并。 [事实表](../../../references/organization-lineage.md) |
| `jobs-pingkai-social` | [平凯星辰（北京）科技有限公司](https://careers.pingcap.com/apply/pingcap/39950/) | 社招 | [官方证据](https://pingkai.cn/join-us)：当前 pingkai.cn 加入我们页的社会招聘直接链接该门户，门户注明完整公司名称并反链旧官网 pingcap.cn。旧官网实际重定向到 pingkai.cn。 | 入口与招聘分类可读，具体岗位列表未展开；urllib/web 直连门户出现重定向循环，Jina 分类页可读。官网共用事业和校园两门户，身份分开。 |
| `jobs-pingkai-campus` | [平凯星辰（北京）科技有限公司](https://campus.pingcap.com/campus_apply/pingcap/39951/) | 校招、实习 | [官方证据](https://pingkai.cn/join-us)：当前官网校园招聘链接该门户，官网明确面向应届毕业生与实习生；社招与校园门户相互链接且公司主体一致。 | 门户归属、校园/实习渠道及分类计数可读；仅见其他共1个职位，不代表已取得完整JD或核实在招。 |
| `jobs-zilliz` | [Zilliz](https://zilliz.com/careers) | 未确认 | [官方证据](https://zilliz.com.cn/careers)：中文官网页脚招聘入口链接 zilliz.com/careers；全球招聘页 HTML 的具体岗位直接链接 jobs.lever.co/zilliz。中文站页脚注明上海赜睿信息科技有限公司。 | 中文招聘页可读但呈空列表；全球招聘 HTML 列11岗，地点东京/纽约/西雅图/Redwood City/Austin，本轮没有确认中国岗位。只做补充全球来源，不计入中国在招样本。 |

## 保留候选

以下入口还未纳入已确认官方来源数；写入用户 watchlist 时保持 `candidate`。可以继续核实，但不把其中旧项目或岗位摘要算作当前招聘样本。

| source_id | 候选入口 | 待核实原因 |
|---|---|---|
| `jobs-siliconflow-liepin` | [硅基流动（SiliconFlow）](https://m.liepin.com/company/21146791/) | 需读到猎聘营业执照认证主体并与官网核对，或找到官网/确认官方公众号指向该招聘主页的链接；公司名称与岗位列表一致不足以替代归属确认。 |
| `jobs-jina-dover` | [Jina AI（Dover 旧招聘目录，待复核）](https://app.dover.com/jobs/jinaai) | 旧项目日期、当前官网 Elastic 品牌与旧 Dover 目录之间缺少现时官方归属/招聘有效性证据；下轮优先从当前官网或 Elastic 官方招聘查证。 |

## 本轮跑通的获取路径

- **Dify**：官网指向招聘站；Jina 报目录加载失败，Chrome 实际打开 4 个中国岗位并读取后端实习完整 JD。保留阅读器失败与浏览器成功两份证据，未投递。
- **智谱**：当前官网按钮指向 Moka，搜索仍能命中旧飞书入口。沿新门户读取 GLM-Code Agent 校招完整 JD，正文完整但未确认投递状态，岗位状态为 `unknown`。
- **平凯星辰**：当前官网与旧 PingCAP 中国招聘域名仍有明确互链，按实际招聘法律主体记录；分类计数不作为完整 JD。
- **旧招聘目录和第三方平台候选**不因同名、页面存在或历史项目可读就自动启用。新增与复查使用[清单维护](tracking.md#来源清单与扩充)，保留已有用户选择和来源 ID。

首次使用只选择与目标地区、渠道和方向相关的入口。这里的公开清单不直接启动完整采集或后台日程。
