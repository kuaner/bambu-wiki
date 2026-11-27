---
path: zh/software/bambu-scan/manual/thin-walled-object
title: "薄壁件扫描技巧"
description: ""
tags: []
created: 2026-11-26T14:02:02.219Z
updated: 2026-11-27T01:59:43.726Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/manual/thin-walled-object
---

## 原理

扫描过程中，软件需要利用纹理、几何或标记点等特征，判断扫描仪与物体的相对位置，并将采集到的点云对齐。当扫描仪移动到薄壁件的侧面时，物体在画面中的**区域变窄**，可**识别特征**减少，容易出现**跟踪丢失**。

因此，对于薄壁物体来说，需要在“变窄处”搭建一个“特征足够”的背景，满足侧壁扫描需求。

![001.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/thin-walled-object/zh/001.png)

## 安全提示

> 本设备采用红外散斑与蓝色激光双光源进行三维扫描。其中，**红外散斑及平行线模式下的蓝色激光处于安全水平**，在对应模式下扫描人体或人脸时无需闭眼或做特别防护。  
> 其余蓝色激光模式符合 **Class 2（Ⅱ类）** 激光安全标准，强烈建议**避免长时间刻意直视激光束或其镜面反射光，同时避免或直接扫描人体**。  
> 扫描过程中投射的激光图案可能呈现闪烁或移动效果。患有光敏性癫痫或相关疾病、或对闪烁光敏感的用户，**建议避免注视扫描光束及其投射图案**，并在使用前咨询医生。若使用过程中感到头晕、视觉不适，请立即停止扫描并离开光照区域。

## 背景物选取

1. 带有标记点的标准柱（使用标记点扫描时）。
2. 较高的常规物体（本文以该方法为例）。

![002.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/thin-walled-object/zh/002.png)

## 扫描过程

根据主要物体选择合适的预设。

![003.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/thin-walled-object/zh/003.png)

开始扫描前，画面视角需要对准背景物和主体，再按下“黄色确认键”。若一开始对准薄壁，扫描仪可能无法识别。

![004.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/thin-walled-object/zh/004.png)

同时扫描背景物和主体。

![005.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/thin-walled-object/zh/005.png)

正面的细节扫描完毕后，视角对准背景物，缓慢移动至薄壁背面。

![006.webp](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/thin-walled-object/zh/006.webp)

调整扫描仪正对背面，扫描细节。

![007.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/thin-walled-object/zh/007.png)

剩余的边缘位置可围绕主体移动扫描仪，逐步补充细节。

![008.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/thin-walled-object/zh/008.png)

## 后处理

扫描完毕后的处理步骤与《首次使用》相同，若您首次使用扫描仪，可跳转到《[首次使用教程](../../../s1/manual/first-scan.md)》。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
