---
path: zh/h2/maintenance/replace-nozzle-lifting-rail
title: "更换 H2D & H2C  升降滑块组件"
description: "本文介绍了如何更换 H2D 及 H2C 升降滑块组件"
tags: []
created: 2025-03-28T09:32:24.069Z
updated: 2026-08-04T03:49:45.327Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-nozzle-lifting-rail
---

> **注意： 本页面以 H2D 机器为例，H2C 的更换步骤相似。**

## 升降滑块组件

升降滑块组件安装在左热端加热组件背面，由升降线轨和升降滑块组成。升降滑块组件以及配件明细如下：

1. 升降滑块 \* 1
2. 升降线轨 \* 1
3. M2x4.5 螺丝 - 用于固定升降滑块和升降线轨 \* 4
4. M2.5x7 螺丝 - 用于固定升降线轨和升降支架 \* 2

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-8.png)

## 何时更换

1. 升降线轨异响
2. 升降线轨卡涩
3. 升降滑块损坏

## 所需的工具和材料

1. 新的升降滑块组件
2. H2.0 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除升降滑块组件

### 步骤 1：移除部件冷却风扇风道和风扇

您可以参考这篇 Wiki 来移除部件冷却风扇风道：

[更换 H2D 部件冷却风扇风道](replace-part-cooling-fan-air-duct.md)

### 步骤 2：移除左热端和左热端加热组件

1. 取下左热端硅胶套，然后解锁热端卡扣，将热端从工具头上取下；

> 需要将热端切换至左热端，您可以通过在屏幕点击切换，或关机并断开电源后手动拨动升降摆杆来切换。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-9.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-7.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-12.png)

2. 使用 H2.0 内六角扳手移除四颗左热端固定螺丝，然后使用 H1.5 内六角扳手移除两颗理线片/挡风片固定螺丝。将热端从升降滑块上取下，无需从 TH 板上断开连接。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-3.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/img_v3_02ip_22cf05b2-0407-49b8-8f53-f5c6ece63b7g.jpg)

### 步骤 3：移除热端风扇左风道

使用 H1.5 内六角扳手移除一颗固定螺丝，将热端风扇左风道往前抽出。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-6.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-2.png)

### 步骤 4：移除挤出机前盖导向

拧出前盖导向上的 4 颗或3颗螺丝（M2.5x7 \* 3；BT2x6 \* 1），具体拧下几颗螺丝以你的实际情况为准。

- [更换 H2D 挤出机前盖导向](replace-dual-extruder-filament-guide.md)

![前盖导向螺丝.png](https://wiki.bambulab.com/h2/maintenance/replace-dual-extruder-filament-guide/%E5%89%8D%E7%9B%96%E5%AF%BC%E5%90%91%E8%9E%BA%E4%B8%9D.png)

用手指向上抵住黑色热端连接件，同时按压左切刀刀柄，使左切刀从切刀螺丝附近的开口槽中脱出一点，然后从前盖导向右下角向外用力撬出前盖导向。

![向上顶住.png](https://wiki.bambulab.com/h2/maintenance/replace-dual-extruder-filament-guide/%E5%90%91%E4%B8%8A%E9%A1%B6%E4%BD%8F.png)

![拆下前盖导向.webp](https://wiki.bambulab.com/h2/maintenance/replace-dual-extruder-filament-guide/%E6%8B%86%E4%B8%8B%E5%89%8D%E7%9B%96%E5%AF%BC%E5%90%91.webp)

左切刀位于前盖导向中，拆除前盖导向时会被一同带出，请注意保存，防止丢失。

> **注意**：拆装前盖导向时无需取下上面的黑色滑块

![正确弹簧.png](https://wiki.bambulab.com/h2/maintenance/replace-dual-extruder-filament-guide/%E6%AD%A3%E7%A1%AE%E5%BC%B9%E7%B0%A7.png)

如不小心取下滑块，请注意正确安装好弹簧（弹簧应当装在左侧），以下为示例。

|  |  |
| --- | --- |
| 正确安装 正确 | 错误安装 错误 |

如不小心错误安装，可按照以下步骤复原：

当弹簧装错时，从右侧向左看上图位置会有一个1.5型号的小螺丝，用1.5的扳手拧下就可以拆下黑色滑块，进而正确安装的弹簧。

### 步骤 5：移除升降滑块和升降线轨

1. 使用 H2.0 内六角扳手移除四颗升降滑块固定螺丝，将升降滑块从左侧抽出；

> 请小心抽出，避免触碰到左涡流线圈！

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-13.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-1.png)

2. 使用 H2.0 内六角扳手移除两颗升降线轨固定螺丝，然后将升降线轨往前抽出。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-25.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/img_v3_02ip_4e201487-9c92-4ad6-9c96-de4426685a8g-1.jpg)

## 安装升降滑块组件

### 步骤 1：安装升降滑块和升降线轨

1. 将新的升降线轨从正面放入升降支架，然后使用 H2.0 内六角扳手拧紧两颗固定螺丝；

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/img_v3_02ip_4e201487-9c92-4ad6-9c96-de4426685a8g.jpg)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-24.png)

