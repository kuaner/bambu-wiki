---
path: zh/software/bambu-studio/subtract-a-part
title: "负零件"
description: ""
tags: []
created: 2023-08-20T14:26:05.962Z
updated: 2026-04-28T02:28:26.823Z
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

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
