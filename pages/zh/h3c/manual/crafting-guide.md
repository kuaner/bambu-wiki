---
path: zh/h3c/manual/crafting-guide
title: "H3C 刀切加工介绍"
description: ""
tags: []
created: 2026-11-03T12:12:20.629Z
updated: 2026-11-03T12:38:10.037Z
source: https://wiki.bambulab.com/zh/h3c/manual/crafting-guide
---

## 功能简介

H3C 可兼容多种工具，包括打印头和平面加工头（刀切头/画笔头），在平面加工头基座上安装刀座/笔座及对应的刀头和画笔，可执行切割、绘画、烫金、压痕等 2D 任务。用户可根据实际需求安装对应工具，并配合刀切垫板和多种材料完成不同类型的加工操作。

> 注：冷烫金刀和压痕刀预计在产品发布当天的固件中支持。

## 工具介绍

### 刀切头

**可实现切割等工艺的刀切头 = 平面加工头基座 + 刀座 + 对应刀头**，用于完成切割、烫金、压痕等 2D 加工。

**平面加工头基座**

平面加工头基座底部带有螺纹，可旋转固定刀座或笔座。

![001.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/001.png)

**刀座**

各类刀头的安装载体。负责固定刀头位置，并在加工时为刀头提供稳定的下压力。

![002.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/002.png)

**刀头**

H3C 共有三种类型刀头，可实现不同的刀切效果。

![003.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/003.png)

- **精细尖刀：** 通用切割刀头，适合裁切纸张、贴纸、卡纸等大部分2D耗材，可用于轮廓切割和精细形状加工。

![004.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/004.png)

- **压痕刀：** 不切断材料，只在表面压出折痕，方便后续折叠或立体造型。

![005.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/005.png)

- **冷烫金刀：** 配合适配冷压的烫金纸使用，将金属箔转移到指定区域，用于制作装饰线条等烫金效果，无需高温烫印。

![006.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/006.png)

### 刀切垫板

刀切垫板由刀切保护钢板和刀切粘板组成。刀切工作开始前，需要将加工材料贴在粘板表面，用于在加工过程中固定耗材。

![007.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/007.png)

## 加工前准备

### 工具和材料

- 刀切头
- 刀切垫板
- 加工材料
- 俯视摄像头（可选）

### 辅助工具打印

