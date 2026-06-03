---
path: zh/x2d/maintenance/replace-flow-blocker-assembly
title: "更换 X2D 堵嘴组件"
description: "本文介绍了如何更换 X2D 堵嘴组件。"
tags: ["x2d"]
created: 2026-04-14T13:07:51.685Z
updated: 2026-04-14T13:08:59.413Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-flow-blocker-assembly
---

## 堵嘴组件

堵嘴组件安装在工具头底部，用于切换堵嘴片的位置，同时控制右辅助热端的升降。  
堵嘴组件配件包装内包含：

1. 堵嘴组件
2. 螺丝 \* 3
3. 堵嘴片  
   ![fac208.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/fac208.png)

## 何时更换

- 堵嘴片无法正常切换位置或右辅助热端无法正常升降。

## 所需工具和材料

- 新的堵嘴组件
- H1.5 内六角扳手
- H2.0 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除堵嘴组件

### 步骤 1：移除工具头外壳

请参考[更换 X2D 工具头外壳](replace-toolhead-housing.md)，移除工具头的前后盖。  
![disconnect_rear_and_front_cover.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/disconnect_rear_and_front_cover.jpg)

### 步骤 2：移除堵嘴片

1. 向左拨动升降拨杆，将堵嘴片移动到左热端位置。  
   ![shift_flow_blocker_001.webp](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/shift_flow_blocker_001.webp)
2. 用 H1.5 内六角扳手从工具头后方移除 1 颗固定螺丝，取下堵嘴片。  
   ![remove_flow_blocker_002.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/remove_flow_blocker_002.png)

### 步骤 3：移除堵嘴组件

1. 将右热端风扇线缆和堵嘴组件排线从TH板上断开。  
   ![disconnect_fpc_to_switch.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/disconnect_fpc_to_switch.jpg)
2. 从工具头后方找到固定堵嘴组件的 3 颗螺丝，使用 H2.0 内六角扳手完全拧松，取下堵嘴组件（螺丝采用防脱落设计，完全拧松后即可，无需取出）。  
   ![lock_3_screws.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/lock_3_screws.jpg)

> **因固定堵嘴组件的 3 颗螺丝位于视野盲区，建议您通过以下方式定位螺丝位置。**

1. 将手机正面朝上放置于热床上，打开前置摄像头，借助摄像头画面辅助定位螺丝；
2. 用手触摸堵嘴组件后方位置，通过触感的变化寻找螺丝沉孔；
3. 移除背板，从后丝杆位置可观察到螺丝。

## 安装堵嘴组件

> **安装位置提醒：标识凹槽要位于两个带有凸点的齿牙之间！**  
> ![gear_position.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/gear_position.jpg)

### 步骤 1：安装堵嘴组件

确认右辅助热端位于工具头最下方，将堵嘴组件拨杆拨到最左侧。  
![install_position.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/install_position.jpg)  
将堵嘴组件安装到工具头下方，注意确保堵嘴组件上的齿轮和工具头上的齿条保持正确的啮合关系，依次锁紧 3 颗螺丝。  
![lock_3_screws.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/lock_3_screws.jpg)  
连接堵嘴组件排线和右热端风扇线缆。  
![connect_fpc_cable.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/connect_fpc_cable.jpg)

> **因固定堵嘴组件的 3 颗螺丝位于视野盲区，建议您通过以下方式定位螺丝位置。**

1. 将手机正面朝上放置于热床上，打开前置摄像头，借助摄像头画面辅助定位螺丝；
2. 用手触摸堵嘴组件后方位置，通过触感的变化寻找螺丝沉孔；
3. 移除背板，从后丝杆位置可观察到螺丝。

### 步骤 2：安装堵嘴片

将堵嘴片上的圆孔与堵嘴组件支架上的安装柱对齐，用 H1.5 内六角扳手锁紧 1 颗螺丝。  
![install_flow_blocker_screw_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/install_flow_blocker_screw_001.png)

### 步骤 3：安装工具头外壳

请参考[更换 X2D 工具头外壳](replace-toolhead-housing.md)，安装工具头的外壳。  
![install_toolhead_cover_001.png](https://public-cdn.bblmw.com/wiki/new/x2d/replace-flow-blocker-assembly/install_toolhead_cover_001.png)

## 如何验证成功

左右拨动堵嘴组件拨杆，堵嘴片能正常切换，右辅助热端能正常升降到位。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
