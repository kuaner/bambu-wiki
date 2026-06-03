---
path: zh/x2d/maintenance/replace-extruder-filament-sensor-left
title: "更换 X2D 的左霍尔检测板"
description: "本文介绍了如何更换 X2D 的左霍尔检测板"
tags: []
created: 2026-04-14T13:09:16.966Z
updated: 2026-04-24T02:58:33.943Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-extruder-filament-sensor-left
---

## 物料名称

左霍尔检测板组件是安装在挤出机左侧，主要由霍尔开关板、挤出机入料口和固定座组装而成的组件。它除了是挤出机的供料入口，还同时具备检测料线的功能。  
![dlb067.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/dlb067.png)

## 适用打印机型号

X2D

## 何时更换

- 连接电缆损坏；
- 误报退料异常；
- 误报切刀卡住，经拓竹服务团队确认是霍尔检查开关的问题。

## 所需要工具和材料

- 新的霍尔开关板组件
- H1.5 内六角扳手
- 平头镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 视频教程

## 移除旧的左霍尔检测板

### 1. 移除工具头外壳

请参考[这篇 Wiki](replace-toolhead-housing.md)  来移除工具头前壳和工具头中框。

### 2. 移除切料拨杆组件

请参考[这篇 Wiki](replace-filament-cutter-lever.md)  来移除左右切料拨杆组件的螺丝，将拨杆向外张开，放置在不影响后续操作的位置。

![002_cutting_lever.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/002_cutting_lever.png)

### 3. 移除热端加热组件接口板支架

移除热端加热组件接口板支架螺丝，  
![003_bracket_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/003_bracket_screws.png)

然后将左热端加热组件的连接器从热端加热接口板上断开。  
![004_left_heating_assembly.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/004_left_heating_assembly.png)

### 4. 移除左霍尔检测板

撕开工具头接口板上的泡棉，露出左霍尔检测板的线座  
![005_form.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/005_form.png)

打开线座上的卡扣，断开左霍尔检测板的排线  
![006_remove_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/006_remove_cable.png)

移除右热端加热组件的插头，  
![007_remove_right_assembly.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/007_remove_right_assembly.png)

移除左霍尔检测板的2颗螺丝，向上提起左霍尔检测板组件。

|  |  |
| --- | --- |
| 移除螺丝 | 移除左霍尔检测板 |

## 安装新的左霍尔检测板

### 1. 安装左霍尔检测板

如图示的方向将左霍尔检测板放置到挤出机前盖里  
![009_install_left_hall.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/009_install_left_hall.png)

将线缆有背胶的位置贴在挤出机前盖上。  
![010_tape.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/010_tape.png)

将线缆安装到位，并扣上卡扣，贴回泡棉  
![006_remove_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/006_remove_cable.png)

安装左霍尔检测板的螺丝，  
![008_remove_left_hall_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/008_remove_left_hall_screws.png)

将左右热端加热组件连接到加热组件接口板上  
![002_cutting_lever.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/002_cutting_lever.png)

将热端加热组件接口板的支架放置好，然后锁上螺丝。  
![003_bracket_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_filament_sensor_left/003_bracket_screws.png)

### 2. 安装切料拨杆组件

请参考[这篇 Wiki](replace-filament-cutter-lever.md)  来安装左右切料拨杆组件。

### 3. 安装工具头外壳

请参考[这篇 Wiki](replace-toolhead-housing.md)  来安装工具头前壳和工具头中框。

## 功能验证

打开打印机电源，手动上料(或通过 AMS 加载耗材)，然后操作一次退料操作，能正常完成说明更换完成。

否则，请再次检查所有连接并重试。如果左霍尔开关板仍然不能正常工作，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
