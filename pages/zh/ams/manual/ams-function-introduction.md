---
path: zh/ams/manual/ams-function-introduction
title: "AMS 主要功能和工作流程介绍"
description: ""
tags: []
created: 2023-04-20T11:38:20.070Z
updated: 2025-05-16T01:39:46.876Z
source: https://wiki.bambulab.com/zh/ams/manual/ams-function-introduction
---

本文将介绍 AMS各组件的一些基本工作原理、主要功能和工作流程。

## **AMS 供料系统介绍**

AMS供料系统主要分为以下两大模块：

**1.上下料器+五通+供料缓冲器**

**2.挤出机（切刀传感器+耗材检测传感器）**

![](https://wiki.bambulab.com/ams/ams-function-introduction/ams%E4%BE%9B%E6%96%99%E7%B3%BB%E7%BB%9F%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

**AMS供料路径示意图**

上下料器和五通能够检测耗材并负责进料和退料，缓冲器反馈信号给AMS和打印机来控制送料的速度。挤出机内部有切刀传感器和耗材检测传感器，同样会反馈传感器信号给AMS来判断能否正常送料。简单来说，AMS和打印机是依靠各个传感器的信号反馈来进行交互的，确保整个供料过程顺畅。

### 上下料器

AMS上有4个上下料器，也叫第一阶段进料器，负责把耗材拉入到AMS内部。退料的时候它也会驱动退料轴转动料盘进行退料。

上下料器有个耗材检测传感器，当检测到插入耗材丝后它的电机会开始工作，自动拉入耗材进行预上料。检测传感器的位置如下图：

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E4%B8%8A%E4%B8%8B%E6%96%99%E6%A3%80%E6%B5%8B%E5%BC%80%E5%85%B3%E4%BD%8D%E7%BD%AE.png)

### 五通

五通位于 AMS 的尾部，由四个传感器、一个里程轮和一个无刷电机组成。 它将四个送料路径合并为一个。 传感器检测到耗材从上下料器进入五通内部后，激活无刷电机为耗材提供第二级驱动力将其送至挤出机。

![](https://wiki.bambulab.com/x1/manual/intro-ams/filament-hub.jpg)

五通的耗材检测传感器和里程轮位置如下图所示，当耗材进出五通的时候，传感器的信号会发生变化，以此来判断耗材是否送入到五通。五通内部结构可以参考：[拆解和清洁AMS五通组件 | Bambu Lab Wiki](../../x1/troubleshooting/clean-the-filaments-hub.md)

**里程轮**用来判断耗材丝是否从AMS中被送出，也可以用来计算送的耗材丝长度。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E4%BA%94%E9%80%9A%E9%9C%8D%E5%B0%94%E4%BC%A0%E6%84%9F%E5%99%A8%E5%92%8C%E9%87%8C%E7%A8%8B%E8%BD%AE.png)

**霍尔传感器和里程轮**

### 缓冲器（AMS集线器）

在AMS和打印机之间会用到缓冲器（连接多台AMS的情况下会用到AMS集线器）， 它由滑块、弹簧和传感器组成。AMS将耗材推入工具头挤出机时，送入耗材的压力会推动滑块向右移动，并存储一小段耗材在缓冲器内。当挤出机消耗缓冲器内的耗材后滑块会退回到左侧。通过传感器检测滑块所在的位置，并反馈回 AMS 和打印机，进而调整送料的速度。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E7%BC%93%E5%86%B2%E5%99%A8%E6%BB%91%E5%9D%97%E7%A7%BB%E5%8A%A8.png)

### **挤出机**

挤出机用于打印中挤出耗材丝，它的内部有耗材检测开关和切刀检测开关，位置如下图所示：

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E6%8C%A4%E5%87%BA%E6%9C%BA%E9%9C%8D%E5%B0%94%E4%BC%A0%E6%84%9F%E5%99%A8%E4%BD%8D%E7%BD%AE.jpeg)

#### 耗材检测开关

耗材丝检测开关如下图所示，由磁铁和霍尔传感器组成。当耗材丝插入时，磁铁会靠近霍尔传感器，当没有耗材丝时，磁体会自动弹回。打印机根据检测到的霍尔值来判断挤出机内部是否有料。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E7%A9%BA%E9%97%B2%E5%92%8C%E6%9C%89%E6%96%99%E7%8A%B6%E6%80%81%E5%AF%B9%E6%AF%94.png)

