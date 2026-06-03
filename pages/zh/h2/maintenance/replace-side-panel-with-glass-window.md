---
path: zh/h2/maintenance/replace-side-panel-with-glass-window
title: "更换 H2 系列左/右侧板"
description: "本文介绍了如何更换 H2 系列左/右侧板"
tags: []
created: 2025-03-25T02:59:23.984Z
updated: 2026-03-10T08:27:15.760Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-side-panel-with-glass-window
---

## 左/右侧板

左侧板是安装在打印机的左侧（面朝打印机的方向），左侧板上有一个玻璃视窗或激光防护视窗（左）。  
右侧板安装在打印机的右侧。在右侧板的上面装有一块玻璃或激光防护视窗（右）。

**左侧板的备件中包含以下物品：**

1. 左侧板（预装玻璃视窗或激光防护视窗）；
2. ST3x3 螺丝 - 用于在立柱位置锁侧板 \* 2；
3. BT3x8 螺丝 - 用于在上框及辅助部件冷却风扇后面锁左侧板 \* 3

**右侧板的备件包含如下：**

1. 右侧板 - 预装玻璃视窗或激光防护视窗（右）\* 1；
2. BT3x8 螺丝 - 用于固定右侧板 \* 3；
3. ST3x3 螺丝 - 用于固定右侧板 \* 2

## 何时更换

左/右侧板损坏，凹陷等。

## 所需的工具和材料

- 左/右侧板
- H2.0 内六角扳手
- 镊子

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系在线技术支持 （服务时间 9:00-21:00），我们将及时回复并为您提供所需的帮助。

## 视频指南

## 移除左侧板

### 步骤 1：**下降热床**

通过屏幕来控制热床，将热床下降至打印机底部。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-81.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-70.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-82.png)

降低热床后关闭打印机电源，并断开电源连接。

### 步骤 2：移除背板

在移除左侧板前需要先移除背板，您可以参阅这篇 Wiki 来移除 H2D 的背板：

[更换 H2D 背板](replace-rear-panel.md)

### 步骤 3：移除前门玻璃/激光防护视窗（前）

用 H2.0 内六角扳手移除固定前门的 4 颗螺丝（M3x3，螺帽直径 10mm），上下各 2 颗，然后一只手扶住前门玻璃，将前门取下。

> 注意用手扶住前门玻璃，防止跌落。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-80.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-83.png)

### 步骤 4：移除辅助部件冷却风扇

由于有一颗侧板固定螺丝位于辅助部件冷却风扇的后面，因此您需要先移除辅助部件冷却风扇。

辅助部件冷却风扇通过软螺钉（上排两颗）和螺丝（下排两颗）固定。您可以使用 H2.0 内六角扳手移除下排两颗固定螺丝（BT3x16），将风扇用力拔下用于移除软螺钉，然后将风扇放在热床上，无需从 MC 板处断开连接线。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-78.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-77.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-79.png)

您也可以参考这篇 Wiki 来了解移除辅助部件冷却风扇的详细步骤：

[更换 H2D 辅助部件冷却风扇](replace-auxiliary-part-cooling-fan.md)

### 步骤 5：移除左侧板固定螺丝

1. 使用 H2.0 内六角扳手依次移除锁上框的两颗固定螺丝（BT3×8），一颗锁横梁的固定螺丝（BT3×8）；

> 注：AP 板盖上预留了对应的孔位，无需移除 AP 板盖即可移除上框的两颗固定螺丝，下图为便于拍摄将 AP 板盖移除。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-73.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-75.png)

2. 两颗锁在立柱的螺丝（M3×3），这两颗螺丝在胶条后面，您需要从胶条的开孔处撬开胶条，然后即可看见螺丝。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-72.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-76.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-71.png)

### 步骤 6：移除左侧板

1. 左侧板除了使用螺丝固定外，还使用卡扣固定在打印机上。在掰开左侧板之前请先将左侧板上的硅胶撕断，以及将左侧板霍尔连接线从 AC 板理线盖的线扣中松开，避免在掰开侧板的时候扯断线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-74.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-85.png)

2. 然后您可以先掰开位于打印机后方的卡扣；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-86.png)  
![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-98.png)

