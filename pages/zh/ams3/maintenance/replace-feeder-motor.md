---
path: zh/ams3/maintenance/replace-feeder-motor
title: "AMS 送料电机更换指南"
description: ""
tags: []
created: 2026-11-03T13:25:43.992Z
updated: 2026-11-06T02:30:00.983Z
source: https://wiki.bambulab.com/zh/ams3/maintenance/replace-feeder-motor
---

## AMS 送料电机

![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feeder-motor/zh/53_ams__________ams_3h_feeder_motor_replacement_guide_d2338b0120.jpg)

## 何时更换

- AMS 送料电机报错。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> **重要提醒!**  
> 在对AMS及其内部电子设备进行任何维护工作之前,请关闭AMS及打印机电源,并断开电源连接,以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。拆装过程中请避免暴力操作,防止造成零部件或连接结构的二次损伤。拆除部件前,请妥善保管拆除的固定螺丝,以免丢失。

## 移除 AMS 送料电机

> 请参考 WIKI：[AMS 3H 舱体拆装指南](../../h3c/maintenance/replace-chamber.md)，先将 AMS 舱体从AMS 支架上分离出来。

### 第 1 步 移除 AMS 进料组件上盖

参考 [AMS进料组件上盖更换指南](replace-auto-filament-loader-cover.md)，移除 AMS 上下料组件上盖。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feeder-motor/zh/10_ams_3h____________ams_3h_auto_filament_loader_replacement_guide_15119abbe1.jpg)

### 第 2 步 移除送料电机螺丝

用 H2.0 内六角扳手移除 2 颗螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feeder-motor/zh/53_ams__________ams_3h_feeder_motor_replacement_guide_c5b4eca0e6.jpg)

### 第 3 步 移除 AMS 送料电机连接线

翻转 AMS 使其底部朝上，用 H1.5 内六角扳手移除 3 颗螺丝，取下 AMS 主板装饰盖。  
![mainboard-cover-screws.jpeg](https://wiki.bambulab.com/ams-3h/replacement/mainboard-cover-screws.jpeg)

断开电机线连接，并将线缆从各卡扣中松出，移除送料电机。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feeder-motor/zh/53_ams__________ams_3h_feeder_motor_replacement_guide_b517d142f4.jpg)

## 安装 AMS 送料电机

### 第 1 步 将电机连接到 AMS 主板，整理线缆

将送料电机线缆连接到 AMS 主板的连接器上，整理好线缆。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feeder-motor/zh/53_ams__________ams_3h_feeder_motor_replacement_guide_cd6279e9e5.jpg)

安装主板装饰盖，锁入 3 颗螺丝固定。  
![mainboard-cover-screws.jpeg](https://wiki.bambulab.com/ams-3h/replacement/mainboard-cover-screws.jpeg)

### 第 2 步 安装送料电机

确认连接器的朝向，然后倾斜电机主动轮，将电机塞进中框的电机安装孔，可以轻松微摆动电机，使电机能安装到底。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feeder-motor/zh/47_ams_3h___________ams_3h_feeder_gear_set_replacement_guide_a7ad3bfcc1.jpg)

从 AMS 正面确认对齐螺丝孔，锁入 2 颗螺丝将电机固定。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feeder-motor/zh/53_ams__________ams_3h_feeder_motor_replacement_guide_c5b4eca0e6.jpg)

### 第 3 步 安装 AMS 进料组件上盖

请参考 WIKI: [AMS进料组件上盖更换指南](replace-auto-filament-loader-cover.md)， 安装 AMS 上下料组件上盖、上下料嘴、烘干仓盖。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-feeder-motor/zh/10_ams_3h____________ams_3h_auto_filament_loader_replacement_guide_f53cd077fa.jpg)

## 功能验证

- 连接打印机并启动，执行一次上料的操作，确认耗材能正常输送。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
