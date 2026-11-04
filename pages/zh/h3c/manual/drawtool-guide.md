---
path: zh/h3c/manual/drawtool-guide
title: "H3C 画笔加工介绍"
description: ""
tags: []
created: 2026-11-03T12:12:28.711Z
updated: 2026-11-03T14:30:18.996Z
source: https://wiki.bambulab.com/zh/h3c/manual/drawtool-guide
---

## 功能简介

H3C 可兼容多种工具，包括打印头和平面加工头（刀切头/画笔头），在平面加工头基座上安装刀座/笔座及对应的刀头和画笔，可执行切割、绘画、烫金、压痕等 2D 任务。用户可根据实际需求安装对应工具，并配合刀切垫板和多种材料完成不同类型的加工操作。

## 工具介绍

### 画笔头

可实现绘画等工艺的画笔头 = **平面加工头基座 + 笔座 + 对应画笔**，用于在平面材料上完成绘画、填色和图案绘制。

**平面加工基座**

平面加工头基座底部带有螺纹，可旋转固定刀座或笔座。

![001.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/001.png)

**笔座**

画笔的安装载体，负责固定画笔，并在绘制时提供稳定的下压力。

![002.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/002.png)

**彩色画笔**

不同颜色画笔带有不同 maker；用于多色 2D 绘画，可按颜色分区上色，完成插画、填色、装饰图案等平面绘制任务。

![003.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/003.png)

**画笔补墨**

为彩色画笔补充墨水，延长单支画笔的使用时间。画笔补墨步骤请参考 wiki：[补墨教程](marker-refill-guide.md)。

> 为了安全，请将其放置在儿童接触不到的地方，避免误食。

![004.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/004.png)

### 刀切垫板

刀切垫板由刀切保护钢板和刀切粘板组成，刀切工作开始前需要把加工的材料贴在粘板表面，用于在加工过程中固定耗材。

![005.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/005.png)

## 加工前准备

### 工具和材料

- 画笔头
- 刀切垫板
- 加工材料

### 辅助工具打印

