# 固定招聘来源清单

2026-10-14 系统补充见[逐公司研究与工程团队清单](../../../references/team-inventory.md)：逐一排查83个主体，包含最新新增入口、公司级缺口和读取边界；下表保留原批次核验范围。

这是一份随技能分发的入口种子表，供建立或扩充用户的 watchlist。**当前已确认范围为 79 家公司、2 家独立研究机构，156 个已确认入口、10 个候选入口（共 166 条来源）。**原互联网／创业清单核验日为2026-10-13；本次团队与行业扩充核验日为2026-10-14。公司、团队、门户分别计数，候选不计入已确认企业覆盖。入口核实不代表完整JD已经采集或岗位当前开放。

`source_id` 标识招聘门户或有实际招募内容的团队入口，`company` 标识所属公司／机构，`team` 标识团队；独立研究机构另记组织类型。同一门户的搜索页、城市／部门筛选和具体岗位不另建来源 ID。渠道列表示有证据支持的入口范围，资格与在招状态仍须逐岗核验。固定清单保存核验快照，是否启用、暂停或仅保留为候选，由用户工作目录的 watchlist 决定。

## 分表导航

| 范围 | 清单 |
|---|---|
| 互联网平台 | 本页原8家13入口与[互联网扩展表](large-internet-sources.md)合计26家公司、49个已核入口 |
| 早期创业／专项企业分组 | [原8家11入口](startup-growth-sources.md)，另2候选；此为首批子集，不是AI创业公司全集 |
| 基模公司、公司研究组与独立实验室 | [基模与实验室分表](foundation-lab-sources.md)，含面壁、百川、零一万物、商汤及公司专项团队 |
| 具身智能与机器人 | [具身分表](embodied-sources.md)，保留公司、模型团队、控制与硬件方向的区别 |
| 芯片、IC与计算平台 | [芯片与IC分表](chip-ic-sources.md)，含GPU、SoC、IP/EDA、制造和存储 |

跨流程衔接见[ai-career覆盖总览](../../../references/company-coverage.md)。总量按用户清单读回去重，原有团队再次出现在分表不增加公司数。

## 基础来源

