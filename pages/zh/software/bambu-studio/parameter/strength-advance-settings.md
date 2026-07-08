---
path: zh/software/bambu-studio/parameter/strength-advance-settings
title: "强度高级设置"
description: ""
tags: []
created: 2024-03-04T11:29:51.406Z
updated: 2026-07-07T01:43:18.513Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/strength-advance-settings
---

在Bambu Studio中，您可以**工艺——强度——高级**中对强度相关的参数一些高级设置。

![strength_advance_zh.png](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/strength_advance_zh.png)

## 填充/墙 重叠

填充区域的走线被轻微扩大，并和墙产生重叠，适当的重叠产生更好的粘接。该参数的本质是控制所有填充走线 **（这里的“填充”指的是所有水平方向的壳体，包括稀疏填充/内部实心填充/顶面/底面/桥接）** 与垂直面（内外墙）的重叠，可以增加或者减少它们之间的铆接。数值表示为相对稀疏填充的线宽的百分比，默认值是15%。

- 当重叠设置为50%，从下图可以看出稀疏填充的走线有50%宽度是和内墙重叠了，重叠率设置太高会导致模型表面凸起从而影响外观。

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E5%A1%AB%E5%85%85%E5%A2%99%E9%87%8D%E5%8F%A050.png)

- 重叠率还可以设置为负值，负值说明填充和墙完全不重叠，且中间留有一定的间隙。例如重叠率设置为-50%，从下图可以看出，稀疏填充和内墙已经完全没有重叠，且中间还有50%线宽的间隙。

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E5%A1%AB%E5%85%85%E5%A2%99%E9%87%8D%E5%8F%A0-50.png)

- 不过如果重叠率设置为负数，有可能会影响顶面和底面的外观，因为顶面和底面的走线将不会与墙铆接。

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E5%BA%95%E9%9D%A2%E5%A2%99%E9%87%8D%E5%8F%A0-50.png)

## 填充方向

填充图案的角度，决定填充走线的开始或整体方向。**该参数也是调整所有填充走线的方向，包括顶面、底面、稀疏填充和内部实心填充（外部桥接除外）。**

- **填充方向45°**：

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E5%A1%AB%E5%85%85%E6%96%B9%E5%90%9145%C2%B0.png)

- **填充方向90°：**

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E5%A1%AB%E5%85%85%E6%96%B9%E5%90%9190%C2%B0.png)

## 桥接方向

**设置外部桥接的架桥方向。** 如果设置为0，该角度将会自动计算。否则外部的桥接将用提供的值。180°表示0度。

- **桥接方向45°：**

![](https://wiki.bambulab.com/bambu-studio/parameter/bridge/%E6%A1%A5%E6%8E%A5%E6%96%B9%E5%90%9145%C2%B0.png)

- **桥接方向90°：**

![](https://wiki.bambulab.com/bambu-studio/parameter/bridge/%E6%A1%A5%E6%8E%A5%E6%96%B9%E5%90%9190%C2%B0.png)

关于更多桥接设置的介绍，可以参考wiki：[如何在 Bambu Studio 中提升桥接质量](../../../filament-acc/filament/print-quality/bridging.md)

## 稀疏填充最小阈值

小于这个阈值的稀疏填充区域将会被内部实心填充替代。 也就是说，**如果内部填充区域的面积小于这个设定值，该区域的填充走线类型将会用内部实心填充，否则将采用稀疏填充。主要目的是改善强度，狭小的区域内用实心填充填满，避免强度过低导致断裂。** 下面用一个1cm³大小的立方体作为示例：

- **稀疏填充最小阈值15mm²：**

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/1%E7%A8%80%E7%96%8F%E5%A1%AB%E5%85%85%E6%9C%80%E5%B0%8F%E9%98%88%E5%80%BC15.png)

- **稀疏填充最小阈值100mm²：**

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/2%E7%A8%80%E7%96%8F%E5%A1%AB%E5%85%85%E6%9C%80%E5%B0%8F%E9%98%88%E5%80%BC100.png)

## 合并填充

自动合并若干层稀疏填充一起打印，启用该功能可以缩短打印时间时间。**合并填充的逻辑是，在不超过喷嘴直径的范围内，取内外墙层高的最大整数倍作为稀疏填充的层高。**

例如，选择0.4的喷嘴预设，在开启合并填充后，0.08mm和0.2mm外墙层高稀疏填充层高取0.4mm（前者每打5层外墙打印1层稀疏填充，后者每打印2层外墙打印1层填充），0.12mm外墙层高稀疏填充用0.36mm层高（每打3层外墙打印1层稀疏填充），0.16mm外墙层高稀疏填充用0.32mm层高（每打2层外墙打印1层稀疏填充）。**而0.24mm和0.28mm层高由于取倍数后超出喷嘴直径，没有合适的稀疏填充层高，所以无法使用合并填充功能。**

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E5%90%88%E5%B9%B6%E5%A1%AB%E5%85%85%E6%BC%94%E7%A4%BA.gif)

