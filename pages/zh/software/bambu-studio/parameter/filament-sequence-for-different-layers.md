---
path: zh/software/bambu-studio/parameter/filament-sequence-for-different-layers
title: "设置不同层耗材打印顺序"
description: ""
tags: []
created: 2024-03-21T12:35:28.688Z
updated: 2025-10-09T01:29:20.401Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/filament-sequence-for-different-layers
---

# **简介**

在多色（多材料）打印任务中，我们可以自定义不同层的耗材打印顺序，包括指定首层和其他层打印顺序。**在Bambu studio的准备页面，点击打印板旁的设置图标，在弹出的“盘参数设置”窗口即可设置首层和其它层耗材的打印顺序。**

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/盘参数设置.png)

# **功能操作介绍**

## **首层耗材打印顺序**

**首层耗材打印顺序分为自动和自定义两种.**

### 自动

自动分配首层打印的耗材丝顺序，分配顺序的逻辑如下：

1. 比较每个颜色区域的最小的独立轮廓，按照最小轮廓从大到小的顺序打印。如下所示，绿色部分的最小轮廓 > 橙色部分最小轮廓，所以先打绿色部分。

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/比较每个颜色区域的最小独立轮廓.gif)

2. 如果不同颜色的独立轮廓面积都一样，将会按照耗材丝列表里的先后顺序打印。

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/耗材丝列表.png)

### 自定义

在下拉列表里选择“自定义”，并拖动各颜色方块来自定义首层的打印顺序。

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/自定义首层打印顺序.gif)

## **其它层耗材打印顺序**

其它层定义的是除首层之外的所有层的打印顺序。用户可以指定具体的层高范围来自定义其打印顺序。它也有自动和自定义两种方式：

### 自动

1.尽可能让下一层打印的第一个材料 = 前一层打印的最后一个材料。如下动图所示，上一层打印的最后一个材料是红色耗材丝，那么下一层将会从红色耗材丝开始打印，尽量减少换料次数：

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/下一层的第一个颜色等于上一层最后一个颜色.gif)

2. 尽可能采用这一层的冲刷量最小的材料顺序。例如，比如耗材丝顺序 1->2->3 的总冲刷量大于 1->3->2 的总冲刷量，就会使用后者作为该层的打印顺序。

### 自定义

1. 用户可以自定义需要修改的层高范围，默认是从第二层到最后一层（end）。

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/自定义第二层到最后一层.png)

2. 也可以增加自定义层高范围区间，比如下图设置了3个层高区间，每个层高区间可以独立设置打印顺序

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/自定义层高区间1.png)

3. 如果两个层高区间有重叠部分，则重叠区间的打印顺序，优先使用排序靠后的区间打印顺序，如下图，两个区间分别是[2-10]，[5-End]。实际上将会把它拆分为[2-4]和[5-End]两个区间来定义打印耗材顺序。

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/自定义区间重叠.png)

4. 如果自定义的层高区间没有包含打印对象的所有层高，则剩余的层高将采用“自动”的逻辑来分配耗材打印顺序。如下图，设定了[2-10]层高区间的打印顺序，而模型的层高不止10层，则[11-End]的层高区间将自动分配打印顺序。

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/层高区间只设置一部分1.png)

5. 我们可以通过拖拽图中的颜色方块来定义其它层打印顺序。切片后预览可以看到，中间任何一层都采用了自定义的耗材顺序打印。

![](https://wiki.bambulab.com/bambu-studio/parameter/filament-sequence-for-different-layers/自定义其它层打印顺序.gif)
