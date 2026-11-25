---
path: zh/p3c/maintenance/replace-ap-board
title: "P3C AP 板更换指南"
description: "本文介绍了如何更换 P3C AP 板"
tags: []
created: 2026-11-24T14:06:10.929Z
updated: 2026-11-24T14:06:10.929Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-ap-board
---

## AP 板

简述：AP 板的全称是应用处理器主板（Application Processor Main Board），它是打印机内处理信息交互的电路板，安装在打印机的左侧维修盖板以内。它为打印机提供了一个独立的操作环境，并支持打印机应用所需的所有系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。

AP 板连接器说明如下：  
![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/001.png)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 工具头 | 6 | 选配相机 |
| 2 | 24V 电源 | 7 | Wi-Fi 天线 |
| 3 | AP-MC 通信线 | 8 | 屏幕排线 |
| 4 | 补光灯-左 | 9 | 实况摄像头排线 |
| 5 | AP-MC USB线 |  |  |

## 何时更换

1. AP 板出现明显的物理损坏，如连接器损坏、元器件脱落或烧坏；
2. 经 Bambu Lab 技术支持分析需更换 AP 板。

## 所需工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手
- 镊子
- AP 板

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 AP 板

### 步骤 1. 移除维修盖板

使用 H2.0 内六角扳手移除维修盖板 4 颗螺丝，取下维修盖板。

|  |  |
| --- | --- |
| 002.png | 003.png |

### 步骤 2. 断开线缆连接

依次断开除 WiFi 天线、 USB-C 接头以外的连接线缆接口；

![004.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/004.png)

使用 H2.0 内六角扳手移除黑色固定片 1 颗螺丝，松开固定片后断开 USB-C 线缆连接。

|  |  |
| --- | --- |
| 005.png | 006.png |

### 步骤 3. 移除 AP 板

> **拆装提示：**
>
> - 市面上 WiFi 天线有 2 个版本，松出 AP 板时可以进行判断，其中短款天线线长（右图）余量较少，需要拆卸左侧板后拆装；长款天线（左图）则不需要拆卸侧板。
>
> ![007.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/007.png)  
> 长款天线可以直接将 WiFi 天线接头连接到 AP 板
>
> ![008.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/008.png)  
> 短款天线线长余量少较难直接操作
>
> - WiFi 天线上有白色电子硅胶，断开连接前切勿大力拖拽，可**先除胶后**再进行拔除。
>
> ![009.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/009.png)
>
> - 电子硅胶主要用于运输过程中确保插头的稳定连接，重新安装无需再涂抹硅胶。

**长款天线：**

使用 H1.5 内六角扳手，移除 AP 板 4 颗固定螺丝，将 AP 板松出，随后再断开 WiFi 天线接头移除 AP 板。

|  |  |
| --- | --- |
| 010.png | 011.png |

**短款天线：**

请参考WiFi：[P3C 左侧板/右侧板更换指南](replace-side-panel-left.md)，移除左侧板。随后使用 H1.5 内六角扳手，移除 AP 板 4 颗固定螺丝，将 AP 板松出后再断开 WiFi 天线接头移除 AP 板。

|  |  |
| --- | --- |
| 012.png | 013.png |

## 安装 AP 板

### 步骤 1. 连接 WiFi 天线

**长款天线连接：**

将 WiFi 天线连接到 AP 板；

![014.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/014.png)

**短款天线连接：**

将 WiFi 天线连接到 AP 板。

![015.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/015.png)

### 步骤 2. 安装 AP 板

找到机器侧板上的定位销，将 AP 板对齐定位销安装到位；使用 H1.5 内六角扳手锁入 AP 板 4 颗固定螺丝。（若为短款WiFi天线，需参考WiFi：[P3C 左侧板/右侧板更换指南](replace-side-panel-left.md)，增加安装左侧板的步骤）

|  |  |
| --- | --- |
| 016.png | 017.png |

### 步骤 3. 连接线缆

将 Tpye-c 线缆接头插入连接器座，并依次锁附固定片和 1 颗固定螺丝（USB-C 接头带有凸起部分的一侧朝上，当该凸起部位与固定片槽位完全卡入嵌合时，即表示接头已插入到位）；

|  |  |
| --- | --- |
| 018.png | 019.png |

依次插入除 Wi-Fi 天线以外的其他线缆连接；

|  |  |
| --- | --- |
| 020.png | 021.png |

### 步骤 4. 装回维修盖板。

将维修盖板装回侧板，并使用 H2.0 内六角扳手锁入维修盖板 4 颗螺丝。

![022.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/022.png)

### 步骤 5. 绑定新序列号（SN）

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的 AP 板也将不能再被注册或绑定。

更换了 AP 板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换 AP 板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录[拓竹官网](https://bambulab.com/zh/support)申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。

![023.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ap-board/zh/023.jpg)

## 功能验证

连接电源线并启动打印机，能执行并通过打印机的校准流程。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
