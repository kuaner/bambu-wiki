---
path: zh/h2c/manual/bambu-studio-h2c-operation
title: "H2C Bambu Studio 操作指南"
description: ""
tags: []
created: 2025-11-18T12:40:13.380Z
updated: 2025-11-18T13:36:15.050Z
source: https://wiki.bambulab.com/zh/h2c/manual/bambu-studio-h2c-operation
---

## 机器信息同步

为优化 H2C 多喷嘴机型的切片效果与运行效率，软件引入了新的机器信息同步逻辑。H2C 支持右热端自动更换，最多可安装 6 个右热端交替使用，其使用数量将直接影响切片时的耗材冲刷量。

点击**同步信息**，Studio 可自动获取打印机上的喷嘴直径、流量、数量等关键信息。您只需在同步喷嘴界面选择喷嘴类型，系统将自动切换对应的机器预设、流量设置与喷嘴配置。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-11.png)

- 软件默认将喷嘴数量设置为：1 个左喷嘴，6 个右喷嘴。
- **Studio 目前不支持使用不同直径的喷嘴进行混合切片。**如果机器的热端挂架上安装了不同直径的喷嘴，您必须在同步信息界面中手动选择一个直径的喷嘴来完成配置。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-9.png)

![喷嘴信息显示](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-7.png)

## 混合流量切片

当安装了**直径相同但流量不同的右喷嘴**以作交替使用时，待机器信息完成同步，系统会自动将喷嘴流量设置为“混合模式”。

![混合流量模式](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-14.png)

在该模式下切片时，Studio 会根据两种流量喷嘴的数量以及 AMS 和左右热端的连接关系，自动将耗材分配至合适的喷嘴；**在不产生额外冲刷的前提下，会优先分配标准流量喷嘴，再分配高流量喷嘴。**

除自动分配外，软件也支持手动分配，允许您为每种材料指定所使用的喷嘴流量类型。

![自定义模式下指定耗材使用不同流量的喷嘴](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-6.png)

## 冲刷模式选择

针对 H2C 机型，Studio 提供了两种擦料塔冲刷模式：标准模式和省料模式。

![冲刷模式选择](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-3.png)

- **标准模式**：擦料塔的冲刷量严格按用户在切片中设定的材料清理量执行，以确保最佳打印质量。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image.png)

- **省料模式**：擦料塔的清理量**固定为 15mm³**，旨在减少耗材浪费并提升打印速度。

详情请参考： [Bambu Studio H2C 擦料塔冲刷模式详解](../../software/bambu-studio/h2c-purge-mode.md)

## 分组算法

在 H2C 机型上，分组算法不仅需要统筹耗材在左右热端间的分配，还需依据感应热端的数量，自动将不同耗材合理分配至同一喷嘴进行打印。切片时，感应热端数量将直接影响最终的耗材分配方案与冲刷消耗量。

为满足多样化打印需求，分组算法提供多种模式。您可根据实际打印目标选择对应分组策略进行切片，例如追求省料，或减少打印过程中的耗材位置的调整频次。  
具体模式介绍与使用方法，请参考：[双喷嘴打印机耗材切片分组](../../software/bambu-studio/manual/dual-nozzles-slicing-filament-grouping.md)

相较于 H2D 的双热端切换，H2C 拥有更多可切换的热端，从而能在多色打印中将不同耗材尽可能分配至独立的热端，有效减少因材料切换产生的冲刷量。其整体分配逻辑如下：

1. 当切片所使用的耗材数量**大于等于 2 种**时，自动分组算法**必定会分配其中一种至左热端**进行打印。这是因为左右热端之间的切换不仅节省冲刷量，也更节省时间。而右侧感应热端之间的切换虽能节省冲刷量，但需要 AMS 执行重新进退料操作，因此会耗费更多时间。

![image_-_2025-11-12t114513.495.png](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image_-_2025-11-12t114513.495.png)

2. 若切片所使用的耗材种类**超过打印机内可用热端总数**，算法会**优先考虑将冲刷量最小的两种耗材分配至同一热端打印**，以此实现最节省耗材的目的。

![screenshot-20251112-114623.png](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/screenshot-20251112-114623.png)

因此，为获得最佳切片效果，强烈建议在完成机器和 AMS 信息同步后，再进行切片操作。

## 喷嘴映射

在发起打印时，打印机会根据打印参数与当前机器上的喷嘴状态，自动计算并生成耗材与喷嘴之间的映射关系（该计算在打印机端完成，若网络状况不佳，可能无法完成自动映射）。其中，**R 喷嘴**指工具头上已安装的感应喷嘴，挂架上的喷嘴则按 1~6 进行编号。如对自动映射结果不满意，您可在打印设置页面中手动重新配置。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-2.png)

需注意的是，Studio 在进行喷嘴映射时，依据的是**切片文件中的耗材设定**，而非实际映射的耗材信息。因此，建议您先同步打印机上的耗材信息，以确保映射设置的准确性。

由于切片阶段已为每种耗材设定了所需的喷嘴类型（包括直径与流量），在重新映射时，**不符合要求的喷嘴将在列表中显示为灰色不可选**，您仅能从符合切片要求的喷嘴中进行选择。

![发起打印时自动将材料映射到不同热端](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-16.png)

完成重新映射后，若新配置会导致耗材消耗量增加，软件将显示**预估的耗材消耗增量**，方便您评估调整后的影响。

![手动修改映射后，耗材消耗量增加会有相应的提醒](https://public-cdn.bblmw.com/wiki/new/h2c/manual/bambu-studio-operation/image-18.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
