---
path: zh/r1/manual/measure-feature-introduction
title: "R1 一键准备功能介绍"
description: "本文介绍了 R1 一键准备功能"
tags: []
created: 2026-09-22T12:48:17.224Z
updated: 2026-09-22T12:48:18.543Z
source: https://wiki.bambulab.com/zh/r1/manual/measure-feature-introduction
---

## 概述

“一键准备”将加工前必须的多个准备动作按当前加工模式自动串联执行，省去逐一手动点击的重复操作，提高作业效率与准确性。您只需点击一次，系统便会依次完成拍照、官方材料识别（带二维码）、测距、扫描测量或滚轮送料相关的动作，并将最新结果实时刷新显示在软件界面上。

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/001.png)

## 适用的加工模式

一键准备的具体行为取决于用户在 Bambu Suite 中手动选择的加工模式：

| **加工模式** | **自动执行的动作序列** |
| --- | --- |
| **平面加工** | ① 拍照 → ② 识别轮廓 → ③ 扫描测量 |
| **曲面加工** | ① 拍照 → ② 识别轮廓 → ③ 扫描测量 |
| **圆柱/旋转体加工** | ① 扫描测量 → ② 拍照 |
| **滚轮送料加工** | ① 夹紧材料 → ② 测量距离 → ③ 逐次拍照拼接 → ④ 扫描测量 |

> 各动作的详细原理、参数设置与注意事项，请参见对应的独立功能页面（拍照、测高、扫描测量等）。本页重点介绍一键准备的整体流程与组合使用方法。

## 如何使用一键准备功能

### **确认加工模式**

在 Bambu Suite“准备制作”页面，确认当前已切换至所需的加工模式（平面 / 曲面 / 滚轮送料）。

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/002.png)

### **执行一键准备**

- 点击加工盘上方工具栏中的“**一键准备”** 按钮。

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/003.png)

- 点击后无二次确认弹窗，将直接开始执行流程；界面进度条会显示当前执行的步骤及进度。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/004.png)

所有动作完成后，系统会将以下获取到的最新信息自动更新至准备页面：

- 加工区域背景图像（俯视照片 / 曲面点云 / 全景图）
- 材料信息（必须是带二维码的官方材料）
- 加工距离测量值
- 滚轮送料模式下的材料总长度

> 处理期间请勿关闭打印机电源或使电脑进入休眠状态。

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/005.png)

### **加工前微调**

若对自动测量的结果不满意，例如在滚轮送料加工模式下，需要修改材料长度或距离，可直接在右侧信息栏中手动输入修正值。

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/006.png)

- **长度**： 支持手动修改；
- **距离**： 除手动输入外，若自动测距失败，还可使用独立的「**选点测距**」工具重新测距。

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/007.png)

## 各加工模式执行细节

### 平面加工

1. **拍照**

自动拍摄加工平面俯视图，该图像将作为背景辅助您拽图案进行对位，实现更准确的“所见即所得”摆盘。

![008.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/008.png)

2. **测量距离**

拍照完成后自动触发测距。系统采用自动测距方式：拍照后识别材料轮廓并取其中心点测量加工距离。测距结果会写入右侧信息栏的“距离”字段。

> 注意：若识别到多个材料，则无法自动测距，会提示用户进行选点测距；具体请参考 wiki：[R1 材料距离测量](material-thickness-measurement.md)。

|  |  |
| --- | --- |
| 009.png | 010.png |

#### 特殊情况说明

1. 如果希望得到和实际物体尽可能接近的图片，设备需要获取物体表面与工具头的正确距离。测量后，软件获得了物体上表面距离，并会自动调节对实际物体拍照的正确尺度。

![011.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/011.webp)

2. 在通过拍照识别材料轮廓中心寻找测量点时，由于系统此时尚未获知物体厚度，受光学透视效应影响，摄像头中识别出的轮廓中心与实际会产生一定的偏差。但只要物体表面平整，所确定的测量点则不会超出该平面范围，从而仍能计算出准确的距离数值，并生成对位精准的相机影像。

![image-center.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/image-center.png)

若您希望测量物体某个特点的位置，手动切换“选点测量” 或者 “手拖工具头测量” 模式，对目标区域进行手动测距。测距完成后，系统会自动完成图像调整。

![](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/009.png)

