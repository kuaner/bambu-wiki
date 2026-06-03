---
path: zh/software/bambu-studio/modifier
title: "Studio 修改器操作指南"
description: "本指南介绍了如何通过 Studio 中的修改器优化高模型的打印速度、调整填充密度以增强模型强度，并在模型表面添加平面文本。"
tags: ["bambu studio"]
created: 2024-09-05T04:18:29.988Z
updated: 2024-11-12T06:32:46.744Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/modifier
---

## 介绍

**修改器（Modifier）** 是一种特殊的对象类型，用于修改模型重叠部分或指定高度范围内的参数。

## 何时使用

例如：

- 当打印模型的高度较高时，可以使用高度范围修改器来减慢模型上部的打印速度，从而防止其在打印过程中发生倒塌。
- 为了增强模型某些较脆弱部分的强度，可以调整相应区域的填充密度，使其更加坚固。
- 如需在模型表面添加平面文本，可使用修改器来实现。

如果想在模型上添加凹陷的文本形状，请参考：[负零件](subtract-a-part.md)  
如果想添加凸出的文本形状，请参考：[添加3D文本](3d-text.md)

## 高度范围修改器

### 修改指定高度范围内的打印速度

步骤 1. 右键单击模型，并从菜单中选择**高度范围修改器**。

