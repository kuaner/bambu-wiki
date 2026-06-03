---
path: zh/a1-mini/maintenance/mc-board-replacement-guide
title: "A1 mini 主板更换指南"
description: "本指南详细介绍了如何卸下和安装A1 mini的主板。"
tags: ["a1 mini", "主板"]
created: 2024-05-24T09:32:38.525Z
updated: 2026-05-21T13:44:21.755Z
source: https://wiki.bambulab.com/zh/a1-mini/maintenance/mc-board-replacement-guide
---

![](https://wiki.bambulab.com/a1m/remove-mc-board/mc_board_a1m.jpeg)

## 何时使用本指南？

主板出现故障时使用本指南。主板故障引起的常见问题有：

- 打印机无法开机
- 主板损坏
- 拓竹技术支持建议更换

## 工具和材料

A1 mini 主板

- H2.0 六角扳手
- PH2 十字螺丝刀
- 30 分钟

### **安全警告**

> **重要提醒！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## A1 mini 主板接口示意图

![](https://wiki.bambulab.com/a1m/remove-mc-board/a1_mini_mainboard.png)

1. 工具头 USB-C 线缆
2. 屏幕
3. Y 电机
4. X 电机
5. Z 电机
6. Y 涡流传感器
7. 实况摄像头
8. 主板散热风扇
9. 主板供电
10. 热床供电
11. 热床信号线
12. AMS lite
13. SD 卡槽

## 移除旧主板

### 1. 移除打印机底部的盖子

以 Z 轴为接触点，将打印机侧放至桌子上。

然后，卸下固定底部盖子的 16 颗螺丝。移除盖子之后，可以看到主板的风扇。

请注意，15 和 16 号螺丝和其他螺丝不一样。在重新安装底盖时要记住。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/remove_bottom_cover_screws_for_a1_mini.jpeg)

卸下螺丝后，从右上方开始，绕着打印机轻轻撬动，直到底盖松动。

### 2. 移除主板风扇

卸下固定风扇的 2 颗螺丝。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/remove_a1_mini_mc_board_fan_screws.jpeg)

卸下螺丝后，将风扇轻轻拉向您的方向，找到风扇电缆的接头，轻轻将其拉动，断开电缆与主板的连接。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/disconnect_mc_fan_connector.jpeg)

### 3. 移除 USB-C 数据线支架并断开接头

如下图所示。支架用于将 USB-C 数据线固定在主板上。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/unscrew_the_usb_cable_bracket.jpeg)

卸下螺丝后，可以轻轻断开 USB-C 数据线。请确保向右拉，并不要将其弯曲，否则可能会损坏主板上的 USB-C 接口。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/remove_the_a1_mini_usb_cable.jpeg)

### 4. 断开 Wi-Fi 天线接头

将 Wi-Fi 天线线缆轻轻拉向您的方向。请格外小心，将其从主板上向上拉，避免损坏主板。

