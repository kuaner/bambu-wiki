---
path: zh/p2s/maintenance/replace-power-switch-assembly
title: "更换 P2S/X2D  电源开关插座"
description: "本文介绍了如何更换 P2S/X2D  电源开关插座"
tags: []
created: 2025-10-14T12:55:03.474Z
updated: 2026-04-30T04:13:22.060Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-power-switch-assembly
---

## 电源开关插座

电源开关插座是安装在打印机背面的电源线插座，它包含一个电源线插座、一个控制打印机电源的开关以及用于连接打印机电源、交流电板和地线的线缆。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac166.jpg)  
电源开关插座的备件包含：

1. 电源开关插座 \* 1；
2. STW3.5x6 螺丝 \* 1

## 何时更换

1. 电源开关插座损坏

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除电源开关插座

### 步骤 1：移除料管支架、缓冲器和背板

您可以参考如下 Wiki 移除料管支架。  
[更换料管支架](replace-ptfe-tube-bracket.md)

参考对应 Wiki 来移除缓冲器：

- [P2S](replace-filament-buffer.md)
- [X2D](../../x2d/maintenance/replace-filament-buffer.md)

| filament_buffer_001.png | filament_buffer.jpg |
| --- | --- |
| P2S | X2D |

参考对应 Wiki 来移除打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

### 步骤 2：移除废料滑梯

使用 H1.5 内六角扳手移除四颗固定螺丝（BT2x5），然后将废料滑梯取下。  
![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 3：移除电源保护盖

使用 H1.5 内六角扳手移除两颗热床线压片固定螺丝（BT2x5），将压片取下。

![01_clamp_fixing_screw_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/01_clamp_fixing_screw_001.png)

使用 H1.5 内六角扳手依次移除五颗 AC 板盖固定螺丝（BT2x5），然后将 AC 板盖取下放置在一旁（热床线无需从电源盖中取出），以便于后续移除电源；

![03_ac_board_cover_fixing_screw_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/03_ac_board_cover_fixing_screw_003.png)  
![05_remove_the_ac_board_cover_2_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/05_remove_the_ac_board_cover_2_005.png)

### 步骤 4：移除左侧板

请参考以下wiki 的内容移除左侧板。  
[更换左侧板](replace-left-side-panel.md)

![take_the_panel_back011.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-left-side-panel/take_the_panel_back011.jpg)

### 步骤 5：移除电源开关插座

使用十字螺丝刀分别拧松 AC 板和电源上的螺丝，将线缆抽出。

![01_ac_board_power_cable_connector_1_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/01_ac_board_power_cable_connector_1_001.png)

![03_power_supply_connector_1_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/03_power_supply_connector_1_003.png)

![04_power_supply_connector_2_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/04_power_supply_connector_2_004.png)

使用 H2.0 内六角扳手移除一颗地线固定螺丝（STW3.5x6），松出地线。

![05_grounding_screw_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/05_grounding_screw_005.png)

![06_ground_wire_passes_through_the_column_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/06_ground_wire_passes_through_the_column_006.png)

揭下电缆束线胶带，从右向左将线缆从线扣中取出。

![08_cable_clip_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/08_cable_clip_008.png)

![09_ground_wire_clip_diagram_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/09_ground_wire_clip_diagram_009.png)

![10_peel_off_the_tape_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/10_peel_off_the_tape_010.png)

![11_remove_the_tape_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/11_remove_the_tape_011.png)

使用扁平工具从电源开关座两侧框架上的四个开口处翘松4个卡扣，随后即可将将电源开关座松出。

![12_pry_open_the_switch_1_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/12_pry_open_the_switch_1_012.png)

![13_pry_open_the_switch_2_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/13_pry_open_the_switch_2_013.png)

![14_remove_the_switch_1_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/14_remove_the_switch_1_014.png)

![15_remove_the_switch_2_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/15_remove_the_switch_2_015.png)

## 安装电源开关插座

### 步骤 1：安装电源开关插座

将新的电源开关座所有缆线穿过电源开关座框架后向内推，将电源开关座通过卡扣固定到位；

![16_reinstall_the_switch_1_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/16_reinstall_the_switch_1_016.png)

![17_reinstall_the_switch_2_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/17_reinstall_the_switch_2_017.png)

将线缆从左往右依次卡入线扣中，并贴上胶布。

![11_remove_the_tape_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/11_remove_the_tape_011.png)

![10_peel_off_the_tape_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/10_peel_off_the_tape_010.png)

![09_ground_wire_clip_diagram_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/09_ground_wire_clip_diagram_009.png)

![08_cable_clip_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/08_cable_clip_008.png)

将地线穿过立柱，使用 H2.0 内六角扳手拧紧螺丝（STW3.5x6），将地线固定在横梁上；

![07_reinstall_the_ground_wire_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/07_reinstall_the_ground_wire_007.png)

![05_grounding_screw_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/05_grounding_screw_005.png)

将线缆插入 AC 板和电源，并使用十字螺丝刀拧紧螺丝。

![18_connect_the_wires_018.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-switch-assembly/18_connect_the_wires_018.png)

### 步骤 2：安装左侧板

请参考以下wiki 的内容安装左侧板。  
[更换左侧板](replace-left-side-panel.md)

### 步骤 3：安装电源保护盖

整理电源线缆，装线缆压入电源与内衬的间隙，然后安装电源保护盖，注意需要将电源线缆从盖底部的凹槽中穿出，使用 H1.5 内六角扳手依次拧紧五颗螺丝（BT2x5）。

![20_cable_management_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/20_cable_management_020.png)

![21_install_the_ac_board_cover_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/21_install_the_ac_board_cover_021.png)

![03_ac_board_cover_fixing_screw_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/03_ac_board_cover_fixing_screw_003.png)

将热床线缆装入 AC 板盖上的线槽，使用 H1.5 内六角扳手拧紧两颗压片固定螺丝（BT2x5）。

![01_clamp_fixing_screw_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/01_clamp_fixing_screw_001.png)

![02_remove_the_clamp_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/02_remove_the_clamp_002.png)

### 步骤 4：安装废料滑梯

将废料滑梯对准打印机上的螺丝孔位，使用 H1.5 内六角扳手拧紧四颗固定螺丝（BT2x5）。  
![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 5：安装背板

您可以参考对应 Wiki 来安装打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

参考对应 Wiki 来安装缓冲器：

- [P2S](replace-filament-buffer.md)
- [X2D](../../x2d/maintenance/replace-filament-buffer.md)

| filament_buffer_001.png | filament_buffer.jpg |
| --- | --- |
| P2S | X2D |

参考如下 Wiki 安装料管支架。  
[更换料管支架](replace-ptfe-tube-bracket.md)

## 如何验证成功

连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆是否连接正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
