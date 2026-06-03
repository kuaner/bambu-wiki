---
path: zh/h2/troubleshooting/nozzle-detection-failed
title: "03004039：喷嘴在位检测失败，请查看帮助解决问题。"
description: ""
tags: ["h2"]
created: 2026-04-01T07:14:23.003Z
updated: 2026-04-01T08:49:00.910Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/nozzle-detection-failed
---

## 故障描述

开机校准阶段，设备将检查喷嘴是否正确安装在工具头上，当喷嘴未安装或因其他因素导致检测失败，就会提示该报错。

## 故障排除

### 步骤1. 检查喷嘴安装

如图所示，请将左侧拨片向下拨动，使其完全贴合喷嘴后，再将右侧卡扣向下扣牢。（另一喷嘴的安装操作相同，但是左右对称，注意区分）

![](https://wiki.bambulab.com/h2/17.%E6%89%A3%E7%B4%A7%E5%8D%A1%E6%89%A3.webp)

注意，卡扣错误锁紧是因为同时向下拨动拨片与卡扣，导致左侧拨片错误卡进了右侧卡扣中。

![d卡扣.jpg](https://wiki.bambulab.com/h2/maintenance/replace-hotend/d%E5%8D%A1%E6%89%A3.jpg)

向左推动 H2C 的感应热端锁紧拉柄，然后用手晃动感应热端，确保感应热端被锁紧。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-induction-hotend/019.webp)

### 步骤2. 使用 H2 适配的喷嘴

检查是否安装第三方喷嘴，或其他机型的喷嘴（如 A1/A1 mini），请使用 H2 系列适配的喷嘴。更多 H2 适配的喷嘴信息，请点击 [拓竹热端喷嘴介绍](../../filament-acc/acc/nozzles.md)查看。

| H2 系列普通喷嘴 | A1 系列普通喷嘴 |
| --- | --- |
|  |  |

### 步骤3. 检查涡流传感器安装

- H2D
- H2S
- H2C
