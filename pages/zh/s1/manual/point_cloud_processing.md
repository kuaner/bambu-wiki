---
path: zh/s1/manual/point_cloud_processing
title: "点云编辑"
description: ""
tags: []
created: 2026-11-26T14:00:39.030Z
updated: 2026-11-26T14:00:39.030Z
source: https://wiki.bambulab.com/zh/s1/manual/point_cloud_processing
---

## 介绍

点云编辑主要用于清理多余点云，并将多个扫描点云拼接为一个整体。拼接前以及拼接后，都能够根据实际的扫描情况“新建扫描”，补充缺失部分。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image_6.png)

### 点云清理

使用“套索/多边形/矩形/裁切”工具，删除多余的点云。

> 其中，多边形框选后需双击确定。

![PixPin_2026-10-09_18-12-52.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/pixpin_2026-10-09_18-12-52.gif)

![pixpin_2026-10-09_18-14-20.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/pixpin_2026-10-09_18-14-20.gif)

### 离群项

软件会自动检测散布较为稀疏的孤立点或未相连的点云。通过调节识别敏感度，可以改变检测等级，从而更精准地剔除这些噪声点。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image_1.png)

![PixPin_2026-10-09_18-13-34.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/pixpin_2026-10-09_18-13-34.gif)

### 拼接

#### 自动拼接

1. 特征拼接

软件将自动识别导入的点云特征，并根据特征自动拼接点云。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image_2.png)

点击预览拼接，若拼接无误，可选择“锁定并拼接下一个”或右上角的“应用”。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image_3.png)

2. 标记点拼接

在物体表面粘贴标记点进行扫描时，可使用“标记点拼接”。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image_5.png)

软件将根据标记点分布，自动拼接点云。预览无误后，可选择“锁定并拼接下一个”或右上角的“应用”。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image.png)

#### 手动拼接

该方法需要手动标记两个点云中的相似特征，配对点数量越多，覆盖角度越大，拼接的准确性就越高。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image_4.png)

预览无误后，可选择“锁定并拼接下一个”或右上角的“应用”。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image_8.png)

### 新建扫描

拼接完成后可检查生成的点云是否存在漏缺，若仍需补充可继续“新建扫描”，再按照相同方式拼接。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/point_cloud_processing/image_7.png)

## **结束语**

>我们希望本指南能为您提供有用的信息，帮助您解决问题。  
>如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
>如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
