---
path: zh/h2/manual/h2d-first-print
title: "H2D Combo 首次打印"
description: "H2D Combo 首次打印指南"
tags: []
created: 2025-03-25T04:22:43.564Z
updated: 2025-11-28T07:22:05.022Z
source: https://wiki.bambulab.com/zh/h2/manual/h2d-first-print
---

## 视频教程

视频和图片中展示的机器外观和固件版本并非量产版本，请以您收到的机器外观和用户界面为准。

## 1. 正确连接 AMS 2 Pro

将 AMS 2 Pro 放置在打印机顶部，连接上6PIN线和PTFE料管。

|  |  |
| --- | --- |
|  |  |

观察PTFE管是否从打印机后侧的小孔中穿过，如果能看到PTFE管穿过，说明连接到位；否则，表示PTFE管未连接正确，将会导致进料失败。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-1.png)

### 初始化新AMS 2 Pro

打印机在检测到新AMS 2 Pro接入时，需要进行一次初始化。这一步是为了检测AMS 2 Pro连接到了哪一侧挤出机。**注意：打印机上进料口对应右挤出机，下进料口对应左挤出机**。

本文以AMS 2 Pro连接上进料口，外挂料盘连接下进料口为例进行说明。

|  |  |
| --- | --- |
|  |  |

AMS 2 Pro有两种初始化方式：

1. 自动初始化

在AMS 2 Pro中插入一卷耗材，然后点击“检测”。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-3.png)

|  |  |
| --- | --- |
|  |  |

2. 手动初始化

如果没有耗材用于AMS 2 Pro自动初始化，可以在屏幕上点击“手动设置”，把接入的AMS 2 Pro配置到左/右挤出机上。如果AMS 2 Pro接入的是上进料口，则连接到右挤出机；如果接入的是下进料口，则连接到左挤出机。

![手动初始化.jpg](https://wiki.bambulab.com/h2/manual/first-print/zh2/%E6%89%8B%E5%8A%A8%E5%88%9D%E5%A7%8B%E5%8C%96.jpg)

### 放入料盘

将打印所需的耗材装入AMS 2 Pro中。

|  |  |
| --- | --- |
|  |  |

## 2. 连接外挂料盘

### 安装料盘

在安装外挂料盘之前，请记下耗材类型和颜色，然后根据耗材绕线的方向，将料盘放置在外挂支架上。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-9.png)

### 进料

1. 在屏幕上点击“编辑”，选择耗材的类型和颜色后，点击“确认”。

![编辑外挂料盘.png](https://wiki.bambulab.com/h2/manual/first-print/zh2/%E7%BC%96%E8%BE%91%E5%A4%96%E6%8C%82%E6%96%99%E7%9B%98.png)  
![编辑耗材.png](https://wiki.bambulab.com/h2/manual/first-print/zh2/%E7%BC%96%E8%BE%91%E8%80%97%E6%9D%90.png)

2. 将耗材的一端插入料管，向工具头里推送耗材直至无法前进。此时，打印机屏幕上的工具头处会出现小绿灯，表示检测到耗材进入。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-13.png)  
![左边小绿灯.jpg](https://wiki.bambulab.com/h2/manual/first-print/zh2/%E5%B7%A6%E8%BE%B9%E5%B0%8F%E7%BB%BF%E7%81%AF.jpg)

3. 在屏幕上点击“进料”，等待喷嘴加热，期间再次手动推动耗材，确保耗材仍然留在挤出机内。

|  |  |
| --- | --- |
|  |  |

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-17.png)

4. 根据打印机提示观察喷嘴，看见喷嘴顺利挤出耗材后，在屏幕上点击“耗材已挤出，继续”；如果耗材没有被挤出，选择“耗材未挤出，重试”，然后重复推入耗材的动作。

![挤出.jpg](https://wiki.bambulab.com/h2/manual/first-print/zh2/%E6%8C%A4%E5%87%BA.jpg)  
![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-19.png)

## 3. 开始打印

在开始打印前，请正确放置构建板。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/am404107.jpg)

### 从打印机屏幕发起打印

我们强烈建议您单独购买一个U盘插入打印机使用，这样可以保存打印机内的工作录像和历史打印缓存。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-20.png)

在首页上点击“打印文件”，选择想要打印的模型。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-21.png)  
![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-22.png)

热床调平、动态流量校准、喷嘴偏移校准默认为自动模式，可以根据需要自行调整。然后点击“下一步”。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-23.png)  
![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-24.png)

选择匹配的耗材，开始“打印”。请注意，打印机内置模型或者USB存储中的模型是已经切片完成的文件，切片文件中的耗材与挤出机/热端的配对关系也已确定，故无法强行更改到另一个挤出机/热端进行打印。

如果在匹配耗材页面无法选择想要打印的耗材，可能需要适当调整耗材位置，把它放入另一个挤出机所连接的AMS或者外挂料盘中。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-25.png)  
![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-26.png)

### 从Bambu Studio发起打印

在Bambu Studio中导入想要打印的模型，修改打印参数后点击切片单盘，再点击打印单盘即可将打印任务发送给打印机。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-27.png)  
![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-28.png)

由于H2D具有双喷嘴，在打印多色模型时Bambu Studio会自动计算最省料的耗材摆放情况，并且自动给耗材分组。

如果您不想按照默认的耗材分组进行打印，也可以手动修改耗材分组。点击“材料分组”按钮，选择“自定义”，然后鼠标左键点击耗材图标或者点击中间的交换按钮，即可将耗材切换到另一挤出机。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-29.png)  
![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-30.png)

### 取下模型

打印结束后，需等到热床、模型冷却到室温时再将模型从打印板上轻轻取下，以免造成模型变形、损伤或打印板损伤。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-31.png)

取下擦料塔并用铲刀清除校准线后，重新将打印板放回打印机内。

![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-32.png)  
![](https://wiki.bambulab.com/h2/manual/first-print/zh2/image-33.png)

## 4. 卸载耗材

### AMS 2 Pro退料

在打印任务正常完成后，耗材会自动退回到 AMS 2 pro。然而，**如果打印任务在中途被取消或中断**，您可以在屏幕上点击"退料"，以便让被挤出机咬合的耗材退回到 AMS 2 pro。

![ams退料.jpg](https://wiki.bambulab.com/h2/manual/first-print/zh2/ams%E9%80%80%E6%96%99.jpg)  
![ams抽回.jpg](https://wiki.bambulab.com/h2/manual/first-print/zh2/ams%E6%8A%BD%E5%9B%9E.jpg)

### 外挂料盘退料

在屏幕上点击“退料”。

![进退料.jpg](https://wiki.bambulab.com/h2/manual/first-print/zh2/%E8%BF%9B%E9%80%80%E6%96%99.jpg)  
![退料.jpg](https://wiki.bambulab.com/h2/manual/first-print/zh2/%E9%80%80%E6%96%99.jpg)

根据打印机提示，在耗材退出工具头后边旋转料盘，边拉回耗材。当耗材接近气管接头时，用手接住料盘，并将耗材塞进料盘的孔洞中，然后点击“继续（问题已解决）”。

![拉出.jpg](https://wiki.bambulab.com/h2/manual/first-print/zh2/%E6%8B%89%E5%87%BA.jpg)

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