## 识别狭窄内部实心填充

此选项用于自动识别内部狭窄的实心填充区域。开启后，将对狭窄实心区域使用同心填充图案打印，这样可以明显加快速度，否则使用默认的直线填充图案。

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E8%AF%86%E5%88%AB%E5%86%85%E9%83%A8%E7%8B%AD%E7%AA%84%E5%AE%9E%E5%BF%83%E5%A1%AB%E5%85%85%E5%BC%80.png)

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E8%AF%86%E5%88%AB%E5%86%85%E9%83%A8%E7%8B%AD%E7%AA%84%E5%AE%9E%E5%BF%83%E5%A1%AB%E5%85%85%E5%85%B3.png)

## 确保垂直外壳厚度

该参数用于在斜面表面附近添加实心填充，以保证垂直外壳厚度(顶部+底部实心填充）。**需要保证的垂直外壳厚度取决于设置的顶面壳体厚度（层数）和底面壳体厚度（层数）。**

![layers.png](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/layers.png)

下图是一个示例，如果设置了底面壳体层数是4层并启用了**确保垂直外壳厚度**，那么在切片斜面的时候，垂直方向上不足四层的部分，会添加内部实心填充层。

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E7%A1%AE%E4%BF%9D%E5%9E%82%E7%9B%B4%E5%A3%B3%E4%BD%93%E5%8E%9A%E5%BA%A6%E5%8E%9F%E7%90%86.png)

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E7%A1%AE%E4%BF%9D%E5%9E%82%E7%9B%B4%E5%A3%B3%E4%BD%93%E5%8E%9A%E5%BA%A6%E6%BC%941.png)

## 内部桥接支撑厚度

(由于版本迭代，已移除该参数。新算法可确保成功实现桥接目标。)

如果开启,Studio会沿着内部桥接的边沿在其下方生成支撑轮廓。这些支撑轮廓可以防止悬空地打印内部桥接并提高顶面质量,特别是是在填充密度较低的情下。这个设置用于调整支撑轮廓的厚度。0表示关闭此特性。

如下图所示，当桥接支撑厚度设为0，内部桥接的边沿下方就没有形成完整的支撑轮廓。而把它设置为0.8后，将会生成一圈厚度0.8mm的支撑轮廓。**注意：该功能只用稀疏填充密度不为0时才起作用。**

![](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/%E5%86%85%E9%83%A8%E6%A1%A5%E6%8E%A5%E5%8E%9A%E5%BA%A6%E6%BC%94%E7%A4%BA.gif)

## 单调线空驶延伸

通常情况下，当打印机打印完一条线段后，喷嘴会立即移动到下一条线段的起始点。启用此设置后，喷嘴会在移动前继续沿直线方向多移动一小段距离（进入内壁），这可以让打印件的表面更加平滑。

- 下图示例展示了增大和减小单调线空驶延伸 **%** 数值对打印质量的影响。

![monotonic_line_travel_extend_ch.png](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/monotonic_line_travel_extend_ch.png)

**设置步骤：**

**步骤 1. 在 Bambu Studio 中开启开发者模式。**

点此查看如何启用开发者模式

**步骤 1 - 进入偏好设置**  
点击顶部导航栏中的菜单选择偏好设置，或使用快捷键 Ctrl+P。

![s1.jpg](https://wiki.bambulab.com/software/bambu-studio/dev-mode/s1.jpg)

**步骤 2 - 启用开发者模式**  
在偏好设置中，下拉找到开发者模式，勾选该功能。

![s1.jpg](https://wiki.bambulab.com/software/bambu-studio/dev-mode/s2.jpg)

✅ 若需关闭该模式，也可执行同样的操作步骤。

**步骤 2. 修改顶面/底面图案：** 在“强度”设置下，仅当顶面图案或底面图案设置为“单调线”时，此功能才会生效。

![mono_line_zh.png](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/mono_line_zh.png)

**步骤 3. 数值修改** ：在“强度” → “高级 → “单调线空驶延伸” 修改数值，单位为占线宽的百分比（%）。下图展示了空驶路径（蓝线）随数值变化的情况。

![different_monotonic_line_travel_extend_values.png](https://wiki.bambulab.com/bambu-studio/parameter/strength-advance-settings/different_monotonic_line_travel_extend_values.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
