---
path: zh/ams/manual/ams-not-unloading-to-save-filament
title: "打印相同材料时关闭退料与冲刷以节省耗材"
description: ""
tags: []
created: 2024-01-27T15:57:28.690Z
updated: 2026-05-25T08:49:55.536Z
source: https://wiki.bambulab.com/zh/ams/manual/ams-not-unloading-to-save-filament
---

## 背景

目前，在使用AMS打印结束时 AMS 会自动将耗材退回 AMS 内部，再次发起打印的时候，AMS 会重新进料至工具头。

与此同时，我们收到了一些用户的反馈，在连续多盘任务都是打印相同耗材的情况下，不希望 AMS 在打印结束后就退料，因为再次进料的过程会浪费一定的时间，而且重新进料冲刷也会造成一定量的材料浪费，该需求可通过以下的 Gcode 修改实现，但需注意：

1. 使用AMS打印结束后不退料会影响 RFID 读取等功能；

2. 重新进料不冲刷可能会导致堵头，所以需在更换新材料打印时请还原已修改的设置。

选择对应机型快速跳转：[X2D](https://wiki.bambulab.com/zh/ams/manual/ams-not-unloading-to-save-filament#x2d) |[P2S](https://wiki.bambulab.com/zh/ams/manual/ams-not-unloading-to-save-filament#p2s) | [H2D](https://wiki.bambulab.com/zh/ams/manual/ams-not-unloading-to-save-filament#h2d) | [H2S](https://wiki.bambulab.com/zh/ams/manual/ams-not-unloading-to-save-filament#h2s) | [H2C](https://wiki.bambulab.com/zh/ams/manual/ams-not-unloading-to-save-filament#h2c) | [A1 系列](https://wiki.bambulab.com/zh/ams/manual/ams-not-unloading-to-save-filament#a1-%E7%B3%BB%E5%88%97) | [X1 & P1系列](https://wiki.bambulab.com/zh/ams/manual/ams-not-unloading-to-save-filament#xp%E7%B3%BB%E5%88%97)

## 操作方法

### X2D

若使用AMS连续多盘打印相同耗材，可通过以下方式关闭退料与冲刷以节省耗材和时间：

1. 在**打印机设置->打印机G-code->打印机结束G-code**中将耗材退回AMS的部分的Gcode删除。

![](https://wiki.bambulab.com/x2d/manual/ams-not-unloading-to-save-filament/1.jpg)

删除位于“pull back filament to ams”与“G150.3”之间的 G-code。  
![](https://wiki.bambulab.com/x2d/manual/ams-not-unloading-to-save-filament/2.jpg)

![](https://wiki.bambulab.com/x2d/manual/ams-not-unloading-to-save-filament/3.jpg)

这样打印结束后 AMS 就不会退料，在下一次发起打印任务的时候可以快速开始，将会节省一定的时间。

**需要注意的是：AMS 未退料，材料仍然在工具头中的时候，AMS不属于空闲状态，无法实现读取 RFID、余料检测等功能。**

2. 在打印机起始 Gcode 里注释掉或者删除掉这两行，打印前就不会冲刷耗材，如下图：

![](https://wiki.bambulab.com/x2d/manual/ams-not-unloading-to-save-filament/4.jpg)

这样在下一次开始打印前就不会冲刷耗材，能够节省一定的材料。

**但有一定风险导致下一次打印堵头，请谨慎操作。**

**注意：在需打印其他耗材时还原上述修改，防止堵头或混色。**

### P2S

若使用AMS连续多盘打印相同耗材，可通过以下方式关闭退料与冲刷以节省耗材和时间：

1. 在**打印机设置->打印机G-code->打印机结束G-code**中将耗材退回AMS的部分的Gcode删除，如下图：

![](https://wiki.bambulab.com/p2s/manual/ams-not-unloading-to-save-filament/zh13.png)
![](https://wiki.bambulab.com/p2s/manual/ams-not-unloading-to-save-filament/zh11.png)

这样打印结束后 AMS 就不会退料，在下一次发起打印任务的时候可以快速开始，将会节省一定的时间。

**需要注意的是：AMS 未退料，材料仍然在工具头中的时候，AMS不属于空闲状态，无法实现读取 RFID、余料检测等功能。**

2. 在打印机起始 Gcode 里注释掉或者删除掉这两行，打印前就不会冲刷耗材，如下图：

![](https://wiki.bambulab.com/p2s/manual/ams-not-unloading-to-save-filament/zh12.png)

这样在下一次开始打印前就不会冲刷耗材，能够节省一定的材料。

**但有一定风险导致下一次打印堵头，请谨慎操作。**

**注意：在需打印其他耗材时还原上述修改，防止堵头或混色。**

### H2D

若使用AMS连续多盘打印相同耗材，可通过以下方式关闭退料与冲刷以节省耗材和时间：

1. 在**打印机设置->打印机G-code->打印机结束G-code**中将耗材退回AMS的部分的 Gcode 删除，如下图：

![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/screenshot-20250519-150648.png)
![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/20250519-145048.jpg)

这样打印结束后AMS就不会退料，在下一次发起打印任务的时候可以快速开始，将会节省一定的时间。**需要注意的是：AMS未退料，材料仍然在工具头中的时候，AMS不属于空闲状态，无法实现读取RFID、余料检测等功能。**

2. 在打印机起始 Gcode 里注释掉或者删除掉这两行，打印前就不会冲刷耗材，如下图：

![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/20250519-144939.jpg)

这样在下一次开始打印前就不会冲刷耗材，能够节省一定的材料。**但有一定风险导致下一次打印堵头，请谨慎操作。注意在需打印其他耗材时还原上述修改，防止堵头或混色。**

### H2S

若使用AMS连续多盘打印相同耗材，可通过以下方式关闭退料与冲刷以节省耗材和时间：

1. 在**打印机设置->打印机G-code->打印机结束G-code**中将耗材退回AMS的部分的 Gcode 删除，如下图：

![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/h2s.png)
![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/h2s_end1.png)

这样打印结束后AMS就不会退料，在下一次发起打印任务的时候可以快速开始，将会节省一定的时间。**需要注意的是：AMS未退料，材料仍然在工具头中的时候，AMS不属于空闲状态，无法实现读取RFID、余料检测等功能。**

2. 在打印机起始 Gcode 里注释掉或者删除掉这两行，打印前就不会冲刷耗材，如下图：

![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/h2s_start.png)

这样在下一次开始打印前就不会冲刷耗材，能够节省一定的材料。**但有一定风险导致下一次打印堵头，请谨慎操作。注意在需打印其他耗材时还原上述修改，防止堵头或混色。**

### H2C

若使用AMS连续多盘打印相同耗材，可通过以下方式关闭退料与冲刷以节省耗材和时间：

1. 在**打印机设置->打印机G-code->打印机结束G-code**中将耗材退回AMS的部分的 Gcode 删除，如下图：

![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/h2c.png)
![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/h2c_end1.png)

这样打印结束后AMS就不会退料，在下一次发起打印任务的时候可以快速开始，将会节省一定的时间。**需要注意的是：AMS未退料，材料仍然在工具头中的时候，AMS不属于空闲状态，无法实现读取RFID、余料检测等功能。**

2. 在打印机起始 Gcode 里注释掉或者删除掉这两行，打印前就不会冲刷耗材，如下图：

![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/h2c_start1.png)

这样在下一次开始打印前就不会冲刷耗材，能够节省一定的材料。**但有一定风险导致下一次打印堵头，请谨慎操作。注意在需打印其他耗材时还原上述修改，防止堵头或混色。**

### X1/P1系列

若使用AMS连续多盘打印相同耗材，可通过以下方式关闭退料与冲刷以节省耗材和时间：

1. 在**打印机设置->打印机 G-code->打印机结束 G-code**中将耗材退回AMS的部分的 Gcode 删除，如下图：

![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/删除退料gcode1.png)

这样打印结束后AMS就不会退料，在下一次发起打印任务的时候可以快速开始，将会节省一定的时间。**需要注意的是：AMS未退料，材料仍然在工具头中的时候，AMS不属于空闲状态，无法实现读取RFID、余料检测等功能。**

2. 在**打印机设置->打印机G-code->打印机起始G-code中**删除冲刷旧耗材部分的Gcode，如下图：

![](https://wiki.bambulab.com/ams/ams-not-unload-when-finish/删除冲刷gcode.png)

这样在下一次开始打印前就不会冲刷耗材，能够节省一定的材料。**但有一定风险导致下一次打印堵头，请谨慎操作。注意在需打印其他耗材时还原上述修改，防止堵头或混色。**

### A1 系列

若使用AMS连续多盘打印相同耗材，可通过以下方式关闭退料与冲刷以节省耗材和时间：

1. 在**打印机设置->打印机G-code->打印机结束G-code**中将耗材退回AMS的部分的Gcode删除，如下图：

![](https://wiki.bambulab.com/studio-ams/zh.png)

这样打印结束后AMS就不会退料，在下一次发起打印任务的时候可以快速开始，将会节省一定的时间。**需要注意的是：AMS未退料，材料仍然在工具头中的时候，AMS不属于空闲状态，无法实现读取RFID、余料检测等功能。**

2. 在**打印机设置->打印机G-code->打印机起始G-code中**删除冲刷旧耗材部分的Gcode，如下图：

![](https://wiki.bambulab.com/studio-ams/开始.png)
> 关闭进料冲刷可能会导致下次打印出现堵头的情况，不建议关闭。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（工作日 9:00-21:00；节假日 9:00-18:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
