---
path: zh/h2/maintenance/replace-cooling-fan-for-hotend
title: "更换 H2D & H2C 热端风扇及其支架"
description: "本文介绍了如何更换 H2D & H2C 热端风扇及其支架"
tags: []
created: 2025-03-25T03:05:45.238Z
updated: 2026-03-13T03:09:31.207Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-cooling-fan-for-hotend
---

> **注意： 本页面以 H2D 机器为例。H2C 的更换步骤完全相同。**

## 重要提示

H2D挤出主板上的风扇和涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于 PCB 面方向用力抬起以解锁插头**。切勿在水平方向用力，以免损坏插头。

![插头.jpg](https://wiki.bambulab.com/h2/maintenance/laser-module-40w/%E6%8F%92%E5%A4%B4.jpg)

## 热端风扇

热端风扇安装在 TH 板和挤出机之间，用于给热端散热，防止耗材在热端中提前软化，从而导致堵头。热端风扇以及配件明细如下：

1. 热端风扇 \* 1
2. M2.5x8 螺丝 - 用于固定热端风扇 \* 2
3. BT2.6x8 螺丝 - 用于固定热端风扇 \* 2

![](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/image-13.png)

## 所需的工具和材料

1. 新的热端风扇
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

## 移除热端风扇

本指南的拆装步骤截取自完整的工具头拆装指南，实际上在更换热端风扇时，并不需要拆除PTFE管、工具头前盖以及左右喷嘴，请按需拆装。

![](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/image-14.png)

### 步骤 1：移除部件冷却风扇风道

1. 使用 H2.0 内六角扳手移除四颗固定螺丝（BT3x8）

![replace_h2d_cooling_fan_for_hotend_and_bracket-1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-1.jpg)

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-2.png)

2. 握住部件冷却风扇风道尾部，小心向下将风道取出。

![replace_h2d_cooling_fan_for_hotend_and_bracket-2.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-2.jpg)

### 步骤 2：移除部件冷却风扇

1. 使用 H2.0 内六角扳手卸下两颗固定螺丝，即标有方形符号的 BT3x20 螺丝。暂时不要卸下部件冷却风扇。其下方仍有两颗螺丝。这些螺丝标有红色箭头，将在下一步卸下。

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-5.png)

2. 使用相同的 H2.0 内六角扳手，卸下标有圆形符号的其余两颗 BT2.6x8 螺丝。

![replace_h2d_cooling_fan_for_hotend_and_bracket-3.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-3.jpg)

3. 然后，小心地将零件冷却风扇组件从工具头处拉开。

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-15.png)

4. 撕掉插头上的醋酸胶布，拔掉插头。可将撕下的胶带留在电路板上，便于后续安装。

> 注意：这种类型的插头应该沿插头所在平面向上小心用力推出，而不是沿着电缆方向拉出。请按照视频中的操作进行，以避免损坏插头。

![replace_h2d_cooling_fan_for_hotend_and_bracket-4.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-4.jpg)

### 步骤 3：移除挤出接口板

根据以下表格的顺序依次断开接口板上的插头：

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 2004 切换电机 | 2 | TH 板 |
| 3 | 左热端加热组件 | 4 | 2004 升降电机 |

> **注意：**（1号位置）2004 切换电机排线、（2号位置）FPC 线缆和（4号位置）2004 升降电机排线是被卡扣压住的，需要先解锁卡扣，再拔出 FPC 线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-1.png)

**1 号位置：** 2004 切换电机。需要先解锁卡扣，再拔出 FPC 线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image.png)

**2 号位置：** TH 板。需要先解锁卡扣，再拔出 FPC 线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-2.png)

**3 号位置：** 左热端加热组件。  
撕开（3号位置）左热端加热组件插头泡棉时，建议先松开插头，再从下往上撕开，这样可以保证泡棉的完整性。

![replace_h2d_cooling_fan_for_hotend_and_bracket-5.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-5.jpg)

**4 号位置：** 2004 升降电机。需要先解锁卡扣，再拔出 FPC 线缆。  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-26.png)

依次拔掉这些插头后使用 H1.5 内六角扳手移除两颗固定螺丝（M1.6x4）。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-25.png)

在挤出接口板靠近 2004 切换电机插头的地方轻微晃动，小心地取出挤出接口板。  
![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-27.png)

