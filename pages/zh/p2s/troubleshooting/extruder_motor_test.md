---
path: zh/p2s/troubleshooting/extruder_motor_test
title: "P2S/X2D 挤出电机测试方法"
description: "本文介绍了 P2S/X2D 挤出电机过载时，对挤出电机的测试方法。"
tags: ["p2s", "x2d"]
created: 2026-05-08T02:22:26.905Z
updated: 2026-08-28T06:42:09.462Z
source: https://wiki.bambulab.com/zh/p2s/troubleshooting/extruder_motor_test
---

## 现象描述

当打印机经常提示挤出电机过载时，可能是因为喷嘴或挤出机堵塞等问题导致过载，也可能会是电机存在故障。  
在排除喷嘴/挤出机堵塞后，若设备仍然报错挤出电机过载，可提交技术工单，申请专用固件并完成更新后，再运行测试 Gcode 进行故障排查，运行后如果弹出特定的HMS，则是判断是电机零位发生偏移，需要更换电机。

> 本文档所描述的方案需要配合特定版本的固件方可使用，通常版本的固件测试结果无效，测试前请提交技术工单和日志给客服确认。

## 安全提示

> 注意：在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 故障定位与解决流程

### 步骤 1. 检查是否堵头

请先参考以下 Wiki 检查打印机是否堵塞，并根据指引进行清理。  
[X2D](../../x2d/troubleshooting/clogging.md)  
[P2S](clogging.md)

### 步骤 2. 退料

排除堵头的情况后，在屏幕点击“退料”，确保挤出机此时无负载。对于 X2D 来说只需控制主挤出机退料。  
![p2s退料.png](https://wiki.bambulab.com/p2s/troubleshooting/hmscode/0300_1d00_0001_000a/p2s%E9%80%80%E6%96%99.png)

### 步骤 3. 升级专用固件

专用固件需通过技术工单获取。

### 步骤 4. 运行 G-code 文件

退料完成后，根据产品型号下载附件并导入 U 盘中，将 U 盘插上打印机，然后在打印文件中找到同名文件发起一次打印。

[p2s-zerotest.gcode](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/p2s-zerotest.gcode)  
[x2d-zerotest.gcode](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/x2d-zerotest.gcode)  
![文件1.png](https://wiki.bambulab.com/p2s/troubleshooting/hmscode/0300_1d00_0001_000a/%E6%96%87%E4%BB%B61.png)

X2D:

- 若屏幕出现“0300-1D00-0001-000A”报错，说明故障为电机本身，需要更换挤出电机，请参考[该Wiki](../../x2d/maintenance/replace-3508-extruder-servo-motor.md) 进行更换；
- 若未出现报错，请参考[该Wiki](../../x2d/troubleshooting/hmscode/0300_0900_0002_0001.md) 检查其他可能性。

P2S:

- 若屏幕出现“0300-1D00-0001-000A”报错，说明故障为电机本身，需要更换挤出电机，请参考[该Wiki](../maintenance/replace-3508-extruder-servo-motor.md) 进行更换；
- 若未出现报错，请参考[该Wiki](hmscode/0300_0900_0002_0001.md) 检查其他可能性。

### 步骤 5. 恢复通用固件

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
