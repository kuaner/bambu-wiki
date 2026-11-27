---
path: zh/p3c/troubleshooting/p3c-h3c-nozzle-wiping-issues-loose-purge-wiper
title: "拓竹H3C / P3C 吐料组件松动导致擦嘴异常的排查指南"
description: "本指南介绍了拓竹H3C / P3C 打印机吐料组件位置偏移导致喷嘴擦拭过程异常的排查步骤。"
tags: []
created: 2026-11-26T11:48:27.026Z
updated: 2026-11-27T01:33:06.676Z
source: https://wiki.bambulab.com/zh/p3c/troubleshooting/p3c-h3c-nozzle-wiping-issues-loose-purge-wiper
---

## 故障现象

擦嘴硅胶块被热端蹭脱落，重新安装擦嘴硅胶块后，热端移动到擦嘴位置时，仍会将其蹭落或蹭歪。

|  |  |
| --- | --- |
|  |  |

## 可能的原因

吐料组件松动或位置偏移，导致热端与擦嘴硅胶块之间的间隙异常。此时需要调整吐料组件位置，并锁紧固定螺丝。

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行故障排查或维护时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 排障步骤

### 步骤 1. 安装擦嘴硅胶块

若硅胶块松动或脱落，请参考 [擦嘴块更换指南](../../h3c/maintenance/replace-nozzle-wiping-pad.md)，将擦嘴硅胶块安装到位。

![](https://wiki.bambulab.com/p3c/troubleshooting/p3c-h3c-nozzle-wiping-issues-loose-purge-wiper/install-nozzle-wiping-pad.png)

### 步骤 2. 取用打印头

若工具头未夹持打印头，请在打印机屏幕上执行取用打印头操作。

|  |  |
| --- | --- |
|  |  |

### 步骤 3. 移动工具头

在打印机屏幕上，将工具头移动至最后侧，再向右移动至 **擦嘴硅胶块左侧附近**。

|  |  |
| --- | --- |
|  | 擦嘴硅胶 |

|  |  |
| --- | --- |
|  | 移动至图示位置 |

### 步骤 4. 调整吐料组件

轻微调整吐料组件的位置，确保 1 **热端硅胶底面**与 2 **擦嘴硅胶顶面**有细小缝隙即可。

> **注意**：操作前，请确保打印机处于**空闲状态**，且热端、热床已冷却至安全温度，请勿用手触碰打印头或热床，避免烫伤。

|  |  |
| --- | --- |
|  |  |

**正确状态**：热端硅胶底面与擦嘴硅胶块顶面之间有**细小缝隙**。

|  |  |
| --- | --- |
|  |  |

**错误状态 1**：擦嘴硅胶与热端硅胶底面 **紧贴，没有缝隙**。此状态可能导致擦嘴硅胶块被热端蹭落或蹭歪。

![](https://wiki.bambulab.com/p3c/troubleshooting/p3c-h3c-nozzle-wiping-issues-loose-purge-wiper/incorrect-no-wiper-gap.png)

**错误状态 2**：擦嘴硅胶与热端硅胶底面之间的 **缝隙过大**，可能影响擦嘴硅胶块清除喷嘴残料的效果。

![](https://wiki.bambulab.com/p3c/troubleshooting/p3c-h3c-nozzle-wiping-issues-loose-purge-wiper/incorrect-large-wiper-gap.jpg)

### 步骤 5. 锁紧螺丝

请选择您的机型，参考对应的步骤。

- P3C
- H3C
