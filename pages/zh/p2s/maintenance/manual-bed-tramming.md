---
path: zh/p2s/maintenance/manual-bed-tramming
title: "P2S & X2D 热床手动调平"
description: "本文将详细为您介绍 P2S 和 X2D 打印机手动调平的步骤与流程。"
tags: []
created: 2025-10-14T13:20:21.353Z
updated: 2026-04-27T07:52:59.261Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/manual-bed-tramming
---

Bambu Lab 打印机的热床在出厂前已经过精确校准，通常情况下无需额外调整即可直接进行高质量打印。然而，在某些特定情况下，如长途运输导致的意外位移，或因产品维修需求（如拆装或更换热床）引发的自动调平失败，此时我们可能需要通过**手动调平**的方式，来确保打印热床的平整度，为打印成功奠定基础。

## 视频指南

## 所需工具

在开始手动调平前，请您准备好以下工具：

- **H2.0 内六角螺丝刀：** 用于调整热床下方的调平螺丝。
- **A4 纸：** 作为测量喷嘴与热床间隙的校准介质。
- **U 盘**
- **调平 G-code 文件：** 为 P2S/X2D 手动调平设计的打印指令文件，用于引导工具头移动到预设的调平点。

> [X2D 手动调平 G-code 文件](https://public-cdn.bblmw.com/wiki/new/x2d/first-layer-printing-optimization-guide/x2d_manual_bed_screws_adjust_assist.gcode)  
> [P2S 手动调平 G-code 文件](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/p2s_manual_bed_screws_adjust_assist.gcode)

## 手动调平流程

1. **移除打印板：** 首先，将热床上的打印板（如 PEI 板或工程板）完全移除，以直接接触热床本体进行调平。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/010.png)

2. **预紧调平螺丝：** 找到热床上方的三颗调平螺丝（请注意，**右后方的螺丝通常是锁定死的，无需调整**）。使用 H2.0 内六角螺丝刀将这三颗可调螺丝全部拧紧至底部（顺时针拧到底），并尽量调整至螺丝的中间位置，避免与热床上的螺丝孔出现过度偏心。在锁紧过程中，建议用手捏住热床底部进行感知，确保螺丝已完全拧紧，无任何松动。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/005.png)

> 为什么需要锁紧？
>
> 由于手动调平过程需要人为调整每个角的螺丝位置，为了确保调平起点一致，必须先将3个调平螺丝全部锁紧（拧到底），此时热床与喷嘴间距离为最远值，有助于统一初始状态。

3. 将手动调平 G-code 文件（如下附件所示）复制至 U 盘，并插入打印机的 USB 接口。点击打印文件，屏幕会显示文件列表，选择调平用的 G-code 文件，点击“开始打印”。

|  |  |
| --- | --- |
|  |  |

> 运行 G-code 文件后，打印头（工具头）会首先进行回中操作。随后，它将按预设顺序逐个移动并探测热床的三个可调支撑点（三个点即可确定一个平面）。在每个调平点，工具头会停留约 **30 秒**，以便您有充足时间进行调整。整个程序会**一共执行三轮循环**，以确保调平的精确性和稳定性。

4. 工具头首先会自动移动至热床的左前方调平点。此时，请将 A4 纸（标准厚度约 0.1mm）插入喷嘴与热床之间。通过**调节该位置对应的热床调平螺丝进行微调**，直到您感觉喷嘴刚好轻微触碰到 A4 纸，并且在抽动纸张时能感受到**轻微的滑动阻力**，这表示喷嘴与热床之间的间隙已达到适合打印的标准。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/007.webp)

**顺时针是拧紧调平螺丝，会使热床与喷嘴的距离增加；反之，逆时针是拧松调平螺丝，会使热床更加靠近喷嘴。**

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/006.png)

> **注意：当您发现热床开始主动下降时，请务必停止调平的动作并移走内六角扳手，因为此时工具头会开始移动到下一个位置。**

5. 接下来，工具头会自动移动至右前方调平点。请重复上述相同步骤，将 A4 纸插入喷嘴与热床之间，并**相应调整此处的调平螺丝**，确保喷嘴和纸张之间有合适的接触与轻微的移动阻力。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/001.gif)

6. 最后，工具头会移动至热床的左上方调平点。请再次重复调整螺丝的步骤，**确保该点的喷嘴与 A4 纸之间同样存在合适的间隙与阻力**。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/008.png)

该 G-code 文件会执行共 **3 轮完整的调平循环**，即每个调平点您将有 3 次机会进行微调。这意味着您有多次机会进行精细调整以达到更高的调平精度。为确保最终调平效果稳定可靠，**建议您完整执行所有三轮调平循环**。

## 打印机校准

手动调平完成后，为了使打印机内部的自动调平系统与您的手动调整结果同步并发挥最佳效能，需要再次对打印机执行**自动校准**。

将打印板（如 PEI 板）重新安装到热床上，确保其尾部刚好卡入限位槽，固定稳妥。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/004.png)

点击打印机屏幕上的“设置”图标，进入校准界面。选择“自动热床调平”选项，并点击“开始”。打印机将自动进行热床的网格调平校准，记录各点的精确高度数据。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/manual-bed-tramming/009.png)

完成以上所有步骤后，您的 Bambu Lab P2S/X2D 打印机热床已完成手动调平和自动校准，您现在可以进行打印测试，以验证调平效果。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
