---
path: zh/software/bambu-studio/Seam
title: "接缝设置"
description: "本文介绍如何在 Bambu Studio 中设置和绘制接缝"
tags: ["bambu studio"]
created: 2023-08-18T09:16:33.159Z
updated: 2026-07-28T05:19:32.334Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/Seam
---

## 功能介绍

接缝就是在打印过程中每条走线的起始和终点交接处产生的缝隙（除非你开启了旋转花瓶模式，具体参考 [旋转花瓶 | Bambu Lab Wiki](spiral-vase.md)），它会在模型表面留下垂直方向的接缝，这在 FDM 3D 打印中是不可避免的。在一些不规则的表面（例如有凹凸顶点的表面），可以较好地隐藏接缝。而在另一些较为光滑规则的表面（例如圆柱体的侧面），接缝则会表现得十分明显。

|  |
| --- |
| 图1 圆柱体表面的接缝 |

如图2-2中，第53层的两个白点就是这一层的接缝位置。

|  |  |
| --- | --- |
|  |  |
| 图 2-1 | 图 2-2 接缝 |

## 接缝设置方法

接缝设置界面如下，其中**接缝位置**、**接缝间隔**、**擦拭速度**和**自动擦拭速度**可应用于所有类型接缝。其余设置属于斜拼接缝，会在下文中单独介绍。

> 部分参数需开启“开发者模式”，可按下“**Ctrl+P**”选择开启。

