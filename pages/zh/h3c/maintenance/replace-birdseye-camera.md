---
path: zh/h3c/maintenance/replace-birdseye-camera
title: "俯视摄像头更换指南"
description: ""
tags: []
created: 2026-11-03T12:38:02.460Z
updated: 2026-11-10T11:48:52.278Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-birdseye-camera
---

## 俯视摄像头

拓竹H3C 用户可选配 800 万像素高清俯视摄像头。支持两种模式：3D打印监控模式下分辨率为 1632 × 1224（30fps），确保画面流畅；2D 俯拍创作模式下分辨率可达 3264 × 2448（10fps），满足高精度拍摄需求。

> **提示**：摄像头仅用于打印机相关功能。请确保摄像头已正确安装，使摄像头视野正确朝向打印区域，以避免对打印区域或喷嘴的检测出现问题

![001.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/001.jpg)

> **线材卡扣安装提示**
>
> 1. **卡扣配件更换**：包装内附赠全新线材卡扣。若原装卡扣出现磨损或损坏，请及时更换；若状态良好，可继续复用原装卡扣，配件盒里的卡扣可以替换市面上任意一种卡扣。
> 2. 卡扣**螺丝选用**：市面机器卡扣螺丝分 2 种型号，配件内附 2 颗对应备用螺丝。请务必使用**原装同规格螺丝**固定（例如：原机为细长螺丝(H1.5)，更换时须选用同款细长螺丝(H1.5)），确保安装稳固。
>
> ![002.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/002.jpg)

## 何时更换

1. 俯视摄像头画面异常；
2. 俯视摄像头通信故障。

## 所需工具和材料

> - H2.0 内六角扳手
> - H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## **温馨提示：**

本文操作中最具挑战性的是第 5 步，这一步的的整理线缆操作能让线缆更稳固、外观更整洁，但您也可以选择跳过这一步，只需将线缆顺至后方避开料管，保持视觉清爽即可。此举也能避免未来拆装 AMS 时牵涉线槽走线，大幅简化操作流程。

如果执行第5步若感觉操作空间不足，可先参考wiki[取下 AMS 3H 舱体](replace-chamber.md)，再按本文步骤操作。

## 安装俯视摄像头

### 第 1 步 移除 AMS 左磁吸侧板和打印机左视窗

移除 AMS 左侧磁吸侧板，然后参考 WIKI: [视窗更换指南](replace-side-glass-left.md) ，将打印机左侧视窗移除。

|  |  |
| --- | --- |
| 003.jpg | 004.jpg |

> 注意：机器通电时，切勿从视窗处将手伸入 XY（金属）框内部，以防被夹伤！

### 第 2 步 移除导光板和 USB 线卡

视机器版本而定，若此处有泡棉，请将其推下移除

![002.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/remove-foam.jpg)

用 H1.5 内六角扳手移除 2 颗螺丝，并取下导光板。注意需将导光板向上提，离开卡扣位置后再取下。

![005.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/005.jpg)

用 H2.0 或H1.5 内六角扳手移除 1 颗螺丝，取下 USB 线材卡扣。

![006.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/006.jpg)

### 第 3 步 连接俯视摄像头线缆

用手或内六角扳手在照片蓝色圈所示的位置找到过线孔并撑开，然后将俯视摄像头线缆一字直头的一端穿过这个预留的过线孔。

|  |  |
| --- | --- |
| 007.jpg | 008.jpg |

将线缆整理入卡扣中，断开 AP 板上的图示的两个小连接器，以做好避让。

|  |  |
| --- | --- |
| 009.jpg | 010.jpg |

检查插头的朝向，**有凸起的一侧朝外（极重要）**，然后连接到 AP 板左下的 USB 接口上。

|  |  |
| --- | --- |
| 011.jpg | 012.jpg |

连接上面操作时拔掉的 2 个插头；安装线材卡扣，压紧两个 USB 插头，锁入 1 颗螺丝固定。拧紧螺丝后，建议再次检查所有相关插头，确保其已插紧且无松动。

|  |  |
| --- | --- |
| 013.jpg | 014.jpg |

### 第 4 步 安装俯视摄像头

从料管与料管支架间穿出连接线（弯头），方便后续步骤5将线缆压入线槽。（提示：此项关联步骤5的线缆整理，按需执行）

|  |  |
| --- | --- |
| 017.jpg | 018.jpg |

将弯头一端与摄像头连接，朝向如图所示，插头端面必须**正对镜头面（极重要）**。

|  |  |
| --- | --- |
| 015.jpg | 016.jpg |

