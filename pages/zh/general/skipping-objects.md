---
path: zh/general/skipping-objects
title: "零件跳过"
description: "针对不同系列打印机，本指南为您提供零件跳过的操作方式。"
tags: []
created: 2023-11-06T12:23:19.577Z
updated: 2026-05-22T09:18:52.008Z
source: https://wiki.bambulab.com/zh/general/skipping-objects
---

## 背景

当打印一盘多个模型的时候，有时候会遇到一些意外情况，例如其中某个模型由于脱落、倒塌等原因打印失败了（如下图所示），如果继续打印就会导致炒面。通常我们会希望保留其他完好的打印件继续打印，只跳过打印失败的模型，这样就可以避免耗材的浪费。而 Bambu 系列打印机都配备了“零件跳过”功能，可以帮助您解决这个问题。

![](https://wiki.bambulab.com/general/skipping-objects/%E5%85%B6%E4%B8%AD%E4%B8%80%E4%B8%AA%E6%89%93%E5%8D%B0%E4%BB%B6%E7%82%92%E9%9D%A2.png)

## 功能原理

在切片的过程中，如果一盘打印多个件，切片软件会在 G-code 里给每个件标记一个编号。当你在打印过程中使用零件跳过功能跳过某个件的时候，打印机就会跳过属于这个零件的 G-code 不打印，从而实现零件跳过的功能。（注：这里的“零件”指的是 Bambu studio 中的“对象”，详情可参考[拆分为对象/零件 | Bambu Lab Wiki](../software/bambu-studio/split-to-objects-parts.md)）

不过由于各零件之间的空驶 G-code 并没有被标记为属于某个特定模型，所以在执行零件跳过后，虽然打印机会跳过某个模型不打印，但工具头可能仍然会有一些额外的空驶动作，如下图所示。

![](https://wiki.bambulab.com/general/skipping-objects/%E9%9B%B6%E4%BB%B6%E8%B7%B3%E8%BF%87%E5%8A%A8%E5%9B%BE%E6%BC%94%E7%A4%BA.gif)

另外， 目前在多色打印的过程中使用零件跳过功能（Bambu studio 01.07.04 开始才支持多色打印零件跳过），原本换料、冲刷过程、擦料塔和延时摄影的动作无法被跳过。**所以存在一种情况，当你跳过最高的多色零件后，打印机仍然会将擦料塔打印完后才算完成打印任务。**

![](https://wiki.bambulab.com/general/skipping-objects/%E5%A4%9A%E8%89%B2%E6%89%93%E5%8D%B0%E6%93%A6%E6%96%99%E5%A1%94.png)

同理，如果您开启了延时摄影并跳过本盘中最高的零件后，工具头仍会一直在吐料组件上方来回移动执行延时拍照的 G-code，如下图所示：

![](https://wiki.bambulab.com/general/skipping-objects/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E8%B7%B3%E4%B8%8D%E8%BF%87.gif)

## 操作方法

首先要确保打印机固件和切片软件版本已支持零件跳过功能。最低支持零件跳过功能的固件和软件版本如下表所示：

|  |  |
| --- | --- |
| **机型/软件** | **固件/软件版本** |
| P2S/X2D/H2 系列 | 支持 |
| X1 系列 | 01.06.00.00 |
| P1 系列 | 01.04.02.00 |
| A1 mini | 01.01.00.00 |
| A1 | 01.01.00.00 |
| Bambu Studio | 1.7 |

### 在打印机屏幕操作

在打印过程中，您可以在打印机屏幕使用零件跳过功能。

> 注意：A1 系列打印机暂不支持通过打印机屏幕进行零件跳过，可参考下文其他方式进行。

1. 在屏幕打印任务页面，点击“**跳过**”选项卡。

![h2（1）.png](https://wiki.bambulab.com/general/skipping-objects/h2%EF%BC%881%EF%BC%89.png)

2. 拖动左侧的小方框，把它移动到要跳过零件的区域。

![h2（2）.png](https://wiki.bambulab.com/general/skipping-objects/h2%EF%BC%882%EF%BC%89.png)

3. 在右侧的大方框里，选择要跳过的零件，点击“**零件跳过**”，即可跳过该零件不打印。

![h2（3）.png](https://wiki.bambulab.com/general/skipping-objects/h2%EF%BC%883%EF%BC%89.png)

4. 点击“**确认**”，即可跳过该零件不打印。

![h2（4）.png](https://wiki.bambulab.com/general/skipping-objects/h2%EF%BC%884%EF%BC%89.png)

5. 此时，“**跳过**”选项卡下将显示您跳过的零件个数，（1）表示跳过了一个零件。

![h2（5）.png](https://wiki.bambulab.com/general/skipping-objects/h2%EF%BC%885%EF%BC%89.png)

### 在 Bambu Handy 操作

您可以在手机端通过 Bambu Handy app 来启用零件跳过功能。

#### 打印过程进行零件跳过

1. 点击下图中的图标进入零件跳过页面；

![](https://wiki.bambulab.com/general/skipping-objects/app%E8%BF%9B%E5%85%A5%E9%9B%B6%E4%BB%B6%E8%B7%B3%E8%BF%87%E7%9A%84%E9%A1%B5%E9%9D%A2.png)

2. 选择要跳过的零件，并选择“跳过”即可。

![](https://wiki.bambulab.com/general/skipping-objects/app%E9%80%89%E6%8B%A9%E8%B7%B3%E8%BF%87%E7%9A%84%E9%9B%B6%E4%BB%B6.png)

#### 发起历史打印任务并选择零件跳过

在 APP 的历史打印任务列表再次发起打印的时候，也可以跳过部分零件，仅选择部分零件再次打印。操作步骤如下：

1. 进入打印任务页面，选择你要再次打印的历史任务，

![](https://wiki.bambulab.com/general/skipping-objects/%E5%8E%86%E5%8F%B2%E6%89%93%E5%8D%B0%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8.png)

![](https://wiki.bambulab.com/general/skipping-objects/%E7%BB%A7%E7%BB%AD%E6%89%93%E5%8D%B0%E5%8E%86%E5%8F%B2%E4%BB%BB%E5%8A%A1.png)

2. 然后点击“打印零件”；

![](https://wiki.bambulab.com/general/skipping-objects/%E9%80%89%E6%8B%A9%E6%89%93%E5%8D%B0%E9%9B%B6%E4%BB%B6.png)

3. 选择要打印的零件，并点击“确定”，跳回上个页面后点击“发送打印”即可。**注意：这一步选择的是你要打印的零件，而不是要跳过的零件。**

![](https://wiki.bambulab.com/general/skipping-objects/app%E9%80%89%E6%8B%A9%E8%A6%81%E5%A4%8D%E6%89%93%E7%9A%84%E9%9B%B6%E4%BB%B6.png)

### 在 Bambu Studio 操作

您可以在电脑端通过 Bambu Studio 切片软件来启用零件跳过功能。

1. 打印过程中，点击打印机状态栏中的 “跳过” 按钮。

![](https://wiki.bambulab.com/studio_releasenote/2_2_0_public/cn-1.png)

2. 将打开零件跳过界面，您可以手动选择要跳过的对象。

![](https://wiki.bambulab.com/studio_releasenote/2_2_0_public/cn-2.gif)

**支持的打印机型号**：

- X1 系列、H2 系列和 P2S;
- A1 系列和 P1 系列将在后续固件中逐步支持。

> ⚠️ 请确保您的打印机固件已更新至最新版本，以使用此功能。

### 在农场管家操作

对于 P1 和 A1 系列打印机，您也可以通过[农场管家软件](../software/bambu-farm-manager.md)实现零件跳过功能。

![农场.jpg](https://wiki.bambulab.com/general/skipping-objects/%E5%86%9C%E5%9C%BA.jpg)

## 注意事项

### 无略缩图

由于零件跳过功能需要在打印任务的缩略图上选择零件进行跳过，所以如果打印任务无缩略图（如下图所示），则无法使用零件跳过功能。以下几种情况无法获取打印任务的缩略图：

- 打印的是 gcode 文件而不是 gcode.3mf 文件，gcode.3mf 文件才包含打印任务的缩略图。
- 没有通过云端发送打印任务，仅从 SD 卡、打印机本地缓存的打印文件或者局域网发送的打印任务，由于打印任务没有经过云端服务器，APP 端无法接收到缩略图，所以无法在 APP 上使用零件跳过功能。

![](https://wiki.bambulab.com/general/skipping-objects/app%E6%97%A0%E7%BC%A9%E7%95%A5%E5%9B%BE.png)

**APP 端没有获取到缩略图**

### 零件数量限制

- **单盘仅有 1 个零件或者超过 64 个零件**，无法使用零件跳过功能。

![](https://wiki.bambulab.com/general/skipping-objects/%E9%9B%B6%E4%BB%B6%E8%B7%B3%E8%BF%87%E9%99%90%E5%88%B6.png)

### 当前层无法立刻跳过

- 当打印机正在打印某个零件模型时，如果选择 **“跳过该零件”**，打印机仍会完成当前层的全部打印。等本层结束后，跳过功能才会生效，后续层将不再打印该零件。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
