---
path: zh/software/bambu-studio/reduce-wasting-during-filament-change
title: "减少多色打印时的材料浪费"
description: ""
tags: []
created: 2023-08-14T11:01:20.275Z
updated: 2025-11-24T10:56:53.400Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/reduce-wasting-during-filament-change
---

多色或多材料打印往往要消耗很高的时间和材料成本，本文将帮助您理解消耗的原因，并提供减少浪费的方法。

## 换料过程

根据定义，多材料打印（也称为多色打印）需要使用多种耗材来完成一个打印。尤其是在单喷嘴打印机上，这是通过**换料**来实现的，该过程可以分为几个关键阶段。

### 冲料

每次喷嘴从一种耗材切换到另一种耗材时，都会有少量旧耗材残留在挤出机和喷嘴中，位于切刀切断位置以下。当 AMS 回收旧耗材并送入新耗材时，挤出机会将旧耗材推挤出来，直到喷嘴中完全挤出新的耗材为止。

这些被排出的耗材会在打印平台旁的区域挤出，并从喷嘴脱落。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/filament_purges.jpg)

> **注意**：这些耗材会以最快的速度（最大体积速度）被挤出，在多色打印中可能需要重复执行很多次。最大体积速度取决于多个因素，主要是耗材在熔融状态下的流动性，而喷嘴直径是其中最重要的因素之一。  
> 因此，0.2 mm 喷嘴的冲刷步骤可能会比标准的 0.4 mm 喷嘴耗时明显更长，从而换料时间和整体打印时间也会显著增加。

### 冲刷体积

在换色打印时，需要先挤出一部分材料来把喷嘴里的旧耗材清掉，这部分就是“冲刷体积”。决定冲刷体积大小的主要因素是**耗材颜色**——因为哪怕残留一点旧颜色，也可能在打印层上留下明显的色差。

**深色 → 浅色：需要冲刷得更多，才能保证没有混色。**

**浅色 → 深色：需要的冲刷量相对更少。**

在 Bambu Studio 里，有一个表格会自动显示项目中不同颜色切换时所需的冲刷体积。具体怎么看、怎么调整这些数值，会在“管理冲刷体积”部分介绍。

![flushing_volumes_chart_2.png](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/flushing_volumes_chart_2.png)

除了颜色，材料特性也会影响冲刷体积。例如在支撑耗材中，为了避免支撑材料和被支撑材料之间发生粘连，冲刷体积会被计算得更高，以防止污染。

### 擦拭

在冲料完成后，喷嘴会在擦拭器上来回移动，确保被冲刷出来的耗材完全脱离喷嘴。这也是对喷嘴尖端进行的第一次清洁，避免旧耗材残留污染模型。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/a1_series_nozzle_wiper.png)

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/xp_series_nozzle_wiper.png)

### 准备挤出

在擦拭完成后，喷嘴会在**擦拭塔**上挤出耗材，擦拭塔可以用来清理喷嘴上的残留料，并让喷嘴内部的腔压达到稳定状态，确保喷嘴流动一致，这样继续打印的时候就可以避免打印模型表面出现外观瑕疵。

![擦拭塔.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E6%93%A6%E6%8B%AD%E5%A1%94.jpg)

擦拭塔可能在整个打印过程中都需要存在，因此必须达到打印中涉及换料的最高层高度。

通常擦拭塔的耗材量少于冲刷排料，因为它的打印方式更高效，类似于支撑。

> **注意**：由于擦拭塔必须达到涉及换料的最高层，因此在仅顶部换色的打印中，会浪费干净的耗材来为塔体打底。相反，如果换色仅发生在底部，擦拭塔则会在早期完成并停止。

例如，下图中的擦拭塔使用了 15.15 g 耗材。

![weird_cube.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/weird_cube.jpg)

而在下一个示例中，只需将同一个零件沿z轴镜像旋转 180°（使换色集中在底部），擦拭塔耗材量就减少到 5.92g。

![颠倒.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E9%A2%A0%E5%80%92.jpg)

![weird_cube2.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/weird_cube2.jpg)

---

## 减少耗材浪费的方法

有几种方法可以在不改变最终打印零件的情况下减少耗材浪费。这些方法各有优缺点和适用条件，下面分别介绍。

### 管理冲刷体积

Bambu Studio 会在换料时 **自动计算所需的冲刷体积**。主要参考因素是颜色和材料特性。

要查看和管理项目的冲刷体积，可在 **项目耗材列表**点击 **冲刷体积** 按钮。

![耗材列表.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E8%80%97%E6%9D%90%E5%88%97%E8%A1%A8.jpg)

