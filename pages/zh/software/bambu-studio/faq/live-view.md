---
path: zh/software/bambu-studio/faq/live-view
title: "加载视频流失败排查"
description: ""
tags: []
created: 2023-03-14T13:56:22.942Z
updated: 2026-05-08T12:05:26.859Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/faq/live-view
---

下面列出了您在使用Studio播放视频时可能遇到的问题，找到遇到的问题，并尝试按照说明进行解决。

## 问题1-初始化失败(XXX)！

![video_init_fialed.png](https://wiki.bambulab.com/software/bambu-studio/live-view/video_init_failed.png)

无法从Bambu服务器搜索打印机的视频通道。以下问题将导致此问题：

您没有选择任何打印机。(无设备)

您的打印机没有相机设备。(无相机设备)

您的打印机处于仅局域网模式。(不支持仅局域网模式)

服务器不可用或处于错误状态。在寻求售后帮助之前，请检查网络连接。(网络不可达)

您的打印机仅支持Lan直连，但Bambu Studio无法找到打印机的Lan IP。请关闭计算机的网络防火墙，并重新启动Bambu Studio以重试。(缺少打印机的LAN IP)

您已从打印机注销，Bambu Studio已经失去了这些信息。在尝试启动实时查看时，服务器报告错误。

您的打印机处于仅局域网模式，Bambu Studio已经失去了这些信息。

## 问题2-此任务需要Windows Media Player！(仅适用于Windows)

在Windows系统上，我们使用Windows Media Player播放从打印机的视频流。如果它在您的PC系统上不可用，则在启动实时查看时会弹出错误对话框。

![video_wmp.png](https://wiki.bambulab.com/software/bambu-studio/live-view/video_wmp.png)

在此对话框上单击“确定”，它将带您进入“Windows可选功能”，您可以在那里搜索并安装Windows Media Player。

![install_wmp.png](https://wiki.bambulab.com/software/bambu-studio/live-view/install_wmp.png)

安装 Windows Media Player 后，请重新启动 BambuStudio。   
如果已经安装了Windows Media Player，但此错误仍然存在，则可能有一些Windows更新阻止了Windows Media Player的功能。请安装Windows更新并重新启动计算机，然后再次运行 BambuStudio。

如果使用上述方法安装失败，您也可以尝试安装Windows Media Player离线包。

- [点击此处](https://wiki.bambulab.com/software/bambu-studio/live-view/microsoft-windows-mediaplayer-package-31bf3856ad364e35-amd64.zip)下载文件。
- 解压到C盘:\
- 在 Powershell 中运行命令行来安装它

`Dism.exe /Online /Add-Package /PackagePath:C:\Microsoft-Windows-MediaPlayer-Package~31bf3856ad364e35~amd64~~.cab`

## 问题 3 - BambuSource 未正确注册媒体播放！（仅适用于 Windows）

![来源注册.png](https://wiki.bambulab.com/software/bambu-studio/live-view/bambu_sourece_register.png)
![来源注册2.png](https://wiki.bambulab.com/software/bambu-studio/live-view/bambu_sourece_register2.png)

为了实现与 Windows Media Player 的兼容，我们在网络插件包中包含了一个名为“BambuSource”的 DirectShow 插件。

BambuSource 必须注册才能正常运行。该插件可能由于以下问题而无法正常工作：

- 注册失败   
  过于敏感的杀毒软件干扰
- 注册位置不正确  
  在与正在使用的 Windows 用户帐户不同的帐户下注册

该怎么办？

- 根据提示重新注册 BambuSource。
- 如果注册再次失败，请考虑手动导入 regedit 项目。
- a. 下载下面的文件“bambusource.reg”。
- b. 打开文件并将“Administrator”替换为您的 Windows 帐户名。保存文件。
- c. 双击该文件，将其合并到系统注册表中。

[bambusource.reg](https://wiki.bambulab.com/software/bambu-studio/live-view/bambusource.reg)

[bambu.reg](https://wiki.bambulab.com/software/bambu-studio/live-view/bambu.reg)

## 问题4-缺少为媒体播放注册的BambuSource组件！(仅适用于Windows)

为了与Windows Media Player配合使用，我们在网络插件包中提供了一个名为“BambuSource”的DirectShow组件。当无法加载BambuSource时，将弹出错误对话框。

![video_dll.png](https://wiki.bambulab.com/software/bambu-studio/live-view/video_dll.png)

BambuSource需要注册才能工作。以下问题将导致其无法工作：

- 注册失败
- 有时被过于敏感的防病毒软件阻止
- 被自己或其他软件删除
- 经常被防病毒软件隔离
- 在错误的位置注册
- 为另一个Windows用户帐户注册，而不是使用的帐户

要检查发生了什么，请执行以下步骤：

1. 检查注册表  
打开PowerShell或cmd.exe并执行以下脚本：

*REG QUERY HKEY\_CLASSES\_ROOT\bambu*

*REG QUERY "HKEY\_CLASSES\_ROOT\CLSID\{233E64FB-2041-4A6C-AFAB-FF9BCF83E7AA}\InProcServer32"*

正常输出将是：

*HKEY\_CLASSES\_ROOT\CLSID\ {233E64FB-2041-4A6C-AFAB-FF9BCF83E7AA}\InProcServer32*  
*(Default)  REG\_SZ C:\Users\AppData\Roaming\BambuStudio\plugins\BambuSource.dll*  
*ThreadingModel REG\_SZ Both*

*HKEY\_CLASSES\_ROOT\bambu*  
*Source Filter REG\_SZ {233E64FB-2041-4A6C-AFAB-FF9BCF83E7AA}*

2. 检查BambuSource.dll是否已安装  
在文件夹C:\Users\AppData\Roaming\BambuStudio\plugins中查找BambuSource.dll。  
错误对话框也会检查这些并显示要做什么，只需重新安装Bambu Studio即可解决该问题。  
重新安装时，请注意防病毒软件的警告，并手动忽略这些警告。

## 问题5-加载失败[###]！

![video_load_failed.png](https://wiki.bambulab.com/software/bambu-studio/live-view/video_load_failed.png)

无法从打印机加载视频流。这可能是打印机设备端的问题，也可能是Windows Media Player的问题。  
在打印机端，原因可能有：

- 打印机实际上没有上线，无法提供视频流。
- 打印机处于仅限局域网模式，未连接到网络。
- 打印机已超过服务容量限制。

在播放器端可能会有以下问题：

- Windows Media Player未安装。
- Windows Media Player已损坏，需要重新安装。
- 未注册用于媒体播放的BambuSource组件。

## 问题6 - 加载视频流时程序卡住了！（仅适用于Windows系统）

![video_hung.png](https://wiki.bambulab.com/software/bambu-studio/live-view/video_hung.png)

Windows Media Player使用d3d9驱动程序进行媒体渲染。  
D3d9在一些双显卡系统上存在问题。  
更换另一个显卡可能会解决此问题。您可以通过在Nvidia配置面板中配置Bambu Studio使用的显卡来实现此目的：[用Bambu Studio观看在线视频时软件崩溃 | Bambu Lab Wiki](../../../x1/troubleshooting/bambu-studio-crashes-when-watching-online-video.md)

## 附录:错误码

- 检查播放器 (仅适用于Windows系统)

| **错误码** | **问题** | **解决方案** |
| --- | --- | --- |
| 100 | 未安装 Windows Media Player | 根据提示在 "Windows 可选功能 "中安装 Windows Media Player。 |
| 101 | BambuSource 尚未注册 | 根据提示重新注册，如果再次注册失败，建议手动导入regedit项目 |
| 102 | BambuSource 尚未注册 | 根据提示重新注册，如果再次注册失败，建议手动导入regedit项目 |
| 103 | 播放插件缺失或位置不一致（可能是因为安装了多个Studio版本，插件位于不同的目录中）。 | 按照提示重新注册 BambuSource 或重新安装 Bambu Studio。 |

- 通过 P2P连接（远程）

| **错误码** | **问题** | **解决方案** |
| --- | --- | --- |
| -90 | 打印机并不在线 | 请尝试重新启动打印机。检查打印机的连接性并重试。 |
| -48 | 印机已超出服务容量限制 | 检查打印机的视频连接是否过多 |
| -10 | 证书错误 | 检查您是否正在使用 Bambu Studio官方版本 |
| -68 | 密码错误 | 检查您是否正在使用 Bambu Studio官方版本 |
| -13 | 连接超时 | 检查网络，重启设备，然后稍后重试 |

- 通过LAN连接(仅适用于Windows系统)

| **错误码** | **问题** | **解决方案** |
| --- | --- | --- |
| -10051 | 您的 LAN 网络出现问题 (*尝试对无法访问的网络*执行*套接字操作。*) | 在寻找售后帮助之前，请先检查网络连接情况 |
| -10060 | 您的 LAN 网络出现问题 (*由于连接方在一段时间后没有正确*答复*或连接的主机没有*反应，*连接尝试失败*) | 在寻找售后帮助之前，请先检查网络连接情况 |
| -10061 | 您的 LAN 网络出现问题 (无法建立*连接*，*因为目标计算机主动拒绝*了它。) | 在寻找售后帮助之前，请先检查网络连接情况 |

- 通过LAN连接(适用于Unix系统(MacOS, Linux))

| **错误码** | **问题** | **解决方案** |
| --- | --- | --- |
| -110 | LAN 网络出现问题 | 在寻找售后帮助之前，请先检查网络连接情况 |
| -111 | LAN 网络出现问题 | 在寻找售后帮助之前，请先检查网络连接情况 |
| -112 | LAN 网络出现问题 | 在寻找售后帮助之前，请先检查网络连接情况 |

- 常见的视频加载问题

| **错误码** | **问题** | **解决方案** |
| --- | --- | --- |
| -1 | 您的网络有问题 | 检查网络，重启设备，然后稍后重试 |
| -4 | 连接成功，但数据超时 | 检查网络，重启设备，然后稍后重试 |
| 1 | 使用远程访问的studio/handy设备超限 | 关闭一些并重试 |
| 2 | Windows Media Player 出现问题 | 重新安装 Windows Media Player 并重试 |
| 3 | 连接失败 | 请检查网络并重试 |

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
