---
path: zh/p2s/maintenance/replace-heatbed
title: "更换 P2S 热床"
description: "本文介绍了如何更换 P2S 热床"
tags: []
created: 2025-10-14T12:55:26.370Z
updated: 2025-10-14T13:28:13.048Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-heatbed
---

## 热床

打印机的热床是安装在打印机腔体内，能沿 Z 方向上下运动并能根据设定温度进行加热的平台。设置合适的热床温度能有效提升模型与打印板的粘接力和防止模型翘边。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac164.jpg)  
**热床的备件包含以下：**

1. 热床 \* 1；
2. BT3x8 螺丝 - 用于固定热床 \* 7；
3. STW3.5x6 螺丝 - 用于固定地线 \* 1；
4. BT2x5 螺丝 - 用于固定走线压片 \* 4

## 何时更换

1. 热床损坏
2. 经 Bambu Lab 技术支持分析需更换热床

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除热床

### 步骤 1：移除背板

您可以参考这篇 Wiki 来移除背板：[更换背板 | Bambu Lab Wiki](replace-rear-panel.md)

### 步骤 2：移除左侧板

您可以参考这篇 Wiki 来移除左侧板：[更换左侧板 | Bambu Lab Wiki](replace-left-side-panel.md)

### 步骤 3：移除废料滑梯

使用 H1.5 内六角扳手移除四颗废料滑梯固定螺丝，将废料滑梯从打印机上取下。

