---
path: zh/a1/maintenance/mainboard-replacement-guide
title: "A1 主板更换指南"
description: "介绍更换 A1 主板的步骤。"
tags: []
created: 2024-08-16T06:39:18.713Z
updated: 2026-06-18T02:36:38.601Z
source: https://wiki.bambulab.com/zh/a1/maintenance/mainboard-replacement-guide
---

## 适用型号

A1

## 可解决的问题

- 无法开机
- 主板损坏
- 拓竹技术支持建议更换

## **安全提示**

> **重要提醒！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[*点击提交服务工单*](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 工具和材料

- A1 主板
- H2.0 六角扳手
- H1.5 六角扳手
- PH2 十字螺丝刀

预计耗时：20 分钟

## 拆卸旧主板

### 1. 将打印机正面朝下放置

将打印机正面朝下放置，方便操作打印机底部。

首先将屏幕翻转到一侧，然后轻轻将打印机正面朝下放置，如下图所示。**建议使用一盒耗材将打印机顶部抬起，避免压迫挤出机和屏幕。**

![](https://wiki.bambulab.com/a1/maintenance/power-supply/place_the_a1_printer_on_its_front.jpeg)

### 2. 拆卸线缆支架

1. 断开相机、X 轴电机和 Z 轴电机 3 处线缆；

2. 拧松 1 颗螺丝；

3. 向上推动线缆支架，断开 USB 数据线，即可取下线缆支架。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### 3. 拆除打印机底盖

卸下红色标记的 10 颗螺丝，即可拆卸底盖。

![](https://wiki.bambulab.com/a1/maintenance/wifi-antenna/%E6%8B%86%E5%BA%95%E5%A3%B3%E8%9E%BA%E4%B8%9D10.jpg)

### 4. 取出 SD 卡

从打印机上取出  SD 卡。

### 5. 断开主板上的 5 根线缆

小心地断开如下图所示的 5 根线缆。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/remove_mainboard_cables_from_a1_board.jpeg)

### 6. 移除主板螺丝

小心地移除下图中的 9 颗螺丝。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/remove_the_a1_board_screws.jpeg)

### 7. 移除散热片支架

轻轻向上推动散热片支架，直到从底部塑料卡扣中释放出来，然后向您的方向拉出散热片支架并将它完全取下。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/remove_the_heatsink_bracket.jpeg)

### 8. 移除主板

首先，朝您所在的方向，从右侧轻轻拉动主板。施加轻微压力的同时，轻轻向一侧推动下图中用红色箭头标注的塑料固定夹。这样您就可以松开主板上的固定夹并将主板完全取出。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/remove_the_board_clips.jpeg)

### 9. 断开主板连接线

拧松螺丝至能够断开线缆的程度，然后小心地断开这些线缆。

> 请勿完全卸下螺丝。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/disconnect_the_board_wires.jpeg)

旧主板成功移除。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/remove_the_boadrd_completely.jpg)

## 安装新主板

在开始操作前，请拍摄电路板背面的二维码，用于完成主板更换后的操作。

> 此二维码内容为整机 SN 序列号，用于更换主板之后注册设备

![screenshot-20240926-191519.png](https://wiki.bambulab.com/general/find-sn/screenshot-20240926-191519.png)

### 1. 确认主板批次

最新批次的主板更改了元器件布局，可能和打印机底座产生干涉，可根据下图元器件朝向判断新主板批次。

| 新批次 | 旧批次 |
| --- | --- |
|  |  |

若您收到的新批次主板，请首先检查底壳。

![](https://wiki.bambulab.com/a1/maintenance/mainboard-replacement-guide/pixpin_2026-06-18_10-32-53.jpg)

观察底壳上理线盒安装部分的筋位是否处理过。

![pixpin_2026-06-18_10-33-11.jpg](https://wiki.bambulab.com/a1/maintenance/mainboard-replacement-guide/pixpin_2026-06-18_10-33-11.jpg)

若未处理，可参考下图裁断对应位置。

|  |  |
| --- | --- |
| pixpin_2026-06-18_10-33-47.jpg | pixpin_2026-06-18_10-33-59.jpg |

### 2. 重新将主板线缆连接至电源

小心地将主板上的线重新连接到电源上。

1. 红线-**正极**
2. 黑线-**负极**
3. 较长的黑线-**零线**

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/disconnect_the_board_wires.jpeg)

### 3. 连接排线

先安装柔性排线电缆后再安装主板。如图所示，确保对齐连接器。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/install_ribbon_cable.jpeg)

### 4. 安装新主板到打印机

首先将主板与框架对齐，倾斜角度，然后轻轻按压主板以将其固定到打印机上。

确保顶部和底部的塑料卡扣都已将主板固定好，然后进入下一步操作。

蓝色硅脂需要涂抹在主板上与散热片接触的区域，以确保热量能够有效传导到散热片。

![install_new_board_with_silicone.png](https://wiki.bambulab.com/a1/manual/replace-mainboard/install_new_board_with_silicone.png)

### 5. 安装主板散热片

小心地将散热片支架滑入塑料卡扣下面，如图所示。

将螺丝孔与主板对齐，然后拧入 1 号和 2 号螺丝。

最后拧入 3 号螺丝，完成支架的安装。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/install_the_board_heatsink.jpeg)

### 6. 拧入主板螺丝

使用剩余的 6 颗螺丝将主板固定到位。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/install_the_remaining_board_screws.jpeg)

