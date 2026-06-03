---
path: zh/x2d/maintenance/adjust-the-eddy-sensor
title: "X2D 涡流线圈调整"
description: "本文将详细为您介绍 X2D 涡流线圈与热端距离调整方法。"
tags: []
created: 2026-04-14T13:09:58.416Z
updated: 2026-05-20T03:27:08.290Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/adjust-the-eddy-sensor
---

## 概述

工具头上的涡流线圈用于参与 **Z 轴归零、热床调平以及动态流量校准** 等功能。当涡流线圈与喷嘴之间的距离过近或过远时，这些功能都可能受到影响。

如果两者之间的间距偏差较大，设备可能会出现 **涡流传感器信号频率过低或灵敏度不足** 的情况。此时需要按照以下步骤对涡流线圈的位置进行调整，以恢复正常工作状态。

![](https://public-cdn.bblmw.com/wiki/new/x2d/adjust-the-eddy-sensor/003.png)

## 视频教程

> 本文以右热端为主要操作对象，视频中包含左热端调整操作。

## 调整步骤

### 1. 打开工具头前盖

抬起工具头前盖组件，并将其固定在工具头上方，露出热端部分，便于后续操作。

![](https://public-cdn.bblmw.com/wiki/new/x2d/adjust-the-eddy-sensor/010.webp)

### 2. 粗略检查涡流线圈间距

裁剪一段约 **6 mm × 60 mm** 的 A4 纸条，并将其 **对折一次**。将纸片插入 **喷嘴与涡流线圈之间**，前后轻轻抽拉纸片进行测试。

![](https://public-cdn.bblmw.com/wiki/new/x2d/adjust-the-eddy-sensor/008.webp)

**判断标准如下：**

- 如果纸片 **过紧难以移动**，说明间距过小；
- 如果纸片 **几乎没有阻力**，说明间距过大；
- 理想状态下应能感受到 **轻微摩擦阻力，但纸片仍可以自由移动**。此时说明喷嘴与涡流线圈之间的间隙大约为 **0.2–0.3 mm**。

### 3. 移除热端组件

如果检测发现间距异常，需要先移除热端组件，以便调整涡流线圈的位置。

![](https://public-cdn.bblmw.com/wiki/new/x2d/adjust-the-eddy-sensor/004.png)

### 4. 调整涡流线圈位置

使用工具 **松开两颗涡流线圈固定螺丝**（无需完全拆下）。

![](https://public-cdn.bblmw.com/wiki/new/x2d/adjust-the-eddy-sensor/002.png)

> 左涡流线圈固定螺丝如下：  
> ![pixpin_2026-05-20_11-25-02.jpg](https://wiki.bambulab.com/x2d/maintenance/adjust-the-eddy-sensor/pixpin_2026-05-20_11-25-02.jpg)

使用 **镊子轻微移动涡流线圈**，调整其与喷嘴之间的距离；调整完成后，使用 **H1.5 内六角螺丝刀**重新锁紧固定螺丝。

|  |  |
| --- | --- |
|  |  |

### 5. 重写装回热端组件

将热端组件装回工具头，并确认 **固定卡扣已完全锁紧到位**。

![](https://public-cdn.bblmw.com/wiki/new/x2d/adjust-the-eddy-sensor/001.png)

### 6. 再次确认间距

再次使用对折的 A4 纸片插入 **喷嘴与涡流线圈之间**进行测试；当纸片移动时能够感受到 **轻微摩擦阻力，同时仍可顺畅滑动**，则说明间隙已经调整至合适范围（约 **0.2–0.3 mm**）。

![](https://public-cdn.bblmw.com/wiki/new/x2d/adjust-the-eddy-sensor/009.webp)

## 功能验证

为确保设备运行正常，请开机执行一次热床调平校准；如果过程中未出现回零失败或调平失败等报错，说明涡流线圈与热端之间的距离处于合适范围。

![](https://public-cdn.bblmw.com/wiki/new/x2d/adjust-the-eddy-sensor/005.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
