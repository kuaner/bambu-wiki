---
path: zh/makerworld/cyberbrick/ai-advanced-programming
title: "高级编程与AI "
description: ""
tags: ["cyberbrick"]
created: 2025-06-10T02:43:45.799Z
updated: 2025-10-28T08:56:39.409Z
source: https://wiki.bambulab.com/zh/makerworld/cyberbrick/ai-advanced-programming
---

## CyberBrick 代码库

CyberBrick 官方代码库可以[在此访问](https://github.com/CyberBrick-Official)。

## API文档

[API文档链接](https://makerworld.com/en/cyberbrick/api-doc/)。

## 如何上传CyberBrick的自定义项目，帮助我实现丰富多样的功能？

在新版 CyberBrick 中，除了可以使用官方提供的 **无线遥控（RC）项目** 外，您还可以上传**自定义项目，**来实现您的创意。

自定义项目基于 [**MicroPython**](https://docs.micropython.org/en/latest/) 编写，能够实现更高的自由度和个性化玩法，让您开发出丰富多样的功能。

![group_68_(1).png](https://wiki.bambulab.com/cyberbrick/troubleshooting/forget-the-pin-code/group_68_(1).png)

### **如何上传自定义项目**

若您希望将自己的项目在 **CyberBrick 社区** 中分享，可通过 [**MakerWorld 网页**](https://makerworld.com.cn/zh/my/models/publish?type=original) 上传自定义项目的 **配置文件** 或 **项目源码**。

### 上传 MPY 项目源码时，请注意以下事项：

- 压缩包根目录必须包含 **`boot.py`** 文件（详见下方 ***自定义项目构成说明***）。
- 解压后的所有源码文件总大小 **不超过 800 kB**。
- 上传到 MakerWorld 平台后，系统会再次压缩源码：

  - 压缩后的体积需 **不超过 250 kB**。
  - 若出现报错提示，请适当减少源码文件体积。

### 自定义项目构成说明

自定义项目构成需符合以下条件，且其运行方式如下。

- 自定义项目必须包含文件`boot.py`.
- `boot.py` 必须位于项目文件夹的根目录。
- 核心板上电后将自动执行 `boot.py`，执行结束后程序停止运行，直至再次复位。因此，`boot.py` 实现了本项目的核心功能。

![图为无线遥控（RC）项目示例](https://wiki.bambulab.com/cyberbrick/troubleshooting/forget-the-pin-code/img_v3_02ot_673e2833-a73e-40cb-84fe-ebbe800b097g.jpg)

**自定义项目非必须的文件包含：**

- **`.ignore` 文件**
- rc\_config
- log/

![](https://wiki.bambulab.com/cyberbrick/troubleshooting/forget-the-pin-code/img_v3_02ot_b4958bad-f45c-4494-bb86-268be7e9d67g.jpg)

- 声明哪些文件/目录属于临时文件，不纳入项目内容比对。
- 用法类似 Git 仓库中的 `.ignore` 文件，但仅支持 2 条语法：

  - 只允许匹配具体文件/文件夹路径。
  - 不支持通配符等复杂匹配。
- 典型场景：运行日志、用户生成的个性化配置文件等。

**其他 `.py` 或 `.mpy` 文件**

- 可被 `boot.py` 调用，扩展功能实现。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