3. 对于带有孔洞的物体，系统默认选择最大面积的区域中心进行测量。若因测量点落入孔洞内而导致拍照或测距失败，您可以在拍照完成后，手动切换至 **“手拖工具头测量”** 模式，对目标区域进行手动测距。测距完成后，系统会自动完成图像调整。

|  |  |
| --- | --- |
| 013.png | 014.png |

### 曲面加工

1. **拍照**

获取加工区域背景图，用于后续框选曲面测量区域。

2. **扫描测量**

拍照后自动进入曲面测量环节。激光工具头将进行高精度曲面建模，生成点云数据，并在页面中显示物体的 3D 轮廓。该轮廓可用于精确的曲面加工对位。

![015.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/015.png)

### 圆柱/旋转体加工

自动进入圆柱/旋转体测量环节。激光工具头将进行高精度测量，并在页面中显示物体的 3D 轮廓，该轮廓可用于精确的圆柱/旋转体加工对位。

![017.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/017.png)

测量完成后，俯视摄像头随机拍照，机器获得圆柱/旋转体加工区域背景图；

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/016.png)

### 滚轮送料加工

滚轮送料加工模式专为**长板材连续加工**设计。

> 注意：“一键准备”按**固定顺序**执行以下四个动作，任何一个环节失败都会**终止操作**并报错，不会跳过执行。

1. **夹紧材料**

机器的压紧机构自动夹紧材料，内置传感器会确认夹紧到位。夹紧状态由系统自动控制，无需手动辅助。

|  |  |
| --- | --- |
| 018.png | 019.png |

2. **测量距离**

与平面模式类似，采用**自动测距方式**获取加工距离，用于激光对焦校准。

3. **逐次拍照拼接**

夹紧轴前后传送长木板，系统逐次拍摄当前机箱内的局部图像，并自动拼接成一幅完整的材料全景图。拼接结果将呈现在软件中的加工盘上，作为背景辅助您摆放加工对象、确认加工位置。拼接过程全自动完成，不支持手动调整。

![auto-passthrough-3.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/auto-passthrough-1.png)

4. **测量长度**

自动测量材料的总长度，测量原理详见：[快速测长功能](roller-feed-processing-quick-length-measurement.md)。结果展示在准备页面右侧信息栏的“长度”项中，支持用户手动修改，以便根据实际情况校正。

![022.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/022.png)

## 注意事项

- 透明、强反光或严重不平整的材料可能导致测量失败；
- 执行一键准备功能前，请先确认**材料已正确放置**在机箱中；
- 精细轮廓提取需在功能设置中提前配置，一键准备将沿用该配置；
- 曲面加工的“一键准备”功能会自动识别机箱内的所有目标物体，并选取会自动筛除小体积的物体，但如果机箱内有多个正常物体的话，还是会类似平面的操作，报识别到多物体，并回到图片界面，由用户手动框选扫描范围；如需测量特定区域，请使用独立的“框选选区测量”工具；
- 进行滚轮送料加工前，请确保**材料已正确装入**，且夹紧传感器工作正常。拼接图像仅用于加工对位参考，不可编辑拼接结果。

## 常见问题

### 功能容错与报错后处理

一键准备过程中，若任何步骤执行失败（如测距异常、拍照模糊、扫描中断等），界面会**弹出明确错误提示**，告知失败原因。用户可根据提示采取相应措施，例如：

- **测距失败：** 常见于材料未被识别，或视野中存在多块材料导致无法确定测量点。此时可点击“选点测量”手动指定测距位置，完成距离测量。
- **轮廓识别异常：** 请检查材料是否摆放妥当、上盖是否关好，根据提示调整后重试；如果是因为材料表面过于反光/透明，请将设备升级至最新版本固件后重试。

![023.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/023.png)

所有操作均会记录在**软件日志**中，联系客户服务或提交工单时可通过软件日志排查问题。

### 俯视摄像头拍照精度误差

正常情况下，机器在图上雕刻图案的位置，和软件里预览时摆放的位置偏差不会超过 \*\* 0.6mm\*\*；可以在加工完成后再次进行拍照，来判断实际雕刻位置与您设计的位置的偏差：

![024.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/024.png)

如果误差较大，请按照以下步骤处理：

1. 确认材料放置位置；
2. 将设备升级至最新版本的固件后重新拍照尝试；
3. 若对雕刻图案的对位精度有更高要求，可以尝试使用精细拍照功能，具体请参考此 wiki：[精细拍照介绍](fine-capture-guide.md)。

![025.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/measure-feature-introduction/zh/025.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