![bs_seam_setting.png](https://wiki.bambulab.com/software/bambu-studio/seam/bs_seam_setting.png)

### 接缝位置

为了获得更好的打印效果，可以在工艺预设中设置接缝位置。有四种类型的接缝位置可供选择：**最近**、**对齐**、**背面**和**随机**。

![bs_seam_position.png](https://wiki.bambulab.com/software/bambu-studio/seam/bs_seam_position.png)

#### 最近

“最近”首先按以下优先级找到所有可能的候选位置：凹非悬垂顶点 > 凸非悬垂顶点 > 非悬垂顶点 > 悬垂顶点

也就是说，它会优先选择凹的或者凸的非悬垂顶点，让接缝位置更好地隐藏。如果你的模型有尖角，这将使接缝看不见。

然而如果当前层没有可用的这两种顶点，它会在其他候选的非悬垂顶点位置中选择，让它最接近上一条打印走线的结束位置。因此，该选项将优化空驶路径，能够尽可能减少喷嘴漏料的影响。

![](https://wiki.bambulab.com/software/bambu-studio/seam/nearest.png)

#### 对齐

选择候选接缝位置的逻辑与“最近”相同，但它将选择最接近前一层接缝的位置。这将确保大部分接缝能够在整个模型中对齐。

![](https://wiki.bambulab.com/software/bambu-studio/seam/alig-1.png)

#### 背面

接缝将会被设置在模型的背部。如果你想在模型的前面得到一个光滑的表面，比如钢铁侠面具，这将是一个不错的选择。

![](https://wiki.bambulab.com/software/bambu-studio/seam/back-1.png)

#### 随机

接缝将会被随机设置在每层的不同位置，使接缝看起来不如“对齐”或者“背面”那样统一，相对也会没那么明显。但是它会使模型表面出现一些类似“青春痘”的效果。

![](https://wiki.bambulab.com/software/bambu-studio/seam/%E9%9A%8F%E6%9C%BA%E6%8E%A5%E7%BC%9D.png)

### 接缝间隔

为了让接缝看起来更加隐蔽，打印内外墙的时候会提前终止挤出，在接缝位置预留出一段间隔来容纳多余的材料。这个长度是当前喷嘴直径的百分比。该参数的默认值为15%。

![](https://wiki.bambulab.com/software/bambu-studio/seam/%E6%8E%A5%E7%BC%9D%E9%97%B4%E9%9A%94.gif)

### 擦拭速度

在空驶回抽的时候，通常会进行一段擦拭来清洁喷嘴（详情可以参考：[回抽设置 | Bambu Lab Wiki](parameter/retraction.md) {target="\_blank"}），擦拭的速度可以调整。该值以百分比形式表示，将根据空驶速度的百分比进行计算。**例如擦拭速度设置为80%，表示擦拭速度=空驶速度\*80%。**

![](https://wiki.bambulab.com/software/bambu-studio/seam/%E6%93%A6%E6%8B%AD%E9%80%9F%E5%BA%A6.jpg)

### 自动擦拭速度

擦拭速度由当前走线类型的打印速度决定。例如，如果擦拭动作紧随外墙，擦拭速度将使用外墙速度。**勾选“自动擦拭速度”后，上文中设置的“擦拭速度”将不再生效。**

### 接缝绘制

有时自动设定的接缝位置不理想，您可以通过手动绘制的方法来自定义接缝位置。Z缝绘制的功能可以在下图位置开启：

![](https://wiki.bambulab.com/software/bambu-studio/seam/z%E7%BC%9D%E7%BB%98%E5%88%B6.jpg)

手动绘制接缝的方法如下图所示：

![](https://wiki.bambulab.com/software/bambu-studio/seam/%E6%89%8B%E5%8A%A8%E7%BB%98%E5%88%B6%E6%BC%94%E7%A4%BA.gif)

## 斜拼接缝

Bambu Studio 在 1.9 版本引入斜拼接缝，大部分情况下，它可以减弱接缝的明显程度，减弱打印件起始部分的凸起。这个功能的改变了接缝处的走线方式，使得接缝处像围巾一样重叠走线，通过分段的流量控制和擦嘴速度控制，改善铆接来弱化接缝。下图是接缝位置的示意图片。

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E6%96%9C%E6%8B%BC%E6%8E%A5%E7%BC%9D%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

由图片可以看出，通过控制起始点的喷嘴高度和挤出材料量，让接缝在起始点和结束点位置结合得更加严密。下图是具体走线渲染图：

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E6%96%9C%E6%8B%BC%E6%8E%A5%E7%BC%9D%E8%B5%B0%E7%BA%BF%E6%B8%B2%E6%9F%93%E5%8A%A8%E5%9B%BE.gif)

## 斜拼接缝参数

有以下两种方法可以调整斜拼接缝的参数：

1. 从 1.10 版本开始，您可以在“**耗材丝设置**”里针对每种材料调整“**材料斜拼接缝参数**”。  
   ![bs_filament_settings.png](https://wiki.bambulab.com/software/bambu-studio/seam/bs_filament_settings.png)
2. 您还可以在“**工艺**”菜单勾选“**覆盖材料的斜拼接缝参数**”，进而显示可以调整的参数。这里的设置将覆盖上图中对“材料斜拼接缝参数”的设置。  
   ![bs_override_filament_settings.png](https://wiki.bambulab.com/software/bambu-studio/seam/bs_override_filament_settings.png)

接下来介绍四种斜拼接缝参数的设置：

### 斜拼接缝类型

斜拼接缝类型一共有3个选项：**无**、**轮廓**、**轮廓和孔**。若要开启斜拼接缝，可以选择“轮廓”或者“轮廓和孔”。轮廓和孔的定义可以参考wiki：[XY孔洞/轮廓补偿](xy-hole-contour-compensation.md)

- 斜拼接缝选择“**无**”：轮廓和孔的接缝均为普通接缝。  
  ![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E5%9C%86%E7%8E%AF%E6%99%AE%E9%80%9A%E6%8E%A5%E7%BC%9D.png)
- 斜拼接缝选择“**轮廓**”：轮廓为斜拼接缝，孔为普通接缝。  
  ![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E5%9C%86%E7%8E%AF%E8%BD%AE%E5%BB%93%E6%96%9C%E6%8B%BC.png)
- 斜拼接缝选择“**轮廓和孔**”：轮廓和孔的接缝均为斜拼接缝。  
  ![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E5%9C%86%E7%8E%AF%E8%BD%AE%E5%BB%93%E5%92%8C%E5%AD%94%E6%96%9C%E6%8B%BC.png)

### 斜拼接缝起始高度

起始高度指墙开始打印时的z高度，这个数值可以用毫米或者当前层高的百分比表示，如10%代表的是斜拼接缝的起始高度是当前层高度的10%。如果起始高度设置为100%，将会变成普通接缝。

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E6%96%9C%E6%8B%BC%E6%8E%A5%E7%BC%9D%E8%B5%B7%E5%A7%8B%E9%AB%98%E5%BA%A6%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E8%B5%B7%E5%A7%8B%E9%AB%98%E5%BA%A610.png)

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E8%B5%B7%E5%A7%8B%E9%AB%98%E5%BA%A650.png)

### 斜拼接缝间隔

启用斜拼接缝间隔后，内墙会被裁剪去一部分来容纳多余的材料。该参数如果单位是百分比，则是用特定系数乘以喷嘴直径的百分比计算来接缝间隔。

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E6%96%9C%E6%8B%BC%E6%8E%A5%E7%BC%9D%E9%97%B4%E9%9A%94.gif)

### 斜拼接缝长度

斜拼接缝的长度为 0 时会禁用斜拼接缝。若启用了“围绕整个围墙”，则设置的斜拼接缝长度将不起作用。

![bs_scarf_length.png](https://wiki.bambulab.com/software/bambu-studio/seam/bs_scarf_length.png)

## 斜拼接缝的效果调整

如果对接缝的效果不满意，可以对以下其他参数进行调整以优化接缝效果。

### 智能应用斜拼接缝

Bambu Studio 具备智能选择接缝功能，根据模型的特点来选择是否应用斜拼接缝。当接缝位置的悬垂过大，或接缝位置角度较小可以掩藏接缝时，会选择不应用斜拼接缝。当墙壁没有合适的锐角，以至于传统接缝无法有效隐藏时，则选择应用斜拼接缝。**关闭此选项则所有区域都应用斜拼接缝。**

#### 悬垂区域不应用斜拼接缝

因为斜拼接缝的挤出流量较小，在悬垂区域可能会存在难以正常粘接的问题。所以为保证外观面的正常打印，此选项只应用于悬垂度较小的区域。悬垂度较大的区域仍然采用普通接缝模式。

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E6%82%AC%E5%9E%82%E5%8C%BA%E5%9F%9F%E4%B8%8D%E5%BA%94%E7%94%A8%E6%96%9C%E6%8B%BC%E6%8E%A5%E7%BC%9D.png)

### 斜拼角度阈值

因为锐角处可以较好的隐藏接缝，所以当模型表面有锐角的时候，默认不开启斜拼接缝，可以直接把接缝藏在锐角处。若希望锐角处应用斜拼接缝，或是需要调整斜拼接缝的应用范围，可以调整角度阈值这个参数。

此选项设置判断是否应用斜拼接缝的角度阈值。如果单层围墙环内的**接缝角度**超过了这个值（表示模型表面没有足够锐的角），则使用斜拼接缝，否则将不使用斜拼接缝。

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E6%8E%A5%E7%BC%9D%E8%A7%92%E5%BA%A6%E5%A4%A7%E4%BA%8E%E8%A7%92%E5%BA%A6%E9%98%88%E5%80%BC.png)

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E6%8E%A5%E7%BC%9D%E8%A7%92%E5%BA%A6%E5%B0%8F%E4%BA%8E%E8%A7%92%E5%BA%A6%E9%98%88%E5%80%BC.png)

### 围绕整个围墙

将斜拼接缝延伸到整个围墙。**此选项开启需要慎重，它会导致整圈都使用较小的挤出量挤出，可能引发材料粘接不良，导致外观面瑕疵。**

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E5%9B%B4%E7%BB%95%E6%95%B4%E4%B8%AA%E5%9B%B4%E5%A2%99.gif)

### 斜拼段数

斜拼接缝所需的**最少段数**，也就是把斜拼接缝起始位置的斜坡分成几段。**不过要注意的是，有些接缝起始位置不能被精确地划分成所设置的段数，所以实际斜拼段数≥设置的斜拼段数。**

![](https://wiki.bambulab.com/software/bambu-studio/seam/scarf-seam/%E6%96%9C%E6%8B%BC%E6%AE%B5%E6%95%B0.gif)

### 应用斜拼于内墙

启用该选项后，内墙也将采用斜拼接缝，该选项默认开启。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn?from=5)，它能够即时解答常见问题，并为您提供操作指导。
