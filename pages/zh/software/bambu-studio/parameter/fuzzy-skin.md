---
path: zh/software/bambu-studio/parameter/fuzzy-skin
title: "绒毛表面"
description: "本文介绍如何在 Bambu Studio 中为模型增加绒毛表面"
tags: ["bambu studio"]
created: 2023-11-20T10:46:48.063Z
updated: 2026-08-13T01:56:38.933Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/fuzzy-skin
---

## 功能介绍

绒毛表面功能，顾名思义就是在模型的侧面生成一种类似动物绒毛的粗糙纹理。这个功能不仅能打印出特殊的模型外观，还可以有效地隐藏层纹、振纹和接缝，并增加模型表面的摩擦力。它的原理是在切片时给墙走线增加随机的抖动，从而使原始的直线的墙走线变成密集粗糙的折线来实现这种不规则的纹理效果。由于它只作用于墙走线，所以顶面和底面无法产生绒毛表面效果，因为底面和顶面的走线是属于实心填充，无法在打印一层填充时Z轴上下抖动。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E6%89%93%E5%8D%B0%E7%BB%92%E6%AF%9B%E8%A1%A8%E9%9D%A2%E6%95%88%E6%9E%9C.png)

## 绒毛表面开启选项

绒毛表面功能可以在 **工艺 > 其他 > 绒毛表面** 中开启。

![fuzzy_skin_setting_zh.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/fuzzy_skin_setting_zh.png)

以下选项决定了绒毛表面生效的**位置**：

### 无（允许绘制）

这是默认选项。它不会自动将绒毛表面效果应用到模型上，但允许你使用“**绒毛表面绘制**”工具，仅为选定区域添加该效果。

![none_allow_paint_zh.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/none_allow_paint_zh.png)

### 轮廓

仅在模型的外轮廓位置生成绒毛表面效果。**有关轮廓和孔的定义，可以参考：**[**XY孔洞/轮廓补偿**](../xy-hole-contour-compensation.md)。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E4%BB%85%E8%BD%AE%E5%BB%93.png)

### 轮廓和孔

在模型的外轮廓和孔洞位置均生成绒毛表面效果。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E8%BD%AE%E5%BB%93%E5%92%8C%E5%AD%94.png)

### 所有墙

在模型的所有内墙和外墙均生成绒毛表面效果。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E6%89%80%E6%9C%89%E5%A2%99.png)

### 关闭

此选项会完全关闭绒毛表面效果，包括绒毛表面绘制。

## 绒毛表面设置

上述选项决定了绒毛表面生效的位置。此外还有一些可用设置，说明如下：

### 绒毛表面生成器模式

该设置决定如何生成绒毛表面效果。不同模式会产生不同的运动方式和纹理风格，包含以下三种选项：

- **位移**：通过让喷嘴相对原始路径左右轻微偏移，形成粗糙的纹理效果，但不改变挤出量。  
  ![fuzzy_skin_displacement.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/fuzzy_skin_displacement_zh.png)
- **挤出**：在喷嘴路径保持基本不变的情况下，通过改变材料挤出量来形成纹理。  
  ![fuzzy_skin_extrusion.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/fuzzy_skin_extrusion_zh.png)
- **组合**：同时使用喷嘴位移和挤出量变化，观感接近位移模式，且能填补层与层之间的间隙。  
  ![fuzzy_skin_combined.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/fuzzy_skin_combined_zh.png)

> **说明**：挤出与组合模式仅在「绒毛表面厚度」不大于「实际打印线宽」时生效。

### 绒毛噪声类型

该设置用于控制生成绒毛效果的噪声类型。不同的噪声类型会产生不同的纹理风格和表面外观，包含以下五种选项：

- **经典**：经典的均匀随机噪声，表面粗糙感较为均衡。这是默认选项，适用于大多数打印。  
  ![classic.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/classic_zh.png)
- **Perlin(柏林噪声)**：创建更平滑、更自然的纹理，并具有渐变式的表面起伏。  
  ![perlin.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/perlin_zh.png)
- **Billow(云状噪声)**：纹理类似柏林噪声，但更聚集，使打印件呈现蓬松的外观。  
  ![billow.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/billow_zh.png)
- **Ridged Multifractal(脊状多重分形)**：创建更锐利、更粗犷的纹理，具有明显的脊状结构和更深的表面细节。  
  ![rigged.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/rigged_zh.png)
- **Voronoi(维诺图)**：将表面划分为 Voronoi 单元，每个单元随机位移，形成不规则的蜂窝状图案。  
  ![voronoi.png](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/voronoi_zh.png)

### 绒毛表面点间距

该参数控制喷嘴在相邻两个抖动点之间的平均距离。降低**绒毛表面点间距**将增加墙走线上随机偏移点的数量，效果如下：

|  |  |
| --- | --- |
| 绒毛表面点间距 1 mm | 绒毛表面点间距 0.2 mm |

### 绒毛表面厚度

该参数控制喷嘴每次抖动的大小和深度。增加**绒毛表面厚度**将使模型表面更不平整，绒毛感更明显。不过如果该值设置太大，可能会在模型表面出现悬空墙，效果如下：

|  |  |
| --- | --- |
| 绒毛表面厚度 0.3 mm | 绒毛表面厚度 1 mm |

### 绒毛表面应用至首层

启用后，打印首层也会应用绒毛表面效果；禁用时，首层将保持光滑。

## 用修改器添加局部绒毛表面效果

您还可以使用修改器功能，来给模型的局部添加绒毛表面效果。

- **右键单击**模型，然后选择**添加修改器** - 选择合适的修改器模型。  
  ![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E6%B7%BB%E5%8A%A0%E4%BF%AE%E6%94%B9%E5%99%A8.png)
- 把修改器模型**拖动**到模型上与之重叠，可以适当调节其位置和大小。  
  ![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E8%B0%83%E6%95%B4%E8%B4%9F%E9%9B%B6%E4%BB%B6%E5%A4%A7%E5%B0%8F%E5%92%8C%E4%BD%8D%E7%BD%AE.png)
- 在**对象列表**里，给修改器单独设置绒毛表面，它将会给修改器和模型重叠部分增加绒毛表面效果。  
  ![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E5%AF%B9%E8%B1%A1%E5%88%97%E8%A1%A8%E5%90%AF%E7%94%A8%E7%BB%92%E6%AF%9B%E8%A1%A8%E9%9D%A2.png)
- 切完片后，就会看到模型局部生成绒毛表面的效果。  
  ![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E5%88%87%E7%89%87%E5%AE%8C%E7%BB%92%E6%AF%9B%E8%A1%A8%E9%9D%A2%E6%95%88%E6%9E%9C.png)
- 局部绒毛表面打印后的**实际效果**  
  ![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/%E5%AE%9E%E9%99%85%E6%89%93%E5%8D%B0%E6%95%88%E6%9E%9C.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
