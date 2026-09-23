---
path: zh/r1/manual/material-thickness-measurement
title: "R1 材料距离测量"
description: "本文介绍了 R1 材料距离测量功能"
tags: []
created: 2026-09-22T12:48:05.982Z
updated: 2026-09-22T12:48:07.277Z
source: https://wiki.bambulab.com/zh/r1/manual/material-thickness-measurement
---

## 材料距离测量介绍

R1 采用光学镜组进行材料距离测量，准确的测距可以用来在加工时通过激光对焦获得最佳切割焦距。

![material-measure.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/material-measure.png)

测量时，需要保证**测距激光**（虚线处）打在材料表面，测量后显示的距离值为**工具头下表面**（上直线）到**材料上表面**（下直线）的距离。

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/002.png)

## 可测量的材料种类

1. **非透明材料：** 木材、软木、卡纸、皮革等；
2. **透明材料**：透明亚克力和玻璃，包括带颜色的透明材料。

> **注意**：**不支持红色透明材料**；因为红色材料会吸收大部分蓝色激光，导致测量时激光几乎不可见，从而影响测量效果。

## 测量方式

### 一键准备测量

1. 点击 **“一键准备”** 按钮，机器将自动拍照，并基于识别到的材料轮廓选择中心测量。

> 若识别到多个材料，则无法自动测量，会提示用户进行选点测量，请参考后文“选点测量”。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/004.png)

2. 一键准备结束后，会自动将测得的材料长度填进距离方框中。

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/005.png)

### 选点测量

1. 在右侧材料组面板中，选择测量方式为“选点测量”；

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/006.png)

2. 在画布中选定某个具体位置，工具头会移动到该点上方，通过测距激光测量该处板材上表面高度，得出距离；

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/007.png)

3. 测量完成后，距离值自动回填到软件，设备复位以支持下一次测量。

![008.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/008.png)

**注意事项**

- 请尽量将测量点选在板材表面平整、无异物、无孔洞的位置，避免选在板材边缘，以提高测量成功率与准确；
- 透明或强反光材质可能导致测量异常，请谨慎确认结果或改为手动输入。

### 手拖工具头测量

1. 在右侧材料组面板中，选择测量方式为“手拖工具头测量”；

|  |  |
| --- | --- |
| 009.png | 010.png |

2. 根据页面提示，手拖工具头到想要测量的位置，suite 画布上会同步显示红色十字光标，标示当前工具头在可测量区域内的位置；

|  |  |
| --- | --- |
| 011.png | 012.png |

3. 按下机器“启停按钮”，机器会开始测量；

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/013.png)

4. 测量完成后，suite 会显示距离值；

![014.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/014.png)

5. 点击“应用距离”，即可自动填到当前材料的测量参数；如需重新测量，请点击“重新选点”。

![015.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/015.png)

**限制与前提条件**

- 主要用于**平面加工**和**滚轮送料加工**模式，其他模式需使用对应的测量方式；
- 若设备已装载**旋转轴组件**，则无法使用测量功能，须先拆卸旋转轴组件；
- 部分机型可能不支持，具体是否显示该测量方式，取决于机型配置；
- 设备测量过程中请勿移动材料，避免测量失败或数值偏差。

### 触碰测量

触碰测量的原理是通过气嘴碰撞工件进行高度的计算，触碰测量的触发有两种模式：

1. **自动切换触发：**

在一键准备或选点测量等环节中，机器识别到工况复杂且材料为透明物体，若视觉测量失败，则会自动切换为触碰测量；但在手拖工具头测量流程中，不会自动切换至触碰测量。

2. **手动触碰测量：**

- 在右侧材料组面板中，选择测量方式为“触碰测量”；

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/016.png)

- 通过手拖工具头的方式将工具头气嘴对准需要测量的位置，然后按下启停按钮，机器会通过气嘴触碰材料表面进行测量；

![contact-mearuse.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/contact-mearuse.webp)

- 测量结束后，suite 会自动显示测量值；

![018.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/018.png)

**注意事项**

- 触碰测量前需**确保气嘴在位；** 如果未安装气嘴，则会导致透明材料测量有误；

![019.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/019.png)

- 请勿使用太薄的物体进行触碰测量，且测量时，气嘴点位需放在物体中心，不要放在物体边缘，否则容易造成物体移动（如下图）；

![020.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/020.webp)

- 请勿将物体放在齿条面以下的位置（如托盘或底板）进行触碰测量。

![021.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/021.png)

- 使用太软的材料会导致触碰异常，因此请勿使用该方法测量软材料。

## 常见测量失败原因

### **材料距离超出加工范围**

当材料距离超过 79.73 mm 时，软件会判定为测量异常。该情况通常可能出现在使用增高架时，把较薄材料直接放置在托盘上，从而使材料表面距离工具头太远。

![022.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/022.png)

### 手拖工具头测量失败

如果材料为高透明、高反光，或者测量点不在物体表面，那么“手拖工具头测量”的非接触测量方式可能会失败，请手动选择 **“触碰测量”**，进行测距操作。

![023.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/023.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
