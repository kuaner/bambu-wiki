---
path: zh/software/bambu-studio/timelapse-xp-series
title: " X1 / P1 / P2S / H2S 延时摄影介绍"
description: "本文介绍了  X1 / P1 / P2S / H2S  等 Corexy 结构单喷嘴打印机的延时摄影功能"
tags: []
created: 2026-06-30T02:19:09.582Z
updated: 2026-06-30T07:45:09.442Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/timelapse-xp-series
---

## 延时摄影是什么？

如果在打印过程中启用了延时摄影，那么打印机每打印完一层后，摄像头都会拍摄一次快照，并在打印任务完成后，将所有快照组成一个延时视频。

## 延时摄影模式

根据切换策略的不同，延时摄影可分为传统模式和平滑模式两种。

### 传统模式

在传统模式下，打印机会在每层打印完成后直接拍摄快照，以下为双喷嘴打印机使用单喷嘴打印的延时摄影。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E4%BC%A0%E7%BB%9F%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.gif)

### 平滑模式

每层打印完成后，工具头都会移动至废料滑梯位置进行快照拍摄。由于拍摄过程中工具头需要停顿片刻，熔融的耗材可能会从喷嘴中渗漏出来。因此在平滑模式下，需要借助**擦料塔**来清洁喷嘴、吸收渗漏的材料，避免打印件表面出现瑕疵。

基于此，如果热床上没有擦料塔，系统会自动生成一个；如果热床上已存在擦料塔，则会直接复用。

在该模式下，工具头始终停留在擦拭塔上方，不会遮挡模型，因此延时视频的画面会非常流畅连贯。但需要注意的是，由于增加了工具头的额外移动路径和擦料动作，**整体打印时间会有所延长**。

![timelapse_video.gif](https://wiki.bambulab.com/software/bambu-studio/timelapse/timelapse_video.gif)

## 外置配件支持

MakerWorld 延时摄影套件可连接至 AMS 接口，通过蓝牙将指令转发给拍照设备，实现外置延时摄影。

![延时摄影套件.jpg](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E5%A5%97%E4%BB%B6.jpg)

当用户在发起打印时勾选"延时摄影"选项后，固件会在执行延时摄影时自动向外置配件发送拍照命令。由于从 MC 发送指令到相机完成拍照的链路较长，且市面上相机型号众多，从触发到拍照完成的时间存在波动。因此，MC 固件在平滑模式下，默认会在发送指令后延时 500ms 再继续动作。如需设置更长的延时时间，可通过 M9711 D 参数进行配置（单位：ms）。下图为延时时间设置为 1s 的示例：

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/image.png)

> 关于延时摄影套件的更多信息，请参考：[延时摄影套件使用指南](../../makerworld/cyberbrick/example-projects/time-lapse.md)。

## 如何启用和查看延时摄影？

### 通过打印机屏幕启用

从打印机屏幕发起打印时，可选择是否开启延时摄影。

![h2s-kaiqi.png](https://wiki.bambulab.com/software/bambu-studio/timelapse/h2s-kaiqi.png)

### 通过 Bambu Studio 启用与查看

在切片软件菜单栏中，点击"其他"，可在“特殊模式”下找到"延时摄影"；

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.png)

开始打印前，请确保将有**足够内存空间的存储介质**插入打印机，并在发送打印任务时**勾选“延时摄影”**。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%90%AF%E7%94%A8%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.png)

> **注意**：选择平滑模式时，请确保启用擦料塔（该功能默认开启）。  
> ![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BC%80%E5%90%AF%E6%93%A6%E6%8B%AD%E5%A1%94.png)

打印完成后，您可以在 Bambu Studio 中从 **“设备 > 存储介质”** 页面直接下载延时摄影视频文件。

![p2s-studio.jpg](https://wiki.bambulab.com/software/bambu-studio/timelapse/p2s-studio.jpg)

### 通过 Bambu Handy 启用与查看

点击“准备打印 > 选项 > 延时摄影”可开启延时摄影。如下面动图所示：

![cn-准备打印_webp.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/cn-%E5%87%86%E5%A4%87%E6%89%93%E5%8D%B0_webp.webp)

当打印完成后，可在 **设备界面 > 延时摄影** 中找到已录制完成的视频，并选择下载到本地相册中。

![cn-查看延时摄影_web.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/cn-%E6%9F%A5%E7%9C%8B%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1_web.webp)

### 物理存储路径

如果您选择将延时摄影文件存储至外部 SD 卡，打印完成后，您可以在 SD 卡的 **timelapse 文件夹**中找到对应的视频文件：  
![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E6%96%87%E4%BB%B6%E5%A4%B9.png)

> P2S 可选择将延时摄影文件保存至外部或内部存储，具体内容请参考：[延时摄影内置存储和素材管理](../../knowledge-sharing/timelapse-internal-storage-and-video-management.md)。

## FAQs

#### 1. 延时摄影时长和打印时长的关系

延时视频时长独立于实际打印时间，延时摄影时长仅由层数和帧率决定；  
有些打印面积较大但是层高较少的模型，虽然打印时间较长但是延时摄影下拍出的视频依然较短的。  
其中总帧数=层数（N），帧率为 30（fps）。

视频时长（秒）=N帧率（fps）\text{视频时长（秒）} = \frac{N}{\text{帧率（fps）}}
视频时长（秒）=帧率（fps）N​

例如：1000 层 / 30fps → 视频时长 ≈ 33.3 秒。

#### 2. 打印过程中实时预览画面昏暗

为了避免因环境光线变化导致的画面闪烁或亮度不一致的问题,延时摄影过程中会锁定曝光，确保整个序列的亮度一致性；如果在较亮的环境下开始打印，当环境光线变暗之后（比如从白天到夜晚的过渡），那么锁定的曝光设置会导致实时预览的画面显得过暗。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
