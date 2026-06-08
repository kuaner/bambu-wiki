---
path: zh/h2/maintenance/replace-H2D-TH-board
title: "更换 H2D 挤出接口板/TH 板/FPC 排线"
description: "本文介绍了如何更换 H2D 挤出接口板/TH 板/FPC 排线"
tags: []
created: 2025-03-25T03:04:06.264Z
updated: 2026-06-08T02:29:50.026Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-H2D-TH-board
---

## 重要提醒

H2D 挤出主板上的风扇和涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于 PCB 面方向用力抬起以解锁插头**。切勿在水平方向用力，以免损坏插头。

![插头.jpg](https://wiki.bambulab.com/h2/maintenance/laser-module-40w/%E6%8F%92%E5%A4%B4.jpg)

## 挤出接口板/ TH 板/ FPC 排线

本指南将挤出接口板/ TH 板/ FPC 排线的更换教程写在同一篇 Wiki 中，您可以根据实际需求来更换对应的备件。例：如果您只需要更换 FPC 排线，那么即可跳过后续更换 TH 板的步骤。

TH 板和挤出接口板安装在工具头背面，TH 板和挤出接口板之间通过 FPC 排线连接。TH 板、挤出接口板以及配件明细如下：

**挤出接口板的配件明细如下：**

1. 挤出接口板 \* 1
2. M1.6x4 螺丝 - 用于固定挤出接口板 \* 2

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-11.png)

**FPC 排线的配件明细如下：**

1. FPC 排线 \* 1

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-12.png)

**TH 板，目前有两个版本，请以您收到的版本为准。配件明细如下：**

|  |  |
| --- | --- |
| **版本一：** 1. TH 板 × 1 2. BT2.6x8 螺丝 - 用于固定 TH 板 × 4 | **版本二：** 1. TH 板 × 1 2. BT2.6x8 螺丝 - 用于固定 TH 板 × 4  3. MC-TH 电源通讯转接线 × 1 \* |
|  |  |

> 🔺 **注意：** 若您收到版本二的TH板，请检查设备原装转接线是否匹配，若版本不同需要**先更换 MC-TH 电源通讯转接线**，请参考[这篇指南](replace-toolhead-to-mc-board-cable.md)更换。

## 所需的工具和材料

1. 新的 TH 板/ FPC 排线/挤出接口板（请根据实际情况来选择更换对应的配件）
2. H2.0 内六角扳手
3. H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除挤出接口板/ TH 板/ FPC 排线

> 🔺 **注意：** 若您收到[版本二](#my-anchor)的TH板，请检查设备原装转接线是否匹配，若版本不同需要**先更换 MC-TH 电源通讯转接线**，请参考[这篇指南](replace-toolhead-to-mc-board-cable.md)更换。

### 步骤 1：移除部件冷却风扇风道和风扇

您可以参考[更换 H2D 部件冷却风扇指南](replace-part-cooling-fan.md)这篇 Wiki 或者是下方视频（前1分40秒的内容）来移除部件冷却风扇风道和部件冷却风扇。

### 步骤 2：移除挤出接口板

依次拔掉接口板上的 （1号位置）2004 切换电机 FPC 插头、（2号位置）TH 板接口 FPC 插头、（3号位置）左热端加热组件插头及其泡棉（插头位于 TH 主板，泡棉位于挤出接口板），和 （4号位置）2004 升降电机 FPC 插头。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-1.png)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 2004 切换电机 | 2 | TH 板 |
| 3 | 左热端加热组件 | 4 | 2004 升降电机 |

注意：

- **（1号位置）2004 切换电机排线、（2号位置）FPC 线缆**和 **（4号位置）2004 升降电机排线**是被卡扣压住的，需要先解锁卡扣，再拔出 FPC 线缆。

1号位置：  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image.png)

2号位置：  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-2.png)

4号位置：  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-26.png)

