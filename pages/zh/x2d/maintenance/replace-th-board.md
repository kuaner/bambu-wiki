---
path: zh/x2d/maintenance/replace-th-board
title: "更换 X2D 工具头电路板"
description: "本文介绍了如何更换 X2D 挤出主板（TH 板）、工具头接口板、热端加热组件接口板"
tags: []
created: 2026-04-14T13:08:30.420Z
updated: 2026-08-13T04:08:27.728Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-th-board
---

## 工具头电路板

工具头电路板指：

1. TH 板（挤出主板）：实现对打印机耗材挤出关联动作（如进退料、回抽、温度调节等）的电路板。
2. 工具头接口板：提供连接挤出机、左右进料霍尔检测板、涡流线圈及工具头前壳等部件接口的电路板；
3. 热端加热组件接口板：提供工具头前壳脱落检测、加热组件接口的电路板。

![dlb064.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/dlb064.png)![dlb066.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/dlb066.png)![dlb065.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/dlb065.png)

> TH 板上的散热片同时有黑色和银色的版本，请以实物为准，下图所示为使用银色散热片的 TH 板。  
> ![th_board_with_silver_heatsink.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/th_board_with_silver_heatsink.jpg)

## 适用打印机型号

X2D

## 何时更换

## 所需要工具和材料

1. H1.5 螺丝刀
2. 镊子

## 视频教程

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 易损提示

> 移除工具头接口板布线泡棉时，请您沿左侧向玻璃前门方向轻拉，避免因拉力过大导致左霍尔检测板连接器盖板松脱或损坏。  
> ![泡棉3.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/%E6%B3%A1%E6%A3%893.jpg)

## 移除旧的工具头电路板

### **第 1 步 - 移除工具头外壳**

请参考 [更换工具头外壳](replace-toolhead-housing.md) 来移除工具头外壳。

### **第 2 步 - 移除 TH 板（挤出主板）**

用镊子依次断开连接到 TH 板（挤出主板）上的热端加热组件接口板排线、工具头接口板排线、挤出电机排线、工具头摄像头排线、辅助热端风扇线缆、堵嘴组件排线、左热端风扇线缆。

![003_disconnect_the_th_board_cable_connection.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/003_disconnect_the_th_board_cable_connection.png)

用 H1.5 内六角扳手，依次移除固定 TH 板（挤出主板）的 4 颗螺丝，松开 TH 板。  
![004_remove_th_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/004_remove_th_board_screws.png)

拔出工具头线缆，取下 TH 板（挤出主板）。  
![005_remove_the_usb-c_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/005_remove_the_usb-c_cable.png)

### 第 3 步：移除加热组件接口加固支架

移除右切料组件侧边的螺丝，如图向右抬起拨杆。  
![010_remove_right_cutter_lever_pull_out.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/010_remove_right_cutter_lever_pull_out.png)

移除左切料组件侧边的螺丝，如图向左抬起拨杆。  
![011_remove_left_cutter_lever_pull_out.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/011_remove_left_cutter_lever_pull_out.png)

用H1.5 内六角扳手拆下热端加热接口板支架的两颗螺丝。  
![012_hotend_heating_assembly_connection_board_screrws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/012_hotend_heating_assembly_connection_board_screrws.png)

取下热端加热接口加固支架。  
![013_remove_the_bracket.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/013_remove_the_bracket.png)

### 第 4 步：移除工具头接口板

撕下布线泡棉。

![泡棉.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/%E6%B3%A1%E6%A3%89.jpg)

依次断开左涡流线圈、左霍尔检测板、右霍尔检测板、右涡流线圈的连接；

| 序号 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 接口说明 | 左涡流线圈 | 左霍尔检测板 | 右霍尔检测板 | 右涡流线圈 |

![connector.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/connector.jpg)

涡流线圈可参考下图拆装。  
![](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_right_eddy_sensor_connector_001.webp)  
![](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_eddy_sensor_connector_001.webp)

用 H1.5 内六角扳手拆下两颗螺丝，取下工具头接口板。