> 安装俯视摄像头时：
>
> 1. 摄像头的线缆要卡进 AMS 支架的挂钩；
> 2. 请先将摄像头底部的卡爪对准 AMS 支架安装槽上的大缺口装入，随后朝**小缺口**方向（从前往后）平滑推到底。固定摄像头。
>
> |  |  |
> | --- | --- |
> | 019.jpg | 020.jpg |

根据上述关注点，对齐卡爪和大缺口安装摄像头，然后从前往后滑动锁紧摄像头，需要听到咔哒一声（极重要）表示安装到位。

|  |  |
| --- | --- |
| 021.jpg | 022.jpg |

**安装状态确认（极重要）**：请参照右图，将摄像头正确装入支架，确保完全安装到位。

|  |  |
| --- | --- |
| 023.jpg | 024.jpg |

### 第 5 步 整理俯视摄像头线缆（选做，3个理线位置（卡扣或者槽)）

> 温馨提示：本文操作中最具挑战性的是第 5 步，整理线缆的操作能让线缆更稳固、外观更整洁，但您也可以选择跳过本步，只需将线缆顺至后方避开料管，保持视觉清爽即可。此举也能避免未来拆装 AMS 时牵涉线槽走线，大幅简化操作流程。  
> 若整理线缆时，贴线扣空间受限或拆料管支架困难，可先参考 Wiki 拆下 AMS 3H 舱体。操作空间变大后，无需拔出左料管支架，直接将线缆卡入 2 个线槽即可理线。 [AMS 3H 舱体拆装指南](replace-chamber.md)

从 AMS 左框架处将手伸入腔内，在料管主支架左侧位置贴附一个线扣（如有），保持按压 5 ~ 8 秒，卡口朝上，将线缆卡入线缆卡扣中。

|  |  |
| --- | --- |
| 025.jpg | 026.jpg |

把手伸进 AMS 左侧，大拇指抵住支架底部（1）、食指捏住线槽（2），直接把左料管支架拔出来。

|  |  |
| --- | --- |
| 027.jpg | 028.jpg |
| 029.jpg | 030.jpg |

将线缆整理进上左料管支架上面的2个线槽中，然后将左料管支架装回原位，按压到位。

|  |  |
| --- | --- |
| 031.jpg | 032.jpg |

### 第 6 步 安装导光板和视窗

推入装回泡棉(如有)

![002.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/install-foam2.jpg)

根据 2 个螺丝孔的位置安装导光板，先将导光板两侧的螺丝位挂进卡扣，然后锁入 2 颗螺丝进行固定。

![034.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/034.jpg)

请参考 WIKI: [视窗更换指南](replace-side-glass-left.md)，将左侧视窗安装到左侧板上。

![035.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/035.jpg)

## 移除俯视摄像头

### 第 1 步 移除视窗和导光板

参考本指南中，安装俯视摄像头部件的第 1 步和第 2 步，移除视窗和导光板、 USB 线材卡。

![036.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/036.jpg)

### 第 2 步 断开俯视摄像头与 AP 板的连接

向后拔出 USB 插头，将线缆从 AP 板上断开，然后将线缆从卡扣上松出，。

|  |  |
| --- | --- |
| 037.jpg | 038.jpg |

将线缆通过过线孔向上抽出，在退出 USB 插头手，用手协助调整位置并提供助力。。

|  |  |
| --- | --- |
| 039.jpg | 040.jpg |

### 第 3 步 移除俯视摄像头

如下图，滑动摄像头进行解锁卡扣，然后将摄像头从 ASM 支架上移除。

|  |  |
| --- | --- |
| 041.jpg | 042.jpg |

沿着线缆的布置路径，将线缆松出，移除俯视摄像头。

![043.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/043.jpg)

### 第 4 步 安装导光板和视窗和AMS磁吸侧板

推入装回泡棉(如有)

![002.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/install-foam2.jpg)

根据 2 个螺丝孔的位置安装导光板，先将导光板两侧的螺丝位挂进卡扣，然后锁入 2 颗螺丝进行固定。

![044.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/044.jpg)

请参考 WIKI: [视窗更换指南](replace-side-glass-left.md)，将左侧视窗安装到左侧板上。（可以在验证安装成功后再安装）

![045.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/045.jpg)

对齐左框架下方的安装槽，将左侧板贴向 AMS 支架，按压左侧板将其安装到位，确认无浮起。

|  |  |
| --- | --- |
| 046.jpg | 047.jpg |

## 功能验证

接通电源并用 Bambu Studio 绑定打印机，在设备状态页点击圆圈处切换至俯视视角；若画面正常显示，即代表安装成功。

![033.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-birdseye-camera/zh/033.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
