---
path: zh/x2d/maintenance/replace-power-supply
title: "更换 X2D 电源"
description: "本文介绍了如何更换 X2D 的电源"
tags: []
created: 2026-04-14T13:09:41.508Z
updated: 2026-04-14T13:09:42.515Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-power-supply
---

## 电源

X2D 打印机的电源是一个输入电压为 AC 100-240V 的交流电转换为输出电压为 DC 24V 的直流电源的装置，它能为除热床以外的整台打印机提供稳定、干净且符合要求的直流电源。  
![fac220.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/fac220.png)

## 适用打印机型号

X2D

## 何时更换

- 电源出现明显的物理损坏，如连接器损坏、元器件脱落或烧坏；
- 经 Bambu Lab 技术支持确认需更换电源。

## 所需要的工具和材料

- H1.5 内六角螺丝刀
- H2.0 内六角螺丝刀
- 新的电源

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除旧的电源

### 步骤 1. 移除料管支架、缓冲器和背板

参考[更换 X2D 背板](replace-rear-panel.md)的相关指引，移除料管支架、缓冲器及背板。  
![002_remove_rear_panel.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/002_remove_rear_panel.png)

### 步骤 2. 移除废料滑梯

使用 H1.5 内六角扳手移除四颗固定螺丝（BT2x5），然后将废料滑梯取下。  
![003_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/003_remove_purge_chute.jpg)

### 步骤 3. 移除电源保护盖

使用 H1.5 内六角扳手移除两颗热床线压片固定螺丝（BT2x5）和五颗电源保护盖螺丝，取下压片，松出电源保护盖。  
![004_remove_power_supply_cover_clip.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/004_remove_power_supply_cover_clip.jpg)

![005_remove_supply_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/005_remove_supply_cover.png)

### 步骤 4. 移除电源

使用十字螺丝刀拧松电源线接口螺丝，将五根线缆依次从电源中取出。  
![006_power_supply_cable.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/006_power_supply_cable.jpg)  
使用 H2.0 内六角扳手移除两颗电源固定螺丝，然后即可将电源抽出。  
![007_power_supply_screws.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/007_power_supply_screws.jpg)

## 安装新的电源

### 步骤 1. 安装电源

将电源模块装入内衬中，使用 H2.0 内六角扳手拧紧两颗固定螺丝（BT2x5）。  
**注意：** 底部的固定螺丝需要将地线一起固定。  
![007_power_supply_screws.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/007_power_supply_screws.jpg)

将五根线缆参考下图依次插入电源接口，从上往下颜色依次为：棕、蓝、黄、黑、白。然后使用十字螺丝刀拧紧螺丝。在使用螺丝刀拧紧螺丝的时候可以用手扶住线缆，避免线缆松脱。  
![006_power_supply_cable.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/006_power_supply_cable.jpg)

### 步骤 2. 安装电源保护盖

将电源线往电源一侧推动，将线缆靠近在电源一侧，然后将电源保护盖装入，将电源线缆从电源保护盖底部的凹槽中穿出，使用 H1.5 内六角扳手依次拧紧五颗螺丝（BT2x5）。  
![008_power_supply_screws.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/008_power_supply_screws.jpg)

将热床线缆装入电源保护盖上的线槽，使用 H1.5 内六角扳手拧紧两颗压片固定螺丝（BT2x5）。  
![004_remove_power_supply_cover_clip.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/004_remove_power_supply_cover_clip.jpg)

### 步骤 3：安装废料滑梯

将废料滑梯对准打印机上的螺丝孔位，使用 H1.5 内六角扳手拧紧四颗固定螺丝（BT2x5）。  
![003_remove_purge_chute.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/003_remove_purge_chute.jpg)

### 步骤 4. 安装背板 （含料管支架&缓冲器）

您可以参考 [更换 X2D 背板](replace-rear-panel.md) 来安装背板。  
![002_remove_rear_panel.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/002_remove_rear_panel.png)

## 功能验证

连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查线缆是否连接正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
