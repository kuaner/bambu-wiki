---
path: zh/x2d/maintenance/replace-extruder-components
title: "更换 X2D 挤出机配件"
description: "本文介绍了如何更换 X2D 的挤出机前盖、挤出机齿轮组件、左霍尔检测板及右霍尔检测板"
tags: []
created: 2026-04-14T13:08:52.144Z
updated: 2026-06-10T12:06:50.292Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-extruder-components
---

## 挤出机配件

**X2D 的挤出机，设置了 4 个独立的配件，分别是：**

- **左霍尔检测板组件：** 安装在左挤出机的上部，具有检测耗材功能的配件。
- **右霍尔检测板组件：** 安装在右挤出机的上部，具有检测耗材功能的配件。
- **挤出机齿轮组件(同P2S)：** 安装在挤出机内部，经挤出电机带动后，能实现将耗材输送到热端或退出挤出机的齿轮组件。
- **挤出机前盖组件：** 挤出机的外壳。  
  ![dlb067.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/dlb067.png)![dlb068.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/dlb068.png)![fae056.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/fae056.png)

## 适用打印机型号

X2D

## 何时更换

**需要更换挤出机齿轮组件的常见情况：**

- 齿轮磨损或轴承磨损，导致打印异常
- 经拓竹技术支持判断，需要更换齿轮组件  
  **需要更换霍尔板开关组件的常见情况：**
- 耗材检测功能失效
- 排线断裂损坏  
  **需要更换挤出机前盖组件的常见情况：**
- 物理损坏，影响产品使用

## 所需要工具和材料

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 易损提示

> 移除工具头接口板布线泡棉时，请您沿左侧向玻璃前门方向轻拉，避免因拉力过大导致左霍尔检测板连接器盖板松脱或损坏。  
> ![泡棉3.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/%E6%B3%A1%E6%A3%893.jpg)

> 在重新安装右霍尔检测板组件时，请您注意将右霍尔检测板组件上的凹槽准确卡入涡流线圈支架。若安装不到位，将导致辅助热端无法切换。  
> ![右霍尔检测板组件安装限位.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-extruder/%E5%8F%B3%E9%9C%8D%E5%B0%94%E6%A3%80%E6%B5%8B%E6%9D%BF%E7%BB%84%E4%BB%B6%E5%AE%89%E8%A3%85%E9%99%90%E4%BD%8D.jpg)  
> 正确安装的右霍尔检测板组件下方能与涡流线圈齐平（右图），若两者之间存在明显距离（左图），说明安装未到位，需重新调整。  
> ![右霍尔检测板组件安装对比.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-extruder/%E5%8F%B3%E9%9C%8D%E5%B0%94%E6%A3%80%E6%B5%8B%E6%9D%BF%E7%BB%84%E4%BB%B6%E5%AE%89%E8%A3%85%E5%AF%B9%E6%AF%94.jpg)

> 右切料拨杆只能在辅助热端抬升后（右图）才能进行手动切料测试，否则切料组件会错位并与切料拨杆卡住。  
> ![切料拨杆组件.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-filament-cutter-lever/%E5%88%87%E6%96%99%E6%8B%A8%E6%9D%86%E7%BB%84%E4%BB%B6.jpg)

## 视频教程

## 移除旧的挤出机部件

### 第 1 步. 移除工具头外壳

请参考[这篇 Wiki](replace-toolhead-housing.md) 来移除工具头外壳。

### 第 2 步. 移除热端

请参考[这篇 Wiki](replace-hotend-and-silicone-sock.md) 来移除左右两个热端。  
![hotend_removed.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/hotend_removed.jpg)

### 第 3 步. 移除左右切料拨杆组件

移除左切料拨杆组件的螺丝，将拨杆向外张开，放置在不影响后续操作的位置。

|  |  |
| --- | --- |
|  |  |

移除右切料拨杆组件的螺丝，将拨杆向外张开，放置在不影响后续操作的位置。

|  |  |
| --- | --- |
|  |  |

### 第 4 步. 移除料管