![金箍棒-高度范围.png](https://wiki.bambulab.com/modifier/%E9%87%91%E7%AE%8D%E6%A3%92-%E9%AB%98%E5%BA%A6%E8%8C%83%E5%9B%B4.png)

步骤 2. 点击**范围**，可设置指定的模型高度范围。

![金箍棒-范围.png](https://wiki.bambulab.com/modifier/%E9%87%91%E7%AE%8D%E6%A3%92-%E8%8C%83%E5%9B%B4.png)

步骤 3. 可更改指定高度范围内的多个设置。在本指南中，适当调整模型指定高度范围内的打印速度。

![修改速度.png](https://wiki.bambulab.com/modifier/%E4%BF%AE%E6%94%B9%E9%80%9F%E5%BA%A6.png)

步骤 4. 单击屏幕右上角**切片单盘**。切片完成后，在颜色方案中选择**速度**，即可查看指定高度范围内的打印速度与其他部分的速度差异。

![颜色方案-速度.png](https://wiki.bambulab.com/modifier/%E9%A2%9C%E8%89%B2%E6%96%B9%E6%A1%88-%E9%80%9F%E5%BA%A6.png)  
![切片单盘-速度.png](https://wiki.bambulab.com/modifier/%E5%88%87%E7%89%87%E5%8D%95%E7%9B%98-%E9%80%9F%E5%BA%A6.png)

## 修改器的常用功能

### 修改部分填充密度

#### 添加修改器

步骤 1. 右键单击打印板上的模型，在菜单栏中单击**添加修改器**，选择您想要添加的修改器类型。

![添加修改器.png](https://wiki.bambulab.com/modifier/%E6%B7%BB%E5%8A%A0%E4%BF%AE%E6%94%B9%E5%99%A8.png)

步骤 2. 添加后，单击打印板并拖动鼠标，可全方位观察修改器，并调整其与模型重合的部分。

![动画_移动修改器.gif](https://wiki.bambulab.com/modifier/%E5%8A%A8%E7%94%BB_%E7%A7%BB%E5%8A%A8%E4%BF%AE%E6%94%B9%E5%99%A8.gif)

> **注意：任何.stl模型文件都可当做修改器。**
>
> 1. 在**添加修改器**中点击**加载...**，即可将存储的模型文件设置为修改器。  
>    ![加载修改器.png](https://wiki.bambulab.com/modifier/%E5%8A%A0%E8%BD%BD%E4%BF%AE%E6%94%B9%E5%99%A8.png)  
>    ![添加修改器-小船.png](https://wiki.bambulab.com/modifier/%E6%B7%BB%E5%8A%A0%E4%BF%AE%E6%94%B9%E5%99%A8-%E5%B0%8F%E8%88%B9.png)
> 2. 将修改器移动至理想位置时，即可进行切片。  
>    ![小船修改器.png](https://wiki.bambulab.com/modifier/%E5%B0%8F%E8%88%B9%E4%BF%AE%E6%94%B9%E5%99%A8.png)  
>    ![方块小船.png](https://wiki.bambulab.com/modifier/%E6%96%B9%E5%9D%97%E5%B0%8F%E8%88%B9.png)

#### 修改稀疏填充密度

选中修改器后，在屏幕左侧**常用**菜单栏下的**稀疏填充密度**框中，输入想要的模型填充密度值，按回车键即可生效。

![稀疏填充密度.png](https://wiki.bambulab.com/modifier/%E7%A8%80%E7%96%8F%E5%A1%AB%E5%85%85%E5%AF%86%E5%BA%A6.png)

#### 切片单盘

单击屏幕右上角**切片单盘**。切片完成后，移动右侧进度条，可观察到修改器覆盖部分的填充密度明显高于其他部分。

![动画_修改填充密度.gif](https://wiki.bambulab.com/modifier/%E5%8A%A8%E7%94%BB_%E4%BF%AE%E6%94%B9%E5%A1%AB%E5%85%85%E5%AF%86%E5%BA%A6.gif)

### 在模型表面添加文字

#### 添加文本形状

步骤 1. 单击**文本形状**。

![文本形状-添加.png](https://wiki.bambulab.com/modifier/%E6%96%87%E6%9C%AC%E5%BD%A2%E7%8A%B6-%E6%B7%BB%E5%8A%A0.png)

步骤 2. 在**输入文本**框中输入文本，可设置文本字体、大小、厚度等。

![文本设置.png](https://wiki.bambulab.com/modifier/%E6%96%87%E6%9C%AC%E8%AE%BE%E7%BD%AE.png)

步骤 3. 拖动文本，将其放置到模型的任意位置。

![动画_移动文本位置-bbl.gif](https://wiki.bambulab.com/modifier/%E5%8A%A8%E7%94%BB_%E7%A7%BB%E5%8A%A8%E6%96%87%E6%9C%AC%E4%BD%8D%E7%BD%AE-bbl.gif)

#### 修改文本颜色

步骤 1. 单击 **text\_shape**。

![选择bbl文本.png](https://wiki.bambulab.com/modifier/%E9%80%89%E6%8B%A9bbl%E6%96%87%E6%9C%AC.png)

步骤 2. 按下键盘上相应的耗材序号，将文本颜色设置为对应的耗材颜色。

![动画_修改颜色-bbl.gif](https://wiki.bambulab.com/modifier/%E5%8A%A8%E7%94%BB_%E4%BF%AE%E6%94%B9%E9%A2%9C%E8%89%B2-bbl.gif)

#### 将文本附在模型表面

步骤 1. 右键单击文本，选择**更改类型 > 修改器**。

![更改类型-bbl.png](https://wiki.bambulab.com/modifier/%E6%9B%B4%E6%94%B9%E7%B1%BB%E5%9E%8B-bbl.png)  
![更改为修改器.png](https://wiki.bambulab.com/modifier/%E6%9B%B4%E6%94%B9%E4%B8%BA%E4%BF%AE%E6%94%B9%E5%99%A8.png)

步骤 2. 调整文本位置，确保文本与模型表面重合。

![动画_表面重合.gif](https://wiki.bambulab.com/modifier/%E5%8A%A8%E7%94%BB_%E8%A1%A8%E9%9D%A2%E9%87%8D%E5%90%88.gif)

#### 切片单盘

单击屏幕右上角**切片单盘**。切片完成后，可看到文本已附着在模型表面。

![动画_qianru.gif](https://wiki.bambulab.com/modifier/%E5%8A%A8%E7%94%BB_qianru.gif)

## 结束语

> *我们希望本指南能为您提供有用的信息，帮助您解决问题。*
>
> *如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。*  
> *我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)*  
> *我们将尽最大努力及时回复，并为您提供所需的帮助。*