在全局范围内，可以通过“**乘数**”调整冲刷体积。默认值为 1.00，若改为 0.90，表示所有换料对的冲刷体积减少 10%。

![乘数.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E4%B9%98%E6%95%B0.jpg)

尝试降低乘数可以节省耗材，因为默认值通常会稍高以保证打印质量。0.8 或 0.9 的倍数可能是不错的折中方案，但务必要通过测试打印确认不会影响颜色或物理性能。

如果乘数过低，可能会出现颜色层污染，如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/insufficient_flushing_layer_bleed.png)

此外，你还可以在表格中逐一手动调整某些耗材对的冲刷体积。如果之后需要恢复默认，只需点击 “**重新计算**” 按钮即可。

### **冲刷到模型填充**

模型的填充部分通常被外壳覆盖。因此，在很多情况下，可以启用 **冲刷到对象的填充** 功能，将原本要浪费掉的冲刷耗材用于打印填充部分。

![冲刷到对象的填充.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%86%B2%E5%88%B7%E5%88%B0%E5%AF%B9%E8%B1%A1%E7%9A%84%E5%A1%AB%E5%85%85.jpg)

不过要谨慎使用：某些浅色或透明耗材可能会透色，导致填充的杂色在外表可见。外壁层数少的模型更容易出现这种问题。

例如下图，尽管使用了深绿色且只有 1 层外壁，仍然能隐约看到填充颜色透出。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/flush_into_objects_infill_abberation.png)

### **冲刷到对象的支撑（默认启用）**

由于支撑部分会在打印后被移除，因此可以使用这部分来冲刷耗材。对于支撑面积大的模型，启用该功能可以大大减少浪费并缩短打印时间。

![冲刷到对象的支撑.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%86%B2%E5%88%B7%E5%88%B0%E5%AF%B9%E8%B1%A1%E7%9A%84%E6%94%AF%E6%92%91.jpg)

缺点是，支撑部分通常不足以显著降低浪费。但因为没有副作用，所以该功能默认启用。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/flush_into_support_visual.png)

个别情况下，若使用不同性能的耗材，可能会轻微影响支撑强度。但这种情况一般不明显。

> **注意**：必须启用擦拭塔，该功能才会生效。

### **冲刷到指定模型**

此功能只有在 **同时打印大于一个模型** 时才可用。启用后，该模型会被用来接收冲刷耗材，打印出来会带有渐变或杂色效果。

![多个冲刷.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%A4%9A%E4%B8%AA%E5%86%B2%E5%88%B7.jpg)

这种方式推荐用于对外观颜色一致性要求不高的模型，比如功能件或后续要上色的零件。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/flush_into_object_visual.jpg)

通过在同一打印板上放置多个启用“冲刷到此模型”的物件，可以最大限度利用冲刷耗材。例如：

在下图中，单独打印一个彩色 Bambu Cube 需要约 70g 冲刷耗材。但通过添加多个“冲刷对象”，浪费量减少到不到 1g。

![冲刷量.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%86%B2%E5%88%B7%E9%87%8F.jpg)

要注意：如果冲刷对象比主模型更高，它们剩余高度会用新耗材打印，所以最好保持高度接近。

## 减少换料次数

如上所述，打印过程中“浪费”的耗材主要来源于每次换料时进行的冲刷和清理步骤。因此，打印过程中耗材浪费的多少，直接取决于**换料次数**（即执行换料流程的次数）。

![换料次数.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E6%8D%A2%E6%96%99%E6%AC%A1%E6%95%B0.jpg)

### 每层的换料次数

在一次打印中，不同的层可能会有不同的换料次数，这取决于该层所使用的耗材数量。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/filament_changes_1_layer.png)

在绝大多数情况下，单层的换料次数比该层所用耗材数少 1。  
这是因为最后一种耗材会直接延续到下一层，从而避免一次不必要的换料。  
当然，单层最少可能的换料次数为 **0**，这种情况发生在整层完全由同一种耗材组成时。

以下图所示的层为例，它包含三种颜色：红色、绿色和黄色。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/bambu_cube_example_layer_filament_changes.gif)

可以看到，这一层先用红色开始，然后进行一次换料（喷嘴暂时消失）切换到绿色，再进行第二次换料切回黄色。完成该层后，打印机会直接继续用黄色打印下一层，而无需再次换料。

### 总层数

由于层数会直接影响换料次数，因此减少层数可以有效减少耗材浪费。最简单的方法就是**增加层高**。

