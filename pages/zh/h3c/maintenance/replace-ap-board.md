---
path: zh/h3c/maintenance/replace-ap-board
title: "AP 板更换指南"
description: ""
tags: []
created: 2026-11-03T12:39:44.453Z
updated: 2026-11-03T12:39:45.518Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-ap-board
---

## AP 板

AP 板的全称是应用处理器主板（Application Processor Main Board），它是打印机内处理信息交互的电路板，安装在打印机的左侧视窗以内。它为打印机提供了一个独立的操作环境，并支持打印机应用所需的所有系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_db7f55c28e.jpg)

> **AP 板连接器说明如下：**  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_ef4dadfe0e.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | MC -AP 通信 2 | 6 | 俯视摄像头（选配） |
| 2 | 左补光灯 | 7 | 腔温传感器 |
| 3 | MC -AP 通信 1 | 8 | 实况摄像头 |
| 4 | MC - AP ( 24 V 电源线) | 9 | 屏幕 |
| 5 | 工具头 （USB 线） | 10 | WIFI 天线 |

## 何时更换

1. AP 板出现明显的物理损坏，如连接器损坏、元器件脱落或烧坏；
2. 经 Bambu Lab 技术支持分析需更换 AP 板。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 AP 板

### 第 1 步 移除左视窗

请参考 WIKI: [视窗更换指南](replace-side-glass-left.md)，将左侧视窗移除，  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/06_x____________tool_head_with_x_axis_assembly_replacement_guide_d7d13a6323.jpg)

### 第 2 步 移除导光板

用 H1.5 内六角扳手移除 2 颗螺丝，并取下导光板。注意需将导光板向上提，离开卡扣位置后再取下。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/27___________birdseye_camera_replacement_guide_92b5608580.jpg)

### 第 3 步 断开连接线缆

用 H1.5 内六角扳手移除 USB 线缆支架的螺丝，取下支架。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_c15a964ef8.jpg)

将可见的连接线缆从 AP 板的连接器上断开，共 8 根（不含 WIFI 天线）。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_846a76e47e.jpg)

### 第 4 步 移除 AP 板

用 H1.5 内六角扳手移除 AP 板 的 4 颗螺丝，将 AP 板从框架上取出。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/11_h3c_____screws_kit_for_h3c_2472dbb704.jpg)

用镊子去除 WIFI 天线插头上的硅胶，然后用镊子夹住插头线缆根部，将 WIFI 天线从连接器上断开。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_03f95682a8.jpg)

## 安装 AP 板

### 第 1 步 连接天线和软排线

先连接天线插头，注意同轴线缆的连接要对齐后再按压。然后连接屏幕 FPC 和摄像头 FPC，合上连接器盖子。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_ee5ff1aadf.jpg)

### 第 2 步 安装 AP 板

根据 2 个定位柱安装 AP 板，先安装右侧已连接 FPC 排线的一端，对齐螺丝孔位后按下图标识的顺序依次锁上 4 颗螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_178ca2d2ad.jpg)

连接线缆，注意 USB 线插头上有凸起的一面朝外。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_1fe0d4bc1b.jpg)

### 第 3 步 安装导光板

根据 2 个螺丝孔的位置安装导光板，先将导光板两侧的螺丝位挂进卡扣，然后锁入 2 颗螺丝进行固定。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/27___________birdseye_camera_replacement_guide_f89ead02c2.jpg)

### 第 4 步 安装视窗 （可以在验证问题解决后再安装）

请参考 WIKI: [视窗更换指南](replace-side-glass-left.md)，将左侧视窗安装到左侧板上。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/27___________birdseye_camera_replacement_guide_a781df3294.jpg)

### 第 5 步 绑定新序列号（SN）

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的 AP 板也将不能再被注册或绑定。

更换了 AP 板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换 AP 板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ap-board/zh/45_ap_______ap_board_replacement_guide_8dcc9d3576.jpg)

## 功能验证

连接电源线并启动打印机，能执行并通打印机的校准流程。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
