---
path: zh/h3c/troubleshooting/clogging
title: "H3C堵塞（挤出阻力异常或者空打）排查指南"
description: "当设备提示挤出阻力异常，或出现悬空打印时，可参考本文进行排查。"
tags: []
created: 2026-11-03T12:57:47.714Z
updated: 2026-11-03T12:57:48.838Z
source: https://wiki.bambulab.com/zh/h3c/troubleshooting/clogging
---

## 适用场景

当打印机屏幕出现挤出阻力异常、空打的报错，或者观察到热端无法挤出耗材时，可能是挤出齿轮打滑或热端存在堵塞，可根据本文完成故障排查。

## 所需工具

- 清洁毛刷
- 隔热手套

## 排障步骤

### 步骤 1. 检查耗材是否缠料

观察报错槽位的料盘，检查耗材是否出现缠绕。

![001.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/001.jpg)

若耗材存在缠绕，请按住打结位置，取出料盘。

![new1.jpeg](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/new1.jpeg)

拉出打结部分的耗材，解开缠绕。

![new2.gif](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/new2.gif)

完成后将料盘放回 AMS，恢复打印。

![new3.jpeg](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/new3.jpeg)

### 步骤 2. 检查料盘转动是否顺畅

尝试转动料盘。

![003.webp](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/003.webp)

若料盘转动不畅，请重新安装料盘并检查耗材支撑轴是否受损。

![004.png](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/004.png)

料盘过宽会与槽位发生剐蹭，也会增加进料阻力，通常料盘宽度为 65mm 左右。

![005.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/005.jpg)

若无以上异常情况，可进行下一步骤。

### 步骤 3. 检查挤出轮

停止当前任务后，在屏幕上放置工具头上的打印头。

![sc2.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/sc2.jpg)

取下 AMS 的磁吸侧板。

|  |  |
| --- | --- |
| 007.png | 008.png |

检查挤出轮上是否有较多耗材碎屑。

- 若表面附着较多耗材碎屑，请使用毛刷清理干净。

![009.png](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/009.png)

点击“挤出”按键，观察挤出轮能否正常转动。

![sc3.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/sc3.jpg)

若挤出轮无法正常转动，请参考[挤出电机更换指南](../maintenance/replace-2521-extruder-servo-motor.md)重新安装挤出电机的线缆，若依然无效则需要更换挤出电机。

若齿轮表面干净，并且转动顺畅，则进行下一步骤。

![011.webp](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/011.webp)

### 步骤 4. 检查打印头

取下打印头，检查打印头上残留的耗材是否膨胀或磨损。

![012.png](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/012.png)

- 若存在异常，请先按压上方切刀。

![013.png](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/013.png)

> 手动切断耗材后，切刀刀片会卡住，需再按住刀柄下方调回切刀以避免下次进退料失败。

![014.png](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/014.png)

再使用剪钳从中间剪断这段耗材，并拉出上半部分。

![015.gif](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/015.gif)

下半部分则需要将热端加热到打印温度后（如 PLA 为 220 ℃），再拉出。

> 注意：此时热端处于高温状态，操作时请务必佩戴隔热手套，以防烫伤。

![016.gif](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/016.gif)

- 若挤出轮上没有明显碎屑残留，并且转动顺畅，请按下黑色压块，拔下该打印头的料管。

![017.webp](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/017.webp)

然后将打印头加热到耗材打印温度，如 PLA 为 220℃。

> 注意：此时热端处于高温状态，操作时请务必佩戴隔热手套，以防烫伤。

![sc1.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/sc1.jpg)

从打印头顶部插入一截耗材。

![019.png](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/019.png)

观察热端是否能够挤出粗细足够的耗材丝。

![020.png](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/020.png)

若热端仍无法挤出耗材或明显偏细，请参考[热端堵塞疏通](unclogging.md)处理。即使热端没有堵塞可以观察到正常出料，建议定期完成[冷拔](../maintenance/nozzle-cold-pull-maintenance.md)。

完成该步骤后，收回 AMS 中的耗材，重新插入耗材并进料。

![021.png](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clogging/zh/021.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
