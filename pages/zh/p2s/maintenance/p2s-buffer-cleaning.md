---
path: zh/p2s/maintenance/p2s-buffer-cleaning
title: "P2S 缓冲器清洁指南"
description: "本指南指导如何清洁 P2S 缓冲器内部的碎屑。"
tags: ["p2s", "buffer"]
created: 2025-12-23T03:53:22.474Z
updated: 2026-01-13T02:10:00.374Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/p2s-buffer-cleaning
---

## 何时清洁

- 打印过程中频繁出现缓冲器相关报错
- 进料时不能顺畅通过缓冲器或通过后很快就回退，且已排除挤出机堵塞和内部五通组件的故障。

![1-connect-ams.jpeg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/1-connect-ams.jpeg)

## 所需工具和材料

- H2.0 & H1.5 内六角扳手
- 条形磁铁（辅助拆装，需要自备）
- 清洁工具（棉签、气吹）

## 安全提示

在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请**关闭打印机电源并断开电源连接**，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。

## 准备工作

请参考[更换 P2S 缓冲器 | Bambu Lab Wiki](replace-filament-buffer.md) 从打印机上移除缓冲器。拆卸下来的缓冲器如下图。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/1。.png)

## 操作步骤

操作步骤包括 基础清洁和深度清洁。

**基础清洁：** 只移除缓冲器电路板即可完成的清洁操作；  
**深度清洁：** 需拆解分离耗材通道后才能完成的清洁操作，容易导致内部小配件的跌落，务必在干净的水平台面上进行操作。

### 基础清洁（优先）

#### 步骤 1 ：移除黑色上盖和电路板

1. 用 H1.5 内六角扳手移除固定黑色上盖和电路板的 4 颗螺丝。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/2。.png)

2. 依次取下黑色上盖和电路板。
3. 为避免丢失，请将红色箭头指示的弹簧和磁铁取出并妥善保管。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/3。.png)

#### 步骤 2 ：清除缓冲器内部明显的杂质

在缓冲器内，料筒周围有时会堆积熔融耗材丝。请检查该区域，并清除所有肉眼可见的杂质。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/4。.png)

#### 步骤 3 ：清理耗材通道内部中的杂质

1. 取一小段耗材，从双气动接头的一端插入，沿另一侧推出。反复操作2~3次，疏通内部杂质。使用相同方法清理另一条通道。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/5._用耗材通.gif)

2. 耗材通道内部可能仍残留细小碎屑，前一步的操作无法完全清除。请使用气吹对通道进行吹扫，以排出内部残留物。

#### 步骤 4 ：安装黑色上盖和电路板

1. 将辅助磁铁贴在缓冲器外部，靠近左侧两个气动接头的位置。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/6.png)

使用内六角扳手装回磁铁，请注意磁铁的方向。再将弹簧放置在磁铁上方。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/7.png)

2. 依次装回电路板和黑色上盖。
3. 用 H1.5 内六角扳手拧上 4 颗固定螺丝。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/8。.png)

#### 步骤 5 ：验证功能

1. 请参考[更换 P2S 缓冲器 | Bambu Lab Wiki](replace-filament-buffer.md) 将缓冲器装回打印机。
2. 将 AMS 连接到打印机并打开电源。将耗材装载到 AMS 的任一料槽中，然后单击屏幕上的“进料”；进料完成后，再点击“退料”，执行一次退料操作。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/9.png)

若进退料过程表现正常，说明缓冲器已清洁完成，可以正常使用。

若仍无法正常使用打印机，请继续尝试深度清洁。

### 深度清洁（请严格按照操作步骤处理）

#### 步骤 1 ：移除螺丝

用 H1.5 内六角扳手移除固定料筒的 2 颗螺丝。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/10。.png)

#### 步骤 2 ：移除进料气动接头

1. 捏住 Y 型料筒两侧，轻轻向上抬起料筒的上半部分。

