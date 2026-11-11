---
path: zh/ams3/manual/component-introduction
title: "AMS 3H 部件介绍"
description: "本文介绍了 AMS 3H 的主要部件及功能。"
tags: []
created: 2026-11-03T13:23:44.371Z
updated: 2026-11-10T08:46:57.770Z
source: https://wiki.bambulab.com/zh/ams3/manual/component-introduction
---

## AMS 3H

AMS 3H 是适配拓竹H3C 的智能供料设备，可实现多色 / 多材料打印、自动进料与续料，还具备耗材烘干防潮保护、耗材信息识别等功能，能减少手动操作，提升打印效率与智能化程度。本文将介绍 AMS 3H 的主要部件及功能。

![001.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/001.png)

## 料管导向组件

料管导向组件安装在 AMS 3H 正下方，用于衔接 AMS 3H 与料管架组件。为了优化进料路径并降低阻力，系统中包含两类连接件：

- **直列料管连接件**：对应 1–2、3–4、7–8、9 号料管；
- **分叉料管连接件**：对应 5–6 号料管。

![002.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/002.png)

料管导向组件上方共有 5 对孔位，分别对应 1-2、3-4、5-6、7-8 和 9 号槽位，打印机通过 AMS 3H 自动进料组件完成选料和送料操作，可将耗材通过导向支架送至对应的路径中，最终送入打印头内。

![003.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/003.png)

## 料管支架组件

料管支架组件分为主料管支架、左料管支架和右料管支架，避免料管垂放至机箱内部；

- **主料管支架：** 位于料管导向支架正下方，用于固定 9 个打印头的线缆和料管；

![005.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/005.png)

- **左料管支架：** 用于固定左侧的 5 根料管（1-5 号）；

![006.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/006.png)

- **右料管支架：** 用于固定右侧的 4 根料管（6-9 号）。

![007.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/007.png)

## 撑杆组件

AMS 3H 有左右两个撑杆组件，完全打开 AMS 上盖后松手，撑杆可撑住上盖；再次完全打开上盖，即可释放撑杆，向下可合上上盖。

![008.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/008.png)

## 自动进料组件

自动进料组件将 AMS 分为上下两部分，上方包含 4 个槽位，分别对应 2、4、6、8 号上下料料嘴；下方包含 5 个槽位，分别对应 1、3、5、7、9 号料嘴。

![009.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/009.png)

自动进料组件包含两个电机：**选料电机**和**送料电机**，统一控制 9 个料槽。

1. **选料电机**：驱动选料杆在左右方向移动，定位并锁定需要进料的槽位；
2. **送料电机**：驱动送料挤出轮，将已选中槽位中的耗材压出并送入打印头。

![010.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/010.png)

自动进料组件的工作流程如下：

1. 当某个槽位需要供料时，选料电机将送料选择器左右移动进行槽位选择，并把齿轮咬入某一槽位的定位孔，完成选料动作，此时其余槽位保持空闲状态；
2. 选料完成后，送料电机启动，挤出轮把耗材推入料管内，耗材进入工具头即标志送料结束，此时进料组件为空闲状态，由挤出电机直接拉动耗材进行进退料。

通过**选料/送料**两个电机的协同控制，AMS 3H 能在 9 个槽位之间快速切换，实现多色或多材料打印时的稳定、连续供料。

![011.webp](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/011.webp)

## 耗材信息读取

AMS 3H 配备了 7 个线圈（前面 4 个，后面 3 个），可以识别 Bambu Lab 官方耗材上的标签，并支持耗材自动续料等功能。

将料盘放入槽位后，将耗材末端插入上下料料嘴 70 mm，AMS 即可预上料并自动读取耗材信息。

![012.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/012.png)

## 烘干防潮系统

### 烘干模块

AMS 3H 配备了一组烘干模块，由加热片、风扇以及 NTC 温度传感器构成。在 9 个耗材插槽中，**只有 2 个插槽具备烘干功能**，最大烘干温度可达 **85℃。**这两个具有烘干功能的插槽上额外配有可磁吸快拆的**耗材烘干仓盖**，能够有效去除耗材中的水分，提升打印质量。

![013.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/013.png)

### 进出气口

AMS 3H 的进出气口位于烘干模块侧面，配备主动开关的进气和出气风门。

在烘干耗材时，AMS 3H 会通过外循环的方式将湿气从内部排出。进行外循环时，进气口和出气口会打开，**请确保进气口和出气口不被其他物品遮挡**，以获得最佳烘干效果。

![014.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/014.png)

### 温湿度传感器

AMS 3H 在烘干仓和非烘干仓中分别配备了一个温湿度传感器，可以分别检测两个仓内的温度和湿度。您可以在打印机屏幕 / Bambu Studio / Bambu Handy 中查看 AMS 当前的湿度状态。

![015.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/015.png)

### 干燥剂和密封胶圈

AMS 3H 出厂配备**变色硅胶干燥剂**，可放置在撑杆旁及烘干仓盖内。干燥剂吸收水分，保持舱内空气干燥。吸湿后，黄色颗粒会变为深绿色，此时需要更换或烘干干燥剂后重复使用。上盖与外壳之间的橡胶密封圈可保持 AMS 的密封性，防止外部湿气进入。当湿度超出预设标准时，湿度传感器会提醒用户。

标配 80g 硅胶干燥剂，共 8 小包，烘干槽上盖的槽位最多可以放 4 小包，其他可以放在腔体内其他干燥剂槽位；如果对湿度要求特别高，也可以自己额外购买干燥剂放在 8 号槽右侧的槽位内。

> **注意**：干燥剂需从密封透明袋中取出后再放入 AMS。

|  |  |
| --- | --- |
| 016.png | 017.png |

## 腔体散热风扇

该风扇的核心功能是提升系统散热效率。由于拓竹H3C 腔体体积较大，装配 AMS 后，腔体整体高度随之增加，且外排冷却需经滤芯过滤，这在一定程度上会削弱散热效果。因此，为进一步加强上部腔体的散热能力，AMS 背板处专门增设了“吸入式”的腔体散热风扇，增强散热。

![018.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/018.png)

> 注意：请勿将热源置于散热风扇附近。例如，请勿将 AMS 2 Pro 紧贴 AMS 3H 摆放，以免吸入 AMS 2 Pro 烘干排出的热风，从而导致散热风扇失效或设备过热。

## 耗材直通口

AMS 3H 设有 7 个专用的 TPU 进料口，无需通过料管即可直接将 TPU 耗材输送至工具头进行打印，从而降低打印阻力。关于 TPU 打印的具体步骤请参考：[TPU 打印指南](../../h3c/manual/tpu-printing-guide.md)。

![019.png](https://public-cdn.bblmw.com/wiki/new/ams3/manual/component-introduction/zh/019.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