3. 然后可以使用内六角扳手将左侧板顶部的卡扣撬开，再从正面掰开左侧板，并断开左侧板玻璃霍尔连接线，将贴在左侧板上的胶布撕下，然后取下左侧板。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-99.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-97.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-87.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-96.png)

4. 请注意在辅助部件冷却风扇后面的螺丝孔位处有一个圆形硅胶塞，在拆除侧板时请注意，避免丢失。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-92.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-88.png)

### 步骤 7：移除辅助部件冷却风扇软螺钉（可选）

**如果您的软螺钉未出现损坏或长度足够穿过辅助部件冷却风扇，则可以忽略这一步，无需更换软螺钉。**

您可以从外侧拉动软螺钉，将两颗软螺钉从打印机横梁上移除。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-95.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-93.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-91.png)

## 安装左侧板

### 步骤 1：安装辅助部件冷却风扇软螺钉（可选）

**如果您的软螺钉未出现损坏或长度足够穿过辅助部件冷却风扇，则可以忽略这一步，无需更换软螺钉。**

将软螺钉穿过横梁上的小孔，然后拉动软螺钉直至卡入横梁中。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-94.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-90.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-89.png)

### 步骤 2：扣紧左侧板的卡扣

1. 在安装前请先检查横梁螺丝孔位置处的硅胶塞是否安装到位，如果没有找到请检查是否留在打印机左侧横梁上；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-112.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-111.png)

2. 将左侧板底部的两个大插销先与打印机底部对应的小孔对齐并插入，然后将左侧板霍尔板与霍尔连接线连接，并将粘贴霍尔连接线的胶布重新粘贴到侧板上；

> 建议先将打印机背面的卡扣推进，因为背面的卡扣没有用于固定的舌头，更容易推进。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-114.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-113.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-105.png)

3. 将左侧板缓缓往上推，先用手托住扶手处，将扶手处的卡扣卡入打印机底部，然后将靠近前门和背面的两个小卡扣插入打印机底部对应的小孔中；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-110.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-109.png)

4. **将左侧板底部装好后请先检查底部所有的卡扣是否已经扣到位，并且没有浮起。**然后再将右侧板往内推，将所有卡扣扣到位。

> 卡扣为冗余设计，在拆装的过程中有断裂不影响正常使用，无浮起即可。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-103.png)

### 步骤 3：拧紧左侧板固定螺丝

1. 使用 H2.0 内六角扳手拧紧两颗左侧板内侧的螺丝（BT3x8），然后使用 H2.0 内六角扳手拧紧一颗固定在横梁上的螺丝（BT3×8）；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-104.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-107.png)

2. 撬开硅胶条上的开口，使用 H2.0 内六角扳手拧紧两颗固定螺丝（ST3x3）；

> 如果开口不好撕开，拧可以使用内六角扳手来辅助撬开。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-100.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-101.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-102.png)

### 步骤 4：安装辅助部件冷却风扇

**方法一：**

1. 将软螺钉穿过辅助部件冷却风扇上的靠近内侧的小孔，然后用手拉动软螺钉，将辅助部件冷却风扇的顶部通过软螺钉固定；将内侧的安装完成后再安装外侧的软螺钉；

> 注：
>
> - 软螺钉拉到位时可听见“咔哒”一声；
> - 软螺钉在出厂时做的比较长是为了便于安装，在安装完成后您使用剪刀剪掉一些，以便于更美观。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-108.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-106.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-124.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-123.png)

2. 使用 H2.0 内六角扳手拧紧两颗底部固定螺丝。

> 注：H2D 的辅助部件冷却风扇的固定螺丝均位于上方的小孔中。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-122.png)

**方法二：**

1. 您可以先将辅助部件冷却风扇对准左侧板上的螺丝孔位，然后使用 H2.0 内六角扳手拧紧底部两颗固定螺丝（BT3x16）；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-120.png)

2. 双手轻微掰开辅助部件冷却风扇，将风扇顶部两个螺丝孔位对准软螺钉，将软螺钉插入孔位中；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-117.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-116.png)

3. 使用镊子将软螺钉拉出一些，然后拉动软螺钉使其固定住风扇。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-118.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-119.png)

