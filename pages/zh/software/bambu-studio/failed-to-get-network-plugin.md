---
path: zh/software/bambu-studio/failed-to-get-network-plugin
title: "无法获取网络插件"
description: "Bambu Studio 报无法获取网络插件可能得原因与解决方法"
tags: ["bambu studio", "studio"]
created: 2023-08-03T06:42:59.101Z
updated: 2026-01-08T06:58:32.834Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/failed-to-get-network-plugin
---

# 无法获取网络插件

## Windows

`1. 请确认其他的 Bambu Studio 窗口已经关闭`

`2. 检查是否能访问插件服务器`  
使用浏览器打开以下链接，检测是否能访问插件服务器:  
<https://public-cdn.bambulab.cn/upgrade/studio/plugins/01.07.01.04/win_01.07.01.04.zip>

如果你能看到一个zip压缩包正在打开，说明可以访问。  
如果提示找不到网页，可能无法访问，请检查你的网络连接。

`3. 请确认其他的程序没有占用网络插件`  
关闭Bambu Studio，打开文件夹 `C:\Users\your_user_name\AppData\Roaming\BambuStudio`, 删除里面的 `plugins` 文件夹。

- 如果成功删除，则重新打开Bambu Studio，它会自动重试安装插件;
- 如果失败，请检查无法删除文件夹的原因，查看是什么程序占用了此文件，关闭相关的程序后重试。通常重启电脑后可以被删除。文件夹被删除后，可重新打开Bambu Studio 重试安装插件。

已知会占用网络插件的应用:

- **Microsoft Teams**
- **Microsoft Agent**
- **Skype**
- **Nvidia Broadcast**

`4. 确保你的杀毒软件没有阻止网络插件的下载`  
如果尝试了以上步骤，依旧无法成功安装网络插件，请检查你的杀毒软件是否阻挡或删除了网络插件。如果是，请将网络插件加入杀毒软件的白名单。

`5. 如果仍然失败，可以尝试手动安装网络插件`

使用Bambu Studio 的版本号替换这个网址内的 AA BB CC `https://api.bambulab.cn/v1/iot-service/api/slicer/resource?slicer/plugins/cloud=AA.BB.CC.00`

> 其中AA.BB.CC对应当前您Bambu Studio的版本号的前三位，例如，Bambu Studio版本号是 01.07.03.50, 则 AA.BB.CC对应 01.07.03，修改后的网址是： <https://api.bambulab.cn/v1/iot-service/api/slicer/resource?slicer/plugins/cloud=01.07.03.00> （示例）

替换完成后，粘贴到浏览器的地址栏，直接使用浏览器访问这个网址。  
浏览器会返回如下json字符串。（请根据实际返回结果操作，不要直接使用以下字符串和地址）

```
 {"message":"success","code":null,"error":null,"software":{"type":null,"version":"01.07.03.50","description":"###https://wiki.bambulab.com/en/software/bambu-studio/release/release-note-1-7-3###","url":"https://public-cdn.bambulab.cn/upgrade/studio/software/01.07.03.50/Bambu_Studio_win-v01.07.03.50.exe","force_update":false},"guide":null,"resources":[{"type":"slicer/plugins/cloud","version":"01.07.03.02","description":"","url":"https://public-cdn.bambulab.cn/upgrade/studio/plugins/01.07.03.02/win_01.07.03.02.zip","force_update":false}]}
```

在json字符串中找到类型为"slicer/plugins/cloud"的资源，找出它对应的url (.zip 结尾的网址)，例如 `https://public-cdn.bambulab.cn/upgrade/studio/plugins/01.07.03.02/win_01.07.03.02.zip`

将url复制到浏览器地址栏，并访问即可下载正确的网络插件。

最后，将zip包解压缩到 `C:\Users\your_user_name\AppData\Roaming\BambuStudio\plugins` 目录并重启 Bambu Studio 即可完成安装。

## Macos

通常原因是网络问题，有一些VPN服务会阻止 Bambu Studio 下载网络插件。

- **Cisco AnyConnect**
- **iCloud Private Relay**
- **AVG Security**

`禁用Cisco AnyConnect的步骤:`  
使用下列命令停止 "Cisco Anyconnect Socket Filter"

1. /Applications/Cisco/Cisco\AnyConnect\Socket\Filter.app/Contents/MacOS/Cisco\ AnyConnect\Socket\Filter -deactivateExt
2. 禁用 "Cisco Anyconnect Socket Filter"， 在"System Preferences"的 Network page
3. 卸载 "Cisco Anyconnect Socket Filter"
4. 当安装 Cisco AnyConnect时, 尝试只安装"VPN"相关的组件。

![](https://wiki.bambulab.com/software/bambu-studio/bambu-studio-common/wiki-printer-failed-17.png)

`禁用AVG Security的步骤:`

1. 在系统设置的网络页面禁用 AVG Security.

![](https://wiki.bambulab.com/software/bambu-studio/bambu-studio-common/wiki-printer-failed-16.png)

# 结束语

**获取、使用网络插件即视为您同意与接受Studio的**[**用户条款**](https://bambulab.cn/zh-cn/policies/terms)**。否则，请勿下载、使用本插件及任何相关功能。**

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
