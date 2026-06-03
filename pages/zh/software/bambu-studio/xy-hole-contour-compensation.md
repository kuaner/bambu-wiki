---
path: zh/software/bambu-studio/xy-hole-contour-compensation
title: "X-Y 内/外轮廓尺寸补偿"
description: "了解 Bambu Studio 中的 X-Y 内/外轮廓补偿如何提升尺寸精度。本指南将说明何时使用该功能、如何逐步完成校准，以及常见的限制因素，帮助您实现可靠的零件装配与配合。"
tags: []
created: 2023-08-31T03:30:11.734Z
updated: 2026-05-08T04:05:57.533Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/xy-hole-contour-compensation
---

## 如何判断是否需要进行 X-Y 内/外轮廓尺寸补偿？

当出现以下情况时，您可能需要进行 X-Y 内/外轮廓尺寸补偿：

- 螺丝或螺栓无法装入打印孔中
- 销钉或轴感觉过紧
- 组装部件需要打磨或用力才能配合
- 测量的孔径小于设计值

![screw_doesnt_fit.gif](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/screw_doesnt_fit.gif)

  

## 什么是 X-Y 内/外轮廓尺寸补偿？

**X-Y 内/外轮廓尺寸补偿**是 Bambu Studio 中用于校正零件尺寸的功能。

它包含两个独立设置，均用于改善配合度和尺寸精度：

- **X-Y 内轮廓尺寸补偿**  
  调整每一层中孔（封闭、中空区域）的大小。  
  仅影响孔的尺寸，不改变模型的外部尺寸。
- **X-Y 外轮廓尺寸补偿**  
  调整模型的外部轮廓。  
  在保持孔尺寸不变的情况下，增大或减小整体 XY 尺寸。

![hole_vs_contour_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/hole_vs_contour_zh.jpg)

  

## 何时使用？

当模型需要与其他组件（如螺丝、销钉、磁铁或其他打印零件）精确配合时，请使用 X-Y 内轮廓补偿和 X-Y 外轮廓补偿。这些设置可以微调尺寸，使其更加适配。

  

## 其他相关问题

其他因素也可能影响模型尺寸精度。在调整 X-Y 内/外轮廓尺寸补偿之前，请检查这些问题：

- [材料收缩](../../knowledge-sharing/3d-prints-shrinkage.md)：耗材冷却时会收缩，这可能导致孔变小
- [象脚](parameter/elephant-foot.md)：由热床首层过度挤压引起
- [潮湿耗材](../../filament-acc/filament/dry-filament.md)：导致挤出不一致
- [动态流量](calibration_pa.md)：未正确校准
- [接缝](Seam.md)：此功能可能影响孔精度

  

## 如何校准 X-Y 内轮廓尺寸补偿

### 第 1 步：打印测试模型

