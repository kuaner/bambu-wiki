---
path: zh/x2d/maintenance/replace-mc-board-and-the-cooling-fan
title: "更换 X2D MC 板/MC 板风扇"
description: "本文介绍了如何更换 X2D 的 MC 板 及 MC 板风扇"
tags: []
created: 2026-04-14T13:08:19.533Z
updated: 2026-04-24T03:02:41.939Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-mc-board-and-the-cooling-fan
---

## MC 板/MC 板风扇

MC板的全称是 Main Control Board，中文通常称为 “主控板” ，它是一块集成了微处理器、各种驱动芯片、接口和电路的印刷电路板。

配件包装内包含：  
MC 板 \* 1；  
BT2x5 螺丝 \* 3 - 用于固定 MC 板；  
![dlb071.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/dlb071.png)

MC 板风扇是安装在 MC 板的散热片上，用于给 MC 板芯片散热的风扇。  
![faf024.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/faf024.png)

## 适用打印机型号

X2D

## 何时更换

1. 正常供电情况下， 主控板工作指示灯不闪烁；
2. 连接器损坏，有明显的元器件损坏；
3. MC 风扇异响、不工作或报错（更换风扇）；
4. 拓竹服务团队通过日志文件确认是主控板关联问题。

## 所需要工具和材料

1. 新的 MC 板
2. H2.0 内六角扳手
3. H1.5 内六角扳手
4. 镊子或其他尖锐工具

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 视频教程

## 移除旧的 MC 板及 MC 板风扇

### 步骤 1. 移除背板 （含料管支架&缓冲器）

您可以参考 [更换 X2D 背板](replace-rear-panel.md) 来移除背板。  
![002_remove_rear_panel.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/002_remove_rear_panel.png)

### 步骤 2. 移除废料滑梯

使用 H1.5 内六角扳手移除四颗固定螺丝（BT2x5），然后将废料滑梯取下。  
![003_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/003_remove_purge_chute.jpg)

### 步骤 3. 移除 MC 板风扇

将固定 MC 板风扇的橡胶软钉从 MC 板散热片上松脱出来。  
![004_remove_mc_board_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/004_remove_mc_board_fan.png)  
断开 MC 板风扇连接线，取下 MC 板风扇。  
![005_remove_mc_board_fan_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/005_remove_mc_board_fan_connector.png)

### 步骤 4. 移除 MC 板风扇软钉（如仅更换 MC 板，则可以忽略这一步）

捏住软钉的一端（如图所示），向外拉出，分离 MC 板风扇和软钉。  
![006_remove_mc_board_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/006_remove_mc_board_screw.png)

### 步骤 5. 移除 MC 板

取下 MC 板上的所有线缆接头，请注意不要将线缆拔断，避免影响后续安装。  
![007_remove_all_mc_board_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/007_remove_all_mc_board_cable.png)

断开MC板上正面的所有连接线。请注意，有些插头采用卡扣结构，需先按压插座上方的卡扣解锁插头才能拔出。具体需要解锁卡扣的插头，参考下图。  
![008_cable_clip.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/008_cable_clip.png)

为了防止运输过程中插头松动，散热片下方的三个步进电机插头使用电子硅胶进行了加固，  
![009_cable_glue.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/009_cable_glue.png)

请先使用尖锐的工具，如镊子，移除白胶后再拔除线缆接头。  
![010_use_tweezer_to_remove_glue.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/010_use_tweezer_to_remove_glue.png)

移除 MC 板上的 3 颗螺丝，取下MC板。  
![011_mc_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/011_mc_board_screws.png)

## 安装新的 MC 板/ MC 板风扇

### 步骤 1. 安装 MC 板

避让连接线缆，将 MC 板放置在内衬的安装位置上，锁紧 3 颗固定螺丝。  
![011_mc_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/011_mc_board_screws.png)

连接线缆，MC 板接口说明如下：  
![012_mc_board_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/012_mc_board_connector.png)

| 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AP 板（通信） | 5 | 腔温 NTC | 9 | XY 电机（A） | 13 | 辅助挤出机（电机） |
| 2 | AP 板（供电） | 6 | 腔温加热组件 NTC | 10 | XY 电机（B） | 14 | Z 电机 |
| 3 | 自适应风道切换组件 | 7 | 腔温加热组件 | 11 | 电源 | 15 | AC 板 |
| 4 | 缓冲器 | 8 | 热床（信号线） | 12 | 辅助挤出机（通信） | 16 | MC 板风扇 |

### 步骤 2. 安装 MC 板风扇软钉（如仅更换 MC 板，则可以忽略这一步）

> 安装新风扇时，需要先将软橡胶钉的一端安装到风扇上

将软钉从风扇有标签的一面安装，从另一头将钉子拉出，需要确保风扇固定在软钉两端的限位中间。然后将四个软钉都安装到位。

|  |  |
| --- | --- |
|  |  |

### 步骤 3. 安装 MC 板风扇

连接风扇电缆  
![005_remove_mc_board_fan_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/005_remove_mc_board_fan_connector.png)

将软橡胶钉连接到散热片上（顺序：右上、右下、左下、左上）  
![014_install_mc_board_fan_on_sink.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/014_install_mc_board_fan_on_sink.png)

### 步骤 4. 安装废料滑梯

使用 H1.5 内六角扳手安装四颗固定螺丝（BT2x5），将废料滑梯安装好。  
![003_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/003_remove_purge_chute.jpg)

### 步骤 5. 安装背板 （含料管支架&缓冲器）

您可以参考 [更换 X2D 背板](replace-rear-panel.md) 来安装背板。

## 功能验证

连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆连接是否正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
