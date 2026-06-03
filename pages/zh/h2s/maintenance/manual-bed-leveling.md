---
path: zh/h2s/maintenance/manual-bed-leveling
title: "H2S 热床手动调平"
description: ""
tags: []
created: 2025-08-24T12:58:45.757Z
updated: 2026-02-05T03:12:13.179Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/manual-bed-leveling
---

Bambu Lab H2S 打印机的热床在出厂时是已调整好的，按照手册的指引操作完成后，即可直接打印。 但如果由于运输原因导致热床出现了异常，或因产品维修的需要，拆装或更换过热床，导致了热床自动调平失败，这时我们可能需要通过手动调平的方式来确保打印机的热床是平整的。

## 调平前的准备

在开始热床手动调平之前，准备工作很重要：

### 所需工具：

具有 90 度弯折的 H2.0 内六角扳手（如果可以使用棘轮扳手会更加省力）。

![](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E5%86%85%E5%85%AD%E8%A7%92%E6%89%B3%E6%89%8B.jpg)  
![](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E6%A3%98%E8%BD%AE.jpg)

打印 2mm 辅助调平块(您可以使用其他高度为 2mm 的垫块)，该辅助工具可以在调平的时候将喷嘴和热床之间保持一定距离避免在手动调平过程刮伤热床。

[手动调平辅助块.3mf](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E6%89%8B%E5%8A%A8%E8%B0%83%E5%B9%B3%E8%BE%85%E5%8A%A9%E5%9D%97.3mf)  
![配件.jpg](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E9%85%8D%E4%BB%B6.jpg)

### 下载调平G-code

