---
path: zh/ams-2-pro/maintenance/filament-funnel-cleaning
title: "AMS 2 Pro 上下料组件堵塞清理"
description: "AMS 2 Pro 上下料组件堵塞清理及上下料电机故障排查"
tags: []
created: 2025-09-19T02:49:01.594Z
updated: 2026-02-27T10:40:32.934Z
source: https://wiki.bambulab.com/zh/ams-2-pro/maintenance/filament-funnel-cleaning
---

## 何时清理

当 AMS 2 Pro（文中简称AMS）上下料组件出现进退料故障时；  
当 AMS 2 Pro 上下料中能够明显观察到耗材碎屑时；

## 入料口组件故障现象

AMS 2 Pro 的每个上下料组件均配备有传感器，该传感器位于入料口组件。当插入一小段耗材到入料口时，耗材将推动传感器的圆柱磁铁（如下图）移动，从而触发传感器检测，驱使上下料组件的齿轮转动，并自动将耗材拉入 AMS。

在日常使用中，常见的异常情况包括：

1. 插入 10 cm 耗材后，上下料组件传感器始终检测不到耗材；
2. 在未插入耗材的情况下，上下料组件传感器依然检测到存在耗材。

- *您可以参考指示灯状态来判断是否为上下料组件的问题（[AMS 2 Pro 指示灯状态解析](../troubleshooting/led-status.md)）*

![传感器.jpg](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E4%BC%A0%E6%84%9F%E5%99%A8.jpg)

以上问题通常是入料口组件种有残留的耗材碎屑或者断料导致的，**可以尝试用一段耗材反复捅入入料口来清理**，然后根据 LED 灯状态判断传感器是否恢复正常。如果仍然无法恢复，请参考以下指导，进行排查和清洁入料口结构件。

## 上下料组件故障现象

1. 插入耗材后，入料口组件的传感器能检测到耗材，但是电机始终未反应，齿轮无法转动以拉入耗材；
2. 插入耗材后，电机能够带动齿轮转动，但 AMS 无法自动拉入耗材，这种情况通常是上下料组件中存在碎屑。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/clean-the-ams-2-pro-feeder-unit/feed-unit.jpg)

## 所需工具和材料

1. H2.0及H1.5 内六角扳手

2. 镊子

3. 钳子

4. 一段耗材

## 开始操作前的安全警告和机器状态

关闭打印机电源并断开 AMS 与打印机的连接。

## 拆卸工作

### 1. 拆卸上下料组件

请参考 [更换 AMS 2 Pro 上下料组件](replace-feeder-unit.md) 的步骤1~7的内容将需要处理的 AMS 2 Pro 上下料组件拆下并移除料管。

![展示.jpg](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E5%B1%95%E7%A4%BA.jpg)

### 2. 分离底座和上盖

用H1.5内六角扳手移除4颗螺丝。

|  |  |
| --- | --- |
| 螺丝_(2).jpg | 螺丝_(1).jpg |
| 螺丝_(3).jpg | 螺丝_(4).jpg |

分离上盖和底座，**小心移除弹簧**，断开入料口电路板的电缆连接。

|  |  |
| --- | --- |
| 分离_(1).jpg | springandcable.jpg |

### 3. 取出转轴

利用内六角扳手和钳子，将料嘴转轴敲击出来，注意转轴出来的地方要留有避让位置。

![下敲1.jpg](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E4%B8%8B%E6%95%B21.jpg)

### 4. 取下入料口组件

用钳子移除转轴，然后取下 AMS 入料口组件 。

|  |  |
| --- | --- |
| 取轴.jpg | 取出.jpg |

## 清理工作

### 1. 检查传感器磁铁

使用螺丝刀拆除入料口组件上的电路板。  
![板螺丝.png](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E6%9D%BF%E8%9E%BA%E4%B8%9D.png)

**小心吸出磁铁以及弹簧**，检查磁铁是否磨损，如下图所示。如果磁铁磨损则需要更换新的入料口组件。  
![screenshot-20251010-175721.png](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/screenshot-20251010-175721.png)  
![磨损zh.png](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E7%A3%A8%E6%8D%9Fzh.png)

### 2. 清洁入料口组件

检查磁铁的移动管道中是否存在耗材碎屑，并且用一段耗材反复插入入料口，尝试清除通道以及孔内的堵塞物。

![碎屑.png](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E7%A2%8E%E5%B1%91.png)

如果传感器检测仍无法恢复正常，说明传感器有故障，需要更换入料口组件。

### 3. 清洁上下料组件

使用干净的毛刷清理上下料组件齿轮。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/clean-the-ams-2-pro-feeder-unit/using_brush_to_clean_gears.jpeg)

### 4. 重装上下料电机线缆

重新插拔电机的连接线，若电机依然无法工作，则需要更换上下料组件电机。

![电机连接线.png](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E7%94%B5%E6%9C%BA%E8%BF%9E%E6%8E%A5%E7%BA%BF.png)

## 安装工作

### 1. 安装入料口电路板

磁铁的圆头向下放入孔中，然后放置弹簧，最后安装上下料电路板。

|  |  |
| --- | --- |
| 图片2.png | 板螺丝.png |

### 2. 安装入料口组件

安装 AMS 入料口组件，压入转轴，用钳子将转轴敲到位。

|  |  |
| --- | --- |
| 装轴.jpg | 下敲2.jpg |

### 3. 安装上盖

将弹簧安装到 AMS 入料口组件上，并接上电缆。

|  |  |
| --- | --- |
| 装弹簧.jpg | 弹簧线2.jpg |

调整好齿轮组件的位置，将上盖和底座接合起来，在接合的过程中，用镊子调整弹簧位置并将另一端安装到底座凸柱上。

|  |  |
| --- | --- |
| 位置3.jpg | 对弹簧2.jpg |

![弹簧.webp](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E5%BC%B9%E7%B0%A7.webp)

接合到位后，检查齿轮组的位置，如果位置不对，请调整齿轮位置后重新安装。  
![确认位置.jpg](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-the-feed-funnel-assy/%E7%A1%AE%E8%AE%A4%E4%BD%8D%E7%BD%AE.jpg)

用H1.5内六角扳手依次锁入4颗螺丝固定，锁到位即可，不可大力拧紧，防止滑牙。

|  |  |
| --- | --- |
| 螺丝_(2).jpg | 螺丝_(1).jpg |
| 螺丝_(3).jpg | 螺丝_(4).jpg |

### 4. 安装上下料组件

请参考 [更换 AMS 2 Pro 上下料组件](replace-feeder-unit.md) 的步骤8~14的内容将料管接好，将上下料器安装到AMS上，并组装好AMS。

## 如何验证完成/成功

### 预上料

在 AMS 2 Pro 空闲状态时，插入耗材至进料口，AMS 可以自动预上料（上下料器送料至AMS五通传感器后往回拉）。

### 读取RFID

在屏幕的**设置——AMS选项**里对自动读取RFID功能进行相关设置。  
![](https://wiki.bambulab.com/h2/manual/ams2pro/image.png)  
设置后，AMS 2 Pro 在插料后可以自动读取RFID，或能完成手动读取RFID；并且重启 AMS 后可以自动读取已插入的耗材的RFID信息。  
![](https://wiki.bambulab.com/h2/manual/ams2pro/image-2.png)

具体操作请参考 [AMS 2 Pro 工作流程和功能介绍](../manual/setup-and-printting.md)。

如果以上功能验证可行，则清理完成。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
