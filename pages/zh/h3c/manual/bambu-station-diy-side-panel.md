---
path: zh/h3c/manual/bambu-station-diy-side-panel
title: "拓竹工作站 L DIY 侧板加工与更换指南"
description: "本文介绍如何使用拓竹 R1 将木质板材加工为拓竹工作站 L 的洞洞板侧板，并安装至工作站两侧。"
tags: []
created: 2026-11-08T09:27:24.838Z
updated: 2026-11-11T06:03:09.608Z
source: https://wiki.bambulab.com/zh/h3c/manual/bambu-station-diy-side-panel
---

拓竹工作站 L 支持 DIY 侧板设计与加装。您可以选择官方提供的图案样式进行切割与雕刻，也可以自行设计独一无二的侧板图案。

本文将介绍如何使用拓竹 R1 自主加工拓竹工作站 L 洞洞板侧板，并完成安装。

> ℹ️**说明**：除洞洞板侧板外，后续还将推出更多官方图案设计文件。您可以根据个人喜好选择不同图案进行加工，让工作站拥有更多个性化外观。

![pegboard-side-panel_for_bambu_station_l.png](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/pegboard-side-panel_for_bambu_station_l.png)

## 所需材料与工具

- 图案文件（[点击下载官方洞洞板侧板 .lac 文件](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/pegboard_side_panel.lac)）
- 木质板材 × 2
  - **尺寸建议**：厚度 10 mm，宽度 600 mm，长度不小于 600 mm
  - **材质建议**：椴木 / 胡桃木
  - **板材状态**：板材需平整，**无明显翘曲、起拱或扭曲**，否则影响拍图、测距与加工精度
