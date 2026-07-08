---
path: zh/ams-ht/maintenance/ams-ht-feeder-unit-magnet-installation
title: "更换 AMS HT 进料检测传感器磁铁"
description: "本文介绍了如何移除和安装位于 AMS HT 上下料组件的进料检测传感器的磁铁与弹簧。"
tags: []
created: 2026-06-30T06:30:24.602Z
updated: 2026-07-02T06:09:27.328Z
source: https://wiki.bambulab.com/zh/ams-ht/maintenance/ams-ht-feeder-unit-magnet-installation
---

> **说明：本文内容不属于常规产品维护流程，主要面向因拆除进料检测传感器霍尔板时内部磁铁不慎弹出的用户，指导其如何将磁铁重新装回。**

## AMS HT 进料检测传感器磁铁

AMS HT 上下料组件的进料检测传感器霍尔板下方装有一片磁铁，用于检测耗材位置。当耗材到达上下料组件时，会将磁铁顶起；进料检测传感器随即感应到磁铁的位移，当达到阈值时，即判定耗材已插入。

![note_magnet_and_spring.jpg](https://wiki.bambulab.com/filament-acc/acc/replacing-the-pneumatic-connector/note_magnet_and_spring.jpg)

## 适用机型

AMS HT

## 何时使用

在更换电机或上下料组件等相关部件时，可能需要移除进料检测传感器霍尔板，此时磁铁和弹簧可能会弹出。在这种情况下，请按照本文的操作指引重新装回磁铁。

## 所需工具和材料

- H2.0 & H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除磁铁

### 1. 移除 AMS HT 背面铁氟龙料管

从 AMS HT 背面按压料管释放按钮，解锁接头，然后从 AMS HT 背面拉出料管。

![取出料管.jpg](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/%E5%8F%96%E5%87%BA%E6%96%99%E7%AE%A1.jpg)

### 2. 取出 AMS HT 中框

首先需要拆下料槽的**从动支撑轴**和**主动支撑轴**，取出轴承套时，小心两端的轴承，避免丢失。

|  |  |
| --- | --- |
|  |  |

移除底部两颗螺丝（BT3\*8）。

![3.底壳螺丝.jpg =800x](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/3.%E5%BA%95%E5%A3%B3%E8%9E%BA%E4%B8%9D.jpg)

移除螺丝后缓慢向上拉动中框组件。

|  |  |
| --- | --- |
|  |  |

打开缝隙后向上提起中框组件，**注意有电缆连接，请勿暴力操作**。

|  |  |
| --- | --- |
|  |  |

### 3. 取下上下料组件

按压气动接头黑色垫圈，同时拔出料管。

![disconnect_ht_ptfe_tube.jpg](https://wiki.bambulab.com/filament-acc/acc/replacing-the-pneumatic-connector/disconnect_ht_ptfe_tube.jpg)

按压底座解锁，拔出上下料组件线缆与上下料电机线缆。

![feeder_and_motor_cables.png](https://wiki.bambulab.com/filament-acc/acc/replacing-the-pneumatic-connector/feeder_and_motor_cables.png)

移除上下料器 4 颗固定螺丝（黑色）。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/42%E4%B8%8A%E4%B8%8B%E6%96%99%E7%BB%84%E4%BB%B64%E9%A2%97%E8%9E%BA%E4%B8%9D.jpg)

按住耗材释放按钮即可将上下料组件推出。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/3.%E6%8E%A8%E5%87%BA%E7%94%B5%E6%9C%BA.jpg)

### 4. 移除磁铁

首先，移除下图标记的一颗螺丝，然后将这块小电路板移开。

![feeder_silver_screws_i.jpg](https://wiki.bambulab.com/filament-acc/acc/replacing-the-pneumatic-connector/feeder_silver_screws_i.jpg)

使用扳手将磁铁和弹簧吸附取出。

> **注意**：零件细小，请注意缓慢操作，避免零件丢失。

![removing_magnet.webp](https://wiki.bambulab.com/ams/ams-ht/install-the-magnets-in-feeder-unit/removing_magnet.webp)

## 安装磁铁

### 1. 安装磁铁

将磁铁吸附至扳手上，缓慢放入安装孔位中。

|  |  |
| --- | --- |
|  |  |

将弹簧较小的一端吸附至磁铁上。

|  |  |
| --- | --- |
|  |  |

放回小电路板，拧入下图标记的一颗螺丝。

![feeder_silver_screws_i.jpg](https://wiki.bambulab.com/filament-acc/acc/replacing-the-pneumatic-connector/feeder_silver_screws_i.jpg)

### 2. 安装上下料组件

将上下料组件装回中框组件，并拧入4颗黑色固定螺丝。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/42%E4%B8%8A%E4%B8%8B%E6%96%99%E7%BB%84%E4%BB%B64%E9%A2%97%E8%9E%BA%E4%B8%9D.jpg)

将料管插入气动接头。

![insert_ptfe_tube.jpg](https://wiki.bambulab.com/filament-acc/acc/replacing-the-pneumatic-connector/insert_ptfe_tube.jpg)

插入上下料组件线缆与上下料电机线缆。

![feeder_and_motor_cables.png](https://wiki.bambulab.com/filament-acc/acc/replacing-the-pneumatic-connector/feeder_and_motor_cables.png)

### 3. 安装中框组件

用手指勾住凸出的线缆，将中框组件安装至下盖组件内。

|  |  |
| --- | --- |
|  |  |

需要确保中框组件完全压入下壳组件且前后没有翘起的情况，安装底部两颗固定螺丝（BT3\*8）。

|  |  |
| --- | --- |
|  |  |

### 4. 安装主动支撑轴和从动支撑轴

主动支撑轴压入 AMS HT 前端槽内，直到听到“咔嗒”声，注意主动支撑轴黑色齿轮一端需要和中框组件内的黄色齿轮一端对齐。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/2%E5%AE%89%E8%A3%85%E4%B8%BB%E5%8A%A8%E8%BD%B4.jpg)

将从动支撑轴压入中框组件内，直到听到“咔嗒”声。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/%E4%BB%8E%E5%8A%A8%E8%BD%B4%E3%80%81.jpg)

> 注意：安装完成后可以手动转动**主动支撑轴和从动支撑轴**，需要确保旋转顺滑。

## 功能验证

将 AMS HT 连接到打印机并打开电源。将耗材插入进料口中，然后单击屏幕上的“进料”。如果能够成功进退料，则安装正常。

否则，请检查电缆和铁氟龙料管的连接后重试。如果未发现异常但仍出现故障，请联系 Bambu Lab 服务团队以获得进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
