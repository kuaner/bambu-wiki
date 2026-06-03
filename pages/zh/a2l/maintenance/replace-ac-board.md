---
path: zh/a2l/maintenance/replace-ac-board
title: "A2L 更换 AC 板"
description: ""
tags: []
created: 2026-06-01T13:12:56.134Z
updated: 2026-06-01T13:12:56.134Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/replace-ac-board
---

## A2L AC板

![dlb079.png](https://public-cdn.bblmw.com/wiki/new/a2l/danpintu/dlb079.png)

## 何时使用本指南？

- 热床无法加热
- 开关电源无法上电
- AC板外观损坏
- 拓竹售后技术支持建议更换

## 所需的工具和材料

A2L 主板

- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀
- 十字螺丝刀
- 镊子（可选）

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子元件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## **拆卸教程**

### 1. 拆除前底盖

将Z轴降低至距离热床约 5-8 cm位置。  
![dk001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk001.webp)

翻转打印机露出底盖。  
![dk002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk002.jpg)

使用 H2.0 内六角螺丝刀拆下图示 12 颗螺丝，蓝色标记的两颗螺丝与其他 10 颗不同，请注意区分。  
![dk019.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk019.jpg)

取下 Y 轴张紧器盖板、前底盖。  
![dk006.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk006.webp)![dk012.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk012.webp)

### 2. 拆除 AC 板插头

参照下方提示依次拔出 AC 板上的插头。

![ac001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac001.jpg)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 热床信号线 | 4 | 电源模块转接线 |
| 2 | 热床加热线 | 5 | 主板 — AC连接线 |
| 3 | 市电输入 |  |  |

> 后续操作涉及市电部分，请务必再次确认设备已经完全断电。

1号连接器可以直接向上拔出，5号位置连接器需按下卡扣解锁后拔出。  
![ac009.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac009.webp)

2号位置有两个独立插头，需要使用螺丝刀等尖锐工具将插头弹片向后顶出一段距离解锁，然后拔出插头。  
![ac003.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac003.webp)![ac002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac002.jpg)

3、4号位置各有两个插头，掀开盖板，使用十字螺丝刀拧松对应螺丝后可拔出对应线缆。  
![ac005.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac005.webp)![ac006.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac006.jpg)

### 3. 拆除 AC 板

使用 H1.5 内六角螺丝刀拆除两颗螺丝，取下 AC 板。  
![ac008.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac008.jpg)![ac007.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac007.webp)

## **安装教程**

### 1. 安装 AC 板

将新的转接线插入 AC 板，向上轻拔插头确认插头已经牢固插好。注意线缆颜色顺序需与图片一致。  
![ac011.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac011.jpg)

将AC板装入原位，使用 H1.5 内六角螺丝刀锁入两颗螺丝固定。

![ac010.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac010.webp)![ac008.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac008.jpg)

### 2. 连接 AC 板插头

1、2、5号位置插头可以直接插入，注意将2号插头保护套装回。  
![ac001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac001.jpg)

3、4号插头，先将端子插入方形垫片下方，然后使用十字螺丝刀锁紧螺丝固定。**注意插头及线缆颜色需要与图示保持一致**。  
![ac111.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/ac111.jpg)

> 插头位置和线缆颜色必须与图示完全一致，接错可能导致设备烧毁！

### 3. 安装前底盖

将前底盖装回，按压四周确保安装到位，使用 H2.0 内六角螺丝刀锁入 12 颗螺丝。蓝色标记位置螺丝与其他 10 颗螺丝不同，请注意区分。  
![dk011.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk011.webp)![dk019.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk019.jpg)

装回 Y 轴张紧器盖板  
![dk007.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk007.webp)

小心地将打印机翻转回正常放置位置。  
![dk016.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk016.jpg)

## 功能验证

开启打印机电源，将热床温度调整到65℃，观察热床温度是否正常加热无报错。操作完成后请将热床温度调整回0℃。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队。  
> 我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
