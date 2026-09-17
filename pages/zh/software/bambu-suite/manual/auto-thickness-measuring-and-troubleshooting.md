---
path: zh/software/bambu-suite/manual/auto-thickness-measuring-and-troubleshooting
title: "自动测厚功能及常见问题排查 "
description: ""
tags: []
created: 2025-03-25T13:31:46.610Z
updated: 2026-08-28T06:21:27.377Z
source: https://wiki.bambulab.com/zh/software/bambu-suite/manual/auto-thickness-measuring-and-troubleshooting
---

在使用激光工艺加工前，需测量材料厚度以确保加工效果。Bambu Suite 提供了两种自动测厚方式：**自动测量**和**选点测量**，本文将介绍这两种测厚方式，并排查常见问题。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-7.png)

## 自动测量

点击“自动测量”即可开始测量；

- **未提前拍照**：若未点击"拍照"获取加工背景图，软件会以加工区域的中心位置作为测量点。
- **已获取背景图**：软件会自动识别材料位置并传给打印机，选择材料轮廓的中心作为测量点，随后进行厚度测量。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/1.gif)

### 测量失败的可能原因

- **材料预设厚度与实际厚度偏差较大**，需输入与实际厚度较为接近的预设厚度再尝试。
- **使用了透明材料**，如透明亚克力、玻璃；建议更换不透明材料后重试。若必须使用透明材料，请手动测量厚度后在软件中输入厚度值。

> 注意：激光可能无法在透明材料表面聚焦，这可能会影响加工效果。

- **材料表面不平整**，建议更换较为平整的材料后再尝试。

## 选点测量

进行选点测量前，需先点击“拍照”按钮获取加工平面的背景图，然后点击“选点测量”，根据提示在材料表面选择点位进行厚度测量。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/2.gif)

> 注意：若未拍照，软件会弹窗提醒。  
> ![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-5.png)

### 注意事项

手动选点测量需注意以下几点：

1. **选择物体中心位置作为测厚点**

请尽量选择物体中心位置作为测量点，提高测厚的成功率。

2. **适当调整材料预设厚度**

较为准确的材料预设厚度可以帮助设备更精确地测量材料厚度，您可以：

- 点击“选择材料”，从材料库中加载预设材料及其预设厚度值。
- 若您使用的是自定义材料，请输入与材料实际厚度接近的值作为预设厚度。
- 若您不确定材料厚度，可估测后输入一个大概值。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-6.png)

3. **选择不透明且平整的材料进行加工**

- 材料测厚依赖于光学测量功能，目前**尚不支持透明材料**的测厚。
- 若物体表面不平，厚度测量也可能会失败，请勿在 2D 加工模式下使用表面严重不平整的材料。建议您更换不透明且表面平整的材料后，在软件上重新发起材料测厚。

4. **注意选点盲区，合理摆放材料**  
   选点测厚存在盲区，可选点区域**小于**激光模组的可加工区域，需注意材料摆放位置。测厚需激光雷达识别到物体，而激光雷达的可运动范围与激光模组并不一致：

- 工具头移至最左侧时，雷达位置在 **X = 56 mm**
- 工具头移至最外侧时，雷达位置在 **Y = 40 mm**

|  |  |
| --- | --- |
|  |  |

整体盲区范围为：**X < 56 mm** 且 **Y < 40 mm**

![激光雷达运动盲区](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-2.png)

- 软件中的**绿框**为激光雷达可识别区域，即可手动选点测量的区域。若小块材料摆放超出该区域，请重新调整材料位置。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-3.png)

### 测量失败的可能原因

如果手动选点测量厚度失败，出现相应的报错弹窗或者 HMS 提醒，则有可能是以下原因导致：

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-4.png)

- **选择的测量点位置不当**，靠近物体边缘或物体表面之外，需将测量点选至物体中心位置再次尝试。
- **材料预设厚度与实际厚度偏差较大**，需输入与实际厚度较为接近的预设厚度再尝试。
- **使用了透明材料**，如透明亚克力、玻璃；建议更换不透明材料后重试。若必须使用透明材料，请手动测量厚度后在软件中输入厚度值。

> 注意：激光可能无法在透明材料表面聚焦，这可能会影响加工效果。

- **材料表面不平整**，建议更换较为平整的材料后再尝试。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