按压左霍尔检测板的气动接头并拔出料管。  
![004_left_ptfe_tube.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/004_left_ptfe_tube.png)  
向右拨动堵嘴组件的拨杆，使得右霍尔检测板的气动接头露出，用扳手逆时针拧松气动接头，拔出料管。

|  |  |
| --- | --- |
|  |  |

### 第 5 步. 移除热端加热组件及其他线缆

移除热端加热组件接口板支架螺丝，移除支架，然后断开热端加热组件的连接器。  
![006_heating_assembly_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/006_heating_assembly_connector.png)  
撕下布线泡棉，将工具头接口板上的连接器断开（LOGO LED 线缆除外）

|  |  |
| --- | --- |
|  |  |

将所有线缆从线槽中移出，稍微拨到不影响后续操作的位置上。  
![008_pull_out_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/008_pull_out_cable.png)

### 第 6 步. 移除左热端风扇

移除左热端风扇上的两颗螺丝，检出左热端风扇。

|  |  |
| --- | --- |
|  |  |

### 第 7 步. 移除挤出机前盖

移除挤出机前盖的 3 颗螺丝，  
![010_extruder_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/010_extruder_screws.png)  
轻轻地将挤出机前盖组件从工具头上分离，可以稍微按压住热端加热组件接口板，避免过度拉扯线缆导致损坏。  
![011_remove_extruder_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/011_remove_extruder_cover.png)  
向上松出挤出机前盖组件，将右霍尔检测板留在工具头上。  
![011_right_hall.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/011_right_hall.png)

### 第 8 步. 移除右霍尔检测板

将布线的醋酸胶布撕开，取下右霍尔检测板。

|  |  |
| --- | --- |
|  |  |

### 第 9 步. 分离挤出机齿轮组件

用手拿着挤出机上的减速大齿轮，取下挤出机齿轮。

|  |  |
| --- | --- |
|  |  |

移除挤出机组件上方的从动轮压块螺丝。  
![016_remove_block_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/016_remove_block_screw.png)  
取下从动轮压块，并用钳子或镊子取下从动轮齿轮组件。  
![017_driven_extruder_gear.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/017_driven_extruder_gear.png)  
将从动轮压块中的弹簧和压片取出。  
![018_gear_block.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/018_gear_block.png)

### 第 10 步. 移除左切料组件

用螺丝刀取下压块螺丝，取下压块。  
![014_left_cutter_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/014_left_cutter_screw.png)  
移除左切料组件。

|  |  |
| --- | --- |
|  |  |

### 第 11 步. 移除左霍尔检测板

移除挤出机组件上的 2 颗左霍尔检测板螺丝，  
![019_left_hall_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/019_left_hall_screws.png)  
捏住左霍尔开关板上的气动接头，向上拿出左霍尔检测板，  
![020_left_hall_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/020_left_hall_connector.png)  
分离排线和挤出机前盖（排线有背胶，请轻轻撕下），分离左霍尔检测板和挤出机前盖。

|  |  |
| --- | --- |
|  |  |

## 安装新的挤出机部件

### 第 1 步. 安装挤出机齿轮组件

将挤出机从动轮组件安装如图所示的方向，穿过转轴，放入挤出机前盖，  
![022_install_driven_gear.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/022_install_driven_gear.png)  
拿起从动轮压块，放入压簧，

|  |  |
| --- | --- |
|  |  |

将压片凸起的一面朝向压簧放置好，将整个从动轮压块如图放入挤出机前盖中，  
![024_tableting.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/024_tableting.png)  
将主动挤出机齿轮放入挤出机前盖，  
![025_install_driven_gear_block.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/025_install_driven_gear_block.png)  
安装固定压块的螺丝。  
![026_install_block_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/026_install_block_screw.png)

### 第 2 步. 安装左切料组件

如图所示方向将左切料组件放入挤出机前盖下方的凹槽中，安装到位，  
![027_install_left_cutter.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/027_install_left_cutter.png)  
将料线压块安装到挤出机前盖上，并锁 1 颗螺丝。

|  |  |
| --- | --- |
|  |  |

### 第 3 步. 安装左霍尔检测板

