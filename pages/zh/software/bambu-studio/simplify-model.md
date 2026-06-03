---
path: zh/software/bambu-studio/simplify-model
title: "简化模型"
description: ""
tags: []
created: 2023-07-27T07:40:34.701Z
updated: 2026-05-11T01:57:33.268Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/simplify-model
---

3D模型通常由三角面片组成，对于一些由大量三角形组成的模型，由于打印机本身的精度限制（如喷嘴直径限制），并不能将模型中非常小的细节打印出来。而且这类模型往往需要很长时间才能完成切片，甚至会因为生成大量短工具路径而拖慢FDM 3D打印机的速度。这时候就可以使用简化模型功能，通过一定程度地减少模型的三角形数量来减少切片时间。注意，简化模型可以减少切片的时间，但不一定会减少模型的打印时间。  
  
在您导入复杂模型时，会收到建议模型简化的通知，如下图。

![](https://wiki.bambulab.com/software/bambu-studio/simplify-model/简化提示.png)

这时，您可以直接点击上图中的“简化模型”。或者您可以使用简化网格功能减少网格中的三角形面片数量。请右键单击模型，从右键菜单中选择 "简化模型"。（见下图中的红色方块。）

![](https://wiki.bambulab.com/software/bambu-studio/simplify-model/简化模型.png)

可以通过勾选“显示线框”，查看各个三角形面片的白色轮廓。  
您可以通过调节“细节等级”对模型简化进行粗调，是在简化率的一个小范围内进行调整。

![](https://wiki.bambulab.com/software/bambu-studio/simplify-model/细节等级.gif)

也可以通过调节“简化率”对模型从0-100%进行细调，可以大幅度减少三角形面片的数量。

![](https://wiki.bambulab.com/software/bambu-studio/simplify-model/简化率.gif)

值得一提的是，如果您希望达到"低多边形"效果，您可以利用"简化模型"功能，将简化率调至极高水平，以减少三角形面片的总数。简化率越高，三角形面片的数量越少，从而使模型呈现出更为简单和抽象的外观。

以原始三角形面片数量为225154的模型为例，打印效果为：

![](https://wiki.bambulab.com/software/bambu-studio/simplify-model/原始模型三角形面片.png)
![](https://wiki.bambulab.com/software/bambu-studio/simplify-model/原始模型1.png)

如果将模型简化率不断降低，当模型的三角形面片数量简化到315个时，打印效果为：

![](https://wiki.bambulab.com/software/bambu-studio/simplify-model/简化率高模型.png)
![](https://wiki.bambulab.com/software/bambu-studio/simplify-model/简化率高模型打印.png)