### 步骤 4：断开 TH 板上的连接线

依次拔掉 TH 板上的插头，具体的线缆接头及连接对象请参考图片和表格。

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 挤出接口板 - TH 板 FPC 排线 | 7 | 右涡流线圈 |
| 2 | 3513 挤出电机 | 8 | 喷嘴摄像头 |
| 3 | 挤出机霍尔转接板 | 9 | 工具头摄像头 |
| 4 | 左热端加热组件 | 10 | 热端风扇 |
| 5 | 左涡流线圈 | 11 | 右热端加热组件 |
| 6 | 升降霍尔板 |  |  |

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-21.png)

在 TH 板上共有三种插头，根据不同的插头类型您可以使用不同的方法来断开。

其中：

- 1,2,3,6,8,9 这几个插头都是通过卡扣固定，您需要先扣开接口上的卡扣，然后将线缆取出；
- 5,7,10 这几个插头是从正面固定，您需要沿着接口所在的平面推出；
- 4,11 是通过插排固定，您可以直接往外拔出即可。

**断开 TH 板上连接线的详细步骤如下：**

1. **3 号：挤出机霍尔转接板，11 号：右热端加热组件，10 号：热端风扇**

- 3 号和 11 号：先将右热端加热组件的连接线拔出，然后扣开挤出机霍尔转接板接口上的线扣，将线缆抽出。
- 10 号：沿导线方向拨动连接线。请勿拉扯线缆。牢牢握住插头外壳，然后相对于TH板垂直向上拉动以断开连接。

![replace_h2d_cooling_fan_for_hotend_and_bracket-6.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-6.jpg)

2. **9号：工具头摄像头，8号：喷嘴摄像头**

- 先使用镊子剥离工具头摄像头和喷嘴摄像头 FPC 排线的背胶，然后扣开接头处的线扣，将工具头摄像头和喷嘴摄像头 FPC 线抽出。

![replace_h2d_cooling_fan_for_hotend_and_bracket-7.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-7.jpg)

3. 如图箭头处有 2 个理线槽，其中下面的箭头处的大理线槽，用于收纳左热端加热组件线缆，上面箭头的小理线槽用于整理左涡流线圈插头、右涡流线圈插头和升降霍尔插头线缆。

> 在拔这 3 个小插头之前，需要先将 2 个线槽里的线依次抽出来，以增加线缆长度，便于拔插头。

**抽出线缆的先后顺序为：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-22.png)

**5号：左涡流线圈**  
沿导线方向拨动连接线。请勿拉扯线缆。牢牢握住插头外壳，然后相对于TH板垂直向上拉动以断开连接。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-42.png)

**6号：升降霍尔板**  
解锁卡扣以拔出线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-43.png)

**7号：右涡流线圈**  
沿导线方向拨动连接线。请勿拉扯线缆。牢牢握住插头外壳，然后相对于TH板垂直向上拉动以断开连接。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-41.png)

**1号：挤出接口板 - TH 板 FPC 排线，2号：3513 挤出电机**  
您可以扣开 FPC 接口和 3513 挤出电机接口的卡扣，将 FPC 线缆取下后放置在桌面上（请保存好，后续将会安装该 FPC 排线），然后将 3513 挤出电机连接线从卡扣中取出。

![replace_h2d_cooling_fan_for_hotend_and_bracket-8.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-8.jpg)

### 步骤 5：移除 TH 板

1. 断开连接到旋转基座的拖链一侧。

![710f7ce4-fa3c-45f8-8af3-a988de2ca429.png](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/710f7ce4-fa3c-45f8-8af3-a988de2ca429.png)

2. 将 USB-C 数据线和 MC-TH 线缆从拖链中部分拔出，露出约 10 厘米的线缆。

![replace_h2d_cooling_fan_for_hotend_and_bracket-9.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-9.jpg)

3. 使用 H2.0 内六角扳手移除两颗固定螺丝（BT2.6x8）。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-48.png)

4. 将 TH 板从工具头上取出，露出热端风扇。

![](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/image-11.png)

5. 小心地将线缆从线缆槽中取出。这样做可以将 TH 板拉到一侧。

![](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/image-12.png)

### 步骤 6：移除热端风扇

1. 确认喷嘴相机 FPC 排线没有粘住升降电机后盖后，借助镊子撬开升降电机后盖。

