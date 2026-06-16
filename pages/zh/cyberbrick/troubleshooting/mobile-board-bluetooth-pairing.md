---
path: zh/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing
title: "如何使用手机端CyberBrick绑定设备核心板?"
description: "本文将详细讲述如何在CyberBrick手机端app的设备列表里，快速找到设备并准确地通过蓝牙连接设备核心板。"
tags: []
created: 2025-10-16T14:24:43.170Z
updated: 2026-06-03T05:51:50.031Z
source: https://wiki.bambulab.com/zh/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing
---

**在多台设备蓝牙开启的状态下，也可以实现设备蓝牙匹配简便又精准。**

在多个设备的蓝牙同时开启的状态下，在CyberBrick手机端 App上，设备列表里会显示多个设备。

如何在CyberBrick手机端app的设备列表里，快速找到设备并准确地通过蓝牙连接设备核心板？请按照以下步骤操作，来完成设备核心板的匹配和连接。

## 1. 寻找模型

打开 CyberBrick 手机端 App，在'发现'页面找到您的模型，点击并打开模型。点击’开始使用‘ > ‘连接设备’。

![cn-mobile-board-bluetooth-1.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing/cn-mobile-board-bluetooth-1.png)

## 2. 选择核心板

在 ‘创作者配置’ 页面中，点击选择创作者配置文件（或我的配置文件）。在下方上传配置到你的设备模块中，点击 '模型' 卡片中的 ‘选择设备’ 按钮。

![cn-mobile-board-bluetooth-2.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing/cn-mobile-board-bluetooth-2.png)

## 3. 连接设备

设备核心板的产品序列号印在核心板的标签上，请查看该标签获取序列号(参考下图中的产品序列号示例。此示例的核心板蓝牙出厂默认名称为CyberBrick-[9236])。按照核心板产品序列号后四位，在'连接新设备' 菜单中，匹配到对应的核心板蓝牙出厂默认名称CyberBrick-[产品序列号后4位]，然后点击'连接‘。

> **提示**
>
> 1. 设备核心板的蓝牙出厂默认名称为CyberBrick-[产品序列号后4位]，并会显示在'连接新设备' 菜单的设备列表中。如果已修改设备核心板的蓝牙名称，请选择新的蓝牙名称。
> 2. 部分核心板的蓝牙出厂默认名称为RC\_MODULE，且会对应地显示在设备列表中。

![cn-mobile-board-bluetooth-3.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing/cn-mobile-board-bluetooth-3.png)

## 4. 确认指示灯

当板载指示灯弹窗出现时，观察设备核心板指示灯的颜色和闪烁频率是否与弹窗中示例图的内容相符。如果相符，点击 '下一步' 。（如果核心板已输入过PIN码，则按钮显示‘连接’。）

|  |  |
| --- | --- |
|  |  |

如果不相符，点击'重新选择'，返回设备列表。选择正确的设备名称后，再重新连接。

![cn-mobile-board-bluetooth-4.1.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing/cn-mobile-board-bluetooth-4.1.png)

## 5. 输入PIN码

在PIN码弹窗中，输入您的PIN码。然后，点击'连接'。

![cn-mobile-board-bluetooth-5.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing/cn-mobile-board-bluetooth-5.png)

## 6. 发送配置

在 ‘确认开始上传’ 的弹窗中，点击 ‘开始上传’，开始将配置文件上传到设备核心板。  
在上传过程中，点击上传面板中的 ‘后台运行’ 按钮，上传面板收起。在探索、设备、我的页面底部，您将会看到上传进度条。

![cn-mobile-board-bluetooth-6.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing/cn-mobile-board-bluetooth-6.png)

## 7. 确认配置上传完成

上传配置成功后，您将会收到'上传成功'的消息提示。点击该提示，进入上传成功结果页。

![cn-mobile-board-bluetooth-7.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/mobile-board-bluetooth-pairing/cn-mobile-board-bluetooth-7.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
