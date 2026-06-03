---
path: zh/knowledge-sharing/flowrate-calibration-by-microlidar
title: "自动流量比例校准注意事项"
description: ""
tags: ["自动流量"]
created: 2023-08-01T09:47:12.851Z
updated: 2024-06-18T08:17:55.920Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/flowrate-calibration-by-microlidar
---

**注意:**  
这个功能目前还在持续优化中，可能会产生不准确的结果。只推荐给有经验的用户使用。在使用校准设置时，请谨慎操作，因为错误的流量设置可能会损坏你的打印机，包括可能引发喷嘴堵塞或挤出堵塞。

---

# 为什么需要校准流量？

FDM 3D打印利用热量将材料融合成组件。然而，由于热膨胀等因素，各种不同的材料，特别是独特且创新的丝材，如木质丝材或活性发泡耗材（LW-ASA，PLA-Aero等），在打印过程中的体积会膨胀。材料生产中的不一致性也可能导致挤出的变化。此外，不适当的长期存储条件，例如高湿环境，可能会损害耗材质量，导致在打印过程中出现无法预见的改变。另外，长期使用造成的轻微机械磨损也可能导致挤出不良。不准确的挤出量必然会影响打印质量。

如果这些流量被准确地校准，我们的打印机可以增强与各种材料的兼容性，使我们能够使用甚至是有瑕疵或特殊的耗材来提高整体打印质量。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/filament-diameter-off.png)

一些因为打印缺陷被闲置的耗材，测量出来的直径过度偏离了 1.75mm.

# 常用的流量校准是如何完成的，以及它的限制是什么？

不少爱好者曾经尝试过调整E步进和流量比例来解决挤出问题。一个典型的校准方法是打印流量测试板并通过肉眼观察评估其质量。然而，这些测试可能无法完全反映实际打印条件，也不能直接测量挤出量。这种方法的可靠性和精度不可控。

还有的人尝试过打印单壁立方体，然后测量壁的厚度并对比设置的。然而，每条挤出线两侧的弧形面会引起测量误差，且不好估计，使得这些方法的可靠性和精度有待探究。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/manual-flow-plates-wall.png)

左图：通过打印流量卡片来观察哪一个流量比例打印出来的卡片比较完美。右图：通过打印单层墙的方块，计算实际线宽和理论线宽的比例。

有时候遇到缺陷，尝试了调整各种参数试图提高打印质量但效果不好。然而，这些调整可能导致不同情况下的打印质量不一致。特殊材料，如轻微膨胀的木质耗材或明显膨胀的发泡材料，如PLA-Aero或LW-ASA，可能需要流量校准以保持质量并避免过度挤出。在轻质发泡丝材如木质耗材的情况下，校准可能有助于减少过度挤出并提高表面质量。

# 使用Bambu Lab Micro Lidar进行自动流量校准

下面，我们介绍如何使用Bambu Lab Micro Lidar 进行高精度流量校准。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/flowcalib-wood-compared.png)

## 原理

针对流量的校准Bambu Lab's high-precision Micro Lidar 提供了一种全新的方式，可以直接测量挤出量，并使用它来计算适合这个耗材的流量比例参数。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/lidar-principle.png)

首先，我们会尽可能模拟实际打印条件的环境，并使用几个不同的参数，打印出一组校准挤出线。然后，使用Micro Lidar扫描校准线对打印的校准线截面积做测量，并通过图像算法增强测量精度。在这个看似简单的过程背后，隐藏着一系列复杂的图像和信号处理算法。通过这些复杂的打印和计算过程，最后结合我们的智能算法，给出针对这个耗材最佳的流量设置。不同于先前的方法，这个方法通过对实际挤出进行测量，可以客观地给出流量比例，并提供比较高质量的测量结果。

## 如何开始测量

使用Micro Lidar 做自动流量测量需要 Bambu Studio 1.7以上的版本。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/flowrate-calib-entry.jpg)

请详细读开始页面上的信息。需要注意的是，有一些材料（透明材质，半透明材质，丝绸材质，有微粒的材质等）因为其反射特性会干扰测量结果，这些材料暂时不支持自动流量校准。 请看下文“不支持的耗材”表格