| source_id | company | 官方入口与用途 | 渠道 | 归属／渠道证据 | 实际核验范围与边界 |
|---|---|---|---|---|---|
| `jobs-alibaba-campus` | 阿里巴巴 | [阿里校招门户](https://campus-talent.alibaba.com/campus/index)，按业务与招聘项目发现岗位 | 校招、实习 | 阿里官方域名；同站[实习岗位](https://campus-talent.alibaba.com/campus/position/199907160001)与[校招岗位](https://campus-talent.alibaba.com/campus/position/199907640058)已于同日完整采集 | 本次 web／Jina 只返回标题和空正文；此前具体 JD 已读。下轮用动态页面读取，不把入口空白当作无岗位 |
| `jobs-alibaba-tongyi` | 阿里巴巴 | [Token Foundry 招聘](https://careers-tongyi.alibaba.com/)，针对 Qwen／Token Foundry 团队发现岗位 | 社招；其他渠道须另核 | 门户正文标明 Token Foundry 与阿里关系，页脚为通义实验室；同站[社招岗位](https://careers-tongyi.alibaba.com/off-campus/position-detail?positionId=7000031308&lang=zh)已采集 | Jina 读到团队介绍与招聘联系信息；web 超时。仅代表该团队，不代表阿里全部社招 组织补证：2026-04-08通义升级，6月8日与原淘天未来生活实验室合并ATF；应用侧千问事业部另列。 [事实表](../../../references/organization-lineage.md) |
| `jobs-bytedance` | 字节跳动 | [字节招聘门户](https://jobs.bytedance.com/)，进入校园／社招目录 | 校招、实习、社招 | 官方域名；同站[校招](https://jobs.bytedance.com/campus/position/7676056716118755637/detail)、[实习](https://jobs.bytedance.com/campus/position/7537986474445113607/detail)、[社招](https://jobs.bytedance.com/experienced/position/7517205893478451464/detail)已于同日采集 | 本次 web 空正文、Jina 超时；此前 Chrome 成功读取具体 JD。保留入口，复用浏览器路径 |
| `jobs-tencent-campus` | 腾讯 | [腾讯校招](https://join.qq.com/)，校园项目与岗位目录 | 校招、实习 | 官方 qq.com 域名；同站[校招](https://join.qq.com/post_detail.html?postid=1282707395466077184)、[实习](https://join.qq.com/post_detail.html?postid=1200889496565214208)已采集 | 本次 web／Jina 标题可见、正文为空；此前公开前端接口读到 JD，但三份校园样本在招状态仍为 unknown |
| `jobs-tencent-social` | 腾讯 | [腾讯招聘](https://careers.tencent.com/)，社会招聘目录 | 社招 | Jina 读取到 Tencent Careers 及腾讯版权信息；同站[社招岗位](https://careers.tencent.com/jobdesc.html?postId=2061654749727600640)已采集 | Jina 读到首页和 Find jobs；本次未遍历职位列表。中英文路径可能指向同岗，按岗位 ID 去重 |
| `jobs-meituan` | 美团 | [美团招聘](https://zhaopin.meituan.com/)，首页进入社招、校园与专项项目 | 校招、实习、社招 | Jina 首页直接列出[社招](https://zhaopin.meituan.com/web/social)与[校园](https://zhaopin.meituan.com/web/campus)；同站[实习岗位](https://zhaopin.meituan.com/web/position/detail?jobUnionId=4555593816)已采集 | Jina 读到招聘项目导航，web 超时；此前具体 JD 经公开前端接口读取。不同项目的届别、时间要求分别核实 |

## 原扩展来源

以下四家公司入口已在后续 26 家盘点中纳入当前用户清单，复用同日核验，不伪装成重新读取。其中小米已在后续 Agent／评测采集中取得6份完整JD；下表其他正文边界仍按原核验记录，不把入口盘点量计入岗位样本。其他用户仍按自己的范围选用。

| source_id | company | 官方入口与用途 | 渠道 | 归属／渠道证据 | 实际核验范围与边界 |
|---|---|---|---|---|---|
| `jobs-baidu-campus` | 百度 | [百度校园招聘](https://talent.baidu.com/jobs/)，校招与实习项目目录 | 校招、实习 | 百度 talent 官方子域名，正文标明百度集团校园项目；[公司招聘页](https://home.baidu.com/jobs/jobs.html)也指向该域名 | web 读到校招、AIDU 和实习项目说明；Jina 空正文。旧公司链接仍指向旧版 campus.html，不把旧地址当新增门户 |
| `jobs-baidu-social` | 百度 | [百度社会招聘](https://talent.baidu.com/external/baidu/index.html#/social/2)，社会招聘目录 | 社招 | [百度公司招聘页](https://home.baidu.com/jobs/jobs.html)的“社会招聘”直接链接此路径 | 公司页正文及链接已读；目标页面 web 仅标题，职位列表未读。保留 hash 路由，不据空白判断职位数 |
| `jobs-kuaishou-social` | 快手 | [快手招聘](https://zhaopin.kuaishou.cn/)，社会招聘与日常实习目录 | 社招、实习 | Jina 页脚为北京快手科技有限公司；导航直接列出“社会招聘”“日常实习”及校招链接 | Jina 读到导航和归属，web 只返回需启用 JavaScript；未读取具体 JD |
| `jobs-kuaishou-campus` | 快手 | [快手校招](https://campus.kuaishou.cn/recruit/campus/e/#/campus/index/)，校园项目目录 | 校招、实习 | [快手招聘首页](https://zhaopin.kuaishou.cn/)直接链接此校园入口，目标页注明官方招聘平台 | 根域名读取仅品牌简介；沿官方完整路径用 Jina 读到应届／实习导航，未读到具体 JD。根域名是同门户别名，不重复建源 |
| `jobs-jd-social` | 京东 | [京东招聘](https://zhaopin.jd.com/)，进入[社会招聘目录](https://zhaopin.jd.com/web/job/job_info_list/3) | 社招；校招／实习转校园门户 | 官方 jd.com 子域名，首页含京东版权与校招／实习站内导航 | web 读到首页职位摘要和社招导航；社招目录只有筛选框，本次没有完整 JD。重定向的 jsessionid 不进入固定 URL |
| `jobs-jd-campus` | 京东 | [京东校招](https://campus.jd.com/)，校园及实习项目入口 | 校招、实习 | [京东招聘首页](https://zhaopin.jd.com/)的“校园招聘”“实习生招聘”均链接此门户 | 归属和渠道导航已读；目标页 web／Jina 空正文。搜索索引里的项目介绍仅作线索 |
| `jobs-xiaomi` | 小米 | [小米招聘](https://hr.xiaomi.com/)，[职位目录](https://hr.xiaomi.com/website/opportunities.html)与[校园项目](https://hr.xiaomi.com/website/campus.html) | 校招、实习、社招 | [小米官网](https://www.mi.com/about/join)页脚直接链接招聘站；职位目录有社招／校招／实习筛选 | Jina 读到招聘首页；web 读到职位目录筛选、校园流程，动态职位数未加载。搜索索引与直接读取的项目正文不一致，届别和具体岗位待实时核验 |

## 使用与扩充

- 把本轮选中的来源 ID、入口、公司和渠道写进工作目录的 watchlist；用户已有取舍优先。来源清单升级不能覆盖个人暂停项、地区或方向偏好。
- 新增公司时，从公司官网“加入我们”、已确认官方账号或招聘系统的认证主体验证归属；记录入口、渠道、实际读取方式、核验日期及边界。只发现搜索摘要时先作为候选，不标记为可采完整 JD。
- 优先补当前未覆盖的公司类型、团队或招聘渠道。同一站的备用网址、新版路径迁移记为原来源的别名；新门户或有独立招募内容的团队入口才增加稳定 ID。保留变更原因，不因一次访问失败删除来源。
- 任务包含岗位采集时，从已启用来源读取具体 JD，按本轮覆盖表记录成功数和空缺。入口发现、来源纳入、完整 JD 新增是三件不同的事；每轮报告分别计数。

此清单不保证长期可读，也不表示后台已运行。使用时复查入口和实际读取结果，详细执行与证据要求见 [岗位发现](discovery.md) 和 [持续追踪](tracking.md)。
