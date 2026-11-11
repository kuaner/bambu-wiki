---
path: zh/h3c/troubleshooting/printtool-controlboard-not-detected
title: "0300403A：拓竹H3C"
description: ""
tags: []
created: 2026-11-03T12:08:02.406Z
updated: 2026-11-10T08:47:25.873Z
source: https://wiki.bambulab.com/zh/h3c/troubleshooting/printtool-controlboard-not-detected
---

## 故障描述

设备检测到打印头控制板未安装时，将提示该报错信息，请检查打印头控制板连接线是否安装。

## 可能的原因

- 打印机背部的连接线未插入或松动
- AMS 下侧的连接线未插入或松动

## 故障排除

> 请先将 AMS 右侧板取下，方便后续操作。

### 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

#### 步骤 1. 检查打印机背部线缆

- 检查下图中箭头指示的接线是否插紧，确保插头插紧。  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/printtool-controlboard-not-detected/zh/01_0300403a_h3c-01.png)
- 若报错消失，则可以正常使用。
- 若报错仍存在，请参考步骤 2。

#### 步骤 2. 检查 AMS 下方线缆

- 打开 AMS 右侧板；  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/printtool-controlboard-not-detected/zh/01_0300403a_h3c-02.png)
- 检查 AMS 下方的连接线是否插紧；如未插紧，请重新插入；  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/printtool-controlboard-not-detected/zh/01_0300403a_h3c-03.png)
- 若报错消失，则可以正常使用；
- 若仍报错，请联系客户支持团队。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
