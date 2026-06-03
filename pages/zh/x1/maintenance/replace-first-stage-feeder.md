---
path: zh/x1/maintenance/replace-first-stage-feeder
title: "更换AMS上下料组件"
description: ""
tags: []
created: 2022-08-01T02:58:49.938Z
updated: 2026-04-21T08:58:33.522Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-first-stage-feeder
---

## 什么是上下料组件

上下料组件安装在AMS上为并AMS提供第一阶驱动力的供料装置，一个AMS中有4个上下料组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/429px-first_stage_feeder1.png)

## 何时更换

出现齿轮错误或内部有可见损坏，或者检测开关工作不稳定时。

## 所需工具和材料

AMS上下料组件

H2.0 内六角扳手

## 开始操作前的安全警告和机器状态

关闭打印机电源并断开AMS 与打印机的连接。

## 操作指南

### **第 1 步 -** (拆卸) 拆除PTFE管

打开AMS上盖，按压AMS 五通组件上的按钮（解锁快速接头），然后从AMS背面拉出PTFE管。

|  |  |
| --- | --- |

### **第 2 步 -** 移除螺丝

移除固定AMS主框架上2颗螺丝（BT3×8）。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/611px-remove_2_screw.png)

### **第 3 步 -** 移除AMS主框架组件

向上翻转中间框架组件，断开bambu总线电缆和电源电缆，移除AMS主框架组件。

|  |  |
| --- | --- |

### **第 4 步 - 移除AMS主框架主动支撑套筒组件**

拆下需要更换上下料器对应位置上的AMS主框架主动支撑套筒组件 。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/408px-remove_the_ams_driving_sleeve_unit.png)

### **第 5 步 - 断开电缆和PTFE管**

断开对应上下料号的电缆与主板的连接，以及对应上下料号的PTFE 管与AMS五通组件的连接。例如，如果要更换料槽 1 中的上下料器，则断开相对应位置的电缆和PTFE管。

|  |  |
| --- | --- |

### **第 6 步 - 移除上下料**组件

根据需要更换的上下料组件，拆下 对应位置的4 颗固定螺丝（BT2×8），按压上下料器的两侧解锁上下料组件并将其取下。

|  |  |
| --- | --- |

### **第 7 步 - 移除** PTFE 管

按下快速接头按钮，将PTFE 管从上下料组件上取下。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/376px-press.png)

### **第 8 步 -**（组装）连接 PTFE 管

将从旧的上下料组件上取下的PTFE 管连接到新的上下料组件上。

*（注：槽 1&4 的料管长度为 230mm；槽 2&3 的料管长度为 195mm）。*

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/404px-connect_ptfe_tube.png)

### **第 9 步 - 安装上下料**组件

将电缆和PTFE管穿过安装位置上的孔，将上下料组件安装到位，锁入4颗螺丝（BT2×8）固定。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### **第 10 步 -** 连接电缆和 PTFE 管

连接电缆和 PTFE 管。将电缆连接到主板对应的连接器，将 PTFE 管连接到AMS五通组件对应的接口。

|  |  |
| --- | --- |

### **第 11 步 -** 安装 **AMS主框架主动支撑套筒组件**

安装 AMS主框架主动支撑套筒组件，注意对齐齿轮位置，防止装反。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/375px-install_the_drivig_gear_uiit.png)

### **第 12 步 -** 安装AMS主框架组件

将AMS主框架组件装入AMS外壳，并将Bambu总线电缆和电源电缆连接到AMS电源板。

|  |  |
| --- | --- |

### **第 13 步 -** 固定AMS主框架组件

如下图所示，将AMS主框架安装到位，用2颗螺丝（BT3×8）固定AMS主框架组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/524px-remove_2_screw.png)

### **第 14 步 -** 连接PTFE管

检查确认PTFE管硅胶支架与五通组件的料孔对齐，并从AMS后部推入PTFE管。装完后，拉动PTFE管，确认PTFE管已固定。

|  |  |
| --- | --- |

## 如何验证完成/成功

将 AMS 连接到打印机并打开电源。将材料装载到您更换了上下料器的料槽上，单击屏幕上的“进料”开始加载打印丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/494px-load1.png)

这里以更换料槽1的上下料器为例

进料完成后，再单击“退料”开始退打印丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/557px-unload_filament.png)

重复以上操作3次，如果所有功能OK，则更换完成并成功。

否则，请检查电缆和料管的连接后重试，如果没有发现异常但仍存在故障，请联系服务团队寻求解决方案。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
