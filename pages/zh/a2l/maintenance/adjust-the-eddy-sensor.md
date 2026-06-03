---
path: zh/a2l/maintenance/adjust-the-eddy-sensor
title: "A2L 涡流线圈调整教程"
description: "当设备回中或调平出现异常时，可能需要调整涡流线圈位置，本文介绍如何操作。"
tags: []
created: 2026-06-01T13:17:06.438Z
updated: 2026-06-01T13:17:06.438Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/adjust-the-eddy-sensor
---

## 何时使用

当设备回中或调平出现异常时，可能需要调整涡流线圈位置。

## 所需工具和材料

- H1.5 & H2.0 内六角螺丝刀
- 镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 操作步骤

### 取下工具头前盖

双手按住工具头前盖靠下的两侧部分（注意避开热端散热风扇），向斜上方轻提，即可取下工具头前盖。

![gjt001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/gjt001.webp)

### 移除热端风扇

拧松固定热端风扇的 2 颗螺丝。

![hotendfan.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/hotendfan.jpg)  
![hotendfan2.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/hotendfan2.jpg)

小心地将热端风扇挂在旁边，请勿用力拉扯线缆。

> 螺丝孔位也可查看下图了解

![hotendfan3.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/hotendfan3.jpg)

### 调整涡流线圈

从 A4 纸上裁剪出纸片，对折两次得到厚度大概为 0.2mm 的纸条。

![a4.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/a4.jpg)

向热端上表面与黑色零件的缝隙中塞入纸条，并来回拉动确保纸张能够塞入缝隙且阻力较小。

![eddygap.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/eddygap.jpg)  
![adjust.webp](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/adjust.webp)

若阻力较大，请打开加热组件卡扣，取下热端。

![hotend.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/hotend.jpg)  
![hotend2.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/hotend2.jpg)

使用 H1.5 螺丝刀拧松涡流线圈的 2 颗固定螺丝，无需拧下。

![screw31.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/screw31.jpg)  
![screw1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/screw1.jpg)  
![screw21.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/screw21.jpg)

使用镊子调整涡流线圈位置，重新锁紧螺丝。

![higher.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/higher.jpg)

### 功能验证

安装上喷嘴后开机，点击屏幕进行回中。若 Z 回中成功则涡流线圈功能正常，若回中依然失败，请重复上述调整过程或联系客户支持团队。

![homing.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/homing.jpg)

### 装回热端风扇和前盖

回中成功后，拧紧热端风扇的 2 颗固定螺丝。

![hotendfan3.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/adjust-the-eddy-sensor/hotendfan3.jpg)

将硅胶套自下而上安装到热端上，确保安装后硅胶套平整，且不与周围塑胶部件接触。  
![rdgjt001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-silicone-sock-for-hotend/rdgjt001.webp)

再将前盖安回挤出机上。

![gjt002.webp](https://public-cdn.bblmw.com/wiki/new/a2l/gjt002.webp)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
