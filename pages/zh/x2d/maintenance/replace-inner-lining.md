---
path: zh/x2d/maintenance/replace-inner-lining
title: "更换 X2D 内衬"
description: ""
tags: []
created: 2026-04-26T12:04:43.135Z
updated: 2026-05-11T03:07:25.392Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-inner-lining
---

## 内衬

内衬是位于打印机后部的塑料支架，用于承载 MC 板、AC 板、电源模块等电路配件，并将其与打印腔室隔离。

![fas083.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/fas083.png)

> 在早期的产品中，我们配备了辅助热端的擦嘴硅胶来解决喷嘴清洁的问题。后来我们已通过算法优化解决了这一问题，不再需要使用辅助硅胶，所以重新设计并去除这个辅助擦嘴装置。我们出货的产品中虽然存在不同的版本，但都是正常的，都可以安装到机器上正常使用。

|  |  |
| --- | --- |
| 变更前 | 变更后 |

## 何时更换

1. 内衬出现变形损坏

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除内衬

### 步骤 1. 移除辅助挤出机、料管支架、缓冲器和背板

您可以参考如下 Wiki 的拆解部份内容，依次移除料管支架、缓冲器和背板。

- [更换辅助挤出机](replace-auxiliary-extruder.md)
- [更换缓冲器](replace-filament-buffer.md)
- [更换背板](replace-rear-panel.md)

![002_remove_rear_panel.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_left_side_panel/002_remove_rear_panel.png)

### 步骤 2：移除吐料组件和废料滑梯

使用 H1.5 内六角扳手移除四颗固定螺丝（BT2x5），然后将废料滑梯取下。  
![003_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/003_remove_purge_chute.jpg)

您可以参考 [更 X2D 吐料组件](replace-purge-wiper.md) 来移除吐料组件。  
![003_lift_purge_wiper.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_purge_wiper/003_lift_purge_wiper.png)

### 步骤 3：移除 MC 板风扇

将固定 MC 板风扇的橡胶软钉从 MC 板散热片上松脱出来。  
![004_remove_mc_board_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/004_remove_mc_board_fan.png)  
断开 MC 板风扇连接线，取下 MC 板风扇。  
![005_remove_mc_board_fan_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/005_remove_mc_board_fan_connector.png)

### 步骤 4：移除屏幕和前面盖

您可以参考 [更换前面盖](replace-front-cover.md) 的内容，移除屏幕和前面盖。  
![009_pull_out_the_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_front_cover/009_pull_out_the_cable.png)

### 步骤 5：移除腔温加热组件和左侧板

您可以参考[更换腔温加热组件](replace-chamber-heater-unit.md)，来移除腔温加热组件。  
![009_remove_chamber_unit.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/remove_chamber_heater_unit/009_remove_chamber_unit.png)

您可以参考[更换 X2D 左侧板](replace-left-side-panel.md)，来移除左侧板。  
![016_remove_left_panel.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_left_side_panel/016_remove_left_panel.jpg)

### 步骤 6：移除自适应风道切换组件和右侧板

您可以参考 [更换自适应风道切换组件](../../p2s/maintenance/replace-adaptive-airflow-switching-unit.md) 来移除自适应风道切换组件。  
![remove_the_fan_assembly.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/remove_the_fan_assembly.png)

您可以参考 [更换 X2D 右侧板](replace-right-side-panel.md) 来移除右侧板。  
![010_remove_left_panel.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_right_side_panel/010_remove_left_panel.jpg)

### 步骤 7：移除电源保护盖和电源线

断开热床信号线和供电线，用 H1.5 内六角扳手移除 5 颗螺丝，将电源保护盖从内衬上移除。  
![protective_cover.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/protective_cover.png)  
用十字螺丝刀拧松 AC 板和电源板上的供电线螺丝，移除供电线缆；用 H1.5 内六角扳手移除1颗银色螺丝，移除电源板地线。  
![power_cables.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/power_cables.png)

### 步骤 8：断开连接线

将除 MC 板供电线和MC-AC 连接线以外的线缆从 MC 板上断开

![mc_cables.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/mc_cables.png)  
将穿过 XY 电机旁边通孔的线缆全部向上抽出。  
![ksnip_20260426-205308.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/ksnip_20260426-205308.png)

### 步骤 7：移除内衬

1. 使用 H2.0 内六角扳手移除 8 颗固定螺丝；

> 热床不能下降到最底部，不然编号为 5 的螺丝会被热麻滑块遮挡住，

![9_screws.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/9_screws.png)

