---
path: zh/h3c/troubleshooting/h3c-circuit-troubleshooting-guide
title: "拓竹H3C 电路排查指南-设备无法开机工作"
description: ""
tags: []
created: 2026-11-03T12:08:46.904Z
updated: 2026-11-10T08:47:17.665Z
source: https://wiki.bambulab.com/zh/h3c/troubleshooting/h3c-circuit-troubleshooting-guide
---

## 介绍

当设备外部或内部供电异常时，设备将无法正常工作，因屏幕与软件均无法显示故障信息，此时需依据主板灯语来判断故障。本文将根据电源输入顺序，进行系统性排查。

## 所需工具

- H2.0 内六角扳手
- H1.5 内六角扳手
- 十字螺丝刀

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 故障排查过程中临时需要开机检查灯语，观察过程中请勿直接触碰裸露元器件。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 排查流程

设备无法上电的现象，通常会有两种可能性。

1. 市电输入设备时存在异常，如电源开关故障、电源线故障等。
2. 设备内部电源输出存在异常，如某一组件短路导致相连的主板或其他主板进入保护状态，暂停工作。

## 检查外部输入

### 检查开关

设备接上电源线并按下开关后，白色灯会自动亮起。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-01.png)

若此处白灯正常亮起，则参考本文末尾处的船型开关指示灯异常进行下一步检查。

## 检查内部输出

### 检查电源模块

从打印机后方出风口观察电源模块的绿色指示灯是否亮起。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-02.jpg)

若指示灯常亮，则进行后续检查。  
若指示灯熄灭，可能是电源模块出现故障，需[更换电源模块](../maintenance/replace-power-supply.md)。  
若指示灯闪烁，则电源模块可能工作正常。请参考[更换电源模块](../maintenance/replace-power-supply.md)，拆卸电源模块的输出线缆（1、2）后，开机观察指示灯是否常亮。若指示灯恢复常亮，则进行后续检查。

> 电源连接端子示意图如下，请根据电源上的标识和线缆颜色来连接。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-03.png)

| 序号 | 端子用途 | 线材颜色 | 序号 | 用途 | 线材颜色 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直流正极输出 | 白色 | 4 | 高压零线输入 | 蓝色 |
| 2 | 直流负极输出 | 黑色 | 5 | 高压火线输入 | 棕色 |
| 3 | 共用地线 | 黑色 （直流）/黄绿色（交流） | / |  |  |

### 检查 MC 板模块

#### 步骤 1. 拆卸背板和废料滑梯

参考[背板更换教程](../maintenance/replace-back-panel.md)，[废料滑梯更换教程](../maintenance/replace-purge-chute.md)，拆除背板和废料滑梯。

#### 步骤 2. 检查线缆连接

关机检查 MC 板上的线缆是否接好，避免连接器歪斜。若外观正常则进行下一步。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-04.png)

#### 步骤 3. 排查异常组件

关机后逐次取下 1、2、5、7、8/9、11、13 位置的连接器，每取下一个连接器后重新开机，观察指示灯状态。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-05.gif)

- 如果 1 连接器未接入的情况下，指示灯正常，说明右自适应风道组件异常，参考[右自适应风道组件更换指南](../maintenance/replace-adaptive-airflow-assembly-right.md)更换。
- 如果 8 连接器未接入的情况下，指示灯正常，说明后自适应风道及腔温组件异常。参考[后自适应风道及腔温组件更换指南](../maintenance/replace-adaptive-airflow-assembly-back.md)，拆除左后内衬，并更换转接板以及腔温组件。
- 如果 13 连接器未接入的情况下，指示灯正常，说明 AC 板异常。参考[AC板更换教程](../maintenance/replace-ac-board.md)更换 AC 板。
- 如果 2/7、5、11 连接器未接入的情况下，指示灯正常，说明 AP 板/打印头控制转接板或挂架控制板存在异常，请装回对应连接器后进行后续的排查。

如果以上 7 个连接器与故障无关，则按照相同方式逐一检查其他连接器，仅保留 10 号供电线正常连接。

- 若其余连接器均未接入时，灯语依然异常，则说明 MC 板本身存在故障，需参考[MC 板更换教程](../maintenance/replace-mc-board.md)更换 MC 板。
- 若取下某一组件连接器时，灯语恢复正常，则更换对应组件。  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-04.png)

> **MC 板连接器说明如下：**（红色 “X” 标识的两个连接器不可用，请忽略。 ）

| 序号 | 连接对象 | 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- | --- | --- |
| 1 | 背侧内衬转接板 | 7 | MC-AP （24 V 电源） | 14 | 空 |
| 2 | MC - AP 通信 1 | 8 / 9 | 右侧内衬转接板 | 15 | 热床 NTC |
| 3 | 空 | 10 | 电源（ 24 V 电源） | 16 | 热床通信 |
| 4 | 缓冲器/6 PIN 接口板 | 11 | 闪切挂架控制板 | X | X 电机 |
| 5 | 打印头控制转接板 | 12 | 电源散热风扇 | Y | Y 电机 |
| 6 | AP-MC 通信 2 | 13 | AC 板（通信） | Z | Z 电机 |

### 检查 AP 板模块

关机后参考 WIKI: [视窗更换指南](../maintenance/replace-side-glass-left.md)，移除左侧视窗。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-07.jpg)

用 H1.5 内六角扳手移除 2 颗螺丝，并取下导光板。注意需将导光板向上提，离开卡扣位置后再取下。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-08.jpg)

用 H1.5 内六角扳手移除 USB 线缆支架的螺丝，取下支架。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-09.jpg)

