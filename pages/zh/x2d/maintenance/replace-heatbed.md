---
path: zh/x2d/maintenance/replace-heatbed
title: "更换 X2D 热床"
description: "本文介绍了如何更换 X2D 的热床"
tags: []
created: 2026-04-14T13:09:47.971Z
updated: 2026-04-14T13:09:49.013Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-heatbed
---

## 热床

打印机的热床是安装在打印机腔体内，能沿 Z 方向上下运动并能根据设定温度进行加热的平台。设置合适的热床温度能有效提升模型与打印板的粘接力和防止模型翘边。

**热床的备件包含以下：**

1. 热床 \* 1；
2. BT3x8 螺丝 - 用于固定热床 \* 7；
3. STW3.5x6 螺丝 - 用于固定地线 \* 1；
4. BT2x5 螺丝 - 用于固定走线压片 \* 4  
   ![fac219.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/fac219.png)

## 适用打印机型号

X2D

## 何时更换

1. 热床损坏
2. 经 Bambu Lab 技术支持分析需更换热床

## 所需要的工具和材料

- 新的热床
- H1.5 内六角扳手
- H2.0 内六角扳手

> 拔除热床的供电线时，请务必先解除锁扣的锁定。可以直接按压图示位置，然后向外拔出插头。**（移除胶套的照片是为了更清楚地展示要按压解锁的位置）**![disconnect-plug.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_heatbed/disconnect-plug.png)

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除旧的热床

### 步骤 1. 移除背板

您可以参考[更换 X2D 背板](replace-rear-panel.md)来移除背板。

### 步骤 2. 移除左侧板

您可以参考[更换 X2D 左侧板](replace-left-side-panel.md)这篇 Wiki 来移除左侧板。

### 步骤 3. 移除废料滑梯

使用 H1.5 内六角扳手移除四颗废料滑梯固定螺丝，将废料滑梯从打印机上取下。  
![002_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/002_remove_purge_chute.jpg)

### 步骤 4. 移除热床

先从 MC 板上断开热床温度传感器线缆。  
![003_mc_heatbed_cable.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/003_mc_heatbed_cable.jpg)

然后从 AC 板上断开热床供电线。注意在断开热床供电线时，需先按下接口处的卡扣解锁，然后才能拔出线缆。

|  |  |
| --- | --- |
| 高压版 | 低压版 |

使用 H2.0 内六角扳手移除一颗地线固定螺丝（STW3.5x6），将地线从框架上取出，

|  |  |
| --- | --- |
|  |  |

并将地线从线扣中取出；  
![006_ground_wire_clip.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/006_ground_wire_clip.png)

使用 H1.5 内六角扳手移除两颗电源保护盖上的走线压片螺丝（BT2x5），将走线压片取下。然后将热床线缆从电源保护盖上的线扣中穿过；

|  |  |
| --- | --- |
|  |  |

使用 H1.5 内六角扳手移除 Z 滑块底面的两颗走线压片固定螺丝（BT2x5），将走线压片取出；  
![008_heated_bed_bottom_clamp_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/008_heated_bed_bottom_clamp_screw.png)

使用 H2.0 内六角扳手移除七颗热床固定螺丝（BT3x5），  
![009_full_view_of_heated_bed_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/009_full_view_of_heated_bed_screws.png)

将热床向上提起后侧放，然后将热床线缆从 Z 滑块中抽出，然后即可移除热床。

|  |  |
| --- | --- |
|  |  |

## 安装新的热床

### 步骤 1. 安装热床

将新的热床侧着放入打印机，将热床线缆依次穿过 Z 滑块。  
![011_route_the_heated_bed_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/011_route_the_heated_bed_cable.png)

在穿线时可以先依次将三根热床供电线穿过 Z 滑块，然后将拉动热床线，再依次将热床地线和热床温度线从 Z 滑块中拉出；

|  |  |
| --- | --- |
|  |  |

将热床放在 Z 滑块上，先使用 H2.0 内六角扳手将热床后方三颗螺丝（编号 1 - 3）拧紧。然后将前方四颗螺丝（编号 4 - 7）拧入，无需将螺丝完全拧紧，以便于后续调整热床位置；

|  |  |
| --- | --- |
|  |  |

将 Z 滑块底部的线缆整理进线槽，安装走线压片，  
![013_organize_the_cables.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/013_organize_the_cables.png)

使用 H1.5 内六角扳手拧紧两颗固定螺丝（BT2x5）；

|  |  |
| --- | --- |
|  |  |

将热床线缆穿过电源保护盖上的护线盖，  
![007_route_through_ac_board_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/007_route_through_ac_board_cover.png)

将地线穿过立柱，使用 H2.0 内六角扳手将地线用螺丝（STW3.5x6）锁附到立柱上。

|  |  |
| --- | --- |
|  |  |

然后将地线整理到线扣中安；  
![006_ground_wire_clip.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/006_ground_wire_clip.png)

将热床供电线缆按图所示，连接到 AC 板的连接器上；

|  |  |
| --- | --- |
| 高压版 | 低压版 |

将热床线缆连接到 MC 板上。  
![003_mc_heatbed_cable.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/003_mc_heatbed_cable.jpg)

将线缆整理好，卡入线槽中，安装走线压片，使用 H1.5 内六角扳手拧紧两颗固定螺丝（BT2x5）。  
![007_power_cover_clip.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/007_power_cover_clip.jpg)

### 步骤 2. 安装废料滑梯

将废料滑梯对准打印机上的螺丝孔位，使用 H1.5 内六角扳手依次拧紧四颗固定螺丝。  
![002_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/002_remove_purge_chute.jpg)

### 步骤 3. 安装左侧板

您可以参考[更换 X2D 左侧板](replace-left-side-panel.md)这篇 Wiki 来安装左侧板。

### 步骤 4. 安装背板

> 在安装背板前，可以通过拉到Z同步带，将热床上升或下降至下图位置，以便利用底座结构卡住线缆，以保证线缆方向的一致性。  
> ![015_heatbed_cables.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/015_heatbed_cables.png)

然后参考[更换 X2D 背板](replace-rear-panel.md)来安装背板。

### 步骤 5. 锁紧热床螺丝

通过触摸屏选择"回中"，将热床温度升至 55℃ 并保持 5 分钟预热；  
![016_homing.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/016_homing.png)

![017_heating.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/017_heating.png)

![018_heatbed_temperture.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/018_heatbed_temperture.png)

使用 H2.0 内六角扳手拧紧前方的四颗螺丝（编号 4 - 7）。  
![009_full_view_of_heated_bed_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-heatbed/009_full_view_of_heated_bed_screws.png)

## 功能验证

连接电源，打开打印机，确认热床否可以正常升温且温度显示正常。

如果您遇到任何问题，请先回溯您的步骤并检查热床的连接线是否连接正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
