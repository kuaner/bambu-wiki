---
path: zh/software/bambu-studio/Timelapse
title: "延时摄影"
description: "本篇介绍了延时摄影的用途。"
tags: ["bambu studio"]
created: 2023-03-14T13:57:18.420Z
updated: 2026-06-15T02:47:40.012Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/Timelapse
---

本页介绍了延时摄影的用途。延时摄影是一种视频拍摄技术，将几分钟、几小时甚至几天的过程压缩成一段短视频。

## 1.延时摄影模式介绍

在 Bambu Studio 中，如果你启用了延时摄影，每一层打印完成后，机箱摄像头都会拍摄一次快照。打印完成后，所有的快照会组成一个延时视频。

延时摄影有两种模式：平滑模式和传统模式。针对不同的打印机，拍摄延时摄影的动作会有一些区别，具体介绍如下：

### X1, P1 系列以及 P2S 打印机

**平滑模式：** 每层打印完后工具头都会移动到废料滑梯，然后拍摄快照。由于在每次拍摄快照的过程中工具头会停顿一会儿，熔融的耗材可能会从喷嘴中漏出，所以在平滑模式下，需要一个擦拭塔来清洁喷嘴，吸收掉渗漏的材料避免打印模型表面出现瑕疵。因此，如果热床上没有擦拭塔，就会默认自动生成一个擦拭塔。如果热床上已经有一个擦拭塔了，则会重复利用现有的擦拭塔。

在这种模式下，视频中的工具头始终保持在擦料塔上方，不会阻挡模型所在的位置，所以延时视频看起来会非常流畅。但是，由于增加了工具头额外的移动路径以及擦料操作，整体打印时间会增加。

![timelapse_video.gif](https://wiki.bambulab.com/software/bambu-studio/timelapse/timelapse_video.gif)

**传统模式：** 它会在每层打印完成后直接拍摄快照，所以在这种模式下无需擦料塔。在延时摄影视频中，会看到工具头不断移动。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E4%BC%A0%E7%BB%9F%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.gif)

### A 系列打印机

|  |  |
| --- | --- |
| i3_machine.jpg |  |

X1 和 P1 系列打印机在打印时，热床只会上下移动，它通过移动热床改变 Z 方向上的位置。由于结构不同，A 系列打印机则是通过前后移动热床来改变 Y 轴方向上的位置，所以在打印过程中，热床在水平方向上不断移动。

拍摄延时视频时，需要保持热床的水平位置固定，只改变 Z 方向的位置。然而，A 系列打印机在打印过程中，热床不断移动，导致模型也在水平方向上不断移动。因此，为了成功拍摄延时视频，A 系列打印机会在每张照片之前将热床移动到固定位置，并将喷嘴移动到吐料槽，然后在拍摄完照片后将其移回模型上方继续打印。**无论是传统模式还是平滑模式的延时摄影，它都会将热床和工具头移动到固定位置后再进行拍照。你可以在切片后预览的空驶路径中看到工具头移动到吐料槽的路径（如下图），不过如果你在发起打印时未启用延时摄影功能的话，在实际打印过程中并不会执行这些移动指令。**

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E7%A9%BA%E9%A9%B6%E8%B7%AF%E5%BE%84.png)

**传统模式：** 打印过程中由于拍摄快照会造成停顿漏料，传统模式的延时摄影没有擦料塔来吸收这个瑕疵，影响打印效果。所以我们的策略是尽可能将缺陷打印到填充中，以保证表面质量，但是如果模型在这一层没有填充区域，瑕疵是不可避免的。在这种情况下，不建议启用传统模式的延时摄影，而是建议使用平滑模式。在发起打印任务之前也会收到相应的提示。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E4%BC%A0%E7%BB%9F%E6%A8%A1%E5%BC%8F%E5%BB%B6%E6%97%B6%E8%AD%A6%E5%91%8A.png)

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E4%BC%A0%E7%BB%9F%E6%A8%A1%E5%BC%8F.png)

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/a1%E4%BC%A0%E7%BB%9F%E6%A8%A1%E5%BC%8F.gif)

