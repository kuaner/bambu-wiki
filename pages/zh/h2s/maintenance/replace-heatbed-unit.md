---
path: zh/h2s/maintenance/replace-heatbed-unit
title: "更换 H2S 热床组件"
description: "本文介绍了如何更换 H2S 热床组件"
tags: []
created: 2025-08-26T06:44:37.159Z
updated: 2026-02-04T10:54:42.054Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-heatbed-unit
---

## 热床组件

打印机的热床是安装在打印机腔体内，能沿 Z 方向上下运动并能根据用户的设定温度进行加热的平台。设置合适的热床温度能有效提升模型与打印板的粘接力和防止模型翘边。

![dsc04057_compressed.jpg](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-heatbed-unit/dsc04057_compressed.jpg)

**热床组件的备件包含以下：**

1. 热床（预装 H2S 状态灯连接线）\*1
2. M3x8 螺丝 - 用于锁热床与 Z 滑块 \* 6
3. 硅胶塞 \* 2
4. STW3x5 螺丝 - 用于锁热床的地线 \* 1

## 何时更换

- 热床不升温， 且已排查过，确认热床故障；
- 影响功能的物理损坏或明显的形变；
- 经过 Bambu Lab 官方确认需要更换热床。

## 所需的工具和材料

- 新的热床组件
- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除热床

> 本文中的部分图片使用了H2D的热床，H2S和H2D在拆装热床的方法上是相同。因此，请忽略这个小细节，图片仅作示意用途。

### 步骤 1：移除状态灯和喷嘴偏移校准线圈

状态灯通过卡扣固定在热床上，您可以先将状态灯的连接线断开连接，然后**握住状态灯两侧，从后面用力掰解锁后面的卡扣**，当卡扣解锁后再将状态灯往后推，以解锁前面的卡扣，即可取出状态灯；

|  |  |
| --- | --- |
|  |  |

![20250407-115744.gif](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/20250407-115744.gif)

### 步骤 2：移除背板、废料滑梯和 AC 板理线盖

您可以参阅这篇 Wiki 来依次移除

1. 背板
2. 废料滑梯
3. AC 板理线盖

由于更换热床不涉及 AC 板的拆装，因此您可忽略更换 AC 板的步骤：

[更换 H2D AC 板/AC 板理线盖](../../h2/maintenance/replace-ac-board-for.md)

### 步骤 3：断开热床连接线

1. 由于热床与 MC 板的两根连接线在“**步骤 2**”中已经移除，您可以直接跳过这一步。热床与 MC 板连接的两个线缆为 3 和 4，分别为：

- 3：H2S 状态灯连接线
- 4：热床信号线

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-25.png)

2. 当加热模块供电线移除后，可以直接使用镊子顶住热床供电线接头上的卡扣，将供电线移除。依次将三根热端供电线移除；

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-26.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-21.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-23.png)

3. 将热床地线从卡扣中取出并撕开泡棉，然后使用 H2.0 内六角扳手拧松一颗热床地线固定螺丝（STW3x5），将热床地线松开；

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-19.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-16.png)

4. 使用 H2.0 内六角扳手拧松一颗线扣固定螺丝（BT3x12），将线扣打开，将热床线缆一起从卡扣中抽出，然后从左内衬的缝隙中抽出，最后从 Z 滑块后面的卡扣中取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-18.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-17.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-15.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-22.png)

### 步骤 4：移除热床

1. 您可以使用 H2.0 内六角扳手或镊子先撬开热床左右两侧的两个硅胶塞，然后即可看见螺丝。使用 H2.0 内六角扳手依次拧松下图所示的六颗螺丝（M3x8）。

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-20.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-43.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-44.png)

![heatbed.jpeg](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/heatbed.jpeg)

2. 当所有线缆移除以及螺丝拧松后，将热床往上拿出一点，然后将热床线缆先从 Z 滑块中抽出一些，再依次将尼龙扎带中的热床线缆抽出。如果一起抽出的话，由于 Z 滑块的孔隙比较小，插头会互相干涉导致难以抽出，因此建议一次抽出一根连接线，然后直到将所有的线缆移除。

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-42.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-41.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-39.png)

## 安装热床

### 步骤 1：安装热床

1. 接下来您需要将热床线缆依次穿过 Z 滑块的小孔，再将剩余的线缆先对折然后拉出；  
   **首先您可以将红色线缆穿过。**

|  |  |
| --- | --- |
|  |  |

