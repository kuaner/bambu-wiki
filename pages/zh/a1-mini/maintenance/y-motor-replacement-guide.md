---
path: zh/a1-mini/maintenance/y-motor-replacement-guide
title: "A1 mini Y 电机更换"
description: "本文提供A1 mini Y 电机拆解和组装的相关指引和注意事项，在这个拆解过程中涉及的可更换配件的拆装也可参考本文进行处理。"
tags: ["a1 mini"]
created: 2025-06-24T08:05:33.356Z
updated: 2025-09-02T03:38:32.990Z
source: https://wiki.bambulab.com/zh/a1-mini/maintenance/y-motor-replacement-guide
---

## Y 电机

Y 电机是安装在打印机 Y 轴上，用于驱动热床在 Y 轴方向上移动的步进电机。

## 何时使用

- Y 电机烧坏
- 经官方技术支持通过分析日志，确认是 Y 电机故障。

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击此处联系在线技术支持 （服务时间 9:00-21:00）](hhttps://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- 新的 X 电机（购买链接：[京东](https://item.jd.com/10086619835424.html) [天猫](https://www.taobao.com/list/item/742404070175.htm)）
- H2.0 内六角扳手
- H1.5 内六角扳手
- 十字螺丝刀
- 钳子
- 平头镊子

## 移除 Y 电机

### 步骤 1：移除底板

向后放倒打印机，使 Z 轴的支柱接触桌面。  
用 H2.0 内六角扳手移除 2 颗螺丝 (BT2.6×8)，再移除 14 颗螺丝 (BT3×8)，拉扯尼龙扎网使底板松动，移除底板。

![a1_mini_y电机拆装_底板螺丝拆装-1.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_%E5%BA%95%E6%9D%BF%E8%9E%BA%E4%B8%9D%E6%8B%86%E8%A3%85-1.png)

### 步骤 2：移除主板风扇

用 H2.0 内六角扳手移除 2 颗螺丝 (MG2.5×15)，再从主板上断开主板风扇连接线。

![a1mini_y_motor_2.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1mini_y_motor_2.png)

### 步骤 3：断开连接线

移除 2 颗螺丝 (BT2×5) 和压片，从主板上断开USB线、Y 电机连接线、X 电机连接线和摄像头连接线。请注意摄像头连接线是带锁扣的，要按压解锁后断开。将尼龙包裹的线缆轻轻移至一侧，避免操作过程中拉扯或损伤内部接线。

![a1_mini_y电机拆装-01.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85-01.png)

### 步骤 4：移除部分电源模块接线

用H2.0内六角扳手移除 3 颗螺丝 (BT3×8)，取下防火盖；

![a1_mini_y电机拆装-4.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85-4.png)

用十字螺丝刀拧松 3 颗端子螺丝，将打印机电源线从电源模块上移除。

![a1_mini_y电机拆装-5.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85-5.png)

### 步骤 5：移除热床

正放打印机，在热床支架上移除 3 颗热床固定螺丝 (M2.5×5);

![a1_mini_y电机拆装6-02.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%856-02.png)

用手压住热床，用H2.0内六角扳手移除4颗调平螺丝 (MG4×13)，取下热床和调整弹簧。如果调整弹簧是固定的，则不需要取下。

![a1_mini_y电机拆装7-03.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%857-03.png)

### 步骤 6：移除 Y 轴线轨

向后推动热床支架，使连接板的 2 颗螺丝露出并将螺丝完全拧松，然后移除滑车上的 2 颗螺丝 (M3×4.5)，取下连接板;

![a1_mini_y电机拆装8-04.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%858-04.png)

移除 2 颗螺丝 (M2.5×18)，取下 Y 轴后盖;

![a1_mini_y电机拆装9-05.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%859-05.png)

移除 4 颗导轨螺丝 (M4×16)，移除 Y 轴导轨，取下导轨时，请同时拿着支架和导轨，防止滑落。

![a1_mini_y电机拆装10-06.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8510-06.png)

### 步骤 7：松开底座

用平头镊子移除 Z 轴装饰盖；

![a1_mini_y电机拆装11-07.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8511-07.png)

用H2.0内六角扳手移除 4 颗螺丝 (BT3×8)；

![a1_mini_y电机拆装12-08.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8512-08.png)

用H2.0内六角扳手移除1 颗螺丝 (BTG3×45)。

![a1_mini_y电机拆装13-09.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8513-09.png)

### 步骤 8：移除 Y 电机

用手轻轻移动底座，露出 Y 电机。用 H2.0 内六角扳手卸下三颗螺丝 (M3×6)；

![a1_mini_y电机拆装14-10.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8514-10.png)

取下皮带，拆下 Y 电机。

![a1_mini_y电机拆装15-11.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8515-11.png)

## 安装 Y 电机

### 步骤 1：安装 Y 电机

如图所求，将 Y 电机穿过电机安装座，确认电缆朝向，并将主动轮挂上 Y 轴同步带后安装到位；锁入 3 颗螺丝 (M3×6) 固定 Y 电机。

![a1_mini_y电机拆装16-12.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8516-12.png)

### 步骤 2：固定底座

锁入 1 颗螺丝 (BTG3×45)和 4 颗螺丝 (BT3×8)， 固定底座；

![a1_mini_y电机拆装17-13.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8517-13.png)

安装 Z 轴装饰盖。

![a1_mini_y电机拆装18-14.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8518-14.png)

### 步骤 3：安装 Y 轴线轨

用镊子移动 Y 皮带压块（从底部视角看为图中方框所示部件），使 2 颗螺丝露出。根据连接板的安装孔确认安装方向，将 Y 轴线轨放置到底座上，对齐螺丝孔，放入 4 颗螺丝 (M4×16)，交替锁紧;

![a1_mini_y电机拆装19-15.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8519-15.png)

移动热床支架，露出 Y 轴同步带压块，然后安装连接板，确认卡到位，锁 2 颗螺丝 (M3×4.5) 固定连接板；

![a1_mini_y电机拆装20-16.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8520-16.png)

然后透过底座，锁紧 2 颗螺丝，移动热床支架，确认热床支架能带动 Y 皮带运动且动作顺畅；

![a1_mini_y电机拆装21-17.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8521-17.png)

安装 Y 轴后盖，锁入 2 颗螺丝 (M2.5×18)。

![a1_mini_y电机拆装22-18.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8522-18.png)

### 步骤 4：安装热床

将 4 个弹簧用胶水预固定到对应位置上，对齐弹簧位置，放置热床，从热床底下确认热床上的 3 个固定片都在热床支架的外侧； 涂胶主要是为了便于安装弹簧，没有其他特殊的用途，如果弹簧已经固定好了，则可以不用胶水固定；

![a1_mini_y电机拆装23-19.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8523-19.png)

放入 4 颗调平螺丝 (MG4×13)，用手将热床调平弹簧压缩，使调平螺丝能够进行锁定，全部锁紧后，再统一将这 4 颗调平螺丝拧松 1 圈；安装 3 颗热床固定螺丝 (M2.5×5)，但不要锁紧，这 3 颗螺丝需要在完成热床的手动调平后再锁紧。

![a1_mini_y电机拆装24-20.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8524-20.png)

### 步骤 5：连接电源模块接线

将电源线连接到输入端子上，棕色线接L，蓝色线接N，两条黄绿色线接地，锁紧3颗螺丝；

![a1_mini_y电机拆装25-21.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8525-21.png)

整理好电源线，安装防火盖，确认没有压到线缆，然后锁入 3 颗螺丝 (BT3×8)。

![a1_mini_y电机拆装26-22.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8526-22.png)

### 步骤 6：连接电缆

将 Y 电机线、X 电机线和摄像头线连接到主板上。连接USB线，确认磁环的位置，并用 2 颗螺丝 (BT2×5) 将压片锁定，整理好线缆，以确保底板能顺利安装，并且主板风扇在运行中不会碰到线缆。

![a1_mini_y电机拆装27-10.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8527-10.png)  
![a1_mini_y电机拆装28-11.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8528-11.png)

### 步骤 7：安装主板风扇

安装主板风扇，风扇的排线朝左，锁入 2 颗螺丝 (MG2.5×15) 固定，连接风扇排线。

![a1_mini_y电机拆装29-12.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8529-12.png)

### 步骤 8：安装底板

安装底板，对齐位置后，锁入 14 颗螺丝（BT3×8）固定; 然后安装走线夹，锁 2 颗螺丝 (BT2.6×8) 固定；正放打印机。

![a1_mini_y电机拆装30-13.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8530-13.png)

## 功能确认和设备校准

完成以上组装指引的全部操作步骤后，启动打印机，进入控制界面，点击屏幕上的 “-Y” 或 “Y” 按钮移动 Y 轴，以确认 Y 电机是否正常运行。

![a1_mini_y电机拆装31-14.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8531-14.png)

在校准页面，选择振动补偿和自动热床调平，点击开始。完成校准后，拧紧 3 颗热床固定螺丝。  
请执行此步骤以确保打印机正常工作。

![a1_mini_y电机拆装32-15.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8532-15.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