**注意：**必须选择正确的材料类型。不然可能会引起打印件损坏。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/flowrate-calib-filament-select.jpeg)

对于第三方耗材，你可以在耗材设置中修改其预设。**最相关的参数是默认的流量比率和最大体积速度。错误的最大体积速度可能会导致喷嘴堵塞。**

同时检测一下其他参数是否符合耗材的参数性能。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/flowcalib-filament-preset-notes.png)

For third party filaments, you can adjust the preset base on their specs or your printing preferences.

完整的 Studio 发起教程请看 [wiki tutorial for Bambu Studo.](../../en/software/bambu-studio/calibration_flow_rate.md)

校准将需要几分钟的时间来完成。完成后，将会提供一个推荐的流量比率。在保存丝材预设之前，你可以调整结果或改变预设的名字。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/flowcalib-result.png)

## 支持的耗材类型

流量测量需要非常高的精度，目前并非所有的耗材都能通用。当然我们正在努力提高稳定性和兼容性。

具有特殊反射面的丝材（如闪光，金属和丝绸PLA）可能会干扰测量精度，因此不适合校准。

不支持透明或半透明的丝材。

特别注意：对于明显膨胀的发泡丝材（如PLA Aero或LW-ASA），建议以较低的流量开始（例如，0.6）。

下表总结了常见的不兼容耗材。表中未包括的丝材可能也会因为其他独特的属性而失败。

|  |  |  |
| --- | --- | --- |
| 耗材类型 | 表面光泽 | 原因 |
| PLA | Sparkle  Marble  Metal  Silk | 表面材质影响测量精度 |
| 其他所有 | 透明的  半透明的 | （半）透明材料不兼容 |
| TPU |  | 无法打印校准线 |

## 如何知道校准是否成功?

当校准结果返回“失败”时，表示无法正确地识别校准图案。你可以修正下面的问题并尝试再次校准。校准可能由多种原因失败。除了上述不支持的丝材外，最常见的原因包括模糊或收到遮挡的校准图案和错误的耗材设置。

## 被遮挡的校准图案

某些耗材可能会在激光扫描期间产生遮挡校准模式的丝或碎片。碎片可能来自于扫描过程中的过度丝材泄漏，或者仅仅是被风扇吹上校准图案的上一次打印的残余物。试着清除校准图案和干扰后重新进行校准。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/flowcalib-pattern-debris.png)

### 错误的耗材设置

为了校准一种耗材，打印校准图案是必要的，尽管它并不需要被打印地十分完美。错误的耗材设置，例如，不适当的热床温度使得校准图案无法粘附在热床上，错误的初始耗材比例，或者在使用第三方耗材时选择了错误的耗材类型，都可能导致无法打印校准图案或者生成过宽或过窄的校准线。

例如，如果你试图使用为PLA-Aero设定的预设来校准第三方的PLA，而它的初始流率设定为0.6，这对于不发泡的材料来说，会导致严重的欠挤出，此时可能无法准确地得到测量结果。

![](https://wiki.bambulab.com/knowledge-sharing/flowrate-lidar/flowcalib-pattern-common-problem.png)

常见失败原因

### 其他可能的原因:

- 不兼容的耗材
- 耗材的预设与耗材类型不匹配，初始挤出流量偏差过大，或热床与耗材不匹配
- 打印头尺寸不匹配
- Micro Lidar 的镜头脏了导致图像模糊 - 及时清理镜头。
- 热床上有污垢导致材料不粘

如果你对校准结果不满意，你可以使用它测试的结果或者将你的经验值入到耗材预设中，并基于这个新的初始值重新开始测量。

一个接近的真实的初始流量比例有助于打印校准面板，通常能带来更好的流量测量结果。

## 如何使用测量结果

校准后，结果可以存储在耗材预设中。或者，你也可以直接在耗材卷上记下这个数字。

对于未来的打印项目，你可以在Bambu Studio中使用已校准的预设来切片打印。

# 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
