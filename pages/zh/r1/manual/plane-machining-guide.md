---
path: zh/r1/manual/plane-machining-guide
title: "R1 平面加工指南"
description: "本文介绍了如何进行 R1 平面加工"
tags: []
created: 2026-09-22T12:47:50.576Z
updated: 2026-09-22T12:47:51.835Z
source: https://wiki.bambulab.com/zh/r1/manual/plane-machining-guide
---

## 平面加工介绍

平面雕刻是 Bambu Lab R1 的一项核心加工功能，它利用高精度激光模组，实现在平面材料上进行图案雕刻与切割。加工前，通过俯视摄像头拍照，实现“所见即所得”的对位加工，并确保激光在材料表面精确对焦。

常见应用场景：在木板、亚克力、纸张、皮革等平面材料上雕刻文字/图案、制作标牌和装饰品，或进行板材的激光切割成型。

|  |  |
| --- | --- |
| 001.png | 003.png |

平面加工模式支持三种激光加工工艺：**激光线条雕刻**、**激光填充雕刻**和**激光线条切割**。

> 注意：同一加工任务中可混合使用不同工艺（需在软件内分别配置各图案的工艺参数）。

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/005.png)

本文以**激光填充雕刻**为例，介绍具体的加工步骤。

## 平面雕刻材料要求

在加工平面物体之前，要确保材料材质符合要求，具体请参考：[可加工材料清单](processable-materials-list.md)。

## 平面加工流程

### **添加图案并选择加工模式**

- 在设计页面导入或者创建要加工的图案（支持 SVG、PNG 等格式）；

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/006.png)

- 选择需要的工艺类型；

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/007.png)

- 点击右下角“准备制作”；

![008.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/008.png)

- 在加工模式中选择“平面加工”（默认模式）。

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/009.png)

### **拍照和测量**

- 打开上盖，放置需要加工的材料；

> 注意：
>
> - 确保材料最高点不高于气嘴高度，防止碰撞；
> - 待加工材料应稳固放置于机箱中央，避免晃动。

![010.jpg](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/010.jpg)

- 点击“一键准备”按钮 / 使用平面自动模式，机器会自动进行拍照和距离测量；

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/011.png)

- 完成后，界面会出现加工区域背景图像和距离测量值；如果使用的是带有二维码的官方材料，则机器会自动识别材料类型。

![012.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/012.png)

### 加工设置

- 在准备页面，将图案拖至材料的可加工区域，并确认其放置位置和最终的加工效果；

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/013.png)

- 设置激光功率、速度和次数；如果使用的是官方材料，可直接使用对应材料的参数；如果使用的是第三方材料，建议进行材料加工参数标定，具体请参考后文【平面加工注意事项——参数调试】；

![014.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/014.png)

- 点击右下角“制作”，软件会将加工任务发送至打印机，即可开始加工。

![015.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/015.png)

### 加工后检查

加工完成后，可检查图案清晰度和加工精确度。若效果不理想，可调整参数后重新雕刻。

## 平面加工注意事项

### 参数调试

由于实际制作过程中可能涉及**非标准材料**，官方未提供固定参数，因此我们建议：

- 可先选择材料较为接近的官方材料参数进行测试（如加工金属可选择不锈钢吊牌的加工参数）
- 若官方参数未能满足加工需求，可使用边角料进行标定矩阵测试。在同一物体上测试不同功率/速度组合，记录最佳参数，并在材料组的左下角点击“新建材料”，将其保存方便后续使用。具体请参考：[Bambu Suite 材料参数标定、录入和加工优化指导](../../h2/software/bambu-suite/manual/material-parameter-calibration-and-machining-optimization.md)。

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/plane-machining-guide/zh/016.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
