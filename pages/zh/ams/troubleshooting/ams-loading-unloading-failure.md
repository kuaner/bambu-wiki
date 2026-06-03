---
path: zh/ams/troubleshooting/ams-loading-unloading-failure
title: "AMS 进退料失败故障排查"
description: "本文介绍了 AMS 常见的进退料失败的原因和故障排查方法"
tags: []
created: 2023-09-25T09:55:36.101Z
updated: 2026-04-30T10:32:07.036Z
source: https://wiki.bambulab.com/zh/ams/troubleshooting/ams-loading-unloading-failure
---

本文介绍了 AMS 常见的进退料故障的排查方法。当您在打印机的过程中遇到了进退料失败的问题，您可以根据报错信息以及故障现象来参考本文进行故障排查。

在您进行 AMS 进退料故障排查之前，我们建议您先考 [这篇 Wiki](../manual/ams-function-introduction.md) 来了解 AMS 的主要功能，如**预上料、读取RFID、进退料和打印助力模式的工作原理**，方便后续的排查。

## 1. 预上料失败排查

在 AMS 空闲的状态，插入耗材丝，会进行预上料。上下料器会把耗材送入五通，待五通的传感器检测到耗材后再拉回。如果预上料过程失败，则有以下几种可能性：

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/10-%E6%AD%A3%E5%B8%B8%E7%9A%84%E9%A2%84%E4%B8%8A%E6%96%99%E8%BF%87%E7%A8%8B%E5%8A%A8%E5%9B%BE.gif)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E9%A2%84%E4%B8%8A%E6%96%99%E9%98%B6%E6%AE%B54.png)

### 1.1 上下料器传感器异常

插入耗材丝时，指示灯状态不变，传感器并未检测到有耗材丝。您可以参考这篇wiki了解AMS正常时指示灯的状态：[AMS指示灯状态解析](../../x1/troubleshooting/ams-led-status.md)。

正常情况下，插入耗材后指示灯为白色常亮，没有耗材的时候指示灯不亮，如下图所示：

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/08-%E6%96%99%E7%BA%BF%E9%80%80%E5%87%BA%E8%BF%9B%E6%96%99%E5%99%A8%E5%8A%A8%E5%9B%BE.gif)

如果插入耗材后指示灯状态不变，有可能是传感器故障了，可以参考这篇wiki清洁一下霍尔传感器的位置后再重试：[AMS第一阶段进料器故障排查](../../x1/troubleshooting/AMS-first-stage-feeder-fault.md)。也可以使用[插入辅助](https://wiki.bambulab.com/zh/ams/manual/ams-function-introduction#%E6%8F%92%E5%85%A5%E8%BE%85%E5%8A%A9%E5%8A%9F%E8%83%BD)功能，确认一下上下料器的电机是否工作正常。

### 1.2 上下料器电机异常

插入耗材丝后，上下料器的指示灯状态变了，但是上下料电机完全不动，没有把耗材丝往里拉，可能是电机线松了或者电机故障，可以参考这篇wiki进行排查：[AMS第一阶段进料器故障排查](../../x1/troubleshooting/AMS-first-stage-feeder-fault.md)。

### 1.3 上下料器齿轮异常

插入耗材丝后，上下料器的指示灯状态变了，能看到上下料器中的电机轴或者齿轮在旋转，但是无法将料往前送，有可能是齿轮异常了，可以录制一段视频，并联系我们的售后团队。

### 1.4 五通传感器异常

如果耗材丝送入五通后，仍然持续往前送没能拉回，说明是五通的耗材传感器异常了。或者往回退料的时候，把料完全退出上下料器，且上下料器常亮红灯，有可能是耗材丝断在五通内部或者传感器异常了，请参考这篇wiki检查五通内部是否有断料或者传感器是否正常工作：[拆解和清洁AMS五通组件](../../x1/troubleshooting/clean-the-filaments-hub.md)。

检查五通耗材传感器是否正常的方法：手动把耗材送至五通位置，可以看到对应槽的线条变粗；把耗材拉出五通后，加粗的线条消失，如图所示（图片适用于X1系列，其他系列可以在 Bambu Handy 或 Bambu Studio 中查看）：

![](https://wiki.bambulab.com/check-internal-hub-unit-cn.gif)

## 2. 读取RFID失败排查

在读取RFID信息时，**AMS会先进行预上料绷紧料线，然后再把耗材送出AMS一段来转动料盘，让RFID标签扫过电路板读取RFID信息**。如果该过程送料异常或者未能读取到RFID信息，则有以下可能性：

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E8%AF%BB%E5%8F%96rfid%E8%BF%87%E7%A8%8B.gif)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%AF%BB%E5%8F%96rfid%E9%98%B6%E6%AE%B51.png)

