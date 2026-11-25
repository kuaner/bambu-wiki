---
path: zh/p3c/maintenance/manual-bed-tramming
title: "P3C 手动调平"
description: ""
tags: []
created: 2026-11-24T14:06:30.435Z
updated: 2026-11-24T14:06:30.435Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/manual-bed-tramming
---

Bambu Lab 打印机的热床在出厂时已调整好，按照手册的指引操作完成后，即可直接打印。 但如果由于运输原因导致热床出现了异常，或因产品维修的需要，拆装或更换过热床，导致了热床自动调平失败，这时我们可能需要通过手动调平的方式来确保打印机的热床是平整的。

## 准备工作

### 所需工具：

- H2.0 内六角扳手
- 2 mm 辅助调平块（您可以使用其他高度为 2 mm 的垫块），该辅助工具可以在调平的时候将热端和热床之间保持一定距离，避免在手动调平过程中刮伤热床。  
  [附件：手动调平辅助块.3mf](https://wiki.bambulab.com/h3c/maintenance/manual-bed-tramming/zh/manual-bed-tramming-block.3mf)

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/001.png)

- 下载调平 G-code 后，您需要将 G-code 文件拷贝至 U 盘根目录。  
  [p3c\_manual\_bed\_end.gcode](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/p3c_manual_bed_end.gcode)

### 清洁热床及热端

- 取用打印头，确保喷嘴上没有任何残留塑料；如果需要，可加热热端后使用清洁海绵擦拭热端以确保其干净。

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/002.png)

- 移除打印板，并确保热床表面清洁。

![003.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/003.png)

### 锁紧热床调平螺丝

用手用力按压热床，观察调平螺丝是否还能拧紧。

![004.gif](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/004.gif)

锁紧调平螺丝，确保后续操作有足够调整空间。

|  |  |
| --- | --- |
| 005.gif | 006.gif |

热床上总共 4 个调平螺丝，都需拧紧。

![007.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/007.png)

## 开始调平

将调平 G-code 文件复制至 U 盘，并插入打印机的 USB 接口。设备识别后，屏幕会显示文件列表，选择调平用的 G-code 文件，点击“开始打印”。

![008.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/008.png)

首先，工具头会自动移动至左前方的调平点。此时请将辅助调平块插入热端与热床之间，通过旋转调平螺丝进行微调，直到热端刚好轻触调平块，并能感受到**轻微滑动阻力**，表示间隙合适。

> **温馨提示：顺时针是拧紧调平螺丝，会使热床与热端的距离增加；反之，逆时针是拧松调平螺丝，会使热床更加靠近热端。**

![009.gif](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/009.gif)

工具头会逐个探测热床的 4 个角，每个角会停留 30 秒，一共执行三轮（确保调平准确）。当观察到热床开始下降时，请及时抽出螺丝刀和调平模型。

![010.gif](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/010.gif)

依次对热床四角的调平螺丝进行微调，**确保四个调平点在滑动调平块时所感受到的阻力一致**，以保证热床整体水平。

![011.gif](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/011.gif)

该 G-code 文件会执行 3 轮调平循环，即每个角的调平点将重复 3 次，您有多次机会进行微调以达到更高精度。建议完整执行所有三轮调平，以确保最终效果稳定可靠。

> 当调平任务结束，但热床未完成调平。此时您需要再次拧紧 4 颗调平螺丝，重复运行 G-code。

## 设备校准

在打印机屏幕中点击 **设置 > 校准 > 打印校准 > 自动热床调平**，开始进行校准。 如果一切正常，并且校准过程中没有出现错误或警告，则调平成功。如果仍有问题，请联系服务团队寻求进一步帮助。

![012.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/manual-bed-tramming/zh/012.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
