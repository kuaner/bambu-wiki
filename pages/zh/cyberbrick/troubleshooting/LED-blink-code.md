---
path: zh/cyberbrick/troubleshooting/LED-blink-code
title: "CyberBrick核心板状态 LED 灯语"
description: "本章将介绍 CyberBrick 的 LED 灯光信号及其含义。"
tags: []
created: 2025-07-24T14:34:04.910Z
updated: 2025-07-25T10:24:35.146Z
source: https://wiki.bambulab.com/zh/cyberbrick/troubleshooting/LED-blink-code
---

核心板上配有一个可编程的彩色状态指示灯（RGB LED），在核心板处于官方固件环境时，它会根据不同的状态显示对应的颜色和闪烁模式，例如连接状态、识别流程、错误提示等。下表列出了默认状态与灯效的对应关系。

![led.jpg](https://wiki.bambulab.com/cyberbrick/troubleshooting/led.jpg)

> 请注意：核心板运行自定义程序时，LED 灯效将由用户程序控制，可能不会遵循下表中的默认状态指示。

## 引导程序灯效 Loader Blink Codes

引导程序是板端最底层的程序，用于更新固件，只有更新固件时核心板会进入引导程序。

The loader is the low-level program on the Core Controller used for firmware updates. The Core enters loader mode only when a firmware update is in progress.

|  | 状态 | LED灯效 |  |
| --- | --- | --- | --- |
| 1 | 固件升级错误 | 红色（0xFF0000）常亮 |  |
| 2 | 固件等待升级 | 白色（0xFFFFFF）常亮 |  |
| 3 | 固件升级中 | 白色（0xFFFFFF）闪烁10Hz |  |

## 固件灯效

固件是承载官方和自定义项目的运行框架，是CyberBrick基于Micropython项目进行二次开发的程序，用于为上层程序支持各类控制和通讯功能。

|  | **状态** | **LED灯效** |  |
| --- | --- | --- | --- |
| **1** | 开机 | 绿色（0x00FF00）常亮 |  |
| **2** | 仅蓝牙连接 | 蓝色（0x0000FF）常亮 |  |
| **3** | 仅2.4G连接 | 黄色（0xFFFF00）常亮 |  |
| **4** | 蓝牙叠加2.4G连接 | 蓝色（0x0000FF）黄色（0xFFFF00）交替闪烁，频率0.5Hz |  |
| **5** | 配置传输 | 蓝色（0x0000FF）闪烁，频率5Hz |  |
| **6** | 快捷识别 | 绿色（0x00FF00）闪烁，频率1Hz，持续5s |  |
| **7** | 固件密钥区损坏 | 红色（0xFF0000）闪烁，频率10Hz |  |
| **8** | MPY停止运行(包括mpy的错误、崩溃、退出和进入REPL的状态) | 紫色（0xFF00FF）闪烁，频率1Hz |  |
