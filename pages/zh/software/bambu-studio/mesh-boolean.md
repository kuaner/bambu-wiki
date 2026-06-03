---
path: zh/software/bambu-studio/mesh-boolean
title: "布尔运算"
description: ""
tags: []
created: 2023-08-20T14:12:50.483Z
updated: 2025-12-23T06:25:48.555Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/mesh-boolean
---

## 功能介绍

布尔运算是一种逻辑运算方法，通过对多个物体进行并集、差集、交集的运算，从而得到新的物体形态。常见的三种布尔运算方法是：

1. 并集：把多个物体合并成一个物体；
2. 差集：从一个物体中减去其与其他物体重合的部分；
3. 交集：取多个物体公共的部分。

## 操作步骤

在进行布尔运算之前，可以先选中所需对象，单击鼠标右键，选择 “组合”，即可将它们组合起来，以便于涉及多物体操作时的管理。如果所需对象数量较少，也可以不用组合，直接选择所需对象，即可进行运算。

![bambu_studio_2.4.0.70_组合.gif](https://wiki.bambulab.com/software/bambu-studio/mesh-boolean/bambu_studio_2.4.0.70_%E7%BB%84%E5%90%88.gif)

可以对多个物体组合中的物体、独立的物体以及物体组合本身执行布尔运算。当运算对象全部是独立的，或者全部属于同一个组合中时，结果通常最可预测。

  

### 并集

并集运算是将多个物体合并，得到一个新的独立物体的操作。不论物体的数量、位置、与重叠情况如何，都可以对它们执行并集运算。通过对多个重叠模型执行并集运算，可以自动优化切片，统一打印的走线路径。

操作方法：**选择运算对象 > 工具栏 > “布尔运算” > “并集” > “执行”**

如果两个模型重叠在一起，未进行并集运算，切片会出现重叠的走线，并出现错误提示（见下图右下角）。

- 并集运算前后的切片结果区别如下：  
  ![bambu_studio_2.4.0.70_zh_union_comparison_with_warning.jpg](https://wiki.bambulab.com/software/bambu-studio/mesh-boolean/bambu_studio_2.4.0.70_zh_union_comparison_with_warning.jpg)
- **直接切片两个重叠的模型：**  
  ![bambu_studio_2.4.0.70_并集1.gif](https://wiki.bambulab.com/software/bambu-studio/mesh-boolean/bambu_studio_2.4.0.70_%E5%B9%B6%E9%9B%861.gif)
- **对并集运算后的两个模型进行切片：**  
  ![bambu_studio_2.4.0.70_并集2.gif](https://wiki.bambulab.com/software/bambu-studio/mesh-boolean/bambu_studio_2.4.0.70_%E5%B9%B6%E9%9B%862.gif)

  

### 差集

差集运算是指从一个物体中删除其与其他物体重合部分的操作。

操作方法：**选择运算对象 > 工具栏 > “布尔运算” > “差集” > 根据所需来调整对象字母A或B所代表的模型 > “执行”**

这样就可以删除重合部分。如下图所示，从立方体中去除它与球体相重合的部分，或从球体中去除它与立方体相重合的部分。

![bambu_studio_2.4.0.70_差集.gif](https://wiki.bambulab.com/software/bambu-studio/mesh-boolean/bambu_studio_2.4.0.70_%E5%B7%AE%E9%9B%86.gif)

与负零件功能不同，差集运算功能可以使运算后的模型直接导出为STL文件。而负零件功能无法导出减去负零件的 STL，因为它仅作用于切片过程中，实际的模型几何形状不会被修改（详情参考 [负零件 | Bambu Lab Wiki](subtract-a-part.md)）。

**多物体差集运算：** 通常情况下，当 A 对象框中只放置一个物体（用于从中减去其他物体）时，操作会按预期进行。但如果 A 对象框中放置多个物体，由于物体之间相减的顺序不同，可能会产生不可预测的结果。这种情况下，建议对需要放置在 A 对象框中的物体分别执行减法运算，并勾选 **“保留原模型”** 功能。该功能会保留运算中使用的模型，以便用于后续运算。

![bambu_studio_2.4.0.70_保留原模型.jpg](https://wiki.bambulab.com/software/bambu-studio/mesh-boolean/bambu_studio_2.4.0.70_%E4%BF%9D%E7%95%99%E5%8E%9F%E6%A8%A1%E5%9E%8B.jpg)

### 交集

交集运算是指保留多个物体公共部分的操作。

操作方法：**选择运算对象 > 工具栏 > “布尔运算” > “交集” > “执行”**

![bambu_studio_2.4.0.70_交集.gif](https://wiki.bambulab.com/software/bambu-studio/mesh-boolean/bambu_studio_2.4.0.70_%E4%BA%A4%E9%9B%86.gif)

**多物体交集运算：** 对多个物体执行交集运算的前提是，所选物体必须存在公共重叠部分。如果某一个物体与其他所选物体没有重叠部分，则会显示错误提示，无法执行交集运算，如下图所示：

![bambu_studio_2.4.0.70_交集失败.jpg](https://wiki.bambulab.com/software/bambu-studio/mesh-boolean/bambu_studio_2.4.0.70_%E4%BA%A4%E9%9B%86%E5%A4%B1%E8%B4%A5.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
