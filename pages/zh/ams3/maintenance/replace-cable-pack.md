---
path: zh/ams3/maintenance/replace-cable-pack
title: "AMS 3H 线材包更换指南"
description: "本文介绍了AMS 3H 线材包更换指南"
tags: []
created: 2026-11-06T10:13:06.983Z
updated: 2026-11-06T10:13:06.983Z
source: https://wiki.bambulab.com/zh/ams3/maintenance/replace-cable-pack
---

## AMS 线材包

安装在 AMS 内部、用于连接与各功能模块或电路板的连接线缆集，一共有 6 条。

| 编号 | 用途 / 连接对象 | 实物图示 |
| --- | --- | --- |
| 1 | AMS 主板 - AMS AC 板连接线 | Image |
| 2 | AMS 主板 - 6pin接口板连接线 （24 V 电源） |  |
| 3 | AMS 主板 - 接口板连接线 |  |
| 5 | 入料口组件连接线 （ H8 用） |  |
| 5 | 入料口组件连接线 （ 非 H8 用） |  |
| 6 | AMS 3H 自动进料组件指示灯连接线 |  |

## 何时更换

- 连接线缆损坏
- 插头损坏

## 工具和材料

- H1.5 内六角扳手
- H2.0 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 更换 AMS 线材包

### 第 1 步 移除 AMS 舱体

请参考WIKI: [AMS 3H 舱体拆装指南](../../h3c/maintenance/replace-chamber.md)，将 AMS 舱体从AMS 支架上取下。

### 第 2 步 移除 AMS 主板/ 接口板装饰盖

移除 AMS 主板 装饰盖螺丝（3 PCS）和接口板装饰盖螺丝 （4 PCS），移除装饰盖。

|  |  |
| --- | --- |
| 002.jpg | 003.jpg |

### 第 3 步 更换 AMS 主板 到 AMS AC 板连接线

按压插头锁扣并拔出，依次断开线缆在 AC 板和 主板的连接，将 AMS 主板 - AMS AC 板的连接线从卡扣中松出并取下。

![004.jpg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-cable-pack/zh/004.jpg)

将新的线缆分别连接到 AC 板和 主板的连接器，并将线缆整理入卡扣中，即完成连接线的更换。

### 第 4 步 更换 AMS 主板 到 AMS 接口板连接线

按压插头锁扣并拔出，依次断开线缆在 接口 板和 主板的连接，将 AMS 主板 - AMS 接口板的连接线从卡扣中松出并取下。

![005.jpg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-cable-pack/zh/005.jpg)

将新的线缆分别连接到接口板和主板的连接器，并将线缆整理入卡扣中，即完成连接线的更换。

### 第 5 步 更换 AMS 主板 到 6 pin 接口板连接线

按压AMS 主板电源线插头锁扣并拔出，然后将线缆从卡扣中松出。

![006.jpg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-cable-pack/zh/006.jpg)

从电源插座边角处用力扳开尾板并取下；将线缆继续从卡扣中松出，用 H2.0 内六角扳手移除两颗螺丝。

|  |  |
| --- | --- |
| 007.jpg | 008.jpg |

将电源插座松出，可从 6 pin 接口板背面将线缆断开，并移除。换上新的线缆，安装电源插座并锁上螺丝，将上面的操作顺序反过来，可安装好新的线缆。

|  |  |
| --- | --- |
| 009.jpg | 010.jpg |

### 第 6 步 更换入料口线缆/ AMS 状态指示灯板线缆

1. 翻转 AMS 舱体， 使其正面朝上，并打上盖。参考 WIKI: [AMS 3H 自动进料组件上盖更换指南](replace-auto-filament-loader-cover.md)，移除自动进料组件上盖。

![011.jpg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-cable-pack/zh/011.jpg)

2. 根据要更换的线缆，按压插头解除锁定并断开连接（入料口/指示灯板端），断开的线缆会自然向后掉落。(下图是指示灯板和 H7\H9 三根线缆的位置示意图，选 H7 和 H9 是因为刚好两个入料口靠近，且分别连接到 AMS 主板和 接口板。)

|  |  |
| --- | --- |
| 012.jpg | 013.jpg |

然后接上新的线缆，并从原线缆位置穿过过线孔。

![014.jpg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-cable-pack/zh/014.jpg)

3. 参考 WIKI: [AMS 3H 自动进料组件上盖更换指南](replace-auto-filament-loader-cover.md)，安装好自动进料组件上盖。

![015.jpg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-cable-pack/zh/015.jpg)

4. 将 AMS 舱体底面朝上翻转放置，断开主板或接口板上的旧连接线并接入新线，随后严格沿原布线路径整理固定，确保线缆平整。

![016.jpg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-cable-pack/zh/016.jpg)

> 注意：
>
> 在所有入料口连接线缆中，H8 位置的连接线比其他 8 个位置的线缆要长约 40 CM，更换时，可以先对比一下，分出 H8 位置的连接线缆。
>
> ![017.jpg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-cable-pack/zh/017.jpg)

### 第 7 步 安装 AMS 主板/ 接口板装饰盖

检查线缆，确诊已整理好，然后装上 AMS 主板 装饰盖和接口板装饰盖，分别锁入螺丝固定。

|  |  |
| --- | --- |
| 018.jpg | 019.jpg |

### 第 8 步 移除 AMS 舱体

最后，请参考WIKI: [AMS 3H 舱体拆装指南](../../h3c/maintenance/replace-chamber.md)，将 AMS 舱体安装到 AMS 支架上。

## 功能验证

1. 连接打印机并启动，开机自检没有弹出错误提示框；
2. 更换了入料号组件线缆的，在该槽位上料，确认能正常检测耗材即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
