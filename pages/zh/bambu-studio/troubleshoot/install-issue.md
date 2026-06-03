---
path: zh/bambu-studio/troubleshoot/install-issue
title: "Bambu Studio 安装故障排查"
description: ""
tags: []
created: 2023-12-20T09:22:03.305Z
updated: 2025-12-26T06:15:08.513Z
source: https://wiki.bambulab.com/zh/bambu-studio/troubleshoot/install-issue
---

## 软件安装故障

### 始终提示“Bambu Studio 正在运行”（Windows）

此故障可能是由于旧版 Bambu Studio 软件出现问题无法正常退出导致的，最简单的解决方法就是**尝试重启计算机并继续安装。**

### 软件安装过程中覆盖文件失败（Windows）

此故障是由于 BambuSource.dll 错误加载导致的。由于 BambuSource.dll 在系统中是作为 Windows Media Player 的视频播放插件注册的，因此该文件可能被其他播放软件错误加载。**可以通过找到被错误加载的 DLL 文件并手动删除来解决问题。**

如果 DLL 文件删除失败，这是因为某些软件正在使用该 DLL 文件，**重新启动计算机**可以解决问题。但是，不排除一些使用该 DLL 文件的软件随系统自启动，在这种情况下该问题可能通过重启解决。此时，你需要**手动终止该软件的运行，之后再继续安装 Bambu Studio**。

### 命令行参数 0 无法转换为 Unicode，已被忽略

![警告.jpg](https://wiki.bambulab.com/bambu-studio/troubleshoot/%E8%AD%A6%E5%91%8A.jpg)

“Command line argument 0 couldn't be converted to Unicode and will be ignored” 警告，通常与程序启动路径或命令行参数包含非 Unicode 兼容字符有关，此故障是由于Bambu Studio 安装路径存在有中文字符导致，可**将Bambu Studio重新安装至全英文路径中解决。**

### 其他故障

如果在安装过程中遇到其他问题，或以上方法无法解决问题，请联系我们获得技术支持。

在反馈故障时，请截图软件故障提示界面，并和其他相关信息一起作为附件发送给我们，以供技术团队进一步的分析排查。

## 首次启动故障

### VCRUNTIME140.dll, MSVCP140.dll 等文件缺失（Windows）

此故障是由于 Visual C++ 运行库安装失败导致的，**重新手动安装  Visual C++ 运行库可以解决问题。**

Visual C++ 运行库安装包位于 Bambu Studio 软件安装路径下 plugin 子目录中。

![](https://wiki.bambulab.com/software/bambu-studio/install-issue/vc_runtime.png)

如果软件安装依旧失败，可能是您的系统环境设置存在冲突；建议您**在全新的、正式版本的 Windows 操作系统环境中安装使用 Bambu Studio 软件。**

同时，建议通过 Microsoft 手册**下载最新 Visual C++ 库。**

> 若出现 “LoadLibrary failed with error 126: The specified module could not be found” 报错，可参照上述方法，手动重新安装 Visual C++ 库、更新显卡驱动程序，重启电脑后即可解决该问题。
>
> ![0em3g000001seno.jpg](https://wiki.bambulab.com/software/0em3g000001seno.jpg)

### 主页或向导对话框空白（Windows）

首次启动 Bambu Studio 软件时，您可能会遇到主页或向导对话框空白的情况。

比如：

![](https://wiki.bambulab.com/software/bambu-studio/install-issue/blank_.jpg)

#### 可能的原因一

该问题可能是 Edge Runtime 安装失败导致的。在 Windows 版本的 Bambu Studio 中，主页和向导对话框使用的是 Windows 原生浏览器组件（即 Edge），而 Edge Runtime 就是支撑这一浏览器组件正常工作的运行库。如果 Edge Runtime 未正确安装，可能会导致 Bambu Studio 的主页或向导对话框无法正常加载或显示为空白页面。

为解决此问题，您可以尝试**手动重新安装 Edge Runtime。**

Edge Runtime 安装包位于 Bambu Studio 软件安装路径下 plugin 子目录中。

![](https://wiki.bambulab.com/software/bambu-studio/install-issue/edge_runtime.png)

如果软件安装依旧失败，可能是您的系统环境设置存在冲突；建议您在全新的、正式版本的 Windows 操作系统环境中安装使用 Bambu Studio 软件。现请您将**杀毒软件、防火墙**关闭，并根据安装过程弹窗提示内容使用以下方法解决。

- 若弹窗提示“此计算机已有更新版本的 Microsoft Edge。如果此软件无法正常运行，请卸载 Microsoft Edge 并重试”、“安装时出现问题。错误代码: ……”等内容，如：

![](https://wiki.bambulab.com/bambu-studio/trouble/20240923-180407.jpg)

![](https://wiki.bambulab.com/bambu-studio/trouble/d30d6a2c-872b-4d5f-aa58-e6222262c09b.png)

建议您在 Windows 设置当中修复 Edge 浏览器。  
![](https://wiki.bambulab.com/bambu-studio/trouble/90026ad1-47f8-4cd3-8564-20bc4aa23cf6.png)

若修复无效，则需要重新下载安装[正式版本的 Edge 浏览器](https://www.microsoft.com/zh-cn/edge/download?form=MA13FJ) 下载安装后会直接将旧版本覆盖。  
![](https://wiki.bambulab.com/bambu-studio/troubleshoot/pixpin_2025-05-23_10-42-51.png)

- 若弹窗提示“检查是否有可用的磁盘空间以及安装软件的权限。无法创建临时目录。”

![](https://wiki.bambulab.com/bambu-studio/trouble/image_(3).png)

请跳转至文件夹 C:\Program Files (x86)\Microsoft，打开文件夹选项，点击查看，找到“隐藏受保护的操作系统文件（推荐）”，将“√”去掉：

![](https://wiki.bambulab.com/bambu-studio/trouble/image_(5).png)

将文件中出现的下图中文件或其他edge相关文件全部删除：

![](https://wiki.bambulab.com/bambu-studio/trouble/01d4127e-d676-44af-a445-75dbc0c690de_(1).png)

删除后重新安装Edge浏览器，即可打开Bambu Studio。

#### 可能的原因二

可能是由于 Chrome 内核与您的 GPU 型号不兼容，导致 Chrome 渲染无法正常工作。您可以尝试按照以下方法解决该问题。

- 打开环境变量设置
- 将环境变量 WEBVIEW2\_ADDITIONAL\_BROWSER\_ARGUMENTS 设置为 --disable-gpu-driver-bug-workarounds --ignore-gpu-blocklist
- 重启 Bambu Studio 软件

![](https://wiki.bambulab.com/software/bambu-studio/install-issue/environment-variables-cn.jpg)

#### 其他可能的原因

为了更好的排查问题，您可以使用 WebView2APISample 工具来测试 Edge runtime 是否正常运行。

WebView2APISample 工具可以从[此处](https://github.com/bambulab/BambuStudio/files/12699287/WebView2APISample.zip)下载，解压后直接运行即可。

1. Edge runtime 异常，建议您尝试重新安装 edge runtime。
2. Edge runtime 运行正常如果下图所示，则建议您更换电脑测试或者联系拓竹技术支持。  
   ![正常.png](https://wiki.bambulab.com/bambu-studio/troubleshoot/%E6%AD%A3%E5%B8%B8.png)

### 其他故障

如果您在软件首次启动时遇到其他故障，或者以上方法无法解决问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。

反馈问题时，请将[软件日志](../../x1/troubleshooting/bambu-studio-log.md)和配置文件打包作为附件发送给我们。
