---
path: zh/x1e/maintenance/printer-cables
title: "更换 X1E 线材包"
description: "本文将介绍如何更换 X1E 线材包中的线缆。"
tags: ["x1e"]
created: 2026-04-21T10:47:27.724Z
updated: 2026-04-22T04:11:50.134Z
source: https://wiki.bambulab.com/zh/x1e/maintenance/printer-cables
---

X1E 的单独线材包主要包含如下 4 根线缆（从左到右）。

1. 接口板(AMS 接口和网口)到网卡的连接线；

2. 电源模块温度传感器(NTC)

3. 接口板(AMS 接口和网口)到 MC 控制板连接线；

4. 接口板(AMS 接口和网口)到加热模块连接线；

![4.jpg](https://wiki.bambulab.com/x1e/printer-cables/4.jpg)

## 何时更换

- 两端的插头有物料损坏，影响安装；
- 连接线有明显的损伤或断路；
- 拓竹服务团队通过日志文件确认的连接线有异常。

## 工具

- X1E 线材包
- H2.0/H1.5 内六角扳手
- 镊子

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 操作步骤

### 移除背板

用 H2.0 内六角扳手移除 9 颗红色标记螺丝，4 颗橙色标记螺丝，1 颗深蓝色标记螺丝，妥善分开存放。

![](https://wiki.bambulab.com/x1/maintenance/x1e/rear_panel_screws_2.jpg)

先将背板向右推动少许，从右侧张紧器处松出。

![](https://wiki.bambulab.com/x1/maintenance/x1e/power-supply/remove_rear_panel_1.jpg)

然后向左用力，将背板从左侧张紧器处松出，取下后面板。

![](https://wiki.bambulab.com/x1/maintenance/x1e/power-supply/remove_rear_panel_2.jpg)

### 移除接口板

使用 H2.0 内六角扳手拧下图中标记的 3 个螺丝。

![3.jpg](https://wiki.bambulab.com/x1e/printer-cables/3.jpg)  
然后断开接口板上的线缆接头，注意每个接头的顶部都有防松卡扣，需按压卡扣才能拔下插头。

![1.jpg](https://wiki.bambulab.com/x1e/printer-cables/1.jpg)

### 移除加热模块接头

用 H2.0 内六角扳手移除 3 颗螺丝，取下风道。

![2.jpg](https://wiki.bambulab.com/x1e/printer-cables/2.jpg)  
断开加热模块上这三个线缆插头。

1. 电源风扇
2. 电源温度传感器
3. 接口板-电源模块线缆

![加热模块接头定义.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%8A%A0%E7%83%AD%E6%A8%A1%E5%9D%97%E6%8E%A5%E5%A4%B4%E5%AE%9A%E4%B9%89.jpg)

### 更换接口板- MC 板线缆

![线缆_9.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%BA%BF%E7%BC%86_9.jpg)  
按压 MC 板上图示插头的顶部卡扣，取下该插头。

![mc.jpg](https://wiki.bambulab.com/x1e/printer-cables/mc.jpg)

将新的线缆安装在 MC 板上。

![amscom.jpg](https://wiki.bambulab.com/x1e/printer-cables/amscom.jpg)

### 更换接口板-加热模块线缆

![线缆_11.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%BA%BF%E7%BC%86_11.jpg)  
从理线扣中完整抽出接口板-加热模块线缆

![理线槽.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%90%86%E7%BA%BF%E6%A7%BD.jpg)

将新线缆的一端插头安装在加热模块 3 号插座上。

![加热模块接头定义.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%8A%A0%E7%83%AD%E6%A8%A1%E5%9D%97%E6%8E%A5%E5%A4%B4%E5%AE%9A%E4%B9%89.jpg)

再将线缆塞入理线扣中。

![理线槽.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%90%86%E7%BA%BF%E6%A7%BD.jpg)

### 更换接口板-网卡线缆

![线缆_8.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%BA%BF%E7%BC%86_8.jpg)  
使用 H1.5 内六角扳手移除进料口附近的 1 颗固定螺丝。

![进料口固定螺丝.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E8%BF%9B%E6%96%99%E5%8F%A3%E5%9B%BA%E5%AE%9A%E8%9E%BA%E4%B8%9D.jpg)

用力将盖板拉出。

![拔出ap盖板.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E6%8B%94%E5%87%BAap%E7%9B%96%E6%9D%BF.jpg)

从 AP 板的网卡上断开线缆接头。

![网卡线缆.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%BD%91%E5%8D%A1%E7%BA%BF%E7%BC%86.jpg)

撕开包裹所有线缆的醋酸胶布。

![撕开醋酸胶布.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E6%92%95%E5%BC%80%E9%86%8B%E9%85%B8%E8%83%B6%E5%B8%83.jpg)  
单独取出网卡-接口板线缆，并从走线孔中完全抽出。

![穿过理线槽2.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%A9%BF%E8%BF%87%E7%90%86%E7%BA%BF%E6%A7%BD2.jpg)  
![取出网卡-接口板线缆.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%8F%96%E5%87%BA%E7%BD%91%E5%8D%A1-%E6%8E%A5%E5%8F%A3%E6%9D%BF%E7%BA%BF%E7%BC%86.jpg)

取出新线缆，并将接头接上网卡。

![安装新线缆.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%AE%89%E8%A3%85%E6%96%B0%E7%BA%BF%E7%BC%86.jpg)

将线缆塞入理线扣中。

![穿过理线槽2.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%A9%BF%E8%BF%87%E7%90%86%E7%BA%BF%E6%A7%BD2.jpg)  
剩余线缆塞入电机侧面的走线孔，送达 MC 板附近。

![插入走线孔.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E6%8F%92%E5%85%A5%E8%B5%B0%E7%BA%BF%E5%AD%94.jpg)  
![穿过离线槽.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%A9%BF%E8%BF%87%E7%A6%BB%E7%BA%BF%E6%A7%BD.jpg)  
![mc板位置抽出.jpg](https://wiki.bambulab.com/x1e/printer-cables/mc%E6%9D%BF%E4%BD%8D%E7%BD%AE%E6%8A%BD%E5%87%BA.jpg)

最终将剩余的 3 个线缆都安装在接口板上。

![cables.jpg](https://wiki.bambulab.com/x1e/printer-cables/cables.jpg)  
![接口板.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E6%8E%A5%E5%8F%A3%E6%9D%BF.jpg)

### 更换电源温度传感器

![线缆_10.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%BA%BF%E7%BC%86_10.jpg)  
使用 H1.5 内六角扳手移除 7 颗螺丝，取下电源保护盖。

![电源保护盖.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%94%B5%E6%BA%90%E4%BF%9D%E6%8A%A4%E7%9B%96.jpg)

撕开电源模块侧边的醋酸胶布，取出 NTC 线缆。

![取出旧ntc.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%8F%96%E5%87%BA%E6%97%A7ntc.jpg)

撕开黄色高温胶布，取出旧温度传感器探头。

![取出旧ntc探头.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%8F%96%E5%87%BA%E6%97%A7ntc%E6%8E%A2%E5%A4%B4.jpg)

从理线扣中完全抽出旧温度传感器。

![理线槽.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%90%86%E7%BA%BF%E6%A7%BD.jpg)

将新温度传感器探头粘贴在原本位置，若黄色高温胶布失去粘性，可裁剪一段线材包中的醋酸胶布固定。

![粘贴新探头1.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%B2%98%E8%B4%B4%E6%96%B0%E6%8E%A2%E5%A4%B41.jpg)  
![额外的醋酸胶布.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E9%A2%9D%E5%A4%96%E7%9A%84%E9%86%8B%E9%85%B8%E8%83%B6%E5%B8%83.jpg)  
![粘贴新探头.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%B2%98%E8%B4%B4%E6%96%B0%E6%8E%A2%E5%A4%B4.jpg)

找到线缆上带有标签的位置，沿着图中电源模块的侧边折返一段，然后用醋酸胶布固定。

![弯折ntc线缆.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%BC%AF%E6%8A%98ntc%E7%BA%BF%E7%BC%86.jpg)  
![贴醋酸胶布.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E8%B4%B4%E9%86%8B%E9%85%B8%E8%83%B6%E5%B8%83.jpg)

剩余线缆装入理线扣中。

![理线槽.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%90%86%E7%BA%BF%E6%A7%BD.jpg)

最后将接头安装到加热模块的 2 号插座上。

![加热模块接头定义.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%8A%A0%E7%83%AD%E6%A8%A1%E5%9D%97%E6%8E%A5%E5%A4%B4%E5%AE%9A%E4%B9%89.jpg)

### 安装电源保护壳和接口板

使用 H1.5 内六角扳手装回电源保护盖的 7 颗螺丝。

![电源保护盖.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E7%94%B5%E6%BA%90%E4%BF%9D%E6%8A%A4%E7%9B%96.jpg)

再装回接口板。

![安装接口板.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%AE%89%E8%A3%85%E6%8E%A5%E5%8F%A3%E6%9D%BF.jpg)

### 安装仓温风扇风道和背板

装回 1 号电源风扇插头

![加热模块接头定义.jpg](https://wiki.bambulab.com/x1e/printer-cables/%E5%8A%A0%E7%83%AD%E6%A8%A1%E5%9D%97%E6%8E%A5%E5%A4%B4%E5%AE%9A%E4%B9%89.jpg)

再用 H2.0 内六角扳手安装 3 颗螺丝，固定风道。

![2.jpg](https://wiki.bambulab.com/x1e/printer-cables/2.jpg)

最后按照标记安装 9 颗红色标记螺丝，4 颗橙色标记螺丝，1 颗深蓝色标记螺丝。

![](https://wiki.bambulab.com/x1/maintenance/x1e/rear_panel_screws_2.jpg)

## 设备校准

确保热床上没有任何模型或耗材碎屑，然后点击屏幕上的设置菜单，进入校准页面开始校准。

![cali1.png](https://wiki.bambulab.com/x1e/printer-cables/cali1.png)

如果一切正常，并且在校准过程中没有出现错误或警告，则更换成功。否则，请检查连接并重试。如果问题仍然存在，请联系服务团队寻求进一步帮助。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
