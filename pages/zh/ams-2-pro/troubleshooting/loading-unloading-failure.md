---
path: zh/ams-2-pro/troubleshooting/loading-unloading-failure
title: "AMS 2 Pro 进退料失败故障排查"
description: "本文将总结 AMS  2 Pro 进退料失败的故障排查方法。"
tags: ["ams 2 pro"]
created: 2026-06-15T08:45:59.989Z
updated: 2026-06-26T06:26:41.382Z
source: https://wiki.bambulab.com/zh/ams-2-pro/troubleshooting/loading-unloading-failure
---

本文介绍了 AMS 2 Pro 常见的进退料故障的排查方法。当您在打印机的过程中遇到了进退料失败的问题，您可以根据报错信息以及故障现象来参考本文进行故障排查。

> 建议您先了解[AMS 2 Pro 工作流程和功能介绍](../manual/setup-and-printting.md)，再根据本文进行故障排查。

## 预上料异常

在 AMS 2 Pro 空闲时插入耗材丝，会进行预上料工作。上下料器会把耗材送入五通组件，待五通组件的传感器检测到耗材后再拉回。如果预上料过程存在异常，则有以下几种可能性：

### 上下料传感器异常

#### 现象

耗材插入后没有自动送入动作且指示灯熄灭，或耗材未插入时指示灯常亮。

#### 故障排查

请参考[AMS 2 Pro 上下料组件堵塞清理](../maintenance/filament-funnel-cleaning.md)检查磁铁是否被磨出凹槽，以及检查上下料组件中是否存在堵塞。

- 若磁铁磨损，则需要[更换新的上下料组件](../maintenance/replace-feeder-unit.md)。
- 若存在堵塞，取出堵塞物后可重新插入耗材测试，故障依旧请联系客户支持团队。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E7%A3%A8%E6%8D%9Fzh.png)

### 上下料电机异常

耗材插入 AMS 2 Pro 后，上下料电机和齿轮将会开始转动，若电机并没有任何转动迹象，请参考[更换上下料组件](../maintenance/replace-feeder-unit.md)重新安装上下料组件线缆，若故障依旧则需要更换新的上下料组件。

![12.webp](https://wiki.bambulab.com/ams-2-pro/troubleshooting/loading-unloading-failure/12.webp)

### 五通传感器异常

取下五通组件上该槽位对应的料管，并插入一截耗材，观察屏幕上是否有图标变化。

|  |  |
| --- | --- |
|  |  |

1. 若 AMS 中线条变粗，则故障和料管或上下料组件有关。

重新安装该槽位料管，并往里挤压一次，确保料管准确插入气动接头中。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/disassembly-and-assembly/image-11.png)

若故障依旧则需要[更换上下料组件](../maintenance/replace-feeder-unit.md)。

2. 若没有图标变化，则该槽位的传感器可能存在故障，请参考重新连接传感器线缆后再次验证，若故障依旧则需要[更换五通组件](../maintenance/replace-internal-hub-unit.md)。

## 进料失败

> 进退料失败可根据报错内容进行检查，本文以 P2S 为例，其他机型可在主页搜索相关教程。

### 耗材送出 AMS 2 Pro 失败：

请抽出该槽位耗材，观察耗材上是否有磨损痕迹，剪断这截耗材后重新进料。若故障依旧可更换其他耗材尝试。

|  |  |
| --- | --- |
|  |  |

若多卷耗材都出现该情况，请参考以下教程，清理五通组件的滚花齿，并确保里程轮转动顺畅不卡涩。

| AMS 型号 | 里程轮位置 | 相关教程 |
| --- | --- | --- |
| AMS 2 Pro | pixpin_2026-06-12_17-08-04.jpg | [清理教程](clean-the-filaments-hub.md) |

若五通组件外观正常，但耗材依然无法送出 AMS，则需要[更换新的五通组件](../maintenance/replace-internal-hub-unit.md)。

### 耗材送往挤出机失败：

观察耗材送出后的运输情况，根据最后卡住的位置进行检查。

1. 若耗材卡在 **AMS - 缓冲器** 之间，请检查该料管是否弯折、变形，建议更换新的料管。

![ams.jpg](https://wiki.bambulab.com/ams-2-pro/troubleshooting/loading-unloading-failure/ams.jpg)

2. 若耗材卡在 **缓冲器 - 工具头** 之间，请检查该处料管是否弯折、变形，建议更换新的料管。

![进料口.jpg](https://wiki.bambulab.com/ams-2-pro/troubleshooting/loading-unloading-failure/%E8%BF%9B%E6%96%99%E5%8F%A3.jpg)

> 以上两种情况若更换新料管后依然卡在相同位置，请[检查五通组件](#filament-hub-1)。

3. 若耗材已经送入了工具头中，则说明工具头中的耗材传感器可能存在故障，请参考[霍尔开关故障排查指南](../../x1/troubleshooting/filament-sensor-test.md)进行排查。

### 耗材挤出异常：

根据[P2S 堵塞排查](../../p2s/troubleshooting/clogging.md)确定挤出机、喷嘴的堵塞情况，并完成疏通清理。

清理完成后可尝试再次使用 AMS 进料，若故障依旧，请取下 AMS，通过外挂料盘发起打印。

- 若外挂料盘打印成品质量合格，则[检查五通组件](#filament-hub-1)。
- 若外挂料盘打印成品质量出现挤出不足或无法挤出情况，建议更换新的喷嘴。

## 退料失败

分别断开打印机进料口、AMS 2 Pro 背后的料管，裁断耗材后手动拉扯余料，判断失败原因位置。

|  |  |
| --- | --- |
|  |  |

若耗材无法从 AMS 2 Pro 中抽出，则是 AMS 2 Pro 内部存在堵塞，需[检查五通组件](#filament-hub-1)。

若耗材无法从打印机进料口中抽出，则可能是切刀磨损后无法切断耗材，或挤出机存在堵塞，可参考[P2S 挤出机堵塞清理指南](../../p2s/maintenance/extruder-cleaning-guide.md)清理挤出机并更换新的切刀刀片。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