2. 将新的升降滑块从左侧插入升降线轨，然后使用 H2.0 内六角扳手拧紧四颗固定螺丝。

> 请小心放入，避免触碰到左涡流线圈！

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-22.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-19.png)

3. **验证：**使用一张 A4 纸对着后插入左涡流线圈和升降滑块之间，检查 A4 纸是否可以滑动。一般而言，左涡流线圈和升降滑块之间的距离为 0.2mm，而一张 A4 纸对折后的厚度为 0.2mm 左右。

### 步骤 2：安装挤出机前盖导向

左切刀需要跟随前盖导向一起安装。确保左切刀的缺口面朝上，然后将其放入前盖导向的切刀槽中。

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-71.png)  
![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-70.png)

安装前盖导向时，需要一直往上顶住黑色热端连接件；

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-66.png)

并轻微按压左切刀，将其调整到一个合适的角度便于左切刀进入，然后将前盖导向装入。最后按压两侧切刀，同时用力将前壳完全压平。

![安装前盖导向.webp](https://wiki.bambulab.com/h2/maintenance/replace-dual-extruder-filament-guide/%E5%AE%89%E8%A3%85%E5%89%8D%E7%9B%96%E5%AF%BC%E5%90%91.webp)

然后重新锁紧前盖导向上的4颗螺丝（M2.5x7 \* 3；BT2x6 \* 1）。

![前盖导向螺丝.png](https://wiki.bambulab.com/h2/maintenance/replace-dual-extruder-filament-guide/%E5%89%8D%E7%9B%96%E5%AF%BC%E5%90%91%E8%9E%BA%E4%B8%9D.png)

### 步骤 3：安装热端风扇左风道

将热端风扇左风道插入热端风扇风道中，然后使用 H1.5 内六角扳手拧紧一颗固定螺丝；

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-18.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-14.png)

### 步骤 4：安装左热端和左热端加热组件

将左热端加热组件装到升降滑块上，使用 H2.0 内六角扳手先拧紧四颗左热端加热组件固定螺丝（M2.5x7，方框标记）；然后放置理线片，使用 H1.5 内六角扳手拧紧两颗固定螺丝（M1.6x4，椭圆标记）。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-23.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-lifting-rail/image-40.png)

### 步骤 5：安装部件冷却风扇风道

您可以参考这篇 Wiki 来安装部件冷却风扇风道

[更换 H2D 部件冷却风扇风道](replace-part-cooling-fan-air-duct.md)

## 如何验证成功

连接电源，打开电源开关，将热端切换至右热端，再切换回左热端，确认是否可以正常切换。然后点击回中，检查是否可以正常回中。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
