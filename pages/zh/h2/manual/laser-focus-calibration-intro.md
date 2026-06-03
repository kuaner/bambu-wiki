---
path: zh/h2/manual/laser-focus-calibration-intro
title: "激光焦点标定介绍"
description: ""
tags: []
created: 2025-03-25T12:35:07.015Z
updated: 2026-02-09T07:11:56.418Z
source: https://wiki.bambulab.com/zh/h2/manual/laser-focus-calibration-intro
---

> **注意**：本页面以 H2D 机器为例。**H2S 和 H2C 的更换步骤完全相同**。

## 为什么要标定激光的焦点？

由于激光模组是手动安装到工具头上的，激光器本身与喷嘴之间的高度差会受到加工公差、装配公差的影响，进而使得激光焦点与喷嘴之间的相对高度跟设计值有轻微的差异。如果加工时依旧按照设计值去执行的话，就有可能导致切割或雕刻时激光焦点没有在期望的高度上，从而导致加工效果变差。

## 什么时候要标定激光的焦点？

1. 激光模组到手第一次安装后；
2. 激光模组受到磕碰（包括其侧面的激光测高器）；
3. 在雕刻时发现线宽变粗。

## 如何触发激光焦点标定？

目前，当雕刻激光安装到工具头上并插入电源线后，可在激光模组初始化中进行激光焦点的标定。

打印机屏幕的操作步骤为：设置 -> 工具箱 -> 激光模组初始化。

![](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-10.png)

## 激光焦点标定操作过程

### 1. 准备标定耗材

如下图所示，找一张矩形白色卡纸：

![](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-12.png)

**如果找不到卡纸了，或是卡纸出现折弯，怎么办？**

- 选项1：卡纸厚度为 0.35mm，如能找到此类卡纸，请剪取一块约 120mm × 120mm 的正方形（尺寸要求不严格，建议边长大于 100mm）。注意：卡纸需为浅色，深色卡纸不可使用。
- 选项2：普通A4纸，建议将 A4 纸的短边紧贴激光垫板底部，长边对半裁开，刀条按隔一放一的方式排列。

|  |  |
| --- | --- |

- 选项3：打印机包装内附有一张白色珠光卡纸，您可以将其对折撕开，取其中一半来替代白色卡纸使用,刀条按隔一放一的方式排列。

|  |  |
| --- | --- |

- 选项4：如果你有透明亚克力板、便签纸、胶水，则可以同时使用这三样，如下图。**注意：一定要将胶水涂满亚克力板，防止纸张有翘曲或鼓起的地方。**

![](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-11.png)

经测试，以下是不太适用于标定的耗材：

1. 木板 ---- 表面纹理以及热溢出会使得标定线模糊不清，勉强可用；
2. 激光调光纸 ---- 焦点处功率太高会直接烧穿；
3. 阳极氧化铝板 ---- 表面纹理会影响识别效果。

### 2. 标定耗材的放置

首先，需要将至少2条刀条放置在靠近激光垫板标定台附近的位置，如下图：

![](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image.png)

然后将标定用的耗材放置在紧贴标定台的中央位置，下图为正确范例：

![](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-1.png)

![虽然使用过，但是烧灼过的区域不在本次标定用到的范围内](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-2.png)

![便签纸或A4纸用胶水完全贴合在透明亚克力板上](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-3.png)

**以下为错误放置的范例：**  
卡纸掉落在齿条中，未贴近标定平台  
![卡纸掉落在齿条中，未贴近标定平台](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-4.png)  
卡纸翘曲

![卡纸翘曲](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-5.png)  
直接将A4/A5纸放置在垫板上，而不调节齿条间距，可能会太薄了容易被吹动  
![直接将A4/A5纸放置在垫板上，太薄了容易被吹动](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-6.png)  
卡纸烧灼过的区域正好是本次标定会用到的范围  
![卡纸烧灼过的区域正好是本次标定会用到的范围](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-7.png)  
使用亚力克板+便签纸组合时，没有用胶将便签纸完全贴合在亚克力板上，导致其边缘翘起  
![使用亚力克板+便签纸组合时，没有用胶将便签纸完全贴合在亚克力板上，导致其边缘翘起](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-8.png)

### 3. 开始标定

在放置好标定耗材后，按照屏幕上的步骤提示，执行激光模组初始化流程即可。

![](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/img_v3_02ig_35339048-e0fb-4ea7-999a-e9e0ed7289ag.jpg)

![](https://wiki.bambulab.com/h2/manual/laser-focus-calibration-intro/image-9.png)
