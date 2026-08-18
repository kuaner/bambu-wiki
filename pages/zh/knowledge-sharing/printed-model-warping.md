---
path: zh/knowledge-sharing/printed-model-warping
title: "模型翘边"
description: ""
tags: []
created: 2024-06-07T08:37:48.870Z
updated: 2026-08-05T01:55:38.641Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/printed-model-warping
---

## 模型翘边

在下面的示例中，模型的一角出现了翘起。

![](https://wiki.bambulab.com/knowledge-sharing/printing-issues/curling_corner.jpg)

> 相关 wiki:
>
> - [模型翘边、脱落或倒塌](../filament-acc/filament/print-quality/warping-falling-off-collapsing.md)
> - [小圆片的使用技巧——防止翘曲](../software/bambu-studio/use-disc-to-avoid-warping.md)

## 潜在原因和解决方案

### 1. 热床温度设置过低/打印板类型不正确

导致模型翘边、从热床上脱落的最常见原因之一，就是热床温度与耗材温度不匹配，或选择了错误的打印板类型。

同一种材料通常在不同的打印板使用不同的热床温度进行打印，如果选错打印板类型，则有可能因为打印的热床温度不足而导致粘接力不足。另外，纹理 PEI 板由于表面有颗粒物，所以在热床调平后，打印机会下压喷嘴 0.04mm 确保首层粘接。如果您使用纹理 PEI 板打印，却在切片时选择了其他类型的打印板，则会导致喷嘴高度过高，影响首层粘接。

因此，请根据所用的耗材，选择正确的打印板类型。同时，在开始打印前要确保打印板是干净的，可以大幅提高打印成功的几率。

![change_build_plate_bambu_studio_zh.webp](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/change_build_plate_bambu_studio_zh.webp)

### 2. 部件冷却风扇速度过高

大多数情况下，在快速打印时，快速冷却适用于 PLA 耗材。但在某些情况下，冷却过快会导致模型翘边。Bambu Studio 的耗材配置文件经过微调，为各种类型的耗材提供最佳效果，通常能达到预期的打印效果。

如果出现翘边，建议仔细检查 “耗材丝设置”下的“冷却”参数：

![](https://wiki.bambulab.com/knowledge-sharing/printed-model-warping/cooling.png)

为了解决翘边，最需要更改的设置之一是“关闭冷却对前 X 层”选项。理想情况下，大多数常见耗材（PLA、PETG、TPU 等）的前 3 层都不需要冷却，可以确保打印层缓慢冷却，获得最佳粘附力，从而避免翘边和打印失败。

我们还建议根据实际情况，调整辅助部件冷却风扇，将其调低至 40-50% 左右。较高的辅助部件冷却风扇转速对 PLA 耗材好处更大，但主要适用于小模型或悬垂度较高的模型。如果模型出现翘边，降低辅助部件冷却风扇的转速会有所帮助。

![](https://wiki.bambulab.com/knowledge-sharing/printed-model-warping/auxiliarypart-cooling-fan-speed.png)

### 3. 环境温度过低

常见的 PETG、ABS、ASA、PA 和 PC 比 PLA 更容易出现翘边。大多数情况下，由于打印层冷却过快，使得层间产生应力，最终导致翘边。这些温度要求高的材料通常要在封闭的 3D 打印机中打印，部件冷却较少或完全没有冷却，使得部件周围的环境温度较高，模型冷却较慢。

如果在非封闭的打印机（如 A1）上打印这些耗材，由于模型周围的温度与室温相同，可能会经常出现翘边。当室温低于 20 摄氏度时，即使是宽容度较高的 PLA 和 PETG 耗材也会出现翘边现象。在这种情况下，最好设置更高的热床温度（+10 摄氏度），通过减慢打印层之间的冷却速、确保打印机周围没有气流（气流会加快模型的冷却速度，增加层间的结合应力，导致翘边），从而提高模型的打印成功率。

### 4. 模型尺寸较大且填充率过高

如果模型尺寸较大且填充率设置得较高，如 60%（默认值是 15%），发生了翘边，可适当调低。另外，填充图案带有较多直线的更容易收缩，可以把填充图案改成螺旋体来降低收缩风险。对于部分对强度要求较高的结构件，可以设置 5 层墙和 25% 左右的填充率，尽量避免使用 50% 以上的填充率，以降低收缩趋势；对于大多数对强度要求较低的非结构件，则可以直接选择默认的 2 层墙和 15% 的填充率。

**螺旋体填充**：  
![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E8%9E%BA%E6%97%8B%E4%BD%93%E5%A1%AB%E5%85%85.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
