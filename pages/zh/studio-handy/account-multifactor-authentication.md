---
path: zh/studio-handy/account-multifactor-authentication
title: "Bambu 账号安全认证功能"
description: "本文介绍了如何进行 Bambu Handy 安全认证"
tags: ["bambu handy"]
created: 2024-11-07T08:52:46.912Z
updated: 2024-11-07T08:52:48.138Z
source: https://wiki.bambulab.com/zh/studio-handy/account-multifactor-authentication
---

## 背景介绍

Bambu Lab 非常注重用户数据的安全保护，在特定条件下引入了新的验证机制。提供了强大的、分层的方法来保护用户数据和 APP 应用免受安全威胁。在这篇文章中，我们将详细介绍 Bambu 账号的安全认证功能。

## 验证机制

最近，在原有的安全功能基础上，我们引入了一项新的验证机制，以更好地保护您的账户。

### 触发条件

登录时需要同时满足以下 2 个条件，才会进行这项额外的验证。

1. 在新设备上首次登录账号；
2. 使用账号密码登录（非第三方登录方式）

### 触发流程

#### 从Bambu Handy登录

如果 Bambu Handy 没有更新到 V2.15.5，又满足了上述2个条件，Bambu Handy 会出现以下提示信息。请将 Bambu Handy 更新到 V2.15.5 或更高版本后重新登录，否则将无法在 Bambu Handy 上输入验证码从而导致无法完成登录。

![触发验证.jpg](https://wiki.bambulab.com/bambu-handy/mfa/cn-mfa/%E8%A7%A6%E5%8F%91%E9%AA%8C%E8%AF%81.jpg)

当 Bambu Handy 已经更新至 V2.15.5 或更高版本之后，在满足上述 2 个条件的情况下，通过账号密码登录时我们会向你的手机号发送一个 6 位验证码。在短信中找到验证码，输入后才可以登录账号。

![触发验证2.png](https://wiki.bambulab.com/bambu-handy/mfa/cn-mfa/%E8%A7%A6%E5%8F%91%E9%AA%8C%E8%AF%812.png)![触发验证3.jpg](https://wiki.bambulab.com/bambu-handy/mfa/cn-mfa/%E8%A7%A6%E5%8F%91%E9%AA%8C%E8%AF%813.jpg)

#### 从Bambu Studio或者网页登录

同样满足上述 2 个条件的情况下，从 Bambu Studio 或者网页端登录 Bambu 账户也需要经过相同的验证过程。在手机短信中找到验证码并输入，即可完成登录。

![登录验证1-cn.jpg](https://wiki.bambulab.com/bambu-handy/mfa/cn-mfa/%E7%99%BB%E5%BD%95%E9%AA%8C%E8%AF%811-cn.jpg)  
![登录验证2-cn.jpg](https://wiki.bambulab.com/bambu-handy/mfa/cn-mfa/%E7%99%BB%E5%BD%95%E9%AA%8C%E8%AF%812-cn.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)
