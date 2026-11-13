---
path: zh/h3c/troubleshooting/xy-homing-failed
title: "03004032：拓竹H3C"
description: ""
tags: []
created: 2026-11-03T13:00:19.252Z
updated: 2026-11-10T08:47:28.086Z
source: https://wiki.bambulab.com/zh/h3c/troubleshooting/xy-homing-failed
---

## 故障描述

当X轴的移动行程小于设定值，或 X 轴回零运动失败时，设备将认为工具头被卡住或 X 轴移动阻力过大。

## 可能的原因：

- 扎带、泡棉未拆下
- 工具头被卡住
- X 轴阻力过大

## 故障排除

### 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

### 步骤1. 外观检查

确保固定工具头的蓝色扎带已经剪断，泡棉已被取下。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/xy-homing-failed/zh/10_03004032_h3c-01.png)

注意请勿剪断一旁的同步带。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/xy-homing-failed/zh/10_03004032_h3c-02.png)

### 步骤2. 手动推拉

手动推拉工具头左右移动，若移动阻力较大，请则沿着同步带检查是否存在异物阻碍，并及时清理；若不存在异物请进行下一步。

![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/xy-homing-failed/zh/10_03004032_h3c-03.gif)  
![mvi_7671_11.gif](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/xy-homing-failed/zh/mvi_7671_11.gif)

### 步骤3. X 轴维护

请参考 [XYZ 轴维护](../maintenance/lubricate-x-y-z-axis.md)清理并润滑 XY 轴，完成后再次发起任务，若依然无法完成回零，请联系客户支持团队。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
