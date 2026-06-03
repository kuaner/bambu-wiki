---
path: zh/h2/maintenance/replace-toolhead-sensor-fpc-cable
title: "更换 H2D 挤出机霍尔转接板"
description: "本文介绍如何更换 H2D 挤出机霍尔转接板"
tags: []
created: 2025-08-14T03:04:37.194Z
updated: 2026-02-11T08:50:06.611Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-toolhead-sensor-fpc-cable
---

## 挤出机霍尔转接板

![挤出机霍尔转接板.png](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E6%8C%A4%E5%87%BA%E6%9C%BA%E9%9C%8D%E5%B0%94%E8%BD%AC%E6%8E%A5%E6%9D%BF.png)

挤出机霍尔转接板黏贴于挤出机背面，是一条带接口的柔软排线，取下时需要拧下固定的三颗螺丝。

![背面.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E8%83%8C%E9%9D%A2.jpg)

## 所需工具与准备工作

- H2.0 及 H1.5 内六角扳手
- 小螺丝托盘（防止遗失）
- 新的挤出机霍尔转接板

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 拆卸步骤

### 步骤 1：移除挤出机组件

|  |  |
| --- | --- |
|  |  |

您可以参考这篇 Wiki 或以下视频来将挤出机从工具头拆卸下来：

[更换 H2D 挤出机组件](replace-dual-extruder-unit.md)

#### 视频指南

### 步骤 2：移除左右切刀

将挤出机放置在桌面上，使用 H2.0 内六角扳手移除一颗右切刀刀柄固定螺丝，将右切刀刀柄和扭簧一起从挤出机上拆下。

|  |  |
| --- | --- |
|  |  |

同样的操作，将左切刀也一并拆下。

![移除左右切刀1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E7%A7%BB%E9%99%A4%E5%B7%A6%E5%8F%B3%E5%88%87%E5%88%801.jpg)

### 步骤 3：移除挤出机前盖导向

使用 H2.0 内六角扳手移除三颗固定螺丝（方框标记：M2.5x7 \* 3），然后将挤出机前盖导向往前抽出。

![移除左右切刀2.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E7%A7%BB%E9%99%A4%E5%B7%A6%E5%8F%B3%E5%88%87%E5%88%802.jpg)

抽出方式如下图：

![](https://wiki.bambulab.com/h2/maintenance/replace-extruder-servo-motor/image-17.png)

### 步骤 4：移除挤出机前盖

使用 H2.0 内六角扳手移除两颗固定螺丝（M2.5x7 \* 2），然后轻微晃动，将挤出机前盖取出，然后断开前盖霍尔连接线；

> 注意：请小心拔出挤出机前盖，避免扯断线缆！

|  |  |
| --- | --- |
| 上方螺丝.jpg | 打开前盖.jpg |

### 步骤 5：移除霍尔排线

使用 H1.5 内六角扳手移除挤出机齿轮从动轮组件右侧的霍尔排线固定螺丝（BT2x5 \* 1），然后将右侧的霍尔排线断开连接，以相同操作移除左边。

|  |  |
| --- | --- |
| image-20.png | 左边霍尔排线.jpg |

之后，将背板上固定排线的螺丝拧下。

![背板螺丝.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E8%83%8C%E6%9D%BF%E8%9E%BA%E4%B8%9D.jpg)

再将两侧霍尔排线穿过小孔，轻轻拉到背面并撕下排线，此操作必须轻柔，避免拉断或损伤排线。

|  |  |
| --- | --- |
| 撕下1.jpg | 撕下2.jpg |

撕下的霍尔转接板如下图：  
![撕下3.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E6%92%95%E4%B8%8B3.jpg)

## 安装步骤

### 步骤 1：安装新的霍尔转接板

按照拆下的位置和顺序黏贴好新的霍尔转接板，注意对其排线和背板上的小孔，拧入背板螺丝（黑色）。  
![对准.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E5%AF%B9%E5%87%86.jpg)

翻到正面，分别固定好左右两侧霍尔排线固定螺丝（银色），并将排线贴紧从动轮组件，锁入接口。  
![螺丝和接口.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E8%9E%BA%E4%B8%9D%E5%92%8C%E6%8E%A5%E5%8F%A3.jpg)

### 步骤 2：安装挤出机前盖

将霍尔排线与挤出机前盖连接，然后将挤出机前盖扣回挤出机，然后使用 H2.0 内六角扳手拧紧两颗固定螺丝（M2.5x7 \* 2）。

![打开前盖.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E6%89%93%E5%BC%80%E5%89%8D%E7%9B%96.jpg)

然后使用 H2.0 内六角扳手拧紧两颗固定螺丝（M2.5x7 \* 2）。

![上方螺丝.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E4%B8%8A%E6%96%B9%E8%9E%BA%E4%B8%9D.jpg)

### 步骤 3：安装挤出机前盖导向

将挤出机前盖导向装入挤出机中，然后使用 H2.0 内六角扳手拧紧三颗固定螺丝。

![移除左右切刀2.jpg](https://wiki.bambulab.com/h2/maintenance/replace-tool-head-sensor-fpc-cable/%E7%A7%BB%E9%99%A4%E5%B7%A6%E5%8F%B3%E5%88%87%E5%88%802.jpg)

### 步骤 4：安装左右切刀

将扭簧装入挤出机中，然后将切刀和切刀刀柄一起插入挤出机，使用 H2.0 内六角扳手拧紧一颗固定螺丝。

这一步需要对准前盖、切刀和后盖三个孔眼，会比较困难，请耐心操作，

![](https://wiki.bambulab.com/h2/maintenance/replace-extruder-servo-motor/image-25.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-extruder-servo-motor/image-26.png)

### 步骤 5：安装挤出机

您可以参考这篇 Wiki 来将挤出机重新安装到工具头上：

[更换 H2D 挤出机组件](replace-dual-extruder-unit.md)

## 如何验证成功

连接电源并打开打印机，发起打印，检查是否可以完成打印。

## 附录

**更换 H2D 挤出电机所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| M2.5x7 |  | 用于固定挤出机前盖（红色圆圈标记） |  |  | 3 |
|  |  | 用于固定挤出机前盖 |  |  | 2 |
| BT2x6 |  | 用于固定挤出机前盖（绿色方框标记） |  |  | 1 |
| BT2x5 |  | 用于固定挤出机从动轮霍尔排线 |  |  | 2 |
| BT3x8 |  | 用于固定部件冷却风扇风道 |  |  | 4 |
| BT3x20 |  | 用于固定部件冷却风扇 |  |  | 2 |
| BT2.6x8 |  | 用于固定部件冷却风扇 |  |  | 2 |
|  |  | 用于固定挤出机（红色圆圈标记） |  |  | 2 |
| M2.5x8 |  | 用于固定挤出机（绿色方框标记） |  |  | 4 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
