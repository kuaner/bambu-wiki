---
path: zh/r1/maintenance/replace-z-axis-linear-rail
title: "Z 轴导轨更换指南"
description: ""
tags: []
created: 2026-09-22T13:11:20.799Z
updated: 2026-09-22T13:11:22.066Z
source: https://wiki.bambulab.com/zh/r1/maintenance/replace-z-axis-linear-rail
---

## Z 轴导轨 Z-axis Linear Rail

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-linear-rail/zh/001.png)

## 所需工具和材料

- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 移除 Z 轴导轨

### 步骤 1.移除 TH 板

参照[TH 板更换指南](replace-th-board.md)移除工具头前盖和TH板。

### 步骤 2.移除卷簧

手动将Z轴上升到最高位置，露出右侧标记螺丝，使用 H2.0 螺丝刀拧下图示螺丝释放卷簧。

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-linear-rail/zh/002.png)

### 步骤 3.移除镜座支架

使用 H1.5内六角螺丝刀移除四颗螺丝。

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-linear-rail/zh/003.png)

取下镜座支架，此时镜座支架上还连接有气管（无需拔出气管），请勿过分拉拽气管。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-linear-rail/zh/004.png)

### 步骤 4.移除 Z 轴导轨

将滑块移动到下方 ，使用 H2.0 内六角螺丝刀拧下两颗螺丝，向上移动滑块，继续拧下两颗螺丝，取下 Z 轴导轨组件。

> 注意：取下导轨时请固定住滑块和导轨，避免滑块从导轨末端脱出。

|  |  |
| --- | --- |
| 005.jpg | 006.jpg |

## 安装 Z 轴导轨

### 步骤 1.安装 Z 导轨

取出新的 Z 轴导轨，用手按住滑块，剪断两端的扎带，然后小心的将 Z 轴导轨装入固定槽。

> 注意：安装过程中请小心滑块从导轨末端脱出。

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-linear-rail/zh/007.png)

使用 H2.0 内六角螺丝刀锁入四颗螺丝固定 Z 轴导轨。

|  |  |
| --- | --- |
| 008.jpg | 009.jpg |

### 步骤 2.安装镜座支架

将镜座支架安装到滑块上，使用 H1.5 内六角螺丝刀锁入四颗螺丝固定。

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-linear-rail/zh/010.png)

### 步骤 3.安装卷簧

将镜座支架抬升到最高为准，对齐卷簧末端和Z轴支架孔位，锁入一颗螺丝固定。安装完成后上下拉动Z轴检查运动是否顺畅。

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-z-axis-linear-rail/zh/011.png)

### 步骤 4.安装 TH 板

参照[TH 板更换指南](replace-th-board.md)装回TH板和工具头前盖。

## 功能验证

更换完成后，请通过屏幕选择：**设置>校准>视觉精度校准**选项，重新运行视觉精度校准。如果校准正常结束则上述安装正确。

|  |  |
| --- | --- |
| 012.png | 013.png |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。
>
> 如果问题仍未解决，请提交 [服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5) 并附上您近期的设备日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。
>
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