- 拓竹 R1 （[购买链接](https://item.jd.com/10232365669917.html?pcdk=ApwIWW7jVBKGvFZHo5vjYbrfQIDILEcZ9mDfHVOCbfo%3D.M8AW.sbc1)）
- R1 增高底座 （[购买链接](https://item.jd.com/10235955321767.html?pcdk=Y2krPofcMKliqk5V8YDoC4JPwOcB3Orreq5t3IV-3PUv8Z9yGgLKcq9QFb7BFZM1.rQ4a.tlbT)）
- R1 滚轮送料系统 （[购买链接](https://item.jd.com/10235955321768.html?pcdk=VU8stwf03bRT07Fc94ZpaYKTbg3V3Pu3p0qMZnn19Qcw_nqhH1cXkt0IlTUF0-Ou.rQ4a.tlbT)）
- R1 L 型聚焦镜 （[购买链接](https://item.jd.com/10235955321770.html?pcdk=2jvN7LwOpwpyNY7-MveiltvXVsAS8aCB5mPlsUZgtRA4a_5e0kMKr-ngKobqKXh8.rQ4a.tlbT)）
- Bambu Suite（[下载链接](https://bambulab.cn/zh-cn/download/suite)）
- M5\*16 机牙螺丝 × 8
- H3.0 内六角扳手
- 剪钳 （[购买链接](https://item.jd.com/10220933359578.html?pcdk=Z0-Xey4cPEz1I20YxIYFVaUyoAQZqFGQIKFUjE6jQXI%3D.M8AW.sbc1)）
- 锉刀（[购买链接](https://item.jd.com/10225316262448.html?pcdk=1i8Gza-Bwvkzh5UHpe2zZZALMxsLr9zjq5TVAXUHtVI%3D.M8AW.sbc1)）
- 锤子
- 手套

> ℹ️**说明**：您也可以使用其他支持木板切割与雕刻的激光加工设备。本指南仅以拓竹 R1 为例介绍操作流程；如使用其他设备，请遵循对应设备的操作说明与安全要求进行加工。

## 安全提示

**开始此次加工项目前，请特别注意以下事项：**

- 加工期间，请始终确保设备处于有人现场看管的状态。
- 开始加工前，请确保排烟管末端已放置在室外，或已连接官方激光专用净化器。
- 请勿加工材质不明、含 PVC、覆膜或可能产生有毒烟雾的材料。
- 加工过程中，请勿打开防护上盖，也请勿长时间直视激光加工区域。
- 加工完成后，请等待烟雾排出，并确认板材无明火、无阴燃后，再打开上盖取出板材。
- 取出板材和进行后处理时，请佩戴手套，避免被焦边、毛刺或残留碎屑划伤。

> ⚠️ **重要**  
> 使用 R1 前，请务必阅读以下激光使用安全相关文档，重点了解操作安全、激光安全、化学品安全、消防安全与电气安全等注意事项，确保遵守所有步骤与限制，并清楚每项操作的风险与应对措施：
>
> - [**R1 激光使用重要信息**](../../r1/manual/laser-important-info.md)
> - [**R1 激光使用条款**](../../r1/manual/laser-module-terms-of-use.md)
> - [**R1 激光安全须知**](../../r1/manual/laser-safety-document.md)
>
> 此外，请按照《[快速入门指南](https://bambulab.cn/zh-cn/support/documentation/1154897064687935488)》或《[开箱指南](../../r1/manual/unboxing.md)》完成必要的初始安装和设置。

## 加工与安装步骤

本章节将介绍如何使用拓竹 R1，将木质板材加工为拓竹工作站 L 的洞洞板侧板。

### 步骤 1. 完成设备准备

使用 R1 进行本次加工前，请完成以下准备工作。

#### 更换聚焦镜

请参考 [R1 聚焦镜更换指南](../../r1/maintenance/replace-focusing-lens.md)，安装 L 型聚焦镜。

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/long-focus-lens.png)

#### 安装滚轮送料机

请参考以下教程，安装 **增高底座** 与 **滚轮送料机**。若您已安装，可跳过此步骤。

- [增高底座安装指南](../../r1/manual/riser-base-unboxing.md)
- [滚轮送料机安装指南](../../r1/manual/conveyor-unboxing.md)

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/roller-conveyor.jpg)

#### **滚轮送料校准**

为获得更高的测量精度，加工前请在设备屏幕上依次点击：**“设置 > 校准 > 滚轮送料校准”**，完成校准。

|  |  |
| --- | --- |
|  |  |

### 步骤 2. 放置板材

拿取板材时，建议佩戴手套，避免脏污和意外剐蹭受伤。

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/wear-gloves.png)

打开上盖，将板材从前门方向对准滚轮送料系统的送料槽口，并向内插入。

> ℹ️ **注意**：请勿从机器后方进料！

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/feed-from-front.jpg)

> ℹ️ **说明**：配图仅供演示参考，实际操作时建议佩戴手套。

### 步骤 3. 导入图案

将下载好的 `.lac` 文件导入或拖进 Bambu Suite。

- 官方洞洞板图案文件：[点击下载.lac](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/pegboard_side_panel.lac)

|  |  |
| --- | --- |
|  |  |

导入成功后，点击右下角「**准备制作**」。

![prepare.png](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/prepare.png)

点击上方「**一键准备**」按钮，设备将自动送料，并测长、测距、分段拍照。

![prepare.png](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/capture-image.png)

拍图完成后，Suite 会在画布上按打印台实际尺寸显示可加工的板材长图，并显示测量的板材长度和距离；点击右下角「**制作**」，并等待文件发送。

> ℹ️ **注意**
>
> 1. 文件的加工参数已预先设置，无须自行调整。
> 2. 拍图完成后，**请勿人为移动设备内板材**；若误碰导致板材位置发生变化，请重新拍照测量后再加工。

|  |  |
| --- | --- |
|  |  |

跳转至下方窗口后，请前往设备，并按照屏幕提示进行操作。

![prepare.png](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/operate-on-device.png)

### 步骤 4. 开始加工

> ⚠️ **注意**  
> 开始加工前，确保产品的排烟管末端已放置在室外，或已接入官方激光专用净化器（请在 [E1 Pro 净化器安装使用指南](../../r1/manual/air-purifier-unboxing.md) 查看连接方式）。

> ❗ **危险**  
> 加工期间，请始终确保本产品处于有人现场看管的状态。加工时，请勿透过机箱长时间直视激光。

关闭设备的防护上盖，按下 **启停按钮**，产品将开始加工。您可在产品屏幕或 Suite 界面查看任务进度和剩余时间。

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/start-pause-button.png)

### 步骤 5. 完成加工

- 加工完成后，在 Bambu Suite 中点击“**松开**”按钮，待滚轮抬起后，即可取出板材。

> ⚠️ **注意**：拿取板材时，**建议佩戴手套**，避免脏污和意外剐蹭受伤。

|  |  |
| --- | --- |
|  |  |

- 随后，**重复步骤 2 至步骤 5**，完成第二块木质板材的加工。

### 步骤 6. 后处理

两块木质板材加工完成后，请按以下步骤进行后处理：

1. 请佩戴手套进行后处理操作，避免脏污和意外剐蹭受伤。

> ℹ️ **说明**：本章节配图仅供演示参考，实际操作时请佩戴手套。

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/wear-gloves.png)

2. 将切割成型的洞洞板侧板从原木板中取出。

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/remove-panel.jpg)

3. 检查洞洞板四周边缘是否有毛刺，若有，请使用剪钳清理。

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/trim-edge.jpg)

4. 移除所有孔位中的木材残留。

![](https://wiki.bambulab.com/h3c/manual/bambu-station-diy-side-panel/pegboard-side-panel/clear-holes.png)

5. 若部分孔位的木材残留难以手动取出，可使用尖头锉刀对准孔位，使用小锤子轻轻敲击锉刀尾部，将残留木材推出。

> ⚠️**注意**：敲击时请务必注意安全，佩戴手套，并控制力度，避免砸伤双手。

|  |  |
| --- | --- |
|  |  |

6. 若孔位边缘有毛刺残留，请先使用剪钳剪除较大的毛刺或残留连接点，随后使用锉刀沿孔位边缘轻轻修整，去除细小毛刺和凸起，使孔位轮廓保持平整。

|  |  |
| --- | --- |
|  |  |

### 步骤 7. 安装侧板

依次安装两块洞洞板侧板至工作站两侧，左右两侧安装方式相同：

1. 安装前，请确认侧板方向正确，即侧板孔位应呈竖向长椭圆形，不能横向放置。
2. 使用 H3.0 内六角扳手，将四颗 M5\*16 机牙螺丝拧入侧板四角的螺丝孔。
3. 以同样的方式安装另一块侧板。

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
