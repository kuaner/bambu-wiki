---
path: zh/r1/maintenance/replace-optical-sensor-module
title: "光学传感器模组更换指南"
description: ""
tags: []
created: 2026-09-22T13:11:08.524Z
updated: 2026-09-22T13:11:09.769Z
source: https://wiki.bambulab.com/zh/r1/maintenance/replace-optical-sensor-module
---

## 光学传感器模组 Optical Sensor Module

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/001.png)

光学传感器模组，负责精细拍照、测距、曲面和圆柱扫描等功能。

## 所需工具和材料

- H1.5 内六角螺丝刀
- H2.0 内六角螺丝刀

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 移除光学传感器模组

### 步骤 1.移除工具头前盖

使用 H1.5 内六角螺丝刀拆卸图示两颗螺丝。

|  |  |
| --- | --- |
| 002.jpg | 003.jpg |

取下工具头前盖。

![004.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/004.webp)

### 步骤 2.移除接口板

接口板线缆较短，请小心操作。

1、2、3号插头需要先打开排线扣，然后向上抬出排线（排线有防松结构，不可直接向后暴力拔出）。4号插头请小心向下拔出。

![005.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/005.jpg)

拧下四颗螺丝，取下接口板，注意此时接口板仍然有线缆未断开。

![006.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/006.jpg)

断开接口板正面2、3号插头，翻转TH板，断开背面两个插头。然后取下接口板。

![007.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/007.webp)

### 步骤 3.移除光学传感器模组

断开图示插头，使用 H2.0 内六角螺丝刀拧下两颗螺丝，向外拔出光学传感器模组。

|  |  |
| --- | --- |
| 008.jpg | 009.png |

## 安装光学传感器模组

### 步骤 1.安装光学传感器模组

连接光学传感器模组插头。

> 注意：此处2PIN插头为白绿线缆，请勿与其他插头插错。

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/010.png)

装回光学传感器模组，使用 H2.0 螺丝刀锁入两颗螺丝固定。

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/011.png)

### 步骤 2.安装接口板

翻转接口板，连接背面两处插头。

> 注意：此处2PIN插头为红黑线缆，请勿与其他插头插错。

![012.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/012.webp)

使用 H1.5 内六角螺丝刀锁入三颗螺丝固定接口板。

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/013.png)

连接接口板三处排线和一处插头。

|  |  |
| --- | --- |
| 014.webp | 015.webp |

### 步骤 3.安装工具头前壳

将工具头前盖装回工具头。

![016.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-optical-sensor-module/zh/016.jpg)

使用 H1.5 内六角螺丝刀锁入两颗螺丝固定。

|  |  |
| --- | --- |
| 017.jpg | 018.jpg |

## 功能验证

更换完成后，请通过屏幕选择：**设置>校准>视觉精度校准**选项，重新运行视觉精度校准。如果校准正常结束则上述安装正确。

|  |  |
| --- | --- |
| 019.png | 020.png |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。
>
> 如果问题仍未解决，请提交 [服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5) 并附上您近期的设备日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。
>
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
