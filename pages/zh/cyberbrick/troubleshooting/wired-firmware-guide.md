---
path: zh/cyberbrick/troubleshooting/wired-firmware-guide
title: "CyberBrick USB 升级工具指南"
description: "本文将详细讲述如何使用CyberBrick USB 升级工具。"
tags: []
created: 2025-07-17T12:49:41.230Z
updated: 2026-05-12T09:46:49.564Z
source: https://wiki.bambulab.com/zh/cyberbrick/troubleshooting/wired-firmware-guide
---

> 本指南详细说明了如何使用 CyberBrick USB 升级工具来更新 CyberBrick 硬件设备的固件或恢复出厂设置。CyberBrick 是一个基于微控制器的多功能平台，适用于遥控（RC）套件和延时摄影套件等应用。本指南涵盖了执行固件更新或重置的步骤。

## 软件界面

1. `RC framework 升级`：恢复出厂设置。单击将重置为 RC 应用（遥控套件）。
2. `延时摄影套件升级`：恢复出厂设置。单击将重置为延时摄影应用（延时摄影套件）。
3. `恢复出厂设置`：重置用户设置信息。单击将清空用户设置信息，包含PIN码，设备命名，主从绑定信息等。

![usb-pic1.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/usb-pic1.png)

4. `刷新`：单击以刷新串口设备列表。

![usb-pic2.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/usb-pic2.png)

## 如何刷入

1. 断开核心板与电池的连接。
2. 保持按住核心板的“KEY”按键，通过Type-C数据线接入电脑后 2秒 再松开“KEY”按键。

![usb-pic3.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/usb-pic3.png)

3. 确认此时核心板的 LED 是熄灭状态。

![usb-pic4.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/usb-pic4.png)

4. 点击''刷新''，左侧将会出现新的 COM 端口。
5. 选择新出现的 COM 端口，然后点击下方对应的固件刷新按钮（遥控套件选择“RC framework 升级”，延时摄影套件选择“延时摄影套件升级”，清除 PIN 码选择“恢复出厂设置”）。等待固件刷新完成。
6. 如果接入Type-C数据线后，检索不到COM 端口，请检查并更换数据线。
7. 如果刷入失败，请按上述步骤重试或联系客户服务团队。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
