---
path: zh/p1/maintenance/pcb-boards-on-toolhead
title: "更换 P1 系列工具头电路板"
description: "本文介绍了 P1P 和 P1S 拆装工具头电路板的教程，包括挤出主板（即 TH 板）、挤出接口板，以及连接两者的挤出连接线（FPC 排线）。"
tags: ["p1p", "p1s"]
created: 2022-12-04T14:11:39.350Z
updated: 2026-05-26T07:47:24.812Z
source: https://wiki.bambulab.com/zh/p1/maintenance/pcb-boards-on-toolhead
---

## 工具头电路板

工具头电路板由三部分组成：挤出主板（即 TH 板）、挤出接口板，以及连接两者的挤出连接线（FPC 排线）。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/pcbas_on_th.jpg)

从左到右，依次是挤出主板、连接线和挤出接口板。

## 阅读指引

本文针对以下三种情况提供独立的操作流程，所需拆解范围与操作步骤各不相同。**请根据待更换的部件，跳转到对应章节执行操作，请勿按全文顺序操作，以避免不必要的过度拆解**。

| 适用情况 | 跳转章节 |
| --- | --- |
| 仅更换**挤出主板** | [快速定位](#%E6%9B%B4%E6%8D%A2%E6%8C%A4%E5%87%BA%E4%B8%BB%E6%9D%BF) |
| 仅更换**挤出接口板** | [快速定位](#%E6%9B%B4%E6%8D%A2%E6%8C%A4%E5%87%BA%E6%8E%A5%E5%8F%A3%E6%9D%BF) |
| 同时**更换挤出主板与挤出接口板** / 插拔 FPC 排线两端 | [快速定位](#%E5%90%8C%E6%97%B6%E6%9B%B4%E6%8D%A2%E6%8C%A4%E5%87%BA%E4%B8%BB%E6%9D%BF%E4%B8%8E%E6%8C%A4%E5%87%BA%E6%8E%A5%E5%8F%A3%E6%9D%BF) |

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作。如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 所需工具和材料

- 新的工具头电路板
- H1.5 内六角扳手

## 更换挤出主板

### 移除挤出主板

#### 步骤 1. 准备工作

- 已完成退料
- 关闭打印机电源并断开电源连接

#### 步骤 2. 移除工具头后盖

使用 H1.5 内六角扳手移除工具头后盖的 4 颗螺丝：

|  |  |
| --- | --- |
|  |  |

移除工具头后盖。

![](https://wiki.bambulab.com/p1/maintenance/toolhead-enclosure/remove_the_rear_cover.jpg)

#### 步骤 3. 断开 FPC 排线（挤出主板侧）

断开 FPC 排线在挤出主板上的连接。

![fpc_on_th_board.png](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/fpc_on_th_board.png)

#### 步骤 4. 移除挤出主板螺丝

断开挤出电机连接线，再用 H1.5 内六角扳手拧下 3 颗螺丝。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/3_screws_on_th_main_board.jpg)

#### 步骤 5. 取下挤出主板

翻转挤出主板，在其另一面断开工具头连接线，然后即可取下挤出主板。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/mc_cable_connector.jpg)

### 安装挤出主板

#### 步骤 1. 连接工具头连接线

将工具头连接线连接到新的挤出主板上。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/mc_cable_connector.jpg)

> ⚠️ **注意：**
>
> **1. 连接器方向**：请确保插座没有浮起、错误插入或插反（引线方向应朝上）。安装错误可能导致 HMS 报错。
>
> |  |  |
> | --- | --- |
> | ❌ 错误 | ✅ 正确 |
>
> **2. 插头方向**：可通过对比工具头线缆座上的文字方向与主板上的文字方向是否一致来确认。**如果该插头插反，可能会导致打印机电源短路**。
>
> |  |  |
> | --- | --- |
> | ❌ 错误 | ✅ 正确 |

#### 步骤 2. 固定挤出主板

将挤出主板的电机接口朝外，安装到滑车后盖上，锁入 3 颗螺丝，连接挤出电机连接线。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/3_screws_on_th_main_board.jpg)

#### 步骤 3. 重新连接 FPC 排线

将 FPC 排线连接回挤出主板对应的接口，并检查排线是否已正确卡紧。

![fpc_on_th_board.png](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/fpc_on_th_board.png)

> 按下图确认 FPC 排线已正确卡紧：
>
> ![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/connectors_on_interface_board_cn.jpg)

#### 步骤 4. 装回工具头后盖

将工具头后盖安装到工具头上，注意上方卡扣对齐。

