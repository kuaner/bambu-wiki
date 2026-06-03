---
path: zh/p2s/maintenance/replace-adaptive-airflow-switching-unit
title: "更换 P2S/X2D  自适应风道切换组件"
description: ""
tags: ["自适应风道切换组件"]
created: 2025-10-14T12:50:16.520Z
updated: 2026-04-30T03:55:47.612Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-adaptive-airflow-switching-unit
---

## 自适应风道切换组件

安装在打印机腔室右侧，能完成空气循环方式的切换和部件冷却功能的组件。  
![fac160.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac160.jpg)

## 何时更换

- 组件切换机构故障
- 冷却风扇故障
- 其他组件功能故障

## 工具和材料

- H2.0 内六角扳手
- 新的自适应风道切换组件

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 安装提示

> 在拆装自适应风道组件时，热床所处位置会影响操作，需要通过拉动 Z 皮带的方式上升或下降热床高度。
>
> - 热床在半高位置，更方便拆装底部和顶部的螺丝.
> - 热床在底部位置，更方便装入或者取出风道组件。  
>   ![up_and_dowm_the_heatbed_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/up_and_dowm_the_heatbed_001.png)

## 拆除自适应风道切换组件

### 第1步：移除料管支架

参考[更换料管支架](replace-ptfe-tube-bracket.md) 的指引，移除料管支架。  
![ptfe_tube_bracket_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/ptfe_tube_bracket_002.png)

### 第2步：移除缓冲器

您可以根据机型，参考对应 Wiki 来移除缓冲器：

- [P2S](replace-filament-buffer.md)
- [X2D](../../x2d/maintenance/replace-filament-buffer.md)

| filament_buffer_001.png | filament_buffer.jpg |
| --- | --- |
| P2S | X2D |

### 第3步：移除背板

您可以根据机型，参考对应 Wiki 来移除打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

### 第4步：移除自适应风道切换组件

按住线缆接头的卡扣，将线缆从 MC 板上断开连接，然后将线缆依次从横梁上的三个线扣中取出。  
![cable_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/cable_007.png)  
通过Z皮带，将热床调整至约半高的设置，使用 H2.0 内六角扳手移除 3 颗螺丝。  
![3_screws_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/3_screws_002.png)  
拉动Z皮带将热床降低至底部。  
![down_to_the_bottom_5.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/down_to_the_bottom_5.png)  
在出风口处向上提，使自适应风道切换组件松动，然后向左侧掰动自适应风道切换组件，并沿斜向上的方向提起，然后将组件取出。  
![remove_the_fan_assembly.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/remove_the_fan_assembly.png)

## 安装自适应风道切换组件

### 第1步：安装自适应风道切换组件

1. 将线缆穿过内衬与侧板间的小孔，然后将自适应风道切换组件的下部装到底座上，顶部向横梁位置装好，再向打印机背部推动，使组件与内衬能完全贴合。  
   ![install_the_unit_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/install_the_unit_009.png)
2. 倾斜打印机，拉动Z皮带将热床上升至打印机中部。  
   ![up_and_dowm_the_heatbed_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/up_and_dowm_the_heatbed_001.png)
3. 使用 H2.0 内六角扳手拧紧三颗螺丝。  
   ![3_screws_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/3_screws_002.png)
4. 将线缆从左往右依次扣入横梁上的三个线扣中，并将线缆重新连接到 MC 板的连接器上。  
   ![connect_cable_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/connect_cable_006.png)

### 第2步：安装背板

您可以根据机型，参考对应 Wiki 来安装打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

### 第3步：安装缓冲器

您可以根据机型，参考对应 Wiki 来安装缓冲器：

- [P2S](replace-filament-buffer.md)
- [X2D](../../x2d/maintenance/replace-filament-buffer.md)

| filament_buffer_001.png | filament_buffer.jpg |
| --- | --- |
| P2S | X2D |

### 第4步：安装料管支架

参考[更换料管支架](replace-ptfe-tube-bracket.md)的指引安装好料管支架  
![ptfe_tube_bracket_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/ptfe_tube_bracket_002.png)

## 如何验证成功

- 启动打印机
- 在屏幕上进行操作
- 能正常切换循环模式

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