### 2.1 五通电机不转

读取RFID过程中，如果料盘转动一点就停止，无法将料送出AMS（从AMS后面的料管无法看到耗材被送出），且能听到耗材丝被堵在AMS内部的声音，有可能是电机不转或者内部齿轮卡死导致的。请录制一段视频并上传日志给我们进一步分析

### 2.2 耗材在五通打滑

读取RFID过程中，料无法被送出AMS，能听到AMS内部电机转动的声音，且取出耗材丝后看到内侧凹陷被磨出坑，说明是耗材和五通齿轮打滑了。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/312px-notch.png)

- 请尝试别的耗材丝。
- 参考下方图片重新拧紧五通保护盖上的这4个螺丝后再次尝试。
- 如果始终无法解决，请录制一段视频并上传日志文件联系我们售后人员，有可能是五通挤出齿轮需要更换：[更换AMS五通挤出轮](../../x1/maintenance/replace-gear-unit-in-filaments-hub.md)。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/remove_gear_unit.png)

### 2.3 里程轮异常

读取RFID过程中，能看到耗材丝被送到大约打印机背面气管接头的位置，然后再被拉回，上下料器发出哒哒哒的声音。重复多次，但始终无法读出RFID信息。

可能是五通的里程轮线松了或者里程轮异常，请参考wiki重新连接五通里程轮的线缆：[更换AMS主板](../../x1/maintenance/replace-ams-main-board.md)。

若无法解决，请录制一段视频并联系我们售后团队。

### 2.4 电路板无法读取RFID信息

如果读取RFID过程进退料正常，但是无法读取出材料信息，则参考以下步骤排查：

1. 当用AMS读取RFID的时候，需要处于空闲状态，如果已经有料送出AMS则无法读取RFID。AMS内部有两块电路板负责读取RFID芯片，一块板负责两个槽位的耗材RFID识别（1&2号槽共用一个RFID板，3&4号槽共用另一个，如下图所示）。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E8%AF%BB%E5%8F%96rfid.png)

2. 如果一组槽里，其中一个槽无法正确识别RFID，可以换一卷料试试，如果其他耗材能被正确识别，说明是这卷耗材的RFID标签有问题，也可以尝试翻转这卷料的两面再试试（每卷料的两侧各有一个RFID标签）。
3. 如果相邻两个槽都无法正确识别RFID，有可能是对应的RFID板出问题了，交换两块RFID板子的位置，看看问题是否转移到另一组槽位上，则可以确认是否是RFID板的问题。
4. 如果无论放入什么耗材，4个槽全部都无法正确读取RFID信息，有可能是AMS主板异常了，需要联系我们售后团队进行确认。

## 3. 进料失败排查

### 3.1 耗材送出AMS失败

如果出现该错误，**说明送料过程中，AMS的五通霍尔开关始终没有检测到耗材丝**。可能是由于以下原因导致进料失败：

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E9%80%81%E5%87%BAams%E5%A4%B1%E8%B4%A5.jpg)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/02-%E6%96%99%E7%BA%BF%E6%9C%AA%E9%80%81%E8%87%B3%E4%BA%94%E9%80%9A%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E9%80%81%E5%87%BAams%E5%A4%B1%E8%B4%A51.png)

#### 3.1.1 上下料器异常