![](https://wiki.bambulab.com/p1/maintenance/toolhead-enclosure/mount_the_rear_cover.jpg)

装入固定后盖的4颗螺丝。

|  |  |
| --- | --- |
|  |  |

#### 步骤 5. 验证完成

参见[如何验证完成](#%E5%A6%82%E4%BD%95%E9%AA%8C%E8%AF%81%E5%AE%8C%E6%88%90)。

## 更换挤出接口板

### 移除挤出接口板

#### 步骤 1. 准备工作

- 已完成退料
- 关闭打印机电源并断开电源连接

#### 步骤 2. 移除工具头前壳

打开工具头前壳组件。

![](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/toolhead_cover_removal.jpg)

#### 步骤 3. 断开 3 个连接器

断开接口板上的 3 个连接器：霍尔开关板、热端风扇、热端加热器。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/%E6%96%AD%E5%BC%803%E4%B8%AA%E6%8E%A5%E5%8F%A3.jpg)

#### 步骤 4. 取下挤出接口板

断开 FPC 排线，再用 H1.5 内六角扳手拧下 2 颗螺丝，将接口板从滑车前盖上取下。

![fpc_and_screws_on_extruder_connection_board.png](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/fpc_and_screws_on_extruder_connection_board.png)

### 安装挤出接口板

#### 步骤 1. 固定挤出接口板

将新接口板放回滑车前盖位置，用 H1.5 内六角扳手锁入 2 颗螺丝固定。再将 FPC 排线的接口端对准新接口板上的接口，按压到位卡紧。

![fpc_and_screws_on_extruder_connection_board.png](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/fpc_and_screws_on_extruder_connection_board.png)

> 按下图确认 FPC 排线已正确卡紧：
>
> ![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/connectors_on_interface_board_cn.jpg)

#### 步骤 2. 连接 3 个连接器

依次连接热端风扇、热端加热器、霍尔开关板的连接线。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/%E6%96%AD%E5%BC%803%E4%B8%AA%E6%8E%A5%E5%8F%A3.jpg)

#### 步骤 3. 装回工具头前壳

![](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/toolhead_cover_removal.jpg)

#### 步骤 4. 验证完成

参见[如何验证完成](#%E5%A6%82%E4%BD%95%E9%AA%8C%E8%AF%81%E5%AE%8C%E6%88%90)。

## 更换挤出主板与接口板

### 移除挤出主板与挤出接口板

#### 步骤 1. 准备工作

- 已完成退料
- 关闭打印机电源并断开电源连接

#### 步骤 2. 移除工具头外壳

参考[工具头外壳](toolhead-housing.md)的内容，拆除完整工具头外壳。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/shell_removed.jpg)

#### 步骤 3. 移除 FPC 排线

断开 FPC 排线两端的连接，移除排线。

|  |  |
| --- | --- |
|  |  |

#### 步骤 4. 移除挤出接口板

断开 3 个连接器（霍尔开关板、热端风扇、热端加热器），用 H1.5 内六角扳手拧下 2 颗螺丝，取下接口板。

|  |  |
| --- | --- |
|  |  |

#### 步骤 5. 移除挤出主板螺丝

断开挤出电机连接线，再用 H1.5 内六角扳手拧下 3 颗螺丝。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/3_screws_on_th_main_board.jpg)

#### 步骤 6. 取下挤出主板

翻转挤出主板，在挤出主板的另一面断开工具头连接线，取下挤出主板。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/mc_cable_connector.jpg)

### 安装挤出主板与挤出接口板

#### 步骤 1. 安装挤出主板

连接工具头连接线，然后将电机接口朝外，把挤出主板安装到滑车后盖上。

|  |  |
| --- | --- |
|  |  |

> ⚠️ **注意：**
>
> **1. 连接器方向**：请确保插座没有浮起、错误插入或插反（引线方向应朝上）。安装错误可能导致 HMS 报错。
>
> |  |  |
> | --- | --- |
> | ❌ 错误 | ✅ 正确 |
>
> **2. 插头方向**：可通过对比工具头线缆座上的文字方向与主板上的文字方向是否一致来确认。**如果该插头插反，可能会导致打印机电源短路**。
>
> |  |  |
> | --- | --- |
> | ❌ 错误 | ✅ 正确 |

#### 步骤 2. 固定挤出主板

锁入 3 颗螺丝，连接挤出电机连接线。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/3_screws_on_th_main_board.jpg)

#### 步骤 3. 安装挤出接口板

将挤出接口板安装到滑车前盖上，锁入 2 颗螺丝固定，依次连接热端风扇、加热器、霍尔开关板。

|  |  |
| --- | --- |
|  |  |

#### 步骤 4. 安装 FPC 排线

将 FPC 排线安装到滑车上方的线槽内，两端分别连接到接口板和挤出主板对应的接口上。

|  |  |
| --- | --- |
|  |  |

> 请按下图检查 FPC 排线是否正确插好：
>
> ![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/connectors_on_interface_board_cn.jpg)

#### 步骤 5. 装回工具头外壳

参考[工具头外壳](toolhead-housing.md)的内容，装回完整工具头外壳。

![](https://wiki.bambulab.com/p1/maintenance/toolhead-enclosure/front_cover_installed.jpg)

#### 步骤 6. 验证完成

参见[如何验证完成](#%E5%A6%82%E4%BD%95%E9%AA%8C%E8%AF%81%E5%AE%8C%E6%88%90)。

## 如何验证完成

1. 目视检查外观，接合位置无错位、无浮起；
2. 启动打印机，运行设备校准流程，如果校准过程顺利通过，说明操作成功。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/calibration2.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。
>
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。
>
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
