---
path: zh/x1/manual/manual-flow-rate-tuning
title: "手动调节流量以获得更好的打印效果"
description: ""
tags: []
created: 2022-09-17T10:36:48.265Z
updated: 2026-05-13T10:11:06.121Z
source: https://wiki.bambulab.com/zh/x1/manual/manual-flow-rate-tuning
---

## 为什么要微调流量？

X1 系列打印机能够根据使用的耗材自动校准流量。 但在某些情况下，需要微调流量以确保良好的顶层光洁度，这也将提高打印件的整体表面质量。

## 在何处更改耗材流量？

对于不同的耗材，每个切片配置文件都设置了默认的流量比例。Bambu 官方耗材已经经过调试，使用默认参数可以获得良好的表面光洁度。但在使用其他耗材时，可能需要更流量比的数值。

![flow_rate_value](https://wiki.bambulab.com/x1/manual/flow-rate-tuning/flow_rate_value.png)

## 使用正确流量参数打印的示例

在下图中，您可以看到使用调整正确的流量打印的 PLA 打印示例。

线条正确对齐，顶部表面摸起来很光滑。

![](https://wiki.bambulab.com/x1/manual/flow-rate-tuning/perfec_extrusion.jpg)

## 如何微调流量？

为了获得正确的流量值，只需使用不同的流量值对同一个简单的模型进行切片并打印，直到找到正确的值，从而获得最好的打印效果。

我们建议采用[此测试模型](https://wiki.bambulab.com/x1/manual/flow-rate-tuning/flowrate_test_model.stl)并使用默认配置文件值对其进行切片。

**层高：0.2 mm**  
**墙层数：2**  
**顶部壳体层数：4**  
**底部壳体层数：3**  
**填充率：15%**

如果流量太高，顶层会出现过度挤压，这会产生不均匀的线条。 如果发生这种情况，则需要降低流量并重新打印进行验证。

![](https://wiki.bambulab.com/x1/manual/flow-rate-tuning/over-extrusion.jpg)

同时，如果流量太低，顶层会出现挤出不足，线条无法连接，线条之间存在间隙。如果发生这种情况，则需要增加流量并重新打印进行验证。

![](https://wiki.bambulab.com/x1/manual/flow-rate-tuning/under-extrusion.jpg)

我们建议以较小的增量进行调整。±0.03 到 ±0.05 的变化会在打印的顶层质量上产生显著差异，但在某些情况下，变化可能更大。
