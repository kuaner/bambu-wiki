---
path: zh/p2s/maintenance/replace-z-belt
title: "更换 P2S/X2D  Z 皮带"
description: ""
tags: []
created: 2025-10-14T13:13:48.546Z
updated: 2026-05-26T01:54:29.501Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-z-belt
---

## Z 皮带

Z 轴皮带是安装在打印机底部的闭口皮带。  
![11_z_belt.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-timing-pulley/11_z_belt.jpg)

## 何时更换

- Z 皮带磨损
- Z 皮带断裂

## 所需的工具和材料

1. H2.0 内六角扳手
2. H1.5 内六角扳手
3. 新的 Z 皮带

## 安全提示

> 重要提醒 ！
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 Z 皮带

### 步骤 1：锁定热床

在显示屏上操作，将热床下降到底部，使用 H2.0 内六角扳手将 3 颗螺丝（开箱时固定热床的螺丝）分别拧入 3 个 Z 滑块，将 Z 滑块和底座固定在一起。然后关闭打印机，断开电源连接。

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/15_015.png)

![16_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/16_016.png)

> 锁定热床是一个关键预备步骤，此操作能有效固定三根Z轴丝杆的相对位置，防止在松开皮带时，丝杆因外力或床身自重而发生意外旋转或位移。从而使热床的基准面得以维持，避免产生超出允许范围的倾斜，保证打印平台的初始水平度。

### 步骤 2：移除玻璃上盖，侧放打印机

请移除玻璃上盖后再将机器侧放，避免损坏。

如需倒放打印机，在将打印机倒置前请务必拆除显示屏避免造成损坏！拆除显示屏的方式可参考[更换屏幕](replace-screen.md)。

![17_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/17_017.png)

### 步骤 3：移除螺丝

释放弹簧，用 H1.5 内六角扳手移除 3 颗银色螺丝，用 H2.0 内六角扳手移除黑色的螺丝（绿色方框标记）。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/01_001.png)

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/02_002.png)

> **关于 X2D Z 张紧器变更的说明：**  
> 由于 X2D 新增了主动腔温功能,打印机底座在高温环境下会产生微小的物理形变。为确保Z轴在不同温度下均能正常回中并避免运动阻力异常，X2D 已取消张紧器的锁定螺丝,使其能够根据环境温度动态自适应皮带张紧状态。因此,X2D 的 Z 轴皮带在日常使用中无需进行额外张紧处理。  
> ![tensioner.png](https://wiki.bambulab.com/x2d/maintenance/z-tensioner/tensioner.png)

### 步骤 4：移除张紧轮盖子和扭簧

取下张紧轮盖子，移除 Z 轴张紧弹簧。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/03_003.png)

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/04_004.png)

### 步骤 5：移除 Z 皮带

将 Z 皮带从靠近 Z 轴张紧器处取下，再将皮带从另外两个同步轮上取下，即可移除皮带。

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/05_005.png)

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/07_007.png)

注：这里可以不用将 Z 轴张紧器取下。

## 安装 Z 皮带

### 步骤 1：安装 Z 皮带

可以先参考下图将 Z 皮带套在同步轮和电机主动轮上，然后将 Z 皮带绕过 Z 轴张紧器，最后沿着张紧器旁边的同步轮边缘套入。

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/07_007.png)

![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/11_011.png)

![12_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/12_012.png)

### 步骤 2：安装盖子，锁螺丝，卡弹簧

放上张紧器盖子，用 H1.5 内六角扳手锁入 3 颗银色螺丝固定张紧轮盖子，用 H2.0 内六角扳手拧入黑色螺丝（绿色方框标记），但不要拧紧。然后将弹簧的两侧分别卡入对应槽中，如下图所示。

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/02_002.png)

![13_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/13_013.png)

### 步骤 3：解除 Z 滑块锁定

正放打印机，然后使用 H2.0 内六角扳手移除锁定 Z 轴滑块的 3 颗螺丝。

![17_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/17_017.png)

![16_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/16_016.png)

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/15_015.png)

### 步骤 4：Z 轴张紧皮带，拧紧螺丝

重新侧放打印机，往复拉动 Z 轴皮带，确认动作顺畅，然后锁紧黑色螺丝。

![13_013.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/13_013.webp)

## 如何验证成功

连接电源线并启动电源。运行设备校准流程，如果没有报错，更换完成。

如果出现异常，请排查组装是否有问题，特别是皮带是否正确张紧。排除后，再次运行设备自检。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步的帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
