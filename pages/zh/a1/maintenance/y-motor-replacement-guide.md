---
path: zh/a1/maintenance/y-motor-replacement-guide
title: "A1 Y 电机更换"
description: "本文提供A1 Y 电机拆解和组装的相关指引和注意事项，在这个拆解过程中涉及的可更换配件的拆装也可参考本文进行处理。"
tags: ["a1"]
created: 2025-07-30T10:04:23.277Z
updated: 2025-09-02T03:36:39.427Z
source: https://wiki.bambulab.com/zh/a1/maintenance/y-motor-replacement-guide
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

- H2.0 内六角扳手
- H1.5 内六角扳手

## 移除 Y 电机

### 步骤 1：移除底板

将屏幕翻向一侧并将 X 轴下降至底部，然后轻放打印机使其正面朝下，如下图所示。建议用一盒耗材垫高顶部，避免压到挤出机和屏幕；

![a1_y_motor_1.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_1.png)

拧松黄色标记螺丝，无需完全取出；  
移除 1、2、3 号线缆，其对应部件分别是摄像头、Z 轴电机、X 轴电机，再向上推出线缆支架断开 USB-C 线缆；

![a1_y_motor_2_画板_1.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_2_%E7%94%BB%E6%9D%BF_1.png)

移除底部 16 颗螺丝，再移除打印机底板。

![a1_y_motor_20.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_20.png)

### 步骤 2：断开线缆

移除散热片固定螺丝和 Y 电机线缆接头；

![a1_y_motor_4.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_4.png)

将 Y 电机线从线槽和卡扣中松出；

![a1_y_motor_5.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_5.png)

移除 2 颗地线固定螺丝。

![a1_y_motor_3.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_3.png)

### 步骤 3：移除热床

将打印机放置在平整的桌面上，缓慢上升 X 轴至顶部；

![a1_y_motor_6.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_6.png)

移除 4 个软硅胶套，再移除 4 颗热床固定螺丝；

![a1_y_motor_7.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_7.png)

> 注意：目前最新版本的热床已取消软硅胶套。  
> ![a1_y_motor_27.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_27.png)

将热床从底座上取下，放置在桌面上。

![a1_y_motor_8.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_8.png)

### 步骤 4：移除 Y 轴上盖

先将 Y 轴上盖后端向上翘起，再水平滑动将其移除。

![a1_y_motor_9.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_9.png)

### 步骤 5：移除 Y 轴组件

将 Y 轴滑车移动到前端，移除 8 颗红色标记螺丝和 2 颗黄色标记螺丝；  
螺丝移除完成后将滑车移动到尾部，再移除前端 2 颗黄色标记螺丝。

![a1_y_motor_10.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_10.png)

移除 1 颗电机固定螺丝，取下 Y 轴组件。

![a1_y_motor_11.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_11.png)

### 步骤 6：调松 Y 轴皮带

释放 Y 轴皮带张紧扭簧，拧松 2 颗张紧器调节螺丝（各拧松 1 圈）。

![a1_y_motor_12.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_12.png)

### 步骤 7：移除 Y 电机

移除 4 颗螺丝，取下 Y 电机。

![a1_y_motor_14.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_14.png)

## 组装 Y 电机

### 步骤 1：安装 Y 电机

确认 Y 电机电缆的朝下，将 Y 电机主动轮穿过 Y 皮带后，将电机安装到固定座上，锁入 4 颗螺丝。

![a1_y_motor_15.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_15.png)

### 步骤 2：张紧 Y 轴皮带

拧紧 2 颗张紧器调节螺丝（各拧紧 1 圈），固定 Y 轴皮带张紧扭簧。

![a1_y_motor_13.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_13.png)

### 步骤 3：安装 Y 轴组件

将 Y 电机线穿过底座，先将 Y 张紧器一端装入底座，然后将 Y 电机端放到位，锁入电机固定座上的 1 颗螺丝；

![a1_y_motor_16.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_16.png)

锁入 12 颗螺丝固定 Y 轴导轨。

![a1_y_motor_10.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_10.png)

### 步骤 4：安装 Y 轴上盖

水平向前滑入 Y 轴上盖，对齐卡扣，将 Y 轴上盖安装到位。

![a1_y_motor_17.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_17.png)

### 步骤 5：安装热床

对准安装位置，将热床放置到热床支架上；

![a1_y_motor_18.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_18.png)

锁入 4 颗热床固定螺丝，安装 4 个软硅胶套。

![a1_y_motor_26.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_26.png)

### 步骤 6：连接线缆

放置打印机使其正面朝下；

![a1_y_motor_1.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_1.png)

穿好 Y 电机线；

![a1_y_motor_19.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_19.png)

将 Y 电机线连接到主板上，锁入 1 颗螺丝将主板散热片固定到 Y 轴导轨上；

![a1_y_motor_4.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_4.png)

锁入 2 颗螺丝固定电源地线，整理好线缆，以确保底板能顺利安装。

![a1_y_motor_3.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_3.png)

### 步骤 7：安装底板

注意线缆盒位置的电机线，插入线缆接头前请确保底壳未压住电机线；  
底壳安装后锁入 16 颗螺丝，此处螺丝为自攻螺丝，避免过度锁紧；

![a1_y_motor_20.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_20.png)

对齐线缆盒后将其向下推入，确保顺利插入 USB-C 电缆；  
拧紧图中黄色标记螺丝，注意螺丝无需过度锁紧；  
依次连接 1、2、3 号线缆，其对应部件分别是摄像头、Z 轴电机、X 轴电机。

![a1_y_motor_21.png](https://wiki.bambulab.com/a1/y-motor/a1_y_motor_21.png)

## 功能确认和设备校准

完成以上组装指引的全部操作步骤后，启动打印机，进入控制界面，点击屏幕上的 “-Y” 或 “Y” 按钮移动 Y 轴，以确认 Y 电机是否正常运行。

![a1_mini_y电机拆装31-14.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8531-14.png)

在校准页面，选择振动补偿和自动热床调平，点击开始。请执行此步骤以确保打印机正常工作。

![a1_mini_y电机拆装32-15.png](https://wiki.bambulab.com/a1-mini/a1mini-y-motor-replacement/a1_mini_y%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%8532-15.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
