---
path: zh/h2c/maintenance/replace-th-board
title: "更换 H2C TH 板"
description: "本文介绍了如何更换 H2C TH 板"
tags: []
created: 2025-11-18T13:15:21.116Z
updated: 2026-06-02T07:35:58.417Z
source: https://wiki.bambulab.com/zh/h2c/maintenance/replace-th-board
---

## 重要提醒

H2C 挤出主板上的风扇和涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于 PCB 面方向用力抬起以解锁插头**。切勿在水平方向用力，以免损坏插头。

![插头.jpg](https://wiki.bambulab.com/h2/maintenance/laser-module-40w/%E6%8F%92%E5%A4%B4.jpg)

## 挤出接口板/ TH 板/ FPC 排线

本指南将挤出接口板/ TH 板/ FPC 排线的更换教程写在同一篇 Wiki 中，您可以根据实际需求来更换对应的备件。例：如果您只需要更换 FPC 排线，那么即可跳过后续更换 TH 板的步骤。

TH 板和挤出接口板安装在工具头背面，TH 板和挤出接口板之间通过 FPC 排线连接。TH 板、挤出接口板以及配件明细如下：

**挤出接口板的配件明细如下：**

- 挤出接口板 \* 1
- FPC 排线 \* 1
- TH 板 \* 1
- BT2.6x8 螺丝 - 用于固定 TH 板 \* 4
- M1.6x4 螺丝 - 用于固定挤出接口板 \* 2

## 所需的工具和材料

1. 新的 TH 板/ FPC 排线/挤出接口板（请根据实际情况来选择更换对应的配件）
2. H2.0 内六角扳手
3. H1.5 内六角扳手

## 移除挤出接口板/ TH 板/ FPC 排线

### 步骤 1：移除部件冷却风扇风道和风扇

您可以参考[更换 H2D 部件冷却风扇指南](../../h2/maintenance/replace-part-cooling-fan.md)或下方视频（前1分40秒的内容）来移除部件冷却风扇风道和部件冷却风扇。

### 步骤 2：移除挤出接口板

依次拔掉接口板上的 2004 切换电机 FPC 插头（#1）、TH 板接口 FPC 插头（#2）和 2004 升降电机 FPC 插头（#3）。

![16.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/16.png)

| **序号** | **连接对象** |
| --- | --- |
| 1 | 2004 切换电机 |
| 2 | TH 板排线 |
| 3 | 感应热端加热组件电源线 |
| 4 | 2004 升降电机 |

注意：插头均被卡扣压住，需要先解锁卡扣，再拔出 FPC 线缆。

- 1号位置：

![extruder_connection_board-1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/extruder_connection_board-1.png)

- 2号位置：

![extruder_connection_board-2.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/extruder_connection_board-2.png)

- 4号位置：

![extruder_connection_board-4.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/extruder_connection_board-4.png)

依次拔掉这些插头后，使用 H1.5 内六角扳手移除两颗螺丝，解锁加热组件电源线。

|  |  |
| --- | --- |
|  |  |

移除两颗挤出接口板固定螺丝（M1.6x4）；

|  |  |
| --- | --- |
|  |  |

在挤出接口板靠近 2004 切换电机插头的地方轻微晃动，小心地取出挤出接口板。  
![remove_extruder_connection_board.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/remove_extruder_connection_board.png)

### 步骤 3：移除缓冲器和 AP 板盖

由于 MC-TH 线被盖在缓冲器和 AP 板盖后面，因此需要先移除缓冲器和 AP 板盖。

1. **移除 AP 板盖：**

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8）；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-24.png)

然后从靠近前门的一侧取下 AP 板盖。

|  |  |
| --- | --- |
|  |  |

2. **移除缓冲器**

您可以参考这篇 Wiki 的**移除步骤2、3、4、5**来移除缓冲器：[更换 H2C 缓冲器指南](../../h2/maintenance/replace-filament-buffer.md)

### 步骤 4：断开 TH 板上的连接线