使用包含多个已知孔径的校准模型。Makerworld 上有多个测试模型，大多数需要游标卡尺测量以校正。  
@Lebadjuras 设计的[模型](https://makerworld.com.cn/zh/models/1947752-xy-kong-bu-chang-wu-xu-qia-chi#profileId-2163636)，使用已知公制螺丝尺寸用于测试孔径。您可以使用 M3、M4、M5 或 M6，具体取决于您手头可用的螺丝。

> ℹ️ **注意**：校准参数**仅适用当前测试耗材**，更换材料时需要重复进行。测试时，请使用与最终零件相同的**工艺配置文件和耗材**打印模型。

- 在 Bambu Studio 中[打开模型](https://makerworld.com.cn/zh/models/1947752-xy-kong-bu-chang-wu-xu-qia-chi?from=search#profileId-2163636)(1) 并打印，使用您所需的耗材和打印配置文件。

![makerworld_xy_hole_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/makerworld_xy_hole_zh.jpg)

在此示例中，使用**M6 螺丝**。使用尺寸大的螺丝可以使校准结果更精确，因此建议使用 M6 螺丝。

> ℹ️ **注意**：M6 螺丝的公称尺寸为 6.0 mm，但由于制造公差，实际直径通常较小。  
> 大多数 M6 螺丝遵循 ISO 6g 标准，故意使螺纹略小以确保易于组装。实际上，直径通常约为 5.9 mm。  
> ![m6_screw_diameter.png](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/m6_screw_diameter_zh.jpg)

**将 X-Y 内轮廓补偿和 X-Y 外轮廓补偿设置为 0 mm**，然后打印模型。  
请注意，M6 孔测量值为 5.9 mm，与螺丝直径匹配。该孔位的螺丝应该非常紧。

![true_diameters_m6.png](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/true_diameters_m6_zh.jpg)

### 第 2 步：测试孔

使用您可用的螺丝尺寸，测试哪个孔能让螺丝紧密配合。不应有任何晃动。

![noxyhole_compensation.gif](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/noxyhole_compensation.gif)

检查哪个孔能确保精确配合后，记录该数值。**在该案例下，为 + 0.15**。

### 第 3 步：在 Bambu Studio 中应用设置

转到**工艺** ⏩ **质量** ⏩ **精度**

在**X-Y 内轮廓补偿**中输入记录的数值，孔直径将增加两倍补偿值，如下图所示。

![xy_hole_compensation.png](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/xy_hole_compensation_zh.jpg)

点击**保存图标** (1) 并重命名**工艺配置文件**以便于参考 (2)，然后点击**确定** (3)。

此保存的配置文件可作为您的自定义**精密配合配置文件**重复使用。

![save_the_profile_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/save_process_zh2.jpg)

### 第 4 步：验证

使用**修改后的打印工艺**重新打印并再次测试。  
这次螺丝应该适合正确的公制尺寸（M3、M4、M5 或 M6）。

![afterocmpensation.gif](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/afterocmpensation.gif)

### 第 5 步：如有需要，重复调整

如果由于某种原因螺丝不适合正确的公制尺寸孔，请确定它适合哪个孔。将新的孔数值添加到 Bambu Studio 中之前记录的数值中。

> **例如**，在第 3 步中，您将 XY 孔补偿设置为 0.2 mm。再次打印校准模型后，螺丝正确适合 +0.1 mm 的孔。在这种情况下，将数值相加：
>
> - **0.2 mm + 0.1 mm = 0.3 mm**
> - **将 XY 孔补偿设置为 0.3 mm**
>
> 根据需要重复此过程，直到达到所需的配合度。  
> 如果在任何时候所有孔都明显变得太大，请重新开始校准过程并返回**第 1 步**。

## 如何校准 X-Y 外轮廓尺寸补偿

### 第 1 步：打印测试模型

@Lebadjuras 设计的[模型](https://makerworld.com.cn/zh/models/1947655-wu-xu-you-biao-qia-chi-de-xylun-kuo-xiao-zhun#profileId-2163528)使用大多数用户都能获得的已知参考尺寸：**原装 Bambu Lab 可重复使用料盘**。  
为了获得准确校准，必须使用原装 Bambu Lab 可重复使用料盘。

![makerworld_xy_contour_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/makerworld_xy_contour_zh.jpg)

### 第 2 步：在 Bambu Lab 料盘中测试配合度

模型打印完成后，尝试将其装入 Bambu Lab 料盘的中间。

![spool_side_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/spool_side_zh.jpg)

它应该紧密配合，没有任何松动。它也应该固定在原位，不会掉入料盘中心孔：  
![perfectfit_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/perfectfit_wiki.jpg)

下面是两个配合不良的示例：  
![fit_check.png](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/fit_check_zh.jpg)

如果您**没有游标卡尺**，不用担心，请按照下一步操作。

### 第 3 步：重复调整配合度

如果没有精确的测量工具，我们可以重复调整 X-Y 外轮廓值并重新打印零件，直到达到所需的配合度。

- 如果**零件在料盘中心太松**，您需要增加数值，尝试 **0.1 mm** 的增量，直到达到合适的配合度。
- 如果**零件无法装入料盘中心**，您需要减小数值，尝试 -**0.1 mm** 的增量，直到达到合适的配合度。

![iteration_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/iteration_wiki_zh1.jpg)

  

### 第 4 步：保存配置文件

一旦达到所需的配合度。点击**保存图标** (1) 并重命名**工艺配置文件**以便于参考 (2)。  
然后点击**确定** (3)。

保存的配置文件可作为您的自定义**精密配合配置文件**重复使用。

![save_process_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/save_process_zh1.jpg)

## 局限性

X-Y 内轮廓尺寸补偿仅适用于闭合走线，如果模型侧边有开口，导致单层内的走线未闭合，则无法使用 X-Y 内轮廓尺寸补偿功能。

如下图模型，侧边有几个孔洞，导致中间有些层未闭合，所以这些层是没有孔的（如右图的74层），将不会受 X-Y 内轮廓补偿功能影响，只能对其进行 X-Y 外轮廓补偿。

![](https://wiki.bambulab.com/software/bambu-studio/xy-hole-contour-compensation/%E4%BB%85%E6%9C%89%E5%A4%96%E8%BD%AE%E5%BB%93%E6%97%A0%E5%AD%94.png)

若对走线未闭合模型使用 **X-Y 内轮廓尺寸补偿**，会发现孔洞处有明显分层。

![real_model_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/ksr-fdm-test/real_model_wiki.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
