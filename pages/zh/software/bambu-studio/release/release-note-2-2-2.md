---
path: zh/software/bambu-studio/release/release-note-2-2-2
title: "Bambu Studio 2.2.2 版本说明"
description: ""
tags: []
created: 2025-09-15T08:41:21.037Z
updated: 2025-09-16T06:10:41.350Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-2-2
---

该版本为基于V2.2.1.60的一个版本，新增支持Helio优化功能，并修复了部分已知bug。

### 功能

#### Helio Addictive优化功能集成（Beta）

最新版Studio（V2.2.2）进一步集成了Helio Addictive**优化**功能。Helio Addictive优化引擎会对GCode文件进行热力学分析，并返回优化后的GCode，用以改善可能的翘曲、粘接或者下垂问题。

**启用/禁用Helio服务：**

1. 使用Helio功能前需要启用该服务，点击切片按钮左侧的**第三方扩展管理按钮**，点击“**立即使用**”。

![](https://wiki.bambulab.com/bambu-studio/manual/release-note-2-2-2/image.png)

- 确认第三方扩展服务说明，如点击“**同意并继续**”即表示**您同意第三方扩展服务说明内容**。随后的弹框中确认Helio隐私政策，如点击“**同意并继续**”即表示**您同意Helio隐私政策**。

![](https://wiki.bambulab.com/bambu-studio/manual/release-note-2-2-2/image-1.png)

![](https://wiki.bambulab.com/bambu-studio/manual/release-note-2-2-2/image-2.png)

- 弹框显示已成功启用Helio第三方插件功能，随后可关闭该弹窗，正常使用Helio Addictive的仿真和优化功能。如需关闭Helio Addictive功能，点击“**卸载Helio Additive插件**”按钮后，对Helio Addictive服务进行卸载。

![](https://wiki.bambulab.com/bambu-studio/manual/release-note-2-2-2/image-3.png)

**优化功能使用方法:**

1. 正常对模型进行切片。
2. 点击切片按钮左侧的**Helio Action**按钮。

![](https://wiki.bambulab.com/bambu-studio/manual/release-note-2-2-2/helio_cn_optimize.png)

- 切换到优化选项卡，可选择**是否优化外墙**，或通过打开高级选项对**速度**、**体积流量**或**优化的层数**进行限制。
- 点击“**确认**”并等待优化运行完成。
- 仿真完成后，可在切片模型上查看优化结果，并发送至打印机进行打印。

![](https://wiki.bambulab.com/bambu-studio/manual/release-note-2-2-2/image-5.png)

ℹ️ **热指数（TQI）颜色映射更新**

• 根据客户反馈调整了 TQI 颜色映射。

• 抗拉强度下降 50%——或进入翘曲临界区——对应 −50 TQI。

• 可打印范围为 -50 至 0 TQI；0 TQI 表示最强、最快的打印（可能牺牲外观质量）。

**⚠ 当前限制与支持配置**

- 支持的打印机：Bambu Lab X1/X1C/X1E、H2D
- 即将支持的打印机：A1、P1S、P1P、H2D Pro
- 支持的耗材：

  - Bambu（13 种）：Bambu PPS-CF、Bambu PPA-CF、Bambu PETG-CF、Bambu PET-CF、Bambu PA6-CF、Bambu TPU 95A HF、Bambu PLA Silk+、Bambu PLA Matte、Bambu PLA Lite、Bambu PLA Basic、Bambu PETG HF、Bambu PC、Bambu ABS
  - Polymaker（5 种）：PolyTerra PLA、PolyLite PLA、PolyLite PETG、PolyLite ASA、PolyLite ABS
  - Fiberon（7 种）：Fiberon PETG-rCF、Fiberon PETG-ESD、Fiberon PET-CF、Fiberon PA612-CF、Fiberon PA6-GF、Fiberon PA6-CF、Fiberon PA12-CF
- G-code 要求：G-code 必须为单色、逐层顺序切片（暂不支持多色或多材料）。

如需[购买配额或查看更多详情](https://wiki.helioadditive.com/zh/bambu-studio)，请参阅 Helio Additive Wiki（[https://wiki.helioadditive.com/zh/bambu-studio）](https://wiki.helioadditive.com/zh/bambu-studio%EF%BC%89) 或加入[Helio Additive Discord](https://discord.com/invite/EjQXDJP9kS)。中国大陆用户可点击链接后扫描关注[Helio微信公众号](https://mp.weixin.qq.com/s/Sl1WH1_q72IDqw_pY5_vig)。

### Bug修复

1. 修复了部分情况下Bambu账号登录后无法保持登录状态的错误。([#7796](https://github.com/bambulab/BambuStudio/issues/7796), [#7887](https://github.com/bambulab/BambuStudio/issues/7887), [#7851](https://github.com/bambulab/BambuStudio/issues/7851), [#7806](https://github.com/bambulab/BambuStudio/issues/7806), [#7988](https://github.com/bambulab/BambuStudio/issues/7988), [#8067](https://github.com/bambulab/BambuStudio/issues/8067))
2. 修复了部分情况下A1 mini发起流量比例校准时无法解析GCode的错误。
3. 更新了部分土耳其语翻译，感谢[@fatih5228](https://github.com/fatih5228)的贡献。
4. AppImage脚本新增多种图标大小的支持，感谢[@mean-ui-thread](https://github.com/mean-ui-thread)的贡献。
5. 修复了延时摄影列表缩略图加载时可能出现的崩溃问题，感谢[@bytedream](https://github.com/bytedream)的贡献。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