2. 用扳手将右侧涂布了结构胶的位置松开；  
   ![press_to_unlock.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/press_to_unlock.png)
3. 在内衬上方将内衬向前门方向松出，然后可向您的右侧取出内衬。  
   ![loose_the_assy.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/loose_the_assy.png)  
   ![right_side.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/right_side.png)
4. 移除滤芯和电路板  
   从内衬的正面打开滤芯盖，取出滤芯；  
   ![filter_cover.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/filter_cover.png)  
   在内衬背面，用 H1.5 内六角扳手依次移除 MC 板的3 颗螺丝、 AC 板的2 颗螺丝 以及 电源板的 1 颗螺丝（银色），将电路板从内衬上移除。  
   ![pcbs.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/pcbs.png)

## 安装内衬

### 步骤 1：安装内衬

1. 安装电路板和滤芯

将电路板安装到内衬背面，用 H1.5 内六角扳手依次锁紧 MC 板的3 颗螺丝、 AC 板的2 颗螺丝 以及 电源板的 1 颗螺丝（银色）。  
![pcbs.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/pcbs.png)  
将滤芯安装到内衬正面，并合上滤芯盖。  
![filter_cover.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/filter_cover.png)

2. 将内衬从右侧移入打印机内侧，安装到原位，检查确认两侧的安装位置，不能在立柱的外面。  
   ![install.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/install.png)  
   ![check_position.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/check_position.png)
3. 锁紧 8 颗螺丝，固定内衬  
   ![9_screws.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/9_screws.png)

### 步骤 2：连接线缆

将 XY 电机旁边的线缆穿回到 MC 板侧，并连接到对应的连接器上。  
![pass_through_cables.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/pass_through_cables.png)

![mc_cables.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/mc_cables.png)

### 步骤 3：安装电源线和电源保护盖

将供电线连接到电源板和 AC 板上，用十字螺丝刀拧紧螺丝；将电源板地线用螺丝锁附到电源板上。  
![power_cables.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/power_cables.png)

安装电源保护盖，用 H1.5 内六角扳手锁紧 5 颗螺丝，将热床信号线和供电线分别连接到 MC 板和 AC 板上。  
![protective_cover.png](https://wiki.bambulab.com/x2d/maintenance/inner_lining/protective_cover.png)

### 步骤 4：安装左侧板和腔温加热组件

您可以参考[更换 X2D 左侧板](replace-left-side-panel.md)，来移安装左侧板。  
![014_lay_down_printer.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_left_side_panel/014_lay_down_printer.jpg)  
您可以参考[更换腔温加热组件](replace-chamber-heater-unit.md)，来安装腔温加热组件。  
![009_remove_chamber_unit.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/remove_chamber_heater_unit/009_remove_chamber_unit.png)

### 步骤 5：安装右侧板和自适应风道切换组件

您可以参考 [更换 X2D 右侧板](replace-right-side-panel.md) 来安装右侧板。  
![011_install_right_panel.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_right_side_panel/011_install_right_panel.jpg)  
您可以参考 [更换自适应风道切换组件](../../p2s/maintenance/replace-adaptive-airflow-switching-unit.md) 来安装自适应风道切换组件。  
![install_the_unit_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/install_the_unit_009.png)

### 步骤 6：安装前面盖和屏幕

您可以参考 [更换前面盖](replace-front-cover.md) 的内容，安装前面盖和屏幕。  
![009_pull_out_the_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_front_cover/009_pull_out_the_cable.png)

![015_install_the_screen.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_front_cover/015_install_the_screen.png)

### 步骤 7：安装 MC 板风扇

将 MC 风扇通过橡胶软钉固定到散热器上，并将插头连接到 MC 板上。  
![004_remove_mc_board_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/004_remove_mc_board_fan.png)

### 步骤 8：安装吐料组件和废料滑梯

您可以参考 [更 X2D 吐料组件](replace-purge-wiper.md) 来安装吐料组件。  
![003_lift_purge_wiper.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_purge_wiper/003_lift_purge_wiper.png)  
安装废料滑梯，使用 H1.5 内六角扳手锁入四颗固定螺丝（BT2x5）。  
![003_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/003_remove_purge_chute.jpg)

### 步骤 9. 安装背板、辅助挤出机、料管支架和缓冲器

您可以参考如下 Wiki 的份内容，依次进行安装。

- [更换背板](replace-rear-panel.md)
- [更换辅助挤出机](replace-auxiliary-extruder.md)
- [更换缓冲器](replace-filament-buffer.md)

## 如何验证成功

由于在更换过程中所需拆装的部件较多，请在更换后连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆连接是否正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
