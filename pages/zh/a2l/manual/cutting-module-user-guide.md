---
path: zh/a2l/manual/cutting-module-user-guide
title: "A2L 刀切/画笔使用教程"
description: "本文介绍了如何在 A2L 上使用刀切/画笔功能完成 2D 作业"
tags: []
created: 2026-06-01T13:01:47.322Z
updated: 2026-07-24T06:54:18.204Z
source: https://wiki.bambulab.com/zh/a2l/manual/cutting-module-user-guide
---

## 功能简介

A2L 工具头内部集成了刀切模组转接板，可兼容刀切模组和画笔模组，用于执行切割、绘画等 2D 任务。用户可根据实际需求安装对应模组，并配合刀切垫板和多种材料完成不同类型的加工操作。以下为各模组的部件介绍及刀切模组参数表：

|  |  |
| --- | --- |
|  |  |

## 使用前准备

### 工具和材料准备

- 刀切/画笔模组
- 刀切垫板
- 加工材料

### 模型打印

建议下载并打印以下 3 个辅助工具：

- [钩针](https://makerworld.com/zh/models/1247117-bambu-weeding-tool-holder#profileId-1268887)：用于移除刀切后的废料；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/092.png)

- [刮刀](https://makerworld.com/zh/models/12702-bambu-scraper-grip#profileId-12703)：用于移除刀切粘板上的材料；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/057.png)

- [滚筒](https://makerworld.com/zh/models/1247127-bambu-roller#profileId-1268902)：用于压平刀切对象，确保刀切精度；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/136.png)

这些工具可用于后续任务中的多种操作。具体请参考[模切模组辅助工具（钩针、刮刀与滚筒）的使用介绍](../../h2/manual/cutting-module-assist-tool.md)。

### 固件/软件版本

- 固件版本：01.01.00.00 及以上
- Bambu Suite：1.3.0.0 及以上
- Bambu Handy：3.21.0 及以上

## 视频指南

## 刀切模组使用流程

### 安装刀切模组

> **注意：如果您的喷嘴内有料，请先进行退料，移除所有料管后再安装刀切模组。**

- 抬升 X 轴至 Z 轴中间位置；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/147.png)

- 取下打印板；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/024.png)

- 放置刀切垫板，注意对齐热床边缘；

|  |  |
| --- | --- |
|  |  |

- 撕下刀切垫板的透明保护膜；

> **注意：**请勿随意丢弃透明保护膜，垫板不使用时需覆盖透明保护膜以保护胶层，否则垫板表面容易粘上灰尘和碎屑，造成脏污并过早失去粘性。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/035.png)

- 握住工具头前盖下部，注意避开热端风扇位置，向上抬起，取下工具头前盖；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/018.webp)

- 拆下旋转轮；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/114.png)

- 取出刀切模组，确认快拆锁扣处于解锁状态；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/103.png)

将刀切模组对准工具头的滑槽，从上往下将模组滑到底；

|  |  |
| --- | --- |
|  |  |

- 向下按压，锁紧快拆锁扣；

|  |  |
| --- | --- |
|  |  |

- 打开工具头扩展接口处的防尘塞；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/074.png)

将刀切模组的连接线对准接口插入；

|  |  |
| --- | --- |
|  |  |

- 取下刀尖上的保护套，请小心操作避免受伤。

> 建议保存好保护套，可在拆装时保护整个刀尖。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/069.png)

- 点击屏幕“校准”，开始进行刀切模组挂载校准。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/004.jpg)

> 关于挂载校准和垫板检测的详细内容，请参考后文：[挂载校准和垫板检测流程介绍](https://wiki.bambulab.com/zh/a2l/manual/cutting-module-user-guide#%E6%8C%82%E8%BD%BD%E6%A0%A1%E5%87%86%E5%92%8C%E5%9E%AB%E6%9D%BF%E6%A3%80%E6%B5%8B%E6%B5%81%E7%A8%8B%E4%BB%8B%E7%BB%8D)。

### 开启刀切作业

- 打开 Bambu Handy 扫描绑定打印机，并打开 Bambu Suite 登录账号；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/066.png)

- 在 Bambu Suite 画布中导入想要加工的图案；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/068.png)

- 选择“基础刀切”；有关 2D 制作的更多介绍请参考：[2D 制作工艺介绍](../../software/bambu-suite/manual/2d-processing-type-intro.md)；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/067.png)

- 把需要加工的材料粘附在刀切垫板上；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/065.png)

并用滚筒工具使其完全贴合；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/073.png)

- 在 Bambu Suite 右下角点击“准备制作”；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/064.png)

- 在最右侧“材料组”中选择加工的材料类型；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/093.png)

- 点击“拍照”；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/090.png)

- 打开 Bambu Handy ，点击“拍照”；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/022.jpeg)

参考指示进行垫板拍照；

> **注意：拍照时需避免 X 轴遮挡垫板，否则很可能导致拍照不通过！**

|  |  |
| --- | --- |
|  |  |

- 在 Bambu Suite 中再次点击“拍照”图标，即可获取加工背景图；

|  |  |
| --- | --- |
|  |  |

- 在背景上调整图案至所需位置；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/085.png)

- 确认无误后点击“制作”发送任务，并检查是否符合任务要求；

|  |  |
| --- | --- |
|  |  |

- 在打印机屏幕点击“制作”；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/083.png)

- 制作完成后，使用铲刀或钩针等工具从垫板上小心取下刀切作品；

|  |  |
| --- | --- |
|  |  |

