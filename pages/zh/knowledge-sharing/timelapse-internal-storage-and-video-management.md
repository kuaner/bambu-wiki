---
path: zh/knowledge-sharing/timelapse-internal-storage-and-video-management
title: "延时摄影内置存储和素材管理"
description: "本文介绍了如何将延时摄影文件保存至内置存储以及文件素材管理功能"
tags: []
created: 2026-04-02T11:55:40.144Z
updated: 2026-04-16T04:01:09.494Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/timelapse-internal-storage-and-video-management
---

## 概述

P2S/X2D 新增了将延时摄影文件保存到内置存储的功能，该功能允许打印机在未挂载外部存储的情况下，也能保存打印过程的延时视频素材。同时，P2S/X2D 支持内置存储的素材文件管理，可直接在屏幕查看素材列表，根据需要将素材导出到外部存储或者删除。

## 功能亮点

1. **摆脱外部存储束缚：**即使不插入外部存储设备，也能自动保存延时摄影素材；
2. **机身文件管理：**支持在打印机上直接管理内置存储中的摄影文件，无需连接电脑或手机，即可通过机身随时浏览素材列表（当前不支持在机身直接播放视频，需要在studio或者handy端下载查看）。
3. **灵活导出：**支持将内置存储中的素材一键导出到外部存储，方便用户在需要时快速转移文件。

## 支持机型与开放计划

1. **P2S**：01.02.00.00  
   **X2D**：01.01.00.00  
   其他机型将在后续通过固件更新的方式逐步支持
2. **Bambu Studio**：版本不低于 2.5.3  
   **Bambu Handy**：版本不低于 3.17.0

> 注意：
>
> - 请保持打印机、Studio 和 Handy 均为最新版本，以获得最佳使用体验。
> - 在存储容量不足的场景下，若开启延时摄影，打印过程中新素材会自动覆盖旧素材。
> - 在存储设备异常（只读/格式不匹配需要格式化）的场景下，素材会自动保存到内置存储。

## 将延时摄影文件保存到内置存储

### 从设备端发起打印

- 发起打印时，需打开延时摄影开关，并在高级选项中进行延时摄影的相关设置。

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/004.png)

- 未插入 U 盘时，延时摄影素材将默认保存至内置存储。已插入 U 盘时，可在此选择素材保存的位置。

  > 注意：每次打印任务将默认保存至机内存储；如需使用外部存储，需手动进行设置。

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/003.png)

- 发起打印后，屏幕中文件视图的左上角会出现延时摄影图标，表示正在录制延时摄影素材。

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/005.png)

### 从 Bambu Studio 发起打印

当前 Studio 版本不支持选择存储位置，默认保存到内置存储。

### 从 Bambu Handy 发起打印

在准备页面可以选择素材存储的位置。默认为机内存储。

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/027.png)

## 素材管理

### 素材预览

打印结束后，可实时查看拍摄的视频文件。文件展示视频时长、模型名称、视频大小，按照拍摄时间顺序排列，同时支持批量导出到外部存储或者删除素材的操作。

#### 设备端入口

点击屏幕“主页 > 影像”，可查看延时摄影素材。

> 注意：
>
> - 新版本固件下的延时摄影素材名称为打印件名称；旧版本固件下的素材名称为“未命名/Unknow”；
> - 机内存储的延时摄影素材最多显示 56 个，超过 56 个的素材请通过 Handy/Studio 端访问。

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/001.png)

#### Bambu Studio 端入口

将在 Studio 的后续版本中支持该功能。

#### Bambu Handy 端入口

- 进入 Bambu Handy 的设备页面，点击“延时摄影”；

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/012.png)

- 点击“机内存储”，可查看机内存储、外部存储和本地文件。

> 注意：在机内存储和外部存储页面播放了的视频会默认保存一份到“本地文件”中。

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/020.png)

### 导出素材到外部存储

> 注意：仅支持在设备端进行导出操作。

- 点击“编辑”图标；

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/021.png)

- 选中需要导出的素材；

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/022.png)

- 点击屏幕右下方的“文件夹”图标。“导出并删除”表示导出素材到外部存储的同时，内置存储的素材将被自动删除且无法恢复；“导出”表示素材导出后，内置存储的素材依然保留，可按需选择。

> 注意:
>
> - 导出过程中请停留在此页面，直到导出成功。此过程中请不要进行任何其他操作，避免文件损坏。
> - 如果出现导出失败的提示，请检查外部存储是否容量不足。

|  |  |
| --- | --- |
|  |  |

- 导出成功。

![](https://wiki.bambulab.com/knowledge-sharing/timelapse-internal-storage/031.png)

### 文件删除

> 打印机恢复出厂设置后，会自动删除内置存储中所有的延时摄影文件。

#### 设备端

点击“编辑”按钮，选中需要删除的素材，点击屏幕右下方的“垃圾桶”图标，即可删除该素材，且支持批量操作。

|  |  |
| --- | --- |
|  |  |

#### Bambu Studio 端

将在 Studio 的后续版本中支持该功能。

#### Bambu Handy 端

点击“编辑”按钮，选中需要删除的素材，点击右下方的“垃圾桶”图标，即可删除该素材，且支持批量操作。

|  |  |
| --- | --- |
|  |  |

## FAQs

**Q：内置存储可以保存的延时摄影文件数量是否有上限？**

A：内置存储预留了 1G 的容量用于存储延时摄影文件，当剩余容量不足 20MB，或者文件数量达到 100 个时，会提示空间不足，请进行清理，或者关闭延时摄影功能。

**Q：内置存储的延时摄影文件导出到外置存储后，存放到了哪里？**

A：延时摄影的视频文件均在外置存储的 **timelapse** 文件夹中，为 **.mp4** 格式，缩略图文件均存放在 **thumbnail** 文件夹中，为 **.jpg** 格式。

**Q：将素材导出到外置存储时，对外置存储设备的性能有什么要求？**

A：建议使用写入速度不低于 15MB/s 的存储设备。

**Q：使用了外置存储，打印过程中如果拔掉了外置存储，会影响到这段延时摄影的素材吗？**

A：拔掉设备后，延时摄影会中断录制，已录制的文件名称为 temp.mp4 且不可用。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