- 下载手动调平专用Gcode ：[h2s\_manual\_bed\_screws\_adjust\_assist.gcode](https://wiki.bambulab.com/h2s/maintenance/h2s_manual_bed_screws_adjust_assist.gcode)；

下载完成之后，您需要将Gcode文件拷贝至 U 盘根目录内。

### 清洁热床及喷嘴

- 需要移除打印板，并确保热床表面清洁。

![dsc04057_compressed.jpg](https://wiki.bambulab.com/h2s/maintenance/manual-bed-leveling/dsc04057_compressed.jpg)

- 接下来您需要确保右侧喷嘴上没有任何残留塑料；如果需要，加热喷嘴并擦拭喷嘴以确保其清洁。

![1.jpg](https://wiki.bambulab.com/h2s/maintenance/manual-bed-leveling/1.jpg)

### 拧松热床固定螺丝

- 您需要提前**拧松 7 颗固定螺丝**；热床左右两侧 4 颗（两侧螺丝拧松一圈即可），底部 3颗，这样热床才具备一定的上下弹性，便于后续手动调平操作。

> 注意：热床7颗固定螺丝拧松即可，不用完全移除否则会造成螺丝较难安装。

> **热床两侧 4 颗螺丝位置展示**
>
> 下图所示为移除左右侧板，正常拧松螺丝（M3\*6）可以不用移除侧板。

|  |  |
| --- | --- |
| 右侧 | 左侧 |

拧松螺丝之前您可以将**热床适当升高**避免和左侧辅助散热风扇产生干涉。

**左前：**

![2_compressed.jpg](https://wiki.bambulab.com/h2s/maintenance/manual-bed-leveling/02.webp)

**左后：**

![12.jpg](https://wiki.bambulab.com/h2s/maintenance/manual-bed-leveling/12.jpg)  
**右前：**

![2_compressed.jpg](https://wiki.bambulab.com/h2s/maintenance/manual-bed-leveling/01.webp)

**右后：**

![2_compressed.jpg](https://wiki.bambulab.com/h2s/maintenance/manual-bed-leveling/4_compressed.jpg)

接下来，请将热床底部的 3 颗固定螺丝拧松。

|  |  |
| --- | --- |
| 尾部 | 前部 |

### 锁紧热床调平螺丝

在松开热床固定螺丝后，您可以通过逐一按压热床四角验证其是否具备按压回弹的空间，如果四角可以正常回弹说明热床固定螺丝已经拧松。

![松动.webp](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E6%9D%BE%E5%8A%A8.webp)

> 为什么需要锁紧？  
> 由于手动调平过程需要人为调整每个角的螺丝位置，为了确保调平起点一致，必须先将四个调平螺丝全部锁紧（拧到底），此时热床与喷嘴间距离为最远值，有助于统一初始状态。

锁紧四颗调平螺丝，直到无法继续拧动为止。

![调平螺丝.jpg](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/20250604-204026.jpg)

在锁紧过程中，建议用手捏住热床进行锁紧，判断螺丝是否已经完全锁紧。

![按压锁紧.jpg](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E6%8C%89%E5%8E%8B%E9%94%81%E7%B4%A7.jpg)

锁紧完成后，热床四角应无法再被按压下去，也就不会有回弹感。

![不能压缩.webp](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E4%B8%8D%E8%83%BD%E5%8E%8B%E7%BC%A9.webp)

## 开始调平

将调平 G-code 文件复制至 U 盘，并插入打印机的 USB 接口。设备识别后，屏幕会显示文件列表，选择调平用的 G-code 文件，点击“开始打印”。

![](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/u%E7%9B%98.jpg)

运行 Gcode 文件后，打印机将进行回中操作，工具头会逐个探测热床 4 个角，每个角工具头会停留 30 秒，一共执行三轮（确保调平准确）。

![](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/gcode%E8%BF%90%E8%A1%8Cen_(1).jpg)

首先，工具头会自动移动至左前方的调平点。此时请将辅助调平块插入喷嘴与热床之间，通过旋转调平螺丝进行微调，直到喷嘴刚好轻触调平块，并能感受到**轻微滑动阻力**，表示间隙合适。

![2_compressed.jpg](https://wiki.bambulab.com/h2s/maintenance/manual-bed-leveling/03.webp)

> **温馨提示：顺时针是拧紧调平螺丝，会使热床与喷嘴的距离增加；反之，逆时针是拧松调平螺丝，会使热床更加靠近喷嘴。**

随后，请依次对热床四角的调平螺丝进行微调，**确保四个调平点在滑动调平块时所感受到的阻力一致**，以保证热床整体水平。

该 G-code 文件会执行 3 轮调平循环，即每个角的调平点将重复 3 次，您有多次机会进行微调以达到更高精度。建议完整执行所有三轮调平，以确保最终效果稳定可靠。

![2_compressed.jpg](https://wiki.bambulab.com/h2s/maintenance/manual-bed-leveling/2_compressed.jpg)

> **注意：当您发现热床开始主动下降时，请务必停止调平的动作并移走内六角扳手，因为工具头要开始移动了。**

> 当三轮调平执行完毕您发现四个角依旧没有调平，此时您需要再次将4颗调平螺丝锁紧，并再次运行调平 Gcode，进行调平。

## 锁紧热床固定螺丝

确认完成调整后，需要请将**热床左右两侧 4 颗螺丝和底部 2 颗螺丝锁紧（靠近前门附近那颗完成调平后可不用拧紧）**，避免后续使用热床高度出现变化。

拧紧热床左右两侧 4 颗螺丝：

|  |  |
| --- | --- |
| 右侧 | 左侧 |

拧紧底部后面2 颗螺丝：  
![](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E7%83%AD%E5%BA%8A%E5%BA%95%E9%83%A8%E4%B8%A4%E9%A2%97%E8%9E%BA%E4%B8%9D-v.jpg)

底部前面这颗螺丝调平后无需拧紧，保持松弛即可（可拧紧后再松0.5-1圈）。它是为运输保护而设，如果拧的过紧可能导致热床这一块区域高度偏高。  
![](https://wiki.bambulab.com/h2/troubleshooting/manual-bed-leveling/%E7%83%AD%E5%BA%8A%E5%BA%95%E9%83%A8%E8%9E%BA%E4%B8%9D.jpg)

## **设备校准**

在打印机屏幕中点击 **设置 > 校准 > 打印校准 > 自动热床调平**，开始进行校准。 如果一切正常，并且校准过程中没有出现错误或警告，则调平成功。如果仍有问题，请联系服务团队寻求进一步帮助。

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
