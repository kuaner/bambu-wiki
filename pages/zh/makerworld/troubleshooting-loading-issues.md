---
path: zh/makerworld/troubleshooting-loading-issues
title: "MakerWorld 加载异常排查"
description: "本文介绍了提交服务工单，协助排查无法打开 MakerWorld 网页、加载缓慢或网页上部分资源无法加载的步骤。"
tags: []
created: 2025-02-28T10:35:58.128Z
updated: 2026-01-16T02:39:48.664Z
source: https://wiki.bambulab.com/zh/makerworld/troubleshooting-loading-issues
---

## MakerWorld 加载异常

### 网页加载异常

屏幕出现**无法打开网页**、**网页加载缓慢**、网页上的**图片无法正常显示**等问题。

#### 切换网络

如果电脑连接 Wi-Fi 时出现加载缓慢的问题，请尝试用手机通过 5G 访问。

#### 更换浏览器

请确认当前使用的浏览器类型（优先推荐使用 Chrome 浏览器），以及是否开启 VPN 等代理软件；

- 若未使用 Chrome 浏览器，建议切换至 Chrome 浏览器后重试操作；
- 若使用 Chrome 浏览器问题仍存在，可尝试开启浏览器无痕 / 隐身模式访问；

还可以尝试关闭所有翻译工具及插件后进行重试。

#### 提交工单

如果以上方法均未解决问题，请将以下**信息**、**截图**以及导出的 **HAR 文件**添加在[MakerWorld 服务工单](tutorials/create_tickets.md)问题描述和附件中，说明您遇到的问题，相关支持人员会尽快查看。

> 请点击[这里](tutorials/create_tickets.md)查看创建 MakerWorld 服务工单的指引。

###### 浏览器相关信息

- 平台运行环境信息及 Chrome 浏览器版本号
- 具体操作步骤
- console.log 日志和 network 网络请求日志

##### 提供地区、运营商、IP 地址信息

- 提供您的所在地。
- 提供您的网络运营商。
- 访问 <https://ip111.cn/> 查询 IP 地址并提供。

##### 访问以下地址并提供截图

请根据实际情况尝试访问如下地址，获取相关信息，并在服务工单中提供对应访问页面的截图。

- 如无法打开 [bambulab.com](https://bambulab.com/en)，请访问 [bambulab.com/cdn-cgi/trace](https://bambulab.com/cdn-cgi/trace) 并截图。
- 如无法打开 [makerworld.com.cn](https://makerworld.com.cn/zh)，请访问 [makerworld.com.cn/cdn-cgi/trace](https://makerworld.com.cn/cdn-cgi/trace) 并截图。
- 如无法打开 [makerworld.com](https://makerworld.com/zh)，请访问 [makerworld.com/cdn-cgi/trace](https://makerworld.com/cdn-cgi/trace) 并截图。
- 如果 [makerworld.com](https://makerworld.com/zh) 上的图片无法加载，请访问 [makerworld.bblmw.com/cdn-cgi/trace](https://makerworld.bblmw.com/cdn-cgi/trace) 并截图。

> 如果您的所在地为中国大陆地区，访问 [makerworld.com](http://makerworld.com) 时出现网页无法打开、页面上的图片无法正常加载等问题，建议您访问 MakerWorld 中国站（[makerworld.com.cn](https://makerworld.com.cn/zh)）。

##### 提供 HAR 文件

在**浏览器开发者模式**下，导出 **HAR 文件**，并服务工单中附上 HAR 文件。

- 查看浏览器工具栏，点击“**更多工具**” → “**开发者工具**”，打开浏览器开发者模式。

![developertools.jpg](https://wiki.bambulab.com/makerworld/troubleshooting-loading-issues/developertools.jpg)

- 点击“**网络/Network**”，并刷新网页，尝试加载。

![network.jpg](https://wiki.bambulab.com/makerworld/troubleshooting-loading-issues/network.jpg)

- 在该页面右键单击，选择 **Copy** → **Copy all as HAR**，将拷贝的内容保存为文件。

![copyallashar.jpg](https://wiki.bambulab.com/makerworld/troubleshooting-loading-issues/copyallashar.jpg)

### 访问被阻止

如果出现 “**抱歉，您已被屏蔽/ Sorry, you have been blocked**” 页面，请[提交 MakerWorld 服务工单](tutorials/create_tickets.md)并在工单中提供该页面底部的 **Ray ID** 以及访问的 **IP 地址**。

![blocked.jpg](https://wiki.bambulab.com/makerworld/troubleshooting-loading-issues/blocked.jpg)

## MakerLab 加载异常

1. 确认当前使用的浏览器是否为 Chrome。若非 Chrome 浏览器，请先切换至 Chrome 浏览器测试问题是否复现。
2. 若在 Chrome 浏览器中问题依旧，需收集以下信息：

- 设备平台信息（如 Windows/macOS 版本）
- Chrome 浏览器版本号
- 触发问题的详细操作步骤
- console.log 日志及 network 网络请求信息

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
