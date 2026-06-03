---
path: zh/h2/manual/PPA-PPS-printing-guide
title: "H2S PPA/PPS-CF 打印指南"
description: "本文将详细介绍使用 H2S 打印 PPA 及 PPS 的方法和注意事项。"
tags: []
created: 2025-08-26T08:57:43.432Z
updated: 2026-02-09T09:46:45.524Z
source: https://wiki.bambulab.com/zh/h2/manual/PPA-PPS-printing-guide
---

## 引言

PPA-CF 与 PPS-CF 属于高强度、高刚度及高耐热的特种工程耗材。由于其刚度和硬度较高，耗材在 AMS 齿轮或 PTFE 料管内部容易产生磨损或脆断问题。本文将介绍如何在 H2S 打印机上正确进料并稳定打印 PPA-CF 与 PPS-CF。

以下为常见的进料错误案例：铁氟龙管在机箱边缘发生过度弯折，导致耗材在管内脆断。

![](https://wiki.bambulab.com/h2s/manual/dsc00170.png)

## 耗材干燥

在正式打印之前，必须对耗材进行充分干燥。PPA-CF 和 PPS-CF 对湿度极其敏感，若受潮会导致拉丝、漏料等打印质量问题。强烈建议在完全干燥后再使用。

烘干参数参考下表：

![pixpin_2025-08-28_19-53-13.png](https://wiki.bambulab.com/h2s/manual/ppa-pps-printing-guide/pixpin_2025-08-28_19-53-13.png)

耗材干燥参考：[耗材准备——干燥](../../filament-acc/filament/dry-filament.md)

耗材干燥完成后，应立即放置于带干燥剂的密封盒中，以防再次吸潮。打印过程中需保持密封盒盖紧，确保湿度低于 20% RH。

![](https://wiki.bambulab.com/h2s/manual/image.png)

## 进料步骤

### 1. 调整 PTFE 料管

打开机器上盖，将 PTFE 料管从工具头拔出，并从拖链中抽出。

![](https://wiki.bambulab.com/h2s/manual/%E6%8B%94%E5%87%BA.webp)

将 PTFE 料管逆时针旋转 360°，以螺旋方式重新插入工具头，避免当工具头移动至机箱右侧时出现弯折，导致 PPA-CF 或 PPS-CF 脆断。

![](https://wiki.bambulab.com/h2s/manual/%E6%97%8B%E8%BD%AC.webp)

完成旋转后的状态如下：

![](https://wiki.bambulab.com/h2s/manual/2025-08-27_193627_422.jpg)

### 2. 安装进料管

准备一段约 15 cm 的 PTFE 料管。

![](https://wiki.bambulab.com/h2s/manual/image-1.png)

将其插入打印机后方的进料口。（注意需要插入到底）

![](https://wiki.bambulab.com/h2s/manual/2025-08-28_170433_735.jpg)

将密封盒放置在进料口右后侧，并调整高度，以减小进料阻力，避免耗材弯折。

![](https://wiki.bambulab.com/h2s/manual/dsc00176_compressed.jpg)

正确摆放方式如下图所示：

![](https://wiki.bambulab.com/h2s/manual/dsc00174_compressed.jpg)

### 3. 进料

手动将耗材送入工具头齿轮啮合处。将热端加热至 340 ℃，点击“下箭头”开始进料。

![](https://wiki.bambulab.com/h2s/manual/dsc00177_compressed.jpg)

确认耗材可连续、稳定地挤出后，盖上上盖，即可开始打印。

![](https://wiki.bambulab.com/h2s/manual/%E6%8C%A4%E5%87%BA.webp)

## 退料步骤

打印完成后，清理打印平台上的模型，在耗材页点击“退料”，机器会自动执行退料流程。

![](https://wiki.bambulab.com/h2s/manual/dsc00179_compressed.jpg)

待退料提示出现后，手动从进料口抽出耗材，该提示页面即可消失。

![](https://wiki.bambulab.com/h2s/manual/dsc00181_compressed.jpg)

![](https://wiki.bambulab.com/h2s/manual/dsc00183_compressed.jpg)

确认 PTFE 料管内无残余耗材。打开机器上盖，将料管从工具头拔出，顺时针旋转 360° 复位。重新将 PTFE 料管穿过拖链固定架，插入工具头接口，恢复初始状态。

![](https://wiki.bambulab.com/h2s/manual/%E5%A4%8D%E5%8E%9F.webp)

恢复后的正常状态如下图所示：

![](https://wiki.bambulab.com/h2s/manual/dsc00188_compressed.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
