---
path: zh/software/bambu-studio/manual/locked-zag
title: "Bambu Studio Locked Zag 填充图案使用说明"
description: ""
tags: []
created: 2025-05-29T07:42:08.319Z
updated: 2025-05-29T08:53:33.891Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/manual/locked-zag
---

## **如何启用 Locked Zag 填充**

您可以在软件界面的**工艺 → 强度 → 稀疏填充图案**的下拉菜单中选择“Locked Zag"填充图案。该填充结构如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-6.png)

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-4.png)

## 纹理结构介绍

Locked Zag 是一种**兼顾外观与结构强度**的填充图案，它由两部分组成：

**Skin（表皮）**：

- 位置：紧贴模型内墙一圈的填充区域；
- 纹理：采用 **Cross Zag** 走线方式；
- 效果：确保侧面纹理与标准 Cross Zag 完全一致；
- 查看技巧：在**走线类型**中关闭"内外墙显示"可直观观察填充侧面效果，如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-2.png)

表面效果与 Cross Zag 填充一致：  
![表面效果与Cross Zag填充一致](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-5.png)

**Skeleton（骨架）**：

- 位置：填充内部核心区域；
- 纹理：采用 **Zigzag** 走线方式；
- 特性：与表皮层存在一定的重叠区域，增强结构强度，完整的填充图案横截面如下图。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-3.png)

![内部纹理和Zig Zag一样](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-1.png)

**优势对比**：

- **使用 Zigzag 骨架，提供更高的强度**（比 Cross Zag 填充的强度更强）；
- **保留 Cross Zag 的表面纹理；**
- **可调节表皮骨架的重叠区域，优化结合强度。**

## 参数介绍

**稀疏填充密度：**控制整体内部稀疏填充的密度，如下所示。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250526191449_rec_.gif)

**注：表皮和骨架填充密度是基于稀疏填充密度的子参数**——

- 当您调整**稀疏填充密度**时，表皮和骨架填充密度会**自动同步更新；**
- 但您仍可**单独调整表皮和骨架密度**，使其在作用范围内覆盖默认值；

**表皮填充密度：**仅调整内部稀疏填充中的表皮区域的填充密度，它会进一步影响内部稀疏填充侧面的密度，如下所示。

![15%表皮填充密度](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250526173416_rec_.gif)

![50%表皮填充密度](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250526173623_rec_.gif)

**骨架填充密度：**

仅调整内部稀疏填充中的骨架区域填充密度，影响内部填充的走线密度，效果如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250526210614_rec_.gif)

**填充互锁深度：**调节表皮与骨架的重叠宽度，互锁深度越深，结构越牢固。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250529141445_rec_.gif)

**表皮填充深度：**控制表皮的厚度，值越大，表层覆盖越深，填充的侧表面更接近 **Cross Zag** 填充。***注意：填充互锁深度不能大于表皮填充深度，默认互锁深度为50%的表皮深度。***

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250526210919_rec_.gif)

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image.png)

**表皮线宽：**调整填充纹理中的表皮走线的宽度。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250527150746_rec_.gif)

**骨架线宽：**调整填充纹理中的骨架走线的宽度。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250527151722_rec_.gif)

## **解决「填充分区」问题**

**什么是填充分区？**

当模型的不同区域使用**不同的填充密度或线宽**时，填充可能会被切割成独立区块，导致：

- **填充之间出现缝隙** → 粘接强度下降
- **打印时易撕裂或打印失败**

下图是用修改器修改立方体局部填充参数的示例，我们可以看到被修改过参数的区域和其他区域出现了明显的分区。

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/20250527155018_rec_.gif)

而 Locked Zag 填充图案的**4 个调整参数**，确保不同密度/线宽的填充仍能**无缝连接**，避免产生分区。下面给立方体添加修改器后，修改局部参数的效果。

**修改表皮和骨架的密度：**

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-7.png)

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-8.png)

**修改表皮和骨架的线宽：**

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-9.png)

![](https://wiki.bambulab.com/software/bambu-studio/locked-zag/image-10.png)

## **使用场景推荐**

我们建议您在下列场景使用该填充图案：

- 需要 Cross Zag 的表面纹理但又需要更高的结构强度
- 想要兼顾打印零件的美观与耐用性

尤其是打印高受力部件（如鞋子）等模型时，您可以选择 Locked Zag 填充图案进行打印。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（工作日 9:00-21:00；节假日 9:00-18:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
