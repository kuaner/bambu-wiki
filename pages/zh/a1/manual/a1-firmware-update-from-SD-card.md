---
path: zh/a1/manual/a1-firmware-update-from-SD-card
title: "通过 microSD 卡升级固件——A1/A2L"
description: "A1/A2L 通过 microSD 卡升级固件的步骤"
tags: ["a1"]
created: 2024-11-25T08:15:53.820Z
updated: 2026-06-04T02:13:54.393Z
source: https://wiki.bambulab.com/zh/a1/manual/a1-firmware-update-from-SD-card
---

## 何时使用

- 当 A1 不联网、无法访问拓竹云服务时，可通过 microSD 卡和离线升级包升级打印机的固件。
- 需要回退至历史固件版本。
- 如果您在将打印机升级到最新版本时未使用 AMS Hub，那么在后续接入 AMS Hub 后，也需要通过 microSD 卡和离线升级包**将 AMS Hub 升级至最新版本**。

## 前提条件

> A1 固件版本至少为 01.04.00.00，才支持离线升级固件功能。如果固件版本低于此版本号，请先将 A1 联网升级。

## 所需工具和材料

- microSD 卡。
- 如果电脑没有 microSD 卡读卡槽，则需要一个读卡器。

## 操作步骤

> 整个过程大约需要 20 分钟。

### 步骤 1：下载对应版本的离线升级包。不同版本的功能请参见[此页面](a1-firmware-release-history.md)。

A1:

| 版本 | 下载地址 |
| --- | --- |
| 01.04.00.00 | [点击下载](https://bambulab.cn/zh-cn/support/firmware-download/a1) |

### 步骤 2：取出 microSD 卡。

A 系列 **不支持热插拔卡**，因此每次取出 SD 卡时，**请务必从菜单中安全弹出**，具体步骤如下：

- 进入 **设置 → SD 卡**
- 在 SD 卡菜单中点击**弹出**
- 点击**是**，确认选项

![a1-弹出sd.jpg](https://wiki.bambulab.com/a1-sd/a1-%E5%BC%B9%E5%87%BAsd.jpg)

只需按下 SD 卡再松开，即可将其从打印机中弹出。

![](https://wiki.bambulab.com/a1/manual/print-from-sd-card/a1_micro_sd_card.jpeg)

### 步骤 3：将离线升级包复制到 microSD 卡的根目录。

> **重要提醒！**  
> 请勿修改离线升级包的文件名、解压缩离线升级包，否则将会导致无法升级。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/update-from-sdcard_(2).png)

### 步骤 4：将 microSD 插入屏幕，注意插入方向。

![](https://wiki.bambulab.com/a1/manual/print-from-sd-card/a1_micro_sd_card.jpeg)

### 步骤 5：在打印机屏幕，选择 “设置 > 固件 > 离线更新”。

![](https://wiki.bambulab.com/a1-mini/manual/update-firmware-from-sd-card/setting-firmware.png)

### 步骤 6：选择需要升级的固件版本进行升级，大约需要 5-10 分钟，升级过程中请勿断电。

> **重要提醒！**  
> 固件升级时请勿断电，请耐心等待 10-20 分钟。

![](https://wiki.bambulab.com/a1-mini/manual/update-firmware-from-sd-card/firmware-list.png)

### 步骤 7：升级完成后，打印机将自动重启。

  

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)
