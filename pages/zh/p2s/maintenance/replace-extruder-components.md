---
path: zh/p2s/maintenance/replace-extruder-components
title: "更换 P2S 挤出机配件"
description: "挤出机相关部件的拆解和安装指引"
tags: []
created: 2025-10-14T12:50:05.307Z
updated: 2025-12-08T02:57:37.672Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-extruder-components
---

## 挤出机

P2S 的挤出机，设置了3个独立的配件，分别是：

- 霍尔开关板组件：安装在挤出机的上部，具有检测耗材功能的配件。
- 挤出机齿轮组件：安装在挤出机内部，经挤出电机带动后，能实现将耗材输送到热端或退出挤出机的齿轮组件。
- 挤出机前盖组件：挤出机的外壳。  
  ![dlb055.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/dlb055.jpg)![fae035.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fae035.jpg)![fae039.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fae039.jpg)

## 何时更换

需要更换挤出机齿轮组件的常见情况：

- 齿轮磨损或轴承磨损，导致打印异常
- 经拓竹技术支持判断，需要更换齿轮组件

需要更换霍尔板开关组件的常见情况：

- 耗材检测功能失效
- 排线断裂损坏

需要更换挤出机前盖组件的常见情况：

- 物理损坏，影响产品使用

## 工具和材料

- 需要更换的配件：霍尔开关板组件/挤出机齿轮组件/挤出机前盖组件
- H1.5 内六角扳手
- H2.0 内六角扳手
- 镊子

> 安装提醒：  
> 1.霍尔开关板处使用的螺丝是 BT2-5的黑色螺丝，组装时请注意检查，过长的螺丝会损伤配件并导致检测异常。  
> ![screw_for_filament_sensor.png](https://wiki.bambulab.com/p2s/maintenance/replace-extruder-components/screw_for_filament_sensor.png)  
> 2.挤出主动轮两端均有一个轴承，分别是在挤出机前盖和工具头滑车上，轴承缺少会导致挤出失败。![bearings.png](https://wiki.bambulab.com/p2s/maintenance/extruder_unit/bearings.png)  
> 3.挤出从动轮处的金属端盖要是放置在弹簧的上方，不然会导致挤出失败。  
> ![install_the_plate.png](https://wiki.bambulab.com/p2s/maintenance/extruder_unit/install_the_plate.png)

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆除挤出机

### 第 1 步：移除工具头外壳

为更方便操作，请参考[更换工具头外壳](replace-toolhead-housing.md)，将工具头外壳拆除。  
![toolhead_housing_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/toolhead_housing_001.png)

### 第 2 步：松开切刀

扶着切刀刀柄，用 H2.0 内六角扳手拧松切刀刀柄螺丝， 使切刀能从挤出机中完全松出。

![cutter_screw_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/cutter_screw_002.png)  
![cutter_released_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/cutter_released_003.png)

### 第 3 步：移除挤出机

按压气动接头，拨出料管。  
![remove_the_tube_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/remove_the_tube_005.png)

用镊子打开挤出接口板的连接器盖子，断开进料霍尔板线缆。  
![dipsconnect_fpc_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/dipsconnect_fpc_007.png)

> 断开该 FPC 排线时，请小心操作，避免因用力过猛导致排线损坏。

用 H2.0 内六角扳手移除 4 颗螺丝(BT3-7)，取下挤出机。  
![4_screws_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/4_screws_009.png)  
![take_off_extruder_unit_010_.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/take_off_extruder_unit_010_.png)

### 第 4 步：移除霍尔开关板组件

用 H1.5 内六角扳手移除 2 颗螺丝。  
![2_screws_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/2_screws_012.png)

取下霍尔开关板组件。  
![filament_sensor_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/filament_sensor_013.png)

### 第 5 步：分离挤出机前盖和挤出机齿轮组件

> 挤出机内有较多小配件，为避免内部零件脱落，请放置在干净的平台上并将齿轮朝上进行处理。

用 H2.0 内六角扳手拧松 1 颗螺丝，并从挤出机上取下黄色的挤出主动轮。  
![yellow_gear_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/yellow_gear_014.png)

> **提示：**
>
> 当耗材卡在挤出机的**主动轮**与**从动轮**之间时，可能无法从正面直接取出主动轮。
>
> |  |  |
> | --- | --- |
> | 耗材卡在齿轮之间示意图 | 卡丝细节图 |
>
> 如无法直接取出，请从**主动轮背面**轻敲轴心将其顶出。敲击位置如下：
>
> ![主动轮背面敲击位置](https://wiki.bambulab.com/p2s/maintenance/out_2.jpg)
>
> 敲出过程如下：
>
> ![主动轮敲出过程演示](https://wiki.bambulab.com/p2s/maintenance/out.webp)

从挤出机前盖里取出压紧块、挤出从动轮等配件。  
![driven_gear_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/driven_gear_015.png)

## 安装挤出机

### 第 1 步：将挤出轮组件安装到挤出机前盖

将挤出从动轮安装到挤出前盖上。  
![install_driven_gear_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/install_driven_gear_017.png)  
将弹簧和金属端盖安装到压紧块里，贴着挤出从动轮，将压紧块安装到挤出前盖。  
![install_spring_and_plate_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/install_spring_and_plate_016.png)  
装上挤出主动轮组件，锁紧 1 颗螺丝。  
![install_yellow_gear_018.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/install_yellow_gear_018.png)

### 第 2 步：安装霍尔开关板组件

将霍尔开关板组件安装到挤出机上。  
![filament_sensor_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/filament_sensor_013.png)  
锁入 2 颗螺丝。  
![2_screws_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/2_screws_012.png)

### 第 3 步：安装挤出机组件

将挤出机安装到工具头滑车上。  
![install_extruder_unit_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/install_extruder_unit_011.png)  
锁入 4 颗螺丝。  
![4_screws_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/4_screws_009.png)  
将霍尔开关板排线连接到挤出接口板的连接器上，合上连接器，按压连接器盖子，使盖子能完全贴合软排线。  
![connect_fpc_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/connect_fpc_008.png)

### 第 4 步：安装切刀

用手扶着切刀刀柄，沿着挤出机切刀刀槽的位置，将切刀滑进挤出机，用内六角扳手锁紧刀柄螺丝。  
![slide_in_the_cutter_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/slide_in_the_cutter_004.png)

### 第 5 步：安装工具头外壳

参考[更换工具头外壳](replace-toolhead-housing.md)的内容，安装好工具头外壳。  
![close_front_cover_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/close_front_cover_002.png)

## 如何验证成功

- 刀柄能顺畅动作
- 通电检查，霍尔开关板能正常检测料线状态
- 通电检查，挤出机能正常被挤出电机带动

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
