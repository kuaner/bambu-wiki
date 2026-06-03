---
path: zh/software/bambu-suite/manual/auto-thickness-measuring-and-troubleshooting
title: "自动测厚功能及常见问题排查 "
description: ""
tags: []
created: 2025-03-25T13:31:46.610Z
updated: 2025-07-21T04:01:39.010Z
source: https://wiki.bambulab.com/zh/software/bambu-suite/manual/auto-thickness-measuring-and-troubleshooting
---

在使用激光工艺加工前，需测量材料厚度以确保加工效果。Bambu Suite 提供了两种自动测厚方式（自动测量和选点测量），本文将介绍如何使用软件的自动测厚功能，并排查常见问题。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-7.png)

## 自动测量

点击“自动测量”，如果没有提前点击“拍照”获取加工背景图，软件会设置打印机去测量加工区域的中心位置。如果已经获取了加工背景图，软件会自动尝试识别材料位置，然后传给打印机，并选择材料的轮廓中心作为测量点，然后进行材料厚度的测量。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/1.gif)

### 测量失败的可能原因

- 材料预设厚度与实际厚度偏差较大，请输入与实际厚度较为接近的预设厚度再尝试。
- 使用了透明材料，如：透明亚克力、玻璃。建议更换不透明的材料再尝试，如果必须要使用透明材料加工，请手动测量厚度后在软件中输入厚度值**（注意：激光可能无法在透明材料表面聚焦，这可能会影响加工效果）**。
- 材料表面不平整，建议更换较为平整的材料后再尝试。

## 选点测量

在选点测量前，首先要拍照获取加工平面的背景图（若未拍照会有响应的弹窗提醒），然后点击“选点测量”，根据提示在材料表面选择点位进行厚度测量。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-5.png)

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/2.gif)

### 注意事项

手动选点测量需要注意以下几点：

1. **选择物体中心位置作为测厚点**

请尽量选择物体中心位置作为测量点，提高测厚功能的容错能力。

2. **适当调整材料预设厚度**

较为准确的材料预设厚度可以帮助设备更精确的测量材料厚度。

您可以：

- 点击“选择材料”，从材料库中加载预设材料及其预设厚度值。
- 若您使用的是自定义材料，**请输入与材料实际厚度接近的值作为预设厚度。**
- 若您不确定材料厚度，可估测后输入一个大概值。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-6.png)

3. **选择不透明且平整的材料进行加工**

- 材料测厚依赖于光学测量功能，目前尚不支持对透明材料的测厚。
- 若物体表面不平，厚度测量也可能会失败，请勿在2D加工模式下使用表面严重不平整的材料。建议您更换不透明且表面平整的材料后，在软件上重新发起材料测厚。

4. **选点测厚存在盲区，所以选点区域相比激光模组可加工的区域要更小，要注意材料的摆放位置。**

- 因为测厚的条件是需要激光雷达识别到到物体，而激光雷达可运动到的区域与激光模组是不一致的。当工具头移动到最左边时，雷达的位置在 X56 这里。当工具头移动到最外侧时，雷达的位置在 Y40 这里。所以整体盲区范围：X < 56 和 Y < 40。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image.png)

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-1.png)

![激光雷达运动盲区](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-2.png)

- 软件里的绿框为激光雷达的可识别的区域，也就是可手动选点测量的区域。若发现小块材料摆放超出可选点区域，请重新调整材料的摆放位置。

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-3.png)

## 测量失败的可能原因

如果手动选点测量厚度失败，出现相应的报错弹窗或者HMS提醒，则有可能是以下原因导致：

![](https://wiki.bambulab.com/h2/manual/auto-thickness-measuring-and-troubleshooting/image-4.png)

- 选择的测量点靠近物体边缘或物体表面之外，请将测量点选至物体中心位置再次尝试。
- 材料预设厚度与实际厚度偏差较大，请输入与实际厚度较为接近的预设厚度后再尝试。
- 使用了透明材料，如：透明亚克力、玻璃。建议更换不透明的材料再尝试，如果必须要使用透明材料加工，请手动测量厚度后在软件中输入厚度 **（注意：激光可能无法在透明材料表面聚焦，这可能会影响加工效果）**。
- 材料表面不平整，建议更换较为平整的材料后再尝试。
