---
path: zh/x2d/maintenance/replace-ac-board
title: "更换  X2D AC 板"
description: "本文介绍了如何更换 X2D AC 板"
tags: []
created: 2026-04-14T14:02:11.043Z
updated: 2026-05-21T07:32:13.004Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-ac-board
---

## 物料名称

AC 板是用于给打印机的热床提供交流电源并实现输出控制的电路板。  
![dlb072.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/dlb072.png)

> AC 板有区分高压版本和低压版本，与热床组件和腔温加热组件要配套使用，不可用错！

## 适用打印机型号

X2D

## 何时更换

AC 板出现明显的损坏；  
经 Bambu Lab 官方技术支持确认需更换 AC 板。

## 所需要工具和材料

- 新的 AC 板
- H1.5 内六角扳手
- H2.0 内六角扳手
- 镊子或其他尖锐工具

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 视频教程

## 移除旧的 AC 板

### 步骤 1. 移除背板 （含料管支架&缓冲器）

您可以参考[更换 X2D 背板](replace-rear-panel.md)来移除背板：  
![002_remove_rear_panel.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/002_remove_rear_panel.png)

### 步骤 2. 移除废料滑梯

使用 H1.5 内六角扳手移除四颗固定螺丝（BT2x5），然后将废料滑梯取下。  
![003_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/003_remove_purge_chute.jpg)

### 步骤 3. 移除 MC 板风扇

将 MC 板风扇从 MC 板散热片上的凹槽中取出。  
![004_remove_mc_board_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/004_remove_mc_board_fan.png)

取下 MC 板风扇线缆接头，断开风扇连接线缆。  
![005_remove_mc_board_fan_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/005_remove_mc_board_fan_connector.png)

### 步骤 4. 移除电源保护盖

使用 H1.5 内六角扳手移除五颗螺丝移除电源保护盖，  
![006_remove_supply_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/006_remove_supply_cover.png)

并将其取下。  
![007_remove_supply_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/007_remove_supply_cover.png)

### 步骤 5. 移除 AC 板线缆

使用螺丝刀撬开电源线保护盖，  
![008_pry_the_lid.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/008_pry_the_lid.png)

用十字螺丝刀拧松供电线固定螺丝，移除三根供电线缆。  
![009_remove_supply_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/009_remove_supply_cable.png)

断开热床组件供电线缆。

|  |  |
| --- | --- |
| 高压版 | 低压版 |

将胶套推出后，使用螺丝刀顶住插头上的卡扣，向外缓慢拔出，该类型插头拆卸方式相同。

|  |  |
| --- | --- |
|  |  |

移除腔温加热组件供电线缆

|  |  |
| --- | --- |
| 高压版 | 低压版 |

### 步骤 6. 移除 AC 板

断开 MC 板上 的 XT30 插头，  
![012_remove_xt30.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/012_remove_xt30.png)

移除 MC 板螺丝，  
![013_mc_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/013_mc_board_screws.png)

使 MC 板位置可以移动，露出AC板螺丝  
![014_remove_mc_board.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/014_remove_mc_board.png)

使用 H1.5 内六角扳手移除 AC 板的三颗螺丝，取下AC板  
![015_ac_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/015_ac_board_screws.png)

将 AC 板取下，断开 MC-AC 连接线。  
![016_mc_ac_cable_.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/016_mc_ac_cable_.png)

## 安装新的 AC 板

### 步骤 1. 安装 AC 板

将 AC 板放置到位，连接 MC-AC 连接线。  
![016_mc_ac_cable_.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/016_mc_ac_cable_.png)

使用 H1.5 内六角扳手安装 AC 板的三颗螺丝，锁紧AC板。  
![015_ac_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/015_ac_board_screws.png)

安装 MC 板螺丝，并连接 MC 板上的 XT30 接头。

|  |  |
| --- | --- |
|  |  |

### 步骤 2.1. 连接 AC 板上的线缆（高压版）

AC 板接头说明如下  
![ac_board_110.png](https://public-cdn.bblmw.com/wiki/new/x2d/ac_board_220.png)

| 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 |
| --- | --- | --- | --- | --- | --- |
| 1 | 电源线（棕色） | 4 | MC - AC 线 | 7 | 腔温加热组件供电线（红色） |
| 2 | 电源线（蓝色） | 5 | 热床供电线（红色） | 8 | 腔温加热组件供电线（蓝色） |
| 3 | 电源线（黄色） | 6 | 热床供电线（棕色） |  |  |

安装腔温加热组件供电线缆，红线在上，蓝线在下，  
![018_chamber_cable_color.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/018_chamber_cable_color.png)

安装热床组件供电线缆，红线在上，棕线在下。  
![010_hv_heatbed_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/010_hv_heatbed_cable.png)

将三根电源线（棕色、蓝色、黄色）与 AC 板连接，盖上橙色盖子。  
![009_remove_supply_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/009_remove_supply_cable.png)

### 步骤 2.2 连接 AC 板上的线缆（低压版）

AC 板接头说明如下

![ac_board_110.png](https://public-cdn.bblmw.com/wiki/new/x2d/ac_board_220.png)  
![ac_board_110.png](https://public-cdn.bblmw.com/wiki/new/x2d/ac_board_110.png)

| 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 |
| --- | --- | --- | --- | --- | --- |
| 1 | 电源线（棕色） | 4 | MC - AC 线 | 7 | 腔温加热组件供电线（黑色） |
| 2 | 电源线（蓝色） | 5 | 热床供电线（红色） | 8 | 腔温加热组件供电线（白色） |
| 3 | 电源线（黄色） | 6 | 热床供电线（棕色） | 9 | 热床供电线接地线（蓝色） |

安装腔温加热组件供电线缆，黑线在上，白线在下。  
![011_lv_chamber_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/011_lv_chamber_cable.png)

安装热床组件供电线缆，红线在左，蓝线在右，棕线在下。  
![010_lv_heatbed_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/010_lv_heatbed_cable.png)

将三根电源线（棕色、蓝色、黄色）与 AC 板连接，盖上橙色盖子。  
![009_remove_supply_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/009_remove_supply_cable.png)

### 步骤 3. 安装电源保护盖

安装电源保护盖，并使用 H1.5 内六角扳手安装五颗螺丝锁紧电源保护盖。

|  |  |
| --- | --- |
|  |  |

### 步骤 4. 安装 MC 板风扇

连接风扇线缆。  
![005_remove_mc_board_fan_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/005_remove_mc_board_fan_connector.png)

将软橡胶钉连接到散热片上（顺序：右上、右下、左下、左上）  
![020_install_mc_board_fan_on_sink.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/020_install_mc_board_fan_on_sink.png)

### 步骤 5. 安装废料滑梯

使用 H1.5 内六角扳手安装四颗固定螺丝（BT2x5），将废料滑梯安装好。  
![003_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ac_board/003_remove_purge_chute.jpg)

### 步骤 6. 安装背板 （含料管支架&缓冲器）

您可以参考 [更换 X2D 背板](replace-rear-panel.md) 来安装背板。

## 功能验证

连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆连接是否正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
