---
path: zh/software/bambu-studio/how-to-change-dns
title: "如何修改 DNS 服务器地址"
description: "该指南介绍了从路由器端及电脑端修改 DNS 服务器地址的方法。"
tags: []
created: 2026-10-09T08:15:01.098Z
updated: 2026-10-09T10:15:15.485Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/how-to-change-dns
---

## 适用范围

打印机网络出现异常，如打印机离线、无法连接云服务器等现象时，可以尝试修改路由器 DNS 解决。下面介绍从路由器端及电脑端修改 DNS 服务器地址的方法。

## 在路由器端修改 DNS 设置

通常电脑的 IP 和 DNS 是由路由器分配的（除非电脑设置了静态 IP/DNS），那么修改路由器上的 DNS 设置，可以实现连接此路由器的所有设备都使用修改后的 DNS。  
不同路由器的界面和设置步骤略有差异，本文以一台特定的路由器设置为例。

1. 登录路由器管理页面  
   可以在路由器的底部标贴上查看路由器出厂的无线信号名称以及管理地址。  
   ![internet_dns7.jpg](https://wiki.bambulab.com/bambu-studio/how-to-change-dns/internet_dns7.jpg)  
   使用手机或电脑连接路由器的无线 WiFi 之后，在浏览器中输入管理地址。输入路由器的管理员密码后，即可登录路由器管理页面。  
   ![internet_dns8.png](https://wiki.bambulab.com/bambu-studio/how-to-change-dns/internet_dns8.png)
2. 修改 DNS 设置  
   在 **DHCP 服务器设置**中可以填写 **DNS 服务器**。推荐首选 DNS 服务器设置为 **223.5.5.5** ，备用 DNS 服务器设置为 **114.114.114.114** 。  
   ![internet_dns6.png](https://wiki.bambulab.com/bambu-studio/how-to-change-dns/internet_dns6.jpg)

## 在电脑端修改 DNS 设置

1. 右键电脑右下角的网络图标，打开网络和 Internet 设置。  
   ![internet_dns.png](https://wiki.bambulab.com/bambu-studio/how-to-change-dns/internet_dns1.png)
2. 在高级网络设置中，点击 **“更改适配器选项”**。  
   ![internet_dns.png](https://wiki.bambulab.com/bambu-studio/how-to-change-dns/internet_dns2.png)
3. 找到需要修改 DNS 的网络适配器（如果是无线网络，会有 WLAN 网络适配器），右键点击选择属性。  
   ![internet_dns.png](https://wiki.bambulab.com/bambu-studio/how-to-change-dns/internet_dns3.png)
4. 选择 **“网络”** 选项卡，双击 Internet 协议版本 4（TCP/IPv4）  
   ![internet_dns.png](https://wiki.bambulab.com/bambu-studio/how-to-change-dns/internet_dns4.png)
5. 默认情况下，电脑的 IP 和 DNS 都是自动获取的。选择 **“使用下面的 DNS 服务器地址”**，即可手动填写电脑的 DNS 服务器。推荐设置为以下地址，或者自行查询并使用其他公用的 DNS 服务器。

- **首选 DNS**：223.5.5.5
- **备用 DNS**：114.114.114.114  
  ![internet_dns.png](https://wiki.bambulab.com/bambu-studio/how-to-change-dns/internet_dnsg.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
