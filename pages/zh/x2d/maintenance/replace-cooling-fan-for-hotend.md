---
path: zh/x2d/maintenance/replace-cooling-fan-for-hotend
title: "更换 X2D 热端风扇"
description: "本文介绍了如何更换 X2D 左热端风扇及右辅助热端风扇"
tags: []
created: 2026-04-14T13:08:34.275Z
updated: 2026-09-14T12:01:54.719Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-cooling-fan-for-hotend
---

## 热端风扇

X2D 搭配了两个热端，也配置了两个热端风扇。由于两个热端使用同样型号的风扇，但使用了不同的支架，我们在配件也只提供一个风扇，但赠送左右两个支架，需要根据实际更换的风扇选择对应的支架。

![001_hotend_cooling_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/001_hotend_cooling_fan.png)

## 适用打印机型号

X2D

## 何时更换

1. 热端风扇报错；
2. 热端风扇出现物理损坏；
3. 风扇异响

## 所需要工具和材料

H1.5 内六角螺丝刀

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 视频教程

## 移除旧的热端风扇

### **第 1 步 - 移除工具头外壳**

请参考 [更换工具头外壳](replace-toolhead-housing.md) 来移除工具头外壳。

![003_cooling_fan_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/003_cooling_fan_connector.png)

| 序号 | 1 | 2 |
| --- | --- | --- |
| 接口说明 | 右辅助热端风扇 | 左热端风扇 |

### 第 2 步：移除右辅助热端风扇;

将右辅助热端风扇线缆从TH板上断开，断开时，需沿**垂直于 TH 板的方向**发力，请勿向左右方向发力。

> **重要提醒**：线缆细小易损，操作时请轻缓用力。**请勿左右插拔、晃动或暴力拉拽该线缆。** 错误操作可能导致线缆端子脱出或连接器损坏。

![004_remove_right_fan_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/004_remove_right_fan_connector.png)

并将线缆从线槽里松出。  
![005_right_cable_tray.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/005_right_cable_tray.png)

用 H 1.5 内六角扳手拧松 2 颗风扇固定螺丝，使右侧热端风扇松脱  
![006_remove_right_cooling_fan_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/006_remove_right_cooling_fan_screws.png)

取下辅助热端风扇  
![007_pull_out_right_cooling_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/007_pull_out_right_cooling_fan.png)

### 第 3 步 移除左热端风扇

将左热端线缆从TH板上断开，并将线缆从线槽里松出。断开时，需沿**垂直于 TH 板的方向**发力，请勿向左右方向发力。

> **重要提醒**：线缆细小易损，操作时请轻缓用力。**请勿左右插拔、晃动或暴力拉拽该线缆。** 错误操作可能导致线缆端子脱出或连接器损坏。

![008_remove_left_fan_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/008_remove_left_fan_connector.png)

分别用H2.0 /H1.5 内六角扳手各移除1颗螺丝；  
![009_remove_left_fan_screw.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/009_remove_left_fan_screw.png)

注意要将左热端风扇的线从线槽中取出，  
![010_left_cable_tray.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/010_left_cable_tray.png)

取下左热端风扇。  
![011_pull_out_left_cooling_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/011_pull_out_left_cooling_fan.png)

## 安装新的热端风扇

### 第 1 步：安装右辅助热端风扇

将辅助热端风扇支架卡进实况摄像头的槽位中，  
![012_right_fan_position.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/012_right_fan_position.png)  
用H 1.5 内六角扳手拧紧 2 颗螺丝，固定风扇，固定好后用手轻轻摇动右辅助热端风扇，查看是否有松动，如有松动则需要检查螺丝是否锁紧。  
![006_remove_right_cooling_fan_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/006_remove_right_cooling_fan_screws.png)

如动图中整理好线缆，将线缆压在线槽下，并将右辅助热端风扇的接头连接到TH 板的辅助热端风扇接口上。  
![013_right_cable_cabling.webp](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/013_right_cable_cabling.webp)

### 第 2 步：安装左热端风扇

将左热端风扇安装到左热端加热组件左侧，注意线缆需要压在过线槽下  
![014_left_cable_tray.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/014_left_cable_tray.png)

用H1.5 内六角扳手锁入1颗固定螺丝固定风扇，用H2.0 内六角扳手锁入1颗螺丝，固定挤出机和风扇。  
![015_install_left_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/015_install_left_fan.png)

整理好线缆，并连接到TH 板的左热端风扇接口上。  
![016_install_left_fan.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_cooling_fan/016_install_left_fan.png)

### 第 3 步：安装**工具头外壳**

请参考 [更换工具头外壳](replace-toolhead-housing.md) 安装工具头外壳。

## 功能验证

1. 连接电源，打开打印机，将左热端升温到100℃，确认温度能正常升温，且热端风扇能正常启动。
2. 切换热端，将右辅助热端升温到100℃，确认温度能正常升温，且热端风扇能正常启动。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
