---
path: zh/p2s/maintenance/replace-mc-and-ac-boards
title: "更换 P2S AC/MC 板"
description: ""
tags: []
created: 2025-10-14T12:50:31.109Z
updated: 2026-04-20T13:03:51.704Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-mc-and-ac-boards
---

## MC 板

MC板的全称是 Main Control Board，中文通常称为 “主控板” ，它是一块集成了微处理器、各种驱动芯片、接口和电路的印刷电路板。

- **配件包装内包含：**

1. MC 板 \* 1；
2. BT2x5 螺丝 \* 3 - 用于固定 MC 板；
3. M2x5 螺丝 \* 2 - 用于固定散热片到 MC 板。

- **连接器介绍：**

![mc_board_connectors_027.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/mc_board_connectors_028.png)

> 产品信息更新：如下图所示为新款的 MC 板散热片，两种散热片均能满足散热需求。  
> ![heat_sink.jpg](https://wiki.bambulab.com/p2s/maintenance/mc-board/heat_sink.jpg)

## AC 板

AC 板是用于给打印机的热床提供交流电源并实现输出控制的电路板。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/dlb054.jpg)  
**配件包装内包含：**

1. AC 板 \* 1；
2. BT2x5 螺丝 \* 3- 用于固定 AC 板。

## 何时更换

1. MC 板或 AC 板出现明显的损坏；
2. 经 Bambu Lab 官方技术支持确认需更换 MC 板或 AC 板。

> 注意：更换 AC 板前，需先拆卸 MC 板。本指引涵盖了两个配件的完整更换流程，请根据您的实际需求参阅相关部分。

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 MC/AC 板

### 步骤 1：移除料管支架、缓冲器和背板

您可以参考如下 Wiki 的拆解部份内容，依次移除料管支架、缓冲器和背板。

- [更换料管支架](replace-ptfe-tube-bracket.md)
- [更换缓冲器](replace-filament-buffer.md)
- [更换背板](replace-rear-panel.md)

![rear_panel_removed_025.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/rear_panel_removed_025.png)

### 步骤 2：移除废料滑梯

