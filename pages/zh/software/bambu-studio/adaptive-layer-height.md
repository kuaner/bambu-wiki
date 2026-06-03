---
path: zh/software/bambu-studio/adaptive-layer-height
title: "可变层高"
description: ""
tags: []
created: 2023-07-21T07:28:02.185Z
updated: 2024-05-28T10:51:40.889Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/adaptive-layer-height
---

# 功能介绍

通常我们在工艺预设中设置打印层高后，切片会得到一个均匀层高的模型。但有时候对一些特殊模型，例如顶面是球状或者有坡度的模型，打印出来的表面可能会不够光滑，“阶梯感”比较明显。可变层高功能将有助于改善这一点。图1和图2为均匀层高与可变层高的区别。

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/可变层高切片对比.png)

**图1.可变层高切片对比**

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/可变层高打印对比.png)

**图2 .左：未开启可变层高；右：开启可变层高**

如图3所示，在层高相同的情况下，坡度越大，模型表面越顺滑。如果模型的顶部有一个小的坡度的话可能没有模型的中间那么光滑。很明显，如果降低顶部的层高，表面的效果会更好。众所周知，低层高所需要的打印时间更长，而对于这种情况，我们只需要降低局部的打印层高，其他地方保持原有的层高。这样既可以保证打印的质量，又尽可能地节省打印时间。

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/explain.png)

**图3.坡度较大模型表面更光滑**

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/explain-2.png)

**图4.小层高有助于减小表面坡度带来的“阶梯感”**

# 操作指南

可变层高的高度范围在打印机设置的层高限制中，例如0.4mm喷嘴的层高范围是0.08-0.28，这是我们实验室测得该喷嘴能够打印出较好打印质量的一个层高范围，通常我们不建议您修改它。

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/层高范围限制.png)

**图5.层高范围限制**

选中盘中的某个对象后，您可以在这里开启这个功能：

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/开启可变层高.png)

**图6.开启可变层高功能**

您可以在右侧的界面中通过快捷键（如图6所示）来拖动不同高度范围的层高，如下图所示：

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/可变层高功能示范.gif)

**图7.调节不同区域的层高**

您也可以通过调节**细节/速度**的倾向后点击**自适应**，它将会综合您对打印细节和速度的需求自动调节不同范围的层高。如果拖动小三角形靠近“细节”，说明打印的模型更精细，它会自动给模型更多的部分设置成较低的层高。如果拖动小三角形靠近“速度”，则会更倾向于更快的打印速度，所以会自动给模型的更多部分设置成较高的层高。

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/自适应可变层高示范.gif)

**图8.自适应可变层高**

**平滑模式：**点击将会让不同层高过渡更加平滑。**半径指的是高斯滤波器的滤波宽度**。更大的过滤半径将使曲线更平滑，你可以多次点击来获得平滑的曲线效果，让不同层高之间更好地过渡。

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/平滑模式.gif)

**图9.平滑模式**

**保留最小：**在使用平滑模式的时候，将不会去改变最小层高部分（绿色部分），也就是在平滑曲线的时候最小层高仍然保持原有值。

# 注意事项

**1. 当一盘中有多个模型对象且使用超过一种颜色时，只有当盘中所有对象的可变层高设置都是一样的才可以启用擦拭塔，如果不同对象之间的可变层高不一样，就没法启用擦拭塔。**如下图中所示：

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/层高差异无法使用擦料塔.png)

**图10.不同对象层高不同，无法启用擦拭塔**

若多色的模型可变层高设置完全相同，则可以启用擦拭塔，如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/层高序列一样可启用擦料塔.png)

**图11.层高完全相同可以启用擦拭塔**

原因是**擦拭塔的高度必须与模型的高度相同**，但如果使用了可变层高，会导致不同模型间出现高度差。例如，如果某个模型的层高被设置为0.18mm，那么擦拭塔的层高度也必须为0.18mm。但是另一个模型的层高仍然是0.2mm，所以擦拭塔需要增加0.02mm才能达到和另个模型一样的高度。但是，这个0.02mm 的层高是不可用的，所以没办法为擦拭塔单独增加一个0.02的层高。

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/wipe-tower.png)

**图12.擦拭塔不可用的原因**

**2. 可变层高也不支持与树状支撑中的“有机树支撑”同时使用。**

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/可变层高不支持有机树.png)

**图13.无法和有机树支撑同时使用**
