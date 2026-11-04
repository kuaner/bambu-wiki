---
path: zh/ams3/maintenance/replace-connector-board
title: "AMS 3H 接口板更换指南"
description: ""
tags: []
created: 2026-11-03T13:25:10.382Z
updated: 2026-11-03T13:25:11.482Z
source: https://wiki.bambulab.com/zh/ams3/maintenance/replace-connector-board
---

## AMS 3H 接口板

![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-connector-board/zh/91_ams_3h_________ams_3h_connector_board_replacement_guide_dd38cf1e36.jpg)

> **接口板连接器说明如下：**  
> H：代指霍尔检测板，用黑色插头； R：代指 RFID，用白色插头。  
> ![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-connector-board/zh/91_ams_3h_________ams_3h_connector_board_replacement_guide_76b0418986.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | AMS 3H 主板 | 6 (H6) | 6 号槽入料口组件 |
| 2 （H2） | 2 号槽入料口组件 | 7 (R6) | 6 号 RFID |
| 3 (R2) | 2 号 RFID | 8 (H8) | 8 号槽入料口组件 |
| 4 (H4) | 4 号槽入料口组件 | 9 (R8) | 8 号 RFID |
| 5 (R4) | 5 号 RFID | 10 (H9) | 9 号槽入料口组件 |

## 何时更换

- AMS 无法正常通信或识别
- 接口板外观出现烧焦、元器件异常
- 插座或插头出现松动、断裂
- 经排查确认是接口板本身存在故障

## 工具和材料

- H1.5 内六角扳手

## 安全提示

> 重要提醒 ！  
> 在对 AMS 及其内部电子设备进行任何维护工作之前，请关闭 AMS 及打印机电源，并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 拆装过程中请避免暴力操作，防止造成零部件或连接结构的二次损伤。  
> 断开插头前，建议拍照记录各插头的连接位置，便于后续按正确顺序恢复连接。

## 拆装提示

> 本指南是在将 AMS 3H 舱体从支架上移除后的情况操作的，请参考WIKI: [AMS 3H 舱体拆装指南](../../h3c/maintenance/replace-chamber.md)，完成将 AMS 舱体从AMS 支架上移除和安装的操作。

## 移除 AMS 3H 接口板

### 第 1 步 移除 AMS 3H 接口板装饰盖

用 H1.5 内六角扳手拧下 4 颗螺丝，移除 AMS 3H 接口板装饰盖。

![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-connector-board/zh/44_ams_3h_rfid_________ams_3h_rfid_reader_replacement_guide_84a2e91957.jpg)

### 第 2 步 移除 AMS 3H 接口板

用 H1.5 内六角扳手，移除 2 颗螺丝，使 AMS 3H 接口板能从中框上分离出来。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-connector-board/zh/91_ams_3h_________ams_3h_connector_board_replacement_guide_fc2846c477.jpg)

依次按压连接插头解锁并断开连接线缆，共9 个连接器，移除 AMS 3H 接口板。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-connector-board/zh/91_ams_3h_________ams_3h_connector_board_replacement_guide_8f54f1087e.jpg)

## 安装 AMS 3H 接口板

### 第 1 步 安装 AMS 3H 接口板

根据 AMS 中框上和接口板上的字母标识，将插头连接到 AMS 3H 接口板上。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 安装 AMS 3H 接口板装饰盖

检查确认无连接线贴在螺丝柱上，装回接口板装饰盖，锁入 4 颗螺丝固定。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-connector-board/zh/91_ams_3h_________ams_3h_connector_board_replacement_guide_ab9e16427e.jpg)

## 功能验证

- 所有插头按代号正确连接并插紧
- 装饰盖安装平整，4 颗螺丝已拧紧
- 重新通电后，AMS 可被正常识别，各通道功能正常。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
