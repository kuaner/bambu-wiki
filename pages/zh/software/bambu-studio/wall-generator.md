---
path: zh/software/bambu-studio/wall-generator
title: "墙生成器介绍"
description: ""
tags: []
created: 2023-09-07T10:04:53.275Z
updated: 2025-06-18T06:42:33.218Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/wall-generator
---

# 前言

本文将介绍3D模型切片过程中，模型的墙是如何生成的，以及两种墙模式（Classic和Arachne）的区别和各自的优缺点。以便于您在切片打印的时候，更清楚地知道要如何选择和使用它。

# 什么是墙生成器

要解释墙生成器，首先需要说明墙的含义。墙是一个二维形状的轮廓，也就是多边形的周长。下图1中的黑色线就是该形状的“墙”。

其次要了解一下是什么是“墙路径”。如图2中的红线所示，它表示了墙是如何生成的，包括它的方向、起始位置和路径宽度。

|  |  |
| --- | --- |
| **图1** | **图2 墙生成过程** |

3D模型的切片和打印，本质上是把一个3D模型切分成许多层，然后一层层打印成立体模型。其中的每一层都可以视作一个多边形。墙生成器负责生成每一层多边形的墙路径。在三维视图中，模型的形状如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/三维模型视图.png)

**图3 切片后的三维模型**

还有一个名为“墙层数”的参数来调整墙的数量。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙层数设置.png)

**图4 墙层数设置**

下图展示了一个有三层墙的立方体切片模型。橙色的路径和黄色的路径都是该立方体的墙。最外层的墙称为外墙，其他的墙都称为内墙。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/内墙和外墙.png)

**图5 外墙和内墙**

# 如何选择墙生成器

墙生成器可以在**工艺——质量**中选择，它有两种类型:Classic和Arachne。这两种墙用不同的算法来产生墙的路径，各有优劣势。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/选择墙生成器.png)

**图6 墙生成器选择**

# 经典墙模式工作原理

首先，需要解释一下“收缩”的含义，以便于接下来的解释。收缩函数如下图所示，其中灰色多边形为原始多边形，橙色多边形为缩小后的多边形。X是收缩宽度。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/收缩函数.png)

**图7 收缩函数**

下图8显示了经典墙模式下生成墙路径的过程。首先是原多边形形状，缩小设置的间距宽度（半个外墙线宽）得到第一层路径。然后，再次给第一层墙的多边形收缩设定的间距宽度（两个墙的中心距离），生成第二个墙路径。下图中绿色的多边形可以视作生成墙路径的中心线（也就是这一圈墙的“骨架”），然后实际的路径宽度为设定的内外墙线宽。在经典墙模式下，单条路径的宽度始终是一致的，并且墙路径始终是一个连续的闭环。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙收缩过程.png)

**图8 收缩生成墙路径过程**

如果多边形太小，收缩的结果会为空，所以就不会生成墙路径。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/收缩结果为空.png)

**图9 图形太小无法生成墙路径**

# 经典墙的优势

另一个需要提到的概念是“接缝”。“接缝”是墙路径起点和终点之间的间隙。它会在墙上留下一个清晰的点，在打印模型的表面会形成一条明显的缝隙（详情可以参考：[接缝设置 | Bambu Lab Wiki](Seam.md)）。

如前所述，经典墙体路径是宽度均匀的，所以表面质量会更好，因为它只有一条接缝。不连续的路径可能造成多条缝线。下图是Classic墙打印出来的连续表面，还有Arachne墙打出来的非连续表面。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/arachne和经典墙打出来的表面对比.png)

**图10 经典墙和Arachne墙打印对比**

# 经典墙的劣势

有些模型会有一些比较细小的部分，这些部分太小而无法生成闭合的墙路径，因此切片后会导致模型的部分缺失。例如，下图11中模型表面有很小的文本，因此切片后无法生成文本的墙路径（如图12所示）。当然，如果你更换一个更小尺寸的喷嘴设置，则很有可能将其成功切片。这个问题根本原因是模型的局部太过精细，所需要的打印走线宽度比当前使用喷嘴尺寸的默认线宽还要细小。而设置更小的墙线宽可以解决这个问题。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/small_part.png)

**图11 模型表面的小文字**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/small_part切片后.png)

**图12 切片后丢失细节**

# 检查薄壁

在某些场景下，“检查薄壁”功能可以解决上述这个问题。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/薄壁检测.png)

**图13 检查薄壁**

如果启用了该参数，则生成墙时的收缩宽度将减小一点，以便为生成墙路径提供空间。如下图所示，生成薄壁后墙中心的间距会更小一些。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/减小收缩生成薄壁.png)

**图14 薄壁和普通墙生成对比**

因此，当启用该选项时，一些细节如小的文字也可以被成功切片。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/small_part被成功切片.png)

**图15 检查薄壁生成小的文字**

然而，“检测薄壁”在某些情况会导致其他问题。如上述所提到的，因为墙间距减小，无法容纳完整的线宽，墙之间可能发生重叠，如下图所示。黑色为原始的图层形状，红色为外墙，蓝色为内墙。虚线是墙路径的中线，实线是墙路径的边缘。如果收缩的间距小于墙线宽的一半，则墙会重叠。多余的耗材丝可能会粘在喷嘴上，然后在打印过程中会粘到其他部件，从而使表面质量变差。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/检测薄壁后中间重叠.png)

**图16 检查薄壁导致墙重叠**

