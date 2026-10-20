# 大厂技术公众号固定清单

首轮核验日：2026-10-13；最近复核：**2026-10-16**。当前关注清单有 **43 个公众号来源：40 个具备官方关联证据（含历史运营或官网入口），3 个候选**。最近复核此前剩余 7 个候选，4 个升级、3 个继续待核，未新增账号，见[七项候选复核](#2026-10-16-七项候选复核)。官方关联、当前显示名、同号关系、平台认证和正文可读性分别记录。固定表是种子来源，实际启用范围仍由用户 watchlist 决定；各来源的公开身份依据与未决关系列在下表。

`official_linked` 表示官网或官方运营说明建立了关联。以下可读性是 2026-10-13 的观察：当时未读取微信平台认证主体，也未取得可遍历的微信历史目录，4 条代表原链均遇验证页。实际采集按[搜狗发现与浏览器正文读取路径](collection.md#公众号发现与正文读取)重查，不将历史访问结果当作永久状态，也不将官方社区文章默认视为公众号全文镜像。

## 账号与身份依据

| source_id / 公众号 | 已核标识 | 官方身份入口 | 日期与边界 |
|---|---|---|---|
| `meituan-tech-wechat` / 美团技术团队 | 微信号 `meituantech`；`biz` 未知 | [美团技术团队 About](https://tech.meituan.com/about.html) 明示博客与微信公众号 | About 未标发布日期；本轮可读。[评测白皮书](https://tech.meituan.com/2026/09/10/Agent-Evaluation-White-Paper-01.html)另有微信文章链接。 |
| `tencent-teg-wechat` / 腾讯技术工程 | 微信号 `Tencent_TEG`；`biz` 未确认 | [腾讯高校合作介绍](https://cloud.tencent.com/developer/article/1146898)明确称官方公众号；[腾讯大讲堂](https://cloud.tencent.com/developer/article/1154690)给出 ID | 关系说明来自 2018 年；社区作者职业认证不等于微信主体认证。第三方索引的 `biz` 只保留为候选，不以显示名确认。 |
| `alibaba-developer-wechat` / **阿里云开发者（当前页面名：千问AI平台）** | `biz=MzIzOTU0NTQ0MA==`；微信号未知；历史官方名“阿里云开发者”，搜索索引名“阿里开发者” | [阿里云开发者运营介绍](https://developer.aliyun.com/article/1354081)于 2023-10-19 说明公众号关系并链接同 `biz` 文章；[阿里云开发者搜索入口](https://weixin.sogou.com/weixin?type=2&query=阿里云开发者)；[题名搜索入口](https://weixin.sogou.com/weixin?type=2&query=自动化评测的九九归一) | 2026-10-15 实际页面《自动化评测的九九归一——评测agent》显示“千问AI平台”，与官网历史链接同 `biz`；保留“阿里云开发者”为显式检索名称，沿用同一来源 ID，不重复计账号。仅确认同号连续关系，更名生效日期及当前认证主体未知。 |
| `bytedance-tech-wechat` / 字节跳动技术团队 | `biz=MzI1MzYzMjE0MQ==`；微信号未知 | [团队沙龙介绍](https://developer.volcengine.com/articles/7599494465660977194)引导关注公众号并链接 4 篇同 `biz` 的文章 | 正文活动发生在 2020 年 8 月；社区显示的 2026-01-26 为迁入元数据，不能当作原声明日期。 |

上述身份页是可读的官方关联入口，`entry_kind=official_identity_page`、`history_url=null`；没有声称它们是微信账号历史页。所有 `certified_entity` 均留未知。后续取得更名、转移或当前认证证据再更新，不从旧文章推断最新主体。

## 补充账号、名称关系与原文入口

初始观察日期为 2026-10-15；大淘宝、京东零售行已更新至 2026-10-16。搜索入口用于重新发现；文章锚点只代表单篇内容，不是完整历史目录。

| source_id / 账号 | 标识与入口 | 已核事实及待核关系 |
|---|---|---|
| `alibaba-taobao-wechat` / 大淘宝技术 | `biz=MzAxNDEwNjk5OQ==`；[官方团队目录](https://developer.aliyun.com/group/taobaotech/)；[运营回顾](https://developer.aliyun.com/article/1134381)；[搜狗入口](https://weixin.sogou.com/weixin?type=2&query=大淘宝技术%20Agent%20评测) | 2026-10-16 补读团队汇编与 2023-01-10 发布说明，确认 2022 年历史官方运营，转为 active。既有原文发布名与 biz 保留；官方旧二维码当前仅落微信首页，未绑定现 biz。“淘系技术／淘宝技术”同号关系、微信号及当前认证仍待核。 |
| `jd-retail-wechat` / 京东零售技术 | `biz=MzUyMDAxMjQ3Ng==`；[京东原始 hotkey README](https://gitee.com/jd-platform-opensource/hotkey/raw/master/README.md)；[项目所链微信原文](https://mp.weixin.qq.com/s/xOzEj5HtCeh_ezHDPHw6Jw) | 2026-10-16 读回原始仓库→公众号→原仓库双向互链，当前发布者与既有 biz 一致，转为 active。微信号、认证与现时活跃度仍待核；与京东云开发者、京东技术分别建源。 |
| `jd-cloud-developer-wechat` / 京东云开发者 | [京东云官方社区](https://developer.jdcloud.com/)；微信号与 `biz` 未知 | 官网页脚关联重新核实，账号原文仍未核；不将京东零售技术原文算作本号成功。“自猿其说Tech”是官方目录中的京东物流团队名称线索，当前微信标识待核，不列本号别名。 |
| `tripcom-tech-wechat` / 携程技术 | 当前页 `biz=MjM5MDI3MjA5MQ==`；[官方历史技术合辑](https://docs.c-ctrip.com/files/6/ctriptech/1gw291200099iy5uyCC5B.pdf)；[GUI Agent 多语言质检原文](https://mp.weixin.qq.com/s/vjyX-ZDvFDEbarnLQ3JTPQ) | 历史合辑标注微信公众号“携程技术”、ID `ctriptech`；当前原文、发布名与 `biz` 已读。保留 `official_linked_historical`，历史微信号与当前 `biz` 的精确绑定及当前认证主体待核；“携程技术中心”仅为待核历史名称线索。 |

正文可读性核验：2026-10-15 已读大淘宝技术、京东零售技术、携程技术的代表原文；2026-10-16 已读千问AI平台《自动化评测的九九归一——评测agent》。千问AI平台的历史官方身份页当日遇验证，同号关系沿用已核官方链接与当前 biz；京东云开发者仍仅核身份入口。阿里与京东零售的搜狗签名链接未作为固定入口。以上状态仅对应核验过的代表原文，不代表所有文章可读或近期更新已完整覆盖。

## 2026-10-15 主动扩充

初始扩充于 2026-10-15，按公司技术站、业务团队、产品／开源项目与研究团队入口检索。下表状态已更新至 2026-10-16；历史运营、当前发布者及同号关系的核验程度分别注明。未读取正文的来源仅核身份，所有当前认证主体仍未知。

| 公司／团队 | 公众号与状态 | 官方证据或发现入口 | 标识与待核项 |
|---|---|---|---|
| 阿里巴巴／闲鱼技术 | **闲鱼技术**<br>`alibaba-xianyu-wechat`<br>已核官方关联 | [固定入口](https://github.com/alibaba/fish-redux#关于我们) · [依据1](https://github.com/alibaba/fish-redux) · [依据2](https://developer.aliyun.com/article/687416) | 微信号／biz 未核；官方项目订阅二维码＋团队预告同证；当前平台身份未核 |
| 阿里巴巴／阿里云 PolarDB | **PolarDB**<br>`alibaba-polardb-wechat`<br>已核官方关联 | [固定入口](https://help.aliyun.com/zh/polardb/polardb-for-postgresql/what-is-polardb-postgresql-standard) | 微信号／biz 未核；官方产品文档明示账号；数据库产品与工程内容 |
| 阿里巴巴／阿里云云原生 | **阿里巴巴云原生**<br>`alibaba-cloudnative-wechat-candidate`<br>已核历史官方运营关联 | [官方天池赛事](https://tianchi.aliyun.com/competition/entrance/531922/introduction) · [历史运营回顾](https://developer.aliyun.com/article/850265) | 官方赛事明确向该公众号投稿、工作人员审核推送；Reader 正文已读，直接 HTTP 为壳。历史 ID Alicloudnative 有原始线索；当前名、biz 及“阿里云云原生”同号更名仍待核 |
| 滴滴／OrangeLab / Hummer、DoKit 团队 | **滴滴OrangeLab**<br>`didi-orangelab-wechat`<br>已核官方关联 | [固定入口](https://github.com/didi/Hummer#微信公众号) · [依据1](https://hummer.didi.cn/) · [依据2](https://github.com/didi/Hummer) · [依据3](https://github.com/didi/DoKit) | 微信号／biz 未核；官网／团队声明已核；当前微信显示名、认证及原文未核 |
| 58同城／58技术 | **58技术**<br>`58tongcheng-tech-wechat`<br>已核官方关联 | [固定入口](https://tech.58.com/home) · [依据1](https://tech.58.com/static/js/app.812fc4c004b8117ac8b7.0_1_0.js) | 微信号／biz 未核；官网／团队声明已核；当前微信显示名、认证及原文未核 |
| 360集团／360智汇云 | **智汇云**<br>`qihoo360-zhihuiyun-wechat`<br>已核官方关联 | [固定入口](https://zyun.360.cn/developer/doc?did=shwlwptcpjg) | 微信号／biz 未核；官网明示“智汇云”；云产品与工程混合内容 |
| 贝壳／贝壳产品技术 | **贝壳产品技术**<br>`ke-product-tech-wechat-candidate`<br>已核官方互链与当前发布者 | [官方项目 README](https://github.com/LianjiaTech/BKFlutterWebNativeBridge/blob/9194ac265c75843132e4abd53a9051647dbf678b/README.md) · [项目所链原文](https://mp.weixin.qq.com/s/zIeU0z-4P5Pd9THVybnDFQ) | 独立浏览器读取原文，显示名贝壳产品技术、`biz=MzIyMTg0OTExOQ==`；历史 `gh_9afeb423f390` 与 `beikeTC` 连续关系仍待核。仅身份补读，未作技术分析或导出 |
| 360集团／奇舞团 | **奇舞周刊**<br>`qihoo360-qiwu-wechat-candidate`<br>已核历史官方关联 | [InfoQ原始负责人采访](https://www.infoq.cn/article/7ukfbyff3cyuemdivlsq) · [团队项目](https://github.com/75team) | 2020年采访明确 360→奇舞团→自有技术公众号；微信号／biz、现名未知，“奇舞精选”关系未核；原站访问仍受阻 |
| 金山办公（WPS）／WPS新潮实验室 | **WPS新潮实验室**<br>`kingsoft-office-newwave-wechat-candidate`<br>已核历史官方关联 | [官方管理员运营说明](https://bbs.wps.cn/topic/21224) · [公众号首发声明](https://bbs.wps.cn/topic/14268) | 官方历史运营关联已核；办公产品实践辅助源；微信号／biz、现名及当前微信入口待核。此次为既有证据复核升级 |
| 腾讯／腾讯云开发者社区 | **腾讯云开发者**<br>`tencent-cloud-developer-wechat`<br>已核官方关联 | [固定入口](https://developer.cloud.tencent.com/) | 微信号／biz 未核；官网／团队声明已核；当前微信显示名、认证及原文未核 |
| 腾讯／腾讯云服务器 / Lighthouse | **腾讯云服务器**<br>`tencent-cloud-server-wechat`<br>已核官方关联 | [固定入口](https://developer.cloud.tencent.com/zone/list) | 微信号／biz 未核；官方专题目录关联；产品教程与工程混合内容 |
| 腾讯／腾讯开源 | **腾讯开源**<br>`tencent-opensource-wechat-candidate`<br>已核官方关联 | [官网](https://opensource.tencent.com/) · [命名二维码出处](https://cloud.tencent.com.cn/developer/article/2302606) | 官网与“腾讯开源”命名宣传图二维码解码同址；历史名已核，当前平台显示名、微信号／biz及认证未知 |
| 腾讯／AlloyTeam | **腾讯AlloyTeam**<br>`tencent-alloyteam-wechat-candidate`<br>候选 | [团队仓库](https://github.com/AlloyTeam/alloyteam.github.com) · [官网声明入口](https://www.alloyteam.com/star.html) · [实读原文](https://mp.weixin.qq.com/s?__biz=MjM5MTY2NTIyMA==&mid=2649000528&idx=1&sn=98521c16c3f24809f426fe39ae48e203) | 2026-10-16 当前名腾讯AlloyTeam、`biz=MjM5MTY2NTIyMA==` 已读，正文有团队自述。历史官网索引名 AlloyTeam 与当前 biz 的精确官方绑定仍待核；微信号与认证未知。 |
| 字节跳动／基础架构服务框架团队 / CloudWeGo | **CloudWeGo**<br>`bytedance-cloudwego-wechat`<br>已核官方关联；原文已导出 | [官方活动](https://developer.volcengine.com/activities/7476296718292631578) · [团队介绍](https://www.cloudwego.io/zh/about/) | 当前页显示 CloudWeGo，`biz=Mzg2MTc0Mjg2Mw==`；2025-11-13 Excel Agent 原文已读。搜狗转载经版权卡回溯本号；字节跳动技术团队是另一账号 |
| 字节跳动／开源委员会 OSPO | **字节跳动开源**<br>`bytedance-opensource-wechat`<br>已核官方关联 | [固定入口](https://developer.volcengine.com/articles/7317464577179844645) · [依据1](https://developer.volcengine.com/activities/7488615140225449996) | 微信号／biz 未核；官网／团队声明已核；当前微信显示名、认证及原文未核 |
| 百度／飞桨 PaddlePaddle | **飞桨PaddlePaddle**<br>`baidu-paddle-wechat`<br>已核官方关联 | [固定入口](https://cloud.baidu.com/support/news?action=detail&id=3052) | 微信号／biz 未核；2023 年运营声明；当前平台身份未核 |
| 百度／百度智能云 | **百度智能云**<br>`baidu-cloud-wechat`<br>已核官方关联 | [固定入口](https://cloud.baidu.com/live/84) | 微信号／biz 未核；官网／团队声明已核；当前微信显示名、认证及原文未核 |
| 快手／研发效能中心、主站技术部等投稿团队 | **快手技术**<br>`kuaishou-tech-wechat-candidate`<br>已核官方关联 | [团队署名及授权的原始发布](https://www.infoq.cn/article/9rX1Ov951gKtaTmQb8Jq) | 发布页明确团队作者、授权并推荐本公众号；第三方 biz 仍待核；未读微信当前身份和正文，不合并“快手AI” |
| 小米／小米技术官网 | **官网关联公众号（显示名待核）**<br>`xiaomi-tech-wechat-candidate`<br>已核官方入口 | [公司官方技术站](https://tech.mi.com/) · [官网二维码资源引用](https://tech.mi.com/js/app.15f7d5a4.js) | 官方微信入口已核；与候选名“小米技术”的精确绑定仍待核，不把第三方名称写成已核别名。微信号／biz未知 |
| 蚂蚁集团／SOFAStack 社区 | **金融级分布式架构**<br>`ant-sofastack-wechat`<br>已核官方关联 | [固定入口](https://www.sofastack.tech/community/) · [依据1](https://www.sofastack.tech/awesome/) · [依据2](https://www.sofastack.tech/faq/) | 微信号 `Antfin_SOFA`；项目名 SOFAStack 是否也是账号更名待核 |
| 蚂蚁集团／蚂蚁技术 | **蚂蚁技术AntTech**<br>`ant-anttech-wechat-candidate`<br>已核官方历史互链与当前发布者 | [SOFAStack 访谈正文](https://github.com/sofastack/sofastack.tech/blob/38c28a43d187f60a3b279ce8e7c140fa6afb4e42/content/zh/blog/sofastack-linux-china/index.md) · [原文](https://mp.weixin.qq.com/s?__biz=MzI0Nzc3MTQyMw==&mid=2247487956&idx=1&sn=342121bca34384ffa95b9cabb4c18821&scene=21) | 浏览器现名蚂蚁技术AntTech，`biz=MzI0Nzc3MTQyMw==`；官方历史文章到当前账号已连通。历史 Ant-Techfin、各次更名日期与认证主体未独立确认 |
| 网易／网易云信 | **网易云信**<br>`netease-yunxin-wechat`<br>已核官方关联 | [固定入口](https://yunxin.163.com/) | 微信号／biz 未核；官网／团队声明已核；当前微信显示名、认证及原文未核 |
| 网易／网易易盾 | **网易易盾**<br>`netease-yidun-wechat`<br>已核官方关联 | [固定入口](https://dun.163.com/) | 微信号／biz 未核；官网／团队声明已核；当前微信显示名、认证及原文未核 |
| 网易／网易伏羲 | **网易伏羲**<br>`netease-fuxi-wechat`<br>已核官方名称关联；原文已导出 | [官网](https://fuxi.netease.com/) | 当前原文名网易伏羲，`biz=MzU2Nzg0NTk0NQ==`；官网二维码到此 biz 的精确绑定未闭合，认证未知。已读2022-06-09 IRAT历史方法案例，不代表近期方向 |
| 网易／云音乐大前端团队 | **网易云音乐大前端团队**<br>`netease-music-tech-wechat`<br>已核历史官方团队关联 | [团队 README](https://github.com/x-orpheus/blog) · [公司 Tango 项目](https://github.com/NetEase/tango/blob/main/README.zh-CN.md) | 公司项目、musicfe.com 团队域、署名作者与原博客发布矩阵互证；原二维码 `biz=MzI1NTg3NzcwNQ==` 已核。固定掘金账号现名“网易云音乐技术团队”，微信更名仍待核 |
| 哔哩哔哩／哔哩哔哩技术 | **哔哩哔哩技术**<br>`bilibili-tech-wechat`<br>升级：官方历史名称已核 | [固定入口](https://ir.bilibili.com/cn/esg/esg-report/) · [依据1](https://ir.bilibili.com/media/ftcjhpj4/bps23090002_bilibili-2023esg_sc_c4856.pdf) | 微信号／biz 未核；官网 2023 ESG p38 已读；当前平台身份未核 |

58技术另有[官方技术站](https://tech.58.com/home)，以 `58tongcheng-tech-blog` 独立保存，通过 `official_mirror_source_id` 关联公众号，仅表示替代发现目录，不保证逐篇镜像。

逐公司覆盖及原有账号见[公司覆盖表](../_shared/references/company-coverage.md)和[历史扩展表](large-internet-sources.md#公众号身份与读取边界)。未核实的名称、微信号或更名关系保留待核；账号已有官方关联证据时，不因某项标识未知而撤销该关联。

<a id="2026-10-16-七项候选与三团队近期研究"></a>

## 2026-10-16 七项候选复核

既有 7 个候选全部复核，**4 个升级、3 个继续待核**。总数仍为 43 个账号，当前 40 个官方关联或官方入口、3 个候选。以下记录账号身份依据，不代表新增文章或全文可读性核验。

| source_id / 公众号 | 状态与新证据 | 仍待核的关系 |
|---|---|---|
| `baidu-geek-wechat-candidate` / 百度Geek说 | active；[百度 babylon 固定 README](https://github.com/baidu/babylon/blob/67cd1491ae46527f9c29565e937f23cf238c3747/README.zh-cn.md)正文微信链接与实读账号 `biz=Mzg5MjU0NTI5OQ==` 相同 | 历史微信号 baidugeektalk、当前认证及活跃度 |
| `sohu-tech-wechat` / 搜狐技术产品 | active；[hotcaffeine README](https://github.com/sohutv/hotcaffeine/blob/71e353a6ecfec3d167c369906961d874884e45a0/README.md)与微信原文双向互链，现 `biz=MzU3NTY3MTQzMg==`；编辑原始招稿补强运营关系 | sohu-tech 微信号、当前认证及活跃度；sohutv 是 GitHub User，不写成认证组织 |
| `alibaba-taobao-wechat` / 大淘宝技术 | active；[原始年度运营说明](https://developer.aliyun.com/article/1134381)与团队汇编确认历史运营 | 当前 biz 精确官方绑定、“淘系技术／淘宝技术”同号关系 |
| `jd-retail-wechat` / 京东零售技术 | active；[原始 Gitee README](https://gitee.com/jd-platform-opensource/hotkey/raw/master/README.md)↔[微信文章](https://mp.weixin.qq.com/s/xOzEj5HtCeh_ezHDPHw6Jw)，现 `biz=MzUyMDAxMjQ3Ng==` | 微信号、当前认证及活跃度 |
| `vipshop-tech-wechat-candidate` / 唯品技术 | candidate；[原刊运营负责人采访](https://wppinwei.com/book/22/6a3e3e3ba216f047f7/)已读到供稿审核及旧号迁移说明，关注码已解 | 刊物与唯品会的独立官方归属、当前账号名/biz；“唯技术”迁移承接不能直接当同 biz 更名 |
| `kingsoft-office-wechat-candidate` / 金山办公 | candidate；[原文头部](https://mp.weixin.qq.com/s/yO5zUmW8fNL_mHXnM0VgQw)显示名已读，`biz=MzIwNTU0NDE1Ng==` | 公司到精确账号的运营关联、认证；正文文本空，不计全文可读；不合并 WPS新潮实验室 |
| `tencent-alloyteam-wechat-candidate` / 腾讯AlloyTeam | candidate；当前页面名与 `biz=MjM5MTY2NTIyMA==` 已读，历史官网声明索引保留 | 官网历史名称 AlloyTeam 到现 biz 的精确绑定、微信号及认证 |

## 持续发现与正文读取

| 来源 ID / 目录 | 本轮可读性 | 使用方法 |
|---|---|---|
| `meituan-tech-blog` / [美团技术博客](https://tech.meituan.com/) | 已有目录；本轮评测白皮书正文可读 | 沿用现有 ID。白皮书与它引用的微信“评测漫谈”是两篇文章，不能将前者当作后者已读。 |
| `tencent-teg-cloud-blog` / [腾讯技术工程作者目录](https://cloud.tencent.com/developer/user/170434/articles) | 目录可读；[腾讯文档 AI](https://cloud.tencent.com/developer/article/2412926)取得正文，实际分析第 2 章与 3.1 | 按发布账号筛选，保留正文作者与具体团队。2024 年案例可供方法学习，不代表当前线上架构。 |
| `alibaba-developer-author-blog` / [阿里云开发者作者目录](https://developer.aliyun.com/profile/6ibaby6qg4ku4) | 部分标题、摘要及链接可读；部分条目缺标题，未翻页 | 标记 `directory_partial`；可用官方博客专题补充发现，逐篇读取后才能生成材料。 |
| `bytedance-tech-volc-blog` / [字节技术团队作者目录](https://developer.volcengine.com/user/2772312065061673) | 目录可读；[AIO Sandbox](https://developer.volcengine.com/articles/7599494081655668799)取得正文，实际分析痛点、整体架构及鉴权 | 发布者与文章日期分别留证；代码链接只代表发现，读取固定版本或运行后再记录验证范围。 |

2026-10-13 的四次微信原链直接读取均为验证页；腾讯另经 Chrome 跳转验证页后被浏览器策略阻止。当次微信正文成功数为 **0/4**。后续轮次按实际工具与页面分别记录结果，官方替代目录的成功不记到微信原链。

## 新增与扩充

1. 先按公司、团队、微信号／`biz`、目录 URL 和别名检查已有清单；同名不能自动合并。同一账号下的新文章不新增账号来源。
2. 找公司自有站、官方运营声明或明确互链，保存日期与实际可见身份；社区开放投稿，仅有官方域名不足以证明作者归属。归属不足保留 `candidate`。
3. 读取身份入口与官方社区替代目录；代表原链用于补充归属证据，或在任务包含正文可读性核验时读取。分别记录方法、时间、结果和证据。没有历史目录就留空；不能用重复读取一篇旧文章判断是否更新。
4. 范围内核实的新源增量加入 `active`，保留已有暂停、排除和别名；账号与替代目录通过 `official_mirror_source_id` 关联，该字段只表达官方替代来源，不保证逐篇相同。公共固定清单只在用户要求维护时更新。
5. 回读关注清单，核对新增、更新、候选与访问边界；重复加入同一 `source_id` 应为零新增。仅扩充来源时只更新来源维护记录，保持材料基线与采集报告不变。

任务包含文章采集或分析时，再按[采集流程](collection.md)读取相关正文、保留实际阅读章节和元数据证据；需要岗位映射且有 JD 证据时，关联具体要求原句。新材料按[追踪流程](tracking.md)生成目录快照，核对成功后推进材料基线。清单扩充不自动建立定时任务；原链失败、镜像读取、文章分析、代码验证分别报告。
