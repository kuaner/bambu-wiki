---
path: zh/software/bambu-studio/release/release-note-1-9-4
title: "Bambu Studio 1.9.4 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2024-08-26T12:45:59.174Z
updated: 2024-08-27T06:47:22.275Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-9-4
---

# 改进

1. 改善悬垂打印的质量  
   a. 在悬垂区和非悬垂区增加速度过渡，改善冷却效果。

![0.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/0.png)

调节 Smooth cofficient 可以控制速度过渡区的长度，以调整悬垂区打印质量。数字越小代表速度调节过度地区域越长。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/left_1.png)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/right_1.png)

增加速度过渡区之后，保持完全悬空区速度不变的情况下，X1C版本打印时间由4h14m增加到4h19m, 虽然打印时间略微增加，但悬垂区可以被更好地打印出来。左侧为改进前，右侧为优化后。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/left_2.png)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/right_2.png)

b. 区分架桥墙和完全悬空的非架桥墙，并使用不同的打印速度，以改善完全悬空的非架桥墙的打印质量。  
![3.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/3.png)

左图是改进前，A1完全悬空区使用桥的速度，右图是改进后，完全悬空区使用设置的非架桥墙的速度。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/left_4.png)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/right_4.png)

在AB两项改善的作用下，A1的打印时间由4h47m增长为5h4m。得到良好的打印质量。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/20240827-144202.jpg)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/20240827-144208.jpg)

2. 改进一些翻译。
3. 添加更多QIDI配置文件。 by [@HYzd766](https://github.com/HYzd766)

# Bug 修复

1. 修复了材料列表偶尔无法在安装向导页面上显示的问题。  
   ![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/6.jpg)
2. 修复在arachne 模式下支撑面距离为0时，悬垂错误使用墙速度的问题。
3. 修复0.2mm喷嘴挤出补偿花费时间过久问题。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/left_7.png)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_9_4/right_7.png)

4. 材料的最大体积流量限制不影响裙缘支撑的速度限制。
5. 修复了擦料塔第二次旋转时Studio崩溃的问题。
6. 修复了更改树边缘宽度对有机树支撑无效的问题。  
   <https://github.com/bambulab/BambuStudio/issues/4487> <https://github.com/bambulab/BambuStudio/issues/4066>
7. 使用高度修改器时，不再使用有机树支撑。  
   <https://github.com/bambulab/BambuStudio/issues/4313>
8. 有机树支撑不再折断长桥。  
   <https://github.com/bambulab/BambuStudio/issues/4318>
9. "绒毛表面”选项现在使用真正的随机性来防止在表面上出现图案化纹理。  
   <https://github.com/bambulab/BambuStudio/issues/4253>, [@SeaRyanC](https://github.com/SeaRyanC)
10. 修复了“添加预设”功能导致Studio崩溃的问题。  
    <https://github.com/bambulab/BambuStudio/issues/4320>
11. PA校准管理界面中的结果现在会按字母顺序排序。  
    <https://github.com/bambulab/BambuStudio/issues/4029>
12. 修复了一些编译问题。[@penguineer](https://github.com/penguineer) [@LightTreasure](https://github.com/LightTreasure)
13. 修复了一些文本拼写错误。 [@t3chguy](https://github.com/t3chguy)
