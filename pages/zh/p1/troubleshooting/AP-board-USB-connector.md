---
path: zh/p1/troubleshooting/AP-board-USB-connector
title: "P1 系列 USB 端口故障排查指南"
description: "本指南主要用于 P1 系列 AP 板上的 USB 端口故障排查过程"
tags: ["p1"]
created: 2025-02-18T07:56:44.143Z
updated: 2025-02-28T09:13:19.794Z
source: https://wiki.bambulab.com/zh/p1/troubleshooting/AP-board-USB-connector
---

P1 系列 AP板 有一个5V 1.5A USB A端口，可以作为外部设备电源使用。

P1 系列 AP 板上 USB 端口的一个常见用途是为外部灯供电，为打印机增加更多照明。我们的[6500K 白色 LED 灯带](https://detail.tmall.com/item.htm?abbucket=8&id=837988590905&pisk=gEXmFc2PssRjgDw3h49b9BOfXHVJcK96GNH9WdLaaU87fosY1ArGWNdZBiFbjlYl5Edv3OfSIMs1Ho9TcKsXCdzLJJQGci96cf634tDr4hIrQf8awLJ9WVh3JJedqS-XBgzdHezXOntKQdR2_3yyPhh27NR2U38Wfhu2QEruqhTy0V82Q0RyXh-qQNkwz4-v0VlqgdyP4HLy7d8N7grkXjnoQeXNFTzyeZATcTHcFnAD8i8VDiBrQIlfmUmS2TfkEeyprAkNEnj5w6WKK5LFOEdpPay-ndjyjwxho4zkQgXfKQW4PAbhr6JkV_aisefND61wZoyVqKYDtTd0Crpc_Z6MGsm_AgJVP6TBg7aWqtBpseOozrSRqERhsZUSQECh4aAde4HpUM5kEgumaXWC-AtzXTls1I-WqeH5DLKKsMvUQuqoOSO2VnUdBucaHI-WceZuqXgMg3tAg&rn=faf21119dfbe361ecfa5fcb21ac4ae54&spm=a1z10.3-b-s.w4011-25177047232.28.17d23c0ecUOKYC)与 P1 系列兼容。

> **注意：避免连接从 AP 板连接负载超过 5V 1.5A 用电器，这大概率会导致 AP 板故障。**

## 何时使用

以下几种情况为 AP 板 USB 端口常见故障：

- 连接用电器没有供电。
- USB A 端口出现物理损坏。
- 拓竹技术支持推荐。

## 所需工具和材料

- 一端带有USB A 接头的线缆
- 万用表（可选）

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 排查指引

关于连接在 USB A 端口的用电器无法正常取电，首先我们确认是否为 USB A 端口物理损坏或 AP 板故障。

### 1.端口物理损坏排查

USB A 端口无法正常使用，常见的物理损坏主要是插接 USB 线缆插接到 AP 板端口用力多大或者插偏位置，导致 USB 母座和 AP 板脱焊。

目视检查 USB A 母座到 AP 板引脚是否正常。

- 左侧的箭头位置是 USB 母座的固定针脚，这部分将是固定在 AP板 上的。
- 右侧方框位置四根引脚主要负责供电和通讯，需要检查引脚是否有断开或翘起的情况。

下图所示为正常无损坏。

![](https://wiki.bambulab.com/p1/troubleshooting/usb-ap-board/usb_connector_pins.jpeg)

可以尝试插入 USB 线缆轻轻地上下晃动 USB 电缆，检查 USB 母座是否有松动的痕迹。

如果没有任何晃动，接下来需要使用 USB 用电器或万用表通继续进行排查故障。

### 2.使用 USB 用电器检查是否供电

可以更换其他 5V 用电器测试该端口是否正常工作；例如，可以使用 USB 线缆为手机充电。

![](https://wiki.bambulab.com/p1/troubleshooting/usb-ap-board/connect_usb_port_to_board.jpg.jpeg)

如果手机正在充电，则确认 USB A 端口工作正常，并且应该检查其他用电设备和线缆是否有出现损坏。

如果手机无法充电，该问题与 AP 板 的电源输出有关，可能需要更换新的 AP 板。

![](https://wiki.bambulab.com/p1/troubleshooting/usb-ap-board/phone.jpeg)

### 3.使用万用表供电

如果您有万用表，可以用它来测试 AP 板的是否有 5V 电压输出。

需要将万用表设置为正确的直流测量档位，测量下图所示 #1 #2 位置。

> 注意：测试过程需要注意两表笔不要触碰到一起避免造成短路。

|  |  |
| --- | --- |
|  |  |

正常输出电压为 5V 左右，如果没有电压输出则需要更换 AP 板。

![](https://wiki.bambulab.com/p1/troubleshooting/usb-ap-board/multimeter.jpeg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
