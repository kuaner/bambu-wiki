---
path: zh/x2d/troubleshooting/noise-during-wiping
title: "X2D 打印擦拭时出现异响的解决方法"
description: "本文介绍如何解决设备打印擦拭时出现的异响。"
tags: ["x2d"]
created: 2026-04-20T08:07:16.740Z
updated: 2026-05-25T12:44:46.782Z
source: https://wiki.bambulab.com/zh/x2d/troubleshooting/noise-during-wiping
---

## 何时使用

换层或者切换打印区域时，挤出机都需要回抽一小段距离耗材并抬升一定的 Z 高度。当设备抬升 Z 高度时，可能会发出噪音。

> **固件 01.01.01.00（20260520）已新增 Z 轴电机降噪功能，升级至该版本及之后的版本后，不需要再使用本 WIKI 的方式进行降噪。**

## 所需材料

U 盘  
[z轴降噪.gcode](https://wiki.bambulab.com/x2d/z-noise-reduction-program.gcode)

> Gcode 更新时间：2026-5-7

## 操作步骤

### 下载 G-code

将上述 G-code 文件下载并导入 U 盘中，然后将 U 盘插入打印机。

![x2d-first-print-image-7.png](https://public-cdn.bblmw.com/wiki/new/x2d/manual/first-print/x2d-first-print-image-7.png)

### 打印 G-code

在屏幕首页点击打印文件。

![文件.jpg](https://wiki.bambulab.com/x2d/troubleshooting/noise-during-retraction/%E6%96%87%E4%BB%B6.jpg)

选择 USB 窗口后点击该文件。

![usb1.jpg](https://wiki.bambulab.com/x2d/troubleshooting/noise-during-retraction/usb1.jpg)

打印该文件。

![打印.jpg](https://wiki.bambulab.com/x2d/troubleshooting/noise-during-retraction/%E6%89%93%E5%8D%B0.jpg)

打印过程中设备只会控制热床上下移动，并在结束时提示“打印停止”。

### 验证

打印停止后，重新发起您所需要打印的模型任务，观察本次打印过程。

![x2d-first-print-start-print-select-model.png](https://public-cdn.bblmw.com/wiki/new/x2d/manual/first-print/x2d-first-print-start-print-select-model.png)

若打印过程中声音得到明显减弱，则问题得到解决。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
