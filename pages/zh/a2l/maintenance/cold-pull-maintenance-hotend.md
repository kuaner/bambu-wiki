---
path: zh/a2l/maintenance/cold-pull-maintenance-hotend
title: "A2L 喷嘴堵塞清理"
description: "本文介绍了 A2L 喷嘴堵塞时应如何清理"
tags: []
created: 2026-06-01T13:32:08.482Z
updated: 2026-06-10T01:29:15.497Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/cold-pull-maintenance-hotend
---

## 部分堵塞

当喷嘴内部被小颗粒物质堵塞住，而不能完全通过耗材时，会导致挤出线宽过细或无法挤出耗材。而喷嘴内部压力和流量的不稳定，也会使[动态流量](../../software/bambu-studio/calibration_pa.md)的 K 值校准不准确，影响打印质量。

## 堵塞原因

热端堵塞是 FDM 3D 打印机较为常见的故障，可能由以下原因引起：

- 耗材直径不稳定。  
  耗材直径通常为 1.75 mm± 0.03，当耗材过粗时，容易卡在热端内部；当耗材过细时，挤出机的齿轮将无法咬住耗材，这也会导致喷嘴无法挤出。
- 耗材表面或挤出机内部的杂质进入热端后造成喷嘴部分或完全堵塞。
- 耗材中的颗粒堵塞喷嘴口（常见于碳纤维增强、夜光或闪光耗材）。
- 在切换不同类型的耗材时，存在前一种耗材残留（如 PLA 与 PC、ASA 与 TPU 等）。

## 所需工具

- 通针
- 钳子
- H1.5 内六角扳手
- 隔热手套
- 一小段耗材

## 安全提示

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子原件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## 方法一：加温挤出

### 步骤 1 ：加热喷嘴

将喷嘴温度提高到**略高于**耗材要求的温度（以PLA为例，设置热端温度为250℃）。

![250zh1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/250zh1.jpg)

#### 步骤 2 ：控制挤出

点击屏幕上的“挤出”按钮挤出耗材。  
**若使用 TPU 材料，“进料”按钮最多只能点击三次。同时避免快速连续点击“退料”按钮，以防出现卡料或缠料。**

![extrudericon.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/extrudericon.jpg)

观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

![6.webp](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/nozzl-cold-pull-cleaning/6.webp)

## 方法二：通针疏通

请注意此方法**不适用于直径小于 0.4mm 的喷嘴**。  
如果喷嘴无法正常挤出，则需要使用通针疏通喷嘴，再尝试重新挤出耗材。

### 步骤 1 ：释放喷嘴压力

按压一次挤出机从动轮柄，释放喷嘴内的耗材压力。

![extru21.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/extru21.jpg)

### 步骤 2 ：加热喷嘴

将喷嘴温度提高到略高于耗材要求的温度，以PLA为例，设置热端温度为250℃。

![250zh1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/250zh1.jpg)

### 步骤 3 ：使用通针上下疏通

温度达到后，将通针插入喷嘴口，反复上下疏通数次。

![nozzle.webp](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/nozzle.webp)

> 拔出通针时，喷嘴内的耗材可能突然喷溅，请佩戴隔热手套，注意安全。

### 步骤 3 ：手动挤出

点击屏幕上的“挤出”按钮挤出耗材。  
**若使用 TPU 材料，“进料”按钮最多只能点击三次。同时避免快速连续点击“退料”按钮，以防出现卡料或缠料。**

![extrudericon.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/extrudericon.jpg)

观察耗材是否正确挤出。耗材应呈直线状连续流出，如下图所示：

![6.webp](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/nozzl-cold-pull-cleaning/6.webp)

## 方法三：使用通针进行冷拔

冷拔是 3D 打印中的一种维护技术，用于清洁打印机喷嘴内部，去除碎屑、堵塞物或残留的耗材。

冷拔耗材就像一个“粘棒”，在融化阶段会与喷嘴内的残留物粘合在一起，轻微冷却后耗材就存在一定的韧性。此时将耗材拔出，就可以物理移除喷嘴内部的污染物，例如灰尘或小堵塞物。

定期进行冷拔程序有助于恢复正常的耗材流动，从而实现稳定的挤出，并有助于防止挤出不足或打印线条不一致等打印缺陷。建议不时进行冷拔，尤其是在更换不同耗材类型时。

### 冷拔流程

在屏幕上点击“设置-维护-喷嘴冷拔维护”，开启冷拔维护。可跳转到[A2L 喷嘴冷拔维护指南](nozzle-cold-pull-maintenance.md)了解详情。

> 冷拔过程中设备会自动冲刷耗材，若冲刷过程中耗材无法从喷嘴挤出，请根据方法二使用通针将堵塞物从喷嘴口推向喷嘴内部。

![1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/nozzl-cold-pull-cleaning/1.jpg)

## 方法四：使用内六角扳手拔出堵塞耗材

> 操作时请佩戴隔热手套，防止高温灼伤手指。

### 步骤 1 ： 加热内六角扳手

首先将内六角扳手加热约 10s。使用钳子牢牢夹住扳手，注意不要被烫伤。

![1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/1.jpg)

### 步骤 2 ：将内六角扳手插入热端顶部

从热端顶部插入加热后的内六角扳手，扳手会插入堵塞的耗材中，如下图所示。  
等待大约 30s，让内六角扳手自然冷却。

![2.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/2.jpg)

### 步骤 3 ： 加热热端，拔出堵塞的耗材

使用打火机对喷嘴尖端加热约 20s。

> 请避免长时间加热喷嘴或使用高功率丁烷喷枪。建议使用普通燃气打火机进行加热。  
> 只需将喷嘴加热至能够将内六角扳手连同堵塞的耗材一并拔出的温度即可。过度加热可能导致耗材从喷嘴尖端滴落或突然喷出。请严格按照说明操作，并确保加热时喷嘴尖端不要朝向自己。

![3.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/3.jpg)

3. 缓慢拔出内六角扳手，热端里被堵塞的耗材会附着在内六角扳手上被带出。

![4.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/cold-pull-maintenance-hotend/4.jpg)

## 验证功能

重新连接 PTFE 管，装载耗材并测试挤出情况。若仍然无法挤出或挤出不足，则需要重复多次喷嘴疏通操作。  
![10.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/nozzl-cold-pull-cleaning/10.jpg)

## 注意

0.2 mm 的喷嘴更难清除堵塞物，可能需要多次进行上述步骤。另一方面，大于 0.4 mm 的喷嘴往往比 0.4 mm 的喷嘴更少堵塞，因为喷嘴的口径开口允许更大的颗粒通过。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
