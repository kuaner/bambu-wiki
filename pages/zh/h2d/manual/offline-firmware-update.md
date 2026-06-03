---
path: zh/h2d/manual/offline-firmware-update
title: "通过 U 盘离线升级固件 —— H2 系列"
description: ""
tags: []
created: 2025-05-29T11:17:00.093Z
updated: 2026-04-30T09:24:15.426Z
source: https://wiki.bambulab.com/zh/h2d/manual/offline-firmware-update
---

## 何时使用

- 当 H2D 不联网、无法访问拓竹云服务时，可通过 U 盘和离线升级包升级打印机固件；
- 需要回退至历史固件版本时。
- 如果您在将打印机升级到最新版本时未使用 AMS Hub，那么在后续接入 AMS Hub 后，也需要通过 U 盘和离线升级包**将 AMS Hub 升级至最新版本**。

## 操作步骤

### 步骤 1：格式化 U 盘

- 将 U 盘插入 H2D 中；

![](https://wiki.bambulab.com/h2/manual/usb-pecifications-and-usage-recommendations/image-10.png)

- 在打印机屏幕上点击**设置 > USB 存储 > 格式化外部存储**；

![格式化.png](https://wiki.bambulab.com/h2/manual/offline-firmware-update/%E6%A0%BC%E5%BC%8F%E5%8C%96.png)

- 点击**格式化**，开始格式化 U 盘。

![format-cn.png](https://wiki.bambulab.com/h2/manual/offline-firmware-update/format-cn.png)

> **注意：** H2D 的格式化只支持 FAT32。对于 2TB 以下的 U 盘，您可以选择直接在打印机上进行格式化。若您的 U 盘大于 2TB，只能先在电脑上将其格式化成 exFAT 格式。**请注意，U 盘容量特别大的情况下（比如大于 1 T），打印机识别文件和格式化需要的时间也会更长。**

### 步骤 2：下载离线升级包

[点击此处](https://bambulab.cn/zh-cn/support/firmware-download/h2d)下载对应版本的离线升级包。

### 步骤 3：取下 U 盘

在打印机屏幕上点击**设置 > USB 存储 > 弹出**，将 U 盘安全弹出。

![安全弹出-cn.png](https://wiki.bambulab.com/h2/manual/offline-firmware-update/%E5%AE%89%E5%85%A8%E5%BC%B9%E5%87%BA-cn.png)

### 步骤 4：复制离线升级包

将离线升级包复制到 U 盘的根目录。

> **重要提醒！**  
> **请勿修改离线升级包的文件名、解压缩离线升级包**，否则将会导致无法升级。

![](https://wiki.bambulab.com/x1/manual/update-firmware-from-sd-card/update-from-sdcard_(2).png)

### 步骤 5：插入 U 盘

重新将 U 盘插入 H2D 中。  
![](https://wiki.bambulab.com/h2/manual/usb-pecifications-and-usage-recommendations/image-10.png)

### 步骤 6：离线升级

- 在打印机屏幕上点击**设置 > 固件 > 离线升级**；

![离线升级---cn.png](https://wiki.bambulab.com/h2/manual/offline-firmware-update/%E7%A6%BB%E7%BA%BF%E5%8D%87%E7%BA%A7---cn.png)

- 选择需要升级的固件版本进行升级，大约需要 20-30 分钟。

![离线升级--cn.png](https://wiki.bambulab.com/h2/manual/offline-firmware-update/%E7%A6%BB%E7%BA%BF%E5%8D%87%E7%BA%A7--cn.png)

> **重要提醒！**  
> 固件升级时请勿断电，请耐心等待升级完成。

- 升级完成后，打印机将自动重启。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（工作日 9:00-21:00；节假日 9:00-18:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。
