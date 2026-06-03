---
path: zh/p2s/maintenance/replace-z-belt-tensioner
title: "更换 P2S/X2D Z 张紧器"
description: "本文介绍了如何更换 P2S Z 张紧器"
tags: []
created: 2025-10-14T13:13:45.929Z
updated: 2026-05-06T06:48:18.323Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-z-belt-tensioner
---

## Z 轴张紧器

Z 轴张紧器是安装在打印机底部，用于张紧 Z 轴皮带的零件。

## 何时更换

- 张紧器惰轮异响，打油未能解决；
- 张紧器惰轮轴承损坏

## 所需的工具和材料

1. H2.0 内六角扳手
2. H1.5 内六角扳手
3. 新的 Z 轴张紧器

## 安全提示

> 重要提醒 ！
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

> **关于 X2D Z 张紧器变更的说明：**  
> 由于 X2D 新增了主动腔温功能,打印机底座在高温环境下会产生微小的物理形变。为确保Z轴在不同温度下均能正常回中并避免运动阻力异常，X2D 已取消张紧器的锁定螺丝,使其能够根据环境温度动态自适应皮带张紧状态。因此,X2D 的 Z 轴皮带在日常使用中无需进行额外张紧处理。  
> ![tensioner.png](https://wiki.bambulab.com/x2d/maintenance/z-tensioner/tensioner.png)

## 移除 Z 轴张紧器

### 步骤 1：锁定热床

在显示屏上操作，将热床下降到底部，使用 H2.0 内六角扳手将 3 颗螺丝（开箱时固定热床的螺丝）分别拧入 3 个 Z 滑块，将 Z 滑块和底座固定在一起。然后关闭打印机，断开电源连接。

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/15_015.png)

![16_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/16_016.png)

> 锁定热床是一个关键预备步骤，此操作能有效固定三根Z轴丝杆的相对位置，防止在松开皮带时，丝杆因外力或床身自重而发生意外旋转或位移。从而使热床的基准面得以维持，避免产生超出允许范围的倾斜，保证打印平台的初始水平度。

### 步骤 2：移除玻璃上盖，侧放打印机

请移除玻璃上盖后再将机器侧放，避免损坏。

如需倒放打印机，在将打印机倒置前请务必拆除显示屏避免造成损坏！拆除显示屏的方式可参考[更换 P2S 屏幕](replace-screen.md)。

![17_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/17_017.png)

### 步骤 3：移除张紧轮盖子和扭簧

释放弹簧，用 H1.5 内六角扳手移除 3 颗螺丝，用 H2.0 内六角扳手移除黑色的螺丝（绿色方框标记）。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/01_001.png)

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/02_002.png)

取下张紧轮盖子，移除 Z 轴张紧弹簧。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/03_003.png)

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/04_004.png)

### 步骤 4：移除 Z 轴张紧器

将 Z 皮带从靠近 Z 轴张紧器处取下，便于后续移除 Z 轴张紧器。

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/05_005.png)

将张紧器移动至导轨尽头以移除张紧器组件。注意组件里有一个螺母，小心切勿丢失。

![z-tensioner.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/z-tensioner.webp)

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/06_006.png)

## 安装 Z 轴张紧器

### 步骤 1：安装 Z 轴张紧器

先确认前面提到的螺母有在组件上，将张紧器组件安装到相应位置，注意根据卡扣位完成安装。

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/06_006.png)

![09_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/09_009.png)

![10_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/10_010.png)

### 步骤 2：安装皮带和张紧轮盖子

将扭簧安装到相应的立柱上，注意扭簧的长边在左边，如下图所示。

![08_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/08_008.png)

将 Z 皮带从 Z 同步轮边缘套入。

![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/11_011.png)

![12_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/12_012.png)

放上张紧器盖子，用 H1.5 内六角扳手锁入 3 颗螺丝固定张紧轮盖子，用 H2.0 内六角扳手拧入黑色螺丝（绿色方框标记），但不要拧紧，然后将弹簧的两侧分别卡入对应槽中。

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/02_002.png)

![13_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/13_013.png)

### 步骤 3：解除 Z 滑块锁定

正放打印机，然后使用 H2.0 内六角扳手移除锁定 Z 轴滑块的 3 颗螺丝。

![17_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/17_017.png)

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/15_015.png)

### 步骤 4：张紧 Z 轴皮带

重新侧放打印机，往复拉动 Z 轴皮带，确认动作顺畅，然后锁紧张紧器螺丝。

![13_013.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/13_013.webp)

## 如何验证成功

连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆是否连接正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