![](https://wiki.bambulab.com/p2s/maintenance/replace-pneumatic-connector/remove_connectors_3.jpg)

2. 然后，在两个气动接头中间抬起的缝隙中，插入内六角扳手或其他细长工具，适度用力撬开料筒。

**注意：请勿过度用力掰开或撬开，以免料筒部件损坏。**

![](https://wiki.bambulab.com/p2s/maintenance/replace-pneumatic-connector/marked_remove_connectors_1.png)
![](https://wiki.bambulab.com/p2s/maintenance/replace-pneumatic-connector/remove_connectors_2.jpg)

3. 此时，即可取出气动接头。

![](https://wiki.bambulab.com/p2s/maintenance/replace-pneumatic-connector/install_connectors_4.jpg)

#### 步骤 3 ：取出料筒

按照箭头所指方向推动黄色滑块，压缩弹簧，取出料筒。

|  |  |
| --- | --- |
|  |  |

> 注意  
> 在分离黄色滑块与料筒时，请不要刮掉黄色滑块连接弹簧上的白胶。如果白胶脱落，弹簧将无法固定在灰色卡扣下方，可能导致耗材无法顺利通过缓冲器，引起进料失败。  
> ![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/13.png)

#### 步骤 4 ：清洁黄色滑块内部的碎屑

取一根棉签，清洁黄色滑块内部的碎屑。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/14_清洁黄色结构.gif)

#### 步骤 5 ：清洁料筒表面碎屑

取下料筒上的弹簧，用棉签清理料筒表面的碎屑。清洁完成后，装回弹簧。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/15_清洁黑色y.gif)
> **注意:**  
> 料筒的背面有一个小卡扣（红框区域）。安装弹簧时，如果听到清晰的“咔哒”声，说明已正确卡入位置。弹簧的开口由大到小递减，正确的安装位置位于较大的开口端，接近第一圈与第二圈弹簧的交界处。  
> ![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/16。.png)

#### 步骤 6 ：装回料筒及气动接头

1. 压缩弹簧，安装料筒。
2. 使用内六角扳手或其他细长工具，插入料筒出口，适度用力撬开料筒。

**注意：请勿过度用力掰开或撬开，以免料筒部件损坏。**

![](https://wiki.bambulab.com/p2s/maintenance/replace-pneumatic-connector/marked_install_connectors_2.png)

3. 然后，依次插入气动接头。

![](https://wiki.bambulab.com/p2s/maintenance/replace-pneumatic-connector/install_connectors_5.jpg)
![](https://wiki.bambulab.com/p2s/maintenance/replace-pneumatic-connector/install_connectors_4.jpg)
![](https://wiki.bambulab.com/p2s/maintenance/replace-pneumatic-connector/pneumatic_connector_on_buffer.jpg)

4. 用 H1.5 内六角扳手拧上 2 颗固定螺丝。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/18。.png)
> 注意  
> 在上述拆卸过程中，如果发现缓冲器内部存在任何结构损坏，请更换缓冲器。

#### 步骤 7 ：安装黑色上盖和电路板

1. 将辅助磁铁贴在缓冲器外部，靠近左侧两个气动接头的位置。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/19.png)

使用内六角扳手装回磁铁，请注意磁铁的方向。再将弹簧放置在磁铁上方。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/20.png)

2. 依次装回电路板和黑色上盖。
3. 用 H1.5 内六角扳手拧上 4 颗固定螺丝。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/21。.png)

#### 步骤 8 ：验证功能

1. 请参考[更换 P2S 缓冲器 | Bambu Lab Wiki](replace-filament-buffer.md) 将缓冲器装回打印机。
2. 将 AMS 连接到打印机并打开电源。将耗材装载到 AMS 的任一料槽中，然后单击屏幕上的“进料”；进料完成后，再点击“退料”，执行一次退料操作。

![](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/22.png)

若进退料过程表现正常，说明缓冲器已清洁完成，可以正常使用。

否则，请检查电缆连接后重试。如果未发现异常但仍出现故障，请联系 Bambu Lab 服务团队以获得进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请在下方留下
>
> 请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
