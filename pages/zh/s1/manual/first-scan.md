---
path: zh/s1/manual/first-scan
title: "S1 首次使用"
description: "首次开机前，建议使用充电设备将电量充满，保证使用体验。"
tags: []
created: 2026-11-26T14:00:51.427Z
updated: 2026-11-27T02:07:30.792Z
source: https://wiki.bambulab.com/zh/s1/manual/first-scan
---

## 视频指南

## 认识扫描仪

S1 配备了 3 种实体按键，熟悉按键功能将帮助您顺利完成首次使用。

- 确认键  
  确认当前选择，开始（短按）/暂停（短按）/完成（长按）扫描。
- 模式切换/电源键  
  长按开机或关机，在扫描过程中短按可切换视图。
- 滚轮  
  可以在扫描时调节曝光或缩放视角。设置参数时，滚动选择参数，短按切换/确认当前选择。

![054.jpg](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/054.jpg)

## 软件下载

[进入官网](https://bambulab.com/zh)，下载 Bambu Scan 软件并安装。

![001.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/001.png)

如果需要使用官方网卡，此处需要勾选“ 安装 Bambu 官方网卡驱动”。

![002.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/002.png)

## 绑定扫描仪

打开软件后，您可以在 **“无线连接”** 与 **“有线连接”** 两种方式中任选其一。

- 首次使用推荐使用有线连接方式，以缓慢补充电量，确保设备有足够的电量完成固件更新、校准工作。
- **采用 "无线连接" 时，该网卡将用于连接扫描仪，在没有其他网卡的情况下，电脑暂时无法访问互联网。**

### 无线连接

扫描仪选择“无线连接”后，会显示一个网络热点。电脑连接该热点后，软件将自动与扫描仪进行绑定。

注：请确保所使用的协议为 **Wi‑Fi 6**（802.11ax）。在其他 Wi‑Fi 协议下，传输速率可能不足，进而影响扫描的稳定性与速度。若不清楚网卡协议或电脑没有无线网卡，推荐使用官方无线网卡进行连接。

![003.jpg](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/003.jpg)

### 有线连接

使用原装线缆连接电脑和扫描仪后，打开软件，软件将自动绑定扫描仪。若未能自动连接，请重新安装一次线缆。

注：为保证足够的传输速度和使用效果，电脑的 **USB 接口必须是 USB 3.1（或更高）标准**。暂不支持拓展坞接入电脑，暂不支持其他 Type-C 线缆接入。

## 更新固件

设备首次使用时若固件版本过低，软件将提示需要升级到 01.01.00.00 版本。若更新后存在更高版本的固件，可选择按后续步骤继续更新到最新版。

先在软件上点击设备信息，开始更新固件。

![004.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/004.png)

### 自动更新

若设备收到在线固件包，可直接点击“下载并更新”。

![005.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/005.png)

### 本地更新

1. 下载固件

进入[固件下载链接](https://bambulab.com/zh/support/firmware-download/s1)，下载最新版的 S1 固件包。

2. 安装固件

点击“从本地文件安装”。

![007.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/007.png)

选择刚才下载的压缩包。

![008.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/008.png)

点击开始更新。

![009.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/009.png)

## 设备校准

> 本设备采用红外散斑与蓝色激光双光源进行三维扫描。其中，**红外散斑及平行线模式下的蓝色激光处于安全水平**，在对应模式下扫描人体或人脸时无需闭眼或做特别防护。  
> 其余蓝色激光模式符合 **Class 2（Ⅱ类）** 激光安全标准，强烈建议**避免长时间刻意直视激光束或其镜面反射光，同时避免或直接扫描人体**。  
> 扫描过程中投射的激光图案可能呈现闪烁或移动效果。患有光敏性癫痫或相关疾病、或对闪烁光敏感的用户，**建议避免注视扫描光束及其投射图案**，并在使用前咨询医生。若使用过程中感到头晕、视觉不适，请立即停止扫描并离开光照区域。

更新完成后进行校准。取出扫描仪和校准板，撕下扫描仪的保护膜。

![010.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/010.gif)

按照图示方向向上放置标定板。

![011.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/011.png)

根据屏幕指示，或者点击 Bambu Scan 左上角校准按钮，进入校准流程。

![012.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/012.png)

请根据校准页面的教程提示，将**扫描仪移至标定板上方，向前微微倾斜扫描仪，确保相机与标定板平行。**

![013.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/013.gif)

当扫描仪和标定板几乎平行时，开始校准。

![014.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/014.png)

后续校准过程中每一步，都需要让橙色小球的数字尽可能与白色数字重合，请再根据屏幕提示在上下左右前后进行微调，并在小球变绿后停顿。步骤完成后自动开始下一步，微微抬升扫描仪后重复前序步骤，直到前11步校准完成。

![015.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/015.webp)

第 12 步根据屏幕提示,向下对准最后一个小球,完成整个校准流程。

![016.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/016.webp)

第12步根据屏幕提示，向下移动对准最后一个小球，完成整个校准流程。

![017.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/017.png)

## 开始扫描

3D扫描的基本原理是，扫描仪每次从一个角度采集被扫描物体表面的一组点，形成**单帧点云**。当你绕着物体扫描时，软件会根据重叠区域对齐不同角度的数据，形成更完整的**融合点云**。最后，软件通过**网格封装**，用许多相连的三角面重建物体的表面，生成可打印或者进一步编辑三维模型。我们先从建立一个扫描项目开始。

![018.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/018.png)

在软件上点击“新建项目”，进入到预设选择页面。

![019.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/019.png)

“智能推荐”通过一系列选项回答，获取一套合适的参数和推荐工作，可以根据被扫描物体的特征进行回答。

![020.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/020.png)

“快速场景”则可直接使用软件默认的参数预设。

![021.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/021.png)

### 简单模型

扫描的物体需满足刚性连接，即物体本身不会因受力而发生变形，并且扫描过程中物体也需要牢牢固定在桌面/平台上，不能发生位移。

![022.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/022.png)

选择“通用中型物体”或其他预设。点间距设置越小，扫描后的细节越丰富，但也会占用更多的电脑资源，可根据实际需求调整。

![023.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/023.png)

将扫描对象放置在框图中心，并保证右侧距离指示器工作在中间位置后再开始扫描。

> 注：按下黄色确认键前，扫描仪距离不宜过近，保持250mm~300mm左右为最佳。注意扫描过程中，被扫描物体需固定牢固。

![024.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/024.png)

按下扫描仪上的黄色确认键，开始时首先扫描整体，缓慢移动扫描仪，绕行物体。

![025.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/025.webp)

扫描过程中尽可能保持扫描距离在右侧距指示器的最佳工作距离（对应指示条的绿色区域），或屏幕上投射区域/激光线条刚好作用在物体表面。

![026.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/026.webp)

> 小技巧：如扫描过程中发生特征丢失，请回到先前已扫描部分，待指示器重新匹配之后，再缓慢逐步过渡到待扫描的部分完成扫描。

由于扫描仪的两个黑白摄像头（深度相机）都需要观察到扫描对象（类似人眼的双目定位），因此扫描鼻尖时，需水平握持扫描仪，确保另一摄像头未被遮挡。

|  |  |
| --- | --- |
| 027.png | 028.png |

扫描过程中可以按下“模式切换/开机”键，切换为质量色谱，根据质量色谱表现，针对性地扫描局部区域。软件上也可通过左下角的圆环切换显示模式。

> 质量色谱：绿色代表扫描点数较多，点云更完整；红色/黑色代表扫描点数较少，点云不足。为获得更优质的扫描结果，建议对所需部分的点云进行充分扫描而且在质量色谱完全变为绿色后再完成扫描。

![029.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/029.png)

首次扫描完毕后，点击设备的确认键，或在软件上暂停扫描，检查本次扫描的点云细节。

![030.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/030.webp)

### 新建扫描

大部分模型通常都无法通过一次扫描获得一个物体的完整数据，此时可新建一个扫描子项目，并调整物体角度。通过多次扫描后拼接为一个点云来获得物体的完整扫描数据。

根据小屏幕指引或点击 Bambu Scan 顶部的“新建扫描”。

![031.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/031.png)

第二次扫描可选择相同预设，或根据需求选用其他。

![032.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/032.png)

重新摆放物体后，开始扫描。

![033.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/033.png)

当所有面都被扫描完毕后，可在设备上短按一次黄色确认键，再长按结束扫描。软件上还有“一键处理”选项。

一键处理：能够自动删除点云中的无效数据，完成贴图和生成网格。但该过程可能漏删一些点云，导致网格中出现无效数据，可在后续“网格清理”中删除。若您选择该功能，可直接跳转到“网格处理”。

![034.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/034.png)

处理模式可根据需求选择，首次使用建议选择“质量优先”。

![035.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/035.png)

## 点云清理

对该物体的所有面都扫描过后，还需要使用不同工具处理背景或悬空的杂乱点云。

1. 离群项检测

软件将认定面积最大的点云为主体，并自动识别四周未合并的孤立点或非连接箱，确认识别正确后可选择删除。当扫描背景面积大于被扫描物体时，建议使用套索工具手动清理。

![036.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/036.webp)

2. 套索手动清理

手动框选点云数据删除，操作更加灵活。

![037.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/037.webp)

清理了某个点云中的数据后，需关闭右侧工具栏，再从左侧项目树选择其他点云。

![038.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/038.webp)

预处理好每个子项目（新建扫描）的点云后，可开始下一步“拼接”。

## 点云拼接

![039.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/039.png)

### 自动拼接

可选择“自动拼接-特征拼接”，此时软件将自动识别导入点云的特征，并根据特征自动拼接点云。

1. 选择所有点云后，选择右下角拼接方式后点击预览拼接。  
   自动拼接方式支持“特征拼接”与“标记点拼接”两种，其中前者适用于多个扫描之间有较多的重合特征，后者适用于多次扫描之间有大量标记点可辅助定位。

> 注意：标记点拼接的精度高于特征拼接，如多个点云间有重复标记点存在，请优先使用标记点拼接方式获得更优的拼接效果。

![040.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/040.png)

2. 检查预览结果，若拼接正确，可选择“锁定并拼接下一个”或右上角的“应用”。

![041.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/041.png)

以该模型为例，拼接完成后会是一个几乎封闭的点云。若点云中仍有较大面积的空洞，可继续新建扫描，然后拼接，或等待后续网格处理阶段补洞完善。

### 手动拼接

当自动拼接无法实现较好的效果时，可使用手动拼接。该方法需要手动对齐两个点云中的相似特征，软件将根据选点位置的特征进行优化处理，至少需要 3 对配对点。

> 配对点越多，覆盖范围越广，拼接的效果越理想。若手动拼接存在异常，可尝试增加标记点。

![042.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/042.png)

完成拼接后，可点击生成网格。

![043.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/043.png)

## 网格处理

预设选择“通用”，也可根据场景切换为其他，点击“应用”。

![044.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/044.png)

网格生成完毕后，也可通过上方悬浮窗进行部分操作。

![045.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/045.png)

### 网格清理

由于之前已经清理了点云，这步通常不会生成多余的网格。若您生成的网格中存在多余部分，可使用该功能删除。

### 补洞

可使用该功能填补模型上的空洞。

![046.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/046.png)

自动模式下可调整最大孔洞直径，一键修复。

![047.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/047.png)

如扫描的是彩色模型，在补洞完成后，可选择重新贴图，软件将拟合生成空洞上的贴图。

![048.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/048.png)

### 简化/细化模型

为了提高导出速度，可以对模型进行简化，简化后的模型面数将大幅缩减。

![049.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/049.png)

若需要模型细节，也可使用细化模型。

![050.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/050.png)

## 导出模型

点击右上角的导出，或在左侧列表里选择网格导出。导出的模型可使用 Bambu studio 进行 3D 打印或者使用其他专业软件逆向建模。

|  |  |
| --- | --- |
| 051.png | 052.png |

该操作流程能够满足绝大多数扫描工作。更多软件功能，可进入[Bambu S1 Wiki](...md) 了解。

## 汽车零部件

尝试了扫描雕塑，并熟悉软件操作后，可再进一步体验“蓝色激光+标记点”的扫描方式，详细内容可阅读[标记点使用教程](marker.md)。

![053.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/first-scan/zh/053.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
