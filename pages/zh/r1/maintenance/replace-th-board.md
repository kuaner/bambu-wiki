---
path: zh/r1/maintenance/replace-th-board
title: "TH 板更换指南"
description: ""
tags: []
created: 2026-09-22T13:11:02.472Z
updated: 2026-09-22T13:11:03.755Z
source: https://wiki.bambulab.com/zh/r1/maintenance/replace-th-board
---

## TH 板 TH Board

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/001.png)

TH 板分为上下两块PCB板，同时包含TH板安装支架。

## 所需工具和材料

- H1.5 内六角螺丝刀
- H2.0 内六角螺丝刀

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 移除 TH 板

### 步骤 1.移除工具头前盖

使用 H1.5 内六角螺丝刀拆卸图示两颗螺丝。

|  |  |
| --- | --- |
| 002.jpg | 003.jpg |

取下工具头前盖。

![004.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/004.webp)

### 步骤 2.移除接口板

1、2、3号插头需要先打开排线扣，然后向上抬出排线（排线有防松结构，不可直接向后暴力拔出），4号插头请小心向下拔出。

> 注意：接口板线缆较短，请小心操作。

![005.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/005.jpg)

打开 1 号卡扣，取出排线，然后断开 4 号插头。

![006.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/006.webp)

拧下四颗螺丝，取下接口板，注意此时接口板仍然有线缆未断开。

![007.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/007.jpg)

断开接口板正面 2、3号插头，翻转TH板，断开背面两个插头。然后取下接口板。

|  |  |
| --- | --- |
| 008.webp | 009.webp |

### 步骤 3.移除TH板

使用 H1.5内六角螺丝刀拆下图示四颗螺丝。

![010.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/010.jpg)

断开图示 TH 板上的三个插头和一处排线。

![011.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/011.webp)

### 步骤 4.移除 TH 板支架

> 注意：如果 TH 板支架并没有损坏可跳过此步骤。

使用 H2.0 内六角螺丝刀拧下图示两颗螺丝，取下光学传感器模组。

|  |  |
| --- | --- |
| 012.png | 013.webp |

使用H2.0 内六角螺丝刀移除图示四颗螺丝，取下TH板支架。下方的两颗螺丝与上方两颗不同，左下角蓝色标记的螺丝为粗牙，右下角螺丝长度稍短，请注意区分。

![014.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/014.jpg)

## 安装 TH 板

### 步骤 1.安装 TH 板支架

装回TH板支架，使用H2.0 内六角螺丝刀锁入四颗螺丝固定。下方的两颗螺丝与上方两颗不同，左下角蓝色标记的螺丝为粗牙，右下角螺丝长度稍短，请注意区分。

![015.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/015.png)

装回光学传感器模组，使用 H2.0 内六角螺丝刀锁入图示两颗螺丝固定。

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/016.png)

### 步骤 2.安装 TH 板

将 TH 板和接口板装好，使用 H1.5 内六角螺丝刀锁入四颗螺丝固定。连接图示排线。

![017.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/017.png)

> 如果您收到的TH板组件已经为图示状态，可直接参照下方步骤操作。

先安装后侧TH板上的两个插头，其中 2 Pin 插头为绿白线，再安装前侧接口板背面的两个插头，其中 2 Pin 插头为红黑线。这两个插头请仔细核对，不可插反。

> TH板组件中间有四个接口，其中两个 2 Pin 接口可能插错，请务必参照图示的线色安装。

|  |  |
| --- | --- |
| 018.webp | 019.webp |

连接光学组件摄像头排线，排线较短，请小心操作。

![020.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/020.webp)

### 步骤 3.固定TH板组件

TH板和接口板已经提前固定，此时只需要使用 H1.5 内六角螺丝刀锁入图示四颗银色自攻丝，固定TH板即可。  
左下角螺丝位置容易被线缆遮挡，请注意检查。

![021.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/021.jpg)

连接剩余的工具头线缆、Z电机线缆、光路校准传感器排线。

![022.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/022.webp)

### 步骤 4.安装工具头前盖

将工具头前盖装回工具头。

![023.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-th-board/zh/023.jpg)

使用 H1.5 内六角螺丝刀锁入两颗螺丝固定。

|  |  |
| --- | --- |
| 024.jpg | 025.jpg |

## 功能验证

打开电源，运行设备[视觉精度校准](../manual/visual-accuracy-calibration.md)，如果校准正常完成，则上述操作正确。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。
>
> 如果问题仍未解决，请提交 [服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5) 并附上您近期的设备日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。
>
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