依次拔掉 TH 板上的插头，具体的线缆接头及连接对象如下所示：  
![13.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/13.png)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 3513 挤出电机 | 7 | 右涡流线圈 |
| 2 | 挤出接口板 - TH 板 FPC 排线 | 8 | 升降霍尔板 |
| 3 | 热端风扇 | 9 | 左涡流线圈 |
| 4 | 感应热端加热组件 | 10 | 左热端加热组件 |
| 5 | 工具头摄像头 | 11 | 挤出机霍尔转接板 |
| 6 | 喷嘴摄像头 |  |  |

在 TH 板上共有三种插头，根据不同的插头类型您可以使用不同的方法来断开。

其中：

- 1、2、4、5、6、8、11 插头都是通过卡扣固定，您需要先扣开接口上的卡扣，然后将线缆取出；

![h2d_example_how_to_open_securing_clip.gif](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/h2d_example_how_to_open_securing_clip.gif)

- 3、7、9 插头是从正面固定，您需要垂直主板方向推出；

![h2d_animation_example_for_connector_3_7_9.gif](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/h2d_animation_example_for_connector_3_7_9.gif)

- 10 是通过插排固定，您可以直接往外拔出。

### 步骤 5：移除 TH 板

使用 H2.0 内六角扳手移除两颗固定螺丝（BT2.6x8）；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-38.png)

将拖链与拖链底座断开连接，  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-35.png)

![connect.webp](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/connect.webp)

将 MC-TH 线缆和 USB-C 数据线从拖链中取出一些；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-34.png)

转动拖链底座，将缺口与工具头中框上的缺口对齐；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-33.png)

将 TH 板向下拖动一些，将 MC-TH 线缆和 USB-C 数据线一起从缺口中取出，  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-32.png)

最后将 USB-C 线缆与 TH 板断开连接。

|  |  |
| --- | --- |
|  |  |

解开拖链上的两个卡扣（分别安装在第 8 和第 18 节拖链上 —— 从工具头一侧开始数）；  
![remove-buckle.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-buckle.webp)

|  |  |
| --- | --- |
|  |  |

将拖链与打印机上盖断开连接，将 MC-TH 线从拖链中取出；

![remove-cable-chain-from-frame.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-cable-chain-from-frame.webp)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/img_v3_02ip_5131aea0-da53-4529-80ab-71c81d16ed8g.jpg)

然后按下 MC-TH 线缆的卡扣，与 MC-TH 转接线断开连接，抽出拖链中的线缆，移除 TH 板。

|  |  |
| --- | --- |
|  |  |

抽出拖链中的USB-C线缆和MC-TH线缆包；这一步完成后，你将分别得到USB-C线缆，TH主板和拖链。

|  |  |  |
| --- | --- | --- |
|  |  |  |

## 安装挤出接口板/ TH 板/ FPC 排线

### 步骤 1：安装 TH 板

1. 将新的 TH 板与 MC-TH 转接线连接，并将线缆扣入拖链中，然后将拖链与上盖连接；

|  |  |
| --- | --- |
|  |  |

- 先将 USB-C 数据线与 TH 板连接；

> 注意：T 字朝外！！

![t字.jpg](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/t%E5%AD%97.jpg)

- 转动拖链底座，将缺口与工具头中框上的缺口对齐，将 MC-TH 线缆和 USB-C 数据线扣入拖链底座和工具头中框。您可以先将较细的线缆（USB-C 线）先卡入，然后再卡入较粗的线缆（MC-TH 线）；

|  |  |
| --- | --- |
|  |  |

- 将拖链与拖链底座重新连接，并将卡扣扣回拖链上（分别安装在第 8 和第 18 节拖链上 —— 从工具头开始数）；

|  |  |
| --- | --- |
|  |  |

|  |  |
| --- | --- |
|  |  |

![cable-chain-buckle.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/cable-chain-buckle.webp)

- 将 TH 板对准工具头上的螺丝孔位，使用 H2.0 内六角扳手拧紧两颗固定螺丝（BT2.6x8）。

> **注意：在拧紧螺丝前请检查是否有线缆被压在 TH 板下面！**

从上至下，从左至右，需要依次检查的线缆包括：2004 切换电机、3513 挤出电机、热端风扇、挤出接口板插头、挤出机霍尔转接板排线、工具头摄像头、喷嘴摄像头、左右涡流线圈、升降霍尔以及 2004 升降电机排线、左右热端加热组件。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-48.png)

### 步骤 2：连接线缆

