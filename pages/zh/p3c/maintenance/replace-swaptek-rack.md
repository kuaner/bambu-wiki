---
path: zh/p3c/maintenance/replace-swaptek-rack
title: "P3C 闪切挂架更换指南"
description: "本文介绍了如何更换 P3C 闪切挂架"
tags: []
created: 2026-11-24T14:06:30.930Z
updated: 2026-11-24T14:06:30.930Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-swaptek-rack
---

## 闪切挂架

简述：闪切挂架安装在机箱前侧，是用于挂载空闲 / 待命的打印头的可升降组件。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack/zh/001.png)

## 何时更换

HMS 报错且经 Bambulab 技术团队确认需更换的。

## 所需工具和材料

- H2.0 内六角扳手
- 闪切挂架

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 本指南是在已移除 AMS 的情况下进行的，请先参考 WiKi：[AMS 3P 拆装指南](replace-ams3p.md) 完成对AMS的移除。

## 移除闪切挂架

### 步骤 1. 移除维修盖板

您可以参考WiKi：[P3C 维修盖板更换指南](replace-service-panel.md)，使用 H2.0 内六角扳手移除右侧板上维修盖板 4 颗螺丝后将其取下，露出闪切挂架控制板；

|  |  |
| --- | --- |
| 002.png | 003.png |

随后按压图示 2 处线缆端子解锁卡扣，断开连接；再掰开磁环上的卡扣，将磁环从线缆上取下。

|  |  |
| --- | --- |
| 004.png | 005.webp |

### 步骤 2. 移除玻璃前门与上合页

请您参考WiKi：[P3C 玻璃前门更换指南](replace-front-door.md)，完成玻璃前门的移除；

![006.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack/zh/006.png)

随后使用 H2.0 内六角扳手，移除左上方的门合页的 2 颗固定螺丝，取下合页。

|  |  |
| --- | --- |
| 007.png | 008.png |

### 步骤 3. 移除闪切挂架

揭开右边门硅胶条上方一小段以露出闪切挂架右侧固定螺丝孔，使用 H2.0内六角扳手移除 4 颗螺丝；

![009.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack/zh/009.png)

先将闪切挂架靠屏幕的一端小幅度向后方轻推，使挂架与打印机分离一部分，再将电机端抽出。（移除挂架前请确认步骤 2 中电机线缆磁环已取下）

![010.webp](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack/zh/010.webp)

## 安装闪切挂架

### 步骤 1. 安装闪切挂架

将 2 根线缆穿过右前角的过线孔；随后将闪切挂架的电机端先卡入右前角凹槽，再将另一端安装到位。

|  |  |
| --- | --- |
| 011.png | 012.webp |

扶住闪切挂架避免掉落，使用 H2.0 内六角扳手按序锁入 1-4 号共 4 颗螺丝固定，随后将那一小段硅胶条重新贴合。

![013.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack/zh/013.png)

### 步骤 2. 安装合页与玻璃前门

将合页对齐打印机金属框架上的螺丝孔，使用 H2.0 内六角扳手锁入 2 颗螺丝固定；再参考WiKi：[P3C 玻璃前门更换指南](replace-front-door.md)，完成玻璃前门的安装。

|  |  |
| --- | --- |
| 014.png | 015.png |

### 步骤 3. 安装维修盖板

将磁环安装到闪切挂架升降电机的线缆上，并将 2 根线缆的接头插入挂架控制板的对应接口；最后用胶布将磁环粘贴固定。

|  |  |
| --- | --- |
| 016.png | 017.png |

将维修盖板对准安装槽装入，并向内按压盖板边缘，伴随连续的卡扣声响，确认所有卡扣安装到位。使用 H2.0内六角扳手依次拧紧维修盖板 4 颗螺丝。

|  |  |
| --- | --- |
| 018.png | 019.png |

## 功能验证

启动打印机，执行一次挂架对位校准，能正常完成即可。

![020.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack/zh/020.png)

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
