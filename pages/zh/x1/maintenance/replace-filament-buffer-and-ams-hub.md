---
path: zh/x1/maintenance/replace-filament-buffer-and-ams-hub
title: "更换 X1/P1 系列的供料缓冲器与料线选通器（AMS Hub）"
description: "本文将详细为您介绍 X1/P1 系列更换供料缓冲器与料线选通器（AMS Hub）的详细步骤和注意事项。"
tags: []
created: 2026-05-09T10:11:05.892Z
updated: 2026-05-14T08:31:10.265Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-filament-buffer-and-ams-hub
---

## 供料缓冲器与料线选通器

**供料缓冲器**位于**打印机的背面**，连接 **AMS 和工具头挤出机**，由滑块、弹簧和霍尔传感器组成。AMS 将耗材推入工具头挤出机时，由于耗材的压力，滑块向前移动，通过霍尔传感器检测滑块移动的位置，供料缓冲器将信号反馈回 AMS 和打印机。通过控制 AMS 的进给速度，可以确保耗材张力在设计范围内，这样工具头挤出机就可以轻松而精确地工作。

![filament_buffer.png](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/filament_buffer.png)

**料线选通器**，也称 AMS Hub。可以替代供料缓冲器。 供料缓冲器能够连接一个 AMS，而料线选通器最多可以连接**四个 AMS** ，实现 **16 色打印**。 料线选通器由耗材选择模块和缓冲模块组成。 耗材选择模块有四个入口连接到四个独立的 AMS，每个插槽都有一个霍尔传感器来检测耗材。其缓冲模块的功能与供料缓冲器的相同，由滑块、弹簧和霍尔传感器构成，确保耗材张力在设计范围内工作。

![ams_hub.png](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/ams_hub.png)

**供料缓冲器购买链接**： [京东](https://item.jd.com/10060212416887.html) ; [天猫](https://detail.tmall.com/item.htm?abbucket=8&id=694049363219&rn=3f1570182437f0b131adfd3122648cc0&spm=a1z10.3-b-s.w4011-25177047232.22.42c01c79unkjoE&skuId=4927623665956)

**料线选通器（AMS Hub）购买链接**： [京东](https://item.jd.com/10059378244689.html)

## 适用打印机型号

X1 / P1 系列

## 所需要的工具和材料

- H2.0 内六角扳手
- 供料缓冲器 / 料线选通器

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 更换供料缓冲器

### 移除供料缓冲器

**步骤1.** 移除供料缓冲器上的两颗螺丝，然后将供料缓冲器拆下。

![screws_on_buffer_(2).png](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/screws_on_buffer_(2).png)

**步骤2.** 按紧线缆接口的底端，分别断开 4-pin 连接线和 6-pin 连接线。

![](https://wiki.bambulab.com/ams/packing--guide/2.remove_cables2.jpg)

**步骤3.** 按压黑色气动接头垫圈，拔出第一根铁氟龙料管。

![](https://wiki.bambulab.com/ams/packing--guide/2.remove_tube1.png)

使用镊子按压黑色气动接头垫圈，拔出第二根铁氟龙料管。

![](https://wiki.bambulab.com/ams/packing--guide/2.remove_tube2.png)

### 安装供料缓冲器

**步骤1.** 将铁氟龙料管插入供料缓冲器两侧。

![tubes_insert_buffer.jpg](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/tubes_insert_buffer.jpg)

**步骤2.** 将供料缓冲器放在安装位置，拧入两颗螺丝来固定。

![screws_on_buffer_(2).png](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/screws_on_buffer_(2).png)

**步骤3.** 用 4-pin 连接线，连接打印机与供料缓冲器；再用 6-pin 连接线，连接 AMS 与供料缓冲器。

![buffer_complete.jpg](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/buffer_complete.jpg)

## 更换料线选通器

### 视频指南

### 移除料线选通器

**步骤1.** 按紧线缆接口的底端，分别断开 4-pin 连接线和 6-pin 连接线。

![connect_cable_to_hub.jpg](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/connect_cable_to_hub.jpg)

**步骤2.** 移除料线选通器上的两颗螺丝。然后即可取下料线选通器

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/remove_and_install_screws_on_hub.jpg)

**步骤3.** 使用镊子，按压料线选通器气动接头，拔出料管。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/disconnect-ptfe-on_ams_hub.jpg)

动图示意：

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/disconnect-ptfe-on_ams_hub.webp)

另一侧的料管同理。

![disconnect-right_ptfe-on_ams_hub.jpg](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/disconnect-right_ptfe-on_ams_hub.jpg)

### 安装料线选通器

**步骤1.** 将铁氟龙料管插入下图所示位置，确保插入到位。

![insert_into_hub_right.jpg](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/insert_into_hub_right.jpg)

**步骤2.** 将料线选通器放在安装位置，拧入两颗螺丝来固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/remove_and_install_screws_on_hub.jpg)

请确保铁氟龙料管从料盘支架下方穿过，而不是上方，如下图所示。

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/avoid_ptfe_from_touching_spool_holder.png.jpg)

**步骤3.** 用 4-pin 连接线，连接打印机与料线选通器；再用一根 6-pin 连接线，连接最常用的 AMS 与料线选通器。然后使用 6-pin 连接线将剩余的 AMS 串联。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/connect_cable_to_hub.jpg)

线缆连接示意图：

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/hub_cables_setup.jpg)

**步骤4.** 插入左侧铁氟龙料管。

![connect_tube_to_hub.jpg](https://wiki.bambulab.com/x1/maintenance/replace-filament-buffer-and-ams-hub/connect_tube_to_hub.jpg)

安装完成。

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/multi_ams_and_hub_connect.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
