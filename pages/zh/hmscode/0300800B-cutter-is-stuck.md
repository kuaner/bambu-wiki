---
path: zh/hmscode/0300800B-cutter-is-stuck
title: "0300800B：切刀卡住，请确保切刀刀柄已弹出。"
description: "0300800B"
tags: ["a1"]
created: 2025-11-18T06:31:50.302Z
updated: 2025-11-18T07:29:53.002Z
source: https://wiki.bambulab.com/zh/hmscode/0300800B-cutter-is-stuck
---

## 故障描述

当打印机在使用 AMS 打印过程中退料或换料时，切刀用于在拉回之前切割耗材。切割时，工具头会移动到打印机的前面，让顶部的杠杆块压住切刀柄，从而推动刀片切割挤出机中的耗材。耗材被切断后，刀柄会自动弹回至起始状态。

### 可能的原因：

- 耗材切刀刀片磨损，导致挤出机摩擦力增大，需要更换刀片。
- 切刀刀柄上的磁铁掉了，无法触发传感器。
- 挤出机中的霍尔传感器出现故障或扁平电缆损坏。

## 所需要工具

- H2.0 内六角扳手
- H1.5 内六角扳手

## 排故措施

### 步骤1. 检查切刀刀片

当切刀刀片磨损时，无法切断耗材，切刀刀柄就会卡在按下的位置。请检查刀片是否磨损，若磨损,请参考 [更换切刀-A1系列](../a1-mini/maintenance/filament-cutter-replacement.md) 更换刀片。  
![](https://wiki.bambulab.com/a1m/replace-filament-cutter/worn_filament_cutter_blade.png)  
当挤出机组件内部有灰尘或耗材碎屑时，也会出现同样的问题。在这种情况下，您可以按照相同的步骤拆卸耗材切割刀片，从侧面清洁挤出机。请参考[A1 系列挤出机清理](../a1-mini/troubleshooting/extruder-clog.md)。  
![](https://wiki.bambulab.com/n1/troubleshooting/extruder-clog/%E6%AD%A5%E9%AA%A42-%E6%8B%A7%E6%9D%BE%E5%88%87%E5%88%80-3.png)

### 步骤2. 检查切刀刀柄的磁铁

在少数情况下，切刀刀柄顶端的磁铁脱落，从而无法触发霍尔传感器，引发提示。若磁铁脱落，请用胶水将磁铁粘回刀柄上。  
![](https://wiki.bambulab.com/a1m/replace-filament-cutter/filament_cutter_magnet.jpeg)  
若磁铁丢失，请准备新的切刀刀柄，参考[挤出模块组件拆装指引 - A1 系列](../a1-mini/maintenance/a1-extruder.md)安装即可。

### 步骤3. 检查霍尔传感器电缆

耗材切刀错误信息的常见原因与霍尔传感器有关。如果霍尔传感器工作异常，切割时传感器将无法检测到磁铁，从而显示错误。  
霍尔传感器故障常见原因是与其连接的黑色扁平电缆损坏。如果您对五通组件进行过维护或其他操作，则扁平电缆可能已损坏或与挤出主板断开连接。  
![](https://wiki.bambulab.com/a1m/replace-filament-cutter/filament_sensor_cable.png)  
请参考[A1 系列进料霍尔板更换指南](../a1/maintenance/filament-sensor-replacement.md)对线缆进行检查以及重新拔插。若线缆破损，请更换线缆。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