逐次断开 AP 板上的 2、5、6、7、8、9 连接器，仅保留 MC-AP 线缆以及 WIFI 天线。

> 6 号插头为选配俯视摄像头，若未加装，则该插孔为空。

![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-10.jpg)

开机观察 AP 板的指示灯是否正常。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-11.gif)

- 如果 2、6、7、8、9 中某个连接器被取下后，AP 板指示灯恢复正常，则更换对应模块即可。
- 如果 5 号连接器被取下后， AP 指示灯恢复正常，则需要装回 5 号连接器，排查 TH 板模块。

> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-10.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | MC -AP 通信 2 | 6 | 俯视摄像头（选配） |
| 2 | 左补光灯 | 7 | 腔温传感器 |
| 3 | MC -AP 通信 1 | 8 | 实况摄像头 |
| 4 | MC - AP (24 V 电源线) | 9 | 屏幕 |
| 5 | 工具头 （USB 线） | 10 | WIFI 天线 |

### 检查 TH 板模块

#### 步骤1：拆开工具头外壳

关机状态下参考[工具头外壳更换指南](../maintenance/replace-toolhead-front-cover.md)拆卸工具头外壳。

#### 步骤2：观察 TH 板指示灯

重新通电开机。下图中 TH 板上两颗常亮的绿色 LED 灯为供电指示灯，若开机后两颗常亮指示灯熄灭，说明 TH 板供电存在异常。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-13.gif)

关机后逐次拆卸 1 至 5 号线缆连接器，并再次开机观察指示灯。

> 部分连接器需提前撬开黑色压块。

![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-14.png)

- 若 3、4、5 中某一连接器拔下后，灯语恢复正常，则说明对应组件存在故障，更换该组件即可。
- 若 1/2 同时拔下后，灯语恢复正常，说明 TH 转接板存在故障，请装回线缆并进行后续排查。
- 若所有连接器均拔下后，指示灯依旧异常，则需要更换 TH 板；

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | 挤出接口板 1 | 4 | 部件冷却风扇 |
| 2 | 挤出接口板 2 | 5 | 工具头摄像头 |
| 3 | 2521 挤出电机 | 6 | AP 板 （USB-C） |

开机观察 TH 接口板的指示灯状态，正常状态下两个指示灯均常亮。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-15.png)

若指示灯异常，请关机后重新连接 9、8 连接器，完成后再次开机观察指示灯状态。  
若重装 9、8 后报错依旧，则关机后依次拔掉 1 至 7 连接器，每取下一个连接器都需要开机观察指示灯。当拔掉某个连接器后指示灯恢复正常，说明该模块存在故障，更换该组件即可。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-16.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | **泊位标定传感器** | 6 | 2012 锁紧电机 |
| 2 | 裹头检测传感器 | 7 | 2012 变距电机 |
| 3 | 工具识别传感器 | 8 | TH 板 1 |
| 4 | 热端风扇 | 9 | TH 板 2 |
| 5 | 涡流线圈 | / | / |

### 打印头控制板模块外设供电异常

请参考WIKI: [AMS 3H 舱体拆装指南](../maintenance/replace-chamber.md)，完成将 AMS 舱体从AMS 支架上移除和安装的操作。

- 步骤 1：拔下挂架的 9 个打印头 4-pin 线缆，以及右侧的挂架散热风扇接头。  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-17.png)
- 步骤 2：开机观察指示灯状态。  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-18.gif)
- 步骤 3：若指示灯均正常，则关机后逐个安装拔下的连接器，每次安装都需要开机重新观察报错，当某一连接器装上后故障出现，则更换该组件即可。  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-19.jpg)

#### 挂架模块外设供电异常

1. 用H2.0六角扳手拆掉打印机右侧的四颗螺丝  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-20.png)
2. 用手从机箱内部用力推动将侧板拆下  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-21.png)
3. 关机状态下依次拔掉挂架板上的 1/2/3/4/5/6/8 连接器，每拔下一个连接器都需要重新开机，观察指示灯。  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-22.gif)

- 若拔下某一连接器后指示灯恢复正常，则是相应组件故障，更换该组件即可。
- 若报错无法消除，则是挂架板异常，需[更换挂架板](../maintenance/replace-swaptek-rack-control-board.md)。  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-23.jpg)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | **挂架升降电机** | 5 | 开门检测传感器 |
| 2 | 挂架防撞霍尔传感器 | 6 | 右LED灯条 |
| 3 | 腔温传感器 | 7 | MC 板 |
| 4 | 挂架校准传感器 | 8 | 打印头控制转接板 （风扇） |

## 船型开关指示灯异常解决方案

如果觉得这一步操作有点难度，也可以选择联系客服或直接[更换电源开关](../maintenance/replace-power-socket.md)，跳过保险丝的测试环节。  
若此处白灯无法点亮，可能会是电源线故障、保险丝烧毁或开关故障。建议先更换其他最大通过电流为 10A 的电源线。若故障依旧，再拔下电源线，从开关中撬开保险丝安装座，取出保险丝。

|  |  |
| --- | --- |
| 图 | 图 |

测试保险丝功能是否正常，若保险丝出现故障，可更换新的电源开关。

- 如果您的手机支持**多点触碰**，那么屏幕类型为“电容屏”。您就可以用手指捏住保险丝的一端，使用另一端触碰手机屏幕，观察屏幕是否能够被点击。如果可以的话那么保险丝就是正常的。  
  ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/h3c-circuit-troubleshooting-guide/zh/02_h3c_______-________-26.webp)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
