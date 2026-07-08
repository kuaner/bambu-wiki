---
path: zh/h2/manual/time-lapse-function
title: "H2D /  H2D Pro / H2C / X2D 延时摄影介绍"
description: "本文介绍了 H2D、H2D Pro、H2C、X2D 等 CoreXY 结构多喷嘴打印机的延时摄影功能"
tags: []
created: 2025-03-25T05:10:57.539Z
updated: 2026-06-30T08:10:32.224Z
source: https://wiki.bambulab.com/zh/h2/manual/time-lapse-function
---

## 延时摄影是什么？

如果在打印过程中启用了延时摄影，那么打印机每打印完一层后，摄像头都会拍摄一次快照，并在打印任务完成后，将所有快照组成一个延时视频。

## 延时摄影模式

双喷嘴打印机的两个喷嘴有约 5mm 的高度差，在切换喷嘴时，热床也会相应地上升/下降 5mm。

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/output.gif)

因此每次延时摄影拍照时，若使用的喷嘴不一致，则热床高度不一致，延时摄影视频中的热床会上下跳动，如下图所示，使用左右喷嘴逐层打印两个不同颜色的方块，延时摄影在每层结束位置执行，拍照时使用的喷嘴不一致，热床的位置也会上下跳动。

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/output1.gif)

因此，为了成功拍摄延时视频，双喷嘴打印机会在延时摄影拍照时，将热床切换至同一个喷嘴高度，且尽可能减少不必要的喷嘴切换。根据切换策略的不同，延时摄影可分为传统模式和平滑模式两种。

### 传统模式

在传统模式下，打印机会在每层打印完成后直接拍摄快照，以下为双喷嘴打印机使用单喷嘴打印的延时摄影。

![双喷嘴打印机传统模式.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%8F%8C%E5%96%B7%E5%98%B4%E6%89%93%E5%8D%B0%E6%9C%BA%E4%BC%A0%E7%BB%9F%E6%A8%A1%E5%BC%8F.webp)

### 平滑模式

在平滑模式下，喷嘴会远离模型再拍摄延时摄影。

- 当打印高度小于 5mm 时，为了避免热床移动撞击喷嘴，喷嘴将主动回到吐料组件处；
- 当打印高度大于 5mm 时，喷嘴将移动到模型附近的安全区域，等待延时摄影完成。

![平滑模式h2c.webp](https://wiki.bambulab.com/h2/manual/time-lapse-function/%E5%B9%B3%E6%BB%91%E6%A8%A1%E5%BC%8Fh2c.webp)

## 拍摄逻辑

双喷嘴打印机拍摄延时摄影视频的主要逻辑有：

1. 逐件并按层计算每个打印对象使用最多的喷嘴（定义为“主喷嘴”），每次延时摄影拍照时，判断当前喷嘴跟“主喷嘴”是否一致，若不一致，则会将工具头挪到废料滑梯处，并调整热床高度至对应“主喷嘴”高度进行拍照。

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/image-2.png)  
2. 分开拍照时刻与换层时刻，如果该层打印需使用“主喷嘴”，拍照时刻统一到正在使用该层“主喷嘴“的时候。

以上逻辑对实际几种打印场景的例子：

1. 若打印只使用了一个喷嘴，在平滑模式下，拍照也会停留在安全区域进行；
2. 若打印使用了左右两个喷嘴且每层都用到主喷嘴，则延时摄影的两种模式都与单喷嘴打印机单喷嘴打印相同，如下图中的双色立方体打印任务，由于右喷嘴是主喷嘴，所以延时摄影每次都会在右喷嘴打印时拍照，而非在每层打印结束的时候拍照。

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/1.gif)

3. 若打印使用了左右两个喷嘴但部分层只使用了一个喷嘴，则在打印这些层拍照时，会将工具头挪到废料滑梯并调整热床高度至对应“主喷嘴”高度进行拍照。平滑模式下，视频效果与单喷嘴打印机（如 X1）相同，但对于传统模式，这些层会变成“平滑模式”，整个视频是传统模式和平滑模式的混合状态。

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/2.gif)