以四色 Bambu Cube 为例：当层高为 0.2mm 时，总共发生 153 次换料，浪费 83 克耗材。

![层高1.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%B1%82%E9%AB%981.jpg)

若将层高提高到 0.28mm，则换料次数降至 111（减少 27%），耗材浪费降至 61 克（减少 26%）。可以看出，换料次数的减少与耗材浪费的减少呈直接相关。

![层高2.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%B1%82%E9%AB%982.jpg)

另一种方法是将高而细的零件横放打印，而不是竖直打印。不过这种方式是否可行取决于零件本身的特性，尤其是理想的层方向（强度或美观）。

下例中，零件横放打印后，换料次数和耗材浪费减少了约 80%，打印时间减少了 70%。对于一个 35g 的零件，节省了 11 小时和将近 180g 耗材！

![条形1.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E6%9D%A1%E5%BD%A21.jpg)

![条形2.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E6%9D%A1%E5%BD%A22.jpg)

> **注意**：横放零件并不总是能节省耗材。这完全取决于零件本身的特征，特别是颜色/耗材的分布方向。  
> 此外，如果零件没有平整的一面可以放置在打印平台上，则可能需要更多的支撑耗材，这可能会抵消甚至超过因减少换料而节省的耗材。  
> 因此，建议始终在 Bambu Studio 中尝试不同的摆放方式，并对比切片结果中的耗材用量。

例如，下图展示的零件如果横放打印就是非常糟糕的情况，因为不同颜色已经按层水平分布。竖直打印时几乎无需换料，总共只发生 3 次换料，浪费 10g 耗材。

![四色1.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%9B%9B%E8%89%B21.jpg)

但如果横放打印，每一层都有四种颜色，需要三次换料。结果是耗材浪费增加 **22 倍**，打印时间延长 **11 倍**！

![四色2.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%9B%9B%E8%89%B22.jpg)

## 设置不同层耗材打印顺序

在多色（多材料）打印任务中，我们可以自定义不同层的耗材打印顺序，包括指定首层和其他层打印顺序。

**在Bambu studio的准备页面，点击打印板旁的设置图标，在弹出的“盘参数设置”窗口即可设置首层和其它层耗材的打印顺序。**  
![盘参数设置.png](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E7%9B%98%E5%8F%82%E6%95%B0%E8%AE%BE%E7%BD%AE.png)

### 首层耗材打印顺序

**首层耗材打印顺序分为自动和自定义两种.**

#### 自动

自动分配首层打印的耗材丝顺序，分配顺序的逻辑如下：

比较每个颜色区域的最小的独立轮廓，按照最小轮廓从大到小的顺序打印。如下所示，绿色部分的最小轮廓 > 橙色部分最小轮廓，所以先打绿色部分。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E6%AF%94%E8%BE%83%E6%AF%8F%E4%B8%AA%E9%A2%9C%E8%89%B2%E5%8C%BA%E5%9F%9F%E7%9A%84%E6%9C%80%E5%B0%8F%E7%8B%AC%E7%AB%8B%E8%BD%AE%E5%BB%93.gif)

如果不同颜色的独立轮廓面积都一样，将会按照耗材丝列表里的先后顺序打印。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E8%80%97%E6%9D%90%E4%B8%9D%E5%88%97%E8%A1%A8.png)

#### 自定义

在下拉列表里选择“自定义”，并拖动各颜色方块来自定义首层的打印顺序。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E8%87%AA%E5%AE%9A%E4%B9%89%E9%A6%96%E5%B1%82%E6%89%93%E5%8D%B0%E9%A1%BA%E5%BA%8F.gif)

### **其它层耗材打印顺序**

其它层定义的是除首层之外的所有层的打印顺序。用户可以指定具体的层高范围来自定义其打印顺序。它也有自动和自定义两种方式：

#### 自动

尽可能让下一层打印的第一个材料 = 前一层打印的最后一个材料。如下动图所示，上一层打印的最后一个材料是红色耗材丝，那么下一层将会从红色耗材丝开始打印，尽量减少换料次数：

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E4%B8%8B%E4%B8%80%E5%B1%82%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E9%A2%9C%E8%89%B2%E7%AD%89%E4%BA%8E%E4%B8%8A%E4%B8%80%E5%B1%82%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E9%A2%9C%E8%89%B2.gif)

尽可能采用这一层的冲刷量最小的材料顺序。例如，比如耗材丝顺序 1->2->3 的总冲刷量大于 1->3->2 的总冲刷量，就会使用后者作为该层的打印顺序。

#### 自定义