有可能是上下料器异常了，通常这种情况预上料也无法正常进行。请参考上文的[预上料失败排查](#%E9%A2%84%E4%B8%8A%E6%96%99%E5%A4%B1%E8%B4%A5%E6%8E%92%E6%9F%A5)，重启打印机，插入耗材进行一次预上料，检查上下料器各项功能是否正常。

#### 3.1.2 五通霍尔开关异常

点击“进料”后，耗材顺利从AMS背面的PTFE管送出，但仍然报错耗材送出AMS失败，这可能是五通的霍尔开关异常，检测不到耗材丝，所以判定为耗材丝仍在AMS内部。请参考上文的[预上料失败排查](#%E9%A2%84%E4%B8%8A%E6%96%99%E5%A4%B1%E8%B4%A5%E6%8E%92%E6%9F%A5)，重启打印机，插入耗材检查五通的霍尔传感器功能是否正常。

#### 3.1.3 缓冲信号丢失

当预上料和读取RFID的过程能够正常工作，而点击“进料”按钮后，上下料器电机没有任何反应且报错“耗材送出AMS失败”，这可能是由于缓冲器异常所导致，请参考这篇Wiki进行故障排查：

[HMS\_0700-4000-0002-0001: 料线缓冲信号丢失，电缆或信号传感器可能出现故障。](../../x1/troubleshooting/hmscode/0700_4000_0002_0001.md)

### 3.2 耗材送往挤出机失败

**当耗材送出AMS五通，五通的霍尔开关检测到耗材了，而挤出机的霍尔开关始终没有检测到耗材，就会出现这个报错。** 可能由于以下原因导致进料失败：

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E9%80%81%E5%BE%80%E6%8C%A4%E5%87%BA%E6%9C%BA%E5%A4%B1%E8%B4%A5.jpg)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/19-%E6%96%99%E7%BA%BF%E6%9C%AA%E9%80%81%E8%87%B3%E6%8C%A4%E5%87%BA%E6%9C%BA%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E9%80%81%E5%85%A5%E6%8C%A4%E5%87%BA%E6%9C%BA%E5%A4%B1%E8%B4%A51.png)

#### 3.2.1 五通电机不转

当五通霍尔开关检测到耗材，但此时可能由于五通电机没有转动，从而无法将耗材送出AMS。如果遇到这个问题，请参考下面wiki重新插拔五通电机连接线，如果电机依然故障，请联系我们的售后服务。[更换AMS五通组件](../../x1/maintenance/replace-filament-hub.md)。

![](https://wiki.bambulab.com/x1/manual/intro-ams/filament-hub.jpg)

#### 3.2.2 料盘或耗材卡住

当耗材缠绕或料盘卡住的时候，会导致进料失败，请检查耗材是否缠绕或料盘是否卡住。

#### 3.2.3 料管中有断料

当料管中有断料的时候，也有可能因为断料挡住了后面的料，使得进料失败。请检查料管中是否有任何断料或者异物。[耗材断在管道中间](../../x1/troubleshooting/filament-breaks-in-path.md)。

#### 3.2.4 耗材在五通打滑

送料过程，且取出耗材丝后看到内侧凹陷被磨出坑，说明是耗材和五通齿轮打滑了。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/312px-notch.png)

- 尝试别的耗材丝。
- 参考下图重新拧紧五通保护盖上的这4个螺丝后再次尝试。
- 如果始终无法解决，请录制一段视频并上传日志文件联系我们售后人员，有可能是五通挤出齿轮需要更换：[更换AMS五通挤出轮](../../x1/maintenance/replace-gear-unit-in-filaments-hub.md)。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/remove_gear_unit.png)

#### 3.2.5 气动接口异常

如果送料过程每次耗材都停在下图所示的位置，请确认耗材是否在气管接头处受到阻力，导致进料失败。

如果耗材在箭头位置处受到阻力，无法送至工具头，请将PTFE管拆下查看是否由于气动接头损坏导致进料失败，或者交换PTFE管的两端再插入试试。如果气动接头损坏，则需更换。

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E5%8D%A1%E5%9C%A8%E6%B0%94%E5%8A%A8%E6%8E%A5%E5%A4%B4.png)

#### 3.2.6 挤出机传感器异常

如果您观察到耗材已经送入挤出机，然后又自动退回，重复几次后报错“耗材送入挤出机失败”，可能是因为挤出机霍尔开关故障导致没有检测到耗材。

请参考这篇Wiki来检查霍尔开关的磁铁是否没有正常回弹：

[HMS\_0700-2000-0002-0004: AMS1 料槽1料线可能断在工具头。](../../x1/troubleshooting/hmscode/0700_2000_0002_0004.md)。

此外，通过以下方式，可以检查挤出机传感器是否能检测到耗材丝：

- X 系列：  
  您可以将显示屏切换到"温度/轴移动"，观察下图所示的绿点是否亮起。如果绿点亮起，则表示挤出机传感器检测到耗材丝。

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/24-x1%E6%8C%A4%E5%87%BA%E6%9C%BA%E5%9B%BE%E6%A0%87%E7%BB%BF%E7%82%B9%E4%BA%AE%E8%B5%B7.png)

