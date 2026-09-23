---
path: zh/r1/manual/roller-feed-processing-quick-length-measurement
title: "R1 滚轮送料快速测长功能介绍"
description: "本文介绍了如何进行 R1 滚轮送料快速测长"
tags: []
created: 2026-09-22T12:48:39.743Z
updated: 2026-09-22T12:48:41.024Z
source: https://wiki.bambulab.com/zh/r1/manual/roller-feed-processing-quick-length-measurement
---

## 为什么需要测量长度？

滚轮送料加工通常适用于较长的加工物。加工物在设备中会沿滚轮送料方向移动，如果软件不知道加工物的真实长度，可能会出现以下问题:

1. 加工内容超出实际加工物范围；
2. 加工路径与加工位置不匹配；

通过长度测量，设备可以获取更接近真实状态的加工物长度，用于后续的摆盘限制和加工范围判断。

## 长度测量的方法

### 一键准备

点击 **“一键准备”** 按钮，机器将自动送料，对材料进行测长、测距、分段拍照；

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/001.png)

一键准备结束后，会自动将测得的材料长度填进方框中。

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/002.png)

### 快速测长

**“快速测长”** 用于自动识别加工物在滚轮送料方向上的长度。在滚轮送料加工模式下，加工物会由滚轮带动前后运动，系统自动捕捉加工物两端边缘经过探测器时的位置数据，并结合探测器间距计算出实际长度。测量完成后，软件会将该长度数据与拍照拼图结果结合，生成加工物区域范围，以此限制后续加工内容的摆放位置，防止加工越界。

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/003.png)

### 手动测量

Suite 支持手动输入加工物长度，可自行测量再填写。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/004.png)

需注意的是，手动输入长度时，该数值不会经过传感器复核，因此，**请使用尺子等工具测量加工物真实长度，并尽量填写准确的数值。** 若输入长度与实际长度偏差较大，可能会影响加工范围判断。

> **注意：软件里自动测量的材料长度上限为 3000 mm，若材料长度超过该值，请手动测量后在方框里输入长度。**

## 测量前准备

在开始长度测量前，请确认以下事项：

1. 已正确安装增高底座和滚轮送料系统，并完成校准动作；
2. 打开增高底座前门上部分、中门和后门；
3. 加工物边缘探测器避免阳光直射，以免引起误检测；
4. R1 整机的前侧下方（加工物上边缘传感器上方）需贴上遮光胶垫，否则也会导致传感器误检测；

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/005.png)

5. 加工物已按提示放入滚轮送料系统，且遮挡加工物边缘探测器；
6. 加工物放置平整，无明显翘起、孔洞或卡住；
7. 设备当前未执行加工、测量或其他运动任务。

## 操作步骤

1. 在 Bambu Suite 中进入“滚轮送料加工”模式；

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/006.png)

2. 放入加工物，确保遮挡两个加工物边缘探测器；

|  |  |
| --- | --- |
| 007.png | 008.png |

3. 点击“快速测长”按钮；

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/009.png)

如果设备检测到加工物尚未压紧，会先自动执行压紧动作，压紧完成后，设备开始滚轮送料长度测量；

> 注意：
>
> 1. 测量过程中加工物会移动，请不要用手扶或拉拽加工物；
> 2. 测量过程中不要将手伸入滚轮送料机构运动区域。

![010.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/010.webp)

4. 测量完成后，长度结果会同步到 Bambu Suite；

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/011.png)

软件根据测量结果更新加工物范围，并限制用户的摆盘位置。

> 注意：如果需要更换加工物，则需重新测量或重新输入长度。

![012.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/roller-feed-proessing-quick-length-measurement/zh/012.png)

## 故障排除

针对“快速测长”过程中可能出现的故障，原因分析与解决方法如下：

| **故障原因/现象** | **解决方法** |
| --- | --- |
| 增高底座的门未按提示打开 | 检查增高底座前门上部分、中门、后门是否按提示打开 |
| - 加工物未处于加工物边缘探测器可识别的位置 - 加工物未被正确压紧，在滚轮运动过程中打滑、卡住或偏移 | 重新摆放加工物，确保加工物正常压紧，并遮挡边缘探测器 |
| 加工物过短、过窄或有孔洞，导致设备难以正常压紧或遮挡边缘探测器 | 更换加工物后再进行加工 |
| 加工物边缘探测器脏污或读数异常 | 清理加工物边缘探测器 |
| 滚轮送料区域存在碎屑、废料或其他异物 | 清理滚轮送料区域内的碎屑或异物 |
| 测量过程中设备被中断或执行了其他任务 | 重新进行测量 |
| 多次测量失败 | 手动测量长度并输入到软件中 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
