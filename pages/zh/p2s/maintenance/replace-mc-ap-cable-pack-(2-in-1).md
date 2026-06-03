---
path: zh/p2s/maintenance/replace-mc-ap-cable-pack-(2-in-1)
title: "更换 P2S/X2D MC-AP 线缆"
description: ""
tags: []
created: 2025-10-14T13:13:58.317Z
updated: 2026-04-30T06:15:57.455Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-mc-ap-cable-pack-(2-in-1)
---

## MC-AP 线

连接 P2S/X2D 打印机 MC 板和 AP 板的 2 根黑色连接线，分别能实现 MC 板与 AP 板之间的数据交互和为 AP 板提供电源。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/cab044.jpg)

## 何时更换

- 两端的插头有物料损坏，影响安装；
- 连接线有明显的损伤或断路；
- 拓竹服务团队通过日志文件确认的连接线有异常。

## 需要的工具和材料

- 新的 MC-AP 线缆
- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 MC-AP 线缆

### 步骤 1：移除背板

您可以参考这篇 Wiki 来移除 P2S 打印机背板：[更换 P2S 背板 | Bambu Lab Wiki](replace-rear-panel.md)

![rear_panel_screws_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/rear_panel_screws_010.png)

![remove_the_rear_cover_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/remove_the_rear_cover_006.png)

您可以参考这篇 Wiki 来移除 X2D 打印机背板：[更换 X2D 背板 | Bambu Lab Wiki](../../x2d/maintenance/replace-rear-panel.md)

### 步骤 2：移除 AP 板盖

您可以参考这篇 Wiki 来移除 AP 板盖：[更换 P2S/X2D AP 板盖/LED 补光灯 - 左 | Bambu Lab Wiki](replace-ap-board-cover-and-led-light-left.md)

### 步骤 3：移除废料滑梯

使用 H1.5 内六角扳手移除四颗固定螺丝（BT2x5），然后将废料滑梯取下。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 4：断开 MC-AP 线缆连接

> X2D 与 P2S 的连接器位置相同

1. 按压插头卡扣，将 MC-AP 的连接线从 AP 板上的两个连接器断开，并从线扣中移除；

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/02_002.png)

2. 按压插头卡扣，将 MC-AP 连接线从 MC 板上的两个连接器中断开连接。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/01_001.png)

### 步骤 5：移除 MC-AP 线

1. 先将最外侧的工具头线缆从线槽中取出，再将 MC-AP 连接线依次从线槽中释放出来；

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/03_003.png)

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/04_004.png)

2. 然后如图所示，分别将两根 MC-AP 线缆从线槽中拉出，取下线缆。

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/05_005.png)

## 安装 MC-AP 线

### 步骤 1：穿线

1. 如下图所示，将 MC-AP 连接线的穿过过线孔；

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/06_006.png)

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/07_007.png)

![08_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/08_008.png)

2. 然后将线依次整理入线槽内。先将 MC-AP 线整理进线槽中，再将工具头线缆卡入。

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/04_004.png)

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/03_003.png)

### 步骤 2：连接线缆

1. 在将线材连接前，请确认好卡扣的方向。AP 板侧需要连接 2 根电缆，连接器位置如图所示。将线缆与 AP 板连接后，再将线缆卡入 AP 板右侧的线扣中；

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/02_002.png)

2. 参考下图将 MC-AP 连接线连接到 MC 板上。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-ap-cable-pack/01_001.png)

### 步骤 3：安装废料滑梯

将废料滑梯安装至打印机上，使用 H1.5 内六角扳手拧紧四颗固定螺丝（BT2x5）。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

### 步骤 4：安装 AP 板盖

您可以参考这篇 Wiki 将 AP 板盖重新装回：[更换 P2S/X2D AP 板盖/LED 补光灯 - 左 | Bambu Lab Wiki](replace-ap-board-cover-and-led-light-left.md)

### 步骤 5：安装背板

您可以参考这篇 Wiki 将 P2S 的背板重新装回：[更换 P2S 背板 | Bambu Lab Wiki](replace-rear-panel.md)

您可以参考这篇 Wiki 来安装 X2D 打印机背板：[更换 X2D 背板 | Bambu Lab Wiki](../../x2d/maintenance/replace-rear-panel.md)

## 如何验证成功

连接打印机电源，开启打印机，确认显示屏能正常启动且能正常发起打印。

否则，请再次检查所有连接并重试。如果仍然不行，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
