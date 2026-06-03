---
path: zh/p2s/maintenance/replace-hall-switch-board
title: "更换 P2S 霍尔开关板组件"
description: "更换 P2S 工具头霍尔开关板的操作指引"
tags: ["p2s"]
created: 2025-11-26T02:39:29.552Z
updated: 2026-01-19T04:20:07.011Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-hall-switch-board
---

## 霍尔开关板组件

霍尔开关板组件是安装在挤出机上，主要由霍尔开关板、挤出机入料口和固定座组装而成的组件。它除了是挤出机的供料入口，还同时具备检测料线和切刀状态的功能。

![filament_sensor_p2s.jpg](https://wiki.bambulab.com/p2s/maintenance/replace_filament_sensor/filament_sensor_p2s.jpg)

## 适用打印机型号

**P2S**

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

## 移除旧的霍尔开关板组件

### 1.移除工具头外框

请参考[更换工具头外壳](replace-toolhead-housing.md)，将工具头前盖、中框和后盖按下图图示顺序移除。

![toolhead_housing_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/toolhead_housing_001.png)

### 2. 移除铁氟龙料管

用镊子按压料管支架气动接头黑色部分，移除铁氟龙料管。

![remove_tube.jpg](https://wiki.bambulab.com/x1/troubleshooting/filament-sensor-test/remove_tube.jpg)

### 3. 移除霍尔开关板组件

步骤一：用镊子辅助，拨开霍尔开关板连接器前盖，移除连接线。

![remove_extruder_filament_sensor_cable.webp](https://wiki.bambulab.com/x1/troubleshooting/filament-sensor-test/remove_extruder_filament_sensor_cable.webp)

> 部分机器在连接器位置有涂布黑胶，使用镊子去除后，再打开连接器即可，重新连接时，不需要额外打胶。  
> ![21_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_th_boards_and_fpc_cable/21_021.png)

步骤二：用 H1.5 内六角扳手松开霍尔开关板组件两颗螺丝。

![remove_2_screws.jpg](https://wiki.bambulab.com/x1/troubleshooting/filament-sensor-test/remove_2_screws.jpg)

步骤三：轻轻晃动霍尔开关板组件，向上移除。

![remove_extruder_filament_sensor.webp](https://wiki.bambulab.com/x1/troubleshooting/filament-sensor-test/remove_extruder_filament_sensor.webp)

## 安装新的霍尔开关板组件

### 1. 安装霍尔开关板组件

步骤一：将新的霍尔开关板组件放至下图图示位置，用 H1.5 内六角扳手重新安装霍尔开关板组件两颗螺丝。

![remove_2_screws.jpg](https://wiki.bambulab.com/x1/troubleshooting/filament-sensor-test/remove_2_screws.jpg)

> **安装注意事项：**  
> 固定霍尔传感器时，需使用黑色 BT2-5 规格螺丝。安装前请务必确认螺丝型号，尤其注意检查螺丝长度。若螺丝过长，拧入后可能损坏传感器组件，进而导致检测功能异常，影响设备正常运行。  
> ![screw_for_filament_sensor.png](https://wiki.bambulab.com/p2s/maintenance/replace-extruder-components/screw_for_filament_sensor.png)

步骤二：放回霍尔开关板组件连接线，并盖上连接器盖板。

![install_extruder_filament_sensor_cover.webp](https://wiki.bambulab.com/x1/troubleshooting/filament-sensor-test/install_extruder_filament_sensor_cover.webp)

### 2. 安装工具头后盖和中框

请参考[更换工具头外壳](replace-toolhead-housing.md)，安装工具头中框和后盖（下图 2、3 部分）。

![toolhead_housing_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/toolhead_housing_001.png)

### 3. 安装铁氟龙料管

![install_tube.jpg](https://wiki.bambulab.com/x1/troubleshooting/filament-sensor-test/install_tube.jpg)

### 4. 安装工具头前盖

重新安装工具头前盖排线，然后安装工具头前盖。

> 安装排线时，请注意连接器锁扣朝上。

![install_the_toolhead_front_cover_cable.png](https://wiki.bambulab.com/x1/troubleshooting/filament-sensor-test/install_the_toolhead_front_cover_cable.png)

## 功能验证

打开打印机电源，手动上料(或通过 AMS 加载耗材)，然后操作一次退料操作，能正常完成说明更换完成。

否则，请再次检查所有连接并重试。如果仍然不行，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
