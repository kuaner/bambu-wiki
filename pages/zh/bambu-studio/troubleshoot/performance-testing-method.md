---
path: zh/bambu-studio/troubleshoot/performance-testing-method
title: "Bambu Studio 性能测试方法"
description: "当您使用 Bambu Studio 时发现软件运行缓慢、准备窗口或调参时卡顿，可参考本文导出软件工作文件，提供给技术团队分析。"
tags: []
created: 2026-05-14T08:43:03.337Z
updated: 2026-06-03T03:51:51.554Z
source: https://wiki.bambulab.com/zh/bambu-studio/troubleshoot/performance-testing-method
---

## 何时使用

当您使用 Bambu Studio 遇到运行过慢或其他卡顿现象时，可根据指南导出软件运行状态，发送给我们的技术团队分析原因。

## 操作步骤

### 下载软件

在[该链接](https://github.com/microsoft/perfview/releases)中下载最新版本 perfview，或下载[该附件](https://wiki.bambulab.com/software/bambu-studio/performance-testing-method/perfview.exe)。

![](https://wiki.bambulab.com/software/bambu-studio/performance-testing-method/1.png)

### 运行软件

打开 Bambu Studio，双击运行 Perfview，并依次选择采集，或使用快捷键 Alt+C.

![](https://wiki.bambulab.com/software/bambu-studio/performance-testing-method/2.png)

### 配置采集参数

- Focus process 填写 bambu-studio.exe
- 在桌面新建一个文件夹，并复制文件夹地址，粘贴进 Current Dir （或在任意您能找到的位置下，图中以 E 盘示例）
- 勾选“Zip”和“Merge”
- 高级选项中只保留 Kernel Base 和 Cpu Samples

![selection.jpg](https://wiki.bambulab.com/software/bambu-studio/performance-testing-method/selection.jpg)

### 开始采集

开始采集，点击 Start Collection

![start.jpg](https://wiki.bambulab.com/software/bambu-studio/performance-testing-method/start.jpg)

复现问题，再回到 Perfview 停止采集。

![stop.jpg](https://wiki.bambulab.com/software/bambu-studio/performance-testing-method/stop.jpg)

### 导出文件

在建立的文件夹中导出生成的 .Zip 压缩包，通过[工单](../../x1/troubleshooting/how-to-upload-log.md)上传给我们用于分析。

![up1.jpg](https://wiki.bambulab.com/software/bambu-studio/performance-testing-method/up1.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
