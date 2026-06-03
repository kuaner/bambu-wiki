---
path: zh/x1/troubleshooting/hmscode/troubleshooting
title: "HMS_0700_5000_0002_0001: AMS1 通信异常，请检查AMS的连接线。"
description: "AMS1 通信异常，请检查AMS的连接线。"
tags: ["ams", "p1", "x1"]
created: 2024-04-17T02:27:08.552Z
updated: 2026-05-20T08:38:32.028Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/hmscode/troubleshooting
---

# 这是什么

在AMS进料或打印机打印过程中，打印机无法识别到AMS。AMS的四个插槽LED灯都是红灯闪烁（如果AMS固件版本太老的话可能还是显示白灯）。同时，打印机操作界面上看不到AMS页面。

![](https://wiki.bambulab.com/ams_is_not_detected/ams_tab.png)

# 操作指导

**排故前请将打印机关机**

## 1. 检查Bambu Bus 4Pin及6Pin电缆接口松动

Bambu Bus 4Pin&6Pin电缆是连接打印机、缓冲器、AMS的两条线缆。线缆接头的松动可能导致AMS与打印机间通讯中断。重新插拔后，测试AMS能否被打印机识别。

## 2. Pin脚检查

检查Bambu Bus 4Pin&6Pin电缆（连接打印机—缓冲器—AMS的两条线缆）的Pin脚是否开路，如下图。

![](https://wiki.bambulab.com/ams_power_on_failure/pin_open.png)

## 2. 检查AMS内部线缆连接

- 检查AMS内部的总线线缆（Bus）是否松动或者脱落。

![](https://wiki.bambulab.com/ams_is_not_detected/bus_inside_ams.png)

- 同时建议稍微摇晃或弯曲4Pin和6Pin的插头和电缆，或者稍微拔出插头（不要完全拔出），看看AMS是否能在短时间内被打印机检测到，这样我们就可以把故障范围缩小到插头/电缆。

## 3. 电阻测量

如果你有万用表，确保4Pin和6Pin电缆正常地连接在机器上，然后用万用表测量AMS、打印机以及4Pin和6Pin线电阻**（打印机处于关机状态）。**

![](https://wiki.bambulab.com/ams_power_on_failure/ams_cable_pin_define.drawio.svg)

**X1C、P1P和P1S正常的电阻值如下（只连接一台AMS）**：

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **pin-pin** | **AMS** | **打印机接口** | **4pin线连接缓冲器** | **4pin线连接打印机** | **6pin线连接缓冲器** | **6pin线连接AMS** | **4pin线连接AMS Hub** | **6pin线连接AMS Hub** |
| GND-sigA | 4~5kΩ | 4~5kΩ | 4~5kΩ | 4~5kΩ | 4~5kΩ | 4~5kΩ | 2~2.5kΩ | 2~2.5kΩ |
| GND-sigB | 4~5kΩ | 4~5kΩ | 4~5kΩ | 4~5kΩ | 4~6kΩ | 4~6 kΩ | 2~2.5kΩ | 2~2.5kΩ |
| sigA-sigB | 8~10kΩ | 8~10kΩ | 8~10kΩ | 8~10kΩ | 8~10kΩ | 8~10kΩ | 4~5kΩ | 4~5kΩ |

**X1E正常的电阻值如下（只连接一台AMS）：**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **pin-pin** | **AMS接口** | **打印机接口** | **4pin线连接缓冲器** | **4pin线连打印机** | **6pin线连接缓冲器** | **6pin线连接AMS** | **4pin线连接AMS Hub** | **6pin线连接AMS Hub** |
| GND-sigA | 4~5kΩ | 2~2.5kΩ | 4~5kΩ | 2~2.5kΩ | 2~2.5kΩ | 4~5kΩ | 2~2.5kΩ | 2~2.5kΩ |
| GNS-sigB | 4~5kΩ | 2~2.5kΩ | 4~5kΩ | 2~2.5kΩ | 2~2.5kΩ | 4~5 kΩ | 2~2.5kΩ | 2~2.5kΩ |
| sigA-sigB | 8~10kΩ | 4~5kΩ | 8~10kΩ | 4~5kΩ | 4~5kΩ | 8~10kΩ | 4~5kΩ | 4~5kΩ |

### 测量打印机4Pin接口和4Pin线两端的电阻

先从打印机上断开4Pin线缆，测量打印机4Pin接口和4Pin线端子的电阻，如下图所示。

![](https://wiki.bambulab.com/ams_is_not_detected/测打印机4pin端口电阻.png)

**打印机4Pin接口正常的测量结果如下：**

|  |  |  |
| --- | --- | --- |
| **Pin-Pin** | **X1C/P1P/P1S** | **X1E** |
| GND-sigA | 4~5kΩ | 2~2.5kΩ |
| GND-sigB | 4~5kΩ | 2~2.5kΩ |
| sigA-sigB | 8~10kΩ | 4~5kΩ |

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-interface-board/350px-connector_ams-mc.png)
![](https://wiki.bambulab.com/ams_is_not_detected/4pin线端子.png)

**4pin线连接缓冲器正常的测量结果如下：**

|  |  |  |
| --- | --- | --- |
| **Pin-Pin** | **X1C/P1P/P1S** | **X1E** |
| GND-sigA | 4~5kΩ | 4~5kΩ |
| GND-sigB | 4~5kΩ | 4~5kΩ |
| sigA-sigB | 8~10kΩ | 8~10kΩ |

然后把4Pin线接回打印机，从缓冲器上拔掉4P线，继续测量另一端4Pin针脚之间的电阻**（把缓冲器从打印机上取下可以更容易拔出线缆）**。

![](https://wiki.bambulab.com/ams_is_not_detected/%E7%BC%93%E5%86%B2%E5%99%A8%E7%AB%AF4pin%E7%BA%BF%E7%AB%AF%E5%AD%90.png)

**4pin线连接打印机正常的测量结果如下：**

|  |  |  |
| --- | --- | --- |
| **Pin-Pin** | **X1C/P1P/P1S** | **X1E** |
| GND-sigA | 4~5kΩ | 2~2.5kΩ |
| GND-sigB | 4~5kΩ | 2~2.5kΩ |
| sigA-sigB | 8~10kΩ | 4~5kΩ |

### 测量AMS 6Pin接口和6Pin线两端的电阻

接着把4Pin线缆接回缓冲器，从AMS上拔掉6Pin线缆，测量AMS 6Pin接口的电阻(两个接口都一样)和6Pin线缆的电阻。

![](https://wiki.bambulab.com/ams_is_not_detected/测ams6pin接口电阻.png)

**AMS 6pin接口正常的测量结果如下：**

|  |  |  |
| --- | --- | --- |
| **Pin-Pin** | **X1C/P1P/P1S** | **X1E** |
| GND-sigA | 4~5kΩ | 4~5kΩ |
| GND-sigB | 4~5kΩ | 4~5kΩ |
| sigA-sigB | 8~10kΩ | 8~10kΩ |

![](https://wiki.bambulab.com/ams_is_not_detected/6pin线端子.png)

**6pin线连接缓冲器正常的测量结果如下：**

|  |  |  |
| --- | --- | --- |
| **Pin-Pin** | **X1C/P1P/P1S** | **X1E** |
| GND-sigA | 4~5kΩ | 2~2.5kΩ |
| GND-sigB | 4~5kΩ | 2~2.5kΩ |
| sigA-sigB | 8~10kΩ | 4~5kΩ |

再把6Pin线缆从缓冲器上拔出，测量6Pin线缆另一端的电阻**（把缓冲器从打印机上取下可以更容易拔出线缆）**。

![](https://wiki.bambulab.com/ams_is_not_detected/缓冲器端6pin线端子.png)

**6pin线连AMS正常的测量结果如下：**

|  |  |  |
| --- | --- | --- |
| **Pin-Pin** | **X1C/P1P/P1S** | **X1E** |
| GND-sigA | 4~5kΩ | 4~5kΩ |
| GND-sigB | 4~5kΩ | 4~5kΩ |
| sigA-sigB | 8~10kΩ | 8~10kΩ |

### 测量AMS主板和MC板的电阻

若在以上的步骤中测出异常的电阻值，则可以判断AMS/打印机/4&6pin线/缓冲器中是哪里出的故障导致AMS无法识别。

**AMS主板电阻的测量**

根据以上的测量结果，如果AMS的6pin接口的电阻异常，可以拆开AMS（可以参考[这篇wiki](../../maintenance/replace-ams-main-board.md)），进一步测量连接主板的总线(Bus)和电源(power)线缆接口的电阻，看是否是AMS主板故障：

![](https://wiki.bambulab.com/ams_is_not_detected/%E6%B5%8Bams%E4%B8%BB%E6%9D%BF%E7%94%B5%E9%98%BB.jpg)

**总线(Bus)和电源线(Power)正常的测量结果如下：**

|  |  |  |
| --- | --- | --- |
| **Pin-Pin** | **X1C/P1P/P1S** | **X1E** |
| GND-sigA | 4~5kΩ | 4~5kΩ |
| GND-sigB | 4~5kΩ | 4~5kΩ |
| sigA-sigB | 8~10kΩ | 8~10kΩ |

- 如果测量连接主板的总线(Bus)和电源(power)线缆接口的电阻正常，则可能是AMS电源板异常，需要更换电源板；
- 如果测量连接主板的总线(Bus)和电源(power)线缆接口的电阻异常，则可能是AMS主板异常。

**MC板电阻测量**

如果测量的打印机4pin接口的电阻异常，则有可能是AMS接口板或者是MC板的故障。可以拆开打印机后盖，拔掉AMS接口板上的6pin线（可以参考[这篇wiki](../../maintenance/replace-ams-interface-board.md)），测量连接MC板的6pin线电阻看是否是MC板故障：

![](https://wiki.bambulab.com/ams_is_not_detected/测量mc6pin线.jpeg)

**连接MC板的6pin线正常的测量结果如下：**

|  |  |  |
| --- | --- | --- |
| **Pin-Pin** | **X1C/P1P/P1S** | **X1E** |
| GND-sigA | 4~5kΩ | 4~5kΩ |
| GND-sigB | 4~5kΩ | 4~5kΩ |
| sigA-sigB | 8~10kΩ | 8~10kΩ |

- 如果测量连接MC板的6pin线电阻正常，则可能是AMS接口板异常，需要更换AMS接口板；
- 如果测量连接MC板的6pin线电阻异常，则可能是MC板异常，需要更换MC板；

对于X1E，如果以上测量的电阻均正常，请参考下图移除风道（左图），然后测量加热模块控制板上网线及AMS接口板接口的电阻（右图）：

|  |  |
| --- | --- |
|  |  |

加热模块控制板上网线及AMS接口板接口正常的测量结果如下：

|  |  |
| --- | --- |
| **Pin-Pin** | **X1E** |
| GND-sigA | 4~5kΩ |
| GND-sigB | 4~5kΩ |
| sigA-sigB | 8~10kΩ |

如果测得的电阻异常，则需要更换加热模块控制板。

### 备注

以上一共有8组电阻值数据，如下图所示。测得哪个部分的电阻值是异常的，说明这个部件是有故障的。请按照下图记录这几组测量的电阻值数据，并联系售后团队获取进一步的帮助。

![](https://wiki.bambulab.com/ams_is_not_detected/8组电阻值数据.png)

**记录测量电阻的表格可以参考如下：**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **pin-pin** | **AMS** | **打印机接口** | **4pin线连接缓冲器/AMS hub** | **4pin线连接打印机** | **6pin线连接缓冲器//AMS hub** | **6pin线连接AMS** | **MC板** | **AMS主板** |
| GND-sigA |  |  |  |  |  |  |  |  |
| GND-sigB |  |  |  |  |  |  |  |  |
| sigA-sigB |  |  |  |  |  |  |  |  |

## 错误信息

HMS\_0700\_5000\_0002\_0001：AMS1 通信异常，请检查AMS的连接线。

下面这些错误代码显示了不同力传感器的相同问题：

0700-5000-0002-0001

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您已经完成了上述的步骤，但问题仍然存在，**请录制一段视频，展示AMS及打印机上料或打印时的工作状态。**之后，请让打印机静置10分钟，**上传录制的视频、**[**并上传打印机的日志文件**](...md)**、附带电阻测量结果更佳。**最后，提交一个技术服务工单以便我们进行进一步的故障排查和修复问题。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
