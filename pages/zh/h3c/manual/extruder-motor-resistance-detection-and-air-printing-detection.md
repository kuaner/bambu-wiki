---
path: zh/h3c/manual/extruder-motor-resistance-detection-and-air-printing-detection
title: "H3C 挤出电机阻力检测与空打检测"
description: ""
tags: []
created: 2026-11-03T12:13:04.888Z
updated: 2026-11-03T12:13:05.928Z
source: https://wiki.bambulab.com/zh/h3c/manual/extruder-motor-resistance-detection-and-air-printing-detection
---

## 概述

为确保打印过程的连续性与可靠性，避免因耗材挤出问题导致打印失败，H3C 集成了挤出电机阻力检测和空打检测，确保打印任务的顺利进行。

- **挤出电机闭环阻力检测：** 在打印过程中，工具头中的挤出电机会实时监测挤出力的变化。当检测到异常挤出力时，会报错并暂停打印任务，需要用户排除故障后才能继续打印。

![001.webp](https://public-cdn.bblmw.com/wiki/new/h3c/manual/extruder-motor-resistance-detection-and-air-printing-detection/zh/001.webp)

- **空打检测：** 主要用于应对因**热端堵塞、耗材磨损/直径异常、温度设置不当、耗材在外挂料盘或 AMS 内发生缠绕、卡料** 等问题，导致喷嘴无法正常挤出耗材而进行悬空打印的情况。当检测到挤出机未能顺利挤出耗材时，系统将暂停打印并发出警报。

![002.webp](https://public-cdn.bblmw.com/wiki/new/h3c/manual/extruder-motor-resistance-detection-and-air-printing-detection/zh/002.webp)

## 伺服挤出电机闭环阻力检测

### 检测目的

监控打印过程中挤出阻力，阻力异常时可报错暂停，避免打印机故障。

### **开启条件**

默认开启

### **注意事项**

当机器检测到挤出阻力异常并暂停打印后，排查并修复挤出系统故障，并确保耗材正常挤出，继续打印，续打位置可能出现瑕疵。

![003.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/extruder-motor-resistance-detection-and-air-printing-detection/zh/003.png)

### **故障处理步骤**

请参考相关 HMS 报错 Wiki 进行处理：

- [HMS\_0300\_0900\_0002\_0002: 挤出阻力异常，可能堵头或者有耗材卡在工具头内。](../troubleshooting/hmscode/0300_0900_0002_0002.md)

## 空打检测

### 检测目的

由于不同耗材在软硬程度、受潮程度及直径公差等方面存在差异，挤出阻力检测无法覆盖所有挤出异常。例如，当耗材线径偏细导致打印机空打时，挤出电机传感器可能无明显变化，此时需依赖空打检测来识别故障。

### **开启条件**

默认开启

### **注意事项**

从异常发生到被检测出来可能**存在一定延迟**，期间耗材可能已空打一段时间。排除问题并续打后，打印件表面可能出现瑕疵。

![004.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/extruder-motor-resistance-detection-and-air-printing-detection/zh/004.png)

### **故障处理步骤**

请参考相关 HMS 报错 Wiki 进行处理：

- [HMS\_0300-0900-0002-0004：挤出阻力异常，可能堵头或者有耗材卡在工具头内，或者外部挂载的耗材缠绕。](../../p2s/troubleshooting/hmscode/0300_0900_0002_0004.md)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
