---
path: zh/h2s/maintenance/replace-extruder-motor
title: "更换 H2S 挤出电机"
description: ""
tags: []
created: 2025-08-26T06:10:47.034Z
updated: 2026-01-19T04:20:07.011Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-extruder-motor
---

> **本文拆装步骤2-5，安装步骤1-4的部分螺丝位置图和操作动图仅用作示意图，实际操作时，挤出机组件是被单独拆出并置于桌面上。**

## 挤出电机

挤出电机安装在挤出机背面，用于驱动挤出机，完成耗材的挤出。

**挤出电机的备件包含如下：**

1. 3513 挤出电机 \* 1
2. M2.5x8 螺丝 - 用于固定挤出电机 \* 2

## 何时更换

- 挤出电机损坏

## 所需的工具和材料

1. 新的挤出电机
2. H2.0 内六角螺丝刀
3. H1.5 内六角螺丝刀

## 螺丝清单

- 螺丝A：挤出机组件上方2颗螺丝：BT3x12
- 螺丝B：挤出机组件下方2颗螺丝：M2.5x5
- 螺丝 C: 部件冷却风扇背面（和后盖共锁）以及工具头后盖螺丝，共 3 颗：BT2x6.5; 涡流线圈螺丝同尺寸，2颗。
- 螺丝 D: 热端风扇螺丝，共 2 颗：BT2x4
- 螺丝 E: 部件冷却风扇左右两侧螺丝，共 2 颗： BT2x5
- 挤出电机螺丝：下图中未包含，共2颗，M2.5x8 螺丝 （和螺丝B的形状一样，螺纹长3cm）

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-9.png)

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除 3513 挤出电机

### 步骤 1：移除挤出机组件

您可以参考这篇 Wiki 将挤出机组件从工具头上移除，以便于后续移除挤出电机：[更换 H2S 挤出机组件](replace-extruder-unit.md)

### 步骤 2：松开切刀刀柄

将挤出机组件放置在桌面上，使用 H2.0 内六角螺丝刀移除一颗切刀刀柄固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-8.png)

> **注意**：松开切刀刀柄后请小心操作，避免刀片割刀手。

### 步骤3：移除进料霍尔组件

使用H2.0内六角螺丝刀，移除进料霍尔组件2颗螺丝。

|  |  |
| --- | --- |
|  |  |

### 步骤4：移除挤出机前盖和挤出齿轮

用H2.0内六角扳手拧松侧边的张紧从动杆锁紧螺丝一圈；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image.png)

用 H2.0 内六角扳手移除前盖上的 4 颗螺丝，取下挤出机前面盖

|  |  |
| --- | --- |
|  |  |

用 H2.0 内六角扳手移除侧面螺丝，取出支架的时候内部弹簧和端盖很容易掉落，请用小心取出，防止丢失。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-3.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/remove-spring.webp)

左右晃动，直接取出挤出机大齿轮。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-4.png)

### 步骤5：移除挤出电机螺丝

移除2颗挤出电机螺丝，取下挤出电机.

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-5.png)

## 安装 3513 挤出电机

### 步骤 1：安装 3513 挤出电机

将新的挤出电机对准挤出机后盖上的孔位，然后使用 H2.0 内六角螺丝刀拧紧两颗固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-6.png)

### 步骤2：安装挤出机前盖和挤出齿轮

安装挤出齿轮。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/extruder-gear.webp)

将从动轮支架安装到对应的转轴上。将弹簧和端盖以**正确的方向和位置**（请参考下方的正确和错误示范）安装到一起，放到从动轮支架对应的位置上，拧入侧面螺丝将其顶住，但先不要将其完全拧紧。

> **重要提醒！**  
> 务必正确安装弹簧和端盖，否则将使得挤出机无法咬合耗材，导致打印失败。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/install-spring.webp)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/install-spring-2.webp)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-10.png)

左：正确示范，螺丝顶住端盖凹面；右：错误示范，端盖装错位置，无法使用螺丝压紧弹簧

预锁侧面的螺丝，锁入2-3圈即可，请勿完全拧紧，否则会给安装前盖带来困难。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-11.png)

装回挤出机前盖，拧入挤出机前盖的 4 颗螺丝。

|  |  |
| --- | --- |
|  |  |

拧紧挤出机侧面螺丝；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-13.png)

### 步骤3：安装进料霍尔组件

安装五通组件，请确保黑色 FPC 线缆不要被折叠，顺利放入空缺的位置。然后拧入 2 颗螺丝，固定进料霍尔组件。拧入螺丝前，请从上方检查排线没有压住螺丝孔，避免排线拍螺丝损坏。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/install-filament-sensor.webp)

|  |  |
| --- | --- |
|  |  |

### 步骤4：安装切刀刀柄

在重新固定螺丝之前，请紧握切刀刀柄并保持其位置。在拧紧螺钉时，请注意不要过度用力，以防滑丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-16.png)

### 步骤5：安装挤出机组件

您可以参考这篇 Wiki 来将挤出机组件重新安装到工具头上：

[更换 H2S 挤出机组件](replace-extruder-unit.md)

## 如何验证成功

- 连接电源，启动打印机；
- 在控制页面，点击挤出机挤出按钮，确认电机能正常驱动挤出机；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-motor/image-17.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