![](https://wiki.bambulab.com/a1m/replace-wifi-antenna/disconnect_the_wi-fi_antenna_connector.jpeg)

### 5. 断开触摸屏的排线

将固定排线的塑料夹子轻轻拉向你的方向，从而松开排线，使其可以被拉出。由于夹子很容易被损坏，所以请格外小心。

![](https://wiki.bambulab.com/a1m/replace-touchscreen/open_the_plastic_clip_of_the_ribbon_cable.jpeg)

### 6. 断开主板上的其他线缆

断开标号为 4 和 5 的电缆时，请格外小心。它们的底部有一个小夹子，取下时需要按住。

![](https://wiki.bambulab.com/a1m/remove-mc-board/disconnect_the_remaining_wires.jpeg)

### 7. 移除塑料电线盖

小心拧下固定塑料电线盖的 3 颗螺丝，可以看到电源端子。

请注意，3 号螺丝位于侧面。

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_plastic_wire_cover.jpeg)

### 8. 从电源上移除主板的电线

松开下图中所示的电源端子螺丝。只需将其拧松即可，**请勿将其完全卸下**，便于在接下来的步骤中将更容易将所有部件重新安装到位。

![](https://wiki.bambulab.com/a1m/remove-mc-board/remove_mc_board_wires_from_the_power_supply.jpeg)

### 9. 卸下主板螺丝并拉出主板

卸下固定主板的 3 颗螺丝，然后轻轻地将主板拉向您的方向将其取出。

![](https://wiki.bambulab.com/a1m/remove-mc-board/mc_board_a1_mini_screws.jpeg)

### 10. 从主板上移除热床电缆

电缆上有一个安全闩锁，用于将其固定，因此在拉动线缆时需要按住金属夹。

![](https://wiki.bambulab.com/a1m/remove-mc-board/remove_the_heatbed_wires_on_a1.jpeg)

此时可将主板移除。

## 安装新的主板

### 1. 安装新的主板

在开始操作前，请拍摄电路板背面的二维码，用于完成主板更换后的操作。

> 此二维码内容为整机 SN 序列号，用于更换主板之后注册设备。

![](https://wiki.bambulab.com/a1m/remove-mc-board/ap_board_a1_sn.jpeg)

用 3 颗螺丝将主板固定在框架上。

![](https://wiki.bambulab.com/a1m/remove-mc-board/mc_board_a1_mini_screws.jpeg)

### 2. 将热床电缆重新连接至主板

小心地将热床线缆重新连接到主板上。黑线在上，红线在下。将橡胶绝缘层推到热床线缆的连接器上，然后重新连接热敏电阻电缆。

![](https://wiki.bambulab.com/a1m/remove-mc-board/re-connect_the_heatbed_cable_wires.jpeg)

### 3. 连接主板电源端子线缆

如下图所示，小心地重新连接电源端子线缆并拧紧螺丝：   
1.  -V 主板线缆（黑）  
2. +V 主板线缆（红）

![](https://wiki.bambulab.com/a1m/remove-mc-board/mc_board_power_wires_on_a1_mini.jpeg)

> 重要提醒
>
> 如下图所示，连接所有线缆后，**确保线缆不会移动并固定到位**。

### 4. 安装固定塑料电线盖的螺丝

将热床电缆和电源电缆按图中所示排列，然后用 3 颗螺钉将塑料盖重新装回打印机。**请避免过度拧紧，以免损坏塑料螺纹**。

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_plastic_wire_cover.jpeg)

### 5. 重新连接其余电缆至主板

1. Z 轴电机

2. X 轴电机

3. Y 轴电机

4. Y 轴涡流线圈

5. 摄像头线缆

![](https://wiki.bambulab.com/a1m/remove-mc-board/disconnect_the_remaining_wires.jpeg)

### 6. 重新连接触摸屏的排线

轻轻地重新连接排线，确保白线与主板上标记的轮廓对齐。

然后，向右推动夹子将排线锁定到位。

![](https://wiki.bambulab.com/a1m/replace-touchscreen/re-install_the_ribbon_cable_of_the_screen.jpeg)

### 7. 重新连接 Wi-Fi 天线接头

轻轻地将圆形的 Wi-Fi 天线接头连接到主板上。操作时请格外小心，Wi-Fi 天线接头中间有一个非常小的针脚，如果未对齐，可能会损坏接头。

![](https://wiki.bambulab.com/a1m/replace-wifi-antenna/mc_board_wi-fi_connector.jpeg)

如果一切操作无误，Wi-Fi 天线的线缆将固定到位，如下图所示：

![](https://wiki.bambulab.com/a1m/replace-wifi-antenna/a1_mini_wi-fi_antenna.jpg)

### 8. 连接 USB-C 数据线并重新安装支架

小心地将 USB-C 数据线引向主板上的 USB-C 接头，然后按下图所示重新连接。然后，用之前卸下的螺丝重新安装金属支架。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/scr-20240131-lcue-2.jpeg)

### 9. 安装主板风扇

将风扇的接头连接至主板。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/disconnect_mc_fan_connector.jpeg)

然后，用 2 颗螺丝将风扇固定在主板散热片上。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/remove_a1_mini_mc_board_fan_screws.jpeg)

### 10. 将线缆排列整洁

如下图所示，在装回底盖之前，确保主板电线走线正确，以免干扰主板风扇。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/a1_mini_board_and_wire_managemet.jpg)

### 11. 安装底盖

首先拧紧 15 号 和 16 号螺丝，确保线槽环正确对准。然后，继续拧紧其余螺丝，同时确保不要拧得过紧。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/remove_bottom_cover_screws_for_a1_mini.jpeg)  
由于2025年新版主板风扇位置有所调整，旧版本 A1 mini 背板在安装时可能无法完全闭合。如下图所示，您需要手动剪除标示位置的部分，方可顺利合上背板。

![](https://wiki.bambulab.com/a1-mini/a1mini-replace-mc-board-fan/a1_mini_%E6%96%B0%E8%83%8C%E6%9D%BF%E4%BF%AE%E5%89%AA_1.jpg)

## 功能验证

为确保一切按预期运行，请打开打印机并执行回中程序尝试将各轴归位，并确认屏幕能正确显示温度。

如果一切正常，则说明主板安装步骤均正确。

### 根据电路板灯语判断

正常状态：MC板和AP板集成在主板上

#### 正常状态：MC板每5秒闪烁一次绿灯（该指示灯需要在特定的角度下观察）

<https://public-cdn.bblmw.com/wiki/video/A1M-MC.mp4>

#### 正常状态：AP板每秒闪烁一次绿灯

<https://public-cdn.bblmw.com/wiki/video/A1M-AP.mp4>

## 打印机 SN 码注册

请参考此篇 Wiki [自助完成 SN 码注册流程](../../general/find-sn.md)。

完成此步骤后，打印机将拥有新的序列号，您才能将其绑定到您的帐户。  
![](https://wiki.bambulab.com/a1m/remove-mc-board/ap_board_a1_sn.jpeg)

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的 AP 板也将不能再被注册或绑定。

更换了 AP 板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换 AP 板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。  
![register_sn.jpg](https://wiki.bambulab.com/x2d/maintenance/ap-board/register_sn.jpg)

## **操作后的校准步骤**

建议您在更换完主板后进行一次全面校准，以确保打印机顺畅运行。

## **潜在问题和解决方案**

如果您在安装新主板时遇到问题，请查阅以下列出的问题及其解决方案：

### 打印机无法开机

确认主板电源线安装正确，请参见\**步骤 3. 连接主板电源端子线缆*。\*

### 热床温度不显示或为0

检查\_步骤 2. 将热床电缆重新连接至主板\_中所示的热床电缆，确认绿色和白色线缆的接头已完全插入主板。

### 热床无法加热

检查\_步骤 2. 将热床电缆重新连接至主板\_中所示的热床电缆，确认红色和黑色线缆已完全插入主板。

### 其中一个轴无法正常工作

检查电机线缆是否正确安装，请参见\_步骤 5. 重新连接其余电缆至主板\_。

### 打印机无法连接至 Bambu Lab 帐户

新主板需要客户支持部门注册。因此，请向客户支持部门提供主板的二维码（位于主板的背面）并等待确认。

![](https://wiki.bambulab.com/a1m/remove-mc-board/ap_board_a1_sn.jpeg)

也可以参考[此wiki页面](../../general/find-sn.md)。

## A1 mini 主板连接口

![](https://wiki.bambulab.com/a1m/remove-mc-board/a1_mini_mainboard.png)

1. USB-C 到 TH 板接口
2. 触摸屏接口
3. Y 电机接口
4. X 电机接口
5. Z 电机接口
6. 涡流传感器接口
7. 摄像头接口
8. MC 板冷却风扇接口
9. 电源输入线
10. 热床电源输出接口
11. 热床信号电缆接口
12. AMS Lite 接口
13. SD 卡

## **结束语**

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
