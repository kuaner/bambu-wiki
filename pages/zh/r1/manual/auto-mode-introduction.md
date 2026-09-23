---
path: zh/r1/manual/auto-mode-introduction
title: "R1 自动模式介绍"
description: "本文介绍了 R1 自动模式"
tags: []
created: 2026-09-22T12:48:21.687Z
updated: 2026-09-22T12:48:22.913Z
source: https://wiki.bambulab.com/zh/r1/manual/auto-mode-introduction
---

## 自动模式介绍

R1 的自动模式针对**平面加工模式**设计，不同于常规操作，用户放置材料后，机器可自动执行拍照和距离测量操作，便于快速加工。以下为常规流程和自动模式的具体步骤：

- **常规操作流程**：

打开上盖——放入材料——点击“一键准备”按钮——点击材料距离测量；

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/001.png)

- **自动模式流程**：

打开上盖——放入材料——自动拍照——自动识别材料数量——关上盖子，识别到单个材料，机器自动测距；若识别到多材料，手动选点再测距。

## 具体操作流程

1. 打开机器上盖，放入需要加工的材料；

![002.gif](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/002.gif)

2. 进入“准备制作”页面，点击右上角“启动自动模式”；

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/003.png)

3. 机器将实时监测当前画面，静止后进行拍照；

> 拍照过程具备自动识别官方材料（带二维码）并同步材料信息的功能。

|  |  |
| --- | --- |
| 004.png | 005.png |

如果未放置加工材料，suite 会提示重新放置；

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/006.png)

4. 手动关闭上盖，机器将基于检测到的材料数量进行材料测量；

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/007.png)

- 如果检测到单个材料，机器会根据材料轮廓中心测量距离，测量结果会自动填在方框中；

![008.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/008.png)

- 如果检测到多个材料，suite 会提示手动选点测量；

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/009.png)

此时需关闭上盖，并用鼠标选择点位进行测量；

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/010.png)

测量完成后，测量结果会自动填在方框中。

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-mode-introduction/zh/011.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
