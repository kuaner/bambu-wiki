---
path: zh/software/bambu-studio/parameter/quality-advance-settings
title: "Bambu Studio 质量高级设置"
description: "介绍 Bambu Studio 中质量相关的高级参数的作用"
tags: ["bambu studio", "打印质量"]
created: 2024-08-22T13:07:43.829Z
updated: 2026-06-01T07:29:39.429Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/quality-advance-settings
---

在 Bambu Studio中，您可以**工艺——质量——高级**中对质量相关的参数一些高级设置。**（注：部分参数需要在偏好设置中启用“开发者选项”后才会显示）**

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E8%B4%A8%E9%87%8F%E2%80%94%E9%AB%98%E7%BA%A7%E8%AE%BE%E7%BD%AE1.png)

## 墙顺序

用于调整模型墙的打印顺序，目前有三个选项，分别是**内墙/外墙、外墙/内墙和内墙/外墙/内墙。**

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E5%A2%99%E9%A1%BA%E5%BA%8F.png)

### 内墙/外墙

先打印最里面一圈的内墙，从内到外，最后打印外墙，该顺序也是默认的打印顺序，如下图所示。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E5%86%85%E5%A2%99%E5%A4%96%E5%A2%99.gif)

**若模型有悬垂部分，使用该顺序打印效果会更好。因为在打印到悬垂部分时，外墙的一侧有先前打印完的内墙，可以确保悬垂部分的粘附，减少悬垂部分翘曲或者塌陷带来的外观瑕疵，具体区别如下图所示。**

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E6%82%AC%E5%9E%82%E5%86%85%E5%A2%99%E5%A4%96%E5%A2%99.png)

采用**外墙/内墙**或**内墙/外墙/内墙**顺序打印，外墙（蓝色线）完全悬空且两侧都是空的，缺少粘附，悬垂质量较差。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E6%82%AC%E5%9E%82%E5%A4%96%E5%A2%99%E5%86%85%E5%A2%99.png)

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E6%82%AC%E5%9E%82%E5%86%85%E5%A2%99%E5%A4%96%E5%A2%99%E5%86%85%E5%A2%99.png)

### 外墙/内墙

先打印最外层的外墙，然后由外到内打印其余的内墙。**使用该顺序打印时，模型表面的接缝可能会相对比较明显。不过先打印外墙，外墙能够先冷却凝固，可以减弱内部线条挤压或者收缩给表面带来的瑕疵、层纹。**

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E5%A4%96%E5%A2%99%E5%86%85%E5%A2%99.gif)

### 内墙/外墙/内墙

先从最里面的内墙打起，由内向外，打印完倒数第二个内墙后，开始打印外墙，最后再打印和外墙相邻的内墙，如下图所示。

**使用该顺序打印，外墙和其他先打印完的内墙中间有一层空的部分，减弱了内墙收缩的影响，而且其他先打印完的内墙也已经先凝固冷却一段时间了，所以能够最大程度避免内部挤压或者收缩影响到外墙从而影响模型外观。**

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E5%86%85%E5%A2%99%E5%A4%96%E5%A2%99%E5%86%85%E5%A2%99.gif)

## 首先打印填充

将会首先打印填充部分，再打印内外墙。**这里的“填充”指的是所有水平方向的壳体，包括稀疏填充/内部实心填充/顶面/底面/桥接。**

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E9%A6%96%E5%85%88%E6%89%93%E5%8D%B0%E5%A1%AB%E5%85%85.gif)

## 桥接流量和厚桥

在原有的桥接流量上，乘以这里设置的比例系数，作为桥接的流量。具体可以参考：[如何在 Bambu Studio 中提升桥接质量 | Bambu Lab Wiki](../../../filament-acc/filament/print-quality/bridging.md)

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E6%A1%A5%E6%8E%A5%E6%B5%81%E9%87%8F.gif)

## 顶部表面流量比例

在原有的流量比例基础上，乘以这个系数，作为顶部表面的流量比例。这个系数会影响着顶部实心填充的材料用量。

## 首层流量比

在原有的流量比例基础上，乘以这个系数，作为首层的流量比例。这个系数会影响着首层的材料用量。

## 顶面单层墙

启用该选项后，所有顶面始终都只有1层墙。该选项默认开启，开启该选项可以使顶部表面的效果更好，尤其是针对顶部平滑的模型。若选择不勾选，则顶面的墙层数与在**强度——墙**中设置的墙层数一致。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E9%A1%B6%E9%9D%A2%E5%8D%95%E5%B1%82%E5%A2%99.gif)

该选项可以作用于顶面和最顶面。顶面指的是模型的所有顶面，最顶面指的是对象最高的那个顶面，具体如下图所示。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E9%A1%B6%E9%9D%A2%E5%8D%95%E5%B1%82%E5%A2%99%E9%80%89%E9%A1%B9.png)

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E4%BB%85%E6%9C%80%E9%A1%B6%E9%9D%A2%E5%BC%80%E5%90%AF%E5%8D%95%E5%B1%82%E5%A2%99.png)

## 顶部区域阈值

开启**顶面单层墙**后可配置此参数。这个参数影响形成顶面单层墙区域的面积阈值。如果顶面的一部分被更上层给覆盖了（例如球形顶部），那么当该层顶面的宽度小于这个阈值时，它不会被认为是顶层。

