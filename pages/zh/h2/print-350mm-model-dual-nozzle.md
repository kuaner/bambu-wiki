---
path: zh/h2/print-350mm-model-dual-nozzle
title: "如何使用 H2D 双喷嘴打印大型模型"
description: "H2D 拥有 350 mm 宽的打印板，让我们来充分地使用它。"
tags: []
created: 2025-12-17T01:24:03.039Z
updated: 2025-12-19T03:57:26.439Z
source: https://wiki.bambulab.com/zh/h2/print-350mm-model-dual-nozzle
---

**H2D打印板的宽度是 350 毫米，但只能打印 320 毫米宽的模型？并非如此，让我们来了解一下原因！**

![full-bed-print_wiki.jpg](https://wiki.bambulab.com/h2/how-to-print-350mm-models/full-bed-print_wiki.jpg)

## 可打印区域限制

H2D 可实现真正的双材料打印，极大地扩展了设计灵活性。但是，它无法使用整个打印板的宽度。双喷头工具头的可打印区域存在特定限制。要了解更多关于 H2D 可打印区域的信息，请访问此 Wiki: [H2D 双喷嘴可打印范围介绍](manual/printable-range-for-dual-nozzles.md)。  
左侧喷头最大打印宽度为 325 毫米，右侧喷头最大打印宽度也为 325 毫米。下图展示了这些区域的划分：

|  |  |
| --- | --- |
|  |  |
| 左喷嘴可打印区域 | 右喷嘴可打印区域 |
|

如果我们观察打印板上工具头的位置，能很容易地分辨这些区域：

|
|  |
|  |  |  |
| 双喷嘴切换 | 左喷嘴触及打印板最左侧 | 右喷嘴触及打印板最右侧 |
|

## 如何打印一个 350 毫米的模型

如果您需要打印 350 毫米宽的模型，有一个技巧可以让 H2D 在使用单一材料时打印全宽物体。虽然有一些注意事项，但让我们深入了解一下！

该模型会同时延伸至“仅左喷嘴可打印区域”和“仅右喷嘴可打印区域”。两个喷嘴都无法进入对方的限制区域。但是，您可以使用右侧喷嘴打印模型的大部分，而位于仅限左侧区域的一小部分可以使用左侧喷嘴打印，反之亦然。

### 装载耗材

要使用这种方法打印，两个喷嘴必须使用相同的耗材。如果模型使用 PLA 打印，则两个喷嘴都应载入 PLA 耗材。建议使用同一品牌和颜色的材料，以避免粘合问题。如果使用不同的材料或颜色，两个打印部分之间的连接处可能会成为薄弱点。

**在两个喷嘴中载入相同的耗材：**  
在本例中，左侧喷嘴使用外置耗材支架，右侧喷嘴使用 AMS 2 PRO。在两个槽位中装入相同类型和颜色的耗材。  
![load_filament_wiki.jpg](https://wiki.bambulab.com/h2/how-to-print-350mm-models/load_filament_wiki.jpg)

在触摸屏上，点击 ① 外部耗材卷轴，然后点击 ② 编辑，为每个喷嘴设置耗材品牌、类型和颜色。③ 选择与实际耗材颜色不同的显示颜色。在本例中，我们将使用绿色。  
![screencn.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/screencn.png)  
如此设置有助于后续您在 Bambu Studio 中识别模型的各个部分，不会影响打印质量或零件的最终颜色。  
![screencn2.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/screencn2.png)

### Bambu Studio 设置

导入您的模型并根据需要调整其大小与方向。本次示例使用了 [mail.iou 提供的 袋子封口夹 模型](https://makerworld.com/zh/models/92592-bag-closure-clips#profileId-99029)并将模型整体放大到 350 毫米宽。此时，Bambu Studio可能会显示错误信息，这是正常现象，可以忽略。

![clip_cn.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/clip_cn.png)

要成功打印，模型必须分割成两部分，一部分由右侧喷嘴打印，另一部分由左侧喷嘴打印。  
要分割模型，请导航至顶部菜单并选择 ① “剪切”。

![cutcn.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/cutcn.png)

出现切割选项后，首先确保对象 A 和对象 B 都选中了 ① “保持方向”，然后勾选 ② “切割到零件”。现在我们可以使用 ③ 轴控件来调整切割面。

![demonscn.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/demonscn.png)

我们可以使用 ④ 角度调节旋钮绕轴旋转平面，只需点击并拖动即可。角度设置好后，我们可以拖动 ⑤ 移动方块沿着轴移动平面。

|  |  |
| --- | --- |
|  |  |
|

最后，当切割面设置符合预期后，单击 ⑥ “执行切割”。

![demons4cn.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/demons4cn.png)

> 在本例中，请将模型分割成不同时出现在两个限制区域内的部件，否则无法打印。以下为分割示例：

|  |  |  |
| --- | --- | --- |
|  |  |  |
|

模型分割完成后，您可以为左右喷嘴分别指定耗材。打开“对象”面板，确认模型已分割为两部分。

将绿色耗材分配给左喷嘴打印的部分。虽然该耗材在 Bambu Studio 中显示为绿色，但它代表的是外置线轴支架上装载的白色 PLA 耗材。因此，模型的左边部分在预览中会显示为绿色。

![demons7.gif](https://wiki.bambulab.com/h2/how-to-print-350mm-models/demons7.gif)

现在模型已经准备好打印了，把它切片然后发送到打印机，然后等待它打印完成吧！

#### 关于切割工具

通过以上命令，您可以将切割面放置在任何您想要分割模型的位置。

![demons6.gif](https://wiki.bambulab.com/h2/how-to-print-350mm-models/demons6.gif)

> 请注意，分割位置会显著影响最终效果和总打印时间。

以下的示例说明了分割位置对打印时间的影响。虽然在本模型中影响不大，但其影响会因模型而异。

![timecn.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/timecn.png)

### 打印模型

在打印时可以观察到，工具头根据 Bambu Studio 中定义的设置切换自动左右喷嘴。在本例中，左侧喷嘴用于打印模型置于打印版最左侧的分件,正如耗材分配的那样。

![first_layer_dual_nozzle_350mm.gif](https://wiki.bambulab.com/h2/how-to-print-350mm-models/first_layer_dual_nozzle_350mm.gif)

由于工具头需要在每一层都切换喷嘴，因此这种打印方式比使用单喷嘴打印耗时更长。但是，它可以让您有效地利用打印平台的全部宽度。

![full-bed-print_wiki.jpg](https://wiki.bambulab.com/h2/how-to-print-350mm-models/full-bed-print_wiki.jpg)

切割面始终可见。模型分件相接处会出现一条垂直的接缝线，这条接缝线会出现在侧面和顶面上。不过，这种接缝通常很牢固，一般不会在模型中形成薄弱点。

![seam_wiki.jpg](https://wiki.bambulab.com/h2/how-to-print-350mm-models/seam_wiki.jpg)

使用这个小技巧，我们就可以打印大型模型，让我们的玉米饼保持新鲜！发挥您的想象力，制作任何您想要的东西！

![torilha_wiki.jpg](https://wiki.bambulab.com/h2/how-to-print-350mm-models/torilha_wiki.jpg)

## 局限性

使用此技巧存在一些限制，例如需要支撑和多色打印的模型会比较棘手。

### 需要支撑的模型

对于需要在“仅限左喷嘴”或“仅限右喷嘴”两个受限区域内添加支撑的模型，难度会更大。生成的支撑不受切割的影响，而且 Bambu Studio 不支持为支撑的具体部分指定喷嘴或耗材。所有支撑都遵循相同的参数，受限区域内的支撑也是。  
但这并不妨碍您将此方法用于需要支撑的模型。然而，如果模型同时在“仅限左喷嘴”和“仅限右喷嘴”区域使用了支撑，则无法使用此方法打印。  
如果模型仅在共享的“双喷嘴”区域或仅在单个受限区域内使用支撑，则仍然可以应用此技巧并成功完成打印。

![warn1cn.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/warn1cn.png)

模型为：[DjangoCashflow 的 Cyberbrick RC 维斯比级](https://makerworld.com/zh/models/1902310-cyberbrick-rc-visby-class-maker-s-supply-only#profileId-2038970)

### 多色打印的模型

使用这种方法打印多色模型会非常困难。除非每个喷嘴都由独立的 AMS 供料，否则无法在两个受限区域内使用同一种耗材。这意味着至少需要两个 AMS 以及两卷同样的耗材。在这种设置下，您需要将匹配的耗材和颜色分别装入对应的 AMS，然后认真调节切割面和颜色分配。

虽然这种技巧能够实现大模型的多色打印，但仍存在一定局限：需要准确的规划与准备，并且设置过程比较复杂。

![warn2cn.png](https://wiki.bambulab.com/h2/how-to-print-350mm-models/warn2cn.png)

模型为：[pbbence1994 的 F-35 闪电II型战斗机套卡](https://makerworld.com/zh/models/970150-f-35-lightning-ii-plane-kit-card#profileId-1073810)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