![connector-screw.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/connector-screw.jpg)

用镊子移除工具头接口板上的白胶，移除LOGO LED 线。  
![009_remove_white_glue.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/009_remove_white_glue.png)

### 第 5 步：移除热端加热组件接口板

从热端加热接口板断开左热端加热组件和辅助热端加热组件的连接。  
![014_remove_hotend_heating_assembly.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/014_remove_hotend_heating_assembly.png)

取下热端加热组件接口板。  
![015_remove_hotend_heating_assembly_connection_board.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/015_remove_hotend_heating_assembly_connection_board.png)

## 安装新的工具头电路板

### 第 1 步：安装热端加热接口板

将热端加热组件接口板安装到挤出机上方，请注意接口板和滑车中间不要压住任何一条线缆，避免影响后续安装。

![016_install_hotend_heating_assembly_connection_board.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/016_install_hotend_heating_assembly_connection_board.png)

分别将左热端加热组件和右辅助热端加热组件的线缆连接到热端加热组件接口板上；

![017_install_hotend_heating_assembly.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/017_install_hotend_heating_assembly.png)

### 第 2 步：安装工具头接口板

将LOGO LED线缆安装到工具头接口板上。

![020_install_extruder_connection_board_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/020_install_extruder_connection_board_cable.png)

将工具头接口板安装到工具头滑车的正上方，注意要将热端加热接口板的排线压住。

![fpc.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/fpc.jpg)

用 H1.5 内六角扳手锁入两颗螺丝。

![connector-screw.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/connector-screw.jpg)

依次将左涡流线圈、左霍尔检测板、右霍尔检测板和右涡流线圈的线缆连接到工具头接口板上。

![connector.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/connector.jpg)

### 第 3 步：安装加热组件接口板加固支架

将热端加热接口板加固支架放置到位，注意线缆要放置在左右热端加热组件的中间，并且压在支架后方。

![hotend.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/hotend.jpg)

用 H1.5 内六角扳手锁入两颗热端加热接口板支架螺丝。

![hotend-screw.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/hotend-screw.jpg)  
![hotend-screw2.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/hotend-screw2.jpg)

贴回泡棉。

![泡棉.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/%E6%B3%A1%E6%A3%89.jpg)

### 第 4 步：安装 TH 板（挤出主板）

将工具头线缆连接到 TH 板（挤出主板）的接口上，安装好工具头线缆。

![023_install_usb-c_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/023_install_usb-c_cable.png)

将 TH 板（挤出主板）对齐螺丝定位柱，用 H1.5 内六角扳手锁入四颗螺丝，将 TH 板（挤出主板）安装到工具头滑车背面。

![004_remove_th_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/004_remove_th_board_screws.png)

依次连接工具头接口板排线、热端加热组件接口板排线、挤出电机排线、工具头摄像头排线、堵嘴组件排线、左热端风扇线缆、辅助热端风扇线缆。

![003_disconnect_the_th_board_cable_connection.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/003_disconnect_the_th_board_cable_connection.png)

| 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 |
| --- | --- | --- | --- | --- | --- |
| 1 | 热端加热组件接口板 | 4 | 工具头摄像头 | 7 | 左热端风扇线缆 |
| 2 | 工具头接口板 | 5 | 辅助热端风扇线缆 |  |  |
| 3 | 挤出电机 | 6 | 堵嘴组件 |  |  |

### 第 5 步：安装切料拨杆组件

将左右切料拨杆组件复原，并锁上螺丝。

|  |  |
| --- | --- |
|  |  |

请注意切料拨杆下端的缺口需要卡住切料组件的刀柄，否则切料拨杆组件无法驱动刀柄切割耗材。  
![019_note_the_gap.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/filament_cutter_lever/019_note_the_gap.png)

### 第 6 步：安装**工具头外壳**

请参考 [更换工具头外壳](replace-toolhead-housing.md) 安装工具头外壳。

## 功能验证

连接电源，打开打印机，执行校准操作，确认校准操作能正常通过。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
