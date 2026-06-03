---
path: zh/software/bambu-studio/object-list
title: "对象列表"
description: ""
tags: []
created: 2023-08-25T11:18:32.708Z
updated: 2024-05-28T10:54:34.891Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/object-list
---

# 对象列表在哪里

对象列表在Bambu Studio的左下方，您可以通过在这里点击，切换到“全局”或者“对象”模式。（了解更多关于“全局”和“对象”的关系，请[参考切片参数设置指南](how-to-set-slicing-parameters.md)）

![](https://wiki.bambulab.com/software/bambu-studio/object-list/global-objects1.png)

对象列表里，可以清晰地看到整个项目的结构，其层次结构包括以下内容：

- 盘
- 对象
- 零件
- 修改器、负零件、支撑屏蔽和支撑生成器
- 每个对象/零件的自定义参数

# 功能介绍

## 为指定对象/零件自定义参数

单击一个或者多个对象，左下角会自动显示参数设置面板，参数值源自“全局”参数。在“对象”里，您可以对指定对象或者零件自定义参数。（对象与零件的区别，请参考[拆分为对象/零件](split-to-objects-parts.md)）  
对于需要进行特殊参数设置的对象，您可以在对象列表对其进行修改。  
比如，在盘上放置了三个对象（正方体、圆锥和圆柱体），它们的填充密度为5%。将设置模式从“全局”改为“对象”，然后将立方体的填充密度设置为20%。切片后，立方体的填充密度变为20%，其他对象的填充密度保持在5%（全局值）。对象级别的参数会覆盖全局级别的参数。详细请参考[参考切片参数设置指南](how-to-set-slicing-parameters.md)

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/%E5%AF%B9%E8%B1%A1.png)

*提示：Bambu Studio 支持选择多个对象并一起设置它们的参数值。*

## 对象的状态

下面解释了对象/零件特定图标的作用。

|  |  |  |
| --- | --- | --- |
| 图标 | 状态 | 描述 |
|  | 可打印 | 点击此图标可切换它的状态。 如果开启，它将被切片打印。 否则，在切片过程中将跳过它。 |
|  | 耗材丝 | 代表它当前的耗材丝号。 点击此该图标可选择耗材丝颜色号。 |
|  | 支撑绘制 | 绘制了支撑屏蔽/支撑生成器。 点击此图标可编辑它的支撑绘制。 |
|  | 涂色 | 已涂色。 点击此图标可编辑这它的涂色状态。 |
|  | 自定义参数 | 点击此图标可重置它的所有设置。 |

这些图标的功能演示如下所示：

![](https://wiki.bambulab.com/software/bambu-studio/object-list/example.gif)

## 为指定对象/零件重命名

当您导入从 CAD 软件导出的数十个具有通用名称的对象/零件时，有时可能需要对它们重命名。

有下面两种方法，可以重命名对象列表中的对象/零件。

- 双击对象列表中的对象/零件名称以对其进行重命名。
- 单击对象/零件，然后按键盘上的空格键。
