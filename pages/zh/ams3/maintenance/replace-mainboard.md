---
path: zh/ams3/maintenance/replace-mainboard
title: "AMS 3H 主板 更换指南"
description: ""
tags: []
created: 2026-11-03T13:25:08.635Z
updated: 2026-11-06T02:20:32.437Z
source: https://wiki.bambulab.com/zh/ams3/maintenance/replace-mainboard
---

## AMS 3H 主板

|  |  |
| --- | --- |
|  |  |

AMS 3H 主板是 AMS 的核心控制单元，安装于 AMS 中框底部，外部配有装饰盖保护。更换时需先拆除装饰盖并断开所有插头，重新安装时需按根据标识正确连接线缆。

> **AMS 3H 主板连接器说明如下：**  
> H：代指霍尔检测板，用黑色插头； R：代指 RFID，用白色插头。  
> ![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________0b4d0d093d.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- | --- | --- |
| 1 | 温湿度传感器（后） | 8 (H5) | 5 号槽入料口组件 | 15 | 温湿度传感器（前） |
| 2 | 烘干组件（温度传感器） | 9 (R1) | 1 号 RFID | 16 | AMS 3H 自动进料组件指示灯 |
| 3 | AMS AC 板 | 10 | 送料电机 | 17 | AMS 6pin接口板 |
| 4 (H7) | 7 号槽入料口组件 | 11 (H3) | 3 号槽入料口组件 | 18 | 烘干组件（风道温度传感器） |
| 5 (R7) | 7 号 RFID | 12 | 选料位置传感器 | 19 | 烘干组件（风扇） |
| 6 | 选料电机 | 13 （H1） | 1 号槽入料口组件 | 20 | AMS 3H 进/出气口组件（风门传感器） |
| 7（R5） | 5 号 RFID | 14 | AMS 3H 接口板 | 21 | AMS 3H 进/出气口组件（风门电机） |

## 何时更换

- AMS 无法正常通信或识别
- 主板外观出现烧焦、元器件异常
- 主板插座或插头出现松动、断裂
- 经排查确认主板本身存在故障

## 工具和材料

- H2.0 内六角扳手

## 安全提示

> 重要提醒 ！  
> 在对 AMS 及其内部电子设备进行任何维护工作之前，请关闭 AMS 及打印机电源，并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 拆装过程中请避免暴力操作，防止造成零部件或连接结构的二次损伤。  
> 断开插头前，建议拍照记录各插头的连接位置，便于后续按正确顺序恢复连接。

## 拆装提示

> 本指南是在将 AMS 3H 舱体从支架上移除后的情况操作的，请参考WIKI: [AMS 3H 舱体拆装指南](../../h3c/maintenance/replace-chamber.md)，完成将 AMS 舱体从AMS 支架上移除和安装的操作。

## 拆除 AMS 主板

### 第1步 移除 AMS 3H 主板装饰盖

将 AMS 舱体底面朝上放置，使用 H1.5 内六角扳手，拆除固定 AMS 主板装饰盖的 3 颗螺丝，取下装饰盖。  
![mainboard-cover-screws.jpeg](https://wiki.bambulab.com/ams-3h/replacement/mainboard-cover-screws.jpeg)

### 第2步 断开连接器

> 主板上的插头均带有锁扣结构，断开插头时请捏住插头按压解锁，不要直接拉扯线缆进行断开。  
> ![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________ca9e2cb98c.jpg)

逐一解锁连接器，断开主板上所有的连接插头（共 21 个连接插头）。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________0cad188632.jpg)

### 第3步 移除 AMS 3H 主板

使用 H1.5 内六角扳手，拧下固定主板的 3 颗螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________61b0594202.jpg)

用手拿住主板的两端，移除主板。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________90dfb8aaca.jpg)

> 取出时注意不要让板卡边缘或元器件与框体发生磕碰。

## 安装 AMS 3H 主板

> 装回装饰盖前，请整理好每根螺丝柱附近的线缆，避免线缆被压住。

### 第1步 安装主板

将 AMS 主板对准中框上的定位柱（橙色箭头所示）进行安装，检查连接线缆，确保没有压到线缆。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________65130324b8.jpg)

锁入 3 颗固定螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________61b0594202.jpg)

### 第2步 连接插头

根据中框上的代号标识，将所有插头连接到主板上。对应插头连接到插座上。如带 R1 标识的线圈插头要连接主板上标识也为 R1 的连接器上。

|  |  |
| --- | --- |
| 图 | 图 |

下图标记红色交叉符号的连接器是空的，不需要连接线缆。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________0cad188632.jpg)

### 第3步 装回装饰盖

整理好每根螺丝柱附近的线缆，确保走线顺畅不被压住。

> 若线缆被压住，可能导致装饰盖无法完全贴合，甚至损伤线缆。

![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/46_ams_3h_________86714a7083.jpg)

将 AMS 主板装饰盖对准安装位，锁入 3 颗固定螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-mainboard/zh/44_ams_3h_rfid_________ams_3h_rfid_reader_replacement_guide_7ab9cb6e6c.jpg)

## 如何验证成功

- 主板 3 颗螺丝已拧紧，定位准确
- 所有插头按代号正确连接并插紧
- 装饰盖安装平整，3 颗螺丝已拧紧
- 重新通电后，AMS 可被正常识别，各通道功能正常

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
