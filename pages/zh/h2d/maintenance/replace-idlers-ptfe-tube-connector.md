---
path: zh/h2d/maintenance/replace-idlers-ptfe-tube-connector
title: "H2D & H2C 从动杆气动接头更换指南"
description: "本文将详细给您解释 H2D & H2C 从动杆气动接头更换的步骤和注意事项。"
tags: []
created: 2025-12-26T06:07:04.132Z
updated: 2026-08-28T06:35:58.739Z
source: https://wiki.bambulab.com/zh/h2d/maintenance/replace-idlers-ptfe-tube-connector
---

## 从动杆气动接头

从动杆气动接头是安装在从动杆上的气动连接器，用以固定 PTFE 料管，使耗材可以顺畅进入打印机。

![dual_extruder_ptfe_tube_connector_zh.jpg](https://wiki.bambulab.com/h2/maintenance/replace-idlers-ptfe-tube-connector/dual_extruder_ptfe_tube_connector_zh.jpg)

## 适用打印机型号

- **H2C**
- **H2D**
- **H2D Pro**

## 何时更换

- 气动接头损坏
- 从动杆无法固定 PTFE 管

> 左图中的从动杆支持更换气动接头；右图中的从动杆无法更换气动接头，这需要[更换从动轮组件](../../h2/maintenance/replace-dual-extruder-idlers-and-filament-sensor.md)。
>
> |  |  |
> | --- | --- |
> | 可更换1.png | 不可更换1.png |

## 所需要工具和材料

- 撬棒或一字螺丝刀
- H2.0 内六角扳手
- 新的从动杆气动接头

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除旧的从动杆气动接头

### 1. 降低热床

通过屏幕下降热床，确保热端位于室温状态，关机。

|  |  |
| --- | --- |
|  |  |

### 2. 移除工具头前盖或工具头散热增强风扇

若打印机未安装工具头散热增强风扇，则捏住工具头前盖顶部的两角处，向上提起以移除工具头前盖。

|  |  |
| --- | --- |
|  |  |

若打印机安装了工具头散热增强风扇，往上拔移除风扇连接插头。然后，捏住工具头散热增强风扇的顶部并向上提起，将其移除即可。

|  |  |
| --- | --- |
|  |  |

### 3. 移除工具头上方 PTFE 管

按住气动接头黑色外圈，以解锁挤出机上方的两个气动接头，然后拔出左右两根 PTFE 料管。

|  |  |
| --- | --- |
|  |  |

### 4. 移除挤出机前盖

根据机型，参考以下 Wiki 以移除移除左右热端、挤出机前盖导向组件及挤出机前盖。

H2D 机型请参考：[更换 H2D 挤出机前盖](../../h2/maintenance/replace-quick-change-tool-interface.md)  
H2C 机型请参考：[更换 H2C 挤出机前盖](../../h2c/maintenance/replace-quick-change-tool-interface.md)

### 5. 移除气动接头

使用撬棒或一字螺丝刀，轻轻撬起气动接头底座上盖，取出两侧从动轮气动接头即可。

|  |  |
| --- | --- |
|  |  |

## 安装新的从动杆气动接头

### 1. 安装左侧气动接头及其底座

安装左侧气动接头及其底座时请注意方向，气动接头平坦一侧需朝向缺口处，底座卡扣长边与缺口平齐。

**气动接头零件脱落后的修复工作**

新气动接头内部零件脱落后，可重新安装以下零件完成修复。

![1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-idlers-ptfe-tube-connector/1.jpg)

先将水平垫片放入气动接头。

> 水平垫片遗失不影响气动接头功能。

![1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-idlers-ptfe-tube-connector/2.jpg)

再放入黄色齿片，注意齿形朝上。  
![1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-idlers-ptfe-tube-connector/3.jpg)  
![1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-idlers-ptfe-tube-connector/4.jpg)

最后压入黑色挡块，反复按压确保固定牢靠即可。  
![1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-idlers-ptfe-tube-connector/5.jpg)  
![1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-idlers-ptfe-tube-connector/6.jpg)

|  |  |
| --- | --- |
|  |  |

### 2. 安装右侧气动接头及其底座

安装右侧气动接头及其底座时，同样需要注意安装方向，与左侧一致。

|  |  |
| --- | --- |
|  |  |

### 3. 安装挤出机前盖

根据机型，参考以下 Wiki 以重新安装移除左右热端、挤出机前盖导向组件及挤出机前盖。

H2D 机型请参考：[更换 H2D 挤出机前盖](../../h2/maintenance/replace-quick-change-tool-interface.md)  
H2C 机型请参考：[更换 H2C 挤出机前盖](../../h2c/maintenance/replace-quick-change-tool-interface.md)

### 4. 安装工具头上方 PTFE 管

|  |  |
| --- | --- |
|  |  |

### 5. 安装工具头前盖或工具头散热增强风扇

若打印机未安装工具头散热增强风扇，装回工具头前面盖的时候，可以先扣入挤出机下方的位置，再往后推，将前面盖安装到位即可。

![](https://wiki.bambulab.com/h2/maintenance/disassemble-and-install-h2d-toolhead/image-279.png)

若打印机安装了工具头散热增强风扇，将风扇的 2 个空缺孔对准挤出机上方左右 2 个定位扣，卡入风扇；然后扶住风扇的下半部分，往后推，完成安装。风扇安装到位时，会听到 “咔嗒” 一声。

|  |  |
| --- | --- |
|  |  |

> - 插入风扇插头时请注意，风扇插头具有方向性，插入前需根据针孔对齐插头和插口的方向。
>
> ![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/maintenance/replace-toolhead-enhanced-cooling-fan/image-7_018.png)

## 功能验证

检查从动杆气动接头无晃动，可以正常固定 PTFE 管即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
