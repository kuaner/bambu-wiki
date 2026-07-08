---
path: zh/x1/maintenance/install-the-magnets-in-filaments-hub
title: "移除和安装 AMS 五通磁铁"
description: "清洁五通组件时候，如果内部磁铁松出，可参考此文进行安装"
tags: ["ams"]
created: 2022-10-13T11:07:04.496Z
updated: 2026-06-30T04:10:12.353Z
source: https://wiki.bambulab.com/zh/x1/maintenance/install-the-magnets-in-filaments-hub
---

**声明：本文所写内容不属于正常产品维护的内容，本文的目的在于帮助一些误拆五通电路板导致内部磁铁弹出的用户，指导他们如何把磁铁装回去。如果您没有可以用来辅助拆装的磁铁，请不要尝试本文所写的任何步骤。**

## AMS 五通磁铁

AMS 五通组件的4个进料孔内各有一片磁铁，用于检测料线位置.当料线到达五通时会把对应位置的磁铁往上顶，在上面的选料板会检测到磁铁在往上，当达到阈值时就知道有料到了。

![](https://wiki.bambulab.com/x1/maintenance/install-filaments-hub-magnets/magnets.jpg)

## 何时使用

清理五通内的材料碎片时，可能会涉及到拆开选料板，这时这些磁铁很大可能会弹出来，在这种情况下，就需要根据操作指引装回4片磁铁。

## 所需工具和材料

- 条形磁铁（辅助拆装，需要自备）
- H2.0 & H1.5 内六角扳手
- 镊子

## 开始运行前的安全警告和机器状态

关闭打印机电源并断开AMS与打印机的连接。

## 拆卸指南

### 步骤 1 - 拆下五通组件

请参考 [更换AMS五通组件](replace-filament-hub.md) 将五通组件的从AMS上拆下和分离电机。

### 第 2 步 - 将辅助磁铁贴装在五通上

|  |  |
| --- | --- |
|  |  |

### 第 3 步 - 移除选料板

用H1.5内六角扳手拆下固定选料板的3颗螺丝，移除选料板。

![](https://wiki.bambulab.com/x1/maintenance/install-filaments-hub-magnets/3_screws.jpg)

### 第 4 步 - 移除弹簧

用镊子依次移除4根弹簧，注意保存好弹簧，防止丢失。

![](https://wiki.bambulab.com/x1/maintenance/install-filaments-hub-magnets/remove_springs.jpg)

### 第 5 步 - 取下磁铁

使用内六角扳手可以很方便地将磁铁逐个取出。

![](https://wiki.bambulab.com/x1/maintenance/install-filaments-hub-magnets/remove_magnets.jpg)

## 安装指南

### 第 1 步 - 安装磁铁

保持辅助磁铁在五通组件的另一面，将4块磁铁如下图所示吸附在一起，然后将磁铁逐个塞入相应的槽位中，注意安装方向。

|  |  |
| --- | --- |
|  |  |

### 第 2 步 - 装上弹簧

 将弹簧逐个放置到已安装的磁铁上方。

![](https://wiki.bambulab.com/x1/maintenance/install-filaments-hub-magnets/install_springs.jpg)

### 第 3 步 - 安装选料板

安装选料板，并锁入 3 颗螺丝进行固定。

|  |  |
| --- | --- |
|  |  |

### 第 4 步 - 安装五通组件

请参考 [更换AMS五通组件](replace-filament-hub.md) 将电机安装到五通组件上，然后将AMS组装好。

## 如何验证完成/成功

将 AMS 连接到打印机并打开电源。将打印材料加载到 AMS 的所有料槽中，然后单击屏幕上的“进料”开始加载打印丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/494px-load1.png)

1号料槽进完料后，点出2号料槽图标加载2号料槽的打印丝，以此类推，直至4个料槽都完成一次进料、退料的操作。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/485px-load234.png)

如果所有进退料过程都表现正常，则安装正常。

否则，请检查电缆和PTFE管的连接后重试。如果未发现异常但仍出现故障，请联系 Bambu Lab 服务团队以获得进一步帮助。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