这个设置可以用于避免在狭窄顶面 （通常非最顶面）触发**顶面单层墙**。这个值代表着线宽的百分比。放大这个值之后，比较小的顶面区域会被筛掉，仍然按照设置的墙层数来生成。但是，此选项对最顶面不生效。

\*\*调整该参数可以使得打印一些带有弧形或者坡度表面模型时表面过渡更加平滑，\*\*具体作用效果如下图所示。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E9%A1%B6%E9%83%A8%E5%8C%BA%E5%9F%9F%E9%98%88%E5%80%BC1.gif)

|  |  |
| --- | --- |
| **默认顶部区域阈值** | **放大顶部区域阈值** |
|  |  |

## 识别悬空外墙

可以检测出墙的悬垂度，并应用不同的速度打印，100% 悬空的悬空墙将使用桥接速度，具体可以参考：[悬垂降速](../slow-down-for-overhang.md)。

若关闭此选项，内外墙将会使用速度设置中的内外墙速度进行打印。具体区别如下：

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E8%AF%86%E5%88%AB%E6%82%AC%E7%A9%BA%E5%A4%96%E5%A2%99.gif)

## 平滑速度不连续区域

Bambu Studio 1.9.4版本引入了平滑速度的选项。悬垂和非悬垂区域通常速度变化较大，启用此选项能够让速度过渡更平滑一些，以提高冷却效果。该选项默认开启。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E5%BC%80%E5%85%B3%E5%B9%B3%E6%BB%91%E9%80%9F%E5%BA%A6%E4%B8%8D%E8%BF%9E%E7%BB%AD%E5%8C%BA%E5%9F%9F.gif)

## 平滑系数

用于控制平滑过渡路径的长度，该值越小，速度过渡的区域越长，也就意味着速度过渡更加平滑。适当调整平滑系数可以使得悬垂区域的打印质量更好，通常建议在1~200范围内设置。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E4%BF%AE%E6%94%B9%E5%B9%B3%E6%BB%91%E7%B3%BB%E6%95%B0%E5%AF%B9%E6%AF%94.gif)

## 避免跨越外墙

启用这个选项，可以尽可能在打印空驶的时候避免跨越外墙，可以减少在**单个对象**的**单层打印**中跨越外墙时漏料形成拉丝的现象。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E9%81%BF%E5%85%8D%E8%B7%A8%E8%B6%8A%E5%A4%96%E5%A2%99.png)

避免跨越外墙——最大绕行长度：当绕行距离比这个数值大时，此次空驶不绕行。

**绕行距离可表达为绝对值，或者相对直线空驶长度的百分比（输入 50 就是 50mm，输入 50% 代表的是百分比）。该数字代表的是绕行相较于普通空驶增加的长度，如果超过了阈值就放弃绕行，仍按照原始路径进行直线空驶。**

\*\*最大绕行长度为默认是 0，代表不限制绕行的长度，将执行所有绕行。\*\*空驶绕行的路径将沿着该层的轮廓，不过只有当起点和终点都在墙内或者墙外，才会进行绕行。若起点和终点一个在墙外，一个在墙内，则无法采取绕行。

具体效果如下图所示，可以看出启用该选项后能大大减少外墙之间的空驶。

![](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/%E9%81%BF%E5%85%8D%E8%B7%A8%E8%B6%8A%E5%A4%96%E5%A2%99.gif)

## 平滑 Z 方向外墙速度

开启后，Bmabu Studio 会尝试对连续对相邻层的外墙速度进行平滑，这有利于模型光滑曲面较多的模型获得更好的效果。注意，该功能开启后会增加打印时间，并且在花瓶模式中不生效。

![smoothing_wall_speed_along_z_cn.png](https://wiki.bambulab.com/bambu-studio/parameter/quality-advance-settings/smoothing_wall_speed_along_z_cn.png)

**✅ 推荐启用的场景：**

- **高表面质量要求的模型**：如摆件、手办、外观件等，这类模型外壁较高且光滑曲面较多。
- **存在速度带 / 光泽不一致 / 阴影条纹的模型**：典型表现是模型某几层突然变亮或变暗，出现横向亮带。通常由层冷却触发的局部降速所致。
- **顶部小截面 + 下部大截面的模型**：顶部容易因层时间过短被降速。
- **具有连续外墙柱的模型**：如柱子、瓶身（非旋转花瓶模式）、人物腿部、长条结构等。
- **使用 PLA Silk、亮面或半透明耗材时**：这类耗材对速度变化极为敏感，由此产生的瑕疵在模型表面上尤为显眼。

**❌不推荐 / 无须开启的场景：**

- **旋转花瓶模式**：在旋转花瓶模式下，该功能不会生效。
- **追求打印速度的模型**：因为开启该功能后打印速度会降低，所以若对打印速度有更快的要求，则无需开启。
- **Z 方向外墙不连续的模型**：如外墙频繁在 Z 方向上中端、由众多独立小柱体堆叠、含大量镂空变化层结构的模型，平滑效果有限。
- **外墙速度本身就稳定的模型**：如标准方块、统一截面的简单几何体，无明显速度突变。
- **细小模型**：外墙面积小，肉眼几乎无法察觉差异，收益有限。
- **打样调参 / 频繁切片迭代时**：启用该功能后切片耗时会增加，影响调试效率。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
