---
path: zh/h2d/troubleshooting/emergency_stop_button
title: "急停按键故障排查指南"
description: "本指南介绍了 H2 系列打印机急停按键故障的排除方法"
tags: ["h2"]
created: 2025-12-09T04:15:57.918Z
updated: 2026-05-09T09:52:25.574Z
source: https://wiki.bambulab.com/zh/h2d/troubleshooting/emergency_stop_button
---

## 何时使用？

在使用激光功能时，为确保符合相关安全规范，H2 系列打印机配备了一个安全钥匙插孔和一个急停按键。急停按键可以确保用户安全使用 H2 系列打印机的激光功能。

- 在激光模式下，打印机必须正确安装急停按键（带有安全钥匙）才能启用电源并发起激光任务；
- 在 3D 打印模式下，急停按键可替代安全钥匙的功能，直接导通打印机的供电回路；
- 急停按键还可以供用户在发生紧急情况时快速断开电源。

因此，急停按键正常工作十分重要，本指南将介绍了 H2 系列打印机急停按键故障情况及排除方法。

|  |  |
| --- | --- |
| 安全钥匙插孔 | 急停按键 |

该 Wiki 仅适用于 H2 系列打印机使用激光模组并且安装急停按键时使用，并用于以下情况：

1. 打印机正常启动，HMS 助手提示急停按键相关报错信息时；
2. 打印机无法正常启动。

|  |  |
| --- | --- |
| 屏幕不能亮.jpg   屏幕不亮 | 电源板灯不亮.png   铁壳电源指示灯未亮 |

## 排查须知

### 指示灯状态

正式排查前首先需要观察打印机各部位指示灯状态。通过观察打印机状态指示灯的颜色变化与闪烁方式，用户可以快速识别打印机当前所处的工作状态，如空闲、准备、执行任务或报错等。状态指示灯作为打印机的“视觉语言”，能够在无需查看屏幕的情况下，提供直观的状态反馈。

- 开关插座指示灯正常状态：常亮

![开关灯.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E5%BC%80%E5%85%B3%E7%81%AF.png)

- 铁壳电源指示灯正常状态：常亮

![电源板灯.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E7%94%B5%E6%BA%90%E6%9D%BF%E7%81%AF.png)

- 热床下方打印机状态指示灯正常状态：UI上打开指示灯后，常亮或闪烁

![闲置.webp](https://wiki.bambulab.com/h2/manual/status-indicator-light-meanings/%E9%97%B2%E7%BD%AE.webp)

- AP 板指示灯正常状态：左侧灯快速闪烁、右侧灯常亮

![board-location.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/board-location.png)  
<https://public-cdn.bblmw.com/wiki/H2D/AP-1.mp4>

### 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行故障排查或维护时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 所需工具和材料

- H 2.0内六角螺丝刀
- 十字螺丝刀
- 镊子

**请确保在使用这些工具时采取适当的安全措施，并遵循以下操作建议：**

- 在进行任何插头拔插之前，请确保打印机已经断开电源，并且电源线已拔出插座。
- 请使用正确尺寸的内六角扳手和十字螺丝刀进行拆卸和安装操作，以避免损坏螺丝或工具。
- 使用镊子时，请小心操作，避免损坏或弯曲零件。

## 现象一：打印机正常启动。HMS 助手提示急停按键相关报错信息。

HMS 助手提示急停按键报错，如：

- HMS\_0500-0400-0001-0051: 急停按钮未正确安装，请按照Wiki正确安装；
- HMS\_0500-0400-0001-0052: 未插入安全钥匙，请按照Wiki正确安装。

### 排查建议

![emergency_stop_button_3.png](https://wiki.bambulab.com/h2/troubleshooting/emergency_stop_button/emergency_stop_button_3.png)

### 故障原因与解决方案

#### 1.急停按键和安全钥匙没有正确安装；

请参考这篇 Wiki 重新安装：[HMS\_0500-0400-0001-0051: 急停按钮未正确安装，请按照Wiki正确安装。](../../h2/troubleshooting/hmscode/0500_0400_0001_0051.md)

#### 2.急停按键磁铁脱落；

该磁铁用于触发霍尔传感器的信号检测，若脱落将导致系统无法正确识别急停按键状态，从而引发误报警。  
建议重新固定磁铁或更换急停按键以确保功能正常。

![emergency_stop_button_magnet_position.jpg](https://wiki.bambulab.com/h2/troubleshooting/emergency_stop_button/emergency_stop_button_magnet_position.jpg)

#### 3.急停按键检测霍尔板线缆接触不良；

步骤一：关闭打印机并断开电源；

步骤二：向右放倒打印机；

霍尔板位于打印机底部，建议向右放到打印机，即可以找到这两个霍尔板。

> 由于打印机较重，建议两个人一起慢慢放倒打印机，避免在操作过程中受伤或对打印机造成损坏。

步骤三：重新插拔霍尔板线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-hall-effect-sensor/img_v3_02k2_cf2ae2b8-2598-4946-b699-54857122c8ag-1.jpg)

#### 4. 急停按键检测霍尔板故障。

若插拔连接线后，报错信息没有消失，请更换急停按键检测霍尔板。  
请上述方法没有解决，提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)，联系拓竹技术支持团队。

## 现象二：打印机无法启动。

安全钥匙与急停按键安装在铁壳电源的输入端，用于控制铁壳电源是否接入交流电（AC）。

如果安全钥匙或急停按键的插头未正确插入、出现松动、或急停按钮被误按下，或安全钥匙组件链路异常（前三种情况较为常见，后一种情况极为少见），都会导致铁壳电源模组无法获得 AC 交流电输入，从而无法输出 24V 直流电压。

![铁壳电源电路图中文.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E9%93%81%E5%A3%B3%E7%94%B5%E6%BA%90%E7%94%B5%E8%B7%AF%E5%9B%BE%E4%B8%AD%E6%96%87.png)

### 故障原因与解决方案

#### 1. 急停按键被按下后无法复位.

正常情况下，急停按键被按下后可以通过稍用力将其顺时针旋转以解锁急停按键。如果急停按键无法解锁复位，说明其损坏，请更换急停按键。

![急停按键.webp](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E6%80%A5%E5%81%9C%E6%8C%89%E9%94%AE.webp)

#### 2. 若急停按键可以正常工作。

请参考这篇 Wiki 继续完成排障：[H2 系列打印机上电异常排查指南-上篇](../../h2/troubleshooting/failure-to-power-on-part1.md)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
