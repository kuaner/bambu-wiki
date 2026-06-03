---
path: zh/x1/manual/X1E-firmware-update-from-SD-card
title: "通过 microSD 卡升级固件——X1E"
description: "X1E 通过 microSD 卡升级固件的步骤"
tags: ["firmware", "x1e"]
created: 2024-07-12T08:37:10.251Z
updated: 2025-06-24T11:04:13.015Z
source: https://wiki.bambulab.com/zh/x1/manual/X1E-firmware-update-from-SD-card
---

## 何时使用

- 当 X1E 不联网、无法访问拓竹云服务时，可通过 microSD 卡和离线升级包升级打印机的固件。
- 需要回退至历史固件版本。

## 前提条件

> X1E 固件版本至少为 01.01.02.00，才支持离线升级固件功能。如果固件版本低于此版本号，请先将 X1E 联网升级。

## 所需工具和材料

- microSD 卡。
- 如果电脑没有 microSD 卡读卡槽，则需要一个读卡器。

## 视频教程

[

](/x1/manual/update-firmware-from-sd-card/x1e_uncompressed1.mp4)

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
|  | 以正确的方向，将 microSD 卡插入屏幕右侧。 |
|  | 点击**格式化**。 |
|  | 确保已备份重要数据后，点击**格式化**。 |
|  | 等待片刻后，格式化成功。 |

### 步骤 2：下载对应版本的离线升级包。不同版本的功能请参见[此页面](X1E-firmware-release-history.md)。

| 版本 | 下载地址 |
| --- | --- |
| 01.01.02.00 | [点击下载](https://bambulab.cn/zh-cn/support/firmware-download/x1e) |

### 步骤 3：按压取下 microSD 卡。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/push-to-pull-out--sdcard.png)

### 步骤 4：将离线升级包复制到 microSD 卡的根目录。

> **重要提醒！**  
> 请勿修改离线升级包的文件名、解压缩离线升级包，否则将会导致无法升级。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/update-from-sdcard_(2).png)

### 步骤 5：将 microSD 插入屏幕，注意插入方向。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/insert-sdcard.png)

### 步骤 6：在打印机屏幕，选择 “设置 > 通用 > 固件版本”，然后点击右下角的“离线升级”。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/update-from-sdcard_(4).png)

### 步骤 7：选择需要升级的固件版本进行升级，大约需要 10-20 分钟，升级过程中请勿断电。

> **重要提醒！**  
> 固件升级时请勿断电，请耐心等待 10-20 分钟。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/update-from-sdcard_(5).png)

### 步骤 8：升级完成后，打印机将自动重启。

  

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
