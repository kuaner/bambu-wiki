---
path: zh/software/bambu-studio/parameter/line-width
title: "线宽设置"
description: ""
tags: []
created: 2023-12-15T11:21:15.679Z
updated: 2026-04-23T02:36:26.655Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/line-width
---

# 线宽介绍

## 什么是线宽

线宽，指的是打印过程中喷嘴挤出单颗融化耗材丝的宽度。通常情况下，挤出材料的宽度和喷嘴直径几乎一致。

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E7%BA%BF%E5%AE%BD%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

喷嘴挤出材料的宽度基本是由喷嘴直径决定的，即多宽的喷嘴直径就挤出多宽的材料。而如果想要线宽比喷嘴直径更宽或者更细，则需要对挤出流量进行控制。**由于喷嘴直径是固定的，所以设置的线宽与喷嘴直径通常都是接近的，如果线宽与喷嘴直径差太多将无法得到好的打印质量**。对于各种口径喷嘴，通常我们都建议不要去修改线宽。如果您想要修改它，建议可设置的线宽范围区间是：**0.75\*喷嘴直径~1.5\*喷嘴直径**。另外，线宽不可以小于层高，因为喷嘴无法挤出瘦高的走线横截面。

## **控制线宽的逻辑**

在喷嘴移动的过程中，增加或减少挤出耗材的流速来调节线宽，即调整**挤出流速/工具头运动速度** 比。喷嘴移动速度不变的情况下，减小挤出流速（单位时间的挤出流量），则会使线条更细一点。而增加挤出流速，由于挤出的耗材量变大，多出来的耗材会被喷嘴压扁，形成比喷嘴内径更宽的线条。**需要注意的是，可以挤出并压扁的最大线宽不会超过喷嘴的外径。我们通常说的喷嘴直径，指的是喷嘴的“内径”，也就是挤出材料的通道，如下图所示：**

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E5%96%B7%E5%98%B4%E5%86%85%E5%BE%84%E5%92%8C%E5%A4%96%E5%BE%84.png)

## 不同线宽效果图

下图是用0.4mm喷嘴打印不同外墙线宽的效果对比：

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E4%B8%8D%E5%90%8C%E7%BA%BF%E5%AE%BD%E6%89%93%E5%8D%B0%E6%95%88%E6%9E%9C%E5%9B%BE.png)

## 线宽设置的限制

**喷嘴只有在前一层或者热床上挤出耗材时，才能控制挤出宽度**。如果是在空中挤出，由于材料无法被压扁，得到的形状将始终是圆形的（如下图所示），所以无法为桥接、悬空墙设置线宽。具体可以参考：[桥接设置 | Bambu Lab Wiki](../../../filament-acc/filament/print-quality/bridging.md)。

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E6%A1%A5%E6%8E%A5%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

## 挤出线的横截面

由于热端加热能力的限制，打印机对于各种耗材丝都有最大体积速度的限制，也就是对单位时间能挤出的最大流量的限制。**最大体积速度=挤出线的横截面积 \* 最大打印速度。**

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E6%9C%80%E5%A4%A7%E4%BD%93%E7%A7%AF%E9%80%9F%E5%BA%A6%E9%99%90%E5%88%B6.png)

对于挤出线条的形状和横截面积计算，我们假设挤压材料的横截面形状是具有半圆形末端的矩形，如下图所示（此处参考[Slic3r](https://manual.slic3r.org/advanced/flow-math)）：

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E6%A8%AA%E6%88%AA%E9%9D%A2%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

# 线宽设置介绍

在Bambu Studio中的工艺——质量——线宽中，可以设置打印各个走线类型的线宽。

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E7%BA%BF%E5%AE%BD%E8%AE%BE%E7%BD%AE.png)

## 缺省

当其他类型走线的线宽设置为0时的默认走线线宽。

## 首层

设置打印首层的时候的线宽，若与其他走线类型的线宽设置冲突，仍然采用设置的首层线宽。首层的默认线宽通常更宽一些，**因为适当增加首层的线宽/层高比可以增强首层的粘附性，确保打印的成功率。**

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E9%A6%96%E5%B1%82%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

## 外墙

设置外墙的走线线宽。模型的最外层壳体属于外墙。

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E5%86%85%E5%A4%96%E5%A2%99%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

## 内墙

设置所有内墙的走线线宽。当你给模型设置了多层墙，除了外墙，其他几层墙都属于内墙。

## 顶层

设置模型顶面的走线线宽。顶面指的是模型的所有顶面走线，如下图所示：

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E9%A1%B6%E9%9D%A2.png)

## 稀疏填充

所有稀疏填充走线的线宽。除了顶壳和底壳层外，其它层中只要有大于“**稀疏填充最小阈值**”的填充区域，都属于稀疏填充。

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E7%A8%80%E7%96%8F%E5%A1%AB%E5%85%85%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

## 内部实心填充

设置内部实心填充的走线线宽。当你给模型设置的底壳或顶壳层数超过1层时，除了最底层和最顶层，其他的底壳和顶壳层都属于内部实心填充。另外，当模型内存在小于\*\*“稀疏填充最小阈值”\*\*的内部填充区域，这部分区域的走线也属于内部实心填充。

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E5%86%85%E9%83%A8%E5%AE%9E%E5%BF%83%E5%A1%AB%E5%85%85%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

## 支撑

设置支撑和支撑面的走线线宽，如下图所示。关于支撑和支撑面详细介绍，可以参考wiki：[支撑结构](../support.md)

![](https://wiki.bambulab.com/bambu-studio/parameter/line-width/%E6%94%AF%E6%92%91%E7%A4%BA%E6%84%8F%E5%9B%BE.png)
