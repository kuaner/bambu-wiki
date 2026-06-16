---
path: zh/a2l/maintenance/replace-cutting-module-adapter-board
title: "A2L 更换刀切模组转接板"
description: "本文介绍了如何更换 A2L 刀切模组转接板"
tags: []
created: 2026-06-01T13:08:04.445Z
updated: 2026-06-05T07:47:05.396Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/replace-cutting-module-adapter-board
---

## A2L 刀切模组转接板

![dlb075.png](https://public-cdn.bblmw.com/wiki/new/a2l/danpintu/dlb075.png)

## 何时使用本指南？

- 刀切模组插座物理损坏或功能异常
- 经拓竹售后技术支持后建议更换

## 所需的工具和材料

刀切模组转接板

- H1.5 内六角螺丝刀
- 镊子（可选）

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**

## 视频指南

## **拆除刀切模组转接板**

### 1. 移除TH板

请参照独立教程完成TH板的拆卸：[TH 板更换指南](replace-th-board.md)

### 2. 移除刀切模组转接板

使用 H1.5 内六角螺丝刀拆除两颗固定螺丝，然后取下刀切模组转接板。  
![dq001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq001.jpg)![dq002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq002.jpg)

### 3. 移除转接板排线

用手握住插头根部，**垂直于 PCB 面方向用力抬起以解锁插头**。  
![dq004.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq004.webp)

> 切勿在水平方向用力拉扯线缆，以免损坏插头。

## **安装刀切模组转接板**

### 1.安装转接板排线

参照图示，将排线端子与母座对齐后按压到底，确保连接牢固。  
![dq005.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq005.webp)

### 2.安装刀切模组转接板

轻轻抬起进料霍尔板的排线，将刀切模组转接板放入工具头支架的对应位置，对准螺丝孔位，使用 H1.5 内六角螺丝刀锁紧两颗固定螺丝。  
![dq003.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq003.webp)![dq001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq001.jpg)

> 注意：锁入螺丝前请确认进料霍尔板排线没有被转接板压到，以免损坏排线。

### 3. 安装 TH 板

请参照独立教程将 TH 板装回：[TH 板更换指南](replace-th-board.md)

## 功能验证

开启打印机电源，连接刀切模组，在打印机控制界面运行模组初始化程序。观察初始化过程是否顺畅，无报错即表示更换成功。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
