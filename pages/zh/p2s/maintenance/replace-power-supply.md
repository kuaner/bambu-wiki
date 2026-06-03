---
path: zh/p2s/maintenance/replace-power-supply
title: "更换 P2S 电源"
description: "本篇介绍了如何更换 P2S 电源"
tags: []
created: 2025-10-14T12:54:57.053Z
updated: 2026-03-31T10:00:32.095Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-power-supply
---

## 电源

P2S 打印机的电源是一个输入电压为 AC 100-240V 的交流电，转换为输出电压为 DC 24V 的直流电源的装置，它能为除热床以外的整台打印机提供稳定、干净且符合要求的直流电源。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac165.jpg)  
电源的备件包含如下：

1. 电源 \* 1
2. BT2x5 螺丝 \* 2

## 何时更换

1. 电源出现明显的物理损坏，如连接器损坏、元器件脱落或烧坏；
2. 经 Bambu Lab 技术支持确认需更换电源。

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除电源

### 步骤 1：移除料管支架、缓冲器和背板

您可以参考如下 Wiki 的拆解部份内容，依次移除料管支架、缓冲器和背板。  
[更换料管支架](replace-ptfe-tube-bracket.md)  
[更换缓冲器](replace-filament-buffer.md)  
[更换背板](replace-rear-panel.md)  
![rear_panel_removed_025.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/rear_panel_removed_025.png)

### 步骤 2：移除废料滑梯

使用 H1.5 内六角扳手移除四颗固定螺丝（BT2x5），然后将废料滑梯取下。  
![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 3：移除电源保护盖

使用 H1.5 内六角扳手移除两颗热床线压片固定螺丝（BT2x5），将压片取下。

![01_clamp_fixing_screw_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/01_clamp_fixing_screw_001.png)

使用 H1.5 内六角扳手依次移除五颗电源保护盖固定螺丝（BT2x5），然后将电源保护盖取下放置在一旁（热床线无需从电源盖中取出），以便于后续移除电源；

![03_ac_board_cover_fixing_screw_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/03_ac_board_cover_fixing_screw_003.png)  
![05_remove_the_ac_board_cover_2_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/05_remove_the_ac_board_cover_2_005.png)

将电源遮盖从右侧推动至左侧，然后即可将电源遮盖移除。

![06_remove_the_power_cover_1_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/06_remove_the_power_cover_1_006.png)  
![07_remove_the_power_cover_2_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/07_remove_the_power_cover_2_007.png)

### 步骤 4：移除电源

使用十字螺丝刀拧松电源线接口螺丝，将五根线缆依次从电源中取出。

![08_power_cable_connector_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/08_power_cable_connector_008.png)

![10_loosen_the_power_cable_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/10_loosen_the_power_cable_010.png)

使用 H2.0 内六角扳手移除两颗电源固定螺丝（BT2x5），然后即可将电源取出。

![11_power_supply_fixing_screw_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/11_power_supply_fixing_screw_011.png)

![12_remove_the_power_supply_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/12_remove_the_power_supply_012.png)

## 安装电源

### 步骤 1：安装电源

将电源模块装入内衬中，使用 H2.0 内六角扳手拧紧两颗固定螺丝（BT2x5）。  
**注意：底部的固定螺丝需要将地线一起固定**。

![13_install_the_power_supply_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/13_install_the_power_supply_013.png)

![11_power_supply_fixing_screw_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/11_power_supply_fixing_screw_011.png)

将五根线缆参考下图依次插入电源接口，从上往下颜色依次为：棕色（火线）、蓝色（零线）、黄绿色（地线）、黑色（24V 负极）、白色（24V 正极）。然后使用十字螺丝刀拧紧螺丝。在使用螺丝刀拧紧螺丝的时候可以用手扶住线缆，避免线缆松脱。

![08_power_cable_connector_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/08_power_cable_connector_008.png)

![16_tighten_the_power_cable_connector_screw_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/16_tighten_the_power_cable_connector_screw_016.png)

### 步骤 2：安装电源保护盖

先将电源遮盖装入电源的左侧，然后用手将电源盖推动至最右侧。

![17_install_the_power_cover_1_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/17_install_the_power_cover_1_017.png)

![18_install_the_power_cover_2_018.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/18_install_the_power_cover_2_018.png)

将电源线往电源一侧推动，将线缆靠近在电源一侧，然后将电源保护盖装入，将电源线缆从电源保护盖底部的凹槽中穿出，使用 H1.5 内六角扳手依次拧紧五颗螺丝（BT2x5）。

![20_cable_management_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/20_cable_management_020.png)  
![21_install_the_ac_board_cover_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/21_install_the_ac_board_cover_021.png)  
![03_ac_board_cover_fixing_screw_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/03_ac_board_cover_fixing_screw_003.png)

将热床线缆装入电源保护盖上的线槽，使用 H1.5 内六角扳手拧紧两颗压片固定螺丝（BT2x5）。

![01_clamp_fixing_screw_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/01_clamp_fixing_screw_001.png)

![02_remove_the_clamp_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-power-supply/02_remove_the_clamp_002.png)

### 步骤 3：安装废料滑梯

将废料滑梯对准打印机上的螺丝孔位，使用 H1.5 内六角扳手拧紧四颗固定螺丝（BT2x5）。  
![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 4：安装背板

您可以参考如下 Wiki 的安装部份内容，依次安装背板、缓冲器和料管支架。  
[更换背板](replace-rear-panel.md)  
[更换缓冲器](replace-filament-buffer.md)  
[更换料管支架](replace-ptfe-tube-bracket.md)

## 如何验证成功

连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆是否连接正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