在某些情况下，某些细小的部分可能会从原本的墙走线上断开，因为检测薄壁选项也会收集小的区域来产生薄壁。某些非常小的部分只产生一条墙路径线不再闭合，如下图所示。因此，这两个部分是分开的，薄壁区域在打印过程中可能会因为太脆弱导致失败。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/机翼模型薄壁切片前后对比.png)

**图17**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/薄壁检测生成非闭环墙路径.png)

**图18**

# Arachne模式介绍

Arachne也被称为“可变线宽模式”，因为墙路径宽度是可变的。如下图所示，单条墙可以得到不同的宽度。由于可以调节墙体的宽度，所以模型上一些小的细节部分切片后也能生成，且相比“薄壁检测”功能，该模式生成的墙没有重叠。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/arachne墙线宽可变.png)

**图19 Arachne墙可变线宽**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/经典墙线宽不变.png)

**图20 经典墙线宽一致**

# Arachne 模式工作原理

多边形从2D转换为3D，然后通过图层切割获得墙路径。如果你对此感兴趣，你可以看看这篇文章：[A Framework for Adaptive Width Control of Dense Contour-Parallel Toolpaths in Fused Deposition Modeling - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0010448520301007?via%3Dihub)

# Arachne模式的弊端

在某些情况下，arachne将生成非连续的墙路径。例如，部分区域不能生成2个相同宽度的内墙，但可以生成一个宽度稍大的单条内墙（如下图所示）。因此，它与另一个内墙不连续。非连续的墙路径会影响打印表面质量，如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/arachne不同区域生成墙数不同.png)

**图21**

# Arachne墙生成器参数设置

当你选择了“Arachne”墙生成器后，会出现一系列的参数可供调整，具体的解释如下：

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/arachne参数设置.png)

**图22 Arachne参数设置**

## 墙过渡

这里需要引入一个名为“墙过渡”的新概念。首先需要说明“偶数墙”和“奇数墙”的概念：闭环的墙路径称为“偶数墙”，否则称为“奇数墙”。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/奇数墙和偶数墙.png)

**图23 奇数墙和偶数墙**

“墙过渡”区域是连接偶数墙和奇数墙的一系列楔形路径。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/奇数墙和墙过渡.png)

**图24 墙过渡**

### 墙过渡阈值角度

从下图中可以看出什么是墙过渡的阈值角度。因此墙过渡阈值角度参数是设置该角度的最大阈值。增加这个值，可以产生更多的楔形，并允许使用更短的楔形路径，所以路径过渡会更加平滑。该参数的设置范围是1°~59°。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙过渡阈值角度.png)

**图25 墙过渡阈值角度**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙过渡阈值角度1°.png)

**图26 墙过渡角度1°**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙过渡阈值角度59°.png)

**图27 墙过渡角度59°**

### 墙过渡过滤间距

该参数控制墙过渡的宽度范围。宽度范围为[最小墙线宽-过滤间距，2\*最小墙线宽+过滤间距]。参数值为相对喷嘴直径的百分比。

如果宽度范围扩大，墙过渡的数量可以增加以适应路径宽度。在某些路径得到较好排序的同时，减少了空驶时间。然而，楔形块的增加可能会导致过度挤压，从而破坏表面质量。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙过渡过滤间距1.png)

**图28 墙过渡过滤间距1%**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙过渡过滤间距25.png)

**图29 墙过渡过滤间距25%**

### 墙过渡长度

该参数控制墙面过渡的长度，参数值表示相对喷嘴直径的百分比。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙过渡长度100.png)

**图30 墙过渡长度100%**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙过渡长度500.png)

**图31 墙过渡长度500%**

## 墙分布计数

此参数决定有多少墙需要使用可变线宽。墙的编号是从中心向外计数。下图显示了不同的宽度和不同的颜色。图32显示只有一个墙路径需要应用可变宽度，图33显示3个墙应用了可变线宽。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙分布计数1.png)

**图32 墙分布计数1**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/墙分布计数3.png)

**图33 墙分布计数3**

## 墙最小线宽

此参数控制设置墙线宽的下限。该参数表示相对喷嘴直径百分比。例如，0.4mm喷嘴直径，85%的墙最小线宽表示可变线宽生成的墙路径，最细的部分是0.85\*0.4=0.34mm

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/最小墙线宽50.png)

**图34 墙最小线宽50%**

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator/最小墙线宽85.png)

**图35 墙最小线宽85%**

## 最小特征尺寸

它是一个宽度过滤器。设置依据的是喷嘴的尺寸，默认情况下，其设置值为喷嘴直径的 25%。如果路径的宽度小于该阈值，则不会打印该路径。如果路径宽度大于阈值，但小于墙最小线宽，则会自动把路径宽度将扩展到墙最小线宽。该参数表示相对喷嘴直径百分比。例如，选择了 0.4 喷嘴配置，某条路径宽度 0.25mm，大于喷嘴直径的25%（0.1mm），则会自动把它扩展到85%的喷嘴直径宽度，也就是 0.34mm。

如果下图所示，打印一些小于喷嘴直径的字体，使用最小特征尺寸为 25% 可以成功切片。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator-advice/25.png)

当最小特征尺寸调整为 100% 时也就喷嘴的直径 0.4mm 此时小于喷嘴直径的特征将不会被切片。

![](https://wiki.bambulab.com/software/bambu-studio/wall-generator-advice/100.png)
