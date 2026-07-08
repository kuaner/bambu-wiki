---
path: zh/filament-acc/filament/print-quality/overhang
title: "如何打印模型悬垂部分"
description: "本文将为您介绍什么是悬垂以及如何提升悬垂部分的打印质量。"
tags: ["打印质量", "悬垂"]
created: 2023-12-10T05:35:36.604Z
updated: 2026-06-26T08:18:41.928Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/overhang
---

## 什么是悬垂？

当模型的某一部分向外延伸，但下面没有实体作为承托时，这部分就属于“**悬垂结构**”。由于 FDM 3D 打印是“一层一层往上堆叠”的，如果下面没有支撑，材料就会因为**重力作用**而下垂或变形。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82_%E6%A8%A1%E5%9E%8B.png)

耗材在这个位置打印时容易由于重力作用下垂，所以此时，悬垂位置下方的[**支撑**](../../../software/bambu-studio/support.md)**结构**就像一张安全网，为上层的模型提供稳固的支撑力量。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82+%E6%94%AF%E6%92%91.png)

### 常见的悬垂有哪些？

常见的悬垂结构如下图，指的是模型在竖直方向的有一定的倾斜角度或者模型有悬空的部分，均属于悬垂的范畴。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82x5.png)

## 打印悬垂部分失败的原因

打印悬垂表面时失败的**直接原因，**是由于**挤出的耗材没有及时冷却，从而无法准确粘接在目标位置上而导致的下坠。**

具体打印情况可以参考下图：左边为悬垂质量较差的模型；右边为悬垂质量较好的模型。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/bad_overhang.jpg)

## 解决方法

出现打印悬垂部分失败时，建议根据实际情况尝试以下方法来改善：

首先观察或在 Bambu Studio 中测量模型的**悬空倾斜角度**，从而判断角度是否过小。可以尝试按照下面列出的具有针对性的优化参数设置，以改善悬垂质量。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82%E5%9B%BE%E8%A7%A3-1.jpg)

> **注意**：
>
> - 此处所指的模型**悬空倾斜角度**，指的是模型倾斜部分的平面与热床面之间所形成的夹角。
> - 与之相对的是，**悬垂阈值**是指挤出线条中不受下层支撑部分在挤出线宽中的占比，两者并不相同。
> - 如下图展示了在 Bambu Studio 中**支撑阈值角度**分别设置为 **5°** 和 **85°** 时的支撑生成的对比效果。输入的角度数值越大，生成的支撑越多。  
>   ![](https://wiki.bambulab.com/filament-acc/filament/print-quality/mergedimages_(8).png)

### 开启支撑

如果模型的悬空倾斜**角度过小**（例如小于45°时），建议您在 Bambu Studio 中**开启支撑**结构以提高打印质量。更多关于支撑的设置您可以参考[支撑耗材与支撑功能的介绍](../../../software/bambu-studio/support.md)了解更多。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82s_1.jpg)

### 降低喷嘴温度

**如果模型的悬空倾斜角度较大，建议您可以适当降低喷嘴温度。**

当悬垂部分的打印速度较慢时，降低喷嘴温度有助于减少对冷却的需求。

- 以 **PLA** 为例，可以把**其它层**喷嘴温度适当降低至 **205** 摄氏度左右；同时调高**悬垂风扇速度**至**100%**
- 对于其他官方耗材，您可以参考该[耗材指南](../../../general/filament-guide-material-table.md)以了解**耗材与各机型、喷嘴、AMS、打印板以及胶水的兼容性、适配性及参数设置**。确保温度保持在推荐范围内，同时适当降低喷嘴温度 5-10℃ 即可。
- 对于第三方耗材，建议通过打印温度塔来测试并确定最佳打印温度。温度塔的打印教程可以参考[第三方打印机校准指南](../../../bambu-studio/Calibration.md)。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82s_2.jpg)

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82s_3.jpg)

### **开启悬垂降速**

**适当降低整体打印速度，或启用悬垂降速以降低悬垂部分的打印速度。** 必要时，您可以进一步降低悬垂速度。悬垂速度一般设置在 10-60mm/s 之间，悬垂阈值越大，悬空部分的幅度也会增加，此时通常需要使用更低的速度以确保打印质量。关于悬垂降速的详细信息，请参考[悬垂降速指南](../../../software/bambu-studio/slow-down-for-overhang.md)以了解更多。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82%E9%99%8D%E9%80%9Fs_3.jpg)

### 调大冷却风扇转速百分比

**适度调大辅助风扇、部件冷却风扇的转速百分比。**如果悬垂质量一直很差，需要检查**部件冷却风扇**和**辅助冷却风扇**在打印过程是否可正常工作，可在 Bambu Studio 里开关和调节风扇转速百分比来测试（下图以 H2D 为例）。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82s_4.jpg)

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%82%AC%E5%9E%82s_5.jpg)

### 增强散热效果

**通常，打开打印机的前门和玻璃盖**可以获得更好的散热效果（一般只针对 **PLA、PETG、TPU** 类材料，其他耗材如此操作易因腔温过低而导致翘曲、层间结合变弱）。

## 打印结果对比

下面是参数调整前与调整后的悬垂模型对比图。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/%E6%89%93%E5%8D%B0%E5%89%8D%E5%90%8E%E5%AF%B9%E6%AF%94.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[*请联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
