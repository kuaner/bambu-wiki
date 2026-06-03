---
path: zh/h2/maintenance/replace-xy-motor
title: "更换 H2 系列 XY 电机"
description: "本文介绍了如何更换 H2 系列 XY 电机"
tags: []
created: 2025-03-31T01:35:22.557Z
updated: 2026-03-13T03:23:19.348Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-xy-motor
---

## X/Y 电机

X/Y 电机是安装在打印机背部，用于驱动工具头完成 X/Y 方向移动的步进电机。左右各一个，为了方便区分，根据位置分别称为 A 电机、B 电机。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor/image-5.png)

## 何时更换

1. 电机堵转
2. 经 Bambu Lab 技术支持确认需要更换电机

## 所需的工具和材料

1. 新的 X/Y 电机

**X/Y 电机的备件包含如下：**

- 电机 \* 1
- MK3x6 螺丝 - 用于固定电机 \* 4
- M3x6 螺丝 - 用于固定电机轴承支架 \* 2

![XY电机更换相关图片](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor/image-3.png)

2. H2.0 内六角扳手

内六角扳手需要准备一个比较长的（长度应大于122 mm）。

![20251011-101642.jpg](https://wiki.bambulab.com/h2s/maintenance/20251011-101642.jpg)

**拆装过程中所涉及的螺丝规格及数量：**

1. BT3×8 螺丝 - 用于固定背板 \* 12
2. ST3×6 螺丝 - 用于固定背板 \* 11
3. ST3x12 螺丝 - 用户固定料盘支架底座 \* 2

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 更换 X/Y 电机（A）

### 移除 X/Y 电机（A）

#### 步骤 1：移除背板和废料滑梯

![](https://wiki.bambulab.com/h2/maintenance/replace-purge-chute/image-23.png)

您可以参阅这篇 Wiki 来移除打印机背板和废料滑梯：

[更换 H2D 废料滑梯](replace-purge-chute.md)

#### 步骤 2：移除 X/Y 张紧器

1. 使用 H2.0 内六角扳手移除两颗张紧器压板固定螺丝（M3x6）和两颗张紧器支架固定螺丝（M3x6）。

|  |  |
| --- | --- |
|  |  |

2. 用力将 X/Y 皮带张紧器从卡扣中推出。

> 这一步需要稍微用力。

![左扣.webp](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/%E5%B7%A6%E6%89%A3.webp)

#### 步骤 3：移除 X/Y 电机（A）

1. 首先需要移除 A 电机线缆接头，在移除线缆接头时 MC 板散片可能会存在干涉，您可以移除散热片两颗固定螺丝取出散热片。然后将电机线缆接头从 MC 板上断开连接，然后将电机连接线从线槽中取出。

|  |  |
| --- | --- |
|  |  |

> 散热片底部蓝色物质为导热硅脂，请勿清除。

2. 移除电机线缆上的磁环。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/45.jpg)

3. 根据 A 电机内侧的两个螺丝固定位置，找到上框的两个小孔，找到后您可以使用 H2.0 内六角扳手将泡棉戳穿，移除 A 电机内侧的两个固定螺丝（MK3x6）；然后使用 H2.0 内六角扳手移除 A 电机另外两颗固定螺丝（MK3x6）；

> 为便于更换电机，在上盖上开了两个小孔，以便于您可以将内六角扳手穿过上盖，来移除 A 电机的固定螺丝。
>
> **注：由于电机的固定螺丝比较紧，拧松时请确保螺丝刀完全插入内六角孔洞，避免接触面积过小，螺丝滑丝。**

|  |  |
| --- | --- |
|  |  |

4. 使用 H2.0 内六角扳手移除两颗电机轴承支架固定螺丝（M3x6）；

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/15.jpg)

5. 先将电机轴承支架从打印机框架上抽出，并将皮带从电机主动轮上取出，然后倾斜电机，将电机从框架上取出。

![移除电机.webp](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/%E7%A7%BB%E9%99%A4%E7%94%B5%E6%9C%BA.webp)

