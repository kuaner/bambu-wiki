---
path: zh/software/bambu-scan/manual/mesh_processing
title: "网格编辑"
description: ""
tags: []
created: 2026-11-26T14:02:01.521Z
updated: 2026-11-27T01:53:51.769Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/manual/mesh_processing
---

### 封装参数

点击右上角的“生成网格”，可选择不同的封装参数。

![001.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/001.png)

#### 网格类型

| 网格类型 | 结构状态 | 处理特点 | 适用场景 |
| --- | --- | --- | --- |
| **非封闭网格** | 保留原始扫描数据，存在大量开放孔洞和未闭合边界。 | 不进行任何填洞修复，数据处理耗时最短。 | 用于观察原始扫描状态、局部特征比对；**不能**直接用于 3D 打印或数控加工。 |
| **半封闭网格** | 通过算法自动封闭了部分较小孔洞（直径＜设定阈值），但较大开口或复杂结构仍保持开放。 | 在效率和基础修补之间取得平衡，减少手动补洞工作量。 | 适合初步特征提取、曲面拟合或非完全实体化模型的快速处理。 |
| **全封闭网格** | 完全没有开放边缘或孔洞，形成水密（Watertight）闭合实体模型。 | 所有三角面首尾相连形成完整容积，通常需额外的修复和封装步骤。 | 可用于 3D 打印、有限元分析（FEA）以及数控加工（CAM）切片等需要实体模型的场景。 |

#### 网格优化

- 网格简化程度：减少面数并缩小文件，避免后续操作加载过慢。
- 网格锐化：强化棱边和转折，提高轮廓清晰度。
- 网格平滑：减轻表面噪点或凹凸，使外轮廓更加光滑。

![002.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/002.png)

### 纹理贴图

扫描前在预设中开启了“彩色扫描”，那么此处可选择是否应用扫描的“彩色贴图”。可使用“AI 彩色图像增强”功能提高锐利度，以及调整人像美化效果以及高光抑制程度。

![003.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/003.png)

生成后左下角将显示该网格的面数。

![004.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/004.png)

### 网格清理

和之前的“点云清理”相似，可使用套索等工具对生成的网格进行清除，删去无效的网格。

![005.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/005.png)

### 补洞

当模型表面存在缺口或孔洞时，使用补洞功能修复。

#### 手动补洞

- 曲率：参考缺口周围的模型弧度，用曲面补全缺口。
- 平面：参考缺口周围的高度，用平面补全缺口。

![006.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/006.png)

选择合适的类型后，点击模型上的孔洞，即可修复。

![007.gif](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/007.gif)

#### 自动补洞

可输入空洞直径，批量补洞。

![008.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/008.png)

多色模型补洞后会出现如下提示，可选择重新贴图。

![009.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/009.jpg)

### 细化网格

如需保留模型细节，可选择增细化网格，增加网格数量。注意，网格数量越高，软件处理时间也会相应增加。

![010.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/010.png)

### 简化网格

简化网格会减少模型面数，使结构更轻量，软件处理更加快捷，但精细度也会相应降低。

智能简化中只需要选择合适的档位，即可快速简化。

![011.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/011.png)

手动简化通过调整百分比控制面数，适合需要限定模型面数的场景。

![012.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/012.png)

### 材质球

材质球用于定义模型表面的颜色、光泽和质感，让模型呈现逼真的视觉效果。

若扫描配置中未选择“彩色扫描”，那么可以使用材质球功能，在网格上增加材质细节。

![013.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/013.png)

### 贴图调整

通过调整颜色参数，确保贴图色彩更加鲜明美观。

![014.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/014.png)

可使用“AI 彩色图像增强”功能提高锐利度，以及调整人像美化效果以及高光抑制程度。

![015.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/mesh_processing/zh/015.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