### 7. 重连主板电线

重新连接线缆后，完成主板的安装。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/remove_mainboard_cables_from_a1_board.jpeg)

> **注意：各接口示意图如下：**
>
> ![](https://wiki.bambulab.com/a1/manual/replace-mainboard/%E6%8E%A5%E5%8F%A3zh.jpg)

#### 根据电路板灯语判断是否连接成功

由于 A1 机型的 MC 板和 AP 板都集成在主板上，因此可通过灯语校验两者是否功能正常。

##### **正常状态：MC板每5秒闪烁一次绿灯**

在拧回所有螺丝前，可先预装或不装盖子（小心用电安全，断电操作），再通电检查该电路板灯语是否正常，灯语正常，再拧回螺丝，这样可以避免返工。

<https://public-cdn.bblmw.com/wiki/video/A1-MC.mp4>

##### 正常状态：AP板有1个每秒闪烁一次的绿灯指示灯

<https://public-cdn.bblmw.com/wiki/video/A1-AP.mp4>

### 8.  安装打印机底盖

**请注意红色箭头标示的电机线缆**。请务必整理好这束线缆后，才能完全按下底盖。

将底盖卡扣到位后，拧入 10 颗螺丝，**请注意不要过度拧紧。**

![](https://wiki.bambulab.com/a1/maintenance/wifi-antenna/%E5%AE%89%E8%A3%85%E5%BA%95%E7%9B%96.jpg)

### 9. 安装线缆支架并连接线缆

对齐线缆支架后，然后向下推动，确保将 USB 数据线完全插入。

然后，拧紧图中所示的螺丝以将其锁定到位。由于这颗螺丝是拧入塑料框架的，**请避免过度拧紧。**

![](https://wiki.bambulab.com/a1/maintenance/wifi-antenna/%E5%AE%89%E8%A3%85%E6%94%AF%E6%9E%B6.jpg)

重新连接摄像头、X 轴电机和 Z 轴电机线缆以完成安装。

> **注意：右侧较短线缆为 X 轴电机线缆，插入右上方接口；较长线缆为 Z 轴电机线缆，插入右下方接口。**

![](https://wiki.bambulab.com/a1/maintenance/wifi-antenna/%E6%8E%A5%E7%BA%BF%E7%BC%86.jpg)

## 联系客户支持注册序列号

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的主板也将不能再被注册或绑定。

更换了主板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换主板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。  
![register_sn.jpg](https://wiki.bambulab.com/x2d/maintenance/ap-board/register_sn.jpg)

## 功能校验

注册新的序列号后，将打印机绑定至您的账户。

为确保更换顺利，请打开打印机并使用。

如果打印机如预期工作，则安装成功。

## **操作后的校准步骤**

建议您在更换完主板后进行一次全面校准，以确保打印机顺畅运行。

## **潜在问题和解决方案**

如果您在安装新主板时遇到问题，请查阅以下列出的问题及其解决方案：

### 打印机无法开机

确认主板电源线安装正确，请参见 *1. 重新将主板线缆连接至电源**。*

### 其中一个轴无法正常工作

检查电机线缆是否正确安装，请参见 *8. 安装线缆支架并连接线缆*。

### 打印机无法连接至 Bambu Lab 帐户

新主板需要客户支持注册。因此，请向客户支持提供新主板的序列号以注册，请参考该wiki：[如何查找序列号及注册新序列号](../../general/find-sn.md)。

## **结束语**

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