### 安装 X/Y 电机（A）

#### 步骤 1：安装 X/Y 电机（A）

1. 把电机连接线的出线口对准打印机背面，将电机连接线穿过内衬和框架的小孔，并将线缆拉出。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/26.jpg)

2. 然后将电机斜着从打印机框架上的小孔穿过，将皮带套在 X/Y 电机（A）的主动轮上，将电机轴承支架的缺口对准框架上的插销装入；

|  |  |
| --- | --- |
|  |  |

3. 首先使用 H2.0 内六角扳手拧紧两颗电机轴承支架固定螺丝（M3x6），

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/15.jpg)

接下来使用 H2.0 内六角扳手拧紧 X/Y 电机（A）前面的两颗电机固定螺丝（MK3x6），然后使用较长的 H2.0 内六角扳手拧紧后面两颗电机固定螺丝（MK3x6）。

|  |  |
| --- | --- |
|  |  |

4. 安装电机线缆磁环。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/25.jpg)

5. 将电机线缆接头连接至 MC 板，线缆需要整理到理线扣中避免出现缠绕的情况；完成后重新后安装散热片。

|  |  |
| --- | --- |
|  |  |

#### 步骤 2：安装 X/Y 张紧器

1. 将弹簧插入张紧器支架的轴上，然后将弹簧垂直插进打印机框架，用力往左推动张紧器，将张紧器卡入打印机；

![左扣.webp](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/%E5%B7%A6%E5%AE%89.webp)

2. 安装时需要将薄片凸出位置朝外放置，将张紧器压板对准螺丝孔位后，使用 H2.0 内六角扳手拧紧两颗压板固定螺丝（M3x6）和两颗张紧器支架固定螺丝（M3x6）。

|  |  |
| --- | --- |
|  |  |

#### 步骤 3：安装废料滑梯和背板

![](https://wiki.bambulab.com/h2/maintenance/replace-purge-chute/image-23.png)

您可以参考这篇 Wiki 来安装废料滑梯和背板：

[更换 H2D 废料滑梯](replace-purge-chute.md)

## 更换 X/Y 电机（B）

### 移除 X/Y 电机（B）

#### 步骤 1：移除背板、废料滑梯和 AC 板理线盖

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ac-board-for/image-13.png)

您可以参阅这篇 Wiki 来依次移除。

1. 背板
2. 废料滑梯
3. AC 板理线盖

由于更换 X/Y 电机（B）不涉及 AC 板的拆装，因此您可忽略更换 AC 板的步骤：

[更换 H2D AC 板/AC 板理线盖](replace-ac-board-for.md)

#### 步骤 2：移除 X/Y 张紧器

1. 使用 H2.0 内六角扳手移除两颗张紧器压板固定螺丝（M3x6）和两颗张紧器支架固定螺丝（M3x6）。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/13.jpg)

2. 用力将 X/Y 皮带张紧器从卡扣中推出。

> 这一步需要稍微用力。

![左扣.webp](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/%E5%8F%B3%E6%89%A3.webp)

#### 步骤 3：移除 AP 板盖和护线盖

1. 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖。

|  |  |
| --- | --- |
|  |  |

2. 从右侧扣开护线盖，剪断绑定线束的扎带。

|  |  |
| --- | --- |
|  |  |

#### 步骤 4：移除 4pin 接口板

为便于安装 X/Y 电机（B），在左内衬的顶部预留了小孔（在 4pin 接口板的后面），因此您可以先将 4pin 接口板移除，以便于后续更换 X/Y 电机（B）。

断开 4pin 接口板上的线缆，使用 H1.5 内六角扳手移除 2 颗固定螺丝（BT2x5），然后取下 4pin 接口板。

|  |  |
| --- | --- |
|  |  |

#### 步骤 5：移除 X/Y 电机（B）

1. 首先需要移除 B 电机线缆接头，在移除线缆接头时 MC 板散片可能会存在干涉，您可以移除散热片两颗固定螺丝取出散热片。然后将电机线缆接头从 MC 板上断开连接，然后将电机连接线从线槽中取出。