用户可以自定义需要修改的层高范围，默认是从第二层到最后一层（end）。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E8%87%AA%E5%AE%9A%E4%B9%89%E7%AC%AC%E4%BA%8C%E5%B1%82%E5%88%B0%E6%9C%80%E5%90%8E%E4%B8%80%E5%B1%82.png)

也可以增加自定义层高范围区间，比如下图设置了3个层高区间，每个层高区间可以独立设置打印顺序

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B1%82%E9%AB%98%E5%8C%BA%E9%97%B41.png)

如果两个层高区间有重叠部分，则重叠区间的打印顺序，优先使用排序**靠后**的区间打印顺序，如下图，两个区间分别是[2-10]，[5-End]。实际上将会把它拆分为[2-4]和[5-End]两个区间来定义打印耗材顺序。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%8C%BA%E9%97%B4%E9%87%8D%E5%8F%A0.png)

如果自定义的层高区间**没有**包含打印对象的所有层高，则剩余的层高将采用“自动”的逻辑来分配耗材打印顺序。如下图，设定了[2-10]层高区间的打印顺序，而模型的层高不止10层，则[11-End]的层高区间将自动分配打印顺序。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E5%B1%82%E9%AB%98%E5%8C%BA%E9%97%B4%E5%8F%AA%E8%AE%BE%E7%BD%AE%E4%B8%80%E9%83%A8%E5%88%861.png)

我们可以通过拖拽图中的颜色方块来定义其它层打印顺序。切片后预览可以看到，中间任何一层都采用了自定义的耗材顺序打印。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%85%B6%E5%AE%83%E5%B1%82%E6%89%93%E5%8D%B0%E9%A1%BA%E5%BA%8F.gif)

## 同时打印多个零件

当一层中增加相同耗材时并不会增加换料次数，因此在一次打印中**增加更多使用相同耗材的对象**，可以有效摊薄每个零件的耗材浪费。  
最简单的方式就是一次性打印多个**相同模型**。

### 相同着色的相同模型

为了最大化利用换料带来的“浪费”，应尽可能在一次打印中放置多个相同模型。当然，这仅适用于需要打印多个相同模型的情况。

之前的 Bambu Cube 例子，在 0.2 mm 层高下，单个打印需要 153 次换料，浪费 83 克耗材，而零件本身只有 11 克，效率极低。  
如果我们复制九个相同方块放在一个打印任务中，换料次数和浪费耗材保持不变，但却额外得到 8 个完成品。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/multiple_identical_multicolor.png)

### 共享部分颜色的不同模型

非相同模型但满足以下条件：

- 至少共享一种材料
- 如果单独打印会产生一定的浪费

将共享部分颜色的不同模型放在同一打印平台上，带来的耗材节省可能极小（甚至为负），也可能非常显著。其核心原则是：**每层共享的耗材越多，收益越大**。

### 相同颜色的不同零件

如下例所示，多个零件共享相同的一组颜色。与分开打印相比，同时在一个平台上打印时，浪费显著减少。

如果分开打印：两个 Bambu Cube 在一个平台，刮刀组件三件套在另一个，总共浪费 171 克耗材。  
若全部放在同一个平台，总浪费减少 23%，为 133 克。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/multiple_similar_multicolor.png)

### 仅共享一种颜色的零件

下例中，两个零件组仅共享一种颜色（绿色），而且绿色是主要基色。由于每层都可能受益于共享的绿色，因此节省效果依然不错。

如果分开打印，总浪费为 144 克；若放在同一个平台，总浪费减少 18%，为 118 克。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/multiple_barely_similar.png)

### 相同颜色但配色不兼容的零件

从以上例子来看，很容易误解为“共享耗材越多，浪费越少”。实际上更准确的总结是：**每层共享的耗材越多，浪费才会越少**。

例如，三个不同的交通锥，它们都使用橙、白、黑三种颜色。理论上看似可以放在一起打印节省浪费，但实际结果却相反。

![交通桶.jpg](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/%E4%BA%A4%E9%80%9A%E6%A1%B6.jpg)

因为这些交通锥采用水平条纹，单独打印时效率已经很高。若放在一起打印，由于条纹高度不一致，反而增加了额外的换料次数。

单独打印时，总浪费 22 克，仅 16 次换料。  
放在一起打印时，浪费变为 72 克，增加了三倍以上！  
这说明决定耗材浪费的根本因素是**每层的换料次数**，而不是整体共享耗材的数量。

> **提醒**：综上所述，在比较多材料零件的不同排布方式时，建议始终在 Bambu Studio 中进行切片并对比总耗材用量。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
