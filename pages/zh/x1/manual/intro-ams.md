---
path: zh/x1/manual/intro-ams
title: "AMS 主要组件介绍"
description: ""
tags: []
created: 2022-07-29T07:10:33.333Z
updated: 2025-01-09T02:27:29.470Z
source: https://wiki.bambulab.com/zh/x1/manual/intro-ams
---

我们将介绍 AMS（Automated Material System）的主要组件，以便您对 AMS 及其工作原理有一个大致的了解。此外，在使用 AMS 时，请注意**环境温度需保持在 10-30 ℃，湿度需低于 85%**。

## **AMS 是如何工作的?**

AMS 由三个主要部分组成：**线材槽**、**线材五通**和**供料缓冲器**。 **线材槽**都有独立电机控制将线材送入或绕回线轴。**线材五通**将四个线材的路径合并为一个，通过无刷电机为线材提供第二级驱动力。**供料缓冲器**位于打印机后部，将 AMS 连接到机头挤出机，以确保线材上的张力在设计范围内，使挤出机能够轻松准确地工作。

线材传送路径中共配备了 10 个传感器，打印时线材的位置、送料速度和张力都受到精细的监控和控制。

|  |  |
| --- | --- |
|  |  |

## 线材槽

AMS 有 4 个线材槽，槽内的一阶送料器有独立的电机和齿轮推动线材向前或将其绕回线轴，有一个传感器来检测线材。当插入线材时，会像挤出机一样拉动线材；当需要将线材卷回料轴时，主动轴会转动料盘将线材缠绕回收。

![](https://wiki.bambulab.com/x1/manual/intro-ams/filament-slots.jpg)

## 线材五通

**线材五通**位于 AMS 的尾部，由四个霍尔传感器、一个磁性旋转编码器和一个无刷电机组成。 它将四个线材路径合并为一个。 霍尔传感器检测线材何时到达特定位置，激活无刷电机为线材提供第二级驱动力。

![](https://wiki.bambulab.com/x1/manual/intro-ams/filament-hub.jpg)

## **供料缓冲器**

供料缓冲器位于打印机的背面，连接到 AMS 和工具头挤出机，由滑块、弹簧和霍尔传感器组成。AMS将线材推入工具头挤出机时，由于耗材的压力，滑块向前移动，通过霍尔传感器检测滑块移动的位置，供料缓冲器将信号反馈回 AMS 和打印机。通过控制AMS的进给速度，可以确保耗材张力在设计范围内，这样工具头挤出机就可以轻松而精确地工作。

![](https://wiki.bambulab.com/x1/manual/intro-ams/filament-buffer.png)![](https://wiki.bambulab.com/x1/manual/intro-ams/ams-connection.jpg)

## **AMS 集束器**

**AMS 集束器**可以替代供料缓冲器。 它允许用户最多连接四个 AMS 单元，可以为打印机提供 16 个不同的材线轴。 AMS 集束器由线材选择模块和缓冲模块组成。 线材选择模块有四个入口连接到四个独立的 AMS 单元，每个插槽都有一个霍尔传感器来检测线材。 缓冲模块的功能与标准供料缓冲器相同，它具有滑块、弹簧和霍尔传感器，确保耗线材上的张力在设计范围内工作。

![](https://wiki.bambulab.com/x1/manual/intro-ams/ams-hub.png)![](https://wiki.bambulab.com/x1/manual/intro-ams/ams-hub-connection.jpg)![](https://wiki.bambulab.com/x1/manual/intro-ams/4x-ams-hub.jpg)

## **RFID 系统**

**RFID 系统**可以识别 Bambu Lab 线材线轴上的 RFID 标签，并将线材信息自动同步到切片软件Bambu Studio中。

![](https://wiki.bambulab.com/x1/manual/intro-ams/rfid-filament.jpg)![](https://wiki.bambulab.com/x1/manual/intro-ams/rfid-antenna.png)

## 防潮系统

**防潮系统**由湿度传感器、两包干燥剂和硅橡胶“O”形圈组成。干燥剂吸收水分保持 AMS 中空气干燥。硅橡胶“O”型圈可以保持 AMS 密封，避免损坏吸湿线材。当空气湿度超出 AMS 预设标准时，湿度传感器会检测并提醒用户更换干燥剂。

![](https://wiki.bambulab.com/ams/ams-lite-body/防潮系统.jpg)
> ***注意：干燥剂需从密封透明塑料袋中取出后，再放入AMS中。***
