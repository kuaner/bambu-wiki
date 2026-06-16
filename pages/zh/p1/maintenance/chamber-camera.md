---
path: zh/p1/maintenance/chamber-camera
title: "更换摄像头和 LED 补光灯"
description: "本文介绍了如何更换 P1 系列摄像头和 LED 补光灯"
tags: ["p1"]
created: 2022-12-05T10:37:22.263Z
updated: 2026-06-08T02:00:38.385Z
source: https://wiki.bambulab.com/zh/p1/maintenance/chamber-camera
---

> **隐私提示**：请确保摄像头已正确安装，使摄像头视野正确朝向打印机腔体，以避免对打印区域或喷嘴的检测出现问题。

## 机箱摄像头和 LED 补光灯

![](https://wiki.bambulab.com/p1/maintenance/chamber-camera/camera-led.png)

## 工具

- H2.0 内六角扳手
- 镊子
- 3M 胶

## 准备工作

- 关闭电源，打开前玻璃门，取下玻璃上盖。
- 移除 microSD 卡。

## 更换摄像头

### 拆除指南

#### **第 1 步 -**  拆除左侧板

请参考 [更换 P1 系列塑胶左侧板](p1s-left-panel.md) 的相关指引，移除左侧板。

#### **第 2 步 - 断开摄像头线缆**

撕下 AP 板保护泡棉，断开摄像头线缆接口。

|  |  |
| --- | --- |
|  |  |

#### **第 3 步 - 移除摄像头**

向右推动摄像头，即可将其拆下。

![p1_camera_removing.png](https://wiki.bambulab.com/p1/maintenance/chamber-camera/p1_camera_removing.png)

### 安装指南

#### **第1步 -** 安装摄像头

将摄像头对齐横梁上的安装口，将摄像头推到位。

|  |  |
| --- | --- |
|  |  |

#### **第 2 步 - 移除保护纸**

去除摄像头软排线上的保护纸。

![](https://wiki.bambulab.com/p1/maintenance/chamber-camera/remove_the_protective_paper.jpg)

#### **第 3 步 -** 贴附软排线

#### 沿着立柱将软排线贴附好，并将带标线的部分排线塞进前面盖和横梁的间隙处。

|  |  |
| --- | --- |
|  |  |

#### **第 4 步 -** 连接摄像头排线

将摄像头排线连接到AP板对应接口上，整理好软排线。

![](https://wiki.bambulab.com/p1/maintenance/chamber-camera/connect_fpc_2.jpg)

#### **第 5 步 -** 安装 AP 板保护泡棉

将保护泡棉贴回到 AP 板表面。

|  |  |
| --- | --- |
|  |  |

#### **第 6 步 -** 安装左侧板

请参考 [更换 P1 系列塑胶左侧板](p1s-left-panel.md) 的相关指引，安装左侧板。

### 如何验证完成

启动打印机，确认屏幕能正常显示，屏幕主页上有摄像头图标，说明安装成功。

![](https://wiki.bambulab.com/p1/maintenance/chamber-camera/camera_label.jpg)

## 更换 LED  补光灯 5V 0.3A

### 拆卸指南

#### **第 1 步 - 断开线缆**

撕下 AP 板保护泡棉，断开 LED 线缆。

|  |  |
| --- | --- |
|  |  |

#### **第 2 步 - 推出 LED** 补光灯

将 LED 补光灯朝背板方向推出，请小心检查是否会被摄像头卡住。如需要更换 LED 线缆，则可以剪断旧的 LED 线缆。

![](https://wiki.bambulab.com/p1/maintenance/chamber-camera/%E6%8B%86%E4%B8%8Bled%E7%81%AF%E5%B8%A6.jpg)

#### **第 3 步 - 拆除**卡扣

翻转 LED 补光灯，用刮刀刮除卡扣。

![](https://wiki.bambulab.com/p1/maintenance/chamber-camera/%E5%88%AE%E5%88%80%E5%88%AE%E9%99%A4.jpg)

#### **第 4 步 - 拆除灯条**

用螺丝刀小心撬开 LED 补光灯后盖，拆下 LED 灯条。

|  |  |
| --- | --- |
|  |  |

### 安装指南

#### **第 1 步 - 安装灯条**

将新的灯条安装到 LED 补光灯上，连接线缆，并将线缆排进线槽中（一些批次没有线槽）。

![](https://wiki.bambulab.com/p1/maintenance/chamber-camera/%E6%8E%92%E7%BA%BF-.jpg)

#### **第 2 步 - 安装 LED** 补光灯

使用 3M 胶将 LED 补光灯粘到打印机上。

|  |  |  |
| --- | --- | --- |
|  |  |  |

#### **第 3 步 - 连接线缆**

将 LED 线缆连接至 AP 板，并将线缆整理好。

|  |  |
| --- | --- |
|  |  |

#### **第 4 步 -** 安装泡棉

重新安装泡棉。

![](https://wiki.bambulab.com/p1/maintenance/chamber-camera/%E8%A3%85%E5%9B%9E%E6%B3%A1%E6%A3%89.png)

### 如何验证完成

连接电源，在打印机屏幕的控制菜单中选择灯泡图标，选择 **打开/Turn on LED**；如果机箱内 LED 补光灯亮，则说明安装成功。

![](https://wiki.bambulab.com/p1/manual/upgrade-list/led_on_p1p.png)

Bambu Studio: 点击设备 > 设备状态 > 灯泡图标，如果显示绿色，则为打开状态。

Bambu Handy APP: 点击打印机按钮 > 底部灯泡图标，如果显示绿色，则为打开状态。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
