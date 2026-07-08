---
path: zh/h2/troubleshooting/calibrate-failed
title: "开机校准过程故障排查"
description: ""
tags: ["h2d"]
created: 2025-10-17T02:26:46.652Z
updated: 2026-07-02T03:02:34.783Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/calibrate-failed
---

## 故障现象

新打印机或打印机恢复出厂设置后，在开机校准过程中出现了问题，无法继续校准。

## 解决方案

### 1. 常见故障

请对照屏幕显示的**故障代码**，点击下表中**对应机型的 Wiki 链接**获取故障排查指引。

| 故障代码 | 故障提示 | 解决方案 |
| --- | --- | --- |
| 0300-4030 | Z轴回零失败，请确认热床滑块固定螺丝已取出且热床升降无异物阻挡。 | [X1](https://wiki.bambulab.com/zh/X1/troubleshooting/z-axis-homing-failure)  |  [P2S/X2D](https://wiki.bambulab.com/zh/P2S/troubleshooting/z-axis-homing-failure)  |  [H2 系列](z-axis-homing-failure.md)  |  [A2L](../../a2l/troubleshooting/hmscode/0300_1800_0001_0005.md) |
| 0300-4002 \ 0300-4038 | 热床调平失败。 | [X1](https://wiki.bambulab.com/zh/X1/troubleshooting/bed-leveling-failure)  |  [P2S/X2D](https://wiki.bambulab.com/zh/P2S/troubleshooting/bed-leveling-failure)  |  [H2 系列](bed-leveling-failure.md)  |  [A2L](../../a2l/troubleshooting/hmscode/0300_2d00_0001_0006.md) |
| 0300-4032 | XY回零失败。 | [通用指南](xy-axis-homing-failure.md) |
| 0300-4036 | 喷嘴偏移校准失败。 | [H2D\H2C](nozzle-offset-calibration-failure.md) |  [X2D](../../x2d/troubleshooting/nozzle-offset-calibration-failure.md) |
| 0300-4015 \ 0300-4037 | 喷嘴裹头位置检测失败。 | [P2S](https://wiki.bambulab.com/zh/P2S/troubleshooting/nozzle-clumping-detection) |  [X2D](../../x2d/troubleshooting/nozzle-clumping-detection.md) |
| 0300-4035 | 喷嘴清理失败。 | [P2S](https://wiki.bambulab.com/zh/P2S/troubleshooting/nozzle-cleaning-failure) |  [H2 系列](nozzle-cleaning-failure.md) |  [X2D](../../x2d/troubleshooting/nozzle-cleaning-failure.md) |
| 0500-4095 | 未检测到打印板。 | [P2S/X2D](https://wiki.bambulab.com/zh/P2S/troubleshooting/build-plate-not-detected)  |  [H2 系列](build-plate-not-detected.md)  |  [A2L](../../x1/troubleshooting/hmscode/0300_0D00_0001_0003.md) |
| 05FF-4031 \ 0300-4031 | 热端未安装，请安装后重新校准。（H2D\H2C 请检查左右热端是否未安装） | [P2S](https://wiki.bambulab.com/zh/P2S/troubleshooting/hotend-not-installed)  |  [X2D](../../x2d/troubleshooting/hotend-not-installed.md)  |  [H2S](https://wiki.bambulab.com/zh/H2S/troubleshooting/hotend-not-installed)  |  [H2D\H2C](hotend-not-installed.md)  |  [A2L](../../a2l/troubleshooting/hmscode/0300_0200_0001_0009.md) |
| 0300-4039 | 喷嘴在位检测失败。 | [H2 系列](nozzle-detection-failed.md)  |  [P2S](../../p2s/troubleshooting/hmscode/0300_1800_0001_000B.md)  |  [X2D](https://wiki.bambulab.com/zh/x2d/troubleshooting/hmscode/0300_1800_0001_000B ) |

请参考以上列出的排查故障指引，在问题解决后请在屏幕上点击**重新校准。**

![1.png](https://wiki.bambulab.com/h2c/1.png)

### 2. 非常见故障

若上表无对应 HMS 链接，请点击打印机屏幕右上角 **“跳过”** 开机校准，进入主页点击 **“[助手](../../x1/troubleshooting/how-to-enter-the-specific-code-page.md)”** 查看 HMS 信息，然后在 [HMS 主页面](../../hms/home.md) 查询具体的 HMS 代码并进行故障排除。

![20251223-151435.jpg](https://wiki.bambulab.com/h2c/troubleshoting/unclogging/20251223-151435.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
