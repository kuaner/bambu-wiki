---
path: zh/h2/troubleshooting/clogging
title: "H2D 堵塞排查"
description: "本文介绍如何进行 H2D 堵塞排查"
tags: []
created: 2025-03-25T04:49:29.633Z
updated: 2025-10-21T12:34:02.920Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/clogging
---

## 适用场景

1. 打印机报错挤出电机过载、空打或者打印机未报错，但是可以观察热端无法出料
2. 使用非 TPU 耗材打印
3. 如果使用 TPU 发生堵塞，建议您参考 [H2D TPU 堵塞排查](tpu-clogging.md) 进行排查。

## 问题可能发生的位置

1. 挤出机组件（包括挤出从动杆、主动轮与从动杆缝隙处、前盖导向）
2. 热端

## 视频指南

## 排障步骤

在进行排障之前，请先重试一次，看能否正常恢复打印。如果问题仍然存在，再进行以下排障步骤。

### 步骤1. 移除热端

打开打印机前门，移除上盖。捏住工具头前盖顶部两侧，拆掉工具头前盖。

![](https://wiki.bambulab.com/h2/troubleshooting/image-14.png)  
确认热端温度处于室温，按压切刀切断耗材。  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-9add.png)

> **请注意一定要等到热端温度降到室温后再切料，否则可能导致切刀处出现二次堵塞。**  
> ![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-10add.png)

然后取下硅胶套。  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-8add.png)

将热端加热至 100℃（以 PLA 为例），在加热的状态下将热端取下。

> **请带好防烫手套操作！**

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-13add.png)  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-11add.png)

### 步骤2. 清理热端

取下热端后，用钳子拔掉热端入口处的耗材。  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-12add.png)

装回热端和硅胶套，并重新在耗材页面点击进料恢复打印。如果可以正常打印，那么说明问题已解决；若仍然无法正常打印，请跳转步骤3.  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-add.png)  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-1add.png)

### 步骤3. 手动退料

按压黑色外圈，断开PTFE管。  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-2add.png)  
再次按压切刀切断耗材，取下热端和硅胶套。  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-5.png)  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-1.png)

用力向左推左从动杆（推动从动杆需要较大的力），直到图中标注的这颗螺丝刚好不会被挤出机前盖遮住。然后用手拉住耗材并向上轻轻拔出耗材。如果往上拉耗材的过程中感受到明显阻力，无法顺利将这截耗材取出，请停止强行拉出耗材，并跳转至步骤4。  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-5add.png)  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-6add.png)

如果可以将耗材退出，并看到耗材存在明显异常，请剪断异常部分的耗材，同时我们建议在打印过程中打开前门、上盖，并拆下工具头前盖，改善挤出机组件散热，有利于防止此类堵塞问题发生。  
![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-7add.png)

改善挤出机组件散热后，重新安装热端、PTFE管并恢复打印。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-14add.png)

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-15add.png)

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-16add.png)

恢复打印后，观察挤出机金属齿轮是否正常旋转，以及热端处是否有耗材被挤出。若挤出机齿轮正常旋转但无法在热端处观察到耗材被挤出，或者能听到哒哒哒的丢步声音。请按照此文章[H2D热端堵塞清理](unclogging.md)疏通热端。

![](https://wiki.bambulab.com/h2/troubleshooting/image-24.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-25.png)

### 步骤4. 拆除导向组件进行清理

在步骤3中，**如果往上拉耗材的过程中感受到明显阻力，无法顺利将这截耗材取出**，说明堵塞可能发生在挤出机组件内部，**请停止强行拉出耗材，大力拔出耗材可能导致异常的耗材卡在从动杆组件中，这会使清理变得非常困难。** 需要拆除前盖导向组件，以清理挤出机组件内部（包括挤出从动杆，主动轮与从动轮缝隙处或前盖导向）的堵塞。

需要说明的是，前盖导向与左右切刀刀柄均存在干涉，拆装存在一定困难，尤其是有一段耗材同时穿过挤出机的齿轮与前盖导向时（双色打印时，可能有2段同时穿过左右），拆装困难会加剧，但请不要灰心，只要你参考下述建议，一定可以顺利拆除前盖导向组件的。

**确保热端处于室温后**，先拆除未被堵嘴片挡住的热端，然后在屏幕上切换挤出机，将另一个热端也拆下。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-262.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-27.png)

拆除前盖导向上的4颗螺丝，往上抵住黑色热端连接件，使左切刀从切刀螺丝附近的开口槽中脱出一点，然后从前盖导向右下角向外用力撬出前盖导向。在这种情况下，通常会有一段耗材同时穿过挤出机和前盖导向，在移除前盖导向时需要较大的力。移除前盖导向后，再剪断导向组件与挤出机之间的耗材，分离前盖导向组件。

