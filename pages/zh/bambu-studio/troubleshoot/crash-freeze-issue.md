---
path: zh/bambu-studio/troubleshoot/crash-freeze-issue
title: "Bambu Studio 崩溃/冻结故障排除指南"
description: ""
tags: []
created: 2023-09-15T04:33:33.152Z
updated: 2025-05-19T13:49:48.231Z
source: https://wiki.bambulab.com/zh/bambu-studio/troubleshoot/crash-freeze-issue
---

本文介绍了如何处理各种操作系统平台上的崩溃和冻结问题。

## Windows平台

### 崩溃问题

- 简单的方法

在Windows平台上，我们将转储信息记录在Studio的日志目录中。请在提交工单时，附上\* .dmp files 文件，有助于我们帮助您分析问题。

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/screenshot-20230907-094745.png)

- 其他方法

您可以从以下地址使用相同的免安装版本的Bambu Studio: [Releases · bambulab/BambuStudio](https://github.com/bambulab/BambuStudio/releases)

例如，v1.7.4.52 的免安装版本是这样的（请确保使用与你要安装版本的相同的版本）

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/non_install_version.png)

如果在使用免安装版本重现此问题后，请将以下日志从[工单](https://bambulab.cn/zh-cn/my/support/tickets?from=5)发送给我们，以便我们进行调试：

- \*.dmp
- crash\_xxx.log
- debug\_xxx.log.n
- debug*network*xxx.log

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/crash_files.jpg)

### 冻结问题

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/screenshot-20230907-095441.png)

当应用程序不再响应用户操作时，尤其是出现无响应弹出对话框时，请使用以下步骤获取转储信息。

- 打开 Windows 任务管理器
- 找到 Bambu Studio 进程
- 从右键单击上下文菜单中选择“创建转储文件”
- 压缩转储文件并通过第三方网盘等云存储方式发送给我们（有时文件可能非常大，约 2GB）

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/20230907-095625.jpg)

## macOS平台

### 崩溃问题

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/crash.png)

在 macOS 上，Crash Reporter 会自动处理崩溃转储。

您可以将文本保存到文件中，然后发送给我们进行分析。

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/crashreport.png)

您还可以从控制台中查找崩溃报告并进入崩溃报告组。

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/crashreportinconsole.png)

或者您可以找到它们在 ~/Library/Logs/DiagnosticReports。在[提交工单](https://bambulab.cn/zh-cn/my/support/tickets?from=5)报告崩溃问题时，请附上 \*.ips 文件。

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/crashreportfiles.png)

### 冻结问题

当应用程序对用户操作不再响应，特别是当出现无响应的弹出对话框时，您可以强制关闭Bambu Studio。诊断报告生成诊断转储文件。

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/forcequit.png)

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/quit.png)

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/hang.png)

您可以将文本保存到文件中，然后发送给我们进行分析。

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/hangreport.png)

您还可以从控制台中查找诊断报告并进入诊断报告组。

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/hangreportincosole.png)

或者在 ~/Library/Logs/DiagnosticReports 中找到它们。在[提交工单](https://bambulab.cn/zh-cn/my/support/tickets?from=5)报告诊断问题时，请附上 \*.ips 文件。

![](https://wiki.bambulab.com/software/bambu-studio/crash_issues/hangdiagfiles.png)

如果您的机器上没有生成 crash report，请按照下列步骤打开 crash report 的设置：

在命令终端上执行

`1\. defaults write com.apple.CrashReporter DialogType developer`  
`设置 crash reporter`  
`2\. defaults read com.apple.CrashReporter`  
`读取 crash reporter，确保设置成了 developer`

然后重启机器，下次软件 crash 的时候就能自动产生 crash report。

## Linux平台

### 崩溃问题

在 Linux 平台上，当遇到 Bambu Studio 崩溃问题时，需要通过 gdb 调试 Bambu Studio。

使用 gdb 调试时，需要找到重现崩溃问题的方法。使用 gdb 调试的步骤如下：

- 运行 gdb BambuStudio\_xxxx\_yyy. AppImage
- 输入 gdb 中的运行命令
- 应用程序崩溃后，在 gdb 中运行 bt 命令
- 将 gdb 执行过程中的所有输出保存到文件中，并在[提交工单](https://bambulab.cn/zh-cn/my/support/tickets?from=5)时一并发送给我们

### 冻结问题

当应用程序不再响应用户操作时，尤其是出现无响应弹出对话框时，可以通过 gdb 调试 Bambu Studio。

使用 gdb 调试的步骤如下：

- 运行 gdb BambuStudio\_xxxx\_yyy. AppImage --pid ,  represents the id of the process
- 按 Ctrl + C
- 在 gdb 中运行 bt 命令
- 将 gdb 执行过程中的所有输出保存到文件中，并在[提交工单](https://bambulab.cn/zh-cn/my/support/tickets?from=5)时一并发送给我们
