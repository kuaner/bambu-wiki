---
path: zh/software/bambu-studio/fix-model
title: "修复模型"
description: ""
tags: []
created: 2023-08-23T08:49:15.647Z
updated: 2026-08-28T06:20:01.160Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/fix-model
---

Bambu Studio 具备自动修复功能，但有时可能需要使用专门的工具来修复模型。如果您在 Windows 10/11 系统下使用 Bambu Studio，可以通过 Netfabb 使用 Microsoft 的 API 来修复 3D 模型，这个功能只支持在 Windows 系统上使用。

## 如何分辨损坏的对象

选中对象，会在Bambu Studio右下角看到“修复”的警告，并且在“对象”里面会看到该对象名字前面有一个警告符号。

![](https://wiki.bambulab.com/software/bambu-studio/repair-model/xiufu.png)

![](https://wiki.bambulab.com/software/bambu-studio/repair-model/objectrepair.png)

## 如何修复损坏的对象

有三种可以用于修复损坏对象的方法，供您选择。

- **选中需要修复的对象，鼠标右击它，然后选择“修复模型”。**

![](https://wiki.bambulab.com/software/bambu-studio/repair-model/youjixiufu.png)

- **点击警告中的“修复”链接**

![](https://wiki.bambulab.com/software/bambu-studio/repair-model/dianjixiufu.jpg)

- **点击对象列表里的警告符号**

![](https://wiki.bambulab.com/software/bambu-studio/repair-model/objectrepair.png)

## 示例

针对原始已损坏的模型对象出现了警告。

![](https://wiki.bambulab.com/software/bambu-studio/repair-model/yuanshixiufujinggao.png)

如果没有进行修复，切片完成后的效果如下图，可以看到部分骆驼图案不见了。

![](https://wiki.bambulab.com/software/bambu-studio/repair-model/sunhuaiqiepian.png)

然而，当它修复完成后，重新进行切片将会得到下图中的正确切片效果。

![](https://wiki.bambulab.com/software/bambu-studio/repair-model/xiufuhouqiepian.png)

该[模型](https://www.thingiverse.com/thing:860034)由[rob keers](https://www.thingiverse.com/braveheart)提供。

## 注意

Studio 只能检测和修复部分错误，有些模型缺陷无法检测，因此可能无法提示需要修复。  
另外，表面不平滑的模型（比如来自 3D 扫描仪的模型）可能打印质量也会较差，尤其是打开圆弧拟合的情况下，问题还会被放大。此时可**关闭圆弧拟合**，并且考虑使用 Meshlab 等软件进行修复和平滑优化模型质量。

![smooth.png](https://wiki.bambulab.com/software/bambu-studio/fix-model/smooth.png)

![arccn.png](https://wiki.bambulab.com/software/bambu-studio/fix-model/arccn.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