> 注意：若由于黑色热端连接件被耗材或者弹簧卡住，无法被上抵避开干涉，或者您觉得拆除前盖导向组件过程遇到强大阻力，可增加一个步骤，先拆除左右切刀刀柄，再拆除前盖导向组件，后续安装时，需参考此教程装回切刀刀柄：[H2D 挤出机拆解与安装](extruder-assembly.md)。

![](https://wiki.bambulab.com/h2/troubleshooting/image-28.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-29.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-30.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-31.png)

成功移除前盖导向后，请根据实际情况进行清理：

#### 场景一：异常耗材可能堵在挤出机主动轮与从动轮缝隙中。

针对这种场景，有两种方式清理堵塞。

1. 从挤出机上方剪断耗材，用镊子或者斜口钳夹住堵塞的耗材并向下用力。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/add1.jpg)  
同时在屏幕上切换挤出机，利用挤出机进行左右切换时松开耗材的间隙，将耗材拔出。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-262.png)

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/add2.jpg)

2. 将导致堵塞的异常料头剪掉，然后将热端加热到175℃，在屏幕上点击退料，将剩余的正常耗材退出。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/add3.jpg)

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-292.png)

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/add4.jpg)

严重情况下，耗材可能在挤出轮内部缠住或打结，难以直接将耗材拔出或者退出，这种情况可参考挤出机拆装方法拆除挤出机前壳或者主动轮进行清理：[H2D 挤出机拆解与安装](extruder-assembly.md)

#### 场景二：异常耗材可能堵在前盖导向入口或者内部。

如果异常耗材只是堵在前盖导向的入口处，使用斜口钳将耗材拔出即可。

![](https://wiki.bambulab.com/h2/troubleshooting/image-38.png)

如果异常耗材堵塞在前盖导向的内部，那么需要将前盖导向拆开清理。先拧开1颗螺丝，然后沿着导轨移除黑色连接件，拆下切刀和弹簧。

![](https://wiki.bambulab.com/h2/troubleshooting/image-39.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-40.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-41.png)

使用H1.5的螺丝刀疏通黑色连接件以及导向组件的内部，防止有耗材仍然堵塞在里面。

![](https://wiki.bambulab.com/h2/troubleshooting/image-42.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-43.png)

清理完成后，将弹簧重新安装到黑色连接件上，并沿着导轨装回连接件，请确保弹簧刚好套在红框中的滑块上。然后重新拧入螺丝并放回切刀。需要注意的是，切刀有一侧凹面，请确保装入切刀的时候**凹面是朝上的**。

![](https://wiki.bambulab.com/h2/troubleshooting/image-44.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-45.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-46.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-47.png)

#### 场景三：异常耗材堵在从动杆出口或内部。

这种情况非常罕见，若发生，建议使用H1.5的螺丝刀，尝试捅出耗材，若不能捅出，则需参考此教程进行清理：[H2D 从动杆卡料处理指南](dual-extruder-Idlers-clogging.md)。  
如果仍然难以完成清理，则可以参考此教程：[H2D 挤出机拆解与安装](extruder-assembly.md)，更换从动杆组件。

![](https://wiki.bambulab.com/h2/troubleshooting/image-48.png)

安装前盖导向时，先用力往上按压黑色连接件，然后微微按压左切刀，将其调整到一个合适的角度便于左切刀进入，将前盖导向装入。最后按压两侧切刀，同时用力将前壳完全压平。

![](https://wiki.bambulab.com/h2/troubleshooting/image-49.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-50.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-51.png)

重新锁紧前盖导向上的4颗螺丝。

![](https://wiki.bambulab.com/h2/troubleshooting/image-52.png)

完成清理后，重新装回热端并锁紧热端卡扣，再装回热端硅胶套。在屏幕上切换喷嘴，以同样的方法安装另一个热端。

![](https://wiki.bambulab.com/h2/troubleshooting/image-53.png)

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/image-262.png)

![](https://wiki.bambulab.com/h2/troubleshooting/image-55.png)

重新连接PTFE管，拖链上方的PTFE管连接到右挤出机，拖链下方的PTFE管连接到左挤出机。

![](https://wiki.bambulab.com/h2/troubleshooting/image-56.png)

装回工具头前面盖的时候，可以先扣入挤出机下方的位置，再往后推，将前面盖安装到位。

![](https://wiki.bambulab.com/h2/troubleshooting/image-57.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
