---
path: zh/h2/troubleshooting/tpu-clogging
title: "H2D TPU 堵塞排查"
description: ""
tags: []
created: 2025-04-10T09:47:44.339Z
updated: 2025-04-18T02:13:12.822Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/tpu-clogging
---

## 适用场景

1. 打印机报错挤出电机过载、空打或者打印机未报错，但是可以观察热端无法出料
2. **使用TPU耗材打印**

## 问题可能发生的位置

由于TPU较软的材料特性，在进料时可能会发生卷料，缠在金属主动轮上。

## 排障步骤

### 步骤1.热端升温

打开打印机的前门，取下顶部盖板。然后，捏住工具头前盖顶部的两侧，将其拆下；按压气动接头黑色外环以断开PTFE管。接着，将热端加热至175°C。

![](https://wiki.bambulab.com/h2/troubleshooting/tpu-clogging/image-1.png)

![](https://wiki.bambulab.com/h2/troubleshooting/tpu-clogging/20250410-173002.jpg)

![](https://wiki.bambulab.com/h2/troubleshooting/tpu-clogging/image.png)

控制挤出机齿轮旋转的前提是热端温度高于170°C。因此，我们建议将热端温度设置为175°C，以便于控制挤出机齿轮旋转。

### 步骤2. 手动退料

等待热端达到175℃，用手辅助略微用力拉住料线，并在屏幕上点击退料**两次**，请注意点击退料两次就够了，如果退料太多可能会导致TPU反卷到主动轮另一侧，会导致清理难度更大。

![](https://wiki.bambulab.com/h2/troubleshooting/tpu-clogging/20250410-172947_-_%E5%89%AF%E6%9C%AC.jpg)

### 步骤3. 取出TPU

完成步骤2之后，请保持挤出轮不动。在屏幕上切换喷嘴，在喷嘴切换的间隙，用手将TPU拉出。如果后续固件更新支持了维护模式功能，你可以开启维护模式，用手拽住料线略微用力，就可以将堵住的TPU拉出。

![](https://wiki.bambulab.com/h2/troubleshooting/tpu-clogging/20250410-172911_-_%E5%89%AF%E6%9C%AC.jpg)

![](https://wiki.bambulab.com/h2/troubleshooting/tpu-clogging/20250410-172955.jpg)

![](https://wiki.bambulab.com/h2/troubleshooting/tpu-clogging/20250410-172955_-_%E5%89%AF%E6%9C%AC.jpg)

若挤出机内部出现严重缠料，请可参考挤出机拆装方法拆除挤出机前壳或者主动轮进行清理。

[H2D 挤出机拆解与组装指引](extruder-assembly.md)