- 所有系列：  
  者可以打开Bambu Studio并切换到“设备”页面，观察下图所示的绿点是否亮起，如果亮起则表明挤出机传感器检测到耗材。

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/p1_con.jpg)

### 3.3 耗材挤出失败

当AMS成功送料至挤出机，且挤出机也成功检测到有耗材送入（如上图所示的绿点），但是报错“耗材挤出失败”，通常是由于挤出机的齿轮没有成功咬合耗材。原因有以下几种：

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E6%8C%A4%E5%87%BA%E5%A4%B1%E8%B4%A5.jpg)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E6%8C%A4%E5%87%BA%E5%A4%B1%E8%B4%A51.png)

#### 3.3.1 挤出机堵塞

当挤出机堵塞时，由于还有耗材堵塞在挤出机中，新送入的耗材无法被挤出机咬合，从而会出现耗材挤出失败的报错信息。可以尝试用外挂料盘上料并尝试挤出。如果用外挂料盘也无法顺利进料挤出，请参考这篇wiki对挤出机进行清理：

[挤出机堵塞](../../x1/troubleshooting/extruder-clog.md)

#### 3.3.2 缓冲信号异常

当挤出机耗材传感器正常，而AMS把耗材送至工具头但挤出机无法咬合耗材并挤出，且可以使用外挂料盘打印，这可能是由于缓冲信号异常所导致进料失败。您可以参考这篇Wiki进行故障排除：

[HMS\_0700-4000-0002-0004: 缓冲区信号异常，弹簧可能被卡住了。](../../x1/troubleshooting/hmscode/0700_4000_0002_0004.md)

#### 3.3.3 五通电机异常

如果不是由于以上的问题所导致进料失败，这可能由于五通电机异常导致进料失败。请您上传打印机日志并联系售后来帮助您解决问题。

- [如何上传打印机的日志文件](https://wiki.bambulab.com/zh/X1/troubleshooting/how-to-upload-log)
- [如何将日志文件上传到现有工单](../../x1/troubleshooting/update-log-to-a-ticket.md)

## 4. 退料失败故障排查

当使用AMS的时候出现退料失败时，请先观察耗材是否从挤出机中退出。

### 4.1 耗材退出挤出机失败

**当AMS退料一段时间后，挤出机仍检测到内部有料，则会出现该报错**。这可能是由于以下原因造成：

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E9%80%80%E5%87%BA%E6%8C%A4%E5%87%BA%E6%9C%BA%E5%A4%B1%E8%B4%A5.jpg)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E9%80%80%E5%87%BA%E6%8C%A4%E5%87%BA%E6%9C%BA%E5%A4%B1%E8%B4%A52.png)

#### 4.1.1 **挤出机堵塞**

当耗材无法从挤出机从退出而导致退料失败，这可能是由于挤出机堵塞或者退料阻力过大导致的。

