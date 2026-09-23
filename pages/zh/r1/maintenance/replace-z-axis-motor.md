---
path: zh/r1/maintenance/replace-z-axis-motor
title: "Z 轴电机更换指南"
description: ""
tags: []
created: 2026-09-22T13:10:39.182Z
updated: 2026-09-22T13:11:10.019Z
source: https://wiki.bambulab.com/zh/r1/maintenance/replace-z-axis-motor
---

## Z 轴电机 Z-axis Motor

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/001.png)

Z 轴电机包含电机和齿条组件，驱动 Z 轴移动。

## 所需工具和材料

- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 移除 Z 轴电机

### 步骤 1.移除 TH 板

参照[TH 板更换指南](replace-th-board.md)移除工具头前盖和TH板。

### 步骤 2.移除镜座支架

使用 H1.5 内六角螺丝刀移除四颗镜座支架固定螺丝，使用 H2.0 内六角螺丝刀移除卷簧到镜座支架端螺丝。

![002.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/002.jpg)

取下镜座支架，此时镜座支架上还连接有气管（无需拔出气管），请勿过分拉拽气管。

![003.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/003.jpg)

### 步骤 3.移除Z电机齿条（可选）

注意：如果齿条并无损坏，可以跳过此部分。

使用 H2.0 内六角螺丝刀拧下图示一颗螺丝，小心翻转镜座支架，继续拧下正面两颗固定螺丝。

|  |  |
| --- | --- |
| 004.jpg | 005.jpg |

移除镜座支架上的齿条。

![006.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/006.jpg)

### 步骤 4.移除 Z 轴电机

使用 H2.0 内六角螺丝刀拆除正面两颗电机固定螺丝，取下电机。

![007.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/007.jpg)

使用 H2.0 内六角螺丝刀拆除两颗理线夹螺丝，取出电机连接线。

![008.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/008.jpg)

将电机线从理线夹中取出。

![009.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/009.webp)

将拖链向外轻微扭转，漏出图示两颗螺丝，然后使用 H2.0 内六角螺丝刀移除图示螺丝。

![010.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/010.jpg)

轻微抬起拖链，向下翻转 Z 电机将其取下。

![011.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/011.webp)

## 安装 Z 轴电机

### 步骤 1.安装Z电机齿条（可选）

如果在前序步骤中拆除了Z电机齿条，则需要安装此步骤装回齿条。

将齿条装入镜座支架，注意齿条方向，使用 H2.0 内六角螺丝刀锁入三颗螺丝固定。

|  |  |
| --- | --- |
| 012.jpg | 013.jpg |

### 步骤 2.安装Z电机

将新的电机安装到原位，使用 H2.0 内六角螺丝刀锁入两颗螺丝，固定拖链。

|  |  |
| --- | --- |
| 014.webp | 015.png |

使用 H2.0 内六角螺丝刀锁入正面两颗电机固定螺丝，固定电机。

> 注意：安装此处螺丝时请先将对齐电机上的螺丝孔，确保电机正常固定。

![016.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/016.jpg)

将Z电机线缆穿过挡灰毛刷。

![017.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/017.webp)

将电机连接线、摄像头线、工具头线依次装入理线夹，尽量露出更长的线缆，便于后续操作。然后使用 H2.0 内六角螺丝刀锁入两颗理线夹螺丝。

|  |  |
| --- | --- |
| 018.webp | 019.png |

### 步骤 3.安装镜座支架

将镜座支架对齐Z轴滑块，使用 H1.5 内六角螺丝刀锁入四颗螺丝固定。

![020.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/020.jpg)

将镜座支架升到最高位置，对齐卷簧孔位和螺丝孔，使用 H2.0 内六角螺丝刀锁入一颗螺丝。

![021.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-motor/zh/021.png)

### 步骤 4.安装 TH 板

参照[TH 板更换指南](replace-th-board.md)装回TH板和工具头前盖。

## 功能验证

更换完成后，请通过屏幕选择：**设置>校准>视觉精度校准**选项，重新运行视觉精度校准。如果校准正常结束则上述安装正确。

|  |  |
| --- | --- |
| 022.png | 023.png |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。
>
> 如果问题仍未解决，请提交 [服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5) 并附上您近期的设备日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。
>
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
