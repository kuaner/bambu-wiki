---
path: zh/software/bambu-studio/split-to-objects-parts
title: "拆分为对象/零件"
description: "了解 Bambu Studio 中「拆分为对象」与「拆分为零件」的区别与用法，掌握模型拆分技巧，轻松实现多色打印、大模型分件打印与零件参数设置。"
tags: []
created: 2023-08-23T12:19:43.816Z
updated: 2026-06-09T06:11:17.785Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/split-to-objects-parts
---

## 概述

一个 STL 文件可以包含多个壳体，每个壳体都由三角形面片组成。打开 STL 文件时，即使文件中包含多个独立壳体，它们也会作为一个整体对象被导入。

在以下情况下，我们需要将这些壳体拆分开：

- 拆分后可以使模型更易于打印时；
- 方便对模型进行涂色；
- 需要为不同的壳体设置不同的打印参数时。

为此，Bambu Studio 提供了两种拆分工具，它们都位于顶部的工具栏上：

1. 「**拆分为对象**」
2. 「**拆分为零件**」

![to_parts_and_to_object.png](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/to_parts_and_to_object.png)

  

## 拆分为对象

「**拆分为对象**」会将模型中所有不相连的壳体拆分成单独的对象。拆分后，每个壳体都会在“对象”面板中显示为一个独立的对象。

此功能通常适用于以下场景：

- 模型太大，无法整体打印。
- 需要多色打印，但打印机未配置 AMS。

拆分为对象后的模型在打印完成后，需将各对象**手动组装**在一起，**拼成完整的模型**。

![zh_split_to_objects.webp](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/zh_split_to_objects.webp)

拆分为对象后，可以移动、缩放、旋转每个对象，为其分配不同的打印设置，或单独打印。

![zh_split_to_objects_2.webp](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/zh_split_to_objects_2.webp)

  

## 拆分为零件

「**拆分为零件**」会保留对象本体，并在其下创建多个零件。拆分后，每个零件都保留在原来的位置上。

此功能通常用于将模型拆分为多个零件，以便为每个零件分配不同的耗材或颜色。这样即可**一次打印出多色模型**，**无需后续组装**。

![zh_split_to_parts.webp](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/zh_split_to_parts.webp)

> **✅ 提示：** 可通过两种方式快速选中零件：从「**对象**」列表中选择，或使用 `Alt + 鼠标左键`。

## 对象和零件的区别

**零件是对象的子集**，它们主要在**选中方式**、**移动规则**、**自动摆盘效果**上有所不同，具体如下：

1. **选中方式**：在盘上用鼠标点击模型时，只能选中对象，无法直接选中某个零件。如需移动某个零件，可以先用以下任一方式选中它，再进行移动：

   - 在「**对象**」列表中选中该零件。
   - 使用 `Alt + 鼠标左键` 选中该零件。

下图中，「**Ifs\_elephant.stl**」是一个对象，「**Ifs\_elephant.stl\_1**」是其中的一个零件。

![select_specific_part.webp](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/select_specific_part.webp)

2. **移动规则**：单个零件可在 Z 方向上自由移动，无需接触打印板；而对象必须至少有一面接触打印板。

下图中，「**Ifs\_elephant.stl**」是对象，「**Ifs\_elephant.stl\_1**」是其中的零件。可以看到，「**Ifs\_elephant.stl**」无法向上移动，而「**Ifs\_elephant.stl\_1**」可以向上移动。

![parts_move_on_z.webp](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/parts_move_on_z.webp)

3. **全局整理**：全局整理的「**自动摆放**」功能仅针对**对象**设计，不会对零件生效。

   - 「**拆分为对象**」后，使用「**自动摆放**」会重新摆放各个对象。
   - 「**拆分为零件**」后，使用「**自动摆放**」不会重新摆放零件（盘上依然只有一个对象）。

![auto_rearrange.webp](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/auto_rearrange.webp)

  

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
