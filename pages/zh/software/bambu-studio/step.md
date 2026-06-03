---
path: zh/software/bambu-studio/step
title: "STEP格式"
description: ""
tags: []
created: 2023-08-23T02:17:46.827Z
updated: 2024-11-14T09:38:38.969Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/step
---

STEP格式是CAD软件中广泛使用的一种标准交换格式。几乎所有的CAD软件都可以导出以STEP格式的模型或组件。这意味着装配中的模型可以很容易地在STEP文件中组合和表达，而不会损失精度。

Bambu Studio支持从STEP文件导入模型和装配。这是基于OpenCASCADE的。因此您不需要从CAD软件中导出STL模型文件，而是可以直接将STEP文件拖拽到Bambu Studio中打开并切片。这带来了很多好处，本文将会为您介绍。

## 装配体视图

大型3D模型通常由多个部分组成，需要拆分。将模型拆分为对象可以帮助我们:

- 能够打印尺寸超过打印机构建体积的模型
- 易于打印将模型分成几个部分可以使其更容易打印。
- 即使没有AMS，也能打印彩色模型(某些部分的颜色与其他部分不同)

但它也有一些缺点:

- 难以为零件上色，因为我们无法预览它们的整体外观，当用户想要基于现有的3mf项目更改颜色时难以操作。
- 不知道每个零件在最终模型中的位置。

**装配体视图解决了这些痛点。**

![](https://wiki.bambulab.com/software/bambu-studio/step-format/%E8%A3%85%E9%85%8D%E4%BD%93%E8%A7%86%E5%9B%BE.gif)

当通过STEP文件导入模型时，Bambu Studio将自动创建它的装配体视图，它会记住每个部件的相对位置。

如果模型在Bambu Studio中被分割成多个对象，它的装配体视图将不会改变。您可以切换到装配体视图进行不同的操作。例如，更方便地为模型的各个部分上色。

您可以根据实际需要来探索模型，轻松地为它的内部部件着色(如果需要)并查看每个部件在装配后的具体位置。

## 在G代码中实现更多的圆弧移动

3D模型大多表示为三角形网格，这意味着最终的切片和打印路径是密集的线段。当打印机速度较慢时，这些密集的路径对打印质量没有明显的不良影响。但当打印速度较高时，在线段的拐点处会产生大量的瞬态脉冲信号，从而产生噪声和振动。为了缓解这个问题，Bambu Slicer通过在一定可接受的公差范围内拟合来生成弧线路径。这样可以减少线段拐点的数量，使路径更加平滑，并减少高速打印中的振动。更多的内容可以参考：[圆弧运动 | Bambu Lab Wiki](acr-move.md)

STEP文件保存模型没有精度损失，原始的STEP文件是矢量模型，在导入STEP文件时，Bambu Studio根据小于默认圆弧拟合公差一半的公差自动将模型转换为三角形网格。也就是说，在Bambu Studio中会把它转换成高精度的STL模型。因此，可以保留更多的模型轮廓细节，支持更多的G2/G3圆弧运动。如下图所示，导入Bambu Studio的STEP模型包含了大量的三角形网格：

![](https://wiki.bambulab.com/software/bambu-studio/step-format/step%E8%BD%AC%E4%B8%BA%E9%AB%98%E7%B2%BE%E5%BA%A6%E7%9A%84stl.png)

## 调整导入质量

step文件导入时可以设置导入质量。这通过两个参数[“线偏转值”和“角偏转值”](https://dev.opencascade.org/doc/overview/html/occt_user_guides__mesh.html)来控制。当这两个参数值设置的越小时，模型导入质量越高，曲面处越平滑，同时生成的三角面数量越多，导入文件和切片的耗时也会相应增加。  
**如果启用了“不再显示”选项，下次导入step文件时，将不在提示此对话框，如果你想恢复显示该对话框，请在“偏好设置”中，启用“显示step参数设置对话框”。**

![step_mesh_zh_1.png](https://wiki.bambulab.com/software/bambu-studio/step-format/step_mesh_zh_1.png)
![step_mesh_zh_2.png](https://wiki.bambulab.com/software/bambu-studio/step-format/step_mesh_zh_2.png)

  

![step_mesh_zh_3.png](https://wiki.bambulab.com/software/bambu-studio/step-format/step_mesh_zh_3.png)
![step_mesh_zh_4.png](https://wiki.bambulab.com/software/bambu-studio/step-format/step_mesh_zh_4.png)
