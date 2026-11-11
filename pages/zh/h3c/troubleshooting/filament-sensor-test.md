---
path: zh/h3c/troubleshooting/filament-sensor-test
title: "拓竹H3C 打印头进料霍尔排查指南"
description: ""
tags: []
created: 2026-11-03T12:08:51.669Z
updated: 2026-11-10T12:02:34.487Z
source: https://wiki.bambulab.com/zh/h3c/troubleshooting/filament-sensor-test
---

## 进料霍尔传感器

打印头上的进料霍尔传感器用于检测耗材是否插入或退出打印头。当耗材插入打印头时，磁铁摇臂会更加靠近传感器，从而判断耗材已插入。

## 故障可能

- 磁铁摇臂被卡住，无法回弹
- 磁铁脱落
- 传感器故障

### 所需工具

- H1.5 内六角扳手
- H2.0 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 排查步骤

### 步骤一：故障确认

放置当前使用的打印头，等待降温。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/filament-sensor-test/zh/03_h3c___________-01.png)

当喷嘴温度降低到26℃左右后，拆卸左右两侧的 AMS 磁吸侧板，取下打印头。

|  |  |
| --- | --- |
| 图 | 图 |

按压打印头上的黑色压块，向前轻推料管，再向外拔出。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/filament-sensor-test/zh/03_h3c___________-04.webp)

将料管塞入侧孔备用。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/filament-sensor-test/zh/03_h3c___________-05.png)

使用一截耗材，观察插入/拔出后 AMS 页面的显示变化。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/filament-sensor-test/zh/03_h3c___________-06.png)

若插入后线条变成实线，拔出后线条变为虚线，则传感器工作正常。

|  |  |
| --- | --- |
| 图 | 图 |

若插入或者拔出耗材后，线条不发生变化，则进行后续故障排查。

### 步骤二：故障确认

关闭打印机电源后，拧松固定热端的3个螺丝，取下热端。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/filament-sensor-test/zh/03_h3c___________-09.png)

拧松打印头前盖的 4 颗固定螺丝，取下打印头前盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/filament-sensor-test/zh/03_h3c___________-10.png)

拧松打印头电路板的 2 颗固定螺丝  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/filament-sensor-test/zh/03_h3c___________-11.png)

小心翻折打印头电路板，检查摇臂上的方形磁铁是否脱落。  
若磁铁脱落则需要[更换打印头基座](../maintenance/replace-printtool.md)。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/filament-sensor-test/zh/03_h3c___________-12.png)

若摇臂无法回弹，可以拧下固定摇臂的螺丝，检查内部杂质，确保摇臂回弹正常。

|  |  |
| --- | --- |
| 图 | 图 |

确保摇臂状态正常后，复原打印头重新进行测试，若故障依旧则可能是传感器故障，需要[更换打印头基座](../maintenance/replace-printtool.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
