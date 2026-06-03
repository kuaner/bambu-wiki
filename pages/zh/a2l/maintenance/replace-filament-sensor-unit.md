---
path: zh/a2l/maintenance/replace-filament-sensor-unit
title: "A2L 更换进料霍尔板"
description: ""
tags: []
created: 2026-06-01T13:08:23.446Z
updated: 2026-06-01T13:08:44.236Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/replace-filament-sensor-unit
---

## 进料霍尔板

![fae059.png](https://public-cdn.bblmw.com/wiki/new/a2l/danpintu/fae059.png)

进料霍尔板包含霍尔板及连接排线，请根据实际需要更换相应部件。

## 何时使用本指南？

- 打印机无法正确检测挤出机内部是否进料
- 打印机误报刀切模组未正常安装
- 打印机误报切刀卡住
- 打印机误报挤出机环境温度过高
- 进料霍尔板排线损坏
- 经拓竹售后技术支持后建议更换

## 所需的工具和材料

A2L 热端风扇

- H 2.0 内六角螺丝刀
- H 1.5 内六角螺丝刀
- 镊子

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子元件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## **拆卸步骤**

### 1. 移除TH板

请参照教程完成 TH 板的拆卸：[TH 板更换指南](https://wiki.bambulab.com/zh/a2l/maintenance/replace-th-board)

### 2. 移除刀切模组转接板

使用 H1.5 内六角螺丝刀拆除两颗固定螺丝，取下刀切模组转接板。  
![dq001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq001.jpg)![dq002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq002.jpg)

### 3. 移除五通组件

使用铲刀或镊子等工具轻轻撬开五通组件的固定卡扣，取下五通组件，并取出内部的弹簧。  
![wt006.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-filament-hub/wt006.webp)

### 4. 移除五通底座

使用 H2.0 内六角螺丝刀拆除两颗固定螺丝，然后垂直向上轻轻拔出五通底座。

![gjtwt008.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-filament-hub/gjtwt008.jpg)![wtheb001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/sanliao/wtheb001.webp)  
注意：拔出底座时请务必小心操作，避免扯断或损坏连接排线。

### 5. 移除霍尔板排线

向上翻开霍尔板上的黑色卡扣，即可轻松取下排线。

![wtheb002.webp](https://public-cdn.bblmw.com/wiki/new/a2l/sanliao/wtheb002.webp)

> **如果您的收到的备件已经预装好的底座和霍尔板，可跳过该步骤。**

### 6. 移除进料霍尔板

使用 H1.5 内六角螺丝刀拆除两颗固定螺丝，取下进料霍尔板。此时，您可以检查下五通底座内的方形检测磁铁是否正常回弹。

![gjtwt003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/sanliao/gjtwt003.jpg)![wt007.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-filament-hub/wt007.webp)

## **安装步骤**

### 1.安装霍尔板

将新霍尔板放入定位槽，使用 H1.5 内六角螺丝刀锁紧两颗固定螺丝。

![gjtwt003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/sanliao/gjtwt003.jpg)

> 如果您的收到的备件已经预装好的底座和霍尔板，则无需进行后续拆卸步骤。

### 2.安装霍尔板排线

参照图示安装排线，将排线准确插入霍尔板插座，并压下黑色卡扣固定。  
![wtheb003.webp](https://public-cdn.bblmw.com/wiki/new/a2l/sanliao/wtheb003.webp)

### 3.安装五通底座

将排线穿过工具头，对准位置放入五通底座，使用 H2.0 内六角螺丝刀锁入两颗固定螺丝。  
![gjtwt008.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-filament-hub/gjtwt008.jpg)

### 4.安装五通

将弹簧安装到五通组件  
![gjtwt005.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-filament-hub/gjtwt005.webp)

将五通组件放入底座，请注意组件上的磁铁及固定环卡扣方向需与图示保持一致。

![wt003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-filament-hub/wt003.jpg)![gjtwt006.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-filament-hub/gjtwt006.jpg)

> 五通固定环上设有一个定位缺口。安装时，该缺口应朝向正前方或正后方，请勿朝向其他方向。

对齐固定环与五通底座卡扣，均匀用力向下按压，直至组件完全卡入到位。  
![gjtwt001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-filament-hub/gjtwt001.webp)

### 5.安装刀切模组转接板

轻轻抬起进料霍尔板排线，将刀切模组转接板放入工具头支架，对准螺丝孔位，锁紧两颗固定螺丝。  
![dq003.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cutting-module-adapter-board/dq003.webp)

> 注意：锁紧螺丝前请确认进料霍尔板排线已理顺且未被压住，以免损坏排线。

### 6. 安装TH板

请参照下方教程完成 TH 板的重新安装：[TH 板更换指南](https://wiki.bambulab.com/zh/a2l/maintenance/replace-th-board)

## 功能验证

开启打印机电源，操作打印机进料和退料，如果整个过程顺畅且无报错信息，即表示更换成功。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