![replace_h2d_cooling_fan_for_hotend_and_bracket-10.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-10.jpg)

2. 使用 H2.0 内六角扳手移除两颗固定螺丝（M2.5x8），这2颗螺丝位于塑料中框槽的内部，需按照图示的方向插入螺丝刀拧出。

> 注意：这里强烈建议使用刀头具有磁性的螺丝刀。

![replace_h2d_cooling_fan_for_hotend_and_bracket-11.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-11.jpg)

3. **检查走线槽，确保没有线缆卡住后**（**重要**），捏住热端风扇的下部分，往后推出热端风扇。

![replace_h2d_cooling_fan_for_hotend_and_bracket-12.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-12.jpg)

## 安装热端风扇

### 步骤 1：安装热端风扇

1. 整理线缆，将**升降电机排线**从风扇支架的洞中穿出，其他线缆全部拨开，不要被压住，强烈建议装好热端风扇之后先依次确认每根线缆未被压住后，再锁入螺丝。
2. 从上至下，从左至右，需要依次检查的线缆包括：切换电机、挤出电机、挤出机霍尔转接板排线、工具头摄像头、喷嘴摄像头、左右涡流线圈、升降霍尔以及升降电机排线（最后一个从电机转子后方的洞中穿出）

![replace_h2d_cooling_fan_for_hotend_and_bracket-13.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-13.jpg)

3. 使用 H2.0 内六角扳手拧紧两颗固定螺丝（M2.5x8），并扣上升降电机盖。

![replace_h2d_cooling_fan_for_hotend_and_bracket-14.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-14.jpg)

4. 将升降电机盖卡回原位。

![](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/image-10.png)

### 步骤 2：安装 TH 板

1. 将 MC-TH 线缆和 USB-C 数据线扣入拖链底座和工具头中框。您可以先将较细的线缆（USB-C 线）先卡入，然后再卡入较粗的线缆（MC-TH 线）。

![replace_h2d_cooling_fan_for_hotend_and_bracket-15.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-15.jpg)

2. 重新连接拖链与拖链底座。

![replace_h2d_cooling_fan_for_hotend_and_bracket-16.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-16.jpg)

3. 将 TH 板对准工具头上的螺丝孔位，使用 H2.0 内六角扳手拧紧两颗固定螺丝（BT2.6x8）。

> **在拧紧螺丝前请检查是否有线缆被压在 TH 板下面！**
>
> 从上至下，从左至右，需要依次检查的线缆包括：2004 切换电机、3513 挤出电机、热端风扇、挤出接口板插头、挤出机霍尔转接板排线、工具头摄像头、喷嘴摄像头、左右涡流线圈、升降霍尔以及 2004 升降电机排线、左右热端加热组件。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-48.png)

### 步骤 3：连接线缆

依次将线缆接回 TH 板。在 TH 板上共有三种插头，根据不同的插头类型您可以使用不同的方法来连接插头。

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-49.png)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 挤出接口板 - TH 板 FPC 排线 | 7 | 右涡流线圈 |
| 2 | 3513 挤出电机 | 8 | 喷嘴摄像头 |
| 3 | 挤出机霍尔转接板 | 9 | 工具头摄像头 |
| 4 | 左热端加热组件 | 10 | 热端风扇 |
| 5 | 左涡流线圈 | 11 | 右热端加热组件 |
| 6 | 升降霍尔板 |  |  |

**其中：**

- 1,2,3,6,8,9 这几个插头都是通过卡扣固定，您需要线将排线插入 TH 板的接口中，将线缆完全插入后再扣紧卡扣。

**1：FPC 排线**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-46.png)

**2：3513 挤出电机**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-45.png)

**3：挤出机霍尔转接板**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-44.png)

**6：升降霍尔板**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-70.png)

**8：喷嘴摄像头**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-67.png)

**9：工具头摄像头**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-68.png)

> **小技巧：** 将工具头摄像头和喷嘴摄像头的连接线与 TH 板连接后，您可以将排线重新贴在工具头上，您可以使用镊子来辅助操作。
>
> ![replace_h2d_cooling_fan_for_hotend_and_bracket-17.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-17.jpg)

5,7,10 这几个插头是从正面固定，您需要将接口的金属面朝上，对齐接口后，向下压入插头。

**10：热端风扇**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-65.png)

**5：左涡流线圈**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-64.png)

