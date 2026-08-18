---
path: zh/a1/maintenance/replace-hotend
title: "更换A1热端"
description: "本文介绍了如何更换 A1 热端"
tags: []
created: 2025-07-29T09:31:50.925Z
updated: 2026-08-03T10:40:39.457Z
source: https://wiki.bambulab.com/zh/a1/maintenance/replace-hotend
---

## 热端

热端安装在工具头上，可用于挤出耗材。对于 A1 打印机，我们提供了 0.2、0.4、0.6 和 0.8mm 四种直径的热端，您可以根据需求来选择。

> **📌 注意**：若您更换了不同规格的喷嘴，请在发起打印前务必在**屏幕上**同步喷嘴信息。

![热端.jpg](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%83%AD%E7%AB%AF.jpg)

### 何时更换

- 热端堵塞
- 热端损坏

### 所需的工具和材料

- 新的热端组件

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## Bambu Studio 软件设置提示

在最新版本的 Bambu Studio（Bambu\_Studio\_win\_public-v02.01.01.52-20250616155614）中，我们已禁用“打印机零件”页面中的喷嘴信息修改功能（在软件中的位置如下图所示），仅保留展示用途。部分用户可能因操作习惯变化误认为是软件或设备故障。此次调整旨在提升操作一致性与使用安全——喷嘴更换必须在打印机上完成，若允许通过软件远程修改，易导致新手误解为无需实际更换即可打印。

![ch_喷嘴设置.jpg](https://wiki.bambulab.com/h2/maintenance/replace-hotend/ch_%E5%96%B7%E5%98%B4%E8%AE%BE%E7%BD%AE.jpg)

## 移除热端步骤

> 如果是上料状态，请使用切刀手动切断料线。

1. 得益于卡扣式的设计，我们可以很快的的更换喷嘴组件。首先，我们需要按下右侧的切刀刀柄切断耗材，确保喷嘴顶部的耗材是断开的状态。

![第一步.png](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E4%B8%80%E6%AD%A5.png)

2. 接下来，从右侧底部轻轻上抬取下前盖。

![第二步.png](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E4%BA%8C%E6%AD%A5.png)

3. 继续移除喷嘴保温硅胶套。

![第三步.gif](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E4%B8%89%E6%AD%A5.gif)

4. 将卡扣向右侧推，打开卡扣，为了方便操作可以找一小段耗材辅助，将卡扣铁片向外推，完全露出喷嘴组件。

![第四步.gif](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E5%9B%9B%E6%AD%A5.gif)

5. 捏住散热鳍片的位置，缓慢取出喷嘴组件。

![第五步.gif](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E4%BA%94%E6%AD%A5.gif)

> 📌 喷嘴可能会因残留物而难以取下，这时可以先适当加热，再使用镊子或螺丝刀轻轻撬动，佩戴隔热手套后取下热端。热端取下后，使用钳子或剪刀剪断热端顶部残留耗材，避免影响后续安装。  
> ![左喷嘴.webp](https://wiki.bambulab.com/h2/maintenance/replace-hotend/%E5%B7%A6%E5%96%B7%E5%98%B4.webp)

## 安装热端步骤

1. 接下来，我们安装新的喷嘴组件，有一些细节是比较重要的，我们可以一步步完成这个过程。

将喷嘴组件的散热鳍片向后方倾斜一定角度放入，内部的磁铁会吸附在螺丝上辅助归位，我们需要确保喷嘴组件和加热组件完全贴合。

![第六步.gif](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E5%85%AD%E6%AD%A5.gif)

2. 重新推回卡扣，锁紧喷嘴组件。

![中间步骤.gif](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E4%B8%AD%E9%97%B4%E6%AD%A5%E9%AA%A4.gif)

> 注意：如果锁紧卡扣的时候感觉比较困难，您需要再次检查，确保卡扣锁紧位置和下图保持一致。

![第七步.png](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E4%B8%83%E6%AD%A5.png)

3. 完成之后，继续安装喷嘴硅胶套，要确保喷嘴组件尖端有正确露出。

![第八步.gif](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E5%85%AB%E6%AD%A5.gif)

4. 最后，将前盖上方凸出的位置对齐工具头凹槽，然后按压底部的位置，直到会听到“咔嚓”声，安装就完成了。

![第九步.gif](https://wiki.bambulab.com/a1/maintenance/replace-hotend/%E7%AC%AC%E4%B9%9D%E6%AD%A5.gif)

## 在设备上同步喷嘴信息

若您更换了其他直径或者其他材质的热端，请在发起新的打印任务前务必在屏幕上更新喷嘴信息，参考下图：  
点击面板上的**设置→维护→喷嘴**，即可修改。

![a1-喷嘴.jpg](https://wiki.bambulab.com/a1/maintenance/replace-hotend/a1-%E5%96%B7%E5%98%B4.jpg)

## Bambu Studio 软件设置提示

在最新版本的 Bambu Studio（v02.01.01.52或之后版本）中，我们已禁用“打印机零件”页面中的喷嘴信息修改功能（在软件中的位置如下图所示），仅保留展示用途。部分用户可能因操作习惯变化误认为是软件或设备故障。此次调整旨在提升操作一致性与使用安全——喷嘴更换必须在打印机上完成，若允许通过软件远程修改，易导致新手误解为无需实际更换即可打印。

![ch_喷嘴设置.jpg](https://wiki.bambulab.com/h2/maintenance/replace-hotend/ch_%E5%96%B7%E5%98%B4%E8%AE%BE%E7%BD%AE.jpg)

## 如何验证成功

热端无松动，能够正常挤出即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
