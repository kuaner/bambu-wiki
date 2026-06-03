---
path: zh/software/bambu-studio/plates_management
title: "盘功能介绍"
description: "本页介绍了Bambu Studio中的“盘”管理。"
tags: []
created: 2023-08-29T07:05:24.397Z
updated: 2024-05-28T10:55:12.861Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/plates_management
---

# 为什么需要盘？

在过去的3D打印中，如果有大型模型由许多物体对象组成时，我们需通常要将这些模型/对象分成多个组：

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/plate_all_cn.png)

在一个打印板上切片并打印模型/对象后，我们需要将另一组模型/对象移到热床上，比较费时还有可能出错。

为了改善这种情况，您可以将这些模型/对象放入不同的 3mf 文件中，每个文件对应一组打印模型，使准备和打印过程更加顺畅。

例如，我们使用 6 个不同的 3mf 文件来存储上述中的组：

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/plates_all.png)

虽然这种方法比以前的方法要好，但在不同的 3mf 文件之间进行切换的效率仍然很低，而且对整个模型的切片和打印也不友好。  
此外，在不同的 3mf 文件之间重新整理对象也很困难，尤其是当我们想开始一个新的打印，将所有打印失败的对象进行分组时。

为了解决这个问题，BambuLab 首次推出了“盘”的功能。

有了盘，您可以将一个模型的所有模型/对象放入一个 3mf 文件，并摆放在不同的盘上，每个盘代表一个打印任务。  
您可以在不同盘之间快速切换，进行单独打印，并在装配视图中看到整个模型的全貌。

# 盘的介绍

## 什么是盘？

盘是一个模型容器，是 Bambu Studio 中的切片和打印的单元。

我们可以创建多个盘，并将模型放入不同的盘中， 可以进行多盘切片、预览和打印。

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/slice_print_plates1_cn.gif)

上图中，该项目有7个盘，编号为01到07。  
盘01是当前的盘，盘01到06是指之前要打印的模型/对象组（这个例子中，盘07是需要另外采购的零件，如螺丝等，所以不需要打印）

## 盘的主要功能

- 最多支持36个盘，以N\*N（数字）样式排列展示，每个盘的原点位于它的左下角
- 支持盘的基本操作，如添加/删除/选择
- 支持盘[自动摆放](auto-arranging.md)/[自动朝向](auto-orientation.md)功能
- 支持盘锁定/解锁
- 在全局模式下，使用[自动摆放](auto-arranging.md)，会自动创建新盘
- 支持盘的切片/预览/打印
- 支持将盘存储为3mf文件和添加3mf文件到盘

## 高效打印零件

在 Bambu Studio 中，我们可以轻松添加新盘/删除盘，只需将对象拖到另一个盘上即可重新安排不同的打印任务，可以在盘上自动摆放零件。我们也可以轻松地将所有盘中打印失败了的对象进行分组，方便再次打印。

### 添加盘

可以在工具栏，点击‘“添加新盘”。

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/add_plate_cn.gif)

### 删除盘

我们可以通过每个盘，右上角的“X”图标来删除该盘。

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/delete_plate_cn.gif)

### 在不同盘上移动模型对象

我们可以在不同盘之间移动模型对象；只要模型对象移动到了一个盘的区域，那它就属于该盘。

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/move_between_plates_cn.gif)

### 盘的选择/切片/预览/打印

切片时，可以选择“切片单盘”或者“切片所有盘”。如果选择了“切片单盘”，会对你当前选中盘进行切片，您也可以在“预览”中，点击左边的各个盘的图示，进行其他盘或者所有盘的切片。

选择盘后，切片/预览/打印都将切换到该盘的模型对象的图示。

下图以盘05为例，对它进行“切片单盘”和“打印单盘”操作。

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/slice_print_plate_cn.gif)

### 模型在单盘上自动摆放

您可以通过点击每个盘右上角的“自动摆放”图标，自动摆放盘上的模型。

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/auto_arrange_cn.gif)

注意，它只会影响该盘上的模型对象。

### 模型在单盘上自动朝向

您可以通过在每个盘右上角的“自动朝向”图标，自动调整摆放盘上的模型的朝向。

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/autochaoxiang_cn.gif)

注意，它只会影响该盘上的模型对象。

### **全局自动排列创建/删除板块**

在全局模式下，进行“自动摆放”时，Bambu Studio会自动计算出盘数，并且会根据结果增加/删除盘。

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/global_arrange_cn.gif)

### 盘的锁定/解锁

您可以通过在每个盘右上角的“锁”图标，来锁定/解锁盘。  
如果该盘处于锁定状态，则无法对其进行自动朝向和自动摆盘；需要解锁之后，才能对改盘上的对象进行“自动朝向”和“自动摆盘”操作。  
如下图所示：

![](https://wiki.bambulab.com/software/bambu-studio/plates-management/lock_plate_cn.gif)
