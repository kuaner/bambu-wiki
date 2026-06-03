---
path: zh/h2d/maintenance/replace-idlers-ptfe-tube-connector
title: "H2D & H2C 从动杆气动接头更换指南"
description: "本文将详细给您解释 H2D & H2C 从动杆气动接头更换的步骤和注意事项。"
tags: []
created: 2025-12-26T06:07:04.132Z
updated: 2026-03-24T08:28:24.659Z
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

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