| **模型名称** | **作用** | **示意图** |
| --- | --- | --- |
| **钩针：** [下载链接](https://makerworld.com.cn/zh/models/1068224-tuo-zhu-gou-zhen-wo-bing#profileId-1109145) | 移除废料 | Image |
| **刮刀：** [下载链接](https://makerworld.com.cn/zh/models/125813-tuo-zhu-re-chuang-gua-dao#profileId-8923) | 移除刀切垫板上的材料 | Image |
| **滚筒：** [下载链接](https://makerworld.com.cn/zh/models/1068223-tuo-zhu-gun-tong#profileId-1109144) | 压平材料，确保加工精度 | Image |
| **取刀器** | 夹持刀头，辅助更安全地安装与拆卸 | Image |

> 注：辅助工具可用于后续任务中的多种操作。具体请参考[模切模组辅助工具（钩针、刮刀与滚筒）的使用介绍](../../h2/manual/cutting-module-assist-tool.md)。

## 加工流程

本文以**精细尖刀**为例，介绍具体加工流程。冷烫金刀和压痕刀的加工流程请参考 wiki：[烫金压痕工艺说明](deboss-and-foil-transfer-tip.md)。

### 安装刀切头和刀切垫板

请参考[平面加工头开箱指南](unboxing-crafttool.md)安装。

### 安装俯视摄像头（选做）

请参考：[俯视摄像头更换指南](../maintenance/replace-birdseye-camera.md)安装俯视摄像头。

> 未选配俯视摄像头时，无法在 Bambu Suite 中直接拍照对位，但可用 Bambu Handy 拍照完成对位。如需体验更顺畅的平面加工流程，建议选购俯视摄像头。

### 加工准备

- 在打印机屏幕上设置正确的加工头信息，并取用该打印头；

|  |  |
| --- | --- |
| 012.png | 013.png |
| 014.png | 015.png |

- 打开 Bambu Handy 扫描绑定打印机，并打开 Bambu Suite 登录账号，在画布中导入想要加工的图案；

![016.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/016.png)

- 在“工艺类型”中选择“基础刀切”；

![017.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/017.png)

- 在右下角点击“准备制作”；

![018.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/018.png)

- 把需要加工的材料粘附在刀切垫板上，并用滚筒工具使其完全贴合，然后安装刀切垫板；

|  |  |
| --- | --- |
| 019.png | 020.png |

- 在 Bambu Suite 最右侧“材料组”中选择加工的材料类型。

![021.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/021.png)

### 拍照对位

#### 俯视摄像头自动拍照

点击“拍照”，俯视摄像头将自动拍照。

> 注：可选择打开“精细轮廓提取”，大多数情况下，使用精细轮廓都会得到更准确的材料轮廓边界，但轮廓提取过程将更加耗时，具体请参考：[精细轮廓提取](../../h2/software/bambu-suite/manual/take-photos-and-troubleshooting.md)。

|  |  |
| --- | --- |
| 022.png | 023.png |

#### Bambu Handy 手动拍照

- 点击“拍照”按钮；打印机检测到未安装俯视摄像头后，将提示打开 Bambu Handy 进行手动拍照；

|  |  |
| --- | --- |
| 024.png | 025.png |

- 打开 Bambu Handy，点击“拍照”，参考指示进行垫板拍照；

|  |  |  |
| --- | --- | --- |
| 026.png | 027.jpg | 028.jpg |

- 拍照完成后，在 Bambu Suite 中再次点击“拍照”图标，即可获取加工背景图，可在背景上调整图案至所需位置。

|  |  |
| --- | --- |
| 029.png | 030.png |

### 开启加工

- 确认无误后点击“制作”发送任务，并检查是否符合任务要求；

![031.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/031.png)

- 检查垫板和材料是否正确，并检查工具是否正确。确认完毕后，点击“发送” 。

![032.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/032.png)

### 完成加工

- 制作完成后，可取下垫板检查加工质量，并使用铲刀或钩针等工具从垫板上小心取下刀切作品；

|  |  |
| --- | --- |
| 033.png | 034.png |

- 重新贴上刀切垫板的离型膜。

> 注：正式粘贴前建议先试贴，并用粘性较弱的一面粘贴，以便后续取下离型膜。

![035.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/035.png)

> 如果加工效果不佳，可参考 wiki：[H3C 平面加工质量排查](crafttool-quality.md)进行排查。

## 校准介绍

平面加工校准分为 **“平面加工偏移校准”** 和“**平面加工调平”**。两项校准均为自主选项，可根据实际加工情况选择合适的校准。

- **平面加工偏移校准**：当多刀具的实际位置与理论位置存在偏差时，用于校准各刀具之间的偏置；
- **平面加工调平**：用于提高切割均匀性，避免出现局部切不穿或局部线条过深的情况。

### 如何开启校准

- 点击屏幕进入①“设置”页面，点击②“校准”；

![036.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/036.png)

- 选择校准类型，并安装刀切头；

![037.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/crafting-guide/zh/037.png)

- 安装完成后，启动对应校准，按屏幕提示完成操作。

### 具体动作介绍

在平面加工偏移校准与平面加工调平中，部分动作相同（工具头回中、自动检查垫板和刀切垫板偏移检测）。各动作均通过俯视摄像头在刀切垫板上进行视觉检测完成，具体动作如下：

| **流程** | **动作描述** |
| --- | --- |
| **工具头回中** | 工具头回中并取刀切头，移至工作区域中心 |
| **热床表面异物检测** | 实况摄像头拍摄热床表面，识别是否有残留耗材、碎屑等异物 |
| **自动检查垫板** **（垫板类型检测）** | 实况摄像头识别垫板上方标记，以此判断热床上是否放置了正确的刀切垫板而非打印板 Image |
| **刀切垫板偏移检测** **（垫板在位检测）** | **工具头摄像头**分别在垫板左上角和左下角拍摄两张图，通过视觉检测计算出垫板是否偏移  Image |
| **平面加工偏移校准** | 刀尖自动在材料上切割**一横一竖两道参考线**，工具头摄像头扫描参考线位置，计算刀尖实际偏移量 Image |
| **自动热床调平** | 根据检测数据自动调平热床 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