**耗材丝插入后会推动磁铁靠近传感器**

当检测到挤出机内有耗材时，屏幕上的这个圆点会变成绿色：

![小绿点.jpg](https://wiki.bambulab.com/screen-operation/%E5%B0%8F%E7%BB%BF%E7%82%B9.jpg)

### 切刀检测传感器

切刀霍尔传感器如下图所示。切刀的刀柄上有一块磁铁。当切刀切料时，磁铁会靠近霍尔传感器；切料完成后，切刀会弹回，整个过程霍尔值会有变化。根据检测到的霍尔值，打印机可以判断切刀是否卡住，以及切料是否成功。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E5%88%87%E5%88%80%E7%A3%81%E9%93%81%E4%BD%8D%E7%BD%AE.png)  
![](https://wiki.bambulab.com/ams/ams-function-introduction/%E6%8C%A4%E5%87%BA%E6%9C%BA%E5%88%87%E5%88%80%E9%9C%8D%E5%B0%94%E4%BC%A0%E6%84%9F%E5%99%A8.png)

## **AMS 功能介绍**

### 预上料

**在AMS空闲状态时，插入耗材丝到上下器后，上下料器会把耗材丝送入到五通，直到被五通传感器检测到后再拉回，这个过程就是预上料。** 预上料除了提供给用户插料时候的交互反馈，还可以绷紧料盘上的耗材，确保料盘上的耗材丝不是松散的。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E9%A2%84%E4%B8%8A%E6%96%99.gif)

**插入辅助功能**：预上料之前，也可以点击屏幕上的空槽处，上下料器的电机和齿轮会开始转动，可以通过助力辅助更容易地插入耗材丝。

