---
path: zh/a2l/troubleshooting/clogging
title: "A2L 堵塞排查"
description: "本文介绍如何排查 A2L 的堵塞情况"
tags: []
created: 2026-06-01T13:02:59.702Z
updated: 2026-06-01T13:32:19.174Z
source: https://wiki.bambulab.com/zh/a2l/troubleshooting/clogging
---

## 适用场景

当打印机屏幕出现挤出电机过载、空打的报错，或者观察喷嘴无法挤出耗材时，可能是挤出机或喷嘴存在堵塞，可根据本文定位堵塞位置并完成疏通。

## 问题可能发生的位置

1. 挤出机组件
2. 喷嘴

## 所需工具

- H1.5 和 H2.0 内六角扳手
- 镊子

![4.png](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/clogging/4.png)

## 排障步骤

### 步骤 1. 取下喷嘴

握住工具头前盖下部，注意避开热端风扇位置，向上抬起取下工具头前盖。

![gjt001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/gjt001.webp)

确保热端已降至室温，且耗材已被切断。如耗材未被切断，请按压右侧切刀刀柄切断耗材。

![gjt009.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/gjt009.jpg)

用手握住硅胶套高温标识的两侧，向斜下方用力拉，即可取下硅胶套。

![gjt003.webp](https://public-cdn.bblmw.com/wiki/new/a2l/gjt003.webp)

解锁热端卡扣，握住热端散热片两侧，取下热端。

![gjt007.webp](https://public-cdn.bblmw.com/wiki/new/a2l/gjt007.webp)

### 步骤 2. 控制挤出

按下五通组件上的黑色压块，同时拔下工具头的铁氟龙管。

![4.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/nozzl-cold-pull-cleaning/4.jpg)

将耗材送入挤出机中，直到无法推动为止。

![installfilament.png](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/clogging/installfilament.png)

进入“控制”，点击屏幕上的挤出按钮。如果打印机提示“请将喷嘴加热至170℃以上”，请选择“仍然进料”。

![screen1.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/clogging/screen1.jpg)  
![screen2.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/clogging/screen2.jpg)  
![screen3.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/clogging/screen3.jpg)

观察耗材是否能够送出挤出机，若耗材顺利挤出，说明很可能是喷嘴堵塞了，建议您参考[喷嘴堵塞清理](https://wiki.bambulab.com/zh/a2l/maintenance/cold-pull-maintenance-hotend) 清理疏通喷嘴。

![clog1.webp](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/clogging/clog1.webp)

若耗材无法被送出挤出机，说明挤出机故障或者内部存在卡料，建议您参考 [挤出机堵塞清理](https://wiki.bambulab.com/zh/a2l/maintenance/extruder-cleaning-guide) 清理挤出机。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
