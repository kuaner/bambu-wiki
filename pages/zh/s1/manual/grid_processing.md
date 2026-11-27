---
path: zh/s1/manual/grid_processing
title: "网格编辑"
description: ""
tags: []
created: 2026-11-26T14:00:33.727Z
updated: 2026-11-26T14:00:33.727Z
source: https://wiki.bambulab.com/zh/s1/manual/grid_processing
---

## 生成网格

点击右上角的“生成网格”，选择对应的网格类型以及其他选项。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_10.png)

| 网格类型 | 结构状态 | 处理特点 | 适用场景 |
| --- | --- | --- | --- |
| **非封闭网格** | 保留原始扫描数据，存在大量开放孔洞和未闭合边界。 | 不进行任何填洞修复，数据处理耗时最短。 | 用于观察原始扫描状态、局部特征比对；**不能**直接用于 3D 打印或数控加工。 |
| **半封闭网格** | 通过算法自动封闭了部分较小孔洞（直径＜设定阈值），但较大开口或复杂结构仍保持开放。 | 在效率和基础修补之间取得平衡，减少手动补洞工作量。 | 适合初步特征提取、曲面拟合或非完全实体化模型的快速处理。 |
| **全封闭网格** | 完全没有开放边缘或孔洞，形成水密闭合实体模型。 | 所有三角面首尾相连形成完整容积，通常需额外的修复和封装步骤。 | 可用于 3D 打印、有限元分析（FEA）以及数控加工（CAM）切片等需要实体模型的场景。 |

生成后左下角将显示该网格的面数。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_11.png)

## 网格清理

和之前的“点云清理”相似，可使用套索等工具对生成的网格进行清除，删去无效的网格。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image.png)

## 补洞

当模型表面存在缺口或孔洞时，使用补洞功能可自动/手动修复。

- 曲率：参考缺口周围的模型弧度，用曲面补全缺口。
- 平面：参考缺口周围的高度，用平面补全缺口。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_1.png)

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_12.png)

选择合适的类型后，点击模型上的孔洞，即可修复。

![PixPin_2026-08-26_10-03-15.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/pixpin_2026-08-26_10-03-15.gif)

## 细化网格

如需保留模型细节，可选择增细化网格，增加网格数量。注意，网格数量越高，软件处理时间也会相应增加。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_6.png)

## 简化网格

简化网格会减少模型面数，使结构更轻量，软件处理更加快捷，但精细度也会相应降低。  
智能简化中只需要选择合适的档位，即可快速简化。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_8.png)

手动简化通过调整百分比控制面数，适合需要限定模型面数的场景。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_7.png)

## 材质球

材质球用于定义模型表面的颜色、光泽和质感，让模型呈现逼真的视觉效果。

若扫描配置中未选择“彩色扫描”，那么可以使用材质球功能，在网格上增加材质细节。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_3.png)

## 贴图调整

通过调整颜色参数，确保贴图色彩更加鲜明美观。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/grid_processing/image_2.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
