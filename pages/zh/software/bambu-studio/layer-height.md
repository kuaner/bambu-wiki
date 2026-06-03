---
path: zh/software/bambu-studio/layer-height
title: "层高设置"
description: ""
tags: []
created: 2023-12-07T12:27:08.829Z
updated: 2024-05-28T11:04:46.896Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/layer-height
---

# 层高定义

层高指的是FDM 3D打印模型中每层的高度，在打印过程中是模型是层层堆叠成型的，通常我们也把层高视作模型的垂直分辨率，即层高越低，模型的精细度也就越高。

在Bambu Studio中，您可以在**工艺——质量——层高**中设置层高参数。

![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/设置层高.png)

您也可以在工艺中直接选择不同的层高预设，Bambu Studio针对Bambu系列打印机不同口径的喷嘴都有配置好的层高预设可供选择：

![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/选择层高预设.png)

**首层层高即打印首层的高度，也就是喷嘴和打印面板之间的高度。**合适的首层层高能够确保打印首层的粘附性，使其具有更好的首层质量，从而提升整个模型的打印成功率。在Bambu Studio系统配置里针对不同直径喷嘴的各种层高预设，都预设了一个固定的首层层高，即**首层层高=喷嘴直径\*50%**。例如0.4mm喷嘴默认首层高度0.2mm。

![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/打印首层示意图.png)

**打印首层示意图**

# 层高的影响

层高影响的是模型表面的精细度以及打印的时间。层高越低，模型表面的层间纹路就越不明显，但打印时间就会相对更长一些。因为模型高度不变的情况下，单层的层高越低，所需要的层数就越多，打印的时间就越长。下面是打印模型 [Glowing Ghosts](https://makerworld.com/zh/models/14307#profileId-14545) (来自 JamesThePrinter)的示例：

|  |  |  |
| --- | --- | --- |
| **0.08mm层高，打印时间1h 19m** | **0.2mm层高，打印时间36m 14s** | **0.28mm层高，打印时间28m 27s** |
|  |  |  |

# 层高的设置范围

在3D打印中，只有在合理的高度范围内设置层高值，才能获得较好的打印质量，层高太高或太低都有可能导致打印质量问题。**通常来说，合理的层高范围应该是喷嘴直径的20%~70%。也就是说，0.4mm直径的喷嘴，合适的打印层高在0.08mm~0.28mm之间。**在**打印机设置——挤出机**中，你也可以看到对当前使用喷嘴的打印层高范围限制：

![](https://wiki.bambulab.com/software/bambu-studio/adaptive-layer-height/层高范围限制.png)

**层高范围限制**

层高较高的时候，挤出的流量比较大，若需要充分熔融挤出耗材，需要较慢的打印速度。在Bambu Studio的不同层高预设中，也配置了不同的默认打印速度，如下所示：

|  |  |  |
| --- | --- | --- |
| **0.08mm 层高预设** | **0.20mm 层高预设** | **0.28mm 层高预设** |
|  |  |  |

# 层数的取整逻辑

当模型的高度无法被层高所整除，这种情况下，切片时会采用取整算法来确认打印所需要的层数。Bambu Studio切片3D模型也是逐层切片的，当切片到最顶层时，**它根据最顶层走线的中心Z高度对比模型实际高度的决定是向上取整还是向下取整。当模型高度 > 最顶层走线中心高度，则该顶层存在。如果模型高度 ≤ 模型最顶层走线中心高度，则该层不存在，取上一层为模型的最顶层。**

以下是一个实例，打印层高0.2mm，模型高度分别为0.5mm和0.51mm的切片结果。

当模型高度为0.5mm时，前两层打完高度是0.4mm，第3层的中心Z高度是0.5mm（0.2+0.2+0.1），等于模型高度0.5mm，所以第3层不存在，切片后只有2层。

![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/模型0.5mm.png)
![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/切片后2层.png)

当模型高度是0.51mm时，第3层的中心Z高度0.5mm < 模型高度0.51mm，所以第3层存在，切片后会有3层。

![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/模型0.51mm.png)
![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/切片后3层.png)

# 精准Z高度

在上述的层数取整过程中，由于层高是固定的，所以层高无法被模型高度整除时，切片后的模型可能会和模型实际高度有误差。在Bambu Studio 1.9版本引入了**精准Z高度**功能，可以在切片后获得精确的模型高度。**该功能的逻辑是微调最后5层的层高，让最终的层高和实际值一样。**

下面是一个例子，一个高度2mm的立方体，层高预设是0.24mm，首层层高是0.2mm。未启用精准Z高度时，按照上面的层数取整算法，最终切片出来的高度是0.2+0.24\*7=1.88mm，共8层。

![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/开启精准z高度.jpg)

开启精准Z高度后，平均增加了最后五层的层高，使得最后切片出来的对象高度和预期高度一致，都是2mm。

![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/开启精准z高度.png)

**注意：当模型对象的层数小于 6 层时，该功能不会生效。而且如果微调最后5层层高时，如果需要它们超出层高限制切片后才能达到预期的模型高度，则该功能也不生效。**

# 可变层高

如上所述，低层高打印出来的模型表面更精细，但所需要的打印时间更长。对于某些模型，我们只想要给局部设置较低的层高，而其他地方保持默认的层高即可。这时候您可以用可变层高功能，给模型的不同部分设置不同的层高。这样既可以保证打印的质量，又尽可能地节省打印时间。具体可以参考wiki：[可变层高 | Bambu Lab Wiki](adaptive-layer-height.md)

![](https://wiki.bambulab.com/bambu-studio/parameter/layer-height/可变层高预览.png)
