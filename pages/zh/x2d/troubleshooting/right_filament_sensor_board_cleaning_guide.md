---
path: zh/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide
title: "X2D 右霍尔检测板组件清理指南"
description: "本文将介绍如何清理右霍尔检测板组件中的断料。"
tags: ["x2d"]
created: 2026-05-27T06:59:32.912Z
updated: 2026-06-11T01:30:14.231Z
source: https://wiki.bambulab.com/zh/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide
---

## 何时使用

当右霍尔检测板组件中存在断料或碎屑时，可能影响右热端的进料过程，这通常需要清理断料或碎屑，才能恢复设备正常工作。

![pixpin_2026-05-29_15-46-22.jpg](https://wiki.bambulab.com/x2d/pixpin_2026-05-29_15-46-22.jpg)

## 工具

- 内六角螺丝刀
- 开口扳手
- 一截耗材

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 操作步骤

### 方法一

打开工具头前盖，按压连接器锁扣并拔掉插头，取下工具头前盖组件。

![](https://public-cdn.bblmw.com/wiki/new/x2d/filament-sensor-test/016.jpg)

取下右喷嘴。

> 若此时右喷嘴被抬升，可参考下一步骤的操作下降喷嘴。

![](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/unlock_right_click.jpg)

向右拨动工具头底部的热端切换柄，抬升右热端。

![切换.webp](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%88%87%E6%8D%A2.webp)

使用扳手逆时针拧松气动接头，取下右侧进料管。

![](https://public-cdn.bblmw.com/wiki/new/x2d/filament-sensor-test/012.png)

插入一小截耗材,尝试顶出断料或者碎屑。

![疏通.webp](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E7%96%8F%E9%80%9A.webp)

若无法顶出断料或碎屑，请尝试方法二。

### 方法二

#### 第 1 步. 移除工具头外壳

请参考[更换 X2D 的工具头外壳](../maintenance/replace-toolhead-housing.md)来移除工具头前盖和中框。

#### 第 2 步：取出右霍尔检测板组件

再参考[更换 X2D 挤出机配件](../maintenance/replace-extruder-components.md)，分离挤出机前盖组件和右霍尔检测板组件。

单独拧下霍尔检测板的固定螺丝，取下送料通道。

![取下霍尔组件.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%8F%96%E4%B8%8B%E9%9C%8D%E5%B0%94%E7%BB%84%E4%BB%B6.jpg)  
![取下霍尔组件2.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%8F%96%E4%B8%8B%E9%9C%8D%E5%B0%94%E7%BB%84%E4%BB%B62.jpg)

#### 第 3 步：清理送料通道

拧下切刀组件的固定螺丝后，小心拉出切刀组件。

![切刀螺丝.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%88%87%E5%88%80%E8%9E%BA%E4%B8%9D.jpg)  
![切刀.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%88%87%E5%88%80.jpg)

再拧下送料通道的 2 个固定螺丝。

![送料管螺丝.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E9%80%81%E6%96%99%E7%AE%A1%E8%9E%BA%E4%B8%9D.jpg)

使用H 1.5 内六角扳手小心撬开送料通道。

> 请在整洁的桌面上撬开该组件。内部零件较小，请勿遗失。

![1.webp](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/1.webp)

清理断料或者碎屑。

![清单.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E6%B8%85%E5%8D%95.jpg)

完成后将所有零件装上塑料件。

![摆放1.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E6%91%86%E6%94%BE1.jpg)  
![摆放.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E6%91%86%E6%94%BE.jpg)

合上另一半塑料件，拧紧固定螺丝。

![合上.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%90%88%E4%B8%8A.jpg)  
![送料管螺丝.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E9%80%81%E6%96%99%E7%AE%A1%E8%9E%BA%E4%B8%9D.jpg)

使用表面较粗糙的物品，调整弹簧位置。

![弹簧.webp](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%BC%B9%E7%B0%A7.webp)

装回切刀和固定螺丝。

![安装切刀.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%AE%89%E8%A3%85%E5%88%87%E5%88%80.jpg)  
![切刀螺丝.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%88%87%E5%88%80%E8%9E%BA%E4%B8%9D.jpg)

#### 第 4 步：复原安装

装回电路板并拧紧固定螺丝。

![取下霍尔组件.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/%E5%8F%96%E4%B8%8B%E9%9C%8D%E5%B0%94%E7%BB%84%E4%BB%B6.jpg)

再参考[更换 X2D 挤出机配件](../maintenance/replace-extruder-components.md)，[更换 X2D 的工具头外壳](../maintenance/replace-toolhead-housing.md)装回挤出机配件以及工具头外壳。

## 功能验证

在屏幕上选择右挤出机进料，当设备提示进料成功，则清理完毕。

![pixpin_2026-05-29_14-53-09.jpg](https://wiki.bambulab.com/x2d/troubleshooting/right_filament_sensor_board_cleaning_guide/pixpin_2026-05-29_14-53-09.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
