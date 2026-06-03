---
path: zh/x2d/maintenance/replace-eddy-sensor
title: "更换 X2D 涡流线圈"
description: "本文介绍了如何更换 X2D 涡流线圈。"
tags: ["x2d"]
created: 2026-04-14T13:08:04.429Z
updated: 2026-04-24T02:56:43.904Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-eddy-sensor
---

## 涡流线圈

涡流线圈安装在热端与挤出机之间，是用于对耗材的流量进行主动校准的配件。  
X2D 有左、右 2 个涡流线圈，分别位于左热端和右辅助热端上方。  
左涡流线圈配件包装内包含：

1. 左涡流线圈
2. 螺丝 \* 2  
   ![fac205.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/fac205.png)

右涡流线圈配件包装内包含：

1. 右涡流线圈
2. 螺丝 \* 2  
   ![fac206.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/fac206.png)

## 何时更换

- 涡流线圈物理损坏；
- Z轴回零、热床调平失败，经分析为涡流线圈故障。

## 所需要工具和材料

1. 新的涡流线圈
2. H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 视频教程

## 移除涡流线圈

### 步骤 1：移除工具头外壳

请参考[更换 X2D 工具头外壳](replace-toolhead-housing.md)，移除工具头的外壳。  
![replace_toolhead_cover_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/replace_toolhead_cover_001.png)

### 步骤 2：移除热端

请参考[更换热端和硅胶套](replace-hotend-and-silicone-sock.md)，移除热端和热端硅胶套。  
![hotend_removed.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/hotend_removed.jpg)

### 步骤 3：移除左涡流线圈

1. 使用 H1.5 内六角扳手移除左切料拨杆螺丝 1 颗，使切料拨杆与切料组件分离。  
   ![replace_left_filament_cutter_lever_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/replace_left_filament_cutter_lever_001.png)
2. 使用 H2.0和H1.5 内六角扳手分别移除 2 颗固定左热端风扇的固定螺丝，用H1.5 内六角扳手移除左涡流线圈支架的 2颗螺丝，将风扇和涡流线圈从工具头滑车前盖上松开。  
   ![remove_4_screws.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_4_screws.jpg)  
   ![loose_the_parts.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/loose_the_parts.jpg)
3. 撕开工具头接口板上的泡棉，断开左涡流线圈连接器（垂直于连接器方向拔起）。

|  |  |
| --- | --- |
| 撕开泡棉 | 断开连接器 |

4. 将涡流线圈的线缆从热端加热组件接口板的支架和两个卡扣中松出，取下左涡流线圈。

![loose_left_cable.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/loose_left_cable.jpg)

### 步骤 4：移除右涡流线圈

1. 使用 H2.0 内六角扳手移除 2 颗螺丝，取下金属压片支架。  
   ![remove_the_press_plate.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_the_press_plate.jpg)
2. 使用 H1.5 内六角扳手移除右切料拨杆螺丝 1 颗，使切料拨杆与切料组件分离。  
   ![replace_right_filament_cutter_lever_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/replace_right_filament_cutter_lever_001.png)
3. 撕开工具头接口板上的泡棉，断开右涡流线圈连接器和右霍尔感应组件连接器（垂直于连接器方向拔起）。

|  |  |
| --- | --- |
| 撕开泡棉 | 断开连接器 |

4. 移除线缆固定胶布，将线缆从金属卡扣中松出。  
   ![remove_right_eddy_sensor_cable_002.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_right_eddy_sensor_cable_002.png)  
   ![open_and_lock_the_clip.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/open_and_lock_the_clip.jpg)
5. 使用 H1.5 内六角扳手移除 2 颗固定螺丝，取下右涡流线圈。  
   ![remove_right_eddy_sensor_screws_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_right_eddy_sensor_screws_001.png)

## 安装涡流线圈

### 步骤 1：安装右涡流线圈

1. 将右涡流线圈安装到右热端加热组件的上方，锁入2颗螺丝固定。  
   ![remove_right_eddy_sensor_screws_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_right_eddy_sensor_screws_001.png)
2. 将右涡流线圈线缆和右霍尔检测板组件连接到工具头接口板上，贴回泡棉。  
   ![connect_right_eddy_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/connect_right_eddy_cable_2.png)
3. 将涡流线圈线缆卡进金属卡扣中，然后重新用胶布进行缠绕线缆。  
   ![remove_right_eddy_sensor_cable_002.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_right_eddy_sensor_cable_002.png)
4. 安装金属压片支架，使用 H2.0 内六角扳手锁入 2 颗螺丝，取下金属压片支架。  
   ![remove_the_press_plate.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/remove_the_press_plate.jpg)
5. 安装右切料拨杆，锁入1颗螺丝固定。  
   ![lock_right_lever_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/lock_right_lever_screw.png)

### 步骤 2：安装左涡流线圈

1. 将左涡流线圈安装到左热端加热组件的上方，锁入2颗螺丝固定；安装左热端风扇，锁入2颗螺丝固定。  
   ![lock_4_screws.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/lock_4_screws.jpg)
2. 将涡流线圈的线缆从热端加热组件接口板支架的底下穿过，连接到接口板上，然后将线缆整理入两个卡扣中，  
   ![connect_left_eddy_cable.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/connect_left_eddy_cable.jpg)
3. 安装左切料拨杆，要保证切断组件的柄部被卡到拨杆缺口处，锁入1颗螺丝固定拨杆。  
   ![lock_left_lever.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace_eddy_sensor/lock_left_lever.jpg)

### 步骤 3：安装热端

请参考[更换热端和硅胶套](replace-hotend-and-silicone-sock.md)，安装热端和热端硅胶套。  
![install_hotend_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_hotend_001.png)

### 步骤 4：安装工具头外壳

请参考[更换 X2D 工具头外壳](replace-toolhead-housing.md)，安装工具头的外壳。  
![install_toolhead_cover_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-3508-extruder-servo-motor/install_toolhead_cover_001.png)

## 如何验证成功

更换涡流线圈后，执行一次热床校准，如果热床校准有异常，请参考 *X2D 涡流线圈调整* 进行调整。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
