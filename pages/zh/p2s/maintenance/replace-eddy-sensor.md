---
path: zh/p2s/maintenance/replace-eddy-sensor
title: "更换 P2S 涡流线圈"
description: ""
tags: []
created: 2025-10-14T13:14:20.770Z
updated: 2026-03-26T07:07:34.722Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-eddy-sensor
---

## 涡流线圈

涡流线圈安装在挤出机与热端的中间，用于对耗材的流量进行主动校准的配件。  
![fac155.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac155.jpg)

## 何时更换

1. 涡流线圈损坏

## 需要的工具和材料

1. 新的涡流线圈
2. H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除涡流线圈

### 步骤 1：移除工具头外壳

请参考 [更换工具头外壳](replace-toolhead-housing.md)这篇WIKI，将工具头的外壳拆除。  
![toolhead_housing_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/toolhead_housing_001.png)

### 步骤 2：移除热端

请参考[更换热端和热端硅胶套](replace-hotend-and-silicone-sock.md)，移除热端硅胶套与热端：  
![remove-sock.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/remove-sock.png)  
![remove-hotend.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/remove-hotend.png)

### 步骤 3：移除热端风扇风道

使用 H1.5 内六角扳手移除两颗热端风扇风道螺丝，将风道从工具头上取下。

![08_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/08_008.png)

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/01_001.png)

### 步骤 4：松开线缆

依次将贴在 TH 板上的泡棉和胶带撕下，然后依次从 TH 板上断开热端风扇连接线和热端加热组件连接。断开涡流线圈的连接线时，要垂直于连接器的方向拨起，请勿在连接器左右方向用力或摇晃，以免损坏连接器；

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/02_002.png)

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/03_003.png)

将热端风扇连接线和热端加热组件连接线依次从线扣中取出。

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/04_004.png)

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/05_005.png)

### 步骤 5：移除涡流线圈

使用 H1.5 内六角扳手移除两颗涡流线圈固定螺丝，将涡流线圈取下

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/07_007.png)

## 安装涡流线圈

### 步骤 1：安装涡流线圈

螺丝孔朝下，将涡流线圈安装至热端加热组件上方，使用 H1.5 内六角扳手拧紧两颗固定螺丝。

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/07_007.png)

### 步骤 2：连接线缆

先将涡流线圈的线缆卡入下图所示的线扣中；

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/05_005.png)

将热端加热组件连接线绕过螺丝柱。热端加热组件连接线请勿挡在螺丝孔处，避免后续安装风道时螺丝刮到线缆；

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/06_006.png)

将热端加热组件线缆和涡流线圈线缆依次卡入两个线扣中；

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/04_004.png)

将热端加热组件线缆重新与 TH 板连接，将涡流线圈接头与 TH 板上的接口对齐后再完全压入，贴回胶布和泡棉。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/03_003.png)

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/02_002.png)

### 步骤 3：安装热端风扇风道

将热端风扇风道安装至热端风扇左侧，检查确认线缆没有被压在螺丝孔上，使用 H1.5 内六角扳手拧紧两颗固定螺丝。

![08_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/08_008.png)

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-eddy-sensor/01_001.png)

### 步骤 4：安装热端硅胶套和热端

请参考 [更换热端和热端硅胶套](replace-hotend-and-silicone-sock.md) 这篇WIKI，安装热端硅胶套与热端：

|  |  |
| --- | --- |
|  |  |

### 步骤 5：安装工具头外壳

参考 [更换工具头外壳](replace-toolhead-housing.md) 的内容，安装好工具头外壳。  
![close_front_cover_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/close_front_cover_002.png)

## 如何验证成功

更换涡流线圈后，请参考 [P2S 涡流线圈调整](adjust-the-eddy-sensor.md) 进行调整。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
