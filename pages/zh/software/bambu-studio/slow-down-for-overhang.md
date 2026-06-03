---
path: zh/software/bambu-studio/slow-down-for-overhang
title: "悬垂降速"
description: ""
tags: ["悬垂降速"]
created: 2023-07-11T13:27:58.204Z
updated: 2026-01-26T09:45:29.761Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/slow-down-for-overhang
---

# 概述

在打印悬垂面时，为保证更好的打印效果，Bambu Studio可以根据您的模型自动降低内外墙打印速度。

# 功能介绍

传统的切片软件对不同的走线类型有特定的速度设置，例如，内墙速度，外墙速度，稀疏填充速度，实心填充速度等。内外墙速度对打印模型的表面质量有很大的影响，特别是对于悬垂表面。

一般来说，当整体打印速度较慢时，悬垂面质量通常不会有问题。但对于高速打印场景，即便是层面积大、单层打印时间长且冷却充足，过快的墙速度依然可能导致悬垂表面质量不及预期。对于有明显悬垂结构的模型，当你不想启用支撑又希望悬垂面的打印质量较好时，我们通常建议采用较低的墙速度。然而，模型即使在同一层高度的不同部分也会有不同的悬垂度。**为了在打印时间和打印质量之间取得平衡**，有必要对悬垂区域进行检测，并以较慢的速度打印。因此我们在Bambu Studio中引入了“**悬垂降速**”功能来控制不同悬垂部分的墙体速度。

启用“悬垂降速”后，墙的挤出线会根据不同的悬垂程度分成几组。不同**悬垂度**的线条会被映射到不同的打印速度上。从微观的角度来看，悬垂度以百分比表示，**它表示的是挤出线条不受下层的支撑的部分所占挤出线宽的比例**，图如下所示**（L2=挤出线宽，L1=悬空部分的宽度）**。

![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/overhang-degree.png)

**如何计算悬垂程度**

计算墙体每条挤出线的悬垂度需要较长的时间进行二维图形运算。因此，我们把**悬垂度分为四个区间**，以加快切片速度。

# 操作指南

 悬垂降速功能在Bambustudio中默认开启，你可以在下图位置修改不同区间的墙速度。**注意：速度设为0mm/s代表着不降速。**

![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/悬垂降速.png)

当您不需要此功能时，取消勾选“**悬垂降速**”，此时悬垂速度会被隐藏并且不起作用。

![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/关闭悬垂降速.png)

## 应用案例

同时打印两个相同的模型，并为其中一个对象启用“**悬垂降速**”，在速度预览页上可以看到不同的悬垂打印速度。

(感谢这个测试模型的设计者，可以在这里下载该模型:  <https://github.com/kickstarter/kickstarter-autodesk-3d>)

![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/开启悬垂降速对比.png)

悬垂质量对比如下图所示。左图的模型启用了“**悬垂降速**”，右图是模型禁用了“**悬垂降速**”。

我们可以看到左边模型的悬垂面质量比右边好很多。

![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/result1.png)
![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/result2.png)

# 特别说明

1. 悬垂度 0% 表示无悬垂，悬垂度为 100% 时表示悬空墙（即定义为桥接）。**请注意，10% 不包括在 (10%，25%) 部分，100% 也不包括在 [75%，100%) 部分。**

2. 所以在某些情况下，模型的倾斜表面的悬垂度可能达到 100% 从而无法成功启用悬垂降速，而是会采用**桥接**或**完全悬垂墙**的速度进行打印。这与模型本身、线宽设置等有关，需要具体分析。

3. Bambu Studio 1.9.1版本引入了**平滑过渡悬垂调速**功能，所以悬垂区域的速度不再只根据4个区间来分配固定的速度，而是均匀地根据每个区间内的悬垂度来映射对应的过渡速度，这样使得悬垂降速的过渡更加平滑。例如：当悬垂度是25%，对应的速度是50mm/s，悬垂度是50%，对应速度是30mm/s。故每增加1%的悬垂度，就降速 (50-30) / (50-25) = 0.8mm/s。则当采样得到的悬垂度是40%的时候，该部分悬垂的打印速度就是50 - (40-25) \*0.8=38mm/s。

**注：该平滑调速功能仅在“经典”墙生成器下可用，**且有些模型可能单层打印时间较短，故实际打印的速度还会受到[冷却降速](auto-cooling.md)的影响。

![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/悬垂降速区间.png)
![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothoverhang_1.png)

**平滑过渡悬垂调速效果**