- 撕开（3号位置）左热端加热组件插头**泡棉**时，建议先松开插头，再**从下往上**撕开，这样可以保证泡棉的完整性。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-29.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-28.png)

依次拔掉这些插头后使用 H1.5 内六角扳手移除两颗固定螺丝（M1.6x4）；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-25.png)

在挤出接口板靠近 2004 切换电机插头的地方轻微晃动，小心地取出挤出接口板。  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-27.png)

### 步骤 3：移除缓冲器和 AP 板盖

由于 MC-TH 线被盖在缓冲器和 AP 板盖后面，因此需要先移除缓冲器和 AP 板盖。

1. **移除 AP 板盖：**

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8）；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-24.png)

然后从靠近前门的一侧取下 AP 板盖。  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-23.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-19.png)

2. **移除缓冲器**

您可以参考这篇 Wiki 的**移除步骤2、3、4、5**来移除缓冲器：[更换 H2D 缓冲器指南](replace-filament-buffer.md)

### 步骤 4：断开 TH 板上的连接线

依次拔掉 TH 板上的插头，具体的线缆接头及连接对象如下所示：

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-21.png)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 挤出接口板 - TH 板 FPC 排线 | 7 | 右涡流线圈 |
| 2 | 3513 挤出电机 | 8 | 喷嘴摄像头 |
| 3 | 挤出机霍尔转接板 | 9 | 工具头摄像头 |
| 4 | 左热端加热组件 | 10 | 热端风扇 |
| 5 | 左涡流线圈 | 11 | 右热端加热组件 |
| 6 | 升降霍尔板 |  |  |

在 TH 板上共有三种插头，根据不同的插头类型您可以使用不同的方法来断开。

其中：

- 1,2,3,6,8,9 这几个插头都是通过卡扣固定，您需要先扣开接口上的卡扣，然后将线缆取出；
- 5,7,10 这几个插头是从正面固定，您需要沿着接口向上拉出；

![output.webp](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/output.webp)

- 4,11 是通过插排固定，您可以直接往外拔出即可。

  - 注意：4 - 左热端加热组件在“**步骤 2**”中已经移除。

**断开 TH 板上连接线的详细步骤如下：**

1. 先将（11号位置）右热端加热组件的连接线拔出，然后扣开（3号位置）挤出机霍尔转接板接口上的线扣，将线缆抽出；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-18.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-20.png)

2. 先使用镊子剥离（9号位置）工具头摄像头和（8号位置）喷嘴摄像头 FPC 排线的背胶，然后扣开接头处的线扣，将工具头摄像头和喷嘴摄像头 FPC 线抽出；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-17.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-15.png)

3. 如图箭头处有 2 个理线槽，其中下面的箭头处的大理线槽，用于收纳左热端加热组件线缆，上面箭头的小理线槽用于整理左涡流线圈插头、右涡流线圈插头和升降霍尔插头线缆，在拔这 3 个小插头之前，需要**先将 2 个线槽里的线依次抽出来**，以增加线缆长度，便于拔插头。

**抽出线缆的先后顺序请参照下图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-22.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-42.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-43.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-41.png)

- 最后您可以扣开 FPC 接口和 （2号位置）3513 挤出电机接口的卡扣，将 FPC 线缆取下后放置在桌面上（**请保存好，后续将会安装该 FPC 排线**），然后将 3513 挤出电机连接线从卡扣中取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-16.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-40.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-39.png)

### 步骤 5：移除 TH 板

使用 H2.0 内六角扳手移除两颗固定螺丝（BT2.6x8）；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-38.png)

将拖链与拖链底座断开连接，  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-35.png)

将 MC-TH 线缆和 USB-C 数据线从拖链中取出一些；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-34.png)

转动拖链底座，将缺口与工具头中框上的缺口对齐；  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-33.png)

将 TH 板向下拖动一些，将 MC-TH 线缆和 USB-C 数据线一起从缺口中取出，  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-32.png)

