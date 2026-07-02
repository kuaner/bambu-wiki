---
path: zh/software/bambu-studio/timelapse-a-series
title: "A 系列延时摄影介绍"
description: "本文介绍了 A 系列 i3 结构打印机的延时摄影功能"
tags: []
created: 2026-06-29T07:29:51.167Z
updated: 2026-06-30T07:42:45.396Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/timelapse-a-series
---

## 延时摄影是什么？

如果在打印过程中启用了延时摄影，那么打印机每打印完一层后，摄像头都会拍摄一次快照，并在打印任务完成后，将所有快照组成一个延时视频。

## 拍摄位置

拍摄延时视频时，需保持热床水平位置固定，只改变 Z 方向位置。但 A 系列打印机为 i3 结构，通过前后移动热床来改变 Y 轴方向上的位置，因此在打印过程中，热床会在水平方向上不断移动，导致模型也在水平方向上不断移动。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/a2l-intro/034.png)

因此，为了成功拍摄延时视频，A 系列打印机**会在拍摄每张照片之前将热床移动到固定位置，并将喷嘴移动到吐料组件处**，拍摄完后将其移回模型上方继续打印，可在切片后预览的空驶路径中看到工具头移动到吐料槽的路径（如下图）。

> 如果发起打印时未启用延时摄影，则实际打印过程中则不会执行这些移动指令。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E7%A9%BA%E9%A9%B6%E8%B7%AF%E5%BE%84.png)

## 延时摄影模式

延时摄影分为**传统模式**和**平滑模式**。无论开启哪种模式，热床和工具头均会移动至固定位置后再进行拍照。

### 传统模式

在传统模式下，拍摄快照会造成停顿漏料，且由于没有擦料塔吸收漏料，容易影响打印效果。因此，切片算法会尽量将漏料缺陷隐藏在填充区域内，以保证表面质量。

|  |  |
| --- | --- |
|  |  |

**如果模型在当前层没有填充区域**，瑕疵将无法避免，因此推荐使用平滑模式。在发起打印任务前，系统也会弹出相应的提示。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E4%BC%A0%E7%BB%9F%E6%A8%A1%E5%BC%8F%E5%BB%B6%E6%97%B6%E8%AD%A6%E5%91%8A.png)

### 平滑模式

选择平滑模式后，打印时会额外打印一个擦料塔，在停顿拍摄照片之后，喷嘴会先在擦料塔上打印一段，再回到模型上继续打印，以确保停顿漏料产生的缺陷都被擦料塔吸收。

|  |  |
| --- | --- |
|  |  |

下图为无填充的模型在启用传统模式（左）和平滑模式（右）之间的打印质量比较。

![i3-noinfill-timelapse.jpg](https://wiki.bambulab.com/software/bambu-studio/timelapse/i3-noinfill-timelapse.jpg)

## 外置配件支持

MakerWorld 延时摄影套件可连接至 AMS 接口，通过蓝牙将指令转发给拍照设备，实现外置延时摄影。

![延时摄影套件.jpg](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E5%A5%97%E4%BB%B6.jpg)

当用户在发起打印时勾选"延时摄影"选项后，固件会在执行延时摄影时自动向外置配件发送拍照命令。由于从 MC 发送指令到相机完成拍照的链路较长，且市面上相机型号众多，从触发到拍照完成的时间存在波动。因此，MC 固件在平滑模式下，默认会在发送指令后延时 500ms 再继续动作。如需设置更长的延时时间，可通过 M9711 D 参数进行配置（单位：ms）。下图为延时时间设置为 1s 的示例：

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/image.png)

> 关于延时摄影套件的更多信息，请参考：[延时摄影套件使用指南](../../makerworld/cyberbrick/example-projects/time-lapse.md)。

## 如何启用和查看延时摄影？

### 通过打印机屏幕启用

从打印机屏幕发起打印时，可选择是否开启延时摄影。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/pre-print-cn.png)

此外，在打印机屏幕上还可以选择**延时摄影渐变模式**；该模式开启后，拍摄首层时，画面会放大，并随层数的增加逐渐缩小，如下图：

|  |  |
| --- | --- |
| 开启渐变模式 | 未开启渐变模式 |

**开启方式：** 设置 > 相机选项 > 延时摄影渐变模式

|  |  |
| --- | --- |
|  |  |

### 通过 Bambu Studio 启用与查看

在切片软件菜单栏中，点击"其他"选项下的“特殊模式”，可以找到"延时摄影"；

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.png)

开始打印之前，请确保将有**足够内存空间的 SD 卡**插入打印机，并在发送打印任务时**勾选“延时摄影”**。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%90%AF%E7%94%A8%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.png)

> **注意**：选择平滑模式时，请确保启用擦料塔（该功能默认开启）。  
> ![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BC%80%E5%90%AF%E6%93%A6%E6%8B%AD%E5%A1%94.png)

打印完成后，您可以在 Bambu Studio 中从“设备 > 存储介质”页面直接下载延时摄影视频文件。

![a2l-studio-cn.jpg](https://wiki.bambulab.com/software/bambu-studio/timelapse/a2l-studio-cn.jpg)

### 通过 Bambu Handy 启用与查看

点击“准备打印 > 选项 > 延时摄影”可开启延时摄影。如下面动图所示：

![handy-延时摄影-cn.png](https://wiki.bambulab.com/software/bambu-studio/timelapse/handy-%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1-cn.png)

当打印完成后，可在 **设备界面 > 延时摄影** 中找到已录制完成的视频，并选择下载到本地相册中。

![a2l-延时摄影-cn_(1).png](https://wiki.bambulab.com/software/bambu-studio/timelapse/a2l-%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1-cn_(1).png)

### 物理存储路径

如果您选择将延时摄影文件存储至外部 SD 卡，打印完成后，您可以在 SD 卡的 **timelapse 文件夹**中找到对应的视频文件：  
![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E6%96%87%E4%BB%B6%E5%A4%B9.png)

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
