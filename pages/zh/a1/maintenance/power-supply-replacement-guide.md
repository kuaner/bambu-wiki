---
path: zh/a1/maintenance/power-supply-replacement-guide
title: "A1 电源更换指南"
description: "本指南介绍如何更换 A1 打印机电源模块"
tags: []
created: 2025-02-15T08:45:58.622Z
updated: 2025-09-12T04:11:43.079Z
source: https://wiki.bambulab.com/zh/a1/maintenance/power-supply-replacement-guide
---

## 电源模块

本指南中，我们将展示 A1 24V 电源模块的更换过程。

![a1_mini_power_supply.jpg](https://wiki.bambulab.com/a1/maintenance/power-supply/a1_mini_power_supply.jpg)

## 适用打印机型号

A1

## 何时使用

- 打印机无法开机
- 拓竹技术支持建议更换

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- 新的电源模块
- H2.0 内六角扳手
- PH2 十字螺丝刀
- 20 分钟

## 移除旧的电源模块

### **1.将打印机正面朝下放置**

将打印机正面朝下放置，方便操作打印机底部。

首先将屏幕翻转到一侧，然后轻轻将打印机正面朝下放置，如下图所示。建议使用一盒耗材将打印机顶部抬起，避免压迫挤出机和屏幕。  
![place_the_a1_printer_on_its_front.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/place_the_a1_printer_on_its_front.jpeg)

### **2.拆除线缆盒**

拧松黄色标记螺丝不用完全取出，移除 1、2、3 号线缆分别是摄像头、Z 轴电机、X 轴电机之后向上推出线缆支架断开 USB-C 线缆。

![disconnect_the_a1_wires_and_remove_the_wire_bracket_-_22.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/disconnect_the_a1_wires_and_remove_the_wire_bracket_-_22.jpeg)

> **注意**：若不能轻易移除线缆支架，可以完全取出黄色标记螺丝并再次尝试。

### **3：移除打印机底盖**

移除底壳 10 颗红色标记螺丝，轻轻撬开底壳即可。

![remove_the_bottom_housing_cover_screws.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/remove_the_bottom_housing_cover_screws.jpeg)

### **4：移除电源模块螺丝**

A1 电源模块由两颗螺丝和塑料卡扣固定。  
首先，需要移除两颗电源模块固定螺丝，如下图两个位置。

![power_supply_screws.jpeg](https://wiki.bambulab.com/a1/maintenance/power-supply/%E7%94%B5%E6%BA%90%E8%9E%BA%E4%B8%9D.png)

### **5：移除电源模块线缆**

如下图所示松开电源模块端子；  
只需要松开即可移除线缆，不用完全移除螺丝，方便后续的收纳。

![a1_power_supply_screws_.jpeg](https://wiki.bambulab.com/a1/maintenance/power-supply/%E7%94%B5%E6%BA%90%E7%AB%AF%E5%AD%90.png)

### **6：取下电源模块**

将电源端子上的线缆移除之后，接下来需要从打印机上拆除电源模块。  
轻轻将塑料卡扣向下推，同时抬起电源模块即可完全取出。

> 注意：不要用力弯折卡扣，可能会导致卡扣断裂，向下推 2-3mm 即可；可以逐个打开卡扣，取出电源模块。

|  |  |
| --- | --- |
|  |  |

## 安装新的电源模块

### **1：连接电源模块线缆**

按住电源模块，将线缆插入对应的端子内，并锁紧螺丝；如下图所示。

1. +V 主板正极线缆
2. -V 主线负极线缆
3. 地线
4. 交流零线
5. 交流火线

![a1_power_supply_screws_.jpeg](https://wiki.bambulab.com/a1/maintenance/power-supply/%E7%94%B5%E6%BA%90%E7%AB%AF%E5%AD%90.png)

> 注意：如上图所示接好全部线缆之后，要确保线缆接头固定到位且没有松动。

### **2：安装电源模块**

先沿顶部插入电源模块，当顶部的螺丝孔对齐后，轻轻推电源底部对准底部螺丝孔。

|  |  |
| --- | --- |
|  |  |

接下来，安装电源模块固定螺丝。  
如下图所示将螺丝拧入塑料支架；不要过度锁紧，否者可能会导致塑料螺纹滑丝。

![power_supply_screws.jpeg](https://wiki.bambulab.com/a1/maintenance/power-supply/%E7%94%B5%E6%BA%90%E8%9E%BA%E4%B8%9D.png)

### **3：安装打印机底壳**

现在可以对打印机底壳进行安装；需要注意的是下图左上角电机线，插入线缆接头之前避免底壳压住电机线缆；  
底壳安装之后锁入对应的 10 颗螺丝，此处螺丝为自攻螺丝，避免过度锁紧。

![install_the_back_cover_on_a1.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/install_the_back_cover_on_a1.jpeg)

### **4：安装底部线缆盒并连接线缆**

在最后一步中，小心对齐线缆盒，将其向下推入，同时确保 USB-C 电缆插入对应的母座。  
然后，拧紧图中所示的螺丝 1；注意螺丝无需过度锁紧。

![install_the_cable_bracket.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/install_the_cable_bracket.jpeg)

之后依次连接摄像头、X 电机、Z 电机线缆。  
![a1_wires.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/a1_wires.jpeg)

## 功能验证

为了确保打印机可以正常工作，完成所有安装后可以通电并打开电源开关测试；  
可以正常开机点亮显示屏，则表明安装正确。

## 潜在问题及解决方案

安装完成电源模块之后可能会遇到其他功能故障，请参考如下方案进行排查。

### 打印机无法开机

确认点亮模块线缆安装是否正确；可以参考安装[步骤 1](#step1) 所示。

### X/Z 电机报错

确认 X 电机和 Z 电机电线是否有接错或者松动的情况；如[步骤 4](#step4) 所示。安装线缆和并连接其他线缆。

### 屏幕出现TH板或者涡流线圈工作异常

USB-C 线缆可能出现连接异常。松开固定线缆盒的螺丝，参考[步骤4](#step4) 重新插拔 USB-C 线。安装线缆和并连接其他线缆。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
