---
path: zh/software/bambu-studio/subtract-a-part
title: "负零件"
description: ""
tags: []
created: 2023-08-20T14:26:05.962Z
updated: 2026-08-28T06:19:55.751Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/subtract-a-part
---

在某些情况下，我们可能希望从一个形状中减去或抠出另一个形状，以安装其他五金件。而负零件功能可以帮助我们快速实现这一需求。

|  |  |
| --- | --- |
|  |  |

## 添加负零件

1. 选中需要添加负零件的对象，鼠标右击，选择“添加负零件”。  
   负零件可以是基础几何形状（立方体、圆柱体、球和锥体）或者可以加载用户自定义形状的零件。

![](https://wiki.bambulab.com/software/bambu-studio/negative-part/tianjiafulingjian.png)

2. 此外，您还可以通过右键点击零件，选择"更改类型"，将零件更改为负零件。  
   例如，您可以将创建的文字零件更改为负零件，然后进行切片操作，从而在对象上实现文字凹陷的效果。

![](https://wiki.bambulab.com/software/bambu-studio/negative-part/fulingjiangenggaileixing.gif)

> 与[布尔运算](mesh-boolean.md)不同的是，负零件减法只在切片期间执行，不修改对象的几何形状，因此不支持导出包含减法结果的STL文件。

## 调整负零件尺寸

选择负零件后，可以使用上方功能栏中的缩放功能以及平移功能，调整负零件位置与尺寸。

![zh1.gif](https://wiki.bambulab.com/software/bambu-studio/negative-part/zh1.gif)

![zh2.jpg](https://wiki.bambulab.com/software/bambu-studio/negative-part/zh2.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
