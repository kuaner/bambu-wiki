---
path: zh/p2s/maintenance/replace-th-boards-and-fpc-cable
title: "更换 P2S 工具头电路板（TH板）"
description: "介绍更换P2S 工具头上 TH 板、挤出接口板以及TH 板 FPC 线 的操作步骤。"
tags: ["th 板", "th 板 fpc 线", "挤出接口板"]
created: 2025-10-14T12:49:52.663Z
updated: 2026-01-11T13:22:36.836Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-th-boards-and-fpc-cable
---

## TH 板/挤出接口板/TH 板 FPC 线

因为更换 TH 板、挤出接口板以及 TH 板 FPC 线有较强的关联性，我们将更换它们的操作写在同一篇 Wiki 中，您可以根据实际需求来更换对应的备件。

**TH 板：**  
实现对打印机耗材挤出关联动作（如进退料、回抽、温度调节等）的电路板。  
配件包装内包含 TH 板和固定螺丝：

1. TH 板 \* 1；
2. BT2x5 螺丝 \* 4

**挤出接口板：**  
提供连接挤出机和部件冷却风扇接口的电路板。  
配件包装内包含挤出接口板和固定螺丝：

1. 挤出接口板 \* 1；
2. BT2x5 螺丝 \* 2

**TH 板 FPC 线：**  
连接 TH 板和挤出接口板的软排线。  
配件包装内仅有1根TH 板 FPC 线。  
![dlb054.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/dlb057.jpg)![dlb054.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/dlb056.jpg)![cab045.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/cab045.jpg)

## 何时更换

1. 电路板上的元器件、连接器或连接排线出现明显的损坏，并影响使用；
2. 经过交换检查或工具的测量，确认是相关配件的故障；
3. 经 Bambu Lab 技术支持确认，需更换 TH 板、挤出接口板或TH 板 FPC 线。

## 所需的工具和材料

1. 需要更换的新配件
2. H1.5 内六角扳手
3. 镊子

## 安全提示

> 重要提醒 ！
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## TH 板连接器

![22_022.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/22_022.png)

| NO. | 连接部件 |
| --- | --- |
| 1 | 热端加热组件 |
| 2 | TH 板 FPC 线 |
| 3 | 3508 挤出电机 |
| 4 | 热端风扇 |
| 5 | 涡流线圈 |
| 6 | 工具头线缆 |

## 拆除工具头电路板

### 第1步 移除工具头外壳

请参考 [更换工具头外壳](replace-toolhead-housing.md) 这篇WIKI，将工具头的外壳拆除。

![toolhead_housing_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/toolhead_housing_001.png)

### 第2步 移除 TH 板

打开 TH 板 FPC 线和挤出电机连接线的连接器，断开连接线。

|  |  |
| --- | --- |
|  |  |

依次撕下贴在 TH 板上的泡棉和胶布，然后断开热端加热组件、热端冷却风扇和涡流线圈的连接。注意，断开热端风扇和涡流线圈的连接线时，要垂直于连接器的方向拨起，请勿在连接器左右方向用力或摇晃，以免损坏连接器。

|  |  |
| --- | --- |
|  |  |

![unplug_the_hot_end_fan_and_eddy_current_coil_connector_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/unplug_the_hot_end_fan_and_eddy_current_coil_connector_005.png)

用 H1.5 内六角扳手移除四颗螺丝（BT2x5），解锁 TH 板，拨出工具头线缆，即可取下 TH 板。

|  |  |
| --- | --- |
|  |  |

### 第3步 移除挤出机接口板和 TH 板 FPC 线

打开连接霍尔开关板组件连接器的盖子，断开霍尔开关板排线的连接。

|  |  |
| --- | --- |
|  |  |

> 部分机器在连接器位置有涂布黑胶，使用镊子去除后，再打开连接器即可，重新连接时，不需要额外打胶。  
> ![21_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/21_021.png)

使用 H1.5 内六角扳手移除两颗挤出接口板固定螺丝（BT2x5），取下挤出接口板。

|  |  |
| --- | --- |
|  |  |

打开挤出接口板背面的连接器卡口，移除 TH 板 FPC 线。

|  |  |
| --- | --- |
|  |  |

## 安装工具头电路板

### 第1步 连接 TH 板 FPC 线

将 TH 板 FPC 线连接到挤出接口板背面的连接器上，扣紧盖子。

|  |  |
| --- | --- |
|  |  |

### 第2步 安装挤出接口板

将挤出接口板安装到挤出机上方的位置，使用 H1.5 内六角扳手锁入两颗固定螺丝（BT2x5）。

|  |  |
| --- | --- |
|  |  |

将霍尔开关板排线连接到挤出接口板的连接器上，扣紧盖子。

|  |  |
| --- | --- |
|  |  |

### 第3步 安装 TH 板

工具头线缆连接到 TH 板背面的接口上，然后安装到工具头背部。 注意：工具头线缆需要卡入两个线扣中间，工具头线缆的走线如红线所示。

|  |  |
| --- | --- |
|  |  |

使用 H1.5 内六角扳手拧紧四颗 TH 板固定螺丝（BT2x5）。

![th_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/th_006.png)

连接涡流线圈和热端风扇的线缆，注意对齐后再接完全压入连接器。

![_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/_016.png)

连接热端加热组件线缆，重新贴回泡棉和胶布。

|  |  |
| --- | --- |
|  |  |

![attach.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/attach.png)

分别连接挤出电机排线和 TH 板 FPC 线，扣紧盖子。

![pull_fpc.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/pull_fpc.png)

![fpcjichu.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/fpcjichu.png)

### 第4步 安装工具头外壳

参考 [更换工具头外壳](replace-toolhead-housing.md) 的内容，安装好工具头外壳。

![close_front_cover_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/close_front_cover_002.png)

## 如何验证成功

连接电源，打开打印机，执行校准操作，确认校准操作能正常通过。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
