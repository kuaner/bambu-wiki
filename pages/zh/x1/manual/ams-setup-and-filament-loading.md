---
path: zh/x1/manual/ams-setup-and-filament-loading
title: "AMS 的配置和上料步骤"
description: "本文提供 AMS 连接、上料和配置的详细步骤"
tags: ["ams", "x1"]
created: 2022-09-05T07:37:53.190Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/x1/manual/ams-setup-and-filament-loading
---

拓竹 AMS 是我们实现多色3D打印的解决方案，能够提供流畅的自动换料体验。本文将指导您连接 AMS 到打印机、在 AMS 中上料以及配置耗材信息。

## 前期操作

在连接 AMS 到打印机之前，请完成打印机的开箱操作，详细步骤可以参考[开箱 X1C Combo | Bambu Lab Wiki](unboxing-combo.md)。

## 视频指引

## 步骤 1 ：连接 AMS 和打印机

1. 取下 AMS 表面的包装薄膜，将 AMS 放置在打印机顶部。

![](https://wiki.bambulab.com/ams/ams-manual/1.ams_on_the_printer.png)

2. 将 PTFE 管从 AMS 出料口（下图 1）连接到耗材缓冲器左侧圆形接口（下图 2）。

![](https://wiki.bambulab.com/ams/ams-manual/2._ams_出料口-缓冲器.png)

3. 取另一根 PTFE 管，一端插入耗材缓冲器的右侧圆形接口（下图 1），另一端插入气动接头的黑色部分（下图 2）。

![](https://wiki.bambulab.com/ams/ams-manual/3.缓冲器-气动接口.png)

4. 将 6-pin 线缆一端连接到耗材缓冲器左侧方形接口（下图 1），另一端连接到 AMS 背部最下方的任一接口（下图 2）。

![](https://wiki.bambulab.com/ams/ams-manual/4.6-pin线.png)

5. 将 4-pin 线缆一端连接到耗材缓冲器下方（下图 1）， L 型端插入打印机背面的 4-pin 接口（下图 2）。

![](https://wiki.bambulab.com/ams/ams-manual/5.4-pin_线.png)

完整的连接效果如下图所示。

![](https://wiki.bambulab.com/ams/ams-manual/6.效果图.png)

## 步骤 2 ：在 AMS 中上料

AMS 与打印机连接后，就可以上料了。

1. 打开 AMS 上盖，把料盘放在料槽里。
2. 轻轻推动上下料器前面的灰色进料口，然后将耗材插入约 2cm，AMS 将检测到耗材并自动往里送料。

![](https://wiki.bambulab.com/ams/ams-manual/7.推动出料口.jpg)

这里是 AMS 上下料器的另一个视角的图片，需要将其往里推来送入耗材。虽然推的时候有一些阻力，但它可以承受这个力，可以适度用力插入耗材。

![](https://wiki.bambulab.com/ams/ams-manual/8.另一个方向看.jpg)

## 步骤 3 ：配置耗材信息

如果使用的是拓竹官方耗材，则 AMS 会通过 RFID 自动识别耗材的种类和颜色。可以点击已识别的耗材查看具体信息，但无法手动修改。

![](https://wiki.bambulab.com/ams/ams-manual/9.进料.png)
![](https://wiki.bambulab.com/ams/ams-manual/10.rfid识别.png)

如果用的是非官方耗材，则需要手动在屏幕上或者 Bambu studio 里配置耗材信息。当某个槽位配置过耗材信息后，下一次插入非官方耗材时它依然会显示上一次的耗材信息，如有需要可以点击重新配置。

![](https://wiki.bambulab.com/ams/ams-manual/11.非rfid识别.png)

在插入耗材后，也可以在 Bambu Studio 里配置 AMS 中的耗材信息。

![](https://wiki.bambulab.com/ams/ams-manual/12.studio_1.png)
![](https://wiki.bambulab.com/ams/ams-manual/13.studio修改耗材信息.png)
> **📌 注意：在打印的过程中耗材信息无法编辑！**

## 步骤 4 ：退料

1. 点击屏幕上的“**退料**”将耗材从挤出机中退回至 AMS 内部。

![](https://wiki.bambulab.com/ams/ams-manual/14.退料.jpg)

2. 用手将灰色进料口向前推，然后用手把耗材抽出来即可。

![](https://wiki.bambulab.com/ams/ams-manual/15.另一个方向看.png)

有时，AMS 滚轮会卡死，并与黄色驱动齿轮啮合。如果发生这种情况，您往退料方向手动拨动料盘时会感受到阻力。见下图。

![](https://wiki.bambulab.com/ams/ams-manual/16.ams_滚轮卡死.png)

如果发生这种情况，只需将料盘向 AMS 的前面轻轻一推，然后再推回来，黄色齿轮会与滚筒上的黑色齿轮脱开。然后您就可以把剩余的耗材卷到料盘上。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以[点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)。我们随时准备为您提供帮助并回答您的任何问题。
