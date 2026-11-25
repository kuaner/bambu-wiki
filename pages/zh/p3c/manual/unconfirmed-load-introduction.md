---
path: zh/p3c/manual/unconfirmed-load-introduction
title: "P3C 进料待确认状态介绍"
description: ""
tags: []
created: 2026-11-24T14:01:59.438Z
updated: 2026-11-24T14:01:59.438Z
source: https://wiki.bambulab.com/zh/p3c/manual/unconfirmed-load-introduction
---

## 进料待确认状态

由于 P3C 打印头采用特殊结构设计，如果直接将耗材插入打印头，可能出现以下导致进料异常的情况：

1. 耗材从打印头间隙中偏出；
2. 切刀下方残留旧耗材，新耗材虽触发了进料霍尔传感器，但未能被挤出机齿轮成功咬合；
3. 耗材仅触发了进料霍尔传感器，料头未送达齿轮处，导致无法被成功咬合。

## 异常表现

- **屏幕弹框提示**：直接将耗材插入打印头并触发进料传感器时，屏幕会弹出异常进料提示框；

![p3c__________-screenshot_20261112_104632.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/unconfirmed-load-introduction/zh/p3c__________-screenshot_20261112_104632.png)

- **耗材页"问号"标识**：耗材页面对应的打印头位置会显示“问号”标识，点击后可查看相关提示信息；

![p3c__________-image-6.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/unconfirmed-load-introduction/zh/p3c__________-image-6.png)

- **打印前提示**：发起打印时，若选中对应耗材，机器会提示耗材可能未正常插入。此提示不会阻塞打印，如您确认耗材已完全进入打印头热端内部，可正常启动打印。打印过程中，机器挤出耗材时若检测到进料状态正常，耗材页的异常标识会自动消失。

![p3c__________-image-5.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/unconfirmed-load-introduction/zh/p3c__________-image-5.png)

## 解决方法

为避免直接插入耗材导致进料异常，建议通过**屏幕的进料按钮**走标准进料流程。该流程下，机器会在工具头夹持打印头后再提示插入耗材，从而有效约束进料路径，确保耗材顺利进入打印头热端内部。

进料流程入口包括以下三个：

- **AMS 槽位内耗材进料：**

![p3c__________-image-3.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/unconfirmed-load-introduction/zh/p3c__________-image-3.png)

- **AMS 槽位内耗材批量进料：**

![p3c__________-image-4.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/unconfirmed-load-introduction/zh/p3c__________-image-4.png)

- **外挂进料：**

![p3c__________-image-2.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/unconfirmed-load-introduction/zh/p3c__________-image-2.png)

通过正常流程完成进料后，打印头内耗材状态如下图所示，可确保工具头夹持打印头后咬合轮能正常咬住耗材。

![p3c__________-screenshot_20261112_104634.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/unconfirmed-load-introduction/zh/p3c__________-screenshot_20261112_104634.png)

## 补充说明

- 推荐使用耗材页的“**AMS 进料**”功能，可快捷完成多槽批量进料；

|  |  |
| --- | --- |
| p3c__________-image.png | p3c__________-screenshot_20261112_104220.png |

- 当机器检测到进料异常时，若已确认耗材成功进入打印头热端且耗材类型正确，机器仅会给出温馨提示，不会阻止打印；
- **AMS 3P 在线时，请勿将外挂耗材直接插入打印头**，以免打印机误识别为 AMS 3P 槽内耗材；此时请通过屏幕 \*\*“外挂进料”\*\*入口进料。

![p3c__________-image-1.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/unconfirmed-load-introduction/zh/p3c__________-image-1.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
