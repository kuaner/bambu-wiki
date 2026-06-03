---
path: zh/software/bambu-studio/use-disc-to-avoid-warping
title: "小圆片的使用技巧——防止翘曲"
description: ""
tags: []
created: 2024-02-06T04:27:31.180Z
updated: 2025-01-20T08:13:35.188Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/use-disc-to-avoid-warping
---

## 前言

在3D 打印过程中，通常由于材料的**局部收缩或者与打印板的粘接力不足，打印模型会出现翘边的现象，尤其是在打印 ABS 或 ASA 等易收缩的材料时。**通常你可以在Bambu Studio中添加[Brim](auto-brim.md)或者增加热床温度，来增强模型首层的粘接（详情参考 wiki：[模型翘边、脱落或倒塌 | Bambu Lab Wiki](../../filament-acc/filament/print-quality/warping-falling-off-collapsing.md)）。不过有些情况下拆除 Brim 可能会比较麻烦，且不能完全改善翘曲问题。因此，我们还推荐您在 Bambu Studio 中，巧妙地在模型局部添加小圆片，可以帮你改善打印过程中模型翘边的问题，而且模型的后处理也更加方便。

![](https://wiki.bambulab.com/bambu-studio/toolbar/disc-to-avoid-warping/studio立方体添加圆片.png)

## 操作步骤

- 这里我们用立方体模型作为示意。首先在Bambu Studio里，右键点击打印板上的立方体，选择添加“小圆片”，然后把它调整至合适的大小：

![](https://wiki.bambulab.com/bambu-studio/toolbar/disc-to-avoid-warping/添加小圆片.gif)

- 选中小圆片，用快捷键Ctrl+C和Ctrl+V把它复制到所需要的个数，分别挪动到模型易翘边的边角上，如下动图所示：

![](https://wiki.bambulab.com/bambu-studio/toolbar/disc-to-avoid-warping/复制小圆片到所需个数.gif)

- 点击切片后你会发现，此时小圆片和立方体已经完全融为一体了，这也改变了原本模型的形状，我们还需要一些设置把小圆片和立方体分离出来，方便拆卸。如果小圆片和立方体未融为一体，可能是因为小圆片未作为立方体的部件添加，只需将立方体和小圆片组合后重新切片即可。

![](https://wiki.bambulab.com/bambu-studio/toolbar/disc-to-avoid-warping/切片后圆片立方体融为一体1.gif)

- 我们还需要在对象列表里，把小圆片或者立方体的某个参数修改一下来作分隔。例如：把所有小圆片设置成3层墙，而立方体仍保持默认的2层墙。因为此时小圆片和立方体属于同一个对象，同一个对象的不同零件，如果参数完全相同，就会按照一个整体来切片。如果零件之间的墙层数不同，会生成独立的墙走线分隔开来。切片后的效果如下：

![](https://wiki.bambulab.com/bambu-studio/toolbar/disc-to-avoid-warping/修改参数区分零件.gif)

- 此时小圆片和立方体已经区分出来，但是切片后重叠部分保留的是小圆片部分而不是立方体部分。您可以在对象列表里，把立方体拖动到列表中的最后，这样切片时，立方体与圆片的重叠部分会保留立方体的部分。**因为在对象列表中，同一个对象的多个零件，在零件列表里排在越下面，优先级越高，若有重叠部分将保留优先级高的部分：**

![](https://wiki.bambulab.com/bambu-studio/toolbar/disc-to-avoid-warping/拖动立方体至最高优先级.gif)

- 有些机型的预设中，象脚补偿默认值不为0（例如X1C的预设值是0.15），按照上述方法切片后，由于象脚补偿带来的收缩，立方体与圆片的交界处相比旁边会凸出来一点。您可以把象脚补偿设为0后再次切片，操作如下图所示。关于象脚补偿的详细介绍可以参考wiki：[象脚补偿 | Bambu Lab Wiki](parameter/elephant-foot.md)。

![](https://wiki.bambulab.com/bambu-studio/toolbar/disc-to-avoid-warping/象脚补偿设为0.gif)

按照上述方法，你可以在易翘边的模型局部添加小圆片进行切片并打印，能有效防止模型翘曲的问题。

![](https://wiki.bambulab.com/bambu-studio/toolbar/disc-to-avoid-warping/打印示意图.png)