最后将 USB-C 线缆与 TH 板断开连接。  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-36.png)

![](https://wiki.bambulab.com/h2/maintenance/disassemble-and-install-h2d-toolhead/image-81.png)

解开拖链上的两个卡扣（分别安装在第 8 和第 18 节拖链上 —— 从工具头一侧开始数）；  
![remove-buckle.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-buckle.webp)  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-31.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-37.png)

将拖链与打印机上盖断开连接，将 MC-TH 线从拖链中取出；

![remove-cable-chain-from-frame.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-cable-chain-from-frame.webp)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/img_v3_02ip_5131aea0-da53-4529-80ab-71c81d16ed8g.jpg)

然后按下 MC-TH 线缆的卡扣，与 MC-TH 转接线断开连接，抽出拖链中的线缆，移除 TH 板。

> 📌 温馨提示：MC-TH 电源通讯转接线有两种版本，请根据您收到的实际版本参考下方示意图断开连接。

版本一：

|  |  |
| --- | --- |
|  |  |

版本二：

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

![install-cable-chain.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/install-cable-chain.webp)

> 📌 温馨提示：MC-TH 电源通讯转接线有两种版本，请根据您收到的实际版本参考下方示意图进行连接。

版本一：  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/img_v3_02ip_3afebc0f-035d-40fc-8f89-bf4285875c0g.jpg)

版本二：

|  |  |
| --- | --- |
|  |  |

- 先将 USB-C 数据线与 TH 板连接；

> 注意：T 字朝外！！

![t字.jpg](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/t%E5%AD%97.jpg)

- 转动拖链底座，将缺口与工具头中框上的缺口对齐，将 MC-TH 线缆和 USB-C 数据线扣入拖链底座和工具头中框。您可以先将较细的线缆（USB-C 线）先卡入，然后再卡入较粗的线缆（MC-TH 线）；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-54.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-53.png)

- 将拖链与拖链底座重新连接，并将卡扣扣回拖链上（分别安装在第 8 和第 18 节拖链上 —— 从工具头开始数）；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-52.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-51.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-50.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-47.png)

![cable-chain-buckle.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/cable-chain-buckle.webp)

- 将 TH 板对准工具头上的螺丝孔位，使用 H2.0 内六角扳手拧紧两颗固定螺丝（BT2.6x8）。

> **注意：在拧紧螺丝前请检查是否有线缆被压在 TH 板下面！**

从上至下，从左至右，需要依次检查的线缆包括：2004 切换电机、3513 挤出电机、热端风扇、挤出接口板插头、挤出机霍尔转接板排线、工具头摄像头、喷嘴摄像头、左右涡流线圈、升降霍尔以及 2004 升降电机排线、左右热端加热组件。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-48.png)

### 步骤 2：连接线缆

依次将线缆接回 TH 板。在 TH 板上共有三种插头，根据不同的插头类型您可以使用不同的方法来连接插头。

**其中：**

- 1,2,3,6,8,9 这几个插头都是通过卡扣固定，您需要线将排线插入 TH 板的接口中，将线缆完全插入后再扣紧卡扣；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-49.png)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 挤出接口板 - TH 板 FPC 排线 | 7 | 右涡流线圈 |
| 2 | 3513 挤出电机 | 8 | 喷嘴摄像头 |
| 3 | 挤出机霍尔转接板 | 9 | 工具头摄像头 |
| 4 | 左热端加热组件 | 10 | 热端风扇 |
| 5 | 左涡流线圈 | 11 | 右热端加热组件 |
| 6 | 升降霍尔板 |  |  |

**序号1 - FPC 排线**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-46.png)

**序号2 - 3513 挤出电机**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-45.png)

**序号3 - 挤出机霍尔转接板**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-44.png)

**序号6 - 升降霍尔板**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-70.png)