将左霍尔检测板放置在挤出机前盖的左侧槽位，按压到位。  
**注意：** 霍尔板（绿色电路板）需要朝向左方，线缆朝向后方，避免安装错方向，  
![029_install_left_hall.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/029_install_left_hall.png)  
安装左霍尔检测板的 2 颗螺丝。  
![019_left_hall_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/019_left_hall_screws.png)

### 第 4 步. 安装右霍尔检测板

如图示的方向，从挤出机前盖下方向上推入右霍尔检测板，并推到底。  
![030_install_right_hall.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/030_install_right_hall.png)  
向左拨动工具头下方堵嘴组件的拨杆，使得右霍尔检测板降下。  
![005_switch_flow_blocker.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/005_switch_flow_blocker.png)

### 第 5 步. 安装挤出机前盖

将挤出机前盖放置到工具头滑车前盖上，期间请用手抵住右霍尔检测板，以防它掉出。  
![031_install_extruder.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/031_install_extruder.png)  
锁入 3 颗挤出机前盖螺丝。  
![010_extruder_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/010_extruder_screws.png)  
将右霍尔检测板的线缆用醋酸胶布和其他线缆捆绑在一起，并放置在右边的线槽内。  
![032_right_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/032_right_cable.png)  
将左侧的线缆放置在左边的线槽内，请注意先放入更细的涡流线圈线。  
![033_left_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/033_left_cable.png)

### 第 6 步. 安装左热端风扇

将左热端风扇放置到位，并锁入 2 颗固定螺丝。  
![034_left_hotend_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/034_left_hotend_screws.png)

### 第 7 步. 连接线缆

安装工具头接口板和热端加热组件接口板的线缆，并贴回泡棉。  
![035_install_the_form.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/035_install_the_form.png)  
工具头接口板线缆接口说明如下：

| 序号 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 接口说明 | 左涡流线圈 | 左霍尔检测板 | 右霍尔检测板 | 右涡流线圈 |

![007_extruder_connection_board_cable_connection.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/007_extruder_connection_board_cable_connection.png)  
可以参考[这篇 Wiki](replace-th-board.md) 获得更详细的指引。  
将热端加热组件接口板的支架安装到位并锁上 2 颗螺丝。  
![036_install_hotend_heating_bracket.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/036_install_hotend_heating_bracket.png)

> 注意：左涡流线圈、左霍尔检测板、右霍尔检测板、右涡流线圈的线缆均要在支架底下。

### 第 8 步. 安装料管

向右拨动堵嘴组件，使得右霍尔检测板上的气动接头露出，将料管放置到位，然后用打印的扳手顺时针拧紧气动接头，固定住料管，然后向左拨动堵嘴组件，使得右霍尔检测板降下。

|  |  |
| --- | --- |
|  |  |

将左挤出机料管安装到左气动接头上。  
![038_install_left_ptfe_tube.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_extruder_unit/038_install_left_ptfe_tube.png)  
安装完成后可以向上轻轻拔料管，查看是否安装到位。

### 第 9 步. 安装左右切料拨杆组件

将右切料拨杆恢复原位，锁上 1 颗螺丝，

|  |  |
| --- | --- |
|  |  |

将左切料拨杆恢复原位，锁上 1 颗螺丝，

|  |  |
| --- | --- |
|  |  |

**注意：** 左右切料组件的刀柄需要处于切料拨杆组件的缺口内，您可以参考[这篇 Wiki](replace-filament-cutter-lever.md)  来参考更详细的切料拨杆组件安装教程。

### 第 10 步. 安装热端

请参考[这篇 Wiki](replace-hotend-and-silicone-sock.md) 来安装左右两个热端。  
![install_hotend_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_hotend_001.png)

### 第 11 步. 安装工具头外壳

请参考[这篇 Wiki](replace-toolhead-housing.md) 来安装工具头外壳。

![install_toolhead_cover_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-hotend-heating-assembly/install_toolhead_cover_001.png)

## 功能验证

- 刀柄能顺畅运动
- 通电检查，左右霍尔检测板能正常检测料线状态
- 通电检查，挤出机能正常被挤出电机带动

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