- 重新贴上刀切垫板的透明保护膜，并取下刀切垫板；

|  |  |
| --- | --- |
|  |  |

- 解锁快拆锁扣，断开刀切模组连接线，将模组向上滑出。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/016.webp)

## 画笔模组使用流程

### 安装画笔模组

- 取下画笔转接件上的定高块，并安装至转接件的下方；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/012.webp)

- 逆时针拧松画笔锁定器；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/107.png)

将画笔插入到底；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/106.png)

触碰到定高块底部后，顺时针拧紧锁定器；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/105.png)

- 小心向下拔出刀尖；

> 刀头十分锋利，请小心操作，避免手指直接触碰刀头导致划伤！

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/101.png)

- 将画笔插入刀切模组的刀座中；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/104.png)

取下画笔定高块，安装完成。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/099.png)

- 检查屏幕是否出现“笔”的在位标识。如未出现，则说明画笔模组未安装到位，请重新将画笔模组向上推，卡入刀座中。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/102.png)

### 开启画笔作业

> **画笔不支持挂载校准**；若机器在画笔作业前弹出挂载校准的提示，请先换回刀尖再进行挂载校准。

- 打开 Bambu Handy 扫描绑定打印机，并打开 Bambu Suite 登录账号；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/097.png)

- 在 Bambu Suite 画布中导入想要加工的图案；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/098.png)

- 在工艺类型中选择“线条绘画”或“填充绘画”；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/100.png)

- 把需要加工的材料粘附在刀切垫板上；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/094.png)

并用滚筒工具使其完全贴合；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/096.png)

- 在 Bambu Suite 中点击“准备”；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/095.png)

- 在最右侧“材料组”中选择加工的材料类型；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/123.png)

- 点击“拍照”标识；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/122.png)

- 打开 Bambu Handy ，点击“拍照”；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/121.png)

参考指示进行垫板拍照；

> **注意：拍照时尽量避免 X 轴遮挡垫板，否则很可能导致拍照不通过!**

|  |  |
| --- | --- |
|  |  |

- 在 Bambu Suite 中再次点击“拍照”图标，即可获取加工背景图；

|  |  |
| --- | --- |
|  |  |

- 在加工背景上调整图案至所需位置；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/116.png)

- 确认无误后再点击右下角“制作”发送任务，并检查是否符合任务要求；

|  |  |
| --- | --- |
|  |  |

- 在打印机屏幕点击“制作”；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/111.png)

- 绘画完成后，使用铲刀或钩针等工具从垫板上小心取下作品；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/115.png)

- 重新贴上刀切垫板的透明保护膜，并取下刀切垫板；

|  |  |
| --- | --- |
|  |  |

- 向下拔出画笔模组；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/110.png)

- 解锁快拆锁扣，断开刀切模组连接线，将模组向上滑出。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/013.webp)

## 挂载校准和垫板检测流程介绍

### 挂载校准

在正式使用刀切模组加工之前，需要对刀切模组进行挂载校准。当机器判断需要进行刀切挂载校准时，首页会弹出对应的提示。每次打印机重新上电，也需要进行一次刀切模组挂载校准，目的是帮助刀切模组回中与调平。

> 注意：需安装刀尖进行挂载校准，不可安装画笔。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/001.jpg)

您也可以在“设置”中找到“挂载校准”入口。

|  |  |
| --- | --- |
|  |  |

校准时，刀切模组会在刀切垫板整体范围内进行 5 点触碰试探，以此来判断是否进行全局调平。若校准结果与上次差异较大，则会进行全局调平，若不需要则跳过全局调平，结束校准流程。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/006.webp)

### 垫板检测

设备在挂载校准和作业任务开始前均会进行一次刀切垫板检测，分为在位检测和垫板类型检测。

- **在位检测：**用画笔触碰垫板底部凸出的部分，以确认热床上是否放置了垫板；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/010.webp)

- **垫板类型检测：**用刀尖在垫板左侧 marker 内外分别触碰一下，由于 marker 内部和外部存在细微的高度差，设备会根据检测到的高度变化判断热床上是否放置了正确的刀切垫板，而非打印板。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/cutting-module-user-guide/008.webp)

进行 2D 任务时，设备会在**挂载校准**和**作业任务开始前**进行检测，具体的检测时机及原因请参考下表：

|  | 挂载校准时 | 作业任务开始前 | 说明 |
| --- | --- | --- | --- |
| **刀切模组** | 垫板类型检测 | 垫板类型检测 | 垫板类型检测已包含在位判断功能，因此无需再单独执行在位检测。 |
| **画笔模组** | / | 在位检测 | 画笔模组不支持挂载校准，且使用画笔触碰 marker 会弄脏垫板，因此仅执行在位检测。 |

## 定期维护

为了延长刀切/画笔模组的使用寿命，保持其最佳工作状态，定期维护至关重要。

**刀座**

定期检查刀座在工具头是否安装到位。确保锁紧快拆锁扣后，模组不会晃动。如出现晃动，需要锁紧快拆锁扣的螺丝。

**刀尖**

定期拧开端盖，清理耗材碎屑，避免碎屑堆积阻碍刀头旋转。

**消耗品**

- 定期检查垫板的粘性，必要时进行更换，确保材料被牢牢固定。
- 随着使用时间增加，刀尖会出现磨损，导致刀切质量下降。请定期更换刀尖，保证刀切质量。
- 不同的耗材也会影响刀头的使用寿命，更多信息请查阅官方 Wiki。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
