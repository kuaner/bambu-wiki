---
path: zh/h3c/maintenance/replace-touchscreen
title: "屏幕和屏幕 FPC 更换指南"
description: ""
tags: []
created: 2026-11-03T12:38:57.504Z
updated: 2026-11-10T08:47:06.502Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-touchscreen
---

## 屏幕 和 屏幕 FPC

拓竹H3C 打印机使用 5 英寸的可触控屏幕，可用于控制打印机和观察打印机的工作状态。屏幕 FPC 是用于连接屏幕和 AP 板软排线。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-touchscreen/zh/71________touchscreen_replacement_guide_a598d763cb.jpg)

> 为了更高效地解决问题，拓竹H3C 的屏幕配件默认带上了屏幕排线，实际使用时，并不需要更换。只有在更换屏幕后仍未解决问题时才需要继续考虑更换屏幕排线。

## 何时更换

**屏幕**

- 屏幕玻璃损坏；
- 显示屏有亮线、斑块、闪烁等影响观看效果的故障；
- 屏幕出现黑屏/白屏等无法查看的现象，但其他功能正常；
- 触摸功能失效且连接正常；
- 影响使用的结构损坏。  
  **屏幕 FPC**
- 连接插头损坏
- FPC 排线破损或损伤

## 工具和材料

**（更换 屏幕 FPC 时使用 ）**

- H2.0 内六角扳手
- H1.5 内六角扳手
- 镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除屏幕

### 第 1 步 解锁屏幕

按压屏幕支架转轴中间位置进行解锁，并向左推动屏幕，使屏幕从前面盖上松出。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-touchscreen/zh/71________touchscreen_replacement_guide_013c55fe91.jpg)

### 第 2 步 断开屏幕 FPC 排线

按压 屏幕 FPC 排线 插头的两侧，解锁插头并断开 FPC 连接，取下屏幕。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-touchscreen/zh/71________touchscreen_replacement_guide_d9911a0dc1.jpg)

## 安装屏幕

### 第 1 步 连接屏幕 FPC 排线

将 FPC 插头对准屏幕的连接器，插头两边同时用力，将插头与连接器连接。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 安装屏幕

将转轴上的卡扣对准前面盖上的安装槽进行安装。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-touchscreen/zh/71________touchscreen_replacement_guide_2aed2b7a2b.jpg)

然后稍向右推动屏幕，将屏幕锁定。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-touchscreen/zh/71________touchscreen_replacement_guide_c43eb7fe30.jpg)

## 移除屏幕 FPC 排线

## 拆装提示

> 1. 打印机侧板的拆装需要提前移除 AMS 3H，请参考 WIKI： [AMS 3H 拆除与安装指南](replace-ams3.md)，将 AMS 3H 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3H 的场景下进行。
> 2. 拆除的步骤从已移除屏幕开始。

### 第 1 步 移除左侧板

请参考 WIKI ：[左侧板更换指南](replace-side-panel-left.md)，移除玻璃前门和左侧板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-touchscreen/zh/71________touchscreen_replacement_guide_0892f12e20.jpg)

### 第 2 步 移除前面盖

请参考 WIKI ：[前面盖更换指南](replace-front-cover.md)，移除前面盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-touchscreen/zh/71________touchscreen_replacement_guide_b9fef463fe.jpg)

### 第 3 步 移除 屏幕 FPC 排线

在 AP 板上揭开连接器盖子，将屏幕 FPC 排线从连接器上松出，然后沿打印机前门方向拉屏幕 FPC 排线，将其移除。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装屏幕排线

### 第 1 步 安装 屏幕 FPC 排线

将屏幕 FPC 排线中无插头的一端穿过框架上的过线孔，并连接到连接器上，触点侧朝向 AP 板。确认排线连接到位（第一道白线与连接器边沿平齐）后，合上盖子。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 安装前面盖

请参考 WIKI ：[前面盖更换指南](replace-front-cover.md)，安装前面盖和屏幕 （安装后即可上电检查屏幕功能）。

### 第 3 步 移除左侧板

请参考 WIKI ：[左侧板更换指南](replace-side-panel-left.md)，安装左侧板和玻璃前门。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-touchscreen/zh/71________touchscreen_replacement_guide_08314cf422.jpg)

## 功能验证

连接电源线并启动打印机，观看并在屏幕上操作，确认屏幕显示功能和触摸功能均正常。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
