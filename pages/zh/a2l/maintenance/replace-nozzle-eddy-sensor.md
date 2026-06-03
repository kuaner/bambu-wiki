---
path: zh/a2l/maintenance/replace-nozzle-eddy-sensor
title: "A2L 更换挤出机涡流线圈"
description: ""
tags: []
created: 2026-06-01T13:26:55.643Z
updated: 2026-06-01T13:26:55.643Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/replace-nozzle-eddy-sensor
---

## A2L 涡流线圈

![fae067.png](https://public-cdn.bblmw.com/wiki/new/a2l/fae067.png)

## 何时使用本指南？

- Z 轴回零失败
- 涡流线圈断路
- 拓竹售后技术支持后建议更换

## 所需的工具和材料

A2L 涡流线圈

- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀
- 镊子

> 更换涡流线圈预计耗时25分钟

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子元件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## **拆除涡流线圈**

### 1. 移除热端风扇

参照下方教程拆下热端风扇：[更换热端风扇](https://wiki.bambulab.com/zh/a2l/maintenance/replace-cooling-fan-for-hotend)

### 2. 移除涡流线圈

用手握住插头根部，垂直于 PCB 面方向用力抬起以解锁插头断开涡流线圈插头。初次拆卸时，插头上有胶水防松，必须先使用镊子等工具清理胶水或胶布后再操作拔出。

![connectormini.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-nozzle-eddy-sensor/connectormini.jpg)  
![wlxq001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-nozzle-eddy-sensor/wlxq001.webp)

使用 H1.5 内六角螺丝刀拧下图示两颗螺丝，拆下涡流线圈。

![wlxq005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-nozzle-eddy-sensor/wlxq005.jpg)  
![wlxq002.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-nozzle-eddy-sensor/wlxq002.webp)

> TH板上的热端风扇、部件风扇和涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于 PCB 面方向用力抬起以解锁插头**。切勿在水平方向用力，以免损坏插头。

## **安装新涡流线圈**

### 1. 安装涡流线圈

将涡流线圈对准工具头支架的定位凸柱，使用 H1.5螺丝刀锁入两颗螺丝，将涡流线圈线缆沿线槽固定。

![wlxq004.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-nozzle-eddy-sensor/wlxq004.jpg)  
![wlxq003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-nozzle-eddy-sensor/wlxq003.jpg)

### 2. 安装热端风扇

参照下方教程装回热端风扇及其他组件：[更换热端风扇](https://wiki.bambulab.com/zh/a2l/maintenance/replace-cooling-fan-for-hotend)

## 功能验证

为确保一切正常，请打开打印机，操作设备回零，如果设备正常回零无 HMS 报错，表示上方操作均正确。  
![pm03.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/pingmu/pm03.jpg)![pm06.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/pingmu/pm06.jpg)

## 操作后的校准步骤

此外，强烈建议在进行打印之前[清洗纹理PEI打印板](../../general/textured-PEI-plate-not-working-as-expected.md)，因为在更换热端风扇和涡流线圈的过程中，打印板可能会受到污染。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
