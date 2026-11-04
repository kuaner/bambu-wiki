---
path: zh/h3c/maintenance/replace-ac-board
title: "AC 板更换指南"
description: ""
tags: []
created: 2026-11-03T12:41:34.025Z
updated: 2026-11-03T12:41:35.064Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-ac-board
---

## AC 板

AC 板是安装在打印机左内衬中，用于给热床和腔温加热模块提供交流电输入的电路板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/104_ac_______ac_board_replacement_guide_9c20c848d8.jpg)

> AC 板的连接器说明如下：  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/104_ac_______ac_board_replacement_guide_e570172c7c.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 电源开关插座 | 4 | 右腔温组件 （供电、不区分） |
| 2 | 后腔温组件 （供电，不区分） | 5 | MC 板 （通信） |
| 3 | 热床 （供电） | / | / |

## 何时更换

1. AC 板上有明显的烧毁或损坏；
2. 热床或腔温加热模块无法正常加热时可能需要更换 AC 板。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手
- 十字螺丝刀

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 AC 板

### 第 1 步 移除背板

请参考WIKI：[废料滑梯更换指南](replace-purge-chute.md)，移除背板及滑梯。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/14____________printer_cable_pack_replacement_guide_a80238f5ce.jpg)

### 第 2 步 断开连接线

打开 1 号电源线盖子，用 十字螺丝刀拧松螺丝，移除电源线；2 ~4 号使用快速连接端子，按压锁扣位置解锁后拔出母头；5 号按压锁扣后断开连接。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/104_ac_______ac_board_replacement_guide_a5958cdfcc.jpg)

> **快速连接端子拆除：如果直接按压解锁失败，可参考以下步骤进行移除。**  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/104_ac_______ac_board_replacement_guide_a3d24b7324.jpg)

### 第 3 步 移除 AC 板

用 H1.5 内六角扳手移除 3 颗螺丝，取下 AC 板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/104_ac_______ac_board_replacement_guide_c624776717.jpg)

## 安装 AC 板

### 第 1 步 安装 AC 板

将 AC 板安装到电源上方，注意板子左侧要安装在黑色支撑块底下。锁入 3 颗螺丝固定 AC 板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/104_ac_______ac_board_replacement_guide_ff2923741b.jpg)

### 第 2 步 连接线缆

棕色线在上方，连接两根电源线到 1 号座子，锁紧螺丝并合上盖子；连接 2 ~4 号使用快速连接端子，装回绝缘胶套；将 MC-AC 线缆连接到 5 号连接器 。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/104_ac_______ac_board_replacement_guide_36c27b17de.jpg)

如下图，快速连接端子统一朝向进行安装，并确保绝缘胶套全部装回到端子上。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/104_ac_______ac_board_replacement_guide_414e88d5f6.jpg)

### 第 3 步 安装背板

请参考WIKI：[废料滑梯更换指南](replace-purge-chute.md)，将背板及其他配件安装好。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-ac-board/zh/12_z________z_motor_replacement_guide_2980526540.jpg)

## 功能验证

连接电源线并启动打印机，设置热床温度为 50 ℃，确认热床温度能升高到目标值。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
