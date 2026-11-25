---
path: zh/p3c/maintenance/replace-swaptek-rack-frame
title: "P3C 闪切挂架框架更换指南"
description: "本文介绍了如何更换 P3C 闪切挂架框架"
tags: []
created: 2026-11-24T14:06:31.823Z
updated: 2026-11-24T14:06:31.823Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-swaptek-rack-frame
---

## 闪切挂架框架

简述：

闪切挂架安装在机箱前侧，是用于挂载空闲 / 待命打印头的可升降组件，由闪切挂架框架、挂架升降电机、泊位组件\*7 构成，在移除挂架升降电机、泊位组件\*7 后，剩下的就是闪切挂架框架。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack-frame/zh/001.png)

## 何时更换

挂架升降机械传动结构损坏或框架变形。

## 所需工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除闪切挂架框架

### 步骤 1. 取下闪切挂架

请您参考WiKi：[P3C 闪切挂架更换指南](replace-swaptek-rack.md)，取下闪切挂架后放置在桌面上。

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack-frame/zh/002.png)

### 步骤 2. 移除挂架升降电机

揭开联轴器上方的遮盖并撕下，露出联轴器；

|  |  |
| --- | --- |
| 003.png | 004.png |

通过调整挂架升降位置转动联轴器，使联轴器上的顶丝露出；

![005.webp](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack-frame/zh/005.webp)

使用 H2.0 内六角扳手拧松联轴器上靠近电机一侧的顶丝（一般拧松 3~4 圈即可，无需取下）；继续转动联轴器调整升降位置，待另一处靠近电机一侧的顶丝露出后，按相同方式拧松。

|  |  |
| --- | --- |
| 006.png | 007.png |

使用 H2.0 内六角扳手，移除电机顶部的 4 颗螺丝，取下挂架升降电机。

|  |  |
| --- | --- |
| 008.png | 009.png |

### 步骤 3. 移除泊位组件

使用 H1.5 内六角扳手移除图示泊位组件的 3 颗固定螺丝，取下泊位组件；7 个泊位组件拆装方式相同。

|  |  |
| --- | --- |
| 010.png | 011.png |

## 安装闪切挂架框架

### 步骤 1. 安装泊位组件

将泊位组件上的定位柱对齐框架上的定位孔装入，并使用 H1.5 内六角扳手锁入 3 颗螺丝固定。7 个泊位组件拆装方式相同。

|  |  |
| --- | --- |
| 012.png | 013.png |

### 步骤 2. 安装挂架升降电机

> **拆装提示：**
>
> 装入电机前，请调整电机轴位置，使电机轴 D 平面与顶丝位于同一平面。
>
> |  |  |
> | --- | --- |
> | 014.png | 015.png |

保持电机**线缆朝下**将电机装入安装槽，随后使用 H2.0 内六角扳手锁入 4 颗螺丝固定；

![016.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack-frame/zh/016.png)

使用 H2.0 内六角扳手锁紧联轴器上靠近电机一侧的 2 处顶丝；

|  |  |
| --- | --- |
| 017.png | 018.png |

将联轴器上的遮盖重新张贴到位。

![019.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack-frame/zh/019.png)

### 步骤 3. 安装闪切挂架

请您参考WiKi：[P3C 闪切挂架更换指南](replace-swaptek-rack.md)，完成闪切挂架的安装。

![020.webp](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack-frame/zh/020.webp)

## 功能验证

启动打印机，执行一次挂架对位校准，能正常完成即可。

![021.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-swaptek-rack-frame/zh/021.png)

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
