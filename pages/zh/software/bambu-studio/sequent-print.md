---
path: zh/software/bambu-studio/sequent-print
title: "逐件打印"
description: ""
tags: []
created: 2023-07-19T15:45:30.579Z
updated: 2024-05-28T10:51:34.869Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/sequent-print
---

# 概述

当一盘里有多个打印对象时，您可以选择按照默认的方式同时打印多个模型（逐层打印），也可以选择按顺序打印它们。按顺序依次打印模型可以减少模型之间的空驶造成的拉丝漏料。如果其中一个模型打印失败了，通常也不会影响到其它模型的打印。您可以在**特殊模式**里开启**逐件打印**功能：

![](https://wiki.bambulab.com/software/bambu-studio/seq-print/启用逐件打印.png)

# 相关参数

与逐件打印相关的参数有四个：

- `extruder_clearance_max_radius`: 表示**工具头周围的最大避让半径，**其他模型摆放在这个区域之外是安全的。工具头不同方向的避让距离实际上是不同的，不过由于逐件打印的顺序是可调整的，这里我们要求任意两个对象至少相隔最大避让距离，
- `extruder_clearance_height_to_lid`: 表示**Z=0时构建板和打印机顶部之间的距离**。
- `extruder_clearance_height_to_rod`: 表示**Z=0时构建板和最低碳杆之间的距离**。
- `printable_height`: 表示**打印机可打印的最大高度**。

![print_by_object.png](https://wiki.bambulab.com/x1/troubleshooting/hmscode/microlidar/print_by_object.png)

# 打印限制

当你选择了**逐件打印，**不同模型之间的xy距离应大于 **extruder\_clearance\_max\_radius (工具头最大避让半径).**

当你用鼠标在盘上拖动模型时，每个对象周围都有一个圆圈，它通过**工具头最大避让半径/2**的距离将对象区域扩展开。如果两个对象之间的距离小于**工具头最大避让半径**，则会弹出错误提示：

![](https://wiki.bambulab.com/software/bambu-studio/seq-print/对象靠太近提示.png)

如果有两个对象在Y方向上有交集，那么先打印的对象高度应该小于 **extruder\_clearance\_height\_to\_rod（Z=0时构建板和最低碳杆之间的距离）;**

![](https://wiki.bambulab.com/software/bambu-studio/seq-print/逐件打印高度限制.png)

上图中方块-1和方块-2在y方向相交，先打印方块-1再打印方块-2，则方块-1高度应小于**extruder\_clearance\_height\_to\_rod（Z=0时构建板和最低碳杆之间的距离）**；否则将弹出错误提示，并且在此对象的该高度周围显示一个圆圈。

如果该对象在y方向上没有与其他对象相交，或者它是在y方向上有相交的对象中后打印的对象，则该对象的高度需要小于**extruder\_clearance\_height\_to\_lid（Z=0时构建板和打印机顶部之间的距离）**或者**printable\_height（打印机可以打印最大高度）。**可以分为以下两种情况：

![](https://wiki.bambulab.com/software/bambu-studio/seq-print/高度不能高于热床到顶盖.png)

上图中方块-1和方块-2在y方向相交，先打印方块-1再打印方块-2最后打印方块-3，则方块-1高度应小于**extruder\_clearance\_height\_to\_lid（Z=0时构建板和打印机顶部之间的距离）**；否则将显示弹出错误提醒，并且在此对象的该高度周围显示一个圆圈。

如果该对象是最后打印的，那么它的高度只需要小于**printable\_height（打印机可以打印高度）**。

![](https://wiki.bambulab.com/software/bambu-studio/seq-print/高度不超过可打印最大高度.png)

在上图中，方块-3作为最后一个打印的对象，那么它的高度可以大于**extruder\_clearance\_height\_to\_lid（Z=0时构建板和打印机顶部之间的距离）**，只需要小于**printable\_height（打印机可以打印高度）**。

# 调整打印顺序

您可以通过在**对象**列表中拖动对象来调整打印顺序，如下图所示。也可以使用快捷键“**Ctrl+E**”来启用/关闭打印顺序的标签。

![](https://wiki.bambulab.com/software/bambu-studio/seq-print/拖动调整打印顺序.gif)
