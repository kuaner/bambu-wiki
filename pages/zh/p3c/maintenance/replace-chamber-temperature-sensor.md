---
path: zh/p3c/maintenance/replace-chamber-temperature-sensor
title: "P3C 腔温检测传感器更换指南"
description: "本文介绍了如何更换 P3C 腔温检测传感器"
tags: []
created: 2026-11-24T14:06:23.924Z
updated: 2026-11-24T14:06:23.924Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-chamber-temperature-sensor
---

## 腔温检测传感器

简述：

腔温检测传感器是安装在打印机上盖右侧，用于检测打印机腔内温度的 NTC 。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-temperature-sensor/zh/001.png)

## 何时更换

1. 腔温检测传感器连接线损坏；
2. 腔温报错经 Bambulab 技术团队确认需更换的。

## 所需工具和材料

- H2.0 内六角扳手
- 平口螺丝刀或平口撬棍
- 腔温检测传感器

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除腔温检测传感器

### 步骤 1. 移除维修盖板

您可以参考WiKi：[P3C 维修盖板更换指南](replace-service-panel.md)，使用 H2.0 内六角扳手移除右侧板上维修盖板 4 颗螺丝后将其取下，露出闪切挂架控制板。

|  |  |
| --- | --- |
| 002.png | 003.png |

### 步骤 2. 移除腔温检测传感器

撕下磁环固定胶布，随后使用撬棍或平口螺丝刀去除腔温检测传感器固化胶；

|  |  |
| --- | --- |
| 004.png | 005.webp |

按压腔温检测传感器线缆端子解锁卡扣断开连接，随后抽出传感器。

|  |  |
| --- | --- |
| 006.png | 007.png |

## 安装腔温检测传感器

### 步骤 1. 安装腔温检测传感器

将腔温检测传感器的探头插入打印机上盖的预留检测孔，并卡入支架完成固定；可从腔内侧检查传感器探头是否插入到位。

|  |  |
| --- | --- |
| 008.png | 009.webp |

随后将接头插入闪切挂架接口，并将磁环胶布贴回原位。

![010.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-temperature-sensor/zh/010.png)

### 步骤 2. 安装维修盖板

将维修盖板对准安装槽装入，并向内按压盖板边缘，伴随连续的卡扣声响，确认所有卡扣安装到位。随后锁入 4 颗螺丝固定。

![011.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-temperature-sensor/zh/011.png)

## 功能验证

连接电源并打开打印机，检查打印机腔温是否显示正常。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
