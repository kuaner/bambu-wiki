---
path: zh/software/bambu-studio/parameter/elephant-foot
title: "象脚补偿"
description: "本文介绍了象脚以及象脚补偿。"
tags: ["bambu studio"]
created: 2023-12-03T14:32:20.249Z
updated: 2026-06-11T08:03:35.602Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/elephant-foot
---

## 什么是象脚

在 FDM 3D 打印过程中，是通过喷嘴挤压材料一层层堆叠构建成3D模型的。所以在打印过程中，\*\*首层挤出的线条被压在加热的热床上尚未完全冷却，再加上来自上层重力的挤压，打印出来的首层可能会扩展一些出来，这种现象就称之为象脚。\*\*在打印模型较大的模型时，象脚通常会更明显一些。

在大部分情况下，底部轻微的象脚对于大部分模型来说可能都无关紧要。不过当你打印出来的模型需要具有精确的尺寸和公差进行装配，就需要对象脚进行一些处理。

![](https://wiki.bambulab.com/bambu-studio/parameter/elephant-foot/%E8%B1%A1%E8%84%9A%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

**象脚示意图 1**

![](https://wiki.bambulab.com/bambu-studio/parameter/elephant-foot/%E8%B1%A1%E8%84%9A%E5%AE%9E%E7%89%A9%E5%9B%BE.png)

**象脚示意图 2**

## 象脚补偿

### 在 Bambu Studio 启用象脚补偿

在 Bambu Studio 中开启象脚补偿功能后，它将会主动收缩第一层来补偿首层的扩展，使得实际打印出来的模型首层与其它层平齐。这样就不需要你手动打磨首层扩展出来的边沿。

您可以在**工艺 - 质量 - 象脚补偿**来开启它。

![](https://wiki.bambulab.com/bambu-studio/parameter/elephant-foot/%E8%B1%A1%E8%84%9A%E8%A1%A5%E5%81%BF%E5%BC%80%E5%90%AF.png)

启用象脚补偿前后的切片对比：

![](https://wiki.bambulab.com/bambu-studio/parameter/elephant-foot/%E8%B1%A1%E8%84%9A%E8%A1%A5%E5%81%BF0.png)

**未启用象脚补偿**

![](https://wiki.bambulab.com/bambu-studio/parameter/elephant-foot/%E8%B1%A1%E8%84%9A%E8%A1%A5%E5%81%BF0.3.png)

**象脚补偿0.3mm**

## 启用象脚补偿后，预览中 Brim 无法与模型完全贴合

当你启用 [Brim](../auto-brim.md) 且把“ Brim 与模型的间隙”设置为 0mm，发现 Brim 依然没有完全连接到模型，则有可能就是开启了象脚补偿导致的。如果您想要在预览中使 Brim 与模型完全贴合，则需要关闭象脚补偿。

![](https://wiki.bambulab.com/bambu-studio/parameter/elephant-foot/%E5%BC%80%E5%90%AF%E8%B1%A1%E8%84%9Abrim%E6%9C%AA%E6%8E%A5%E4%B8%8A.png)

**启用象脚补偿**

![](https://wiki.bambulab.com/bambu-studio/parameter/elephant-foot/%E5%85%B3%E9%97%AD%E8%B1%A1%E8%84%9Abrim%E6%8E%A5%E4%B8%8A.png)

**关闭象脚补偿**
