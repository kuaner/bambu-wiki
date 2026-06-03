---
path: zh/x1/maintenance/replace-ap-board
title: "更换 AP 主板 -- X1 系列"
description: "本指南介绍更换 X1 系列打印机 AP 板的详细步骤。"
tags: ["x1", "ap 板"]
created: 2022-08-05T03:07:18.696Z
updated: 2026-05-21T13:30:08.307Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-ap-board
---

## 什么是 AP 主板

AP 主板的全称是指应用处理器主板（Application Processor Main Board），它是打印机内处理信息交互的电路板。它为打印机提供了一个独立的操作环境，并支持打印机应用所需的所有系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。

![](https://wiki.bambulab.com/x1/maintenance/replace-ap-board/426px-ap_board_new.png)

AP 板上的连接器

![](https://wiki.bambulab.com/x1/maintenance/replace-ap-board/connectors_on_the_ap_board.jpg)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **序号** | **连接对象** | **序号** | **连接对象** | **序号** | **连接对象** |
| 1 | 机箱摄像头 | 4 | 按键板 | 7 | USB-C |
| 2 | 机箱LED | 5 | MC 板 (电源) |  |  |
| 3 | WIFI 天线 | 6 | MC 板(通信) |  |  |

## 何时更换

如果出现板件电压异常、芯片异常发热甚至烧坏、有不可恢复的系统故障或固件升级故障，可能需要更换AP主板。但更多的情况是，需要结合日志文件的分析来确定机器已出现的问题是否源于AP主板。

## 所需的工具和材料

- 一块新的 AP 主板
- H2.0 内六角扳手
- 吹风机
- 固定胶布或 UV 胶、紫外线灯（为了进一步稳固插头连接器，并不强制使用）
- 硅胶

![](https://wiki.bambulab.com/x1/maintenance/replace-the-chamber-led/silicone_glue.jpg)

仅供参考

## 开始操作前的安全警告和机器状态

在开始本指南中的过程之前，请确保机器已关闭。

> 注意：在开始安装前，请先拍照并留存 AP 板上的序列号（即背面二维码），以便在后续注册流程中使用。  
> ![qr-x1--.png](https://wiki.bambulab.com/x1/maintenance/replace-ap-board/qr-x1--.png)

## 操作指南

### 步骤 1 - 关闭电源

关闭打印机电源，拔下电源线，并取下顶部玻璃盖板。

### 步骤 2 - 打开 AP 主板盖

揭开位于机器左上方的 AP 主板盖，如下图所示。

|  |  |
| --- | --- |
|  |  |

### 步骤 3 - 断开 USB-C 电缆

移除 USB-C 线夹紧块的 1 颗，断开 USB-C 线和另外两条 AP 主板连接到 MC 板的线缆连接。

|  |  |
| --- | --- |
|  |  |

### 步骤 4 - 断开其他电缆

使用吹风机加热软化固定连接器的硅胶，然后断开摄像头电缆、LED 灯电缆和按钮板电缆的连接，最后还要断开 WIFI 天线。

|  |  |
| --- | --- |
|  |  |

### 步骤 5 - 移除 AP 板

移除固定 AP 主板的 4 颗螺丝，缓慢地取出 AP 主板，因为它的另一面仍连接着 1 条软排线。

|  |  |
| --- | --- |
|  |  |

### 步骤 6 - 断开 FPC

用吹风机加热固定 FPC 的 UV 胶，轻轻解锁下图中用红色方块标记的锁扣，移除 FPC。如果发现有 UV 胶残留在 FPC 排线的针脚上，请将其清理干净。

|  |  |
| --- | --- |
|  |  |

### 步骤 7 - (装配) 连接 FPC

准备好替换的 AP 主板，将 FPC 接入到 AP 主板上的连接器。按下连接器锁扣，锁定 FPC。

|  |  |
| --- | --- |
|  |  |

### 步骤 8 - 点 UV 胶（或贴胶布）

在连接器上点上 UV 胶，并用紫外线灯照射硬化 UV，也可使用粘性较强的胶布进行加固，防止 FPC 从连接器上松脱。

![](https://wiki.bambulab.com/x1/maintenance/replace-ap-board/fpc_connected.jpg)

### 步骤 9 -安装 AP 板

将 AP 主板底部的两处缺口对齐两条框架上的限位块，安装到位，并用 4 颗螺丝将 AP 主板固定。

|  |  |
| --- | --- |
|  |  |

### 步骤 10 - 连接电缆（1）

首先将电缆连接到 AP 主板左侧的连接器上，并在 WIFI 电缆、LED 电缆、摄像头电缆和按钮板电缆上点上硅胶固定，需要静置至少 30 分钟。

|  |  |
| --- | --- |
|  |  |

### 步骤 11 - 连接电缆（2）

首先连接 2 根到 MC 板的连接电缆，然后将 USB-C 线连接到 AP 主板上，注意\*\*字母 A 朝外，\*\*然后锁入 1 颗螺丝固定 USB 线夹紧块，并另外 2 根电缆扣到夹紧块的卡扣上。

![](https://wiki.bambulab.com/x1/maintenance/replace-usb-cable/connect_to_ap_board.jpg)

|  |  |
| --- | --- |
|  |  |

### 步骤 12 - 合上 AP 主板盖

将 AP 护盖压回原位，最后盖上玻璃顶盖。

![](https://wiki.bambulab.com/x1/maintenance/replace-ap-board/350px-cover3.png)

### 步骤 13 - 绑定新序列号（SN）

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的 AP 板也将不能再被注册或绑定。

更换了 AP 板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换 AP 板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。  
![register_sn.jpg](https://wiki.bambulab.com/x2d/maintenance/ap-board/register_sn.jpg)

## 如何验证成功

### 根据电路板灯语判断

**正常状态：AP 板有 2 个指示灯,一个常亮红灯,一个 1 秒闪烁一次红灯**

在拧回所有螺丝前，可先预装或不装盖子（小心用电安全，断电操作），再通电检查该电路板灯语是否正常，灯语正常，再拧回螺丝，这样可以避免返工。

<https://public-cdn.bblmw.com/wiki/video/X1-AP.mp4>

### 连接电源线并打开电源，发起打印，检查是否有报错。

连接电源线并打开电源。如下所示运行设备自检操作，如果没有出现错误，则更换成功。

![](https://wiki.bambulab.com/x1/maintenance/replace-chamber-temp-fan/350px-self_test.png)

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
