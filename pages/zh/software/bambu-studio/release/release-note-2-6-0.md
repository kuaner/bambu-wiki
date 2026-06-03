---
path: zh/software/bambu-studio/release/release-note-2-6-0
title: "Bambu Studio 2.6.0 版本说明（Hotfix）"
description: ""
tags: []
created: 2026-04-17T12:36:08.287Z
updated: 2026-04-17T12:36:09.298Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-6-0
---

该版本为基于V2.5.3 Public Release发布的hotfix版本，主要修复了**P2S 打印结束后喷嘴温度无法正常下降**的问题。由于通过预设更新方式修复可能会影响V2.5.0相关用户的现有预设，本次改为通过V2.6.0版本发布，以尽量减少对现有用户的影响。

对于正在使用**P2S**且Studio版本为**V2.5.3**的用户，建议尽快升级至该版本以避免上述问题。

### 关于混色功能的说明

在收到社区反馈后，我们重新核查了当前版本的实现和代码路径。在该功能开发过程中，我们评估了多种颜色混色预测方案，包括**RGB混色方案**，以及**Full Spectrum的混色预测实现**。在当时的验证条件下，我们选择了目前V2.5.3**实际使用的RGB混色方案。**

在开发过程中，为便于横向验证不同方案，我们保留了评估中的实现代码，但我们没有在此前说明中清晰标注其运行状态。该疏漏给用户和社区造成了困扰，我们对此诚挚致歉。

我们接下来做的两件事：

1. 在本次release中更正相关说明，明确当前代码仓库中**包含Full Spectrum颜色预测代码**的事实情况；
2. 结合进一步测试验证和更多实际反馈，推进对Full Spectrum颜色预测实现的正式接入。

我们感谢[@justinh-rahb](https://github.com/justinh-rahb)和[@ratdoux](https://github.com/ratdoux)在这一方向上的贡献，也感谢开源社区对这一问题的指出和监督。

### **Bug 修复**

1. 修复了因End G-code错误导致的P2S打印结束后喷嘴温度无法正常下降的问题。
2. 修复了部分场景下A1切片文件无法发起打印的问题。
3. 移除了部分不必要的提示文案。
4. 修复了省料模式下H2C切片固定分配至左喷嘴的问题。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
