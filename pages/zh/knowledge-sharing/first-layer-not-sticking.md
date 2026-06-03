---
path: zh/knowledge-sharing/first-layer-not-sticking
title: "首层不粘"
description: ""
tags: []
created: 2024-06-07T07:10:24.763Z
updated: 2026-01-22T07:30:36.333Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/first-layer-not-sticking
---

## 首层不粘

|  |  |
| --- | --- |
|  |  |

## 潜在原因和解决方案

### 1. 选择了错误的打印板类型

在 Bambu Studio 中选择了错误的打印板类型，可能会导致首层不粘附。

![](https://wiki.bambulab.com/knowledge-sharing/first-layer-not-sticking/plate-type.png)

例如，如果在[低温打印板](../x1/manual/printing-on-cool-plate.md)上切片一个模型，然后在[纹理 PEI 打印板](../general/textured-PEI-plate-not-working-as-expected.md)上打印，那么模型很有可能无法按照预期粘附在打印板上。低温打印板对 PLA 的温度要求在 **35 摄氏度**左右，而纹理 PEI 板对 PLA 的温度要求在 **55 - 65 摄氏度**左右。纹理 PEI 打印板也有着不一样的 Z 偏移，会影响喷嘴与打印板表面的距离，从而影响首层的打印。

根据所用的耗材，选择正确的打印板类型。同时，在开始打印前要确保打印板是干净的，可以大幅提高打印成功的几率。

### 2. 打印前未清洗打印板

我们强烈建议在打印前用[温水和清洁剂清洗打印板](../general/textured-PEI-plate-not-working-as-expected.md)，去除所有碎屑和污染物，并且避免接触打印板表面。

只要根据打印的耗材类型使用正确设置，并且在 Bambu Studio 中选择了正确的打印板类型，这种方法能解决大多数粘附力相关的问题。

> 在一些情况下，我们还建议使用 Bambu Lab 胶水于打印板上以增强模型附着力，提高打印成功率，例如，使用光面 PEI 打印板打印除 PLA 外耗材时。更多使用胶水的详细信息可参照：[如何使用 Bambu Lab 胶水](../general/how-to-use-bbl-liquid-glue.md)

### 3. 未执行热床调平

在某些极少数情况下，以前校准的热床调平可能不准确，导致打印板的粘附不一致。如果遇到首层质量问题，我们建议在确保喷嘴尖端干净且没有任何碎屑后，在“校准”界面上执行热床调平。

![](https://wiki.bambulab.com/knowledge-sharing/first-layer-not-sticking/bed-leveling-calibration.png)

我们强烈建议在在发送打印的界面上选上热床调平，提高打印的成功几率。

![](https://wiki.bambulab.com/knowledge-sharing/first-layer-not-sticking/bed-leveling-send-print.png)

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