|  |  |
| --- | --- |
|  |  |

> 散热片底部蓝色物质为导热硅脂，请勿清除。

2. 移除电机线缆上的磁环。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/45.jpg)

3. 将 H2.0 内六角扳手穿过左内衬顶部的小孔，移除 4 颗电机固定螺丝（MK3x6）；

|  |  |
| --- | --- |
|  |  |

4. 然后使用 H2.0 内六角扳手移除 2 颗电机轴承支架固定螺丝（M3x6）；

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/7.jpg)

5. 先将电机轴承支架从打印机框架上抽出，并将皮带从电机主动轮上取出，然后倾斜电机，将电机从框架上取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor/ba1ecb43-7cf8-4bf0-b2fc-672d3a5e9784.jpeg)

### 安装 X/Y 电机（B）

#### 步骤 1：安装 AC 板理线盖

请根据[更换 H2D AC 板/AC 板理线盖](replace-ac-board-for.md)指南，将AC板理线盖预先装回打印机。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ac-board-for/image-13.png)

#### 步骤 2：安装 X/Y 电机（B）

1. 先将电机连接线从内衬的线槽中穿过，并将电机的出线口对准线槽，然后将电机斜着从打印机框架上的小孔穿过，并将皮带套在 X/Y 电机（B）的主动轮上，将电机轴承支架的缺口对准框架上的插销装入；

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor/ba1ecb43-7cf8-4bf0-b2fc-672d3a5e9784-1.jpeg)

2. 使用 H2.0 内六角扳手拧紧两颗电机轴承支架固定螺丝（M3x6）；

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/7.jpg)

3. 您可以先将 H2.0 内六角扳手穿过内衬的小孔，然后将电机固定螺丝放置在 H2.0 内六角扳手上，使用内六角扳手将螺丝送到螺丝孔位处，然后拧紧电机固定螺丝。您可以参考同样的方法依次拧紧四颗 X/Y 电机（B）的固定螺丝（MK3x6）。

|  |  |
| --- | --- |
|  |  |

4. 安装电机线缆磁环。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/25.jpg)

5. 将电机线缆接头连接至 MC 板，线缆需要整理到理线扣中避免出现缠绕的情况；完成后重新后安装散热片。

|  |  |
| --- | --- |
|  |  |

#### 步骤 3：安装 4pin 接口板

将的 4pin 接口板装回打印机，然后使用 H1.5 内六角扳手拧紧两颗固定螺丝（BT2x5），将线缆重新与 4pin 接口板连接。

|  |  |
| --- | --- |
|  |  |

#### 步骤 4：安装 AP 板盖和护线盖

1. 使用扎带将线束捆绑固定，再安装护线盖；安装完成后，需确保线束没有外露。

|  |  |
| --- | --- |
|  |  |

> 如果您没有扎带也可跳过捆绑线束步骤，但需要确保安装护线盖后线束没有外露。

2. 从尾部将 AP 板盖扣入槽内，使用 H2.0 内六角扳手安装固定螺丝（BT2.6x8）。

|  |  |
| --- | --- |
|  |  |

#### 步骤 5：安装 X/Y 张紧器

1. 将弹簧插入张紧器支架的轴上，然后将弹簧垂直插进打印机框架，用力往左推动张紧器，将张紧器卡入打印机；

![左扣.webp](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/%E5%8F%B3%E5%AE%89.webp)

2. 安装时需要将薄片凸出位置朝外放置，将张紧器压板对准螺丝孔位后，使用 H2.0 内六角扳手拧紧两颗压板固定螺丝（M3x6）和两颗张紧器支架固定螺丝（M3x6）。

![](https://wiki.bambulab.com/h2/maintenance/replace-xy-motor2/13.jpg)

#### 步骤 6：安装废料滑梯和背板

您可以参阅下面的这篇 Wiki 依次安装：废料滑梯、背板。  
[更换 H2D 废料滑梯](replace-purge-chute.md)

## 如何验证成功

连接电源并打开打印机，发起打印检查是否有报错。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
