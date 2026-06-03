---
path: zh/h2/maintenance/replace-mc-board-fan
title: "更换 H2 系列 MC 板风扇"
description: "本文介绍了如何更换 H2 系列 MC 板风扇"
tags: []
created: 2025-03-25T01:59:44.275Z
updated: 2026-03-13T03:12:33.713Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-mc-board-fan
---

## MC 板风扇

MC 板风扇在打印机左内衬上，用于给 MC 板散热。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-13.png)

**MC 板风扇的备件包含如下：**

1. MC 板风扇 \* 1
2. 软螺钉 \* 4

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/img_v3_02jg_ec578e08-7f58-4ecf-b77f-ee6c6a1f93cg.jpg)

## 何时更换

- MC 板风扇异响；
- MC 板风扇异常

## 所需的工具和材料

1. 新的 MC 板风扇
2. H2.0 内六角扳手
3. H1.5 内六角扳手
4. 镊子（建议准备一个，便于后续安装软螺钉）

**更换 H2D MC 板风扇所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **位置** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定背板（绿色方框标记） |  |  | 12 |
|  |  | 用于固定左侧板 |  |  | 3 |
|  |  | 用于固定废料滑梯 |  |  | 1 |
|  |  | 用于固定 AC 板理线盖 |  |  | 1 |
| M3x3（螺帽直径 10mm） |  | 用于固定玻璃前门 |  |  | 4 |
| BT3x16 |  | 用于固定辅助部件冷却风扇 |  |  | 2 |
| ST3x3 |  | 用于固定左侧板 |  |  | 2 |
| ST3x8 |  | 用于固定背板（红色圆圈标记） |  |  | 11 |
| ST3x12 |  | 用于固定料盘支架底座（黄色方框标记） |  |  | 2 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系在线技术支持 （服务时间 9:00-21:00），我们将及时回复并为您提供所需的帮助。

## 移除 MC 板风扇

### 步骤 1：移除背板

您可以参考这篇 Wiki 来移除 H2D 的背板：

[更换 H2D 背板](replace-rear-panel.md)

### 步骤 2：移除左侧板

您可以参阅这篇 Wiki 来了解移除左侧板的详细步骤：[更换 H2D 左侧板](replace-side-panel-with-glass-window.md)

### 步骤 3：移除废料滑梯

使用 H2.0 内六角扳手移除 1 颗固定螺丝（BT3x8），然后向下拉动废料滑梯，直到可以看见废料滑梯的两个卡扣，然后向外取出废料滑梯。

> 废料滑梯除了通过顶部的螺丝固定外，底部也有两个卡扣扣在内衬上来进行固定。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-3.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-4.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-5.png)

### 步骤 4：移除 AC 板理线盖

1. 从 MC 板依次断开下图所示的 4 根线缆，并将线缆从 AC 板理线盖的线扣上取下，以便于后续移除 AC 板理线盖；

**断开线缆连接**  
![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-14.png)

**从线扣中移除**  
![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-15.png)

**移除后**  
![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-16.png)

2. 使用 H2.0 内六角扳手移除一颗固定螺丝（BT3x8），然后拿住 AC 板理线盖，用拇指将 AC 板理线盖稍微往里按，同时向外拔出，以解锁两个卡扣；然后斜着将 AC 板理线盖取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-17.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-19.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-23.png)

> 注：在移除 AC 板理线盖的过程中要注意避让顶部的线缆和 MC 板散热片。

### 步骤 5：移除 MC 板风扇

MC 板风扇使用四颗软螺钉固定在内衬上，您可以先将 MC 板风扇与 MC 板断开连接，然后从左内衬的外侧依次将四颗软螺钉拔出，将 MC 板风扇移除。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-28.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-27.png)

## 安装 MC 板风扇

### 步骤 1：安装 MC 板风扇

1. 先将软螺钉从外侧穿过左内衬上的小孔，然后拉动软螺，依次将四个软螺钉安装到位；

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-24.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-21.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-22.png)

2. 将新的 MC 板风扇贴有标签的一侧朝向左内侧内侧，并确保 MC 板风扇线缆在左上角。先将左上角软螺钉穿过 MC 板风扇，然后拉动软螺钉安装到位，然后依次安装左下角、右上角和右下角的软螺钉（您可以参考下图所示的编号），最后将 MC 板风扇线缆与 MC 板连接。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-25.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-26.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-20.png)

### 步骤 2：安装 AC 板理线盖

1. 将 AC 板理线盖斜着插入，以便于避开 MC 板散热片，然后将 AC 板理线盖向上推，确保线缆没有被 AC 板理线盖压住：

- 辅助部件冷却风扇连接线和左侧板霍尔连接线在 AC 板理线盖的右侧；
- 热床线缆连接线和状态灯连接线从 AC 板理线盖的底部穿出；
- MC-AC 线缆从 AC 板理线盖的左侧小孔穿出。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-18.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-40.png)

2. 先将 AC 板理线盖内侧的卡扣对准内衬上的卡扣，将 AC 板理线盖上的卡扣卡在内衬卡扣下方，然后将 AC 板理线盖外侧的两个卡扣与内衬上的小孔对准，并将卡扣扣入左内衬中，使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT3x8）；

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-37.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-43.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-42.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-36.png)

3. 先将下图所示的 4 根线缆依次接回 MC 板，并将线缆扣入 AC 板理线盖的线扣中。

> 请参考下图将线缆依次扣入对应的卡扣中。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-35.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-34.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-38.png)

### 步骤 3：安装废料滑梯

1. 先将废料滑梯底部的两个卡扣对准内衬上的两个孔位；

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-31.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-39.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-33.png)

2. 然后将废料滑梯往上扣，确保底部的卡扣扣入内衬中，用手托住废料滑梯的顶部，将废料滑梯的顶部的螺丝孔位对齐，最后使用 H2.0 内六角扳手拧紧一颗固定螺丝，并将黄绿和红白两根线缆扣在废料滑梯顶部的线扣后。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-41.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-29.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-30.png)

注：在安装废料滑梯的时候，需要注意将废料滑梯的两侧扣在内衬的外侧，如果扣在内侧可能无法正常安装。

![](https://wiki.bambulab.com/h2/maintenance/replace-mc-board-fan/image-32.png)

### 步骤 4：安装左侧板

您可以参考这篇 Wiki 来将左侧板安装至打印机上：[更换 H2D 左侧板](replace-side-panel-with-glass-window.md)

### 步骤 5：安装背板

您可以参考下面的这篇 Wiki 来了解安装背板的详细步骤：[更换 H2D 背板](replace-rear-panel.md)

## 如何验证成功

连接电源线并打开电源。如下所示运行设备自检操作，如果没有出现错误，则更换成功。

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
