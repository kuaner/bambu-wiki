---
path: zh/a1/maintenance/x-axis-motor
title: "A1 X 电机更换"
description: "本文提供 A1 X 电机拆解和组装的相关指引和注意事项，在这个拆解过程中涉及的可更换配件的拆装也可参考本文进行处理。"
tags: ["a1"]
created: 2025-07-16T03:59:58.744Z
updated: 2025-09-02T03:37:04.882Z
source: https://wiki.bambulab.com/zh/a1/maintenance/x-axis-motor
---

## X 电机

X 电机是安装在打印机 X 轴上，用于驱动工具头在 X 轴方向上移动的步进电机。

## 何时使用

- X 电机烧坏
- 经官方技术支持通过分析日志，确认是 X 电机故障

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

## 移除 X 电机

### 步骤 1：断开连接线

向左放倒机器，**注意保护好工具头**，露出底部理线盒；依次断开摄像头线、X 电机线、Z 电机线；  
拧松 1 颗银色螺丝，滑动线盒断开 USB 线连接。打开理线盒，从中取出 Z 电机线和 X 电机线。

![a1_x电机_1.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_1.png)

### 步骤 2：移除 X 轴组件

从 X 轴背面，移除 6 颗螺丝，将 X 轴组件从龙门架上取下。

![a1_x电机_2.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_2.png)

### 步骤 3：移除电机盒

移除电机盒前盖和后盖；

![a1_x电机_3.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_3.png)

移除线夹，断开摄像头线，移除 4 颗螺丝，向前移除电机盒；

![a1_x电机_4.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_4.png)

将 X 电机线从尼龙编织网管和电机盒前罩中抽出。

![a1_x电机_5.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_5.png)

### 步骤 4：移除同步带右侧压块

移除 2 颗螺丝，松开同步带右侧压块。

![a1_x电机_6.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_6.png)

### 步骤 5：移除电机固定座

移除 3 颗螺丝，取下电机固定座。

![a1_x电机_7.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_7.png)

### 步骤 6：移除 X 电机

移除 4 颗螺丝，取下 X 电机。

![a1_x电机_8.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_8.png)

## 组装 X 电机

### 步骤 1：安装 X 电机

确认 X 电机电缆的朝向，将 X 电机主动轮穿过 X 皮带后，将电机安装到固定座上，锁入 4 颗螺丝。

![a1_x电机_9.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_9.png)

### 步骤 2：安装电机固定座

将电机固定座装到 X 轴上，锁入 3 颗螺丝。

![a1_x电机_7.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_7.png)

### 步骤 3：安装同步带右侧压块

将同步带右侧压块安装到工具头上，锁入 2 颗螺丝。

![a1_x电机_6.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_6.png)

### 步骤 4：安装电机盒

将 X 电机线穿过电机盒前罩和尼龙编织网管；

![a1_x电机_10.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_10.png)

将电机盒装到固定座上，锁入 4 颗螺丝，连接摄像头线，安装线夹；

![a1_x电机_11.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_11.png)

装上电机盒前盖和后盖。

![a1_x电机_12.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_12.png)

### 步骤 5：安装 X 轴组件

将 X 轴对准两个 Z 轴滑块上的定位销，然后安装到 Z 轴滑块上。最后，在每一侧锁入 3 颗螺丝以固定 X 轴组件。

![a1_x电机_13.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_13.png)

### 步骤 6：连接电缆

用胶布固定尼龙编织网管，整理好线材；

![a1_x电机_15.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_15.png)

向后放倒机器，将 X 电机线和 Z 电机线安装到理线盒上；

![a1_x电机_14.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_14.png)

将理线盒安装在底座上，沿槽位方向滑动理线盒，连接 USB 线，锁紧 1 颗银色螺丝;

![a1_x电机_16.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_16.png)

根据文字提示和颜色标贴，连接 X 电机线、Z 电机线和摄像头线，整理线缆，避免线材被压到；正放打印机。

![a1_x电机_17.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_17.png)

## 功能确认和设备校准

完成以上组装指引的全部操作步骤后，启动打印机，进入控制界面，点击屏幕上的“-X”或“X”按钮移动 X 轴，以确认 X 电机是否正常运行。

![a1_x电机_18.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_18.png)

在校准页面，仅选择振动补偿，点击开始。  
请执行此步骤以确保打印机正常工作。

![a1_x电机_19.png](https://wiki.bambulab.com/a1/x-motor/a1_x%E7%94%B5%E6%9C%BA_19.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