使用 H1.5 内六角扳手移除四颗固定螺丝（BT2x5），然后将废料滑梯取下。  
![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 3：移除 MC 板散热片

> 如果最终的目的是更换 AC 板，侧不需要移除散热片在 MC 板的固定螺丝。

使用 H1.5 内六角扳手移除两颗散热片固定螺丝（红色圆圈标记：M2x5）；  
使用 H2.0 内六角扳手移除两颗散热片固定螺丝（绿色方框标记：ST3x6）。

![01_heatsink_screw_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/01_heatsink_screw_001.png)

用手扶住将散热片从打印机上取下，在取下散热片时注意避让线缆，避免散热片上的导热硅脂沾到线缆上。

![02_remove_the_heatsink_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/02_remove_the_heatsink_002.png)

![03_remove_the_heatsink_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/03_remove_the_heatsink_003.png)

![04_remove_the_heatsink_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/04_remove_the_heatsink_004.png)

### 步骤 4：移除 MC 板

依次断开 MC 板上的连接线，一共需要移除 11 根线缆。

![06_mc_board_interface_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/06_mc_board_interface_006.png)

> ⚠️ 注意事项
>
> 在操作时，请务必**使用镊子清除线缆接口周围的硅胶**（如下图所示的 1-4 号接口），以免硅胶影响卡扣的正常释放。
>
> 在拔出带有卡扣的接头（如下图所示的 4 号接口）之前，务必**确保已完全按住接口卡扣**，避免在卡扣未释放的情况下强行拔插。
>
> ![Remove Glue](https://wiki.bambulab.com/p2s/maintenance/replace-mc-and-ac-boards/05_remove_the_white_glue_005_add.png)

使用 H1.5 内六角扳手移除 3 颗 MC 板固定螺丝（BT2x5），将 MC 板从打印机内衬上取下。  
![22_mc_board_screw_022.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/22_mc_board_screw_022.png)  
由于从 MC 板 - AC 板的连接线比较靠近立柱内侧，如果在之前的操作里，没有断开 MC-AC 的连接线，可以在此时断开。

![23_remove_the_mc-ac_cable_from_the_mc_board_023.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/23_remove_the_mc-ac_cable_from_the_mc_board_023.png)

> **以下是移除AC 板的内容。**

### 步骤 5：移除电源保护盖

用按住热床供电线线缆接头的卡扣，将供电线从 AC 板上依次断开。  
（从左往右依次将红色、蓝色、灰色线缆。）

![12_heated_bed_power_cable_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/12_heated_bed_power_cable_012.png)  
使用 H1.5 内六角扳手依次移除电源保护盖的五颗固定螺丝（BT2x5），然后将电源保护盖从打印机上取下。

![13_ac_board_cover_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/13_ac_board_cover_013.png)

![15_remove_the_ac_board_cover_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/15_remove_the_ac_board_cover_015.png)

### 步骤 6：移除 AC 板

打开电源线盖，使用十字螺丝刀拧松接口处的螺丝，然后将三根电源线从接口中抽出。

正确接法:

- 红色:火线
- 蓝色:零线
- 黄绿:地线

正确接法下AC板控制火线通断，接反零火线时，AC板控制零线，热床火线常通，漏电电流偏高。  
极端情况:如果热床压变形了，热管破损导致火线和热床铝壳接触在一起，火线和地线就会导通，烧毁保险和供电线路。

![lng-cable-en.jpeg](https://wiki.bambulab.com/p2s/maintenance/replace-mc-and-ac-boards/ac_power_supply_cable.jpg)

使用 H1.5 内六角扳手移除三颗 AC 板固定螺丝（BT2x5），然后将 AC 板从打印机上取下，移除 MC-AC 连接线。

![19_ac_board_screw_019.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/19_ac_board_screw_019.png)  
![20_remove_the_mc-ac_cable_from_the_ac_board_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/20_remove_the_mc-ac_cable_from_the_ac_board_020.png)

## 安装 MC/AC 板

### 步骤 1：安装 AC 板

将 MC-AC 连接线接到 AC 板连接器上，将 AC 板底部的凹槽与打印机上的方柱对齐后装入，用 H1.5 内六角扳手拧紧三颗固定螺丝（BT2x5）。

![20_remove_the_mc-ac_cable_from_the_ac_board_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/20_remove_the_mc-ac_cable_from_the_ac_board_020.png)  
![21_install_the_ac_board_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/21_install_the_ac_board_021.png)  
![19_ac_board_screw_019.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/19_ac_board_screw_019.png)

依次将三根电源线（从上往下依次为：棕色、蓝色、黄色）插入接口中，然后使用十字螺丝刀拧紧螺丝并扣上盖子

![lng-cable-en.jpeg](https://wiki.bambulab.com/p2s/maintenance/replace-mc-and-ac-boards/ac_power_supply_cable.jpg)

### 步骤 2：安装 电源保护盖

根据螺丝孔位置，将电源保护盖安装到位，用 H1.5 内六角扳手拧紧 5 颗电源保护盖固定螺丝（BT2x5）。

![14_remove_the_ac_board_cover_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/14_remove_the_ac_board_cover_014.png)

![13_ac_board_cover_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/13_ac_board_cover_013.png)

依次将三根热床供电线插入接口，从左往右依次为：红色、蓝色、灰色

![12_heated_bed_power_cable_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/12_heated_bed_power_cable_012.png)

### 步骤 3：安装 MC 板

将新的蓝色绝缘导热硅脂涂抹在 MC 板的芯片上（如下图），确保每个芯片顶部都有足够的导热硅脂，并连接右下角 MC-AC 线缆

![23_remove_the_mc-ac_cable_from_the_mc_board_023.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/23_remove_the_mc-ac_cable_from_the_mc_board_023.png)

再将 MC 板的右侧与打印机内衬上的槽位对准，然后将 MC 板安装到位。

![24_install_the_mc_board_024.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/24_install_the_mc_board_024.png)

使用 H1.5 内六角扳手拧紧 3 颗 MC 板固定螺丝（BT2x5）。

![22_mc_board_screw_022.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/22_mc_board_screw_022.png)

重新将线缆连接到 MC 板的连接器上。

![06_mc_board_interface_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/06_mc_board_interface_006.png)

| 编号 | 名称 | 编号 | 名称 | 编号 | 名称 |
| --- | --- | --- | --- | --- | --- |
| 1 | 自适应风道切换组件 | 5 | 热床温度线 | 9 | MC 板供电 |
| 2 | MC-AP 线（供电） | 6 | XY 电机（A） | 10 | 工具头线缆 |
| 3 | MC-AP 线（通信） | 7 | XY 电机（B） | 11 | Z 电机 |
| 4 | 缓冲器连接线 | 8 | MC-AC 线 |  |  |

### 步骤 4：安装 MC 板散热片

将靠近打印机立柱的电机线（电机 B）往外先拨开，然后将 MC 板散热片斜着装入，请检查确认没有线缆被压在散热片底部。

![07_install_the_heatsink_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/07_install_the_heatsink_007.png)  
![08_install_the_heatsink_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/08_install_the_heatsink_008.png)

先使用 H1.5 内六角扳手拧入两颗螺丝（M2x5，拧入螺丝前请先检查垫片是否在螺丝上）将 MC 板散热片固定，此时不需要将螺丝完全拧紧，便于后续调整；  
![09_tighten_the_heatsink_screws_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/09_tighten_the_heatsink_screws_009.png)  
![10_tighten_the_heatsink_screws_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/10_tighten_the_heatsink_screws_010.png)

然后使用 H2.0 内六角扳手拧紧两颗螺丝（ST3x6）。  
如果位置有偏差，可以调整 MC 板散热片的位置来将螺丝孔位对准。拧紧这两颗螺丝后，需要再再使用 H1.5 内六角板 MC 板处的另外两颗螺丝完全拧紧。

![2_screws_for_heatsink_029.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/2_screws_for_heatsink_029.png)

### 步骤 5：安装废料滑梯

将废料滑梯对准打印机上的螺丝孔位，使用 H1.5 内六角扳手拧紧四颗固定螺丝（BT2x5）。  
![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 6：安装背板

您可以参考如下 Wiki 的安装部份内容，依次安装背板、缓冲器和料管支架。  
[更换背板](replace-rear-panel.md)  
[更换缓冲器](replace-filament-buffer.md)  
[更换料管支架](replace-ptfe-tube-bracket.md)

## 如何验证成功

连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆连接是否正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
