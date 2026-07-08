---
path: zh/a1/maintenance/ac-board-replacement
title: "A1 AC 板更换指南"
description: "本指南详细介绍了如何卸下和安装A1的AC板。"
tags: []
created: 2024-05-31T02:03:16.213Z
updated: 2026-07-06T08:39:31.733Z
source: https://wiki.bambulab.com/zh/a1/maintenance/ac-board-replacement
---

## AC 板

本指南中，我们将展示 A1 打印机的 AC 板更换过程。

- A1 打印机的 AC 板现有两个版本。两个版本功能相同，只有很细微的区别，故 Wiki 上的相关指南均适用。  
  ![a1-mini-ac-boardoldvsnew.png](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/a1-mini-ac-boardoldvsnew.png)

## 适用打印机型号

A1

## 何时使用

- AC 板出现故障
- 热床加热异常
- 拓竹技术支持建议更换

## 所需工具和材料

- 新的 AC 板
- H 2.0 内六角扳手
- 20 - 30 分钟

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除旧的 AC 板

### **步骤 1：将打印机正面朝下放置**

将打印机正面朝下放置，方便操作打印机底部。

首先将屏幕翻转到一侧，然后轻轻将打印机正面朝下放置，如下图所示。建议使用一盒耗材将打印机顶部抬起，避免压迫挤出机和屏幕。  
![place_the_a1_printer_on_its_front.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/place_the_a1_printer_on_its_front.jpeg)

### **步骤 2：拆除线缆盒**

拧松黄色标记螺丝不用完全取出，移除 1、2、3 号线缆分别是摄像头、Z 轴电机、X 轴电机之后向上推出线缆支架断开 USB-C 线缆。

![disconnect_the_a1_wires_and_remove_the_wire_bracket_-_22.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/disconnect_the_a1_wires_and_remove_the_wire_bracket_-_22.jpeg)

> **注意**：若不能轻易移除线缆支架，可以完全取出黄色标记螺丝并再次尝试。

### **步骤 3：移除打印机底盖**

移除底壳 10 颗红色标记螺丝，轻轻撬开底壳即可。

![remove_the_bottom_housing_cover_screws.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/remove_the_bottom_housing_cover_screws.jpeg)

### **步骤 4：移除热床电源线缆**

移除 1、2 号位热床电源线缆（插接该线缆不分左右），移除硅胶套，并用螺丝刀或者镊子抵住解锁扣移除线缆。

|  |  |
| --- | --- |
|  |  |

> 注意：新版本 AC 板移除地线设计，优化电源开关结构及通流能力；此变更不影响AC板的核心功能及性能。  
> ![new_ac_board_removed_ground_wire_design.png](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-01-52.jpg)

### **步骤 5：移除热床信号线缆**

移除热床 4PIN 信号线缆，可以使用工具或者捏住塑料接头进行拔出；注意不要直接拖住线缆，可能会导致接头损伤。

![pixpin_2026-07-06_16-16-34.jpg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-16-34.jpg)

### **步骤 6：移除 AC 板排线**

断开 AC 板信号排线，抬起黑色固定扣即可顺利拉出线缆。

![pixpin_2026-07-06_16-16-34.jpg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-16-17.jpg)

### **步骤 7：移除 AC 板剩余线缆**

继续移除剩余线缆，首先移除 #1 #2 #3 分别是地线、火线、零线。将蓝色胶套往外拨出后，使用螺丝刀顶住卡扣的同时向外拉出线缆。 #4、#5 电源模块线缆稍后拆除。

![pixpin_2026-07-06_16-16-34.jpg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-03-28.jpg)

![](https://wiki.bambulab.com/knowledge-sharing/printer-electronic-connectors-guide/con5.png)

### **步骤 8：取出旧的 AC 板**

取出 AC 板中间固定螺丝，松开塑料卡扣即可取出 AC 板。

![pixpin_2026-07-06_16-30-09.jpg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-30-09.jpg)

此时继续拆卸 4，5 号电源模块线缆，如果该线缆很难解锁，也可使用螺丝刀直接撬出。

![acboard.webp](https://wiki.bambulab.com/knowledge-sharing/printer-electronic-connectors-guide/acboard.webp)

## 安装新的 AC 板

### **步骤 1：安装塑料绝缘板**

将旧的 AC 板绝缘塑料板取出，安装到新的 AC 板。

![ac_board_plastic_insulation.jpg.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/ac_board_plastic_insulation.jpg.jpeg)

### **步骤 2：安装 AC 板固定螺丝**

将新的 AC 板对准打印机框架上的螺丝孔，然后安装固定螺丝。

![pixpin_2026-07-06_16-30-09.jpg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-30-09.jpg)

### **步骤 3：插入 AC 板排线和热床信号信线**

首先打开黑色卡扣，插入白色排线，需要确保蓝色标签和黑色卡扣平行，压紧黑色卡扣；  
然后将热床 4PIN 信号线缆插入对应的 4PIN 接口座内。

![pixpin_2026-07-06_16-02-32.jpg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-02-32.jpg)

### **步骤 4：连接热床电源线**

小心插入热床电源线，如下图 1、2 号所示（不需要区分颜色和左右）。

![pixpin_2026-07-06_16-16-48.jpg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-16-48.jpg)

### **步骤 5：连接 AC 板剩余线缆**

如下图所示（图示以新版本 AC 板为例），完成 AC 板剩余线缆的连接。

1. 地线（黄色）（适用于旧版本 AC 板）
2. 火线（棕色）
3. 零线（蓝色）
4. 火线（红色）
5. 零线（黑色）

![pixpin_2026-07-06_16-17-09.jpg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/pixpin_2026-07-06_16-17-09.jpg)

> 注意：完成以上安装之后，确保所有线缆安装上绝缘硅胶套。

### **步骤 6：安装打印机底壳**

现在可以对打印机底壳进行安装；需要注意的是下图左上角电机线，插入线缆接头之前避免底壳压住电机线缆；  
底壳安装之后锁入对应的 10 颗螺丝，此处螺丝为自攻螺丝，避免过度锁紧。

![install_the_back_cover_on_a1.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/install_the_back_cover_on_a1.jpeg)

### **步骤 7：安装底部线缆盒并连接线缆**

在最后一步中，小心对齐线缆盒，将其向下推入，同时确保 USB-C 电缆插入对应的母座。  
然后，拧紧图中所示的螺丝 1；注意螺丝无需过度锁紧。

![install_the_cable_bracket.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/install_the_cable_bracket.jpeg)

之后依次连接摄像头、X 电机、Z 电机线缆。  
![a1_wires.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/a1_wires.jpeg)

## 功能验证

为了确保打印机之后的正常运行，可以将打印机热床温度设置为 50°C 进行验证，如果热床正常升温，则打印机 AC 板和热床工作正常。

## 潜在问题及解决方案

安装完成 AC 板之后可能会遇到其他功能故障，请参考如下方案进行排查。

### 打印机摄像头工作异常

确认摄像头线缆完全插入对应的母座；如[步骤7](#step7) 所示。安装线缆和并连接其他线缆。

### X/Z 电机报错

确认 X 电机和 Z 电机电线是否有接错或者松动的情况；如[步骤 7](#step7) 所示。安装线缆和并连接其他线缆。

### 屏幕出现TH板或者涡流线圈工作异常

USB-C 线缆可能出现连接异常。松开固定线缆盒的螺丝，参考[步骤7](#step7) 重新插拔 USB-C 线。安装线缆和并连接其他线缆。

### 热床不能正常升温

参考[步骤4](#step4)  检查热床电源线缆连接是否正常。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