**平滑模式：** 选择平滑模式延时摄影后默认会自动生成一个擦料塔，打印过程中在停顿拍摄照片之后，喷嘴会先去擦料塔上打印一段，再去模型上继续打印，这样停顿漏料产生的缺陷都被擦料塔吸收了。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%B9%B3%E6%BB%91%E6%A8%A1%E5%BC%8F.png)

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/a1%E5%B9%B3%E6%BB%91%E6%A8%A1%E5%BC%8F.gif)

下图是没有填充的模型在启用传统模式延时摄影和平滑模式延时摄影之间的打印质量比较。

![i3-noinfill-timelapse.jpg](https://wiki.bambulab.com/software/bambu-studio/timelapse/i3-noinfill-timelapse.jpg)

**延时摄影渐变模式：** 该模式开启后，打印首层时会出现裁切放大的效果。随着层数的增加，画面逐渐由放大转变为缩小。  
在打印机屏幕上可以开启/关闭此功能：选择“设置 > 相机选项 > 延时摄影渐变模式”。  
![渐变.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E6%B8%90%E5%8F%98.webp)

关闭延时摄影渐变模式，则不会出现缩放效果。  
![111.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/111.webp)

### 双喷嘴打印机的延时摄影（H2D/H2C/X2D）

双喷嘴有约5mm的高度差，在切换喷嘴时，热床也会相应地上升/下降5mm（如下面动图1所示）。因此每次延时摄影拍照时，若使用的喷嘴不一致会导致热床高度不一致\*\*，延时摄影视频中的热床会跳动，如下图2中所示。图2为使用左右喷嘴逐层打印两个不同颜色的方块，延时摄影在每层结束位置执行，拍照时刻使用的喷嘴不一致，热床的位置也会上下跳动。

|  |  |
| --- | --- |
|  |  |
| 图1.H2D 双喷嘴切换 | 图2.双喷嘴延时摄影热床抖动问题 |

#### 针对双喷嘴打印延时摄影的处理方案

针对H2D的处理方案是在延时摄影拍照时热床切换至同一个喷嘴的高度，且尽可能减少不必要的喷嘴切换，主要的逻辑有：

1. 逐件并按层计算每个打印对象使用最多的喷嘴（定义为“主喷嘴”），每次延时摄影拍照时，判断当前喷嘴跟“主喷嘴”是否一致，若不一致时将工具头挪到废料滑梯并调整热床高度至对应“主喷嘴”的高度然后拍照。
2. 拍照时刻与换层时刻分开，如果该层打印有使用“主喷嘴”打印，拍照时刻统一到正在使用该层“主喷嘴“的时候。

以上逻辑对实际几种打印场景的例子：

1. 若打印只使用了一个喷嘴，在平滑模式下，拍照也会停留在安全区域进行；
2. 若打印使用了左右两个喷嘴且每层都用到主喷嘴，则延时摄影的两种模式都与X1/P1打印机单喷嘴打印相同，如下图中的双色立方体打印任务，由于右喷嘴是主喷嘴，所以延时摄影每次都会在右喷嘴打印时拍照，而非在每层打印结束的时候拍照。

|  |  |
| --- | --- |
|  |  |

3. 若打印使用了左右两个喷嘴但部分层只有使用了一个喷嘴，则在打印这些层拍照时，会将工具头挪到废料滑梯并调整热床高度至对应“主喷嘴”的高度然后拍照。对于平滑模式视频效果与X1/P1相同，但对于传统模式，这些层会变成“平滑模式”，整个视频是传统模式和平滑模式的混合状态。  
   ![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/2.gif)
4. 对于逐件打印，打印每个对象时都会更新“主喷嘴”，并按上述3种情况处理每个对象的延时摄影。例如下图中逐件打印双色柱，传统模式与X1/P1效果类似，在打印每个对象拍照时不需要调整热床高度。  
   ![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/4.gif)

#### 双喷嘴打印延时摄影的平滑模式

开启平滑模式后，喷嘴会远离模型再拍摄延时摄影。

当打印高度小于 5mm 时，为了避免热床移动撞击喷嘴，喷嘴将主动回到吐料组件处；  
当打印高度大于 5mm 时，喷嘴将移动到模型附近的安全区域，等待延时摄影完成。

![平滑模式h2c.webp](https://wiki.bambulab.com/h2/manual/time-lapse-function/%E5%B9%B3%E6%BB%91%E6%A8%A1%E5%BC%8Fh2c.webp)

#### 外置配件支持

![产品功能.png](https://wiki.bambulab.com/h2/manual/time-lapse-function/%E4%BA%A7%E5%93%81%E5%8A%9F%E8%83%BD.png)

MakerWorld 新增一个延时摄影套件，连接到 AMS 的接口，通过蓝牙转给拍照设备实现外置延时摄影。

用户发起打印勾选延时摄影的情况下，固件在执行延时摄影时会自动给外置配件发送拍照命令。；

因从MC发送指令到相机执行拍照链路较长且市面相机型号很多,从触发拍照到拍照完成的时间容易波动，MC固件中在**平滑模式**下默认会在发送指令后延时500ms，若需指定更长的延时，可通过**M9711 D**参数设定（单位ms），如下图为设置成1s的延时时间：

![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/image.png)

#### 已知问题

1. 拍照时打印使用的喷嘴和“主喷嘴”不一致，目前只会调整热床高度，工具头不会切换喷嘴，在平滑模式的延时摄影视频能看到左热端上下动以及工具头灯光左右切换；  
   ![](https://wiki.bambulab.com/h2/manual/time-lapse-function/zh1/3.gif)
2. 延时摄影到废料滑梯拍照时会顶起切刀顶杆，会有噪音;
3. 部分内置模型（如小船）不带延时摄影的gcode.

## 2.如何启用延时摄影

在切片软件菜单栏中，在"其他"选项下的“特殊模式”中，可以找到"延时摄影"模式。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.png)

选择平滑模式时，请确保启用擦拭塔（该功能默认是开启的），因为我们需要擦拭塔来清洁喷嘴。

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BC%80%E5%90%AF%E6%93%A6%E6%8B%AD%E5%A1%94.png)

在开始打印之前，请确保将有足够内存空间的 SD 卡插入打印机，并在发送打印任务的时候勾选“延时摄影”：

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%90%AF%E7%94%A8%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1.png)

## 3.延时摄影视频文件存储的位置

打印后，生成的延时视频将存储在打印机的 SD 卡中。你可以在 SD 卡的 **timelapse 文件夹**中找到延时摄影的文件：

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E6%96%87%E4%BB%B6%E5%A4%B9.png)

