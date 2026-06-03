---
path: zh/h2/manual/status-indicator-light-meanings
title: "H2D 状态指示灯含义"
description: "本章节将为您介绍 H2D 打印机状态指示灯的各种显示模式及其对应的含义。"
tags: []
created: 2025-06-06T08:54:55.308Z
updated: 2025-06-10T08:12:15.523Z
source: https://wiki.bambulab.com/zh/h2/manual/status-indicator-light-meanings
---

通过观察打印机状态指示灯的颜色变化与闪烁方式，用户可以快速识别打印机当前所处的工作状态，如空闲、准备、执行任务或报错等。状态指示灯作为打印机的“视觉语言”，能够在无需查看屏幕的情况下，提供直观的状态反馈。

## 空闲状态

- 表现： **白光慢速呼吸（屏幕亮起时）** 或 **灯光熄灭（屏幕休眠时）**
- 说明： 打印机处于空闲待机状态，未执行任何打印任务。

![闲置.webp](https://wiki.bambulab.com/h2/manual/status-indicator-light-meanings/%E9%97%B2%E7%BD%AE.webp)

## 任务准备中

- 表现： **橙色灯光滚动流动**
- 说明： 打印任务准备阶段，包括任务上传、换料、自动调平、喷嘴加热等准备动作正在进行。

![上传.webp](https://wiki.bambulab.com/h2/manual/status-indicator-light-meanings/%E4%B8%8A%E4%BC%A0.webp)

## 执行任务中

- 表现： **白色指示灯显示任务进度条**
- 说明： 正在执行打印任务，**灯光同步显示当前打印进度**，帮助用户直观掌握打印进程。

![打印过程中.webp](https://wiki.bambulab.com/h2/manual/status-indicator-light-meanings/%E6%89%93%E5%8D%B0%E8%BF%87%E7%A8%8B%E4%B8%AD.webp)

## 异常报错

- 表现： **红灯双闪**
- 说明： 打印过程中出现错误，指示灯红灯快速双闪，直到用户关闭错误弹窗提示。

![报错.webp](https://wiki.bambulab.com/h2/manual/status-indicator-light-meanings/%E6%8A%A5%E9%94%99.webp)

## 任务完成

- 表现： **绿灯常亮**
- 说明： 打印任务执行完成。状态指示灯将持续绿色常亮，直到用户在屏幕上关闭“打印完成”提示，或触发门控状态变化（如前门、上盖、左右侧窗开启/关闭）。

![完成状态.jpg](https://wiki.bambulab.com/h2/manual/status-indicator-light-meanings/%E5%AE%8C%E6%88%90%E7%8A%B6%E6%80%81.jpg)