### 步骤 5：装回前门玻璃/激光防护视窗（前）

将前门上的 4 个螺丝孔位，对齐合页上的螺丝位安装好，用手扶稳前门玻璃，并使用 H2.0 内六角扳手拧紧 4 颗螺丝（M3x3，螺帽直径 10mm）。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-115.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-121.png)

### 步骤 6：装回背板

您可以参考这篇 Wiki 来装回背板：

[更换 H2D 背板](replace-rear-panel.md)

## 移除右侧板

### 步骤 1：移除背板

您可以参阅下面的这篇 Wiki 来移除 H2D 的背板：

[更换 H2D 背板](replace-rear-panel.md)

### 步骤 2： 移除螺丝

1. 撬开硅胶条上的开口，使用 H2.0 内六角扳手移除两颗固定螺丝（ST3x3）；

> 如果开口不好撕开，拧可以使用内六角扳手来辅助撬开。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-30.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-40.png)

2. 使用 H2.0 内六角扳手移除侧板内侧的两颗固定螺丝（BT3x8）

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-38.png)

### 步骤 3：移除右侧板

1. 将粘贴在侧板上的与粘在框架上的胶条撕开，便于后续移除右侧板；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-41.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-31.png)

2. 双手拿住右侧板靠近打印机背面的一侧，用力将侧板掰开以解锁卡扣，然后依次将顶部的卡扣（可使用内六角扳手来辅助撬开顶部卡扣）和前门一侧的卡扣全部解锁；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-2.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-5.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-4.png)

3. 双手拿住右侧板缓缓往下拉直到可以看到右侧板霍尔板连接线，然后按下接口上的卡扣（箭头所示）将霍尔板连接线与霍尔板断开连接，最后将右侧板斜着抽出。

> 注：请勿用力直接将侧板取出，避免扯断霍尔连接线。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-6.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-18.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-28.png)

## 安装右侧板

### 步骤 1：扣紧右侧板的卡扣

1. 将右侧板底部的两个大插销先与打印机底部对应的小孔对齐并插入，然后将右侧板霍尔板与霍尔连接线连接；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-27.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-23.png)

2. 将右侧板缓缓往上推，先用手托住扶手处，将扶手处的卡扣卡入打印机底部，然后将靠近前门的小卡扣插入打印机底部对应的小孔中；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-29.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-24.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-25.png)

3. **将右侧板底部装好后请先检查底部所有的卡扣是否已经扣到位，并且没有浮起。**然后再将右侧板往内推，将所有卡扣扣到位。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-22.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-26.png)

### 步骤 2：拧紧螺丝

1. 使用 H2.0 内六角扳手拧紧两颗右侧板内侧的螺丝（BT3x8）；

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-19.png)

2. 撬开硅胶条上的开口，使用 H2.0 内六角扳手拧紧两颗固定螺丝（ST3x3）；

> 如果开口不好撕开，拧可以使用内六角扳手来辅助撬开。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-21.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-20.png)

### 步骤 3：安装背板

您可以参考这篇 Wiki 来安装 H2D 的背板：

[更换 H2D 背板](replace-rear-panel.md)

## 如何验证完成/成功

安装后侧板无浮起，所有卡扣均扣入打印机中即可。

**更换 H2D 左侧板所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 固定背板（绿色方框标记） |  |  | 12 |
|  |  | 固定左侧板 |  |  | 3 |
| M3x3（螺帽直径 10mm） |  | 固定前门玻璃 |  |  | 4 |
| BT3x16 |  | 固定辅助部件冷却风扇 |  |  | 2 |
| ST3x3 |  | 固定左侧板 |  |  | 2 |
| ST3x8 |  | 固定背板（红色圆圈标记） |  |  | 11 |
| ST3x12 |  | 固定料盘支架底座（黄色方框标记） |  |  | 2 |

**更换 H2D 右侧板所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定背板 |  |  | 12 |
|  |  | 用于固定右侧板 |  |  | 2 |
| ST3x8 |  | 用于固定背板 |  |  | 11 |
| ST3x12 |  | 用于固定料盘支架底座 |  |  | 2 |
| ST3x3 |  | 用于固定右侧板 |  |  | 2 |

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
