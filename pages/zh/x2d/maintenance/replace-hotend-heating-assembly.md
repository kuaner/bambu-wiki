---
path: zh/x2d/maintenance/replace-hotend-heating-assembly
title: "更换 X2D 热端加热组件"
description: "本文将详细为您介绍 X2D 更换左热端加热组件和右辅助热端加热组件的步骤和注意事项。"
tags: ["x2d"]
created: 2026-04-14T13:45:34.770Z
updated: 2026-06-12T08:49:38.159Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-hotend-heating-assembly
---

## 热端加热组件

**热端加热组件**是安装在工具头上，负责将打印耗材（如 PLA、ABS 等）加热至熔融状态的配件。  
X2D 工具头上安装有 2 个热端加热组件，分别是左热端加热组件和右辅助热端加热组件，二者互不通用。如果其中一个损坏，您需要先确认是哪一个加热组件故障，避免购错配件。  
![fah057.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/fah057.png)  
![heating_assy.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/heating_assy.png)

左热端加热组件配件包装内包含：

1. 左热端加热组件
2. 螺丝 \* 3

右辅助热端加热组件配件包装内包含：

1. 右辅助热端加热组件
2. 螺丝 \* 3

## 何时更换

- 热端加热功能异常，表明可能存在故障。
- 热端加热组件电缆损坏，影响打印机运行。
- 由于操作不当或外力撞击导致热端加热组件明显物理损坏，从而影响其功能。
- Bambu Lab 技术支持根据诊断结果建议更换热端加热组件。

## 所需工具和材料

- 新的热端加热组件
- H1.5 内六角扳手
- H2.0 内六角扳手

## 视频教程

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

> 右切料拨杆只能在辅助热端抬升后（右图）才能进行手动切料测试，否则切料组件会错位并与切料拨杆卡住。  
> ![切料拨杆组件.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-filament-cutter-lever/%E5%88%87%E6%96%99%E6%8B%A8%E6%9D%86%E7%BB%84%E4%BB%B6.jpg)

## 移除热端加热组件

### 步骤 1：移除工具头外壳

请参考[更换 X2D 工具头外壳](replace-toolhead-housing.md)，移除工具头的外壳。  
![replace_toolhead_cover_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/replace_toolhead_cover_001.png)

### 步骤 2：移除热端

请参考[更换热端和硅胶套](replace-hotend-and-silicone-sock.md)，移除热端和热端硅胶套。  
![hotend_removed.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/hotend_removed.jpg)

### 步骤 3：松开切料拨杆

使用 H1.5 内六角扳手分别移除左、右切料拨杆螺丝各 1 颗，使切料拨杆与切刀组件分离，旋转切料拨杆并将其放置于X轴光轴上。  
![replace_filament_cutter_lever_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/replace_filament_cutter_lever_001.png)  
![replace_filament_cutter_lever_002.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/replace_filament_cutter_lever_002.png)

### 步骤 4：移除热端加热组件连接器支架

使用 H1.5 内六角扳手移除 2 颗热端加热组件连接器固定片固定螺丝，取下支架。  
![replace_connector_retaining_clip_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/replace_connector_retaining_clip_001.png)

> 步骤 5~步骤 6 是移除左热端加热组件的操作步骤，如仅需更换右辅助热端加热组件则可跳转至步骤 7。

### 步骤 5：断开左热端加热组件线缆

断开左热端加热组件连接器，并将线缆从线缆卡扣中取出；  
![replace_left_hotend_cable_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/replace_left_hotend_cable_001.png)

### 步骤 6：移除左热端加热组件

使用 H2.0 内六角扳手移除3颗左热端加热组件固定螺丝，取下左热端加热组件。  
![remove_left_hotend_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/remove_left_hotend_001.png)

### 步骤 7：断开右辅助热端加热组件线缆

1. 断开右辅助热端加热组件连接器，移除线缆固定胶布。  
   ![remove_right_hotend_cable_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/remove_right_hotend_cable_001.png)
2. 用内六角扳手按压一侧金属线缆卡扣，松开卡扣，取出热端加热组件线缆。  
   ![remove_right_hotend_cable_buckle_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/remove_right_hotend_cable_buckle_001.png)

### 步骤 8：移除右辅助热端加热组件

使用 H2.0 内六角扳手移除3颗右辅助热端加热组件固定螺丝，取下右辅助热端加热组件。  
![remove_right_hotend_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/remove_right_hotend_001.png)

## 安装热端加热组件

> 步骤 1~步骤 2 是安装右辅助热端加热组件的操作步骤，如仅需安装左热端加热组件则可跳转至步骤 3。

### 步骤 1：安装右辅助热端加热组件

将热端加热组件线缆固定在右侧卡扣内，然后将右辅助热端加热组件安装到工具头上，使用 H2.0 内六角扳手拧紧三颗固定螺丝。  
![install_right_hotend_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_right_hotend_001.png)

### 步骤 2：固定右辅助热端加热组件线缆

1. 将线缆置于金属凹槽中心位置，将金属卡扣一侧置于凹槽内，用内六角扳手按压金属卡扣另一侧，将金属卡扣固定在金属凹槽内。  
   ![install_right_hotend_cable_buckle_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_right_hotend_cable_buckle_001.png)
2. 将线缆固定胶布缠绕至线缆上，整理线缆使其紧贴工具头滑车一侧，并将线缆插头连接到热端加热组件接口板上。

![install_right_hotend_cable_tapeconnector_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/toolheadhousing/install_right_hotend_cable_tapeconnector_001.png)

### 步骤 3：安装左热端加热组件

将热端加热组件线缆从加热底座侧边穿出，然后安装到工具头上（**请确认线缆没有被压在热端加热底座下面！**），使用 H2.0 内六角扳手拧紧三颗固定螺丝。  
![install_left_hotend_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_left_hotend_001.png)

### 步骤 4：固定左热端加热组件线缆

整理线缆并将线缆放入线缆卡扣内，然后将线缆插头连接到热端加热组件接口板上。

> 请确保线缆已完全放入卡扣内。若线缆脱出，可能会因磨损或挤压导致破损，进而引发设备故障

![install_left_hotend_cable_connector_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_left_hotend_cable_connector_001.png)

### 步骤 5：固定热端加热组件连接器支架

安装热端加热组件连接器支架，使用H1.5 内六角扳手拧紧两颗螺丝。  
![install_connector_retaining_clip_001.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_connector_retaining_clip_001.jpg)

### 步骤 6：安装切料拨杆

使用 H1.5 内六角扳手分别固定左、右切料拨杆螺丝各 1 颗。  
![install_filament_cutter_lever_004.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_filament_cutter_lever_004.png)

### 步骤 7：安装热端

请参考[更换热端和硅胶套](replace-hotend-and-silicone-sock.md)，安装热端和热端硅胶套。  
![install_hotend_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_hotend_001.png)

### 步骤 8：安装工具头外壳

请参考[更换 X2D 工具头外壳](replace-toolhead-housing.md)，安装工具头的外壳。  
![install_toolhead_cover_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_toolhead_cover_001.png)

## 如何验证成功

连接电源，打开打印机，将热端升温到100℃，确认温度能正常升温。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