| **模型名称** | **作用** | **示意图** |
| --- | --- | --- |
| **钩针：** [下载链接](https://makerworld.com.cn/zh/models/1068224-tuo-zhu-gou-zhen-wo-bing#profileId-1109145) | 移除废料 | Image |
| **刮刀：** [下载链接](https://makerworld.com.cn/zh/models/125813-tuo-zhu-re-chuang-gua-dao#profileId-8923) | 移除刀切垫板上的材料 | Image |
| **滚筒：** [下载链接](https://makerworld.com.cn/zh/models/1068223-tuo-zhu-gun-tong#profileId-1109144) | 压平材料，确保加工精度 | Image |
| **补墨盒** | 装载墨水，放置画笔进行补墨 | Image |
| **替换笔头推杆** | 辅助安装，将笔头完全推动至画笔中，同时不损伤笔头 | Image |

> 注：辅助工具可用于后续任务中的多种操作。具体请参考[模切模组辅助工具（钩针、刮刀与滚筒）的使用介绍](../../h2/manual/cutting-module-assist-tool.md)。

## 加工流程

### 安装画笔头和刀切垫板

请参考[平面加工头开箱指南](unboxing-crafttool.md)安装画笔头和刀切垫板。

### 安装俯视摄像头（选做）

请参考[俯视摄像头更换指南](../maintenance/replace-birdseye-camera.md)安装俯视摄像头。

> 注意：未选配俯视摄像头时，无法在 Bambu Suite 中直接拍照对位，但可用 Bambu Handy 拍照完成对位（参考后文“Bambu Handy 手动拍照”）。如需体验更顺畅的平面加工流程，建议选购俯视摄像头。

### 加工准备

- 在打印机屏幕上设置正确的加工头信息，并取用；

|  |  |
| --- | --- |
| 011.png | 012.png |
| 013.png |

- 打开 Bambu Handy 扫描绑定打印机，并打开 Bambu Suite 登录账号，在画布中导入想要加工的图案；

![014.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/014.png)

- 在“工艺类型”中选择“线条绘画”或“填充绘画”；

![015.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/015.png)

- 点击“画笔编辑”按钮，选择取用的画笔类型、规格及颜色；

![016.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/016.png)

- 在右下角点击“准备制作”；

![017.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/017.png)

- 把需要加工的材料粘附在刀切垫板上，并用滚筒工具使其完全贴合，然后安装刀切垫板；

|  |  |
| --- | --- |
| 018.png | 019.png |

- 在最右侧“材料组”中选择加工的材料类型。

![020.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/020.png)

### 拍照对位

#### 俯视摄像头自动拍照

点击“拍照”，俯视摄像头将自动拍照。

> 注：可选择打开“精细轮廓提取”，大多数情况下，使用精细轮廓都会得到更准确的材料轮廓边界，但轮廓提取过程将更加耗时，具体请参考：[精细轮廓提取](../../h2/software/bambu-suite/manual/take-photos-and-troubleshooting.md)。

|  |  |
| --- | --- |
| 021.png | 022.png |

#### Bambu Handy 手动拍照

- 点击“拍照”按钮；打印机检测到未安装俯视摄像头后，将提示打开 Bambu Handy 进行手动拍照；

|  |  |
| --- | --- |
| 023.png | 024.png |

- 打开 Bambu Handy，点击“拍照”，参考指示进行垫板拍照；

|  |  |  |
| --- | --- | --- |
| 025.png | 026.jpg | 027.jpg |

- 拍照完成后，在 Bambu Suite 中再次点击“拍照”图标，即可获取加工背景图，可在背景上调整图案至所需位置。

![028.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/028.png)

### 开启加工

- 确认无误后点击“制作”发送任务，并检查是否符合任务要求；

![029.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/029.png)

- 检查垫板和材料是否正确，并检查画笔类型是否正确；确认完毕后，点击“发送”。

![030.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/030.png)

> 注：如果只有一个槽位可用画笔头，但想使用不同颜色的画笔，此时可选择“制作中更换”，机器会在特定时间暂停任务，提醒用户换笔，然后继续加工。
>
> |  |  |
> | --- | --- |
> | 031.png | 032.png |

### 完成加工

- 制作完成后，取下刀切垫板检查加工质量，并使用铲刀或钩针等工具从垫板上小心取下作品；

|  |  |
| --- | --- |
| 033.png | 034.png |

- 重新贴上刀切垫板的离型膜。

> 注：正式粘贴前建议先试贴，并用粘性较弱的一面粘贴，以便后续取下离型膜。

![035.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/drawtool-guide/zh/035.png)

> 如果加工效果不佳，可参考 wiki：[H3C 平面加工质量排查](crafttool-quality.md)进行排查。

## 校准介绍

安装画笔头时，可进行“**平面加工偏移校准**”；当多刀具的实际位置与理论位置存在偏差时，用于校准各刀具之间的偏置。

### 如何开启校准

- 点击屏幕进入①“设置”页面，点击②“校准”，选择“平面加工偏移校准”。

|  |  |
| --- | --- |
| 036.png | 037.png |

> **注意**：安装画笔头时，只可进行平面加工偏移校准；如需进行平面加工调节，请安装刀切头。

### 具体动作介绍

在平面加工偏移校准中，各动作均通过俯视摄像头在刀切垫板上进行视觉检测完成，具体动作如下：

| **流程** | **动作描述** |
| --- | --- |
| **工具头回中** | 工具头回中并取刀切头，移至工作区域中心 |
| **自动检查垫板** **（垫板类型检测）** | 实况摄像头识别垫板上方标记，以此判断热床上是否放置了正确的刀切垫板而非打印板 Image |
| **刀切垫板偏移检测** **（垫板在位检测）** | **工具头摄像头**分别在垫板左上角和左下角拍摄两张图，通过视觉检测计算出垫板是否偏移  Image |
| **平面加工偏移校准** | 刀尖自动在材料上切割**一横一竖两道参考线**，工具头摄像头扫描参考线位置，计算刀尖实际偏移量 Image |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
