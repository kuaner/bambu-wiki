---
path: zh/software/bambu-suite/manual/sticker-tool
title: "贴纸工具"
description: ""
tags: []
created: 2025-03-25T11:01:17.860Z
updated: 2025-05-28T08:21:21.111Z
source: https://wiki.bambulab.com/zh/software/bambu-suite/manual/sticker-tool
---

Bambu Suite的贴纸工具能够帮助用户基于导入的图案，通过先打印后切割的方式制作带边框的精美贴纸。原始图案可以是由像素点构成的位图，也可以是矢量图。

## 贴纸制作步骤

制作贴纸一般分为如下几个步骤。

1. 导入图片，如果导入的是位图，通常需要对图片做去背景处理，保留需要制作成贴纸的图案部分。您可以参考下面的动图中的步骤，一键智能删除图片背景。而矢量图通常都是无背景的，则无需处理。（[picture](https://www.freepik.com/free-vector/cute-shiba-inu-dog-super-hero-playing-laptop-cartoon-vector-icon-illustration-animal-technology_36238518.htm#fromView=author&page=1&position=35&uuid=e3e9e15e-9c66-4f98-95a8-897e452644fd&query=laptop) from [@catalyststuff](https://www.freepik.com/author/catalyststuff)）

![](https://wiki.bambulab.com/h2/manual/sticker-tool/1.gif)

2. 选中图片，点击贴纸工具，您可以自定义设置贴纸边框宽度、颜色等参数（下文中会有参数的具体介绍），生成贴纸对象。**软件会自动将贴纸图案设置为打印后刀切的制作工艺。**

![](https://wiki.bambulab.com/h2/manual/sticker-tool/2.gif)

3. 准备制作，材料选择**不干胶打印纸**。**并提前在您的纸质打印机内放置不干胶打印纸，用于在上面打印贴纸所需要的图案。**

![](https://wiki.bambulab.com/h2/manual/sticker-tool/image-7.png)

4. 点击“制作”，软件会发送切割任务到Bambu打印机，也会弹窗要求发送纸质打印文件到您的纸质打印机上。在不干胶打印纸上打印出来相关图案后，用户需要将打印好的贴纸从纸质打印机取出，按提示粘贴到刀切垫板的对应位置上，到Bambu打印机屏幕上确认并按机器的启动按钮开始切割。

![](https://wiki.bambulab.com/h2/manual/sticker-tool/3.gif)

5. 等待刀切任务完成，获得精美的小贴纸。

## 贴纸工具的参数介绍

1. 设置贴纸边框的填充颜色和宽度。**如果添加了边框，切割时刀路沿着边框进行切割。如果边框类型选择无边框，则切割时会直接顺着图案边缘进行切割。**可选择的边框宽度有窄（2mm）、标准（4mm）、宽（6mm）和自定义这几种选项，可以根据实际需求来设置边框的宽度。

![](https://wiki.bambulab.com/h2/manual/sticker-tool/image.png)

2. 切割内部孔洞，该选项控制是否切割图案的中空部分。开启与关闭切割内部孔洞的效果如下面图片中所示。

![](https://wiki.bambulab.com/h2/manual/sticker-tool/image-1.png)

![](https://wiki.bambulab.com/h2/manual/sticker-tool/image-2.png)

3. 切穿参数。不干胶打印纸一般都是两层，正面的贴纸以及背面的底纸。因此切割时采用的刀压会有两种，切割一层的刀压和切割两层的刀压（也称为切穿刀压）。如果选择“切穿”，则会把两层全部切穿，从不干胶打印纸上分离。对于贴纸，图案部分一般只需要切穿一层，用户可以将带黏性的这一层揭下来直接粘贴。

![](https://wiki.bambulab.com/h2/manual/sticker-tool/image-3.png)

![](https://wiki.bambulab.com/h2/manual/sticker-tool/image-4.png)

4. 创建额外边框。一般用于将贴纸从不干胶打印纸上彻底地切割下来，选择后软件会额外生成一个边框。如果您已经启用了边框，则图案外侧共会生成两层边框。加工时最外层边框将会切穿两层，方便你取下独立的小贴纸。而内层的边框切穿一层，可直接从不干胶打印纸上揭取图案。**如果要启用创建额外边框，需要先关闭切穿功能（因为选择切穿后，内边框也会切穿两层，额外再加个边框就没有意义了）。**

![](https://wiki.bambulab.com/h2/manual/sticker-tool/image-5.png)

![](https://wiki.bambulab.com/h2/manual/sticker-tool/image-6.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
