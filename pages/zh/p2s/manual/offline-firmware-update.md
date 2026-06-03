---
path: zh/p2s/manual/offline-firmware-update
title: "通过 U 盘离线升级固件 —— X2D/P2S"
description: ""
tags: []
created: 2025-10-14T13:14:45.929Z
updated: 2026-05-07T06:22:40.003Z
source: https://wiki.bambulab.com/zh/p2s/manual/offline-firmware-update
---

## 何时使用

- 当 X2D/P2S 不联网、无法访问拓竹云服务时，可通过 U 盘和离线升级包升级打印机固件；
- 需要回退至历史固件版本时。

## 操作步骤

### 步骤 1：格式化 U 盘

- 将 U 盘插入打印机中；

![u.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/offline-firmware-update/u.jpg)

- 在打印机屏幕上点击**设置 > USB 存储 > 格式化外部存储**；

![20250912-143046.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/offline-firmware-update/20250912-143046.jpg)

- 点击**格式化**，开始格式化 U 盘。

![format-cn.png](https://wiki.bambulab.com//h2/manual/offline-firmware-update/format-cn.png)

> **注意：** X2D/P2S 的格式化只支持 FAT32。对于 2TB 以下的 U 盘，您可以选择直接在打印机上进行格式化。若您的 U 盘大于 2TB，只能先在电脑上将其格式化成 exFAT 格式。**请注意，U 盘容量特别大的情况下（比如大于 1 T），打印机识别文件和格式化需要的时间也会更长。**

### 步骤 2：下载离线升级包

点击以下链接进行下载。

- [P2S](https://bambulab.cn/zh-cn/support/firmware-download/all)
- [X2D](https://bambulab.cn/zh-cn/support/firmware-download/x2d)

![1.png](https://wiki.bambulab.com/p2s/release-note/1.png)

### 步骤 3：取下 U 盘

在打印机屏幕上点击**设置 > USB 存储 > 弹出**，将 U 盘安全弹出。

|  |  |
| --- | --- |
|  |  |

### 步骤 4：复制离线升级包

将离线升级包复制到 U 盘的根目录。

> **重要提醒！**  
> 请勿修改离线升级包的文件名、解压缩离线升级包，否则将会导致无法升级。

![](https://wiki.bambulab.com//x1/manual/update-firmware-from-sd-card/update-from-sdcard_(2).png)

### 步骤 5：插入 U 盘

重新将 U 盘插入 P2S 或 X2D 中。

![u.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/offline-firmware-update/u.jpg)

### 步骤 6：离线升级

- 在打印机屏幕上点击**设置 > 固件 > 离线升级**；

![u.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/offline-firmware-update/2025-09-12_14_46_41.png)

- 选择需要升级的固件版本进行升级，大约需要 20-30 分钟。

![离线升级--cn.png](https://wiki.bambulab.com//h2/manual/offline-firmware-update/%E7%A6%BB%E7%BA%BF%E5%8D%87%E7%BA%A7--cn.png)

> **重要提醒！**  
> 固件升级时请勿断电，请耐心等待升级完成。

- 升级完成后，打印机将自动重启。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
