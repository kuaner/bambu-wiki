---
path: zh/ams3/maintenance/replace-feed-selector-motor
title: "AMS 送料选择器电机更换指南"
description: ""
tags: []
created: 2026-11-03T13:25:35.535Z
updated: 2026-11-03T13:25:36.583Z
source: https://wiki.bambulab.com/zh/ams3/maintenance/replace-feed-selector-motor
---

## 简介

![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/99_ams_____________ams_3h_feed_selector_motor_replacement_guide_d16c8e9d7d.jpg)

## 何时更换

- AMS 送料选择器电机报错。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 重要提醒! 在对 AMS 及其内部电子设备进行任何维护工作之前，请关闭 AMS 及打印机电源，并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。拆装过程中请避免暴力操作，防止造成零部件或连接结构的二次损伤。拆除部件前，请妥善保管拆除的固定螺丝，以免丢失。

## 拆装提示

> 本指南是在已移除 AMS 3H 舱体的情况下操作的，请参考WIKI: [AMS 3H 舱体拆装指南](../../h3c/maintenance/replace-chamber.md)，完成将 AMS 舱体从 AMS 支架上移除和安装的操作。

## 移除 AMS 送料选择器电机

### 第 1 步 移除 AMS 进料组件上盖

请参考 WIKI: [AMS 上下料组件上盖更换指南](replace-auto-filament-loader-cover.md)，移除 AMS 上下料组件上盖。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/10_ams_3h____________ams_3h_auto_filament_loader_replacement_guide_15119abbe1.jpg)

### 第 2 步 移除送料选择器电机螺丝

用 H1.5 内六角扳手移除 3 颗螺丝  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/52_ams___________ams_3h_feed_selector_replacement_guide_4aac27bc66.jpg)

将电机及其外壳从进料组件上分离  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/99_ams_____________ams_3h_feed_selector_motor_replacement_guide_79c5825a55.jpg)

> 如果不需要更换连接线缆，可以在这个时候直接断开连接线缆，移除电机。后续安装时，记得插回电机插头。  
> ![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/99_ams_____________ams_3h_feed_selector_motor_replacement_guide_0beb26368a.jpg)

### 第 3 步 移除 AMS 送料选择器电机连接线

翻转 AMS 使其底部朝上，用 H1.5 内六角扳手移除 4 颗螺丝，取下 AMS 主板装饰盖。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/51_ams_3h_____________ams_3h_air_inlet_unit_replacement_guide_1346e88e7d.jpg)

断开电机线连接，从 AMS 内侧移除送料选择器电机。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/99_ams_____________ams_3h_feed_selector_motor_replacement_guide_28d44a3278.jpg)

## 安装 AMS 送料选择器电机

### 第 1 步 安装送料选择器电机

将电机线缆穿过过线孔，然后将电机安装到齿轮所在位置，确认螺丝孔对齐。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/99_ams_____________ams_3h_feed_selector_motor_replacement_guide_15645260a2.jpg)

锁入 3 颗螺丝将电机固定  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/52_ams___________ams_3h_feed_selector_replacement_guide_4aac27bc66.jpg)

### 第 2 步 将电机连接到 AMS 主板

翻转 AMS 使其底部朝上，将送料选择器电机线缆连接到 AMS 主板的连接器上，整理好线缆。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/99_ams_____________ams_3h_feed_selector_motor_replacement_guide_28d44a3278.jpg)

安装主板装饰盖，锁入 4 颗螺丝固定。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/51_ams_3h_____________ams_3h_air_inlet_unit_replacement_guide_1346e88e7d.jpg)

### 第 3 步 安装 AMS 进料组件上盖

请参考 WIKI: [AMS 上下料组件上盖更换指南](replace-auto-filament-loader-cover.md)，安装 AMS 上下料组件上盖、上下料嘴、烘干仓盖。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feed-selector-motor/zh/10_ams_3h____________ams_3h_auto_filament_loader_replacement_guide_f53cd077fa.jpg)

## 功能验证

连接打印机，通电并启动打印机， AMS 完成自检无报错即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