![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 4：移除热床

1. 先从 MC 板上断开热床温度线，然后从 AC 板上断开三根热床供电线。在断开热床供电线时，需先按下接口处的卡扣解锁，然后即可拔出线缆；

![01_heated_bed_thermistor_cable_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/01_heated_bed_thermistor_cable_001.png)

![02_heated_bed_power_cable_connector_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/02_heated_bed_power_cable_connector_002.png)

2. 使用 H2.0 内六角扳手移除一颗地线固定螺丝（STW3.5x6），将地线从框架上取出，并将地线从线扣中取出；

![03_heated_bed_ground_wire_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/03_heated_bed_ground_wire_003.png)

![04_route_the_ground_wire_through_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/04_route_the_ground_wire_through_004.png)

![05_ground_wire_clip_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/05_ground_wire_clip_005.png)

3. 使用 H1.5 内六角扳手移除两颗电源保护盖上的走线压片螺丝（BT2x5），将走线压片取下。然后将热床线缆从电源保护盖上的线扣中穿过；

![23_ac_clamp_screw_023.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/23_ac_clamp_screw_023.png)

![06_route_through_ac_board_cover_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/06_route_through_ac_board_cover_006.png)

4. 使用 H1.5 内六角扳手移除 Z 滑块底面的两颗走线压片固定螺丝（BT2x5），将走线压片取出；

![07_heated_bed_bottom_clamp_screw_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/07_heated_bed_bottom_clamp_screw_007.png)

5. 使用 H2.0 内六角扳手移除七颗热床固定螺丝（BT3x5），将热床向上提起后侧放，然后将热床线缆从 Z 滑块中抽出，然后即可移除热床。

![12_full_view_of_heated_bed_screws_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/12_full_view_of_heated_bed_screws_012.png)

![14_remove_the_heated_bed_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/14_remove_the_heated_bed_014.png)

![15_pull_out_the_heated_bed_cable_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/15_pull_out_the_heated_bed_cable_015.png)

## 安装热床

### 步骤 1：安装热床

1. 将新的热床侧着放入打印机，将热床线缆依次穿过 Z 滑块。在穿线时可以先依次将三根热床供电线穿过 Z 滑块，然后将拉动热床线，再依次将热床地线和热床温度线从 Z 滑块中拉出；

![16_route_the_heated_bed_cable_1_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/16_route_the_heated_bed_cable_1_016.png)

![17_route_the_heated_bed_cable_2_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/17_route_the_heated_bed_cable_2_017.png)

![18_route_the_heated_bed_cable_3_018.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/18_route_the_heated_bed_cable_3_018.png)

2. 将热床放在 Z 滑块上，先使用 H2.0 内六角扳手将热床后方三颗螺丝（编号 1 - 3）拧紧。然后将前方四颗螺丝（编号 4 - 7）拧入，无需将螺丝完全拧紧，以便于后续调整热床位置；

![14_remove_the_heated_bed_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/14_remove_the_heated_bed_014.png)

![12_full_view_of_heated_bed_screws_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/12_full_view_of_heated_bed_screws_012.png)

3. 将 Z 滑块底部的线缆整理进线槽，将走线压片装入，使用 H1.5 内六角扳手拧紧两颗固定螺丝（BT2x5）；

![20_organize_the_cables_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/20_organize_the_cables_020.png)

![08_install_the_heated_bed_bottom_clamp_1_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/08_install_the_heated_bed_bottom_clamp_1_008.png)

![09_install_the_heated_bed_bottom_clamp_2_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/09_install_the_heated_bed_bottom_clamp_2_009.png)

4. 将热床线缆穿过电源保护盖上的护线盖，将地线穿过立柱，使用 H2.0 内六角扳手将地线固定在立柱上（STW3.5x6）；

![06_route_through_ac_board_cover_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/06_route_through_ac_board_cover_006.png)

![04_route_the_ground_wire_through_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/04_route_the_ground_wire_through_004.png)

![03_heated_bed_ground_wire_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/03_heated_bed_ground_wire_003.png)

![05_ground_wire_clip_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/05_ground_wire_clip_005.png)

5. 将热床线缆依次插入 AC 板和 MC 板，并将线缆卡入线槽中，将 AC 板盖上的走线压片装入，使用 H1.5 内六角扳手拧紧两颗固定螺丝（BT2x5）。

![21_connect_the_wires_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/21_connect_the_wires_021.png)

![22_ac_clamp_screw_022.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/22_ac_clamp_screw_022.png)

### 步骤 2：安装废料滑梯

将废料滑梯对准打印机上的螺丝孔位，使用 H1.5 内六角扳手依次拧紧四颗固定螺丝。

![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 3：安装左侧板

您可以参考这篇 Wiki 将左侧板重新装回：[更换左侧板 | Bambu Lab Wiki](replace-left-side-panel.md)

### 步骤 4：安装背板

> 在安装背板前，可以通过拉到Z同步带，将热床上升或下降至下图位置，以便利用底座结构卡住线缆，以保证线缆方向的一致性。  
> ![heatbed_cables.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/heatbed_cables.png)

然后您可以参考这篇 Wiki 将背板重新装回：[更换背板 | Bambu Lab Wiki](replace-rear-panel.md)

### 步骤 5：锁紧热床螺丝

1. 通过触摸屏选择"回中"，将热床温度升至 55℃ 并保持 5 分钟预热；

![](https://public-cdn.bblmw.com/wiki/new/p2s/troubleshooting/first-layer-printing-optimization-guide/image-1.png)

![](https://public-cdn.bblmw.com/wiki/new/p2s/troubleshooting/first-layer-printing-optimization-guide/image.png)

![](https://public-cdn.bblmw.com/wiki/new/p2s/troubleshooting/first-layer-printing-optimization-guide/image-2.png)

2. 使用 H2.0 内六角扳手拧紧前方的四颗螺丝（编号 4 - 7）。

![12_full_view_of_heated_bed_screws_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/12_full_view_of_heated_bed_screws_012.png)

### 步骤 6：手动调平热床

等待热床温度降低至室温后，您可以参考这篇 Wiki 来对热床进行手动调平：[P2S 热床手动调平 | Bambu Lab Wiki](manual-bed-tramming.md)

## 如何验证成功

连接电源，打开打印机，检查热床是否可以正常升温或温度是否显示正常。

如果您遇到任何问题，请先回溯您的步骤并检查热床的连接线是否连接正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
