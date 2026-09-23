---
path: zh/r1/manual/contour-trace-extraction-guide
title: "Bambu Suite 循边提取功能介绍"
description: "本文介绍了 Bambu Suite 循边提取功能"
tags: []
created: 2026-09-22T12:49:09.690Z
updated: 2026-09-22T12:49:10.938Z
source: https://wiki.bambulab.com/zh/r1/manual/contour-trace-extraction-guide
---

## 循边提取功能介绍

循边提取是一项将拍照图中实物边框提取为可加工矢量路径的功能。只需要将想切割或雕刻的物体放到设备里拍照，在软件中用工具选中图案的轮廓，系统会自动生成一条可以用于激光切割的路径。无需画图或手动描摹，框选即可提取。

![001.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/001.webp)

## 什么时候使用？

| **场景** | **说明** |
| --- | --- |
| **复刻实物轮廓** | 想沿着某个物体的边缘切割出一块一模一样的形状，比如给工具做收纳槽、复刻一个零件 |
| **利用手绘/已有图案** | 在材料上手绘了一个图案/材料上原有图案，想把它切割下来 |
| **复制现有物件** | 有一块积木、拼图或现成零件，想用激光复刻一份 |
| **不规则形状加工** | 物体形状不规则，很难用绘图软件精确描出来 |

## 操作步骤

### 第一步：准备页拍照

进入准备页，点击“一键准备”或“精细拍照”完成拍照，可以使用俯视拍照快速获取全局图像，也可以使用精细拍照获取更高精度的局部图像。

> 精细拍照精度可达 0.2 mm，对于需要高精度复刻的场景（如收纳盒紧配），建议使用精细拍照。

|  |  |
| --- | --- |
| 002.png | 003.png |

### 第二步：进行循边提取

点击 “循边提取” 按钮。

![contour-trace.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/contour-trace.png)

### 第三步：选择提取对象

使用选择工具来指定要提取的对象。

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/005.png)

工作区提供三种工具：**框选、点选和清除选区**。

#### 框选（矩形选区）

拖拽绘制矩形框，框内的内容将被选中。

- **添加到选区**：继续拖拽新的矩形框，追加到现有选区中。
- **从选区中减去**：拖拽矩形框从现有选区中扣除。

![006.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/006.webp)

默认开启“聚焦选区”，将使轮廓选区更精细。

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/007.png)

#### 点选（智能选区）

点击图片上的某个区域，系统会自动选中颜色/亮度相近的连通区域，适合快速选中轮廓清晰的对象。

- **添加到选区**：点击新区域，追加到现有选区中。
- **从选区中减去**：点击已选中的区域，从选区中扣除。

![008.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/008.webp)

#### 清除选区

点击 “清除选区” 按钮，立即清空当前所有选区，重新开始选择。

![009.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/009.webp)

### 第四步：调节提取参数

选区确定后，右侧面板提供三个调节参数，实时影响提取效果：

| **参数** | **说明** | **往大调** | **往小调** |
| --- | --- | --- | --- |
| 亮度阈值 | 控制识别轮廓的灵敏度，决定哪些像素被纳入轮廓范围 | 识别更多区域，轮廓可能变大 | 识别更少区域，轮廓可能变小 |
| 平滑度 | 控制提取轮廓的锯齿平滑程度 | 轮廓更圆润，但可能丢失细节 | 轮廓更精细，保留更多原始细节 |
| 轮廓偏移 | 控制轮廓向内缩进或向外膨胀（范围 -0.5mm ~ +0.5mm） | 正值膨胀，轮廓放大（松配） | 负值缩进，轮廓缩小（紧配） |

> 💡 提示：调节参数时，轮廓预览会实时更新，可以直观看到每个参数对结果的影响。

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/010.png)

### 第五步：节点编辑（可选）

提取完成后，如果对轮廓的局部细节不满意，可以进入节点编辑模式：

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/011.png)

- 选中生成的轮廓线条，点击“编辑节点”
- 您可以拖拽已有节点来调整线条走向
- 您可以增删节点来精细控制轮廓形状

![012.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/012.png)

### 第六步：应用

点击 “应用” 按钮，系统将基于当前选区 + 参数设置，生成矢量切割路径；

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/013.png)

并自动返回准备页，在盘面上直接显示切割路径，位置与提取对象在图片中的位置对应。

![014.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/014.png)

### 第七步：加工或进一步编辑

- **直接加工**：确认轮廓位置无误后，点击“开始加工”，系统按默认切割工艺执行。
- **手动调整**：在准备页选中轮廓，可拖拽移动、旋转、缩放。
- **返回设计页编辑**：切换到 Design 页，可进行高级编辑后再回到准备页加工。

![015.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/contour-trace-extraction-guide/zh/015.png)

## 常见问题

Q：**俯视图和精细拍照都能用吗**？

A：都可以。精细拍照精度更高（0.2 mm），适合需要高精度复刻的场景；俯视图速度更快，适合简单轮廓提取。

Q：**框选和点选有什么区别？**

A：框选是按矩形范围选择，适合区域明确的场景；点选是按颜色/亮度自动吸附选择，适合轮廓清晰、与背景对比明显的对象。两者可以配合使用。

Q：**选错了区域怎么办？**

A：可以用“从选区中减去”功能扣除不需要的部分，也可以直接点击“清除选区”一键清空重新选择。

Q：**亮度阈值调多少合适？**

A：没有固定值。边拖动边观察实时预览，以提取的轮廓与实际物体边缘最贴合为准。

Q：**轮廓偏移参数有什么用？**

A：激光有光斑直径，切出来的实际尺寸会比理论轮廓略大。设置负偏移（缩进）可以补偿这一误差，让切出来的成品与原件严丝合缝——做收纳盒、工具槽时非常有用。

Q：**提取的轮廓可以直接切割吗？**

A：可以。确认后默认采用切割工艺，可直接点击“开始加工”。

Q：**提取的轮廓能带回设计页编辑吗？**

A：可以。切换到设计页后，轮廓会出现在对象列表末尾，您可以进行节点编辑等高级操作。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
