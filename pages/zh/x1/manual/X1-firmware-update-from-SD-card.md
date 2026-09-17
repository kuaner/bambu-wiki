---
path: zh/x1/manual/X1-firmware-update-from-SD-card
title: "通过 microSD 卡升级固件 ——X1/X1C"
description: "X1/X1C 通过 microSD 卡升级固件的步骤"
tags: ["firmware", "x1", "x1c"]
created: 2024-08-12T02:12:04.196Z
updated: 2026-08-28T08:29:31.294Z
source: https://wiki.bambulab.com/zh/x1/manual/X1-firmware-update-from-SD-card
---

## 何时使用

- 当 X1/X1C 不联网、无法访问拓竹云服务时，可通过 microSD 卡和离线升级包升级打印机的固件。
- 需要回退至历史固件版本。
- 如果您在将打印机升级到最新版本时未使用 AMS Hub，那么在后续接入 AMS Hub 后，也需要通过 micro SD 卡和离线升级包**将 AMS Hub 升级至最新版本**。

## 前提条件

> X1/X1C 固件版本至少为 01.08.02.00，才支持离线升级固件功能。如果固件版本低于此版本号，请先将 X1/X1C 联网升级。

## 所需工具和材料

- microSD 卡。
- 如果电脑没有 microSD 卡读卡槽，则需要一个读卡器。

## 视频教程

<https://public-cdn.bblmw.com/wiki/X1/manual/offline-firmware-update.mp4>

## 操作步骤

> 整个过程大约需要 30 分钟。

### （可选）步骤 1：格式化 microSD 卡。

如果 microSD 的格式为 **FAT32**，则可以跳过此步骤。

> 打印机目前仅支持 FAT32 格式的 microSD 卡。对于 Windows 操作系统来说，如果 microSD 卡容量超过 32GB，则默认格式化为 exFAT，而 Linux 和 Mac OS 这两种操作系统则没有此格式限制。如果需要使用容量为 64GB 至 2TB 的 microSD 卡，则可以使用 Linux 或 Mac OS 操作系统的电脑，或者用打印机将其格式化为 FAT32。

推荐根据此步骤，在打印机上对 microSD 进行格式化，可确保 microSD 的格式为 FAT32。

> **重要提醒！**  
> 格式化会删除 microSD 中的所有数据，请确保在格式化前备份重要数据！

|  |  |
| --- | --- |
|  | 以正确的方向，将 microSD 卡插入屏幕。 |
|  | 点击**格式化**。 |
|  | 确保已备份重要数据后，点击**格式化**。 |
|  | 等待片刻后，格式化成功。 |

### 步骤 2：下载对应版本的离线升级包。

- 请参见 [拓竹固件下载 | Bambu Lab CN](https://bambulab.cn/zh-cn/support/firmware-download/x1) 下载对应版本的离线升级包。
- 请参见 [X1/X1C 固件发布记录 | Bambu Lab Wiki](X1-X1C-firmware-release-history.md) 查看不同版本的功能。

### 步骤 3：按压取下 microSD 卡。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/push-to-pull-out--sdcard-x1.png)

### 步骤 4：将离线升级包复制到 microSD 卡的根目录。

> **重要提醒！**  
> 请勿修改离线升级包的文件名、解压缩离线升级包，否则将会导致无法升级。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/update-from-sdcard_(2).png)

### 步骤 5：将 microSD 插入屏幕，注意插入方向。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/insert-sdcard-x1.png)

### 步骤 6：在打印机屏幕，选择 “设置 > 通用 > 固件版本”，然后点击右下角的“离线升级”。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/update-from-sd-card-x1_(1).jpg)

### 步骤 7：选择需要升级的固件版本进行升级，大约需要 10-20 分钟，升级过程中请勿断电。

> **重要提醒！**  
> 固件升级时请勿断电，请耐心等待 10-20 分钟。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/update-from-sd-card-x1_(1).jpg)

### 步骤 8：升级完成后，打印机将自动重启。

  

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
