---
path: zh/a1/maintenance/manual-bed-tramming
title: "A1 热床手动调平"
description: "介绍如何对 A1 的热床进行手动调平"
tags: ["a1", "热床"]
created: 2023-12-09T12:13:58.365Z
updated: 2025-03-30T14:12:25.095Z
source: https://wiki.bambulab.com/zh/a1/maintenance/manual-bed-tramming
---

Bambu Lab A1 打印机的热床在出厂时是已调整好的，按照手册的指引操作完成后，即可直接打印。 但如果由于运输原因导致热床出现了异常，或因产品维修的需要，拆装或更换过热床，导致了热床自动调平失败，这时我们可能需要通过手动调平的方式来确保打印机的热床是平整的。

手动调平专用Gcode ：[a1\_manual\_bed\_screws\_adjust\_assist.gcode](https://wiki.bambulab.com/a1/maintenance/bed-tramming/a1_manual_bed_screws_adjust_assist.gcode)

## 调平前的准备

在开始热床手动调平之前，准备工作很重要：

1. 移除热端硅胶套，并检查喷嘴，确保喷嘴清洁且喷嘴上没有材料附着；

![](https://wiki.bambulab.com/a1/maintenance/bed-tramming/clean_nozzle.jpg)

2. 将热床底下的 2 颗锁定螺丝拧松；

![](https://wiki.bambulab.com/a1/maintenance/bed-tramming/2_screws.jpg)

3. 移除打印板，清理热床表面的异物，并将热床调平螺丝（共 3 颗）各顺时针拧紧 1 圈，或拧到与底部支架平齐的状态（可以用手触碰来确认位置）。

|  |  |
| --- | --- |
|  |  |

## 开始调平

首先，请将[调平 Gcode](https://wiki.bambulab.com/a1/maintenance/bed-tramming/a1_manual_bed_screws_adjust_assist.gcode) 下载到 SD 卡中，将装有调平 Gcode 的 SD 卡插入打印机，然后开启打印机电源。

待机器完成启动并能成功识别文件后，选中上述 Gcode 文件，点击开始打印。

> **注意：A1 不支持热插拔 SD 卡，请关闭电源后再插拔 SD 卡。**

|  |  |
| --- | --- |
|  |  |

运行 Gcode 文件后，打印机将进行回中操作，然后移至热床左前方并等待 30 秒。这时，您可以用内六角扳手拧动热床调平螺丝，将喷嘴调成贴近热床的状态。

![](https://wiki.bambulab.com/a1/maintenance/bed-tramming/p1.jpg)
> **温馨提示：顺时针是拧紧调平螺丝，会使热床与喷嘴的距离增加；反之，逆时针是拧松调平螺丝，会使热床更加靠近喷嘴。**

|  |  |  |
| --- | --- | --- |
|  |  |  |

可使用一张纸垫在喷嘴和热床之间，以检测热床与喷嘴之间的距离。

> **注意：当您发现中喷嘴开始主动抬升时，请务必停止调平的动作并移走内六角扳手，因为工具头要开始移动了。**

（30 秒后）喷嘴将移动到热床右前方， 重复调整操作，使得热床刚好不接触喷嘴。然后是热床左后方，按同样的方法完成调整。

|  |  |
| --- | --- |
|  |  |

当第一次调平完成后，该过程将再会重复两次，以便您微调并仔细检查喷嘴和热床之间的距离。整个 Gcode 的运行时间约 8 分钟。

确认完成调整后，最后请将锁定热床的 2 颗螺丝拧紧。

## 操作视频

## 热床手动调平失败处理方案

如果您在实际的操作中，发现无法完成手动调平，使三个测试点都同时实现喷嘴与热嘴贴近的状态，建议您进行如下操作：

1. 确认侧面的两颗热床锁定螺丝有在原位，并处于拧松的状态；

![](https://wiki.bambulab.com/a1/maintenance/bed-tramming/2_screws.jpg)

2. 将 3 颗调平螺丝都同时顺时针拧到底，然后，**左侧 2 颗逆时针拧松 3 圈，右侧 1 颗只逆时针拧松 1 圈**；

![](https://wiki.bambulab.com/a1/maintenance/bed-tramming/readjust_the_screws.png)

3. 运行 Gcode 开始手动调平。

![](https://wiki.bambulab.com/a1/maintenance/bed-tramming/file.jpg)

## **设备校准**

在打印机屏幕中点击 **设置 > 维护 > 校准**，开始进行校准。 如果一切正常，并且校准过程中没有出现错误或警告，则调平成功。如果仍有问题，请联系服务团队寻求进一步帮助。

![](https://wiki.bambulab.com/a1/maintenance/heatbed/20250115-171322.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