由于孔内较为狭窄需要剥离两个**蓝色**和**棕色**线缆硅胶套，并依次穿过小孔。

|  |  |
| --- | --- |
|  |  |

![pixpin_2025-04-07_19-53-27.png](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/pixpin_2025-04-07_19-53-27.png)

送入红、蓝、棕色线缆后，将**剩余线缆弯折**送入小孔并从另外一端拉出。

|  |  |
| --- | --- |
|  |  |

![mnggiflab-compressed-送入.gif](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/mnggiflab-compressed-%E9%80%81%E5%85%A5.gif)

完成后的状态如下图所示。  
![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-36.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-35.png)

2. 将打印机稍微倾斜或悬空（**请注意扶稳打印机，避免打印机跌落导致损伤**），手动拉动皮带使得三个 Z 滑块下降至底部。在拉动皮带的过程中同时也请将热床立着，避免滑块在下降的时候与热床干涉；

> 注：您可以先来回拉动皮带，确认下降的方向。

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-31.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-34.png)

3. 然后使用 H2.0 内六角扳手拧紧四颗热床滑块固定螺丝（M3x35x8）；

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-30.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-33.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-32.png)

4. 先将热床线缆完全穿过 Z 滑块，再将热床对准三个 Z 滑块，依次拧紧六颗固定螺丝（M3x8），最后将两个硅胶塞重新装入。

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-59.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-58.png)

![heatbed.jpeg](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/heatbed.jpeg)

### 步骤 2：连接热床连接线

1. 将热床线缆依次放入线扣中，然后使用 H2.0 内六角扳手拧紧一颗线扣固定螺丝（ST3x12）；

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-55.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-56.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-57.png)

2. 将热床电源线有卡扣的一侧朝外，依次将三根电源线（棕色、蓝色、红色）与 AC 板连接；

> 请参考下图连接，左上为棕色、右上为蓝色、下方为红色。

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-52.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-53.png)

3. 将原有的热床地线固定螺丝穿过地线的小孔，然后使用 H2.0 内六角扳手将热床锁在打印机底座上，并将地线扣入内衬的线扣中，贴好泡棉；

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-51.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-50.png)

4. 与 MC 板连接的热床信号线和状态灯连接线将在“**步骤 4**”中安装。

### 步骤 3：安装 AC 板理线盖、废料滑梯和背板

您可以参阅下面的这篇 Wiki 依次安装：

1. AC 板理线盖；
2. 废料滑梯；
3. 背板

[更换 H2D AC 板/AC 板理线盖](../../h2/maintenance/replace-ac-board-for.md)

### 步骤 4：安装状态灯

状态灯上有两排卡扣，靠前的一排卡扣较长，您可以先将这一排卡扣对准热床上的孔位，插入后往前拉将卡扣扣入，然后再拿出状态灯往上扣，将后排的卡扣也扣到位，最后重新连接线缆；

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-49.png)

![20250407-115807.gif](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/20250407-115807.gif)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-45.png)

### 步骤 5：移除 Z 滑块固定螺丝

使用 H2.0 内六角扳手移除 4 颗 Z 滑块固定螺丝（M3x35x8）。

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-74.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-73.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-72.png)

### 步骤 6：高温热床调平

更换热床后，为避免打印机工作异常，需完成一次高温热床调平。请点击屏幕“**设置**”>“**校准**”>“**打印校准**”，勾选“**高温热床调平**”，开始校准。

![校准.jpg](https://wiki.bambulab.com/h2/maintenance/replace-mc-board/%E6%A0%A1%E5%87%86.jpg)

## 如何验证成功

连接电源线并打开电源，发起一次打印，确认热床功能是否正常。

## 螺丝规格&数量

**更换 H2S 热床所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定背板（绿色方框标记） |  |  | 12 |
|  |  | 用于固定废料滑梯 |  |  | 1 |
|  |  | 用于固定 AC 板理线盖 |  |  | 1 |
| ST3x8 |  | 用于固定背板（红色圆圈标记） |  |  | 11 |
| ST3x12 |  | 用于固定料盘支架底座（黄色方框标记） |  |  | 2 |
| BT3x12 |  | 用于固定线扣 |  |  | 1 |
| STW3x5 |  | 用于固定地线 |  |  | 1 |
| M3x6 |  | 用于固定热床 |  |  | 6 |
| M3x35x8 |  | 用于固定 Z 滑块 |  |  | 4 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
