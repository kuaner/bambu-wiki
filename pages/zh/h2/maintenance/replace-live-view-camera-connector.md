---
path: zh/h2/maintenance/replace-live-view-camera-connector
title: "H2 系列实况摄像头连接线更换指引"
description: "本wiki介绍了怎样更换 H2 系列实况摄像头的连接线，不包括更换摄像头（文中另有链接）。"
tags: []
created: 2025-04-30T08:55:05.182Z
updated: 2026-05-28T09:15:23.941Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-live-view-camera-connector
---

> **隐私提示**：请确保摄像头已正确安装，使摄像头视野正确朝向打印机腔体，以避免对打印区域或喷嘴的检测出现问题。

## 实况摄像头

实况摄像头安装在打印机内部，可以通过实况摄像头在 Bambu Studio 和 Bambu Handy 中实时查看打印的过程，并提供炒面检测、异物检测、打印板检测以及热端类型识别等多种智能检测功能。

|  |  |
| --- | --- |
|  |  |

> 实况摄像头更换指南请参考：[更换 H2D 实况摄像头](replace-live-view-camera.md)

**实况摄像头的备件包含以下：**

1. 实况摄像头 \* 1
2. 实况摄像头连接线 \* 1
3. M3x6 螺丝 \* 2

[购买链接](https://detail.tmall.com/item.htm?abbucket=15&id=899695675575&pisk=gN9qeCTl6xH4an_AiL6aTMxJ_lXApOuI3d_1jhxGcZbm6jpN_HToDcKG5dWwyUfMhttXzopy8RwjkjKgQO6iR2MIdnnABO0CKw0TWrIfxND1SRjlHGGZ0DIEdnKAWoziAQDQbKTiWoVGSFXlZMjCIG2cj0WlfMBgn12DqabRrO20IG2lrMs4oGVDSuDlcMZ0iG20E8jhYObMSsmyqaININcmQnxgUM1mf-aghcgers7Hmaye2LSmIwkdrRqwEi-A8ncTIRvP0sJk8Li-csOMv6pXxAyRhHRlEGJtx57NTCvfEK0oK_CMEUjklcNO4C-MptBUjxxP3Z5HEsHZfexyjB1yFDDd3tbD1tK_Yqty3EtvUhZgZtWXa6JVKvUc5QteQGJtWY8ejHdGadzV4h4OqsYBBIzg_sjR4wir4ndtOBUCnxn_65Clpg7IciNT6sY7CSJUd5FOZgSPRmwG.&rn=156ac964fe6b943aa6d56065e45b6ca5&spm=a1z10.3-b-s.w4011-25177047232.30.56503c0e4XCIsR&skuId=5755144500539)

## 何时更换

实况摄像头连接线断裂或损坏

> 此wiki只介绍了怎样更换摄像头连接线，如果是摄像头损坏需要更换请[参考此wiki](https://wiki.bambulab.com/e/zh/h2/maintenance/replace-live-view-camera)。

## 所需的工具和材料

1. 新的实况摄像头连接线
2. H2.0 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系[在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 更换实况摄像头连接线

### 移除实况摄像头连接线

#### 步骤 1：移除 AP 板盖

使用 H2.0 内六角板扳手移除一颗 AP 板盖固定螺丝（BT2.5×8），然后从靠近前门的一侧取下 AP 板盖。

|  |  |  |
| --- | --- | --- |
|  |  |  |

#### 步骤 2：移除左侧板

您可以参考下面这篇 Wiki 来移除左侧板：

[更换 H2D 左/右侧板](replace-side-panel-with-glass-window.md)

#### 步骤 3：移除实况摄像头

1. 使用 H2.0 内六角扳手移除两颗固定螺丝（M3x6），将实况摄像头靠近前门的一侧取出，然后即可将实况摄像头取出。

|  |  |  |
| --- | --- | --- |
|  |  |  |

2. 将实况摄像头连接线上方的黑色卡扣往上扣开，然后即可抽出实况摄像头连接线。

|  |  |
| --- | --- |
|  |  |

#### 步骤 4：移除实况摄像头连接线

1. 将实况摄像头连接线与 AP 板连接的卡扣扣开，然后将实况摄像头连接线从 AP 板上的接口中取出；

|  |  |
| --- | --- |
|  |  |

2. 然后将摄像头连接线从上框的小孔中抽出，将贴在打印机上的连接线撕下即可拆除。

![](https://wiki.bambulab.com/h2/maintenance/replace-live-view-camera-connector/image-14.png)

### 安装实况摄像头连接线

#### 步骤 1：连接 AP 板

实况摄像头连接线的安装需要注意区分方向，在连接线的一端印有“AP”，即表示这一端与 AP 板连接：

|  |  |
| --- | --- |
|  |  |

1. 将实况摄像头连接线印有“AP”的一端穿过上框；  
   ![](https://wiki.bambulab.com/h2/maintenance/replace-live-view-camera-connector/image-16.png)
2. 然后插入 AP 板的接口中，并扣上卡扣；

|  |  |
| --- | --- |
|  |  |

3. 撕下实况摄像头连接线的背胶，将连接线参考下图粘贴在打印机上（箭头所示处可以将排线折一下，便于粘贴）；

![](https://wiki.bambulab.com/h2/maintenance/replace-live-view-camera-connector/image-19.png)

4. 然后将另外一端插入打印机立柱的小孔中。  
   ![](https://wiki.bambulab.com/h2/maintenance/replace-live-view-camera-connector/image-37.png)

#### 步骤 2：固定实况摄像头

1. 将实况摄像头连接线插入实况摄像头上，并扣紧黑色卡扣；

> 注意需要将线缆放置到位。

|  |  |
| --- | --- |
|  |  |

2. 拿住实况摄像头的左侧，侧着将摄像头的右侧先装回，然后再装回左侧，并对准螺丝孔位;

|  |  |
| --- | --- |
|  |  |

3. 最后使用 H2.0 内六角扳手拧紧两颗固定螺丝（M3x6）。

![](https://wiki.bambulab.com/h2/maintenance/replace-live-view-camera-connector/image-27.png)

#### 步骤 3：安装左侧板

您可以参考下面的 Wiki 来安装打印机左侧板：

[更换 H2D 左/右侧板](replace-side-panel-with-glass-window.md)

#### 步骤 4：安装 AP 板盖

先从靠近打印机背面的一侧扣回 AP 板盖，然后使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6×8）。

|  |  |
| --- | --- |
|  |  |

## 如何验证成功/完成

连接电源线并打开电源，在 Bambu Studio/Bambu Handy 中点击播放视频，检查是否可以正常播放。  
如果无法正常查看视频，则请检查线缆是否连接正确，然后重试。如果问题仍然存在，请联系 Bambu Lab 技术支持寻求进一步帮助。

## 螺丝型号

**更换 H2D 实况摄像头/实况摄像头连接线所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** |  | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| M3x6 |  | 用于固定实况摄像头 |  |  | 2 |
| BT2.6x8 |  | 用于固定 AP 板盖 |  |  | 1 |
| ST3x6 |  | 固定背板（红色圆圈标记） |  |  | 11 |
| ST3x12 |  | 固定料盘支架底座（黄色方框标记） |  |  | 2 |
| M3x3（螺帽直径 10mm） |  | 用于固定前门玻璃 |  |  | 4 |
| BT3x16 |  | 用于固定辅助部件冷却风扇 |  |  | 2 |
| BT3x8 |  | 用于固定左侧板 |  |  | 3 |
|  |  | 固定背板（绿色方框标记） |  |  | 12 |
| ST3x3 |  | 用于固定左侧板 |  |  | 2 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
