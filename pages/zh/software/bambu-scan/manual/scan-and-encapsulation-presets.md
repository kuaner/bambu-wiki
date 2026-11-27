---
path: zh/software/bambu-scan/manual/scan-and-encapsulation-presets
title: "扫描预设以及封装预设"
description: ""
tags: []
created: 2026-11-26T14:01:57.617Z
updated: 2026-11-27T01:57:31.038Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/manual/scan-and-encapsulation-presets
---

长久以来，关于扫描参数和封装网格参数的选择持续困扰着用户，实际扫描物体时，用户需要充分考虑物体的尺寸、材质特性、精细度等要求并合理设置扫描模式、拼接方式、激光强度等参数，才能得到想要的扫描结果。我们充分借鉴了Bambu Studio和Suite中预设概念，推出面向3D扫描的预设系统来简化扫描流程。Bambu Scan的预设系统分为扫描预设和封装预设两个部分。

## 扫描预设

扫描预设是针对扫描时的参数集合，目前分为智能推荐和快速场景两种，分别适用于扫描新手以及对扫描已经有一定了解的用户。

### 智能推荐

智能推荐系统是通过一系列选项回答，引导用户得到一套合适的参数和提示，来帮新手用户开始一次扫描。用户可以根据其实际被扫描物体的特征进行回答。

![001.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/scan-and-encapsulation-presets/zh/001.png)

部分情况下还需要处理扫描物体表面，可在右侧栏中了解。

|  |
| --- |
| 002.png |

### 默认预设

除了智能推荐以外，我们还内置了一部分扫描预设来满足快速选择。扫描预设的详细参数介绍，可阅读[扫描介绍](../../../s1/manual/scan.md)。

![004.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/scan-and-encapsulation-presets/zh/004.png)

### 自定义预设

如果希望参数更加自由，可以在修改后现有预设后，点击右上角的保存按钮，将其另存为一个自定义预设。

![005.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/scan-and-encapsulation-presets/zh/005.png)

随后在自定义预设下即可进行使用。

![006.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/scan-and-encapsulation-presets/zh/006.png)

## 封装预设

封装预设是针对点云完成后，从点云生成网格时所需要的参数集合。我们目前内置了5种预设，满足不同场景的使用需求。具体参数介绍可阅读[网格编辑](../../../s1/manual/grid_processing.md)。

- **人脸/四肢**：适用于人体相关扫描的点云数据封装。
- **通用**：默认对网格进行适当的简化和少量平滑，适用于绝大部分场景的点云数据封装。
- **细节优先**：进一步降级简化，保留点云细节，适用于微小物体的表面封装。
- **3D打印**：优先封装为全封闭网格，适用于3D打印使用的场景。
- **保留真实**：不做任何额外的网格优化操作，适用于追求原始数据效果的用户。

![007.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/scan-and-encapsulation-presets/zh/007.png)

### 自定义封装预设

同扫描预设，可在修改现有封装预设后，保存为单独的自定义封装预设并使用。

|  |
| --- |
| 008.png |

## 预设管理

对于需要导出和导入的预设，可点击左上角菜单栏-文件-预设管理，可对扫描预设和封装预设进行导入、导出，及批量删除处理。

|  |  |
| --- | --- |
| 010.png | 011.png |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