![empty-cn.jpg](https://wiki.bambulab.com/ams/ams-function-introduction/empty-cn.jpg)  
![kongpan.webp](https://wiki.bambulab.com/ams/ams-function-introduction/kongpan.webp)

### 读取RFID

Bambu官方的耗材卷的两侧都有RFID标签，在AMS上有两个读取RFID的电路板可以读取耗材信息。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E8%AF%BB%E5%8F%96rfid.png)

读取RFID功能可以在屏幕上设置为插入时/开机时检测。如果启用了“插入时检测”，则在预上料后就会进行RFID读取操作。同理，启用了“开机时检测”，在每次重启打印机后，它也会依次开始读取每个槽的RFID。

![插入耗材时读取.jpg](https://wiki.bambulab.com/screen-operation/%E6%8F%92%E5%85%A5%E8%80%97%E6%9D%90%E6%97%B6%E8%AF%BB%E5%8F%96.jpg)

您也可以手动在切片软件上点击每个槽位上方的图标进行RFID读取。

![studio-rfid-cn.png](https://wiki.bambulab.com/screen-operation/studio-rfid-cn.png)

**重读RFID**

选中耗材，点击**重读**，即可重读 RFID。  
![重读.jpg](https://wiki.bambulab.com/screen-operation/%E9%87%8D%E8%AF%BB.jpg)

**读取RFID时，AMS会先进行预上料绷紧料线。然后再把耗材送出AMS一段来转动料盘，让RFID标签扫过电路板读取RFID信息。**

![重读.webp](https://wiki.bambulab.com/screen-operation/%E9%87%8D%E8%AF%BB.webp)

当有某个槽的料线已经被送出AMS，或者挤出机检测到内部有料，此时无法使用读取RFID功能，点击读取会显示AMS忙碌无法读取料线信息。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E6%96%99%E5%B7%B2%E5%8A%A0%E8%BD%BD%E5%88%B0%E5%B7%A5%E5%85%B7%E5%A4%B4%E6%97%A0%E6%B3%95%E8%AF%BB%E5%8F%96rfid.png)

### 余料估算

读取RFID 过程同时可以对料卷进行余料估算，其工作原理是通过料盘上的RFID标签转动一圈后送出的耗材丝长度来估算料盘上剩余耗材丝的百分比，**默认完整1kg的料卷为100%。** 若启用了余料估算功能，则读取RFID的过程会进行两次，第一次读取耗材信息，第二次估算剩余容量。

![剩余容量估计.jpg](https://wiki.bambulab.com/screen-operation/%E5%89%A9%E4%BD%99%E5%AE%B9%E9%87%8F%E4%BC%B0%E8%AE%A1.jpg)

耗材类型下方的小横条显示的就是估算出来的耗材余量。  
![剩余容量cn.jpg](https://wiki.bambulab.com/screen-operation/%E5%89%A9%E4%BD%99%E5%AE%B9%E9%87%8Fcn.jpg)

对P1系列用户，在启用了“更新剩余容量”功能之后，可以在Bambu Studio或者Bambu Handy的页面查看它。

### 自动映射功能

在发起多色打印任务时，会自动给模型匹配AMS上最接近颜色的耗材丝。您也可以在发送打印任务的窗口里自定义选择耗材丝。

![自动分配颜色1.png](https://wiki.bambulab.com/screen-operation/%E8%87%AA%E5%8A%A8%E5%88%86%E9%85%8D%E9%A2%9C%E8%89%B21.png)

### 断料检测和自动续料功能

使用AMS打印依然具备断料检测功能，不过分为以下两种情况：

1. **单材料打印**：跟单打印机打印断料检测逻辑一样，工具头检测到没料后，就会报材料用尽，需要插入新的耗材。
2. **多材料打印**：多材料打印有一种特殊情况，即最后一段耗材已经脱离料盘送入到AMS内部，此时如果打印中途需要更换耗材，由于耗材丝已经脱离料盘无法拉回，会直接冲刷剩余的料，冲刷完毕后再切换到另一个槽的材料继续打印。屏幕会提示料线用尽，正在冲刷旧料。
3. **AMS 自动续料**：AMS上某个槽的耗材用尽后可以自动切换到其他槽位上属性完全相同的耗材。

   - 该功能需要配置的**耗材属性完全相同**，这些属性包括**材料品牌、材料类型、材料颜色、材料打印温度等**，请在打印前配置好耗材信息。
   - 如果 AMS 中耗材属性其一不同，则会自动续料失败。
   - 建议 Bambu 耗材使用 Bambu 耗材作为替代料，非 Bambu 耗材使用非 Bambu 耗材作为替代料。

![自动续料.jpg](https://wiki.bambulab.com/screen-operation/%E8%87%AA%E5%8A%A8%E7%BB%AD%E6%96%99.jpg)

> 注意避免在打印任务进程中点击“暂停”并退料，退料会导致自动续料流程出错，并切换至从外挂料盘进料。

## AMS工作流程

### 换料（进料&退料）

**进料过程**中，上下料器负责把料线送到五通，五通里程轮计算料送出一小段后，上下料器停止工作，然后由五通电机将料线送入工具头。 **退料过程**中，上下料器和五通电机同时工作，进料器负责驱动料盘往回转，五通电机拉回料线，直到料线退到AMS内部。

上下料器的左右摇臂齿轮分别控制进退料动作。右摇臂抬起齿轮拉动耗材丝进料，左摇臂抬起齿轮驱动退料轴转动料盘来退料，如下图所示。

![](https://wiki.bambulab.com/ams/ams-function-introduction/%E4%B8%8A%E4%B8%8B%E6%96%99%E6%91%87%E8%87%82_.gif)

### 送料助力模式

**当 AMS 送料至挤出机并成功挤出后，AMS 会切换到助力模式。AMS 基于缓冲区的反馈值来助力送料或回抽。五通电机会根据滑块的位置来判断是否继续往前送料：** 当送料过程遇到阻力时，滑块会被顶到右侧；当料被挤出机消耗后，滑块会回到左侧。在耗材即将耗尽时，当最后一段耗材通过五通装置送出后，五通电机将持续运转，直至挤出机检测到耗材完全耗尽并暂停打印，随后电机才会停止转动。

下图为助力送料过程：

![](https://wiki.bambulab.com/ams/ams-function-introduction/ams%E5%8A%A9%E5%8A%9B.gif)

**AMS 把料送至挤出机后 AMS 就会切换到助力模式，在打印结束料线退回 AMS 或者机器重启后，AMS 就会从助力模式切换回空闲状态。** 助力模式仅根据缓冲区的信号反馈来判断是否需要送料，与当前是否有打印任务无关。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间：工作日 9:00-21:00；节假日：9:00-18:00）*](https://support.bambulab.cn/cn/im?from=1)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
