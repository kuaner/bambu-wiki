---
path: zh/h3c/maintenance/replace-adaptive-airflow-assembly-right
title: "右自适应风道组件更换指南"
description: ""
tags: []
created: 2026-11-03T12:42:32.968Z
updated: 2026-11-03T12:48:30.501Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-adaptive-airflow-assembly-right
---

## 右自适应风道组件

安装于打印机右侧的加热风道组件，用于固定辅助冷却风扇并集成加热器，为腔室提供主动热源与定向气流。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-adaptive-airflow-assembly-right/zh/37______________adaptive_airflow_assembly_right_replacement_guide_b5232c57bc.jpg)

## 何时更换

- 右腔温加热模块故障
- 右侧风道模式切换故障

## 工具和材料

- H2.0 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 1. 打印机侧板的拆装需要提前移除 AMS 3H，请参考 WIKI： [AMS 3H 拆除与安装指南](replace-ams3.md)，将 AMS 3H 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3H 的场景下进行。
> 2. 根据更换侧板的操作指南，在断电前，先将热床下降到底部。

## 移除右自适应风道组件

### 第 1 步 移除背板

请参考 WIKI: [背板更换指南](replace-back-panel.md)，移除打印机背板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-adaptive-airflow-assembly-right/zh/37______________adaptive_airflow_assembly_right_replacement_guide_4a4f1eee50.jpg)

### 第 2 步 移除右侧板

请参考 WIKI: [右侧板更换指南](replace-side-panel-right.md)，移除右侧板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-adaptive-airflow-assembly-right/zh/37______________adaptive_airflow_assembly_right_replacement_guide_f5e8c50be5.jpg)

### 第 3 步 移除辅助冷却风扇

从控制板上将风扇插头断开，并从卡扣中将线缆松出。然后向外侧拉伸橡胶软钉，将 4 个软钉从风扇卡扣上松出，取下风扇。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 4 步 断开连接线缆

按压插头锁扣，将通信线缆从 MC 板的连接器（编号：8 & 9）上断开；移除右腔温模块供电线的保护胶套，用 H1.5 内六角扳手按住快速连接端子的锁扣解锁并将向外撬，拔除两根右腔温模块供电线。

|  |  |
| --- | --- |
| 图 | 图 |

将断开的连接线缆从卡扣和过线孔中松出，退回到右自适应风道组件内侧。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 5 步 移除右自适应风道组件

用 H2.0 内六角扳手移除右自适应风道组件的 7 颗固定螺丝，其中将右自适应风道组件固定到金属底座的是细牙螺丝。

|  |  |
| --- | --- |
| 图 | 图 |
| 图 |

向右移动，取下右自适应风道组件  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-adaptive-airflow-assembly-right/zh/37______________adaptive_airflow_assembly_right_replacement_guide_4764dc37c0.jpg)

## 安装右自适应风道组件

### 第 1 步 安装右自适应风道组件

将右自适应风道组件从右侧放置到侧框架内。

|  |  |
| --- | --- |
| 图 | 图 |

将拆除了 7 颗螺丝按原位置锁回，第 1 次锁螺丝时，不要直接锁紧，保留最后 2~3 圈的余量，待所有螺丝到锁到位置上时，再进行锁紧，先锁紧后侧的 3 颗 （编号 5/6/7 ）螺丝。

|  |  |
| --- | --- |
| 图 | 图 |
| 图 |

### 第 2 步 连接线缆

将通信线缆和供电线穿过各自的过线孔，将卡住线扣中。然后将通信线缆连接到 MC 板的连接器（编号：8 & 9）上。

|  |  |
| --- | --- |
| 图 | 图 |

将供电线的快速连接插头连接到 AC 板的端子上，并将保护胶套装回。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 3 步 安装辅助冷却风扇

拉伸橡胶软钉并卡进风扇的缺口中，将辅助冷却风扇安装到风道组件上，然后将转接线插头连接到控制板的连接器上，并将线缆整理进卡扣中。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 4 步 安装右侧板

请参考WIKI： [右侧板更换指南](replace-side-panel-right.md)，安装好右侧板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-adaptive-airflow-assembly-right/zh/05_____________chamber_hall_sensor_pack_replacement_guide_1bb43b6dab.jpg)

### 第 5 步 安装背板

请参考 WIKI：[背板更换指南](replace-back-panel.md)，将背板及其他配件安装好。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-adaptive-airflow-assembly-right/zh/12_z________z_motor_replacement_guide_2980526540.jpg)

## 功能验证

1. 启动打印机并进入空调系统界面，切换到腔温模式；
2. 设置腔温为 60 ℃；
3. 确认加热器和风扇能正常开启。

|  |  |
| --- | --- |
| 图 | 图 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
