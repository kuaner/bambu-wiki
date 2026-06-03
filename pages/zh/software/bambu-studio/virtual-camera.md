---
path: zh/software/bambu-studio/virtual-camera
title: "Bambu Lab 打印机的直播功能"
description: ""
tags: ["bambu studio"]
created: 2023-08-29T04:30:56.320Z
updated: 2025-10-23T02:46:50.930Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/virtual-camera
---

## 在 Bambu Studio 内开启直播功能

### **支持机型**

X1、X1C、X1E

部分地区的 H2D、H2S 、P2S暂不支持直播功能（后续会通过软件更新支持）

### 准备虚拟摄像头工具

打开 Bambu Studio，点击顶部菜单栏中的**设备**，选择需要直播的打印机，点击**设置**按钮，开启直播；如果是首次使用，则会弹出安装虚拟摄像头工具包的提示，点击确认即可。

|  |  |
| --- | --- |
|  |  |

摄像头图标亮红灯时，表示虚拟摄像机已经开始工作。

![](https://wiki.bambulab.com/software/bambu-studio/virtual-camera/image_-_2025-01-23t145220.383.png)

此时工具包会安装到配置文件夹内，您可以参考下图，在 cameratools 文件夹内位置找到 ffmpeg.sdp 文件，并从该文件中获取摄像头的视频流。

|  |  |
| --- | --- |
|  |  |

> 注意：**Bambu Studio 仅支持单个虚拟摄像机**；如果选择另一台打印机开启直播，第一个视频流则会停止。
>
> ![](https://wiki.bambulab.com/software/bambu-studio/virtual-camera/image_-_2025-01-23t145503.540.png)

## 使用 OBS 虚拟相机进行推流

OBS Studio（Open Broadcaster Software Studio）是一款免费、开源的跨平台软件，主要用于直播推流和视频录制。

### 安装并配置媒体源

安装 OBS Studio，进入OBS 内添加媒体源并进行配置。

|  |  |
| --- | --- |
|  |  |

选择新建并对视频源进行命名。

![](https://wiki.bambulab.com/software/bambu-studio/virtual-camera/d12676a6b7273cca27326119529e1d5.png)

打开“Bambu Studio”配置文件夹，您可以在子文件夹“cameratools”中找到一个名为“ffmpeg.sdp”的文件。

对媒体源进行配置，取消勾选本地文件复选框，在‘输入’一栏填入打印机摄像头视频流文件地址：

- Windows：C:/Users/[计算机用户名]/AppData/Roaming/BambuStudio/cameratools/ffmpeg.sdp
- Mac OS：/Users/[计算机用户名]/Library/Application Support/BambuStudio/cameratools/ffmpeg.sdp

> 注意：黄色画线位置需要填写自己本地计算机的用户名称。

![](https://wiki.bambulab.com/software/bambu-studio/virtual-camera/e5aaead4d39eda484b596c794ec116b.png)

需要在“FFmpeg选项”中填入 protocol\_whitelist=file,udp,rtp

> 注意：需要输入英文字符。

![](https://wiki.bambulab.com/software/bambu-studio/virtual-camera/image_-_2025-01-23t145512.788.png)

点击确定之后等待 3-5 秒将会出现打印机舱内画面；启动虚拟摄像机恭喜您已经成功创建了虚拟摄像头，下一步您可以在直播软件内使用虚拟摄像头进行直播。

![](https://wiki.bambulab.com/software/bambu-studio/virtual-camera/ee2391dc0ce8f1c5d95af4befd256fc.png)

## 在直播软件内使用虚拟摄像头推流

### 安装直播软件

以下使用bilibili进行演示操作；安装bilibili直播软件“哔哩哔哩直播姬”。

在直播素材中选择“第三方推流”，点击“一键添加虚拟摄像机”。

|  |  |
| --- | --- |
|  |  |

摄像头选择“OBS Virtual Camera”软件中央会显示打印机舱内视频，点击“开始直播”您就开始进行直播了，之后您就愉快的可以分享链接给其他人进行观看了。

|  |  |
| --- | --- |
|  |  |

## 其他

### 使用VLC获取视频流进行直播

打开VLC media player，添加“ffmpeg.sdp”文件。

|  |  |  |
| --- | --- | --- |
|  |  |  |