在 Bambu Studio 中，您可以从 “设备”——“SD卡” 页面下载延时摄影视频文件：

![](https://wiki.bambulab.com/software/bambu-studio/timelapse/studio%E9%87%8C%E4%B8%8B%E8%BD%BD%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1%E8%A7%86%E9%A2%91.png)

如果没有sd卡，可以插入u盘存储并查看。

## 4.在 Bambu Handy 上启用延时摄影

在 Bambu Handy 中您可以在 **准备打印 -> 选项 -> 延时摄影** 的位置选择开启延时摄影。如下面动图所示：

![cn-准备打印_webp.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/cn-%E5%87%86%E5%A4%87%E6%89%93%E5%8D%B0_webp.webp)

当打印完成后，您可以在 **设备界面 -> 延时摄影** 找到已经录制完成的视频，并选择下载到本地相册中。

![cn-查看延时摄影_web.webp](https://wiki.bambulab.com/software/bambu-studio/timelapse/cn-%E6%9F%A5%E7%9C%8B%E5%BB%B6%E6%97%B6%E6%91%84%E5%BD%B1_web.webp)

## FAQs

### 1.延时摄影时长和打印时长的关系

延时视频时长独立于实际打印时间，延时摄影时长仅由层数和帧率决定；  
有些打印面积较大但是层高较少的模型，虽然打印时间较长但是延时摄影下拍出的视频依然较短的。  
其中总帧数=层数（N），帧率为 30（fps）。

视频时长（秒）=N帧率（fps）\text{视频时长（秒）} = \frac{N}{\text{帧率（fps）}}
视频时长（秒）=帧率（fps）N​

例如：1000 层 / 30fps → 视频时长 ≈ 33.3 秒。

### 2.打印过程中实时预览画面昏暗

为了避免因环境光线变化导致的画面闪烁或亮度不一致的问题,延时摄影过程中会锁定曝光，确保整个序列的亮度一致性；如果在较亮的环境下开始打印，当环境光线变暗之后（比如从白天到夜晚的过渡），那么锁定的曝光设置会导致实时预览的画面显得过暗。
