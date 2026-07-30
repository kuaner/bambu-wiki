---
path: zh/a2l/maintenance/manual-bed-tramming
title: "A2L 热床手动调平"
description: "本文介绍了如何对 A2L 热床进行手动调平"
tags: []
created: 2026-06-01T13:25:09.244Z
updated: 2026-07-17T02:21:16.141Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/manual-bed-tramming
---

Bambu Lab 打印机的热床在出厂前已经过精确校准，通常情况下无需额外调整即可直接进行高质量打印。然而，在某些特定情况下，如长途运输导致的意外位移，或因产品维修需求（如拆装或更换热床）调整过热床螺丝，那么可能需要通过**手动调平**的方式，重新确定打印热床的平整度，为打印成功奠定基础。

## 所需工具

- U 盘
- H2.0 内六角螺丝刀
- 调平辅助模型：[手动调平辅助块.3mf](https://public-cdn.bblmw.com/wiki/new/a2l/fuzhu.3mf)
- 调平 G-code 文件：[Manual\_bed\_screws\_adjust\_assist.gcode](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/manual_bed_screws_adjust_assist.gcode)

## 手动调平流程

### 取下打印板

取下热床上的打印板，露出热床调平螺丝。

![plate.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/plate.jpg)

### 预紧调平螺丝

在热床右侧找到 2 颗锁紧螺丝，拧松 2-3 圈。

![screw1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/screw1.jpg)

按压热床，确保锁紧螺丝不再卡住热床。

![bedtest.webp](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/bedtest.webp)

找到热床上方的 4 颗调平螺丝，使用 H2.0 内六角螺丝刀将这 4 颗可调螺丝全部拧紧至底部（顺时针拧到底）。

> 由于手动调平过程需要人为调整每个角的螺丝位置，为了确保每个螺丝都有足够的调整空间，必须先将 4 个调平螺丝全部锁紧（拧到底），有助于后续调整。

![compressedscrew.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/compressedscrew.jpg)

### 运行 G-code 文件

将手动调平 G-code 文件下载至 SD 卡，并插入打印机中。点击打印文件，屏幕会显示文件列表，选择下载的 G-code 文件，点击“打印”。

![screen1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/screen1.jpg)  
![screen2.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/screen2.jpg)  
![screen3.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/screen3.jpg)

工具头首先会自动移动至热床的左前方调平点。此时，请将模型插入喷嘴与热床之间。并且**拧松该位置对应的调平螺丝**，直到您感觉喷嘴刚好轻微触碰到模型，并且在抽动模型时能感受到**轻微的滑动阻力**，这表示喷嘴与热床之间的间隙大概就在 2mm 左右。若阻力过大，请稍微拧紧一点调平螺丝。

![manualtramming.webp](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/manualtramming.webp)

> **注意：当您发现工具头开始主动上升时，请务必停止调平的动作并移走内六角扳手，因为此时工具头会开始移动到下一个位置。**  
> ![move.webp](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/move.webp)

接下来，工具头会自动移动至右前方、右后方、左后方调平点。重复上述相同步骤，将模型插入喷嘴与热床之间，并**相应调整此处的调平螺丝**，确保喷嘴和模型之间有合适的接触与轻微的移动阻力。

![position2.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/position2.jpg)

该 G-code 文件会执行 **3 轮循环**，即每个调平点您将有 3 次机会进行微调。这意味着您有多次机会精细调整。为确保最终调平效果稳定可靠，**建议您完整执行所有三轮调平循环**。

完成整个流程后重新拧紧热床右侧的 2 颗锁紧螺丝。

![screw1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/screw1.jpg)

## 打印机校准

将打印板（如 PEI 板）重新安装到热床上，确保其尾部刚好卡入限位槽，固定稳妥。

|  |  |
| --- | --- |
| installplate1.jpg | installplate2.jpg |

点击打印机屏幕上的“设置”图标，进入校准界面。选择“自动热床调平”选项，并点击“开始”。打印机将自动进行热床的网格调平校准，记录各点的精确高度数据。

![bedlevelone.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/bedlevelone.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
