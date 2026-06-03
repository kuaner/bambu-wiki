---
path: zh/software/bambu-studio/auto-brim
title: "Brim"
description: "介绍在Bambu studio中brim的生成，手动和自动模式的区别"
tags: []
created: 2023-08-26T15:44:25.583Z
updated: 2026-04-16T02:00:47.686Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/auto-brim
---

## 功能介绍

Brim是模型底部周围生成的单层平面区域。它的目的是扩展模型的首层区域，使打印物体和打印板之间的接触面积更大。

- 更大的表面积可以让模型更好地粘在构建板上，这对于又高又瘦的模型非常有用。
- Brim也可以帮助提高模型底面边缘的粘接。有些材料在冷却的时候很容易收缩（如ABS），在打印时往往会容易翘边。有一个足够宽度的brim可以使模型边缘保持在原位，防止这种翘曲。

![](https://wiki.bambulab.com/software/bambu-studio/brim/brim_example.png)

Brim参数在左侧栏的**其他**设置。它是一个针对对象设置的参数，因此您可以为每个对象设置不同的值。

![](https://wiki.bambulab.com/software/bambu-studio/brim/brim%E8%AE%BE%E7%BD%AE.png)

## Brim 类型

![](https://wiki.bambulab.com/software/bambu-studio/brim/brim%E7%B1%BB%E5%9E%8B.png)

### 自动（默认）

这是Bambu Studio设计的新功能。在这种模式下，Bambu Studio会自动分析每个对象，并为其生成适当宽度的Brim。主要考虑以下因素:

#### 零件的形状和方向

一个高的零件和小的底部接触面积通常需要一个Brim，以防止它在打印过程中被打印机的喷嘴推翻。底部接触面积较小的较高零件在冷却过程中很容易与构建板分离，因此需要更宽的Brim。

![](https://wiki.bambulab.com/software/brim-generation/bending.png)

#### 耗材类型

材料类型为PC，ABS，PA-CF，PET-CF或PLA-CF的零件通常会生成更宽的Brim，因为这些材料具有高的热膨胀系数和高成型温度，从而导致零件底部的高热应力。相反，TPU打印的零件通常需要更窄的Brim。

![](https://wiki.bambulab.com/software/brim-generation/thermal.png)

![](https://wiki.bambulab.com/software/bambu-studio/brim/%E8%80%97%E6%9D%90%E7%B1%BB%E5%9E%8B%E9%80%89%E6%8B%A9.png)

#### 打印速度

更高的打印速度通常意味着热端和零件之间的剪切力更大，因此需要更宽的Brim来将零件粘在热床上。

![](https://wiki.bambulab.com/software/brim-generation/speed1.png)

### 手动模式

除自动模式外，也可以手动选择其他几种类型的Brim。Bambu Stduio则会根据“Brim宽度”参数生成Brim，用户可根据实际情况进行设置。手动Brim分为以下几种类型：

#### 仅外侧

仅在模型的外侧周围生成Brim:

![](https://wiki.bambulab.com/software/bambu-studio/brim/%E4%BB%85%E5%A4%96%E4%BE%A7.png)

#### 仅内侧

如果模型内部是空心的，那么会仅在在模型内侧周围生成Brim

**注意：内侧的brim仅针对模型本身内部有孔的时候才能生成。如果模型本身没孔，或者是靠特殊设置使切片后内部是空心的（例如使用负零件功能），它也是无法在切片后生成内侧brim的。**

![](https://wiki.bambulab.com/software/bambu-studio/brim/%E4%BB%85%E5%86%85%E4%BE%A7.png)

#### 内侧和外侧

将会在模型的内侧和外侧周围都生成Brim：

![](https://wiki.bambulab.com/software/bambu-studio/brim/%E5%86%85%E4%BE%A7%E5%92%8C%E5%A4%96%E4%BE%A7.png)

#### 绘制

有时候 Brim 拆除较为麻烦，有些区域并不需要添加，我们可以只在模型尖角处添加Brim，这时绘制耳状 Brim 能够更方便解决这些问题。有关该功能的具体使用方法，详见 [耳状 Brim | Bambu Lab Wiki](brim-ears.md)  
![painted_brim.jpg](https://wiki.bambulab.com/software/bambu-studio/brim/painted_brim.jpg)

#### 无 brim

将不会生成Brim。

![](https://wiki.bambulab.com/software/bambu-studio/brim/%E6%97%A0brim.png)

## Brim 宽度

在手动模式下生成Brim的宽度。

![](https://wiki.bambulab.com/software/brim-generation/brim_width1.png)

## Brim 与模型的间隙

在“自动”和“手动”模式下，对象与其Brim之间所需的间隙。较小的间隙可以提高连接强度，较大的间隙则容易拆卸。如果您将间隙设置为0后发现Brim与模型之间仍有间隙，通常是由于开启了“象脚补偿”功能导致的。您可以关闭象脚补偿，使Brim与模型完全贴合。对比如下图：

![](https://wiki.bambulab.com/software/bambu-studio/brim/brim%E4%B8%8E%E6%A8%A1%E5%9E%8B%E7%9A%84%E9%97%B4%E9%9A%99.png)

![](https://wiki.bambulab.com/software/bambu-studio/brim/brim%E5%92%8C%E6%A8%A1%E5%9E%8B%E5%AE%8C%E5%85%A8%E6%B2%A1%E6%9C%89%E9%97%B4%E9%9A%99.png)
