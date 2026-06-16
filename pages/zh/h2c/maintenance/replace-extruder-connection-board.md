---
path: zh/h2c/maintenance/replace-extruder-connection-board
title: "更换 H2C 挤出接口板"
description: "本文介绍了如何更换 H2C 挤出接口板"
tags: []
created: 2025-11-18T13:16:03.100Z
updated: 2026-06-08T02:44:20.053Z
source: https://wiki.bambulab.com/zh/h2c/maintenance/replace-extruder-connection-board
---

## 挤出接口板

挤出接口板安装在工具头背面，通过 FPC 排线与 TH 板连接。

**挤出接口板的配件明细如下：**

1. 挤出接口板 \* 1
2. M1.6x4 螺丝 - 用于固定挤出接口板 \* 2
3. 导热硅胶片 \* 1

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-11.png)

## 所需的工具和材料

1. 新的挤出接口板
2. H2.0 内六角扳手
3. H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除挤出接口板

### 步骤 1：移除部件冷却风扇风道和风扇

您可以参考[更换 H2D 部件冷却风扇指南](../../h2/maintenance/replace-part-cooling-fan.md)或下方视频（前1分40秒的内容）来移除部件冷却风扇风道和部件冷却风扇。

### 步骤 2：移除挤出接口板

依次拔掉接口板上的 2004 切换电机 FPC 插头（#1）、TH 板接口 FPC 插头（#2）和 2004 升降电机 FPC 插头（#3）。

![16.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/16.png)

| **序号** | **连接对象** |
| --- | --- |
| 1 | 2004 切换电机 |
| 2 | TH 板排线 |
| 3 | 感应热端加热组件电源线 |
| 4 | 2004 升降电机 |

注意：插头均被卡扣压住，需要先解锁卡扣，再拔出 FPC 线缆。

- 1号位置：

![extruder_connection_board-1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/extruder_connection_board-1.png)

- 2号位置：

![extruder_connection_board-2.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/extruder_connection_board-2.png)

- 4号位置：

![extruder_connection_board-4.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/extruder_connection_board-4.png)

依次拔掉这些插头后，使用 H1.5 内六角扳手移除两颗螺丝，解锁加热组件电源线。

|  |  |
| --- | --- |
|  |  |

移除两颗挤出接口板固定螺丝（M1.6x4）；

|  |  |
| --- | --- |
|  |  |

在挤出接口板靠近 2004 切换电机插头的地方轻微晃动，小心地取出挤出接口板。  
![remove_extruder_connection_board.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/remove_extruder_connection_board.png)

## 安装挤出接口板

### 步骤 1：安装挤出接口板

1. 将挤出接口板的插销对准 TH 板上的插槽，将挤出接口板装入 TH 板；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-58.png)

2. 用 H1.5 内六角扳手拧紧两颗固定螺丝（M1.6x4）；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-62.png)

3. 插头均由卡扣固定，将排线依次插入挤出接口板的接口中，将线缆完全插入后再扣紧卡扣。

![16.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/16.png)

| **序号** | **连接对象** |
| --- | --- |
| 1 | 2004 切换电机 |
| 2 | TH 板排线 |
| 3 | 感应热端加热组件电源线 |
| 4 | 2004 升降电机 |

### 步骤 2：安装部件冷却风扇和风道

您可以参考这篇 Wiki 中的安装步骤来安装部件冷却风扇和部件冷却风扇风道：[更换 H2C 部件冷却风扇指南](../../h2/maintenance/replace-part-cooling-fan.md)

## 如何验证成功

连接电源，打开打印机并发起打印，检查是否可以成功打印。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

**更换 H2C 挤出接口板/ TH 板/ FPC 排线所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

###### 螺丝规格：BT3x8

**用途：**用于固定部件冷却风扇风道

**螺丝数量：**4

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-14.png)
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-10.png)
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-9.png)

###### 螺丝规格：BT3x20

**用途：**用于固定部件冷却风扇

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-7.png)

###### 螺丝规格：BT2.6x8

**用途：**用于固定部件冷却风扇

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-8.png)
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-5.png)

###### 螺丝规格：M1.6x4

**用途：**用于固定挤出接口板

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-6.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
