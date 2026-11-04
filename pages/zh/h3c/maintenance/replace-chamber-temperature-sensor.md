---
path: zh/h3c/maintenance/replace-chamber-temperature-sensor
title: "腔温传感器更换指南"
description: ""
tags: []
created: 2026-11-03T12:44:30.720Z
updated: 2026-11-03T12:48:30.501Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-chamber-temperature-sensor
---

## 腔温传感器

腔温传感器共有 2 个，安装在打印机的左右两侧，用于实时监测打印机的腔体温度。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-temperature-sensor/zh/55___________chamber_temperature_sensor_replacement_guide_275d8d7fa9.jpg)

## 何时更换

- 腔温数据异常跳变
- 腔温传感器出现物理损坏

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-temperature-sensor/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 1. 打印机左侧的腔温传感器被屏幕 FPC 遮挡，需要移除左侧板后更换。打印机侧板的拆装需要提前移除 AMS 3H，请参考 WIKI： [AMS 3H 拆除与安装指南](replace-ams3.md)，将 AMS 3H 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3H 的场景下进行。
> 2. 打印机右侧的腔温传感器没有遮挡，移除右侧视窗即可拆除。

## 移除左侧腔温传感器

### 第 1 步 移除 左侧板

请参考 WIKI: [左侧板更换指南](replace-side-panel-left.md)，移除玻璃前门及左侧板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-temperature-sensor/zh/55___________chamber_temperature_sensor_replacement_guide_bd77b714b8.jpg)

### 第 2 步 断开屏幕 FPC

打开屏幕 FPC 连接器的盖子，将屏幕 FPC 从过线孔中退出，使左侧腔温传感器完全露出。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 3 步 移除 腔温传感器

按压插头锁扣进行解锁并断开腔温传感器，用手捍住靠近卡扣位置的线缆将线缆从卡扣中扯出，然后直接拔出腔温传感器。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装左侧腔温传感器

### 第 1 步 安装左侧腔温传感器

将腔温传感器安装进圆形小孔，向内推腔温传感器，直至黑色热缩管刚好露出。

|  |  |
| --- | --- |
| 图 | 图 |

将外露的热缩管弯折进卡扣中，将腔温传感器插头连接到 AP 板的连接器上。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 连接屏幕 FPC

将屏幕 FPC 从过线孔中穿过，并连接到 AP 板的连接器上，确认第一道白线与连接器边缘齐平，然后合上盖子。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 3 步 安装左侧板

请参考 WIKI: [左侧板更换指南](replace-side-panel-left.md)，安装好左侧板及玻璃前门。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-temperature-sensor/zh/55___________chamber_temperature_sensor_replacement_guide_e33e1f35ef.jpg)

## 移除右侧腔温传感器

### 第 1 步 移除视窗

请参考 WIKI: [视窗更换指南](replace-side-glass-left.md)，拆除右侧视框，露出热端挂架控制板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-temperature-sensor/zh/55___________chamber_temperature_sensor_replacement_guide_b6254b615c.jpg)

### 第 2 步 移除右侧腔温传感器

按压插头锁扣进行解锁并断开腔温传感器，撕开固定磁环的胶布，将线缆从卡扣中松出。

|  |  |
| --- | --- |
| 图 | 图 |

用手捍住靠近卡扣位置的线缆将线缆从卡扣中扯出，然后直接拔出腔温传感器。

|  |  |
| --- | --- |
| 图 | 图 |

> 注意：由于组装打印机时，线缆连接的先后顺序有差异，在将腔温传感器的线缆从卡扣中松出时会被其他线缆影响，注意调整即可，重新装回时，卡进线扣即可。

## 安装右侧腔温传感器

### 第 1 步 安装右侧腔温传感器

将腔温传感器安装进圆形小孔，并向内推，直至黑色热缩管刚好露出。

|  |  |
| --- | --- |
| 图 | 图 |

将外露的部分热缩管弯折进卡扣中，然后将线缆整理进线扣中，插头连接到转接板的连接器上，重新贴好磁环胶布。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 安装视窗

请参考 WIKI: [视窗更换指南](replace-side-glass-left.md)，安装右侧视窗。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-temperature-sensor/zh/15_____________swaptek_rack_control_board_replacement_guide_5aa3f7fb53.jpg)

## 功能验证

启动打印机，确认无腔温关联的报错提示即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
