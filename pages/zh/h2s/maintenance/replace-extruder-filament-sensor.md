---
path: zh/h2s/maintenance/replace-extruder-filament-sensor
title: "更换 H2S 霍尔开关板组件"
description: ""
tags: []
created: 2025-08-26T06:10:16.896Z
updated: 2026-05-06T01:31:48.912Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-extruder-filament-sensor
---

![h2s_extruder_filament_sensor.png](https://wiki.bambulab.com/h2s/maintenance/replace-extruder-filament-sensor/h2s_extruder_filament_sensor.png)

## 何时需要该指南

进料霍尔组件故障。

## 需要的工具和材料

- 新的进料霍尔组件
- 内六角扳手H2.0 和H1.5
- 20 分钟

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

备注：下文中的图片未包括热端和旋转轮。实际上，仅拆装进料霍尔组件时，无需取下旋转轮和热端。请根据需要进行拆装。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/image-6.png)

## 拆解指引

### 步骤1：断开PTFE管

按压气动接头，断开PTFE管。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/remove_tube.webp)

### 步骤2: 移除进料霍尔组件

用H2.0内六角扳手移除2颗螺丝。需要注意的是，取出进料霍尔组件时不要大力拉扯，摆放时也应小心操作，避免损坏黑色FPC排线。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/image-4.png)

![fpc-carefull.png](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/fpc-carefull.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/remove_hall_sensor.webp)

### 步骤3：断开进料霍尔板插头

使用H1.5螺丝刀拧下进料霍尔板排线固定螺丝，抠开卡扣，断开插头。

![disconnect-hall-connector.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/disconnect-hall-connector.webp)

## 组装指引

### 步骤1：连接进料霍尔板插头

您收到的进料霍尔板组件是连接了排线的，但通常排线不会故障，因此您需要重复上一步的步骤，拧下螺丝，并断开新备件上的插头。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/image.png)

插入旧的进料霍尔排线，并锁紧一颗螺丝。请注意，FPC排线的板子需要嵌入卡扣中，FPC插头的白线要与PCB插座附近的白线平齐。这个步骤需要耐心，因为通常不容易一次就插入到位。

![filament_sensor-fpc.png](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/filament_sensor-fpc.png)

![connect-new-connector.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/connect-new-connector.webp)  
![screw_1_screw.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/screw_1_screw.webp)

备注：若您确实遇到了需要更换排线的情况，您需要参考[挤出机组件的拆装](replace-extruder-unit.md)，先将整个挤出机组件拆下，再更换进料霍尔排线。

### 步骤2: 安装进料霍尔组件

安装五通组件，请确保黑色 FPC 线缆不要被折叠，顺利放入空缺的位置。然后拧入 2 颗螺丝，固定进料霍尔组件。

> 装回时，注意不要压到霍尔线缆; 用手指或塑料工具移动霍尔线避开螺丝孔; 锁入螺丝前，请从顶部检查螺丝孔，确保线缆没有挡住螺丝孔

![h2s-filament-sensor.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/h2s-filament-sensor.webp)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/install_hall_sensor.webp)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/image-1.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/image-2.png)

### 步骤3：连接PTFE管

插入PTFE管。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-extruder-filament-sensor/image-3.png)

## 如何验证完成/成功

重新打开打印机并在屏幕上控制进料和退料来验证一切是否正常。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
