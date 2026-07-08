---
path: zh/p2s/troubleshooting/build-plate-not-detected
title: "0500-4095： P2S/X2D"
description: ""
tags: []
created: 2026-04-30T10:18:14.384Z
updated: 2026-07-02T02:41:18.750Z
source: https://wiki.bambulab.com/zh/p2s/troubleshooting/build-plate-not-detected
---

## 故障描述

打印板的定位标记未被检测到。Bambu Lab 打印板上印有定位标记，用于检测打印板正确放置和对齐。

**产生此告警的可能原因：**

- 放置打印板的时候没有对齐
- 标记被损坏或被阻挡

> 注意：若您使用的是第三方打印板，只需忽略该消息。

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

### 排故措施

#### 步骤1. 检查打印板放置状态

检查打印板是否放置在热床上。  
![p2sputplate2.png](https://wiki.bambulab.com/zh/h2/troubleshooting/calibrate-failed/p2sputplate2.png)

检查打印板边缘是否对齐热床边缘，是否与热床定位件契合。

![p2splateplacement.png](https://wiki.bambulab.com/zh/h2/troubleshooting/calibrate-failed/p2splateplacement.png)

#### 步骤2. 检查打印板标记状态

检查打印板标记是否完好、无异物阻挡。

![p2smarker.png](https://wiki.bambulab.com/zh/h2/troubleshooting/calibrate-failed/p2smarker.png)

#### 步骤3. 重新校准

完成以上排查步骤后，请在打印机屏幕上点击**重新校准**。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
