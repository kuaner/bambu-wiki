---
path: zh/p1/maintenance/screen-connector-cable
title: "更换屏幕排线 - P1"
description: "本文介绍了如何更换 P1 系列屏幕排线"
tags: ["p1"]
created: 2024-12-05T06:32:18.159Z
updated: 2026-02-24T06:20:31.087Z
source: https://wiki.bambulab.com/zh/p1/maintenance/screen-connector-cable
---

## 屏幕排线

![](https://wiki.bambulab.com/p1/p1-screen-cable.png)

购买链接：[天猫](https://detail.tmall.com/item.htm?abbucket=7&id=696532042331&pisk=fUX-LP9kyr4kj0mxMXND-vvKz5q0o9IzraSsKeYoOZQAJwduY3bHpBLAfQqP-wfvJZ_vPwIU4HTCRwLhZS2G4gJedPvLIRjP8y58bwdWNEsf0hMIRIFJyXvedP4KivOzBp7w4a16RjtXuHKIde_BGjtBl3tSFwTXGhtIFp_BdopXvHuIPYtIGntHlXiWA3TXGH-6AYTWNoIXuHGUIyLjVeDdtbtrxbcyJvMCFJRJW9lnpvCJVQBCVEIcmtKJwFOmIF21FZjCETR4wb9Fm1QdONamZU19XZdGwPHRWa-CvH_8QcLfeMBvas0SNhpJyC6WwcqNmB1AHLX78fScDUO9nsV4rBvRy18wNSzVJiLlRTdjyrYhsiXWMNamHwRdOTvfFrwO4OWGBcVESFKnNoExTXRW0_-kBwKwAsMDDFq8pXlego-vSoEmTXRvcnLg2ulETIWO.&rn=1352d3dacd9891c12bd8852707364cb2&spm=a1z10.3-b.w4011-25177047232.32.43ce3c0ezcaZD4&skuId=5109812410169)；[京东](https://item.jd.com/10067318747676.html)

## 工具

- H2.0/1.5内六角扳手
- 镊子

## 准备工作

关闭电源，移除 MicroSD 卡。

## 拆卸指南

### **步骤 1：移除屏幕和前面盖**

参考 [屏幕组件](screen.md)  和 [P1P前面盖](front-cover.md) / [P1S前面盖](p1s-front-cover.md) 的相关内容，移除屏幕和前面盖。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/front_cover_removed.jpg)

### **步骤 2：**移除密封泡棉

用手移除密封泡棉，注意不要过于用力，避免损坏 AP 主板上的元器件。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/foam.jpg)

### **步骤 3：断开 WIFI 天线，**移除螺丝

1. 用螺丝刀翘起 WIFI 天线，断开连接。
2. 用 H2.0 内六角扳手移除 4 颗螺丝。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/1_connector_4_screws.jpg)

### 步骤 4：断开屏幕排线

将 AP 主板从横梁中取出，断开屏幕排线。

![](https://wiki.bambulab.com/p1/maintenance/screen-connector-cable/屏幕排线.jpg)

## 安装指南

### **步骤 1：**连接屏幕排线

将新的屏幕排线连接至 AP 主板。

![](https://wiki.bambulab.com/p1/maintenance/screen-connector-cable/屏幕排线.jpg)

### **步骤 2：**安装 AP 主板

放置 AP 主板，将屏幕排线穿过线孔，注意避让下方 WIFI 电缆，并将 WIFI 电缆穿出。根据 MicroSD 卡槽的缺口位置，将 AP 主板安装到横梁上。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/install_the_ap_board1.jpg)

### **步骤 3：**锁螺丝固定

锁入 4 颗螺丝，连接好 WIFI 天线。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/1_connector_4_screws.jpg)

### **步骤 4：**贴附密封泡棉

将密封泡棉贴附好。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/foam.jpg)

### **步骤 5：**安装前面盖、屏幕

参考  [前面盖](front-cover.md) 和  [屏幕组件](screen.md) 的相关内容，安装前面盖和屏幕。

![](https://wiki.bambulab.com/p1/maintenance/front-cover/display_installed.jpg)

## 如何验证完成

启动打印机，确认屏幕能正常显示，且其上的按键能正常响应，说明安装成功。

![](https://wiki.bambulab.com/p1/maintenance/screen/screen_ok.jpg)

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
