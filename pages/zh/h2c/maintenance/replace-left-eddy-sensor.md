---
path: zh/h2c/maintenance/replace-left-eddy-sensor
title: "更换 H2C 左涡流线圈"
description: "本文介绍 H2C 更换左涡流线圈的详细步骤和注意事项。"
tags: ["h2c"]
created: 2026-08-20T08:53:07.841Z
updated: 2026-08-27T01:47:48.754Z
source: https://wiki.bambulab.com/zh/h2c/maintenance/replace-left-eddy-sensor
---

## H2C 左涡流线圈

涡流线圈参与 Z 轴归零、热床调平及动态流量校准等关键工作流程，其完好性与安装精度直接决定设备的打印精度和整体运行稳定性。H2C 左涡流线圈安装在**升降滑块的后面**。

**左涡流线圈的备件包含如下：**

1. 左涡流线圈 \* 1
2. BT2x6 螺丝 \* 1 - 用于固定左涡流线圈

![nozzle_eddy_sensor_left_h2.png](https://wiki.bambulab.com/h2c/maintenance/replace-left-eddy-sensor/nozzle_eddy_sensor_left_h2.png)

## 何时更换

- 左涡流线圈损坏
- 经 Bambu Lab 官方技术支持确认需要更换左涡流线圈

## 所需的工具和材料

1. 新的左涡流线圈
2. H2.0 内六角扳手
3. H1.5 内六角扳手

## 安全提示

> ❗ **重要提醒**：  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除左涡流线圈

### 步骤 1：移除挤出接口板

首先，移除**部件冷却风扇风道**、**风扇**和**挤出接口板**。  
详细步骤请参考这篇 Wiki 指南中，移除章节的**步骤1-步骤2**：[更换 H2C 挤出接口板](replace-extruder-connection-board.md)

  

### 步骤 2：移除左热端

将热端切换至左热端，随后移除硅胶套，并取下左热端。

|  |  |
| --- | --- |
|  |  |

> ℹ️ **提示**：移除热端前，请先确认堵嘴组件位置。若其位于左热端底部，移除时会发生干涉，可能导致堵嘴弹片弯曲。此时请手动拨动摆杆，将**堵嘴组件移向右侧**，并确保其尾部与磁铁支架右侧的磁铁吸合到位。

### 步骤 3：移除热端风扇左风道

使用 H1.5 内六角扳手，移除一颗左侧风道的固定螺丝（M2x5），将左风道向外取出。

|  |  |
| --- | --- |
|  |  |

### 步骤 4：移除堵嘴磁铁支架

使用 H2.0 内六角扳手，移除两颗堵嘴磁铁支架固定螺丝（M2.5x2），然后将堵嘴磁铁支架取下。

|  |  |
| --- | --- |
|  |  |

### 步骤 5：移除左涡流线圈

将左涡流线圈接口的胶布撕下， 沿着插头所在平面将插头推出。左涡流线圈的线缆卡在热端风扇的线槽中，须先将线缆从线槽中取出，再将其从工具头上抽出。

> ℹ️ **提示**：右图展示的两个线槽用于收纳线缆。您可以**先将左热端加热组件线缆从下方大线槽中取出，再将左涡流线圈连接线从小线槽中取出**。
>
> - **上方小线槽**：左涡流线圈、右涡流线圈、升降霍尔插头线缆
> - **下方大线槽**：左热端加热组件线缆

|  |  |
| --- | --- |
|  |  |
| 左涡流线圈线缆 | 两个线槽 |

使用 H1.5 内六角扳手移除一颗固定螺丝（BT2x6）。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-17.png)

> ℹ️ **提示**：为了确保运输的可靠性和安装的一致性，工厂在组装左涡流线圈时会涂抹一些胶水。因此，当您移除螺丝后，可能需要稍微用力才能从侧面取出左涡流线圈。在安装新的涡流线圈时，不需要涂抹胶水。

## 安装左涡流线圈

### 步骤 1：安装左涡流线圈

由于在工具头上残留的胶水会影响左涡流线圈的安装精度，您可以先试用铲刀去除残留的胶水（胶水颜色为绿色）。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-16.png)

将新的左涡流线圈插入工具头，然后使用 H2.0 内六角扳手将螺丝拧入，不需要将螺丝完全拧紧。然后，准备一小片 A4 纸，将其对折。

|  |  |  |
| --- | --- | --- |
|  |  |  |

> ✅ **说明**：左涡流线圈和升降滑块之间的距离约为 0.2 mm，A4 纸对折后的厚度约为 0.2 mm。

将对折后的 A4 纸插入左涡流线圈和升降滑块之间，用手将左涡流线圈按住，用手拉动 A4 纸，检查 A4 纸是否刚好可以滑动（存在一点阻力，但比较容易取出）。

![插入白纸.webp](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/%E6%8F%92%E5%85%A5%E7%99%BD%E7%BA%B8.webp)

如果可以刚好滑动，再使用 H2.0 内六角扳手将固定螺丝拧紧。在拧紧螺丝的过程中按住左涡流线圈的手需要保持稳定，避免位置发生变化。螺丝拧紧后，再将 A4 纸拔出。

|  |  |
| --- | --- |
|  |  |

将左涡流线圈的线缆先卡入小线槽中，将左涡流线圈连接线接头的金属面朝上，平着压入 TH 板上的接口，并贴好胶布。

<https://cms.bblmw.com/_e10d2a0e07.mp4>

> ℹ️ **提示**：左热端加热组件线缆将在“步骤 5 - 安装挤出接口板”中整理及安装。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-36.png)

### 步骤 2：安装堵嘴磁铁支架

将堵嘴磁铁支架对准螺丝孔位，使用 H2.0 内六角扳手拧紧两颗固定螺丝（M2.5x2）。

|  |  |
| --- | --- |
|  |  |

### 步骤 3：安装热端风扇左风道

插入左侧风道，使用 H1.5 螺丝刀锁紧固定螺丝（M2x5）。

|  |  |
| --- | --- |
|  |  |

### 步骤 4：安装左热端

安装左侧热端，注意锁紧快拆卡扣。正确安装之后，装回**热端硅胶套**。

|  |  |
| --- | --- |
| 热端卡扣错误锁紧 | 热端卡扣正确锁紧 |

### 步骤 5：安装挤出接口板

最后，安装**挤出接口板**、**部件冷却风扇风道**和**风扇**。  
详细步骤请参考这篇 Wiki 指南中，安装章节的**步骤1-步骤2**：[更换 H2C 挤出接口板](replace-extruder-connection-board.md)

## 所涉及到的螺丝

**更换 H2C 左涡流线圈所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

###### 螺丝规格：BT3x8

**用途：**用于固定部件冷却风扇风道

**螺丝数量：**4

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-14.png)
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-10.png)
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-9.png)

###### 螺丝规格：BT3x20

**用途：**用于固定部件冷却风扇

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-7.png)

###### 螺丝规格：BT2.6x8

**用途：**用于固定部件冷却风扇

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-8.png)
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-5.png)

###### 螺丝规格：M1.6x4

**用途：**用于固定挤出接口板

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-6.png)

###### 螺丝规格：M2x5

**用途：**用于固定热端风扇左风道

**螺丝数量：**1

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-5.png)

###### 螺丝规格：M2.5x2

**用途：**用于固定堵嘴磁铁支架

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-4.png)

###### 螺丝规格：BT2x6

**用途：**用于固定左涡流线圈

**螺丝数量：**1

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-7.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
