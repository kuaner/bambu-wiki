---
path: zh/ams/maintenance/ams-bearing-support-for-internal-hub-unit
title: "AMS 五通轴承支撑座更换指南"
description: "本文将详细为您介绍 AMS 更换五通轴承支撑的详细步骤和注意事项。"
tags: ["ams"]
created: 2025-12-16T06:46:13.112Z
updated: 2026-05-09T09:05:46.665Z
source: https://wiki.bambulab.com/zh/ams/maintenance/ams-bearing-support-for-internal-hub-unit
---

## 五通轴承支撑座

AMS 五通轴承支撑座，顾名思义，用于支撑 AMS 内部的五通轴承。上下料组件将耗材送往 AMS 五通后，五通轴承会进一步将耗材送出 AMS。长时间使用造成的磨损可能导致 AMS 五通轴承支撑座损坏，进而影响 AMS 进退料功能，使其无法正常工作。

![ams-bearing-support-for-internal-hub-unit_cover_zh.jpg](https://wiki.bambulab.com/ams/maintenance/ams-bearing-support-for-internal-hub-unit/ams-bearing-support-for-internal-hub-unit_cover_zh.jpg)

## 适用打印机型号

AMS

## 何时更换

将耗材插入 AMS 上下料组件，上下料组件正常工作将耗材送入五通后，出现电机空转的现象，且该现象发生在四个槽位，此时需要拆开 AMS 检查 AMS 五通轴承支撑座是否损坏。如若发现断裂，则需要更换。

## 所需要工具和材料

- 新的 AMS 五通轴承支撑座
- H2.0 和 H1.5 内六角扳手
- 平头镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除旧的五通轴承支撑座

### 1.取下 AMS 上的 PTFE 管

关闭打印机，断开 AMS 与打印机的连接线。打开 AMS 上盖，按压 AMS 五通组件上用于释放 PTFE 管的按钮，从 AMS 背后拉出 PTFE 管。

|  |  |
| --- | --- |
|  |  |

### 2. 移除螺丝

使用 H2.0 内六角扳手，移除固定 AMS 主框架上 2 颗螺丝。

  
![](https://wiki.bambulab.com/ams/maintenance/ams-bearing-support-for-internal-hub-unit/remove_two_screws.jpg)

### 3. 移除 AMS 主框架组件

小心地抬起 AMS 主框架组件（远离上下料组件一侧），断开 485 总线线缆和电源连接线，移除 AMS 主框架组件。

> **注意：** AMS 电源连接线接口处有卡扣，按压卡扣解锁后即可断开连接。

|  |  |
| --- | --- |
|  |  |

### 4. 断开连接 AMS 五通组件的 PTFE 管

依次按下 AMS 五通上 4 个气动接头的黑色按钮，解锁并断开 4 条 PTFE 料管。

|  |  |
| --- | --- |
|  |  |

### 5. 移除 AMS 五通组件 4 颗固定螺丝

整理 PTFE 料管及两条线缆，使其置于另一侧，方便后续操作。使用 H2.0 内六角扳手，移除 AMS 五通组件 4 颗固定螺丝。

|  |  |
| --- | --- |
|  |  |

### 6. 移除 AMS 五通轴承支撑座 4 颗固定螺丝

将 AMS 五通组件小心翻转过来，以免损坏线缆。使用 H1.5 内六角扳手，拧下 AMS 五通轴承支撑座 4 颗固定螺丝，取下 AMS 五通轴承支撑座。

|  |  |
| --- | --- |
|  |  |

## 安装新的五通轴承支撑座

### 1. 安装 AMS 五通轴承支撑座 4 颗固定螺丝

使用 H1.5 内六角扳手，安装 AMS 五通轴承支撑座 4 颗固定螺丝。翻转并重新安装 AMS 五通组件。

|  |  |
| --- | --- |
|  |  |

### 2. 安装 AMS 五通组件 4 颗固定螺丝

使用 H2.0 内六角扳手，重新安装 AMS 五通组件 4 颗固定螺丝。

  
![](https://wiki.bambulab.com/ams/maintenance/ams-bearing-support-for-internal-hub-unit/4_screws_on_internal_hub.jpg)

### 3. 重新插入 AMS 五通组件的 PTFE 管

依次将 4 条 PTFE 料管插入 AMS 五通上的 4 个气动接头。

|  |  |
| --- | --- |
|  |  |

### 4. 安装 485 总线线缆和电源连接线

连接 485 总线线缆和电源连接线，注意插口方向。

|  |  |
| --- | --- |
|  |  |

### 5. 安装 AMS 主框架及其固定螺丝

重新安装 AMS 主框架组件，安装时，先放置上下料组件一侧；安装另一侧时，可以轻微向外推动边框，防止 AMS 五通组件按钮卡住。然后，使用 H2.0 内六角扳手，安装固定 AMS 主框架上 2 颗螺丝。

|  |  |
| --- | --- |
|  |  |

### 6. 安装 AMS 上的 PTFE 管及 6-pin 线缆

检查确认 PTFE 管硅胶支架与五通组件的料孔对齐，并从 AMS 后部推入 PTFE 管。装完后，拉动 PTFE 管，确认 PTFE 管已固定。然后重新连接 6-pin 线缆。

|  |  |
| --- | --- |
|  |  |

## 功能验证

将 AMS 连接到打印机并打开电源。将耗材加载到 AMS 的所有料槽中，然后单击屏幕上的**进料**。

![screen_1.jpg](https://wiki.bambulab.com/ams/maintenance/ams-bearing-support-for-internal-hub-unit/screen_1.jpg)

1号料槽进完料后，点出2号料槽图标加载2号料槽的耗材，以此类推，直至4个料槽都完成一次进料、退料的操作。

![screen_2.jpg](https://wiki.bambulab.com/ams/maintenance/ams-bearing-support-for-internal-hub-unit/screen_2.jpg)

如果所有进退料过程都表现正常，则更换完成。  
否则，检查所有电缆和 PTFE 管的连接后重试。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