**序号8 - 喷嘴摄像头**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-67.png)

**序号9 - 工具头摄像头**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-68.png)

将工具头摄像头和喷嘴摄像头的连接线与 TH 板连接后，您可以将排线重新贴在工具头上，您可以使用镊子来辅助操作，如下图所示。  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-69.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-66.png)

---

- 5,7,10 这几个插头是从正面固定，您需要将接口的金属面朝上，对齐接口后，向下压入插头。

**序号5 - 左涡流线圈**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-64.png)

**序号7 - 右涡流线圈**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-61.png)

**序号10 - 热端风扇**  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-65.png)

---

- 序号 4,11 的位置是通过插排固定，您可以直接将插排对准插头后插入，确保插紧。

**将线缆卡入理线扣：**

如图箭头处有 2 个理线槽，其中下面的箭头处的大理线槽，用于收纳左热端加热组件线缆，上面箭头的小理线槽用于整理左涡流线圈插头、右涡流线圈插头和升降霍尔插头线缆。您可以将这三个插头与 TH 板重新连接后，将线缆重新卡入小理线槽中。

**卡入线缆的先后顺序为：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-63.png)

### 步骤 3：安装缓冲器和 AP 板盖

1. **安装缓冲器：**

您可以参考这篇 Wiki 来安装缓冲器：[更换 H2D 缓冲器指南](replace-filament-buffer.md)

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

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-57.png)

> 上图中对应位置的部件名称：  
> 1.FPC 排线  
> 2.2004 切换电机连接线  
> 3.部件冷却风扇连接线（在步骤 5 中安装）；  
> 4.左热端加热组件  
> 5.2004 升降电机连接线

**连接线缆的详细步骤如下：**

- （图中4号位置的）热端加热组件与 TH 板连接时，您可以将插排对准 TH 板上的插头后插紧，然后将泡棉贴在挤出接口板上，以固定插头；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-56.png)  
![](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E5%AE%89%E8%A3%85%E5%B7%A6%E5%96%B7%E5%98%B4%E6%8E%A5%E5%A4%B4.webp)

- 对于 1,2,5号位置，这几个插头都是通过卡扣固定，您需要线将排线插入挤出接口板的接口中，将线缆完全插入后再扣紧卡扣；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-85.png)

> **注意**：3号位置 - 部件冷却风扇连接线将在“**步骤 5**”中连接。

### 步骤 5：安装部件冷却风扇和风道

您可以参考这篇 Wiki 中的安装步骤来安装部件冷却风扇和部件冷却风扇风道：[更换 H2D 部件冷却风扇指南](replace-part-cooling-fan.md)

## 如何验证成功

### 根据电路板灯语判断 TH 板是否正确连接

**正常状态：TH 板指示灯常亮（上&中）、快速闪烁（下）**

在拧回所有螺丝前，可先预装或不装盖子（小心用电安全，断电操作），再通电检查该电路板灯语是否正常，灯语正常，再拧回螺丝，这样可以避免返工。

[

您的浏览器不支持 HTML5 视频播放。
](https://public-cdn.bblmw.com/wiki/H2D/TH1.mp4)

### 连接电源线并打开电源，发起打印，检查是否有报错。

连接电源，打开打印机并发起打印，检查是否可以成功打印。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 所涉及到的螺丝

**更换 H2D 挤出接口板/ TH 板/ FPC 排线所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

###### 螺丝规格：BT3x8

**用途：**用于固定部件冷却风扇风道

**螺丝数量：**4

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-82.png)
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-78.png)
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-79.png)

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

###### 螺丝规格：暂无

**用途：**用于固定 AP 板盖

**螺丝数量：**1

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-4.png)

###### 螺丝规格：暂无

**用途：**用于固定 TH 板

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-3.png)

###### 螺丝规格：M1.6x4

**用途：**用于固定挤出接口板

**螺丝数量：**2

**位置示意图：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-6.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
