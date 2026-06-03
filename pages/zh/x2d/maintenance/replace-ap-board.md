---
path: zh/x2d/maintenance/replace-ap-board
title: "更换 X2D AP 板"
description: "本文介绍了如何更换 X2D AP 板"
tags: []
created: 2026-04-14T13:08:24.256Z
updated: 2026-05-21T02:36:39.178Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-ap-board
---

## AP 板

AP 板的全称是应用处理器主板（Application Processor Main Board），它是打印机内处理信息交互的电路板。它为打印机提供了一个独立的操作环境，并支持打印机应用所需的所有系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。

## 适用打印机型号

X2D

## 何时更换

1. AP 板出现明显的物理损坏，如连接器损坏、元器件脱落或烧坏；
2. 经 Bambu Lab 技术支持分析需更换 AP 板。

## 所需要工具和材料

- 新的 AP 板
- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 视频教程

## 移除旧的 AP 板

### 步骤 1. 移除 AP 板盖螺丝

从打印机背后向上提起辅助挤出机，解锁辅助挤出机卡扣，然后将其取下，露出 AP 板盖固定螺丝。

|  |  |
| --- | --- |
|  |  |

用 H1.5 的螺丝刀取下 AP 板盖螺丝。  
![003_remove_ap_board_cover_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/003_remove_ap_board_cover_screws.png)

### 步骤 2. 移除 AP 板盖

移除上盖玻璃，从 AP 板盖的左侧，用手揭开 AP 板盖的检修端，  
![004_open_ap_board_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/004_open_ap_board_cover.png)

断开左 LED 灯的连接，  
![005_left_led_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/005_left_led_cable.png)

将整个 AP 板盖从框架上取下。  
![006_remove_ap_board_cover.webp](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/006_remove_ap_board_cover.webp)

### 步骤 3. 移除 AP 板

屏幕排线需先解开卡扣，再将排线断开；  
![007_screen_cable_clip.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/007_screen_cable_clip.png)

使用 H2.0 内六角扳手移除1颗螺丝，断开USB线连接，  
![008_remove_usbc_cable_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/008_remove_usbc_cable_screw.png)

将 AP 板上的所有连接线按压接头卡扣后断开连接，  
![009_remove_all_ap_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/009_remove_all_ap_cable.png)

使用 H2.0 内六角扳手移除四颗固定螺丝，然后将 AP 板取出。  
![010_ap_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/010_ap_board_screws.png)

使用镊子去除 Wi-Fi 天线接头上的有机硅胶，断开 Wi-Fi 天线，

|  |  |
| --- | --- |
|  |  |

## 安装新的 AP 板

### 步骤 1. 安装 AP 板

先将 Wi-Fi 天线安装在 AP 板上  
![012_install_wifi_antenna.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/012_install_wifi_antenna.png)

将新的 AP 板底部斜着放入，并对准横梁上的螺丝孔位，然后将 AP 板顶部也推入横梁中。  
![013_install_ap_board.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/013_install_ap_board.png)

使用 H2.0 内六角扳手拧紧四颗固定螺丝。  
![010_ap_board_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/010_ap_board_screws.png)

### 步骤 2. 连接 AP 板线缆

AP 板线缆说明如下：  
![014_ap_board_instruction.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/014_ap_board_instruction.png)

| 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 屏幕排线 | 4 | 实况摄像头 | 7 | LED 补光灯-左 | 10 | USB-C 线 |
| 2 | Wi-Fi 天线 | 5 | U 盘接口组件 | 8 | MC 板（通信） |  |  |
| 3 | 开门检测开关 | 6 | LED 补光灯-前 | 9 | MC 板（供电） |  |  |

根据连接器的说明，将线缆重新连接到 AP 板上。  
![009_remove_all_ap_cable.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/009_remove_all_ap_cable.png)

屏幕排线需要将线缆插入接头中，然后合上卡扣。  
![007_screen_cable_clip.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/007_screen_cable_clip.png)

连接USB线，使用 H2.0 内六角扳手锁入1颗螺丝，固定USB线扣  
![008_remove_usbc_cable_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/008_remove_usbc_cable_screw.png)

### 步骤 3. 安装 AP 板盖

沿着安装槽将AP板盖推到位（可使用内六角扳手确认螺丝孔对齐）  
![015_install_ap_board_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/015_install_ap_board_cover.png)

连接左LED，扣好检修端，

|  |  |
| --- | --- |
|  |  |

使用 H1.5 内六角扳锁紧背板的 2 颗 AP 板盖螺丝，  
![003_remove_ap_board_cover_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/003_remove_ap_board_cover_screws.png)

将辅助挤出机放置到位，并固定好卡扣。  
![002_lift_auxiliary_extruder.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/002_lift_auxiliary_extruder.png)

### 步骤 4. 绑定新序列号（SN）

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的 AP 板也将不能再被注册或绑定。

更换了 AP 板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换 AP 板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。  
![register_sn.jpg](https://wiki.bambulab.com/x2d/maintenance/ap-board/register_sn.jpg)

## 功能验证

连接电源，打开打印机，检查是否可以正常发起打印。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
