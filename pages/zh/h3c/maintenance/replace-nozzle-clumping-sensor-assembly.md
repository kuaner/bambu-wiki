---
path: zh/h3c/maintenance/replace-nozzle-clumping-sensor-assembly
title: "裹头检测组件更换指南"
description: ""
tags: []
created: 2026-11-03T12:46:45.578Z
updated: 2026-11-03T12:47:22.769Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-nozzle-clumping-sensor-assembly
---

## 裹头检测组件

裹头检测组件主要由两部件组成，一是检测霍尔板，二是检测弹片。  
检测弹片是安装在工具定位槽下方的，工具定位槽这个单品也已预装了检测弹片。一般情况下，如果发现弹片有变形，导致误报，[更换工具定位槽](replace-tool-holder.md) 即可，操作更加简单。如果确实是检测霍尔板出现故障，可参考本指引更换检测霍尔板。

## 何时更换

- 检测霍尔板失效
- 结构件出现物理损坏

## 工具和材料

- H1.5 内六角扳手
- H2.0 内六角扳手
- 镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除裹头检测组件

### 第 1 步 移除工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，移除 工具头前盖和顶盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-clumping-sensor-assembly/zh/08_____________dock_alignment_sensor_replacement_guide_88cc28be87.jpg)

### 第 2 步 移除部件冷却风扇螺丝

用 H1.5 内六角扳手移除工具头左右两侧及背部固定部件冷却风扇 3 颗螺丝，将部件冷却风扇松出。

|  |  |
| --- | --- |
| 图 | 图 |
| 图 | 图 |

### 第 3 步 移除工具定位槽

用 H2.0 内六角扳手，移除 4 颗螺丝，取下工具定位槽。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-clumping-sensor-assembly/zh/94____________nozzle_clumping_sensor_assembly_replacement_guide_af34abc024.jpg)

### 第 4 步 移除检测弹片（此步骤在只是更换检测霍尔板时不需要操作）

推开工具定位槽上的硅胶，用 H1.5 内六角扳手移除 2 颗螺丝，取下裹头检测弹片。

|  |  |
| --- | --- |
| 图 | 图 |

移除硅胶套。

### 第 5 步 移除裹头检测霍尔板

断开工具头接口板右侧的白色连接插头，用镊子轻微撬开线材卡扣，将检测霍尔板的线缆从卡扣上松出。

|  |  |
| --- | --- |
| 图 | 图 |

用 H1.5 内六角扳手，从工具头滑车底部移除 1 颗固定霍尔板的螺丝，然后将线缆从滑车卡扣上松出，取下裹头检测霍尔板。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装裹头检测组件

### 第 1 步 安装检测弹片（此步骤在只是更换检测霍尔板时不需要操作）

将检测弹片锁到工具定位槽上，锁入 2 颗螺丝固定。

|  |  |
| --- | --- |
| 图 | 图 |

将硅胶套装回到工具定位槽上，注意不要将弹片包裹进去，用镊子检查安装状态，确保硅胶套与弹片无干涉。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 安装裹头检测霍尔板

将裹头检测霍尔板安装到滑车底部，锁入 1 颗螺丝固定，然后将线缆卡进卡扣中。

|  |  |
| --- | --- |
| 图 | 图 |

将检测霍尔板的线缆从下往上依次卡进 3 个卡扣中，用镊子将卡扣恢复到正常状态，然后将线缆连接到工具头接口板右侧白色连接器上。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 3 步 安装工具定位槽

将工具定位槽装到工具头上，锁入 4 颗螺丝固定。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-clumping-sensor-assembly/zh/94____________nozzle_clumping_sensor_assembly_replacement_guide_af34abc024.jpg)

### 第 4 步 锁部件冷却风扇螺丝

将部件冷却风扇装到工具头底部，对齐螺丝孔，在工具头左右两侧及背部锁入 3 颗部件冷却风扇固定螺丝。

|  |  |
| --- | --- |
| 图 | 图 |
| 图 | 图 |

### 第 5 步 安装工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，安装 工具头顶盖和前盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-clumping-sensor-assembly/zh/08_____________dock_alignment_sensor_replacement_guide_3f758f3bab.jpg)

## 功能验证

连接电源并启动打印机，自检无报错即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