依次将线缆接回 TH 板。在 TH 板上共有三种插头，根据不同的插头类型您可以使用不同的方法来连接插头。

**其中：**

- 1,2,4,5,6,8,9,11 这几个插头都是通过卡扣固定，您需要线将排线插入 TH 板的接口中，将线缆完全插入后再扣紧卡扣；

![13.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/13.png)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 3513 挤出电机 | 7 | 右涡流线圈 |
| 2 | 挤出接口板 - TH 板 FPC 排线 | 8 | 升降霍尔板 |
| 3 | 热端风扇 | 9 | 左涡流线圈 |
| 4 | 感应热端加热组件 | 10 | 左加热组件 |
| 5 | 工具头摄像头 | 11 | 挤出机霍尔转接板 |
| 6 | 喷嘴摄像头 |  |  |

**将线缆卡入理线扣：**

如图箭头处有 2 个理线槽，其中下面的箭头处的大理线槽，用于收纳左热端加热组件线缆，上面箭头的小理线槽用于整理左涡流线圈插头、右涡流线圈插头和升降霍尔插头线缆。您可以将这三个插头与 TH 板重新连接后，将线缆重新卡入小理线槽中。

**卡入线缆的先后顺序为：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-63.png)

### 步骤 3：安装缓冲器和 AP 板盖

1. **安装缓冲器：**

您可以参考这篇 Wiki 来安装缓冲器：[更换 H2C 缓冲器指南](../../h2/maintenance/replace-filament-buffer.md)

2. **安装 AP 板盖：**

先从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-59.png)

然后使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-60.png)

### 步骤 4：安装挤出接口板

1. 将挤出接口板的插销对准 TH 板上的插槽，将挤出接口板装入 TH 板；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-58.png)

2. 用 H1.5 内六角扳手拧紧两颗固定螺丝（M1.6x4）；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-62.png)

3. 依次将线缆接回挤出接口板。

![16.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-th-board/16.png)

| **序号** | **连接对象** |
| --- | --- |
| 1 | 2004 切换电机 |
| 2 | TH 板排线 |
| 3 | 感应热端加热组件电源线 |
| 4 | 2004 升降电机 |

### 步骤 5：安装部件冷却风扇和风道

您可以参考这篇 Wiki 中的安装步骤来安装部件冷却风扇和部件冷却风扇风道：[更换 H2C 部件冷却风扇指南](../../h2/maintenance/replace-part-cooling-fan.md)

## 如何验证成功

### 根据电路板灯语判断 TH 板是否正确连接

**正常状态：TH 板指示灯常亮（上&中）、快速闪烁（下）**

在拧回所有螺丝前，可先预装或不装盖子（小心用电安全，断电操作），再通电检查该电路板灯语是否正常，灯语正常，再拧回螺丝，这样可以避免返工。

[

](https://public-cdn.bblmw.com/wiki/H2D/TH1.mp4)

### 连接电源线并打开电源，发起打印，检查是否有报错。

连接电源，打开打印机并发起打印，检查是否可以成功打印。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

**更换 H2C 挤出接口板/ TH 板/ FPC 排线所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

###### 螺丝规格：BT3x8

**用途：**用于固定部件冷却风扇风道

**螺丝数量：**4

**位置示意图：**

[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-14.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-14.png)
[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-10.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-10.png)
[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-9.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-9.png)

###### 螺丝规格：BT3x20

**用途：**用于固定部件冷却风扇

**螺丝数量：**2

**位置示意图：**

[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-7.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-7.png)

###### 螺丝规格：BT2.6x8

**用途：**用于固定部件冷却风扇

**螺丝数量：**2

**位置示意图：**

[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-8.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-8.png)
[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-5.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-5.png)

###### 螺丝规格：BT2.6x8

**用途：**用于固定 AP 板盖

**螺丝数量：**1

**位置示意图：**

[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-4.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-4.png)

###### 螺丝规格：BT2.6x8

**用途：**用于固定 TH 板

**螺丝数量：**2

**位置示意图：**

[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-3.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-3.png)

###### 螺丝规格：M1.6x4

**用途：**用于固定挤出接口板

**螺丝数量：**2

**位置示意图：**

[![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-6.png)](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-6.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
