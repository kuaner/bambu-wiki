---
path: zh/x1/maintenance/belt-tension
title: "X1/P1 系列皮带张紧"
description: "关于 P1 和 X1 系列打印机 XY 轴皮带张紧的操作"
tags: ["张紧", "p1", "x1"]
created: 2022-07-29T06:21:16.059Z
updated: 2026-05-29T09:04:34.267Z
source: https://wiki.bambulab.com/zh/x1/maintenance/belt-tension
---

## 前言

正确的皮带张紧对于 CoreXY Motion 系统至关重要。皮带松动会导致 3D 打印出现多种问题，例如将圆形打印成椭圆。

皮带和龙门架构成了质量-弹簧系统，其中皮带为弹簧（k），龙门架为质量（m）。系统的[固有频率](https://en.wikipedia.org/wiki/Natural_frequency)为 f=√(k/m)。皮带松动会降低 k 和 f，进而影响 Vibration Compensation。

X1 通过方程 f=√(k/m) 监控皮带张力。在校准过程中，Motor 会产生不同频率的振动并寻找共振；当输入频率等于固有频率时，就会发生共振。我们将这一过程称为频率扫描，随着音调升高，会产生较大的噪声。

当 X1 检测到固有频率发生变化时，会收紧皮带。这是一个半自动过程，只需进行简单操作即可完成。您只需拧松皮带张紧器上的 4 颗螺丝，前后移动 toolhead 若干次，并在最后将 toolhead 两端滑车紧贴后壁，然后再次拧紧螺丝即可。皮带张紧器中的弹簧系统会将皮带调整到正确状态，整体操作较为简单。

## 适用机型

- P1 系列
- X1 系列

## 安全提醒

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 皮带张紧

1. 操作前，请先关闭打印机电源。
2. 拧松皮带张紧器的 4 颗螺丝，但不要将其拆下。随后轻轻来回移动 toolhead 几次，最后将其移至打印机后端，再次拧紧 4 颗螺丝。皮带张紧器中的弹簧结构会将皮带张紧至正确的张紧度。
3. 请勿过度拧紧螺丝，以免滑丝。

## 碳管的清洁

请参考[碳管的清洁 | Bambu Lab Wiki](../../general/carbon-rods-clearance.md)，获取更多步骤。

## 校准

完成皮带张紧后，需要重新校准共振频率识别，以记录设备新的共振特性。

X1 系列打印机可以通过 Screen 直接进行校准操作。

![](https://wiki.bambulab.com/x1/maintenance/belt-tension/calibration-cn.jpg)

P1 系列和 X1 系列设备均可通过 Bambu Studio 进行校准。

![](https://wiki.bambulab.com/20240422-195418.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导.
