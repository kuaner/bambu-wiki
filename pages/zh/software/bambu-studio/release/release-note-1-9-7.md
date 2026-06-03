---
path: zh/software/bambu-studio/release/release-note-1-9-7
title: "Bambu Studio 1.9.7 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2024-09-18T10:03:04.314Z
updated: 2024-09-26T13:27:48.242Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-9-7
---

V1.9.7.50因存在A1/A1 mini在Timelapse模式下打印多色时出现的偏移问题已下架，请尽快升级至V1.9.7.52。

请尽快升级至V1.9.7.52，并且**不要再使用V1.9.7.50！**

![](https://wiki.bambulab.com/studio_releasenote/197/1.9.7.52pic.jpg)

## 改进

1. Liveview增加15分钟无操作后自动停止功能（默认）, 可以帮助用户节能和减少数据消耗，在偏好设置中可关闭。  
<https://github.com/bambulab/BambuStudio/issues/4690>

![](https://wiki.bambulab.com/studio_releasenote/197/liveview-option.png)

2. 发送打印时优化了发送文件的大小，对于包含复杂打印指南的MakerWorld模型，能显著减少发送打印的时间。

![](https://wiki.bambulab.com/studio_releasenote/197/new_compare_file_thinner.jpg)

3. 所有盘信息中增加显示每盘的切片时间。

4. 为Mac用户增加修复模型推荐网站链接(已与<https://www.formware.co/onlinestlrepair>沟通并获得允许)。

![](https://wiki.bambulab.com/studio_releasenote/197/new_mac_repair_stl.png)

5. 增加波兰语。  
<https://github.com/bambulab/BambuStudio/issues/4491>  
<https://github.com/bambulab/BambuStudio/issues/4360>

6. 土耳其语部分新增翻译更新，感谢 [**@fatih5228**](https://github.com/fatih5228) 的工作。

7. 在GCode中增加耗材丝使用的统计信息，包含耗材丝使用总量、体积和总长，感谢 [**@THE-SIMPLE-MARK**](https://github.com/THE-SIMPLE-MARK) 。  
<https://github.com/bambulab/BambuStudio/issues/3072>

8. 阿基米德螺旋线图标更换，感谢 [**@MarkussLugia**](https://github.com/MarkussLugia) 的工作。

9. 创建或编辑自定义耗材后返回引导框。

![](https://wiki.bambulab.com/studio_releasenote/197/custom_filament_setting_wizard.gif)

## Bug修复

1. 修复1.9.5引入的特定模型arachne打印线宽错误导致的层纹显著，打印质量差的问题。(模型来自[adriancubas](https://www.instructables.com/member/adriancubas/))

![](https://wiki.bambulab.com/studio_releasenote/197/arachne_compare.png)

2. 修复换料冲刷量较小时，切片未生成冲刷gcode的bug。  
<https://github.com/bambulab/BambuStudio/issues/4738>

3. 修复了A1、A1 Mini机型中挤出补偿后没有回抽的问题。

4. 对PPA-CF材料增加X1E设备。

5. 修改A1 mini的“到顶盖高度”，用于限制使用“逐件打印”时各对象的可打印高度。

6. 修复AMS的映射问题。

7. 修复了用户在Studio的MakerWorld选项卡下使用过程中可能因打开新标签页，Home选项卡内容被错误占用的问题。Studio统一使用本地浏览器打开这些新标签页。

8. 修复A1/A1 mini在Timelapse模式下打印多色时出现的偏移问题。V1.9.7.50在换料GCode结束后，会尝试在盘外进行螺旋抬升，这可能触及到机器的极限位置导致丢步，进而引起偏移。

<https://github.com/bambulab/BambuStudio/issues/4841>

![](https://wiki.bambulab.com/studio_releasenote/197/newnew_remove_spirial.jpg)