**7：右涡流线圈**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-61.png)

4,11 是通过插排固定，您可以直接将插排对准插头后插入，确保插紧。

**将线缆卡入理线扣：**

如图箭头处有 2 个理线槽，其中下面的箭头处的大理线槽，用于收纳左热端加热组件线缆，上面箭头的小理线槽用于整理左涡流线圈插头、右涡流线圈插头和升降霍尔插头线缆。  
您可以将这三个插头与 TH 板重新连接后，将线缆重新卡入小理线槽中。

**卡入线缆的先后顺序为：**

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-63.png)

### 步骤 4：安装挤出接口板

1. 将挤出接口板的插销对准 TH 板上的插槽，将挤出接口板装入 TH 板；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-58.png)

2. 用 H1.5 内六角扳手拧紧两颗固定螺丝（M1.6x4）；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-62.png)

3. 依次将线缆接回挤出接口板。  
   图中对应位置的部件名称：  
   | 序号 | 连接对象 | 序号 | 连接对象 |  
   | :--- | :--- | :--- | :--- |  
   | 1 | FPC 排线 | 2 | 2004 切换电机连接线 |  
   | 3 | 部件冷却风扇连接线 | 4 | 左热端加热组件 |  
   | 5 | 2004 升降电机连接线 | | |

**连接线缆的详细步骤如下：**

1. （图中4号位置的）热端加热组件与 TH 板连接时，您可以将插排对准 TH 板上的插头后插紧，然后将泡棉贴在挤出接口板上，以固定插头；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-56.png)

3. 对于 1,2,5号位置，这几个插头都是通过卡扣固定，您需要线将排线插入挤出接口板的接口中，将线缆完全插入后再扣紧卡扣；

![](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/image-85.png)

### 步骤 5：安装部件冷却风扇

1. 金属面朝上，对齐接口后，向下压入部件冷却风扇插头，并贴回醋酸胶布。

![replace_h2d_cooling_fan_for_hotend_and_bracket-18.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-18.jpg)

2. 对准螺丝孔，盖回部件冷却风扇，拧入 4 颗固定螺丝。（BT3x20 方框标记，BT2.6x8 圆圈标记）

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-21.png)

![replace_h2d_cooling_fan_for_hotend_and_bracket-19.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-19.jpg)

### 步骤 6：安装部件冷却风扇风道

1. 左热端加热组件线缆需要安装在理线槽中，在安装风道前，先将加热组件线缆压入理线槽，避免风道压住线缆。

![replace_h2d_cooling_fan_for_hotend_and_bracket-20.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-20.jpg)

2. 先安装前1/4风道，这样可以使后半部分风道更容易倾斜，从而避开喷嘴摄像头的干涉。然后抓住后半部分风道向上推入。

![replace_h2d_cooling_fan_for_hotend_and_bracket-21.jpg](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/replace_h2d_cooling_fan_for_hotend_and_bracket-21.jpg)

3. 推入后，再分别往外掰风道的两侧，将风道的两侧卡在工具头上，然后将风道用力往上卡紧。

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-28.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-29.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-30.png)

4. 接下来往前推入前部分风道的顶部，使其完全贴合，不留缝隙。

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-31.png)

5. 使用 H2.0 内六角扳手拧紧四颗固定螺丝（BT3x8）

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-32.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-33.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-part-cooling-fan/image-34.png)

## 如何验证成功

连接电源，打开打印机。  
导航至 **“控制”** 菜单，然后点击 **“喷嘴和挤出机”** 选项。

![pixpin_2026-01-22_11-57-04.png](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/pixpin_2026-01-22_11-57-04.png)

选择左或右喷嘴，然后点击相应喷嘴温度输入数值。

![pixpin_2026-01-22_11-59-08.png](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/pixpin_2026-01-22_11-59-08.png)

将热端温度提高到100°C。

![screenshot_20251107_091303.png](https://wiki.bambulab.com/h2/maintenance/replace-cooling-fan-for-hotend/screenshot_20251107_091303.png)

最后，在两个热端中间夹一张纸，如果热端温度达到100°C时纸会移动，那么风扇就在正常工作。

如果纸张不移动且感觉不到气流，则需要进一步检查。

- 检查热端温度是否正确。
- 确保工具头上的所有部件都已正确安装。
- 检查所有插头是否完全就位并正确连接。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
