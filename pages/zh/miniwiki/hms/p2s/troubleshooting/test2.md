---
path: zh/miniwiki/hms/p2s/troubleshooting/test2
title: ""
description: ""
tags: []
created: 2026-01-28T12:18:47.194Z
updated: 2026-03-16T06:42:11.836Z
source: https://wiki.bambulab.com/zh/miniwiki/hms/p2s/troubleshooting/test2
---

![]()
标签

未发现外部挂载的耗材；请装入新的耗材。

当前问题可能对应以下情况，点击可查看帮助指南：

[情况1
耗材已用尽或耗材断了](#mw-case-1)
[情况2
工具头耗材检测传感器损坏](#mw-case-2)

Step 1/4

检查挤出机连接的外挂料盘上耗材是否已用完或者耗材断了。

![检查外挂料盘耗材](https://public-cdn.bblmw.com/hms/actionimage/us/07ff8011/a60c12b86c59916d04917d00e0f2d1e1.png)

若耗材未用完，或耗材未断，请跳转
[情况2](#mw-case-2)。

Step 2/4

在外挂料盘上安装新耗材。手动将耗材推送进工具头内部，直至感觉推送阻力增大，耗材无法继续向前。

![push_filament_p2s.webp](https://wiki.bambulab.com/miniwiki/hms/p2s/push_filament_p2s_2.webp)

Step 3/4

在错误弹窗中点击“重试”，恢复打印。

![点击继续恢复打印](https://wiki.bambulab.com/miniwiki/hms/p2s/hms_zh_p2s.jpg)

Step 4/4

点击重试之后，手动将耗材持续朝料管内推进，直至喷嘴有耗材挤出。

![filament_squeezed_out_p2s.webp](https://wiki.bambulab.com/miniwiki/hms/p2s/filament_squeezed_out_p2s_2.webp)

若问题仍存在，请跳转
[情况2](#mw-case-2)。

Step 1/3

按压黑色气管接头，拔下工具头上的特氟龙管。

![拔下工具头上的特氟龙管](https://public-cdn.bblmw.com/hms/actionimage/us/07ffc012/7db6d3fff317ecd772e569717a9ff383.png)

Step 2/3

插入一小段耗材，用于触发耗材传感器。

![插入一小段耗材触发传感器](https://public-cdn.bblmw.com/hms/actionimage/us/07ffc010/c63f2cd5273828825452c4908f3ac0b0.png)

Step 3/3

观察机器界面显示的耗材传感器状态，并确认图标从灰色变为耗材颜色。

![检查传感器状态](https://wiki.bambulab.com/miniwiki/hms/p2s/sensor-zh1.png)

**灰色图标：**未识别耗材，传感器可能损坏。参考
[Wiki](/zh/p2s/troubleshooting/hmscode/07FF_2000_0002_0002)
深入排查。

**绿色图标：**耗材识别正常。如仍存在报警，请
[联系人工客服](#)。