4. 对于逐件打印，打印每个对象时都会更新“主喷嘴”，并按上述 3 种情况处理每个对象的延时摄影。例如下图中逐件打印双色柱，传统模式与单喷嘴打印机（如 X1）效果类似，在打印每个对象拍照时不需要调整热床高度。

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/4.gif)

### 已知问题

1. 拍照时打印使用的喷嘴和“主喷嘴”不一致，目前只会调整热床高度，工具头不会切换喷嘴，在平滑模式的延时摄影视频能看到左热端上下动以及工具头灯光左右切换；

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/3.gif)

2. 延时摄影到废料滑梯拍照时会顶起切刀顶杆，会有噪音;
3. 部分内置模型（如小船）不带延时摄影的 gcode。

## 外置配件支持

MakerWorld 延时摄影套件可连接至 AMS 接口，通过蓝牙将指令转发给拍照设备，实现外置延时摄影。

![延时摄影套件.jpg](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E5%A5%97%E4%BB%B6.jpg)

当用户在发起打印时勾选"延时摄影"选项后，固件会在执行延时摄影时自动向外置配件发送拍照命令。由于从 MC 发送指令到相机完成拍照的链路较长，且市面上相机型号众多，从触发到拍照完成的时间存在波动。因此，MC 固件在平滑模式下，默认会在发送指令后延时 500ms 再继续动作。如需设置更长的延时时间，可通过 M9711 D 参数进行配置（单位：ms）。下图为延时时间设置为 1s 的示例：

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/image.png)

> 关于延时摄影套件的更多信息，请参考：[延时摄影套件使用指南](../../makerworld/cyberbrick/example-projects/time-lapse.md)。

## 如何启用和查看延时摄影？

### 通过打印机屏幕启用

从打印机屏幕发起打印时，可选择是否开启延时摄影。

![h2d-kaiqi.png](https://wiki.bambulab.com/software/bambu-studio/timelapse/h2d-kaiqi.png)

### 通过 Bambu Studio 启用与查看

在切片软件菜单栏中，点击"其他"，可在“特殊模式”下找到"延时摄影"；

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.png)

开始打印前，请确保将有**足够内存空间的存储介质**插入打印机，并在发送打印任务时**勾选“延时摄影”**。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%90%AF%E7%94%A8%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.png)

> **注意**：选择平滑模式时，请确保启用擦料塔（该功能默认开启）。  
> ![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BC%80%E5%90%AF%E6%93%A6%E6%8B%AD%E5%A1%94.png)

打印完成后，您可以在 Bambu Studio 中从 **“设备 > 存储介质”** 页面直接下载延时摄影视频文件。

![studio_下载视频.jpg](https://wiki.bambulab.com/software/bambu-studio/timelapse/studio_%E4%B8%8B%E8%BD%BD%E8%A7%86%E9%A2%91.jpg)

### 通过 Bambu Handy 启用与查看

点击“准备打印 > 选项 > 延时摄影”可开启延时摄影。如下面动图所示：

![cn-准备打印_webp.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/cn-%E5%87%86%E5%A4%87%E6%89%93%E5%8D%B0_webp.webp)

当打印完成后，可在 **设备界面 > 延时摄影** 中找到已录制完成的视频，并选择下载到本地相册中。

![cn-查看延时摄影_web.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/cn-%E6%9F%A5%E7%9C%8B%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1_web.webp)

### 物理存储路径

如果您选择将延时摄影文件存储至外部 SD 卡，打印完成后，您可以在 SD 卡的 **timelapse 文件夹**中找到对应的视频文件：  
![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E6%96%87%E4%BB%B6%E5%A4%B9.png)

> X2D 可选择将延时摄影文件保存至外部或内部存储，具体内容请参考：[延时摄影内置存储和素材管理](../../knowledge-sharing/timelapse-internal-storage-and-video-management.md)。

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
