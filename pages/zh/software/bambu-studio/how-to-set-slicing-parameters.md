---
path: zh/software/bambu-studio/how-to-set-slicing-parameters
title: "切片参数设置指南"
description: ""
tags: []
created: 2023-08-06T05:14:41.945Z
updated: 2024-09-18T13:38:21.548Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/how-to-set-slicing-parameters
---

# 切片参数

Bambu Studio有数百个切片参数，这些参数主要分为三个大类：打印机、耗材丝和工艺。

在一个类别中，一旦设置了所有参数的值，就可以将其保存为参数预设。例如，我们可以打印机根据 Bambu Lab X1 设置类别中的所有参数值，并将其保存为打印机名为“Bambu Lab X1C 0.4”的预设。 为了便于使用，Bambu Studio 为每个类别提供了一些预设参数。大多数时候，您可以根据自己的要求轻松选择预设来满足基本的切片需求。

## 打印机预设

切片之前，请您根据您的机器选择正确的机型和喷嘴型号的配置。（目前的机器，默认自带的喷嘴都是0.4mm）

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/机器喷嘴.png)

打印机预设里包含所有打印机硬件设置，例如每个轴的最大打印速度、打印区域的限制以及喷嘴的直径等。（注意：不建议新手用户随意更改参数）

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/打印机设置.png)

## 耗材丝预设

在切片之前，您需要根据您使用的耗材丝，选择正确的耗材丝类型参数来打印模型，因为不同类型的耗材丝的参数设置不一样。一旦选错了，由于不同耗材需要的温度、风扇设置等不同，有很大的风险会打印失败。

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/耗材丝设置.png)

耗材丝预设包含所有耗材特定设置，例如打印温度、热床温度和流量比例等。（注意：不建议新手用户随意更改参数）

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/耗材丝设置1.png)

## 工艺预设

您可以根据您的打印需求，在这里选择对应的参数设置，前面的数字代表的是打印层高。层高越小，打印出的模型越精细。默认为0.2mm标准参数。

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/工艺选择.png)

工艺里面包含特定打印任务的所有设置，可以在这里对质量、强度、速度、支撑等参数进行调节。（注意：不建议新手用户随意更改参数）

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/工艺设置.png)

## 创建您自己的用户预设

Bambu Studio 支持自定义用户预设（打印机、耗材丝和工艺预设）。当您有特殊要求时，这个功能非常有用。例如，您可以创建一个工艺预设，通过增加填充密度、墙数和顶部/底部壳数来增加模型的整体强度。或者，您可以为第三方材料创建耗材丝预设。

[参数预设](preset.md)详细介绍了如何创建自定义用户预设。

# 设置切片参数

## 设置打印机或耗材丝参数

您可以根据以下图片设置参数：

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/打印机参数.png)![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/耗材参数.png)

## 设置工艺参数

对于工艺类别中的参数，Bambu Studio 支持在多个参考或级别字段中设置值：

- **全局**   
  在全局级别设置的参数对项目中的每个对象都生效。
- **对象**   
  在对象级别中设置的参数对当前选定对象生效。
- **零件**   
  在零件级别设置的参数对当前选定的零件生效。
- **修改器**   
  修改器是对象的特殊部分。它不是实体模型，可以用修改器更改与它重叠的对象区域的参数。

通常，如果同一参数在多个级别设置不同的值，则会使用最小级别的值，如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/工艺关系.png)

### 全局级别参数

全局参数值将应用于项目中的所有对象。例如，在下面的全局参数中，稀疏填充密度设置为 5%，因此所有对象都将具有 5% 的填充密度。  
 因此，**强烈建议**设置全局参数以适合大多数对象。

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/全局.png)

注意：参数预设是全局的。仅全局参数修改可以保存到（用户或项目）预设。

## 对象级别参数

对于需要特殊参数设置的对象，我们需要在引用的对象字段中设置其值。

首先，我们将过程设置模式从“全局”更改为“对象”，然后将立方体的填充密度设置为20%。切片后，立方体的填充密度变为20%，其他模型保持在5%（全局值）。在对象级别设置的参数会覆盖全局级别的参数。

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/对象.png)

*提示：Bambu Studio 支持选择多个对象并一起设置它们的参数值。*

## 零件级别参数

一个组合模型的对象，可以拆分为零件。 如果您想在对象的不同零件使用不同的参数值，可以在对象列表中选择一个零件并更改其参数值。 将文件名为Mickey\_planter.stl的模型文件“拆分为零件”后，生成了4个零件。

如果我们将对象的耗材丝设置为#1（黑色），并将名为Mickey\_planter.stl\_1的零件设置为#2（红色），则Mickey\_planter.stl\_1零件将使用耗材丝#2打印。在零件级别设置的参数会覆盖在对象或全局级别设置的参数。

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/零件参数.png)

*提示：Bambu Studio 支持从同一对象中选择多个零件，并一起设置它们的参数值。*

## **修改器**

**修改器**是对象的特殊部分，而不是要打印的对象。顾名思义，它旨在修改与对象重叠的设置。通过修改器设置的参数会覆盖在零件、对象或全局级别设置的参数。 要创建修改器，请右键单击对象，在上下文菜单中选择“添加修改器”，然后选择所需的修改器形状。 一般，可以通过这个修改器功能修改重叠部分区域的耗材丝颜色或者填充密度等。

下面的 gif 显示了，将修改对象与修改器重叠部分区域的耗材丝颜色，设置#3（白色）的全过程。

![](https://wiki.bambulab.com/software/bambu-studio/setting-guide-of-slicing-parameters/修改器参数.gif)
