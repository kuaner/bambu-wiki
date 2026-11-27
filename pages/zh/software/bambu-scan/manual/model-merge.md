---
path: zh/software/bambu-scan/manual/model-merge
title: "模型/点云拼接技巧"
description: ""
tags: []
created: 2026-11-26T14:02:02.419Z
updated: 2026-11-27T01:46:45.746Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/manual/model-merge
---

## 模型拼接

大多数物体难以一次性完成全部扫描，往往需要分段对不同面进行采集，然后将多次获取的点云数据拼接合并，得到完整点云数据，进而转化为一个完整的的三维模型。

#### 自动拼接

自动拼接分为特征拼接与标记点拼接。

1. 特征拼接

软件将识别导入点云的特征，并根据特征自动拼接点云。([模型来源](https://makerworld.com.cn/zh/models/175930-zhen-shi-de-discobolusfu-zhi-pin-diao-su-discobolo#profileId-94215))

有多个文件时，可全选所有点云，然后预览拼接。

![001.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/model-merge/zh/001.jpg)

若全选拼接失败，尝试按物体的“前-右-后-左-上-下”（仅供参考，确保过渡连贯即可）的顺序，每次仅拼接两个点云。拼接完毕后，点击预览拼接。若拼接无误，再选择“锁定并拼接下一个”或右上角的“应用”。

![002.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/model-merge/zh/002.jpg)

若某个面一直无法自动拼接，比如从“左”到“上”时拼接错误，可暂时选择“应用”，保存已经拼接完成的文件。退出拼接页面后新建扫描，再次扫描物体“左上方”。

![003.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/model-merge/zh/003.jpg)

扫描完毕后再回到拼接，选择已经拼接的文件以及新扫描的文件。

![004.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/model-merge/zh/004.jpg)

若拼接无误，再选择“锁定并拼接下一个”，直到所有点云都完成拼接。

![005.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/model-merge/zh/005.png)

2. 标记点拼接

在物体表面粘贴标记点进行扫描时，可使用“标记点拼接”。

|  |  |
| --- | --- |
| 006.png | 007.png |

软件将根据标记点的坐标分布，自动拼接不同面的点云文件。预览无误后，可选择“锁定并拼接下一个”或右上角的“应用”。

|  |  |
| --- | --- |
| 008.png | 009.gif |

#### 手动拼接

该方法每次仅能处理两个点云文件，需要手动选择两个点云文件中的相似特征，最少需要 3 组配对点，但配对点数量越多，覆盖角度越大，拼接的准确性就越高。

|  |  |
| --- | --- |
| 011.png | 012.png |

> 注意：
>
> 1. 两个点云中的配对点大致对齐特征即可，软件将自动优化处理。
> 2. 建议在两份点云的重叠区域内选择 **4–5 组配对点**。每组点应对应物体上的同一处特征，各组之间尽量分散，避免集中在一处或部位
>
> ![010.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/model-merge/zh/010.png)

若某个位置出现较大偏差，可在该处多选择几对配对点。

|  |  |
| --- | --- |
| 013.png | 014.png |

预览无误后，可选择“锁定并拼接下一个”或右上角的“应用”。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
