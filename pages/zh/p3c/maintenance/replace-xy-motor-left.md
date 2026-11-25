---
path: zh/p3c/maintenance/replace-xy-motor-left
title: "P3C XY 电机更换指南"
description: "本文介绍 P3C 更换 XY 电机的具体操作方法。"
tags: []
created: 2026-11-24T14:06:53.834Z
updated: 2026-11-24T14:06:53.834Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-xy-motor-left
---

## XY 电机

简述：XY 电机是安装在打印机背部，用于驱动工具头完成 X/Y 方向移动的步进电机。由于线缆的长度不同，我们用左右进行区分，面向打印机，左边的是XY电机-左，右边是XY电机-右。

![p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-13-46.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-13-46.jpg)

## 何时更换

- 电机不转
- 电机异响
- 电机异味
- 经 Bambu Lab 技术支持确认需要更换电机

## 所需工具和材料

- H2.0 内六角扳手
- H2.0 内六角扳手 (XY 电机专用）
- 新电机

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

### 拆装提示

> 1. XY 电机的锁定螺丝需要通过打印机框架上的通孔进行拆除，需要提前移除 AMS 3P，请参考 WIKI：[AMS 3P 拆装指南](replace-ams3p.md) ，将 AMS 3P 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3P 的场景下进行。
> 2. XY 电机-左 和 XY 电机- 右 在拆装操作上基本一致，细节差异会作说明。
> 3. 拆装 XY 电机的螺丝时，请提前给扳手上磁，避免螺丝跌落；拆除 XY 电机-右 时，需要使用配件赠送的专用 H2.0 内六角扳手（螺丝孔较深需更长的扳手）。
>
> ![p3c_xy_______-xy_motor_replacement_guide-image-1.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-image-1.png)

## 移除 XY 电机

### 步骤 1. 拆卸背板

请参考Wiki：[P3C 背板更换指南](replace-back-panel.md)，移除背板。

![p3c_xy_______-xy_motor_replacement_guide-image-2.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-image-2.png)

### 步骤 2. 松皮带固定支架

用 H2.0 内六角扳手按图中螺丝标识的顺序，移除 3 颗螺丝，将 XY 皮带固定支架松出。（若更换左电机则拆除左侧皮带固定支架，若更换右电机则拆除右侧皮带固定支架）

![p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-19_09-34-44.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-19_09-34-44.jpg)

更换左电机拆除左侧支架

![p3c_xy_______-xy_motor_replacement_guide-_____1.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-_____1.jpg)

更换右电机拆除右侧支架

### 步骤 3. 松张紧器

用 H2.0 内六角扳手移除 4 颗螺丝，然后再移除黑色张紧器压片和银色弹簧压片。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-28-10.jpg | p3c_xy_______-xy_motor_replacement_guide-image.png |

将张紧器松出，并取下弹簧；另一侧张紧器操作方式一致。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-31-55.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-37-37.jpg |

### 步骤 4. 移除 XY 电机

断开 MC 板端需要更换的电机线缆接头，并将线缆从理线扣中松出；

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-53-05.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-49-53.jpg |

解锁电机线缆磁环，将磁环取下。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-55-14.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-55-31.jpg |

**左电机：**

用磁铁给专用 H2.0 内六角扳手加磁。随后用扳手沿着电机螺丝的位置捅破顶部的泡棉；移除电机靠背板一侧的 2 颗螺丝；然后使用 H2.0 内六角扳手移除腔内一侧图示 2 颗螺丝，将电机和线缆从腔内一侧移除；

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_11-00-07.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-06-13.jpg |

**右电机：**

右电机移除方法与左电机基本一致，但由于右电机螺丝通道被打印头控制转接板遮挡，需先参考 WIKI：[P3C 打印头控制转接板更换指南](replace-tool-control-bridge-board.md)，松出打印头控制转接板；

![p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_11-04-32.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_11-04-32.jpg)

使用 H2.0 内六角扳手先移除腔内一侧图示 2 颗螺丝；

![p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-12-11.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-12-11.jpg)

随后进一步使用 H2.0 专用扳手从转接板安装槽内伸入并移除右电机靠背板一侧 1 颗螺丝，再将扳手捅破旁边泡棉插入，移除靠背板一侧的另 1 颗电机螺丝，即可将电机从靠背板一侧移除；

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_16-34-42.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_16-36-14.jpg |

## 安装 XY 电机

### 步骤 1. 安装 XY 电机

**左电机：**

将电机线缆从腔内一侧穿过穿线孔，到达靠背板一侧，然后安装电机，注意 XY 皮带需要在电机的主动轮的内侧。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-23-54.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-25-13.jpg |

用手扶着电机，先预锁内侧的 1 颗螺丝，不要锁紧，然后按下图标识的序号，呈对角依次锁入另外 3 颗螺丝，待 4 颗螺丝都锁到位置上后，再依次锁紧。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-28-47.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-30-43.jpg |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-31-35.jpg |

将电机线缆套入磁环，随后埋入绿色标记的理线扣中，随后将线缆接头插入到 MC 板的 Y 接口中。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-55-14-1.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-49-53-1.jpg |

**右电机：**

将右电机从背板一侧安装到打印机，注意 XY 皮带需要在电机的主动轮的内侧。用手扶住电机，使用 H2.0 专用扳手预锁入 1 颗螺丝，不要拧紧；然后按下图标识的序号，呈对角依次锁入另外 3 颗螺丝，待 4 颗螺丝都锁到位置上后，再依次锁紧。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_16-47-25.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_16-48-36.jpg |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_16-49-11.jpg |

安装磁环，并将电机线缆卡入理线扣，随后连接到 MC 板端 X 接口；

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_10-55-14-2.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_16-55-04.jpg |

请参考 WIKI：[P3C 打印头控制转接板更换指南](replace-tool-control-bridge-board.md)，安装打印头控制转接板。

![p3c_xy_______-xy_motor_replacement_guide-20261123-165815.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-20261123-165815.jpg)

### 步骤 2. 安装张紧器

将张紧弹簧安装到张紧器上，并装入张紧器槽中，弹簧先进槽。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-49-03.jpg | p3c_xy_______-xy_motor_replacement_guide-20261120-103031.jpg |

安装张紧器压片，左侧（面向打印机正面）张紧器的压片缺口朝上进行安装（右侧张紧器压片缺口朝下），往弹簧压缩方向轻推张紧器，使压片螺丝孔对齐打印机上的张紧螺丝孔后锁入 1 颗张紧器螺丝（细牙螺丝），不要锁紧，随后用同样的方式锁入第二颗螺丝；

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-20_22-54-36.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_17-14-44.jpg |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_17-17-46.jpg |

安装弹簧压片，方形定位缺口朝上（另一侧方形定位缺口朝下），锁入 2 颗螺丝（粗牙）固定。另一侧操作方式基本一致。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_17-39-04.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_17-22-07.jpg |

### 步骤 3. 安装皮带固定支架

压缩弹簧到极致压缩状态，锁紧张紧器螺丝；

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_17-24-21.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_17-26-29.jpg |

将皮带固定支架安装到工具头两侧，按序号依次锁紧两侧的螺丝。另一侧操作方式基本一致；拧松张紧器 2 颗固定螺丝，前后移动工具头 2~3 次后再重新锁紧张紧器螺丝，重新张紧皮带。

|  |  |
| --- | --- |
| p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-19_10-03-08.jpg | p3c_xy_______-xy_motor_replacement_guide-pixpin_2026-11-23_17-26-29-1.jpg |

### 步骤 4. 安装背板

您可以参考WIKI：[P3C 背板更换指南](replace-back-panel.md)，安装背板。

![p3c_xy_______-xy_motor_replacement_guide-image-3.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-xy-motor-left/zh/p3c_xy_______-xy_motor_replacement_guide-image-3.png)

## 功能验证

启动打印机，执行一次回零操作，能正常完成即可。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
