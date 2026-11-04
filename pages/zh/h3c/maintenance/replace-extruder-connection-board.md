---
path: zh/h3c/maintenance/replace-extruder-connection-board
title: "工具头电路板（TH 板/挤出接口板) 更换指南"
description: "工具头上安装有两块主要的电路板，分板为 TH 板和挤出接口板。"
tags: []
created: 2026-11-03T12:46:16.049Z
updated: 2026-11-03T12:46:17.137Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-extruder-connection-board
---

## TH 板

安装在工具头背部的小型集成电路板，主要负责控制工具头上各个电机的运转、监测工具的状态并协调热端温度与挤出动作的同步。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_d0cdfbe459.jpg)

> **TH 板 连接器说明如下：**  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_fa72ce2ed4.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 挤出接口板 1 | 4 | 部件冷却风扇 |
| 2 | 挤出接口板 2 | 5 | 工具头摄像头 |
| 3 | 2521 挤出电机 | 6 | AP 板 （USB-C） |

## 挤出接口板

安装在工具头顶部的小型集成电路板，主要负责连接挤出主板与各个功能组件，起到了中继电路板的作用。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_953987167e.jpg)

> **挤出接口板 连接器说明如下：**  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_9b8ea2ef65.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | **泊位标定传感器** | 6 | 2012 锁紧电机 |
| 2 | 裹头检测传感器 | 7 | 2012 变距电机 |
| 3 | 工具识别传感器 | 8 | TH 板 1 |
| 4 | 热端风扇 | 9 | TH 板 2 |
| 5 | 涡流线圈 | / | / |

## 何时更换

1. 电路板上的元器件、连接器或连接排线出现明显的损坏，并影响使用；
2. 经过交换检查或工具的测量，确认是相关配件的故障；
3. 经 Bambu Lab 技术支持确认，需更换 TH 板、挤出接口板的故障。

## 工具和材料

- H1.5 内六角扳手
- 镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除工具头电路板

> 1. 挤出接口板与 TH 板在拆装上没有必然的先后关系，实际更换过程中，请根据需要更换的电路板进行移除。本指南按单独更换对应的电路板进行编写。
> 2. 更换新的 TH 板，可能需要运行一个校准代码，请在确认问题解决后进行。

### 第 1 步 移除工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，移除 工具头的所有外壳。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 移除挤出接口板

依次断开接口板上的连接线缆，共 9 条线缆。  
其中：

- 软排线建议借助镊子进行拆装；
- NO. 6/7 两条软排线有贴附胶布，需要撕开后再揭开连接器盖子；
- NO. 2/4/5 三根线缆可以直接拔除。
- NO. 8/9 两条软排线打开盖子即可。  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_9b8ea2ef65.jpg)

用 H1.5 内六角扳手移除 4 颗螺丝，然后向前取下挤出接口板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/11_h3c_____screws_kit_for_h3c_1aaebe72e9.jpg)

### 第 3 步 移除 TH 板

打开 NO. 1/2 的连接器盖子，然后依次断开 NO. 3/4/5 连接线缆。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_fa72ce2ed4.jpg)

用 H1.5 内六角扳手移除固定 TH 板的 3 颗螺丝 和 1 颗 USB-C 线缆接头的加固螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_ff5fa0784f.jpg)

将 TH 板与工具头分离少许，然后将 USB-C 线从 TH 板上断开，取下 TH 板。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装工具头电路板

### 第 1 步 安装 TH 板

将 TH 板贴近 USB-C 插头，将 USB-C 线连接到 TH 板的连接器上。将 TH 板与顶部的两根排线进行连接，确认连接到位并合上盖子。

|  |  |
| --- | --- |
| 图 | 图 |

对齐安装定位柱和螺丝孔，避让 3 根据连接线，将 TH 板安装到工具头背面，锁入 4 颗螺丝，连接 3 根线缆。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 安装挤出接口板

在将挤出接口板放置到工具头顶部时，工具头后盖已安装的情况下，需要同步连接与 TH 板相连的两根软排线，然后避让其他线缆将板子放置到工具头顶部。

|  |  |
| --- | --- |
| 图 | 图 |

用手帮助固定接口板，然后按下图标识的顺序依次锁入 4 颗螺丝进行固定。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_51b09f3580.jpg)

连接其余的所有线缆，其中，NO. 6/7 需要贴上胶布加固。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/75________th______________extruder_connection_board_replacement_guide_9b8ea2ef65.jpg)

### 第 3 步 安装工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，装回工具头的所有外壳。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-extruder-connection-board/zh/01__________2012_toollock_motor_replacement_guide_e6f862449e.jpg)

## 功能验证

连接电源，启动打印机，执行一次加载打印头的操作，能正常完成即可。  
如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
