---
path: zh/h3c/maintenance/replace-mc-board
title: "MC 板更换指南"
description: ""
tags: []
created: 2026-11-03T12:41:43.333Z
updated: 2026-11-05T02:37:27.216Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-mc-board
---

## MC 板

MC板的全称是 Main Control Board，中文通常称为 “主控板” ，它是一块集成了微处理器、各种驱动芯片、接口和电路的印刷电路板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/18_mc_______mc_board_replacement_guide_eab5b83710.jpg)

> **MC 板连接器说明如下：**（红色 “X” 标识的两个连接器不可用，请忽略。 ）  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/18_mc_______mc_board_replacement_guide_813bf272b0.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- | --- | --- |
| 1 | **后自适应风道组件** | 7 | MC-AP （24 V 电源） | 14 | 空 |
| 2 | MC - AP 通信 1 | 8 / 9 | **右自适应风道组件** | 15 | **热床 (通信/NTC)** |
| 3 | 空 | 10 | 电源（ 24 V 电源） | 16 | **热床 (状态指示灯)** |
| 4 | 缓冲器/6 PIN 接口板 | 11 | 闪切挂架控制板 | X | **XY 电机-右** |
| 5 | 打印头控制转接板 | 12 | 电源散热风扇 | Y | **XY 电机-左** |
| 6 | AP-MC 通信 2 | 13 | AC 板（通信） | Z | Z 电机 |

## 何时更换

- 正常供电情况下， MC 板工作指示灯不闪烁；
- 连接器损坏，有明显的元器件损坏；
- 拓竹服务团队通过日志文件确认是主控板关联问题。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 MC 板

### 第 1 步 移除背板

请参考 WIKI: [废料滑梯更换指南](replace-purge-chute.md)，移除背板及滑梯。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/14____________printer_cable_pack_replacement_guide_a80238f5ce.jpg)

### 第 2 步 断开连接线

将 MC 板上所有的线缆逐一移除，共移除 16个 插头。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/18_mc_______mc_board_replacement_guide_d20a40907e.jpg)

> NO. 3 & 14 两个连接器没有连接线，NO. 8 &9 是一体的连接器。

### 第 3 步 移除 MC 板

用 H1.5 内六角扳手移除 6 颗螺丝，取下 MC 板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/18_mc_______mc_board_replacement_guide_409238c41e.jpg)

## 安装 MC 板

### 第 1 步 安装 MC 板

避让线缆，将 MC 板安装到内衬上，按标识的序号依次锁入 6 颗螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/18_mc_______mc_board_replacement_guide_f2a912a674.jpg)

### 第 2 步 连接线缆

参考 MC 板的连接器说明，按下图所示，将各插头连接到相应的连接器上，整理好线缆。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/18_mc_______mc_board_replacement_guide_2bd746ab94.jpg)

> **MC 板连接器说明如下：**  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/18_mc_______mc_board_replacement_guide_813bf272b0.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- | --- | --- |
| 1 | 背侧内衬转接板 | 7 | MC-AP （24 V 电源） | 14 | 空 |
| 2 | MC - AP 通信 1 | 8 / 9 | 右侧内衬转接板 | 15 | 热床 NTC |
| 3 | 空 | 10 | 电源（ 24 V 电源） | 16 | 热床通信 |
| 4 | 缓冲器/6 PIN 接口板 | 11 | 闪切挂架控制板 | X | X 电机 |
| 5 | 打印头控制转接板 | 12 | 电源散热风扇 | Y | Y 电机 |
| 6 | AP-MC 通信 2 | 13 | AC 板（通信） | Z | Z 电机 |

### 第 3 步 安装背板

请参考 WIKI: [废料滑梯更换指南](replace-purge-chute.md)，将背板及其他配件安装好。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-mc-board/zh/12_z________z_motor_replacement_guide_2980526540.jpg)

## 功能验证

连接电源线并启动打印机，执行一次打印机回零的操作，确认能执行并通过。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
