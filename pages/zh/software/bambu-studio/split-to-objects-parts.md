---
path: zh/software/bambu-studio/split-to-objects-parts
title: "拆分为对象/零件"
description: ""
tags: []
created: 2023-08-23T12:19:43.816Z
updated: 2025-07-17T04:04:01.459Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/split-to-objects-parts
---

一个STL文件可以包含多个壳体，每个壳体都由三角形面片组成。当打开STL文件时，它可能包含多个独立壳体，但也会被作为一个整体的对象导入。

有时，为了使模型易于打印、涂色方便或者为不同的壳进行不同的打印参数设置，我们需要对这些壳体进行拆分。

Bambu Studio提供了两种拆分工具：“拆分为对象”和“拆分为零件”，它们都位于顶部的工具栏上。

# 拆分为对象

“拆分为对象”为每个壳体创建了一个单独的对象，并可以将每个新创建的对象放置在盘上。  
这个工具可以解决模型太大而无法打印，或者需要多色打印但没有给打印机配置AMS的问题。在打印完成后需要将各对象放置在一起，组装成完整的模型。

![](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/chaifenweiduixiang.gif)

# 拆分为零件

“拆分为零件”会保留对象本体，并且给对象创建多个零件。拆分后，每个零件将保留在原来的位置上。

这个工具可以将模型分割成多个零件，通常用于轻松设置每个零件区域的耗材颜色。可以一次打印出多色模型，无需组装。

![](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/chaifenweilingjian.gif)

（技巧：可以通过从“对象”列表里选择，或者Alt+鼠标左键，可以快速选中零件）

# 对象和零件的区别

1. 零件是对象的子集

2. 在盘上用鼠标点击模型时，只能选中对象，但是无法选中某个零件。如果您想要移动某个零件时，需要在“对象”列表里选中该零件，或者Alt+鼠标左键选中零件，然后移动它。

下图中“BE-body\_stl”是一个对象，“BE-body\_stl\_5”是其中的一个零件。

![](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/yidong.gif)

3.单个零件可以在Z方向上自由移动，不需要接触打印板，但一个对象必须要有一面是接触打印板的。  
下图中“BE-body\_stl”是一个对象，“BE-body\_stl\_5”是其中的一个零件。可以看到“BE-body\_stl”无法向上移动，但是“BE-body\_stl\_5”可以向上移动。

![](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/lingjianxuankong.gif)

4. “拆分为对象”后，使用“自动摆放”功能会把对象们重新摆盘，但是“拆分为零件”后，使用“自动摆放”功能，不会把零件进行重新摆盘（盘上依然只有一个对象）。“自动摆放”功能是针对对象而设计的，不会对零件进行摆放。
