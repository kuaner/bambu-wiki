---
path: zh/x1/manual/door-sensor
title: "X1C开门检测传感器"
description: "X1C开门检测传感器工作原理"
tags: []
created: 2025-07-28T06:29:18.067Z
updated: 2026-02-11T08:43:12.527Z
source: https://wiki.bambulab.com/zh/x1/manual/door-sensor
---

开门检测传感器是拓竹X1C系列的一项智能部件。该组件能够在打印机前门开启时及时提醒用户，保障打印安全。本指南将全面介绍开门检测传感器的工作原理、开启方法以及更换流程。

## 工作原理

开门检测传感器是一种用于检测玻璃前门开闭状态的小型磁性开关，安装在打印机外壳内部靠近右上角的框架位置（如下图所示）。

![](https://wiki.bambulab.com/knowledge-sharing/door-sensor/door_sensor_in_x1c.png)

该传感器包含一个开关结构，会从打印机内侧穿过框架上的小孔露出。

![](https://wiki.bambulab.com/knowledge-sharing/door-sensor/door_sensor_switch.png)

当门关闭时，门的一侧会压住触发器或开关，使其保持在启动状态；当门被打开时，开关也打开，传感器会向打印机发送信号，打印机将根据您设置的配置作出响应——例如发送通知或暂停打印（关于开门检测响应的两种设置方式，请参阅本Wiki中的说明）。

需要特别说明的是：该功能不会自动关闭前门，它的作用是在检测到门打开时提醒用户手动处理，以保障打印过程的安全性与稳定性。

## 功能与优势

在进行3D打印时，保持打印腔体内的温度稳定至关重要，特别是在使用诸如ABS等对温度变化较为敏感的耗材时。当机壳门被打开时，打印机会立刻检测到这一变化，提醒用户及时采取措施，从而有助于更好地维持机内温度的稳定。但在打印PLA、TPU或PETG等低温材料时，前门应保持部分开启，以防止出现热蠕变，影响打印质量。

此外，为了控制打印时的噪音，保持前门关闭也是非常必要的。门关闭后，打印机的内部风扇和步进电机运行声音会被有效隔绝，从而显著降低噪音水平。此功能可尤其应用于家庭或办公环境，能避免打印过程对周围人群造成干扰。

需要注意的是：该功能默认处于关闭状态。如需启用开门检测功能，可通过Bambu Studio软件或打印机触控屏进行设置。

## 通过Bambu Studio启用开门检测功能

打开Bambu Studio软件，并确保已正确完成设置流程，包括连接你的3D打印机。如果尚未完成初始设置，请参阅[Bambu Studio 快速上手教程](../../software/bambu-studio/studio-quick-start.md)了解详细步骤。  
打开软件后，进入“**设备**”页面。

![bambustudio1.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/bambustudio1.png)

在设备页面中，点击“**打印选项**”。

![bambustudio2.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/bambustudio2.png)

在弹出的设置窗口中，勾选 “**开门检测**”。

![bambustudio3.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/bambustudio3.png)

## 通过触控屏启用开门检测功能

前往“**设置”**。

![lcdscreen_door1.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/lcdscreen_door1.png)

选择“**打印选项”**。

![lcdscreen_door2.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/lcdscreen_door2.png)

向下滑动（点击向下箭头）至“**开门检测”**项。

![lcdscreen_door3.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/lcdscreen_door3.png)

勾选即可启用。

## 开门检测响应设置

启用“开门检测”功能后，系统将提供两个响应模式可选：

- 通知
- 暂停打印

下面分别介绍这两种模式的功能。

### 1. 通知

在本模式下，若在打印过程中打开前门，触控屏的通知区域将弹出警告信息。这是系统的默认设置。

![notification1.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/notification1.png)

该信息会提示你“检测到打印过程中开门”，同时屏幕还会显示一个错误代码和一个二维码，您可以通过扫码访问本Wiki页面，查看详细说明与处理建议。

![notification2.jpg](https://wiki.bambulab.com/knowledge-sharing/door-sensor/notification2.jpg)

请注意：选择此模式时，打印任务不会暂停，打印将继续进行。

### 2. 暂停打印

在本模式下，若在打印过程中打开前门，打印机将自动暂停打印。此时，触控屏上会弹出提示，显示“检测到门已打开，暂停打印”，并提供三个操作选项：

- **继续**：恢复打印任务
- **停止**：终止当前打印
- **前往机器助手**：跳转至通知页面，并显示二维码，可扫码查看相关帮助内容（包括本Wiki页面）

![stopprinting1.jpg](https://wiki.bambulab.com/knowledge-sharing/door-sensor/stopprinting1.jpg)

## 开门检测传感器无响应：可能原因与解决方案

如果您已经启用了开门检测功能，但设备没有任何反应，可能存在以下几种原因及对应的解决方法：

### 1. 固件问题

建议你先尝试将固件更新到最新版本，以排除系统层面的问题。请在页面中点击“**固件**”。

![firmware1.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/firmware1.png)

在新弹出的窗口中，您将看到当前固件的版本历史记录。如固件需更新时，右上角“**更新**”按钮会变亮。

![firmware2.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/firmware2.png)

### 2. 门开关固定不牢

如果前门开关没有固定牢固，就可能发生偏移或与前门错位，从而导致无法准确检测门的开关状态，出现失效或无响应的情况。该开关通过单颗螺丝固定，**确保螺丝紧固但勿过紧**，以免损坏开关或其支架。当开关位置不正确或松动时，门关闭时无法充分压住触发器，门打开时也无法正常释放，这都会使打印机无法正确识别门的状态变化。

### 3. 传感器连线故障或损坏

如果连接开门检测传感器的导线存在故障，或未正确插入连接器，开门检测功能会发生故障。

![](https://wiki.bambulab.com/knowledge-sharing/door-sensor/wire.png)

请仔细检查连接传感器的两根导线，确保它们的线端牢固插入顶部连接器中。  
![faulty_or_broken_wire1.jpg](https://wiki.bambulab.com/knowledge-sharing/door-sensor/faulty_or_broken_wire1.jpg)

如果导线松动或插接不到位，传感器将无法向打印机传输信号。此外，还应检查导线是否存在破损、磨损或老化等问题，这些都可能导致信号中断，影响传感器正常工作。

### 4. 开门检测传感器故障

如果开门检测传感器开关本身发生故障，即使布线正常、安装位置正确，打印机也可能无法检测到门的开启或关闭状态。这将导致无法触发提醒，或在门打开时未能暂停打印任务。

在这种情况下，更换开门检测开关是唯一有效的解决办法。你可以参考官方的[更换开门检测开关](../replace-door-detection-switch.md)页面，了解详细的更换步骤。

## 如何关闭开门检测传感器

如果您不希望在每次前门打开时都收到提示或干扰打印任务，可以选择关闭开门检测功能。操作方法与前文所述的启用步骤相同，不同之处在于取消勾选“开门检测”选项即可。你可以在Bambu Studio或者打印机触控屏上操作：

在X1C打印机的触控屏上，**取消勾选**该项即可。

![door_detection1.png](https://wiki.bambulab.com/knowledge-sharing/door-sensor/door_detection1.png)

完成设置后，开门检测功能将被关闭。此后，即使打印过程中打开前门，系统也不会弹出提示或自动暂停打印任务。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
