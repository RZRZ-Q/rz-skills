# 芯片、IC与计算平台招聘入口

2026-10-14 系统补充见[逐公司研究与工程团队清单](../_shared/references/team-inventory.md)：逐一排查83个主体，包含最新新增入口、公司级缺口和读取边界；下表保留原批次核验范围。

核验日期：2026-10-14。40 个已确认入口、1 个候选；覆盖 24 家至少有一个已确认入口的公司。同公司多入口不重复计公司。

覆盖 AI／GPU 计算、移动与汽车 SoC、IP／EDA、晶圆制造和存储。检索时分开 AI 软件、编译器／Kernel／驱动、嵌入式、RTL／验证、物理设计、模拟电路、工艺与器件；通用大模型项目不能自动作为所有 IC 岗的准备建议。具体要求由后续完整 JD 决定。

渠道“已核”指入口／项目有依据，不代表已采到该渠道完整 JD 或岗位目前开放。候选不计入官方覆盖；“未核”不等于没有。当前启用状态以用户 watchlist 为准。

## 已确认入口

| source_id | 公司／团队与入口 | 渠道／待核线索 | 官方归属依据 | 实际读取与边界 |
|---|---|---|---|---|
| `jobs-nvidia` | [NVIDIA](https://jobs.nvidia.com/careers) | 实习、校招 | [依据1](https://www.nvidia.cn/about-nvidia/careers/university-recruiting/) NVIDIA 中国官网链接 jobs.nvidia.com/careers，并明确 Intern 与 New College Graduate 申请筛选。 | 招聘目录及职位类型可读；已读中国2027软件工程NCG职责和资格全文，为多方向汇总条目。实习渠道已核，中国实习具体岗位未核；社招仅见Regular Employee雇佣类型，渠道待核。 地区：全球来源；中国2027 NCG正文已确认；中国实习岗位待核，社招渠道待核 |
| `jobs-amd` | [AMD](https://careers.amd.com/) | 社招 | [依据1](https://careers.amd.com/) AMD 官方子域名招聘站；上海职位 89398 的职责、学历及工作经验正文可读。 | 已读上海 AI Software Engineer 89398 完整 JD，硕士/博士且 5+ 年专业经验，vLLM/SGLang、分布式推理、GPU Kernel、LLVM/ROCm；Web Reader 403，Jina 正文成功。 地区：全球来源；中国上海社招岗位已确认 |
| `jobs-amd-students` | [AMD](https://careers.amd.com/students/) | 实习、校招 | [依据1](https://www.amd.com/en/corporate/careers/student-programs/regional-programs.html) AMD 官方学生项目页面包含 Internship/Co-op、New Grad；官方区域页单独说明 China 实习项目。 | 学生入口可读，China 春季/秋季实习项目说明可读；中国具体 new-grad JD 尚未核验。 地区：全球学生入口；中国实习项目已确认，校招具体地区待岗位级验证 |
| `jobs-hisilicon` | [华为 / 海思](https://www.hisilicon.com/cn/about-us/career) | 校招、实习、社招 | [依据1](https://www.hisilicon.com/cn/about-us/career) 海思官网人才招聘明确分别链接华为 campus-recruitment.html 与 social-recruitment.html。 | 海思自身入口已核；下游是华为共享招聘门户，校招页包含应届生和实习生。列表动态，未确认某个海思岗位；不得将华为全站职位自动归属海思。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-cambricon-campus` | [寒武纪](https://app.mokahr.com/campus-recruitment/cambricon/44201) | 校招、实习 | [依据1](https://www.cambricon.com/) 公司当前官网“校园招聘”直接链接该 Moka 站。 | 当前栏目可读：2027 届校园招聘、日常实习生招聘、2027 届实习生招聘；页面计数是目录观察，不是去重入库岗位数。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-cambricon-social` | [寒武纪](https://app.mokahr.com/m/apply/cambricon/1113) | 社招 | [依据1](https://www.cambricon.com/) 公司当前官网“社会招聘”直接链接该 Moka 站。 | 官网回链已核；直连目标遇 302 重定向循环，本轮未读社招列表及完整 JD。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-mthreads` | [摩尔线程](https://mthreads.zhiye.com/) | 校招、实习、社招 | [依据1](https://www.mthreads.com/jobs) 摩尔线程官网链接 zhiye 招聘站 social 与 campus；该站当前导航含实习生职位。 | 官方关联与三渠道导航可读；当前校招正文可读，未读单个岗位详情。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-biren-social` | [壁仞科技](https://app.mokahr.com/social-recruitment/biren/44726) | 社招 | [依据1](https://www.birentech.com/join/) 壁仞官网加入我们页直接链接该 Moka 社招站。 | 官网回链已核；直连目标重定向循环，未读社招列表；实习渠道尚未确认。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-biren-campus` | [壁仞科技](https://app.mokahr.com/campus-recruitment/biren/44727) | 校招 | [依据1](https://www.birentech.com/join/) 壁仞官网加入我们页直接链接该 Moka 校招站。 | 校招分类可读：芯片研发、软件、管理与研发支持；未读单个 JD；未找到明确实习入口。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-metax-social` | [沐曦](https://recruitment.metax-tech.com/social-recruitment/metax-tech/58147) | 社招 | [依据1](https://www.metax-tech.com/join.html) 沐曦官网社会招聘直链自有域名招聘子站。 | 官方回链已核；直连重定向循环，社招详情未读。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-metax-campus` | [沐曦](https://recruitment.metax-tech.com/campus-recruitment/metax-tech/58131) | 校招 | [依据1](https://www.metax-tech.com/join.html) 沐曦官网校园招聘直链自有域名招聘子站。 | 校园目录可读 AI、GPGPU 驱动、性能工具、SRE 等标题；渠道取入口，不根据标题猜候选资格。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-metax-intern` | [沐曦](https://app.mokahr.com/campus-recruitment/metax-tech/170510?locale=zh-CN) | 实习 | [依据1](https://recruitment.metax-tech.com/campus-recruitment/metax-tech/58131) 官网关联校园门户导航“实习生招聘”明确指向该 Moka 站。 | 实习职位列表可读，含 AI 推理优化、GPU 编译器、GPU 体系结构研究、GPU 验证和 Agentic AI 工程师（长沙实习）；未读取这些职位的完整 JD。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-enflame-social` | [燧原科技](https://app.mokahr.com/apply/enflame/40891) | 社招 | [依据1](https://www.enflame-tech.com/careers) 当前官网 careers 页“社会招聘”直链此 Moka 入口。 | 已核官网导航；直连目标重定向循环，列表与 JD 未读。旧 /joinus 为 WAF 页面，未用它推断停止招聘。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-enflame-campus` | [燧原科技](https://app.mokahr.com/campus-recruitment/enflame/168420?locale=zh-CN) | 校招 | [依据1](https://www.enflame-tech.com/careers) 当前官网 careers 页“校园招聘”直链此 Moka 入口。 | 已核官网导航；直连目标重定向循环，列表与 JD 未读。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-enflame-intern` | [燧原科技](https://app.mokahr.com/campus_apply/enflame/69993) | 实习 | [依据1](https://www.enflame-tech.com/careers) 当前官网 careers 页“实习生招聘”直链此 Moka 入口。 | 已核官网导航；直连目标重定向循环，列表与 JD 未读。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-kunlunxin` | [昆仑芯](https://kunlunxin1.zhiye.com/) | 校招、实习、社招 | [依据1](https://www.kunlunxin.com/) 昆仑芯当前官网“加入我们”直链 kunlunxin1.zhiye.com。 | 当前站三渠道导航已核，列表未完整读取。搜索可命中旧 kunlunxin.zhiye.com 且混入百度其他业务，旧站不加入本次清单，不把这些职位归属昆仑芯。 地区：中国大陆；具体岗位地点尚未逐岗核验 组织补证：前身百度智能芯片及架构部；2021-06-24官方公告成立独立公司，当前法律名为股份有限公司，变更日期／股比未核。 [事实表](../_shared/references/organization-lineage.md) |
| `jobs-horizon-social` | [地平线](https://wecruit.hotjob.cn/SU64819a4f2f9d2433ba8b043a/pb/social.html) | 社招 | [依据1](https://www.horizon.auto/about?tp=4) 地平线当前官网加入我们区直链该 hotjob 社招入口。 | 官网回链与社招标签可读；招聘目标直连返回 405，未采列表/详情。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-horizon-campus` | [地平线](https://wecruit.hotjob.cn/SU6409ef49bef57c635fd390a6/pb/school.html) | 校招 | [依据1](https://www.horizon.auto/about?tp=4) 地平线当前官网加入我们区直链该 hotjob 校招入口。 | 官网回链与校招标签可读；招聘目标直连返回 405，未采列表/详情。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-horizon-intern` | [地平线](https://wecruit.hotjob.cn/SU6409ef49bef57c635fd390a6/pb/interns.html) | 实习 | [依据1](https://www.horizon.auto/about?tp=4) 地平线当前官网加入我们区直链该 hotjob 实习入口。 | 官网回链与实习标签可读；招聘目标直连返回 405，未采列表/详情。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-blacksesame` | [黑芝麻智能](https://bsthr.zhiye.com/) | 校招、实习、社招 | [依据1](https://www.blacksesame.com/zh/join-us/) 黑芝麻官网当前“加入我们”导航链接 bsthr.zhiye.com。 | 新招聘站三渠道导航与招聘邮箱可读；单个当前 JD 未读。官网旧静态页面含 2022 年岗位，不作为当前招聘机会。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-semidrive-social` | [芯驰科技](https://app.mokahr.com/apply/semidrive/42940) | 社招 | [依据1](https://www.semidrive.com/) 芯驰当前官网首页“加入我们”直接链接该 Moka 社招入口。 | 社招公司介绍可读，列表未读；外部转载 /career 目前 404，不使用该旧路径。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-rockchip-social` | [瑞芯微](https://hr.rock-chips.com/social-recruitment/) | 社招 | [依据1](https://www.rock-chips.com/) 瑞芯微首页“人力资源”指向自有 hr 子域名社招门户。 | 当前城市/职位分类可读，软件、算法、IC、硬件分别列示；未读完整 JD。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-rockchip-campus` | [瑞芯微](https://hr.rock-chips.com/campus-recruitment) | 校招、实习 | [依据1](https://hr.rock-chips.com/social-recruitment/) 已由官网验证的社招门户导航明确链接当前校园门户。 | 校招地点与类别计数可读；明确有“实习岗位”栏目，当前未展示实习条目，不能宣称有开放实习岗位。旧静态校招页不替代当前岗位。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-gigadevice-social` | [兆易创新](https://app.mokahr.com/social-recruitment/gigadevice/100227) | 社招 | [依据1](https://www.gigadevice.com.cn/about/career) 兆易创新官网加入我们页“社会招聘”直链此 Moka 站。 | 官网回链已核；直连目标重定向循环，社招列表/详情未读。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-gigadevice-campus` | [兆易创新](https://app.mokahr.com/campus-recruitment/gigadevice/92215) | 校招 | [依据1](https://www.gigadevice.com.cn/about/career) 兆易创新官网加入我们页“校园招聘”直链此 Moka 站。 | 校招部门栏目可读，包括中央研究院、Flash/DRAM/MCU/PMU 等。中央研究院是部门筛选，不是独立 Lab 官网；实习渠道未确认。 地区：中国大陆；具体岗位地点尚未逐岗核验 |
| `jobs-intel` | [Intel](https://jobs.intel.com/page/show/search-results) | 实习 | [依据1](https://www.intel.com/content/www/us/en/support/articles/000021775/programs/jobs-at-intel.html) Intel 官方支持文档直接链接 jobs.intel.com 搜索页，并明确 Intern/Student 筛选。 | 官方实习流程和搜索入口已确认；目标 jobs 根站直连403，/en读取空白，未核当前校招/社招栏目及中国具体岗位。官方域名关系确定，不把读取失败写为招聘关闭。 地区：全球入口；中国具体地区与三渠道在招状态未核 |
| `jobs-qualcomm` | [Qualcomm](https://careers.qualcomm.com/careers) | 待核 | [依据1](https://www.qualcomm.com/company/careers) Qualcomm 官方 Careers 页 Search open positions 直接链接该招聘子域名。 | 官方全球工作搜索入口已核；本轮未读目标列表与中国岗位。 渠道保留 unknown，社招待核。 地区：全球入口；中国地区具体机会待筛选 |
| `jobs-qualcomm-students` | [Qualcomm](https://www.qualcomm.com/company/careers/internships-and-early-in-career-opportunities) | 实习 | [依据1](https://www.qualcomm.com/company/careers/internships-and-early-in-career-opportunities) 官方学生页明确提供 Intern 筛选、Early in Career 说明及 APAC 分区。 | 明确实习项目；Early in Career 没有核到与应届资格对应的独立栏目，暂不将其计入确认校招渠道。APAC不自动等于中国当前招聘。 地区：全球项目入口；中国及应届资格待岗位级核验 |
| `jobs-mediatek` | [MediaTek（联发科技）](https://careers.mediatek.com/zh-cn) | 实习 | [依据1](https://www.mediatek.com/zh-cn/company/careers) MediaTek 官网职业机会链接 careers.mediatek.com；官方实习说明含 China 地区。搜索索引中的 2027 Campus 只保留待核线索。 | 官方中文门户与大陆地区入口可读；实习项目有 China 说明，但未确认当前大陆实习岗位。校招仅有官方域搜索索引的 2027 Campus 条目（HsinChu，非大陆），详情重定向循环，列待核；社招无明确渠道或工作年限证据。 地区：全球/两岸入口；大陆地区栏目确认，Campus待核索引样本位于新竹，不能计作大陆校招 |
| `jobs-verisilicon` | [芯原](https://www.verisilicon.com/cn/Careers) | 社招 | [依据1](https://www.verisilicon.com/cn/Careers) [依据2](https://www.verisilicon.com/cn/RecruitOpen) 芯原官方加入我们页面区分中国大陆、海外开放职位和投递渠道。；官方职位页正文明确标注“社会招聘”；用于渠道确认。 | 官网加入我们正文可读；RecruitOpen 正文明确“社会招聘”，本轮保存的 Jina 正文显示154条结果，另有部分动态读取曾显示0；不以单次计数判断招聘总量，未逐项核验当前岗位。 地区：中国大陆入口与海外入口分列 |
| `jobs-verisilicon-campus` | [芯原](https://www.verisilicon.com/recruit/RecruitCampus.html) | 校招 | [依据1](https://www.verisilicon.com/cn/Careers) 官方 Careers 页校园招聘直链此自有站点，该页进一步链接 campus.51job.com/VeriSilicon2027。 | 2027 校招入口已核；正文保留部分2023旧内容，不把所有页面文字都当本届条件；实习渠道未确认。 地区：中国大陆校招入口；海外学校资格以具体项目为准 |
| `jobs-smic` | [中芯国际](https://smics.zhiye.com/) | 社招、校招 | [依据1](https://www.smics.com/site/human) 当前简中官网招贤纳士、社招、校招与海外招聘均直接链接 smics.zhiye.com。 | 当前北森站导航可读；实习渠道未确认。繁中旧页仍指旧hotjob/51job，不作为本轮主入口。 地区：中国大陆主入口；海外招聘单独栏目 |
| `jobs-ymtc` | [长江存储](https://ymtc.zhiye.com/) | 社招、校招 | [依据1](https://www.ymtc.com/cn/joinus.html) 长江存储官网加入我们页直接链接 ymtc.zhiye.com/social/jobs 与 /campus/jobs。 | 官网社招/校招回链已核；目标动态正文未读。检索出现独立 ymtc-campus.zhiye.com，尚未找到当前官网关联，未擅自另加正式来源；实习渠道未确认。 地区：中国大陆招聘入口；具体地点和资格未逐岗核验 |
| `jobs-cxmt` | [长鑫存储](https://cxmt.zhiye.com/) | 社招、校招、实习 | [依据1](https://www.cxmt.com/join.html) 长鑫官网当前导航直链 cxmt.zhiye.com 社招/校招，正文明确实习招聘；目标站含实习生招聘栏目。 | 三渠道导航可读；当前读取首页卡片显示各类共0职位，未验证筛选/动态加载是否完整，不能据此断言公司没有岗位。 地区：中国大陆招聘入口；具体岗位地点尚未核验 |
| `jobs-empyrean` | [华大九天](https://app.mokahr.com/social-recruitment/empyrean/118495?locale=zh-CN) | 社招 | [依据1](https://www.empyrean.com.cn/article/job-list.html) 华大九天官网招聘信息导航明确链接该 Moka 租户。 | 当前Moka入口与研发/测试/产品等分类可读；未读具体JD，旧官网职位页不代替当前列表。 地区：中国大陆招聘入口 |
| `jobs-empyrean-campus` | [华大九天](https://app.mokahr.com/su/10Uakw) | 校招 | [依据1](https://app.mokahr.com/social-recruitment/empyrean/118495?locale=zh-CN) 官网已关联的社招门户“校招职位”图片及链接指向此Moka短链接。 | 目标标题为华大九天校园招聘，分类可读；保留官方短链接，未猜测展开路径；实习渠道未确认。 地区：中国大陆校园入口 |
| `jobs-synopsys-china` | [Synopsys](https://careers.synopsys.com/China) | 待核 | [依据1](https://careers.synopsys.com/China) Synopsys 官方招聘子域名中国页面，提供 View All China Jobs 与全球职位搜索。 | 中国入口可读，但当前页面显示无可用职位；这是该页本次观察，不能外推公司中国招聘整体关闭。未读具体JD。 渠道保留 unknown，社招待核。 地区：中国入口已确认；本次地区页为空结果 组织补证：2025-07-17完成Ansys收购，Ansys为全资子公司；该事实不扩展本行招聘覆盖。 [事实表](../_shared/references/organization-lineage.md) |
| `jobs-synopsys-students` | [Synopsys](https://careers.synopsys.com/early-careers) | 实习 | [依据1](https://careers.synopsys.com/early-careers) 官方 Early Careers 页面明确 Internship/Industrial Placement 及 China intern roles 入口。 | 全球实习项目与中国实习筛选已核；本次 China 显示0 intern roles。Early Careers 未核到独立应届资格项目，暂不计确认校招。 地区：全球项目与中国实习入口；当前中国卡片0结果 组织补证：Ansys收购完成不改变本条校园／实习核验边界。 [事实表](../_shared/references/organization-lineage.md) |
| `jobs-cadence` | [Cadence](https://cadence.wd1.myworkdayjobs.com/External_Careers) | 待核 | [依据1](https://www.cadence.com/en_US/home/company/life-at-cadence/careers.html) Cadence 当前 Careers 正文多处 Explore Jobs 明确指向 Workday External_Careers。 | 当前官网职业页和外部招聘关联可读；Workday岗位列表未读取；旧 /company/careers.html 出现403，不据此否定新的可读入口。 渠道保留 unknown，社招待核。 地区：全球入口；中国地区具体岗位未核 |
| `jobs-cadence-students` | [Cadence](https://cadence.wd1.myworkdayjobs.com/Univ_Careers) | 实习、校招 | [依据1](https://www.cadence.com/en_US/home/company/careers/interns-and-new-grads.html) Cadence 官方 Interns and New Grads 页明确链接 Workday Univ_Careers，并区分全球入口与美国专项入口。 | 全球实习与应届入口已核；未读Workday列表。美国 University_Talent 专项不混入中国渠道。 地区：全球学生入口；中国具体开放职位未核 |

## 待核候选

| source_id | 公司／团队与入口 | 渠道／待核线索 | 官方归属依据 | 实际读取与边界 |
|---|---|---|---|---|
| `jobs-semidrive-campus-candidate` | [芯驰科技](https://app.mokahr.com/campus_apply/semidrive/42941) | 校招、实习 | [依据1](https://app.mokahr.com/campus_apply/semidrive/42941) 候选校招页可读、同租户 semidrive，并链接已由官网验证的社招站；本轮未取得官网/官方社招页指向此校招站的正向回链，因此暂留候选。 | 校招职位列表可读数字 IC 设计/验证、STA、嵌入式软件、FAE；存在实习岗位栏目但无具体实习岗位，不能宣称实习在招。待补官方正向关联。 地区：中国大陆；具体岗位地点尚未逐岗核验 |

## 三渠道覆盖

| 公司／机构 | 实习 | 校招 | 社招 |
|---|---|---|---|
| NVIDIA | 入口已核 | 入口已核 | 未核 |
| AMD | 入口已核 | 入口已核 | 入口已核 |
| 华为 | 入口已核 | 入口已核 | 入口已核 |
| 寒武纪 | 入口已核 | 入口已核 | 入口已核 |
| 摩尔线程 | 入口已核 | 入口已核 | 入口已核 |
| 壁仞科技 | 未核 | 入口已核 | 入口已核 |
| 沐曦 | 入口已核 | 入口已核 | 入口已核 |
| 燧原科技 | 入口已核 | 入口已核 | 入口已核 |
| 昆仑芯 | 入口已核 | 入口已核 | 入口已核 |
| 地平线 | 入口已核 | 入口已核 | 入口已核 |
| 黑芝麻智能 | 入口已核 | 入口已核 | 入口已核 |
| 芯驰科技 | 仅候选线索 | 仅候选线索 | 入口已核 |
| 瑞芯微 | 入口已核 | 入口已核 | 入口已核 |
| 兆易创新 | 未核 | 入口已核 | 入口已核 |
| Intel | 入口已核 | 未核 | 未核 |
| Qualcomm | 入口已核 | 未核 | 未核 |
| MediaTek（联发科技） | 入口已核 | 未核 | 未核 |
| 芯原 | 未核 | 入口已核 | 入口已核 |
| 中芯国际 | 未核 | 入口已核 | 入口已核 |
| 长江存储 | 未核 | 入口已核 | 入口已核 |
| 长鑫存储 | 入口已核 | 入口已核 | 入口已核 |
| 华大九天 | 未核 | 入口已核 | 入口已核 |
| Synopsys | 入口已核 | 未核 | 未核 |
| Cadence | 入口已核 | 入口已核 | 未核 |

## 继续核查与衔接

海思使用华为主体并标记团队；IC研究院、部门筛选不另算公司或独立实验室。按本轮目标地区筛选全球招聘站并核对工作资格；无岗位结果和页面未加载分别记录。历史招聘正文只证明曾有该岗位，不能证明今天仍招。NVIDIA中国2027软件NCG、AMD上海AI工程岗位已用于正文可读性核验，未新增账本观察。

新增、暂停、迁移与幂等合并按[清单维护](tracking.md#来源清单与扩充)执行；总目录见[固定来源清单](source-list.md)。
