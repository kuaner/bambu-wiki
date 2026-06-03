---
path: zh/p2s/maintenance/replace-inner-lining
title: "更换 P2S 内衬"
description: ""
tags: []
created: 2025-10-14T13:15:14.439Z
updated: 2025-10-14T13:28:13.048Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-inner-lining
---

## 内衬

内衬是位于打印机后部的塑料支架，用于承载 MC 板、AC 板、电源模块等电路配件，并将其与打印腔室隔离。

## 何时更换

1. 内衬出现变形损坏

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除内衬

### 步骤 1：移除背板

您可以参考这篇 Wiki 来移除打印机背板：[更换 P2S 背板 | Bambu Lab Wiki](replace-rear-panel.md)

![rear_panel_screws_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/rear_panel_screws_010.png)

![remove_the_rear_cover_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/remove_the_rear_cover_006.png)

### 步骤 2：移除 AC/MC 板 和电源

您可以参考以下两篇 Wiki，将 AC板、MC 板和电源从内衬上移除：  
[更换 P2S AC/MC 板 | Bambu Lab Wiki](replace-mc-and-ac-boards.md)  
[更换 P2S 电源 | Bambu Lab Wiki](replace-power-supply.md)

> MC 板供电线可与电源保持连接并与电源一起取下。

### 步骤 3：移除自适应风道切换组件

您可以参考这篇 Wiki 来移除自适应风道切换组件：[更换自适应风道切换组件 | Bambu Lab Wiki](replace-adaptive-airflow-switching-unit.md)

### 步骤 4：移除左侧板

由于热床地线固定在立柱上，您需要先移除左侧板。您可以参考这篇 Wiki 来移除左侧板：[更换 P2S 左侧板 | Bambu Lab Wiki](replace-left-side-panel.md)

### 步骤 5：移除热床

您可以参考这篇 Wiki 来移除热床：[更换 P2S 热床 | Bambu Lab Wiki](replace-heatbed.md)  
使用 H2.0 内六角扳手移除七颗热床固定螺丝（BT3x5），即可取下热床。

![12_full_view_of_heated_bed_screws_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-heatbed/12_full_view_of_heated_bed_screws_012.png)  
您只需要将热床从三个滑块上移除并放置到底座上。

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/02_002.png)

### 步骤 6：移除空气滤芯/吐料组件

您可以参考这两篇 Wiki 来移除空气滤芯和吐料组件：

[更换 P2S 空气滤芯盖和空气滤芯 | Bambu Lab Wiki](replace-air-filter.md)

[更换 P2S 吐料组件 | Bambu Lab Wiki](replace-purge-wiper.md)

### 步骤 7：移除内衬

1. 使用 H2.0 内六角扳手移除 6 颗固定螺丝；

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/01_001.png)

2. 将工具头线缆、A 电机连接线、MC-AP 线缆从内衬的线槽中抽出；

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/03_003.png)

3. 将内衬往上提起，然后倾斜将内衬取出。在取出时需注意避让右侧板的螺丝柱。

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/04_004.png)

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/05_005.png)

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/07_007.png)

## 安装内衬

### 步骤 1：安装内衬

1. 将内衬倾斜装入，然后使用 H2.0 内六角扳手拧紧 6 颗固定螺丝；

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/05_005.png)

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/04_004.png)

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/06_006.png)

2. 将工具头线缆、A 电机连接线、MC-AP 线缆依次穿过内衬的线槽中。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-inner-lining/03_003.png)

### 步骤 2：安装电源、AC 板和 MC 板

您可以参考以下两篇 Wiki ，分别将电源、AC 板和 MC 板装回原位：  
[更换 P2S 电源 | Bambu Lab Wiki](replace-power-supply.md)  
[更换 P2S AC/MC 板 | Bambu Lab Wiki](replace-mc-and-ac-boards.md)

### 步骤 3：安装热床

您可以参考这篇 Wiki 将热床装回原位：  
[更换 P2S 热床 | Bambu Lab Wiki](replace-heatbed.md)

### 步骤 4：安装左侧板

您可以参考这篇 Wiki 将左侧板装回原位：[更换 P2S 左侧板 | Bambu Lab Wiki](replace-left-side-panel.md)

### 步骤 5：安装自适应风道切换组件

您可以参考这篇 Wiki 将自适应风道切换组件装回原位：[更换自适应风道切换组件 | Bambu Lab Wiki](replace-adaptive-airflow-switching-unit.md)

### 步骤 6：安装空气滤芯/吐料组件

您可以参考这两篇 Wiki 将空气滤芯和吐料组件装回原位：

[更换 P2S 空气滤芯盖和空气滤芯 | Bambu Lab Wiki](replace-air-filter.md)  
[更换 P2S 吐料组件 | Bambu Lab Wiki](replace-purge-wiper.md)

### 步骤 7：安装背板

您可以参考这篇 Wiki 将打印机背板装回原位：[更换 P2S 背板 | Bambu Lab Wiki](replace-rear-panel.md)

### 步骤 8：手动调平热床

您可以参考这篇 Wiki 来对热床进行手动调平：[P2S 热床手动调平 | Bambu Lab Wiki](manual-bed-tramming.md)

## 如何验证成功

由于在更换过程中所需拆装的部件较多，请在更换后连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆连接是否正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
