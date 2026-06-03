---
path: zh/a1/maintenance/th-board-replacement-guide
title: "更换挤出主板-A1"
description: "本指南介绍如何更换 A1系列打印机上的挤出主板。"
tags: ["a1", "a1 mini", "挤出主板"]
created: 2024-04-25T03:21:02.371Z
updated: 2026-01-20T09:09:32.907Z
source: https://wiki.bambulab.com/zh/a1/maintenance/th-board-replacement-guide
---

## 挤出主板-A1

![](https://wiki.bambulab.com/a1m/replace-th-board/a1_mini_th_board.jpg)

> 注意：新挤出主板上缺少两个接线柱（红圈处），仅剩焊盘。
>
> ![](https://wiki.bambulab.com/a1/maintenance/toolhead-board/20250123-153719.jpg)

## 何时使用？

可能需要更换A1打印机挤出主板的常见问题包括：

- 热床平整性存在问题，喷嘴无法准确执行归位程序
- 挤出机电机未按预期转动，可能是由于步进电机驱动故障
- USB-C数据线损坏
- 进料霍尔板连接器损坏
- 热端加热片和NTC损坏
- 拓竹技术支持推荐更换

## 工具

- 新的 A1 挤出主板
- H2.0 内六角扳手
- H1.5 内六角扳手
- 15 分钟时间

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除旧版的挤出主板

### 1. 移除工具头后盖

请按照下面所示的方法，小心地向外拉动后盖的底部，轻轻地撬开背盖。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_back_cover.jpeg)

### 2. 从打印头上取下 **USB-C 数据线**

用 H1.5 内六角扳手拆下 A1 工具头上固定 USB-C 数据线的四颗螺钉，然后向上移除 USB-C 数据线。

![](https://wiki.bambulab.com/a1/maintenance/toolhead-board/remove_the_usb_c_cable_of_a1.jpeg)

### 3. 移除挤出主板螺丝

卸下固定挤出主板的 3 颗黑色螺丝。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_th_board_screws.jpeg)

### 4. 断开连接线

移除连接到工具头板的四根电缆。小心地从接头处拔出它们，避免将电线从接头处直接拉出。建议使用扁平工具轻轻撬出，以避免潜在的损坏。

![](https://wiki.bambulab.com/a1m/replace-th-board/disconnect_the_th_board_cables.jpeg)

移除两颗螺丝，取下涡流传感器的导线。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_eddy_sensor_screws.jpeg)

### 5. 移除挤出主板

现在您可以取出挤出主板。

打开固定电缆的卡扣，然后断开电缆。

取出时应小心地慢慢向上拉直，避免晃动电缆，以免造成损坏。

如果它损坏了，您可以在[这里](https://detail.tmall.com/item.htm?abbucket=8&id=742413890652&rn=fdccba1f0182bc3695d538e65c3b3337&spm=a1z10.3-b-s.w4011-25177047232.53.1e811c79Wuo3TI&skuId=5118758836326)购买。

![a1_霍尔板线座.webp](https://wiki.bambulab.com/a1/troubleshooting/hms/1200_4500_0002_0003/a1_%E9%9C%8D%E5%B0%94%E6%9D%BF%E7%BA%BF%E5%BA%A7.webp)

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_filament_sensor_ribbon_cable.jpeg)

## 安装新的挤出主板

### 1. 将挤出主板安装到中框上

安装新的挤出主板时，请先连接进料霍尔板线缆。

在插入排线前，请**扣开插座卡扣**。插座上的卡扣用于固定排线，需要先**轻轻掀开卡扣**，再将排线完全插入插槽，最后按下卡扣将排线锁紧，确保连接稳固。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_filament_sensor_ribbon_cable.jpeg)

如下图所示，小心地将挤出机电机线放在进料霍尔板线缆旁边。  
完成此步骤后，可将工具头板轻轻推回原位。

![](https://wiki.bambulab.com/a1m/replace-th-board/extruder_motor_wiring_on_th_board.jpeg)

### 2.安装挤出主板螺丝

使用三个黑色螺丝固定挤出主板。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_th_board_screws.jpeg)

> 重要提醒！
>
> 请勿过度拧紧螺丝，以免造成任何潜在损坏。

### 3. 重新连接所有线缆

将新的挤出主板放回原位后，可以重新连接所有线缆，如下图所示。

1. 热端加热组件（购买链接： [京东](https://item.jd.com/10086621431814.html)  [天猫](https://detail.tmall.com/item.htm?abbucket=8&id=742608647813&rn=fdccba1f0182bc3695d538e65c3b3337&spm=a1z10.3-b-s.w4011-25177047232.49.1e811c79Wuo3TI&skuId=5293816695460)）
2. 挤出电机
3. 热端散热风扇（购买链接： [京东](https://item.jd.com/10085237113101.html)  [天猫](https://detail.tmall.com/item.htm?abbucket=8&id=742494478597&rn=0cbc7157e9197dbc00e4d97c530cb9f8&spm=a1z10.5-b-s.w4011-25176969463.19.52195a64wKqcmi&skuId=5122905509690)）
4. 部件冷却风扇（购买链接： [京东](https://item.jd.com/10085237672213.html)  [天猫](https://detail.tmall.com/item.htm?abbucket=8&id=742158008755&rn=1dd6f08b194f87e54f0516a6e019a3f4&spm=a1z10.3-b-s.w4011-25177047232.221.1e2d1c79jLk20p&skuId=5122266397335)）
5. 涡流线圈

![](https://wiki.bambulab.com/a1m/replace-th-board/th_board_cables_on_a1.jpeg)

### 4.重新连接 USB-C 数据线

使用第一步中卸下的四颗螺丝重新安装 USB-C数据线，同时注意方向。

![](https://wiki.bambulab.com/a1/maintenance/toolhead-board/usb_c_a1.jpeg)

> **重要提醒!**
>
> 不要过度拧紧这些螺丝，以免造成滑丝。
>
> 注意 USB-C数据线的方向和背面对齐的小凹槽。
>
> ![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/usb_cable_orientation.jpeg)

### 5. 安装工具头后盖

将后盖上的两个支架朝上对齐，然后推动后盖，直到听到几声咔哒声。

![](https://wiki.bambulab.com/a1m/replace-th-board/install-back-cover.png)

## 如何验证成功

### 根据电路板灯语判断

**正常状态：TH板指示灯常亮绿灯**

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_back_cover.jpeg)

如图所示，拉住后盖底部，小心撬开后盖。

<https://public-cdn.bblmw.com/wiki/video/A1M-TH.mp4>

## 操作后的校准步骤

建议在完成更换后，对打印机进行校准操作。

## 潜在问题和解决方案

如果在安装新挤出主板时遇到问题，请检查以下列出的潜在问题和解决方案：

### 热端温度为0

检查热端加热组件连接器，确认其正确插入，如步骤 3 ，重新连接所有线缆。  
请确保所有线缆跟挤出主板对齐。  
如果问题仍然存在，则热敏电阻导线可能已损坏（白色导线）。

### 热端无法加热

检查热端加热组件连接器，确认其正确插入，如步骤 3 ，重新连接所有线缆。  
请确保所有线缆跟挤出主板对齐。  
如果问题仍然存在，加热器电线可能已损坏（半透明电线）。

### 打印机无法回中

检查涡流线圈（5 和 6），确认它们已正确安装在挤出主板背面，如步骤 3 ，重新连接所有线缆。

### 进料霍尔板不工作

如步骤 1 将挤出主板安装到中框上所示，检查进料霍尔板线缆并确认其正确安装在挤出主板的背面。将挤出主板安装到中框上。  
如果进料霍尔板线缆损坏，则需要更换进料霍尔板。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