在退料失败时，先按压气管接头并拆除料管，然后拉动耗材丝。如果无法拉动耗材丝，说明是耗材堵塞在挤出机内部；如果可以轻易地将耗材丝从工具头拉出，则说明是阻力过大导致的退料失败，请参考下文的[退料阻力过大](#%E9%80%80%E6%96%99%E9%98%BB%E5%8A%9B%E8%BF%87%E5%A4%A7)进行排查。如果挤出机堵塞了，请参考这篇Wiki对挤出机进行清理：

[挤出机堵塞](../../x1/troubleshooting/extruder-clog.md)

![](https://wiki.bambulab.com/x1/troubleshooting/ams-filament-run-out/%E6%96%99%E7%AE%A1%E6%8E%A5%E5%A4%B4.png)

#### 4.1.2 挤出机霍尔开关异常

当耗材已经从挤出机中退出，而依然显示耗材退出挤出机失败。请先参考[挤出机传感器异常](#%E6%8C%A4%E5%87%BA%E6%9C%BA%E4%BC%A0%E6%84%9F%E5%99%A8%E5%BC%82%E5%B8%B8)来查看挤出机图标中的绿点是否亮起，如果绿点亮起，则可能的原因如下：

- 挤出机中存在断料
- 挤出机霍尔开关异常

具体的故障排查方法参考wiki：[HMS\_0700-2000-0002-0004: AMS1 料槽1料线可能断在工具头。](../../x1/troubleshooting/hmscode/0700_2000_0002_0004.md)

#### 4.1.3 退料阻力过大

通常，工具头料管弯曲过多或者五通内部有碎屑堆积会带来过大的阻力，从而影响到正常退料。**首先要确保把打印机固件升级到最新版本，最新的固件优化了退料失败的问题。**

**(1) PTFE管弯折过大**

当在工具头上方的PTFE管弯折过大时，则可能导致耗材在PTFE管中的阻力过大，因此无法被拉回，从而导致退料失败。

您可以[点击这里](https://wiki.bambulab.com/ams/ams-load-unload-failure/pipe_bracket_id.stl)下载来PTFE管支架，将其安装在工具头上方，防止与工具头连接的PTFE管弯折过大。

**PTFE管支架安装如下图所示：**

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/29-%E6%96%99%E7%AE%A1%E6%94%AF%E6%9E%B6%E5%AE%89%E8%A3%85%E7%A4%BA%E6%84%8F%E5%9B%BE.jpg)

**(2) 五通碎屑堆积**

当使用AMS时间较长时，过多的耗材碎屑堆积在五通内部会造成过大的阻力，从而导致退料失败。您可以参考这篇wiki来对五通内部进行清理：

[清洁AMS五通组件](../../x1/troubleshooting/clean-the-filaments-hub.md)

**(3) 特殊耗材退料失败**

如果仅仅是某些耗材退料失败，例如PLA-CF之类较硬的耗材，我们建议您将其放在打印机背后的料盘支架上来打印。

### 4.2 耗材退回AMS失败

**当AMS退料一段时间后，挤出机的霍尔开关检测到料已退出挤出机，但是AMS的五通仍然检测到有料（完整的退料过程会把料退到AMS内部）**，则会弹出该报错。这可能由以下原因导致：

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E9%80%80%E5%9B%9Eams%E5%A4%B1%E8%B4%A5.jpg)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/%E8%80%97%E6%9D%90%E9%80%80%E5%9B%9Eams%E5%A4%B1%E8%B4%A51.png)

#### 4.2.1 阻力过大导致无法退回

请参考[退料阻力过大](#%E9%80%80%E6%96%99%E9%98%BB%E5%8A%9B%E8%BF%87%E5%A4%A7)，尝试减小退料时的阻力来改善这个问题。

#### 4.2.2 五通内有断料或者传感器异常

当耗材从上下料器中已经退出，但此时AMS仍然在持续退料过程，并且AMS上下料器指示灯保持红色常亮（如下图所示）。这可能是由于五通内部存在断料，从而导致退料失败。请参考这篇Wiki拆开五通进行清理，并检查传感器是否正常。

[清洁AMS五通组件](../../x1/troubleshooting/clean-the-filaments-hub.md)

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/22-%E4%BA%94%E9%80%9A%E5%AD%98%E5%9C%A8%E6%96%AD%E6%96%99%E6%97%B6%E8%BF%9B%E6%96%99%E5%99%A8%E7%BA%A2%E7%81%AF%E5%B8%B8%E4%BA%AE.png)

#### 4.2.3 料盘转动异常

退料时，五通电机负责往回拉动耗材丝，而上下料器负责驱动料盘往回转。如果退料时出现下图中的现象，说明料盘没有转动，或者料盘的转动速度慢于五通电机退料的速度。

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/30-%E6%96%99%E7%9B%98%E4%B8%8D%E8%BD%AC%E5%AF%BC%E8%87%B4%E9%80%80%E6%96%99%E5%A4%B1%E8%B4%A5.jpg)

**（1）料盘完全不转**

这可能是由于主动支撑套筒没有完全卡入AMS框架中，因此只有进料器黄色齿轮转动，而黑色主动支撑套筒没有转动，从而无法带动料盘转动导致退料失败，通常这种情况上下料器齿轮还会摩擦发出嗡嗡嗡的声音。您可以参考下图将主动支撑套筒卡入AMS框架中：

![](https://wiki.bambulab.com/ams/ams-load-unload-failure/31-%E4%B8%BB%E5%8A%A8%E6%94%AF%E6%92%91%E5%A5%97%E7%AD%92%E5%AE%89%E8%A3%85%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

**（2）料盘转动速度慢于五通退料速度**

如果退料时料盘会转，但是转动速度慢于五通退料的速度。请确认该现象是否只发生在某一个特定槽位，如果是，可以尝试交叉验证，交换两个槽的上下料器试试。如果问题始终发生在同一个上下料器上，则说明是上下料器故障。如果问题发生在多个槽位，请录制一段视频并联系我们售后团队。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
