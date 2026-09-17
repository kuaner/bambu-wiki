---
path: zh/x1/manual/switch-from-ams-to-spool-holder
title: "从 AMS 上料切换到打印机上料"
description: "本指南指导您如何从 AMS 上料切换到打印机上料"
tags: ["ams", "x1"]
created: 2022-07-29T07:26:47.142Z
updated: 2026-08-28T04:25:27.220Z
source: https://wiki.bambulab.com/zh/x1/manual/switch-from-ams-to-spool-holder
---

## 前言

**AMS 不支持某些耗材（如 TPU）和一些更大尺寸的料盘**。此类耗材需要放置在打印机后部的料盘支架上，才能正常打印。

## 适用机型

AMS

## 安全提醒

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 操作指引

### 将耗材退料至 AMS

如果耗材已经被送入挤出机，请在屏幕中点击 AMS 页面，选择正在使用的线槽，并按下退料按钮，将耗材退回至 AMS。

如果耗材已经退回到 AMS，则跳过此步骤。

![退料.jpg](https://wiki.bambulab.com/%E9%80%80%E6%96%99.jpg)

### 拔掉料盘支架附近 AMS 的 4-pin 连接头

> **注意：** 如果您使用的是 OTA 1.0.0.0 之前的固件，则不可热插拔，需要先关闭打印机电源。

![](https://wiki.bambulab.com/x1/manual/switch-from-ams-to-spool-holder/unplug_cable_4pin.jpg)

### 按下气动接头，从打印机侧取出气动接头和 PTFE 管

![](https://wiki.bambulab.com/x1/manual/switch-from-ams-to-spool-holder/disconnect_ptfe_tube_connector.jpg)

### 装入新耗材

您可以参考此页面装入新耗材：[更换打印耗材 | Bambu Lab Wiki](loading-filament.md)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
