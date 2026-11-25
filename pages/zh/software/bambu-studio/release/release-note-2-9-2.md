---
path: zh/software/bambu-studio/release/release-note-2-9-2
title: "Bambu Studio 2.9.2 版本说明"
description: ""
tags: []
created: 2026-11-24T14:02:25.837Z
updated: 2026-11-25T06:46:50.425Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-9-2
---

本次 Bambu Studio 版本更新新增对拓竹新品 P3C 打印机的支持，同时支持H2D多口径混合打印，并带来多项软件性能与体验优化，修复了若干影响打印质量与稳定性的问题。

## 新功能

### 支持拓竹P3C 打印机

支持拓竹P3C 多喷头3D打印机，最多可同时装载 7 个打印头。每个打印头都有独立的进料与加热系统，让耗材始终处于装载状态，并可主动预热，最快 6 秒内完成两种耗材的接力打印。

![001.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/001.jpg)

### H2D 支持多口径混合打印(包括选料器场景)

支持H2D的多口径切片和打印，包含选料器场景，在同一模型中可为局部细节和主体指定不同口径的喷嘴，让不同口径采用各自合适的层高打印：小口径负责文字与刻度等细节，大口径负责快速打印主体

另外，不同于其他切片软件的多口径功能，BambuStudio 基于切片引擎深度重构，带来了独树一帜的自由度方案：

- 全尺寸混搭：不仅支持不同口径，更重要的是支持不同口径匹配不同层高。
- 区域自由定制：不仅限于墙和填充，用户也可对模型不同精细度的外观区域自由指定喷嘴，将多口径组合的自由度发挥到极致。

多口径的使用方法可[参考wiki](../../../h3c/manual/mixed-nozzle-size-printing.md)

> H2C、X2D 等机型适配说明：机型的适配需要一个过程，我们正在全力推进。适配时间最晚不晚于[官方公告](https://mp.weixin.qq.com/s/C1DNh4_YXBhanpIjvJhMXQ)中公布的时间节点，请大家耐心等待，并持续关注后续更新公告。

![002.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/002.png)

### 其他新功能

- 稀疏填充密度支持小数点输入 [#12513](https://github.com/bambulab/BambuStudio/issues/12513)。

![003.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/003.png)

- 新增跨零件涂色渗透参数：允许颜色从该零件涂色的顶面和底面渗透到相邻零件中。关闭时,涂色渗透将不会到达相邻零件。([#8642](https://github.com/bambulab/BambuStudio/issues/8642)）

|  |  |
| --- | --- |
| 004.gif | 005.gif |

- 新增鼠标旋转灵敏度偏好设置：可在偏好设置中调整三维视图的旋转灵敏度 [#12616](https://github.com/bambulab/BambuStudio/issues/12616)。

![006.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/006.png)

- 支持将选中零件拆分为新对象：选中一个或多个零件后可一键拆分为独立对象。

![007.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/007.png)

- 切片预览支持逐段查看喷嘴与耗材信息。

![008.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/008.png)

- 切片后预览新增统计每根耗材的打印耗时，新增不同耗材单独显示预计的打印时间。

![009.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/009.png)

---

## 优化与改进

### 添加耗材时的选择对话框多项改进

设备页AMS耗材选择处直接显示料盘的备注信息，标记当前正在使用的耗材与位置，便于选择耗材时区分

![010.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/010.png)

### 优化模型简化页面的交互

优化模型简化页面的交互，将不同的简化方式拆开独立使用简化等级，方便用户使用，同时默认开启保留所有绘制，防止简化模型导致色彩丢失

![011.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/011.png)

### 优化多色模型的接缝位置

优先选择其后隐藏于色块内更远的位置，使接缝的起点远离外表面，减少因长距离空驶后，熔融区压力不稳定引起的外表面瑕疵。

![012.gif](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/012.gif)

优化前

![013.gif](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/013.gif)

优化后

![014.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-studio/release/release-note-2-9-2/zh/014.jpg)

### 其他优化项

- 设备页AMS耗材设置显示颜色名称与色值，便于分辨 [#12812](https://github.com/bambulab/BambuStudio/pull/12812) 感谢 @[longrackslabs](https://github.com/longrackslabs) 。
- 新增当填充图案为 3D 蜂窝、蜂窝或螺旋，且加速度设定较高时，打印机可能产生明显的振动与噪声提示。
- 公网打印连接方式优化：云端发送失败时会自动尝试局域网直连，减少因云端异常导致的发送失败。
- 优化了 AMS 槽位余量进度条的配色与边框，读数更清晰。
- 优化软件启动与界面响应速度。
- 优化多口径下的支撑参数，支撑顶 / 底 Z 间距支持编辑。
- 优化普通支撑与经典树状支撑的生成算法。对于支撑结构复杂、支撑面较多的模型，减少切片时间的等待。
- Bambu Lab H3C&P3C机型单口径模式0.2mm喷嘴的首层填充线宽改为0.6mm，提升首层附着力，改善质量。
- 多色打印的冲刷量手动修改上限已提升至 2000 mm³。实际冲刷量受打印机固件限制，支持的冲刷量请参阅固件发布说明。

## Bug 修复

1. 修复网格参数对话框中禁用“确定”时，STEP 导入卡死 [#13103](https://github.com/bambulab/BambuStudio/pull/13103) 感谢[edg2s](https://github.com/edg2s)。
2. 修复二进制STL中零法线的ASCII读取 [#12963](https://github.com/bambulab/BambuStudio/pull/12963) 感谢[aklipi](https://github.com/aklipi)。
3. 修复相同对象共享切片图层时打印位置错误的问题 [#12861](https://github.com/bambulab/BambuStudio/pull/12861) 感谢[aklipi](https://github.com/aklipi)。
4. 修复：在多直径模式下，树状支撑在重复悬垂多边形时卡住 [#13060](https://github.com/bambulab/BambuStudio/pull/13060) 感谢[mattlyle](https://github.com/mattlyle)。
5. 修复一些编译问题 [#12975](https://github.com/bambulab/BambuStudio/pull/12975) 感谢[hadess](https://github.com/hadess)。
6. 修复检查 G-code 冲突检测问题，改为检查所有的实例 [#12862](https://github.com/bambulab/BambuStudio/issues/12862) [#12863](https://github.com/bambulab/BambuStudio/pull/12863) 感谢[aklipi](https://github.com/aklipi)。
7. 修复Linux 在点击“下载并打开”时崩溃问题 [#13063](https://github.com/bambulab/BambuStudio/pull/13063) 感谢[sproctor](https://github.com/sproctor)。
8. 修复预设比较弹窗兼容性问题 [#12843](https://github.com/bambulab/BambuStudio/pull/12843) 感谢[flavioheleno](https://github.com/flavioheleno)。
9. 修复Linux上无法启动的问题 [#12925](https://github.com/bambulab/BambuStudio/pull/12925) 感谢[freasy](https://github.com/freasy)。
10. 修复CLI由于等待备份线程导致命令行无法退出问题 [#12875](https://github.com/bambulab/BambuStudio/pull/12875) 感谢[aklipi](https://github.com/aklipi)。
11. 帮助菜单新增日志文件夹入口 [#11493](https://github.com/bambulab/BambuStudio/pull/11493) 感谢[BenJule](https://github.com/BenJule)。
12. 预览页支持按对象独立着色：可在预览中区分同一模型的不同对象,需要在偏好设置中开启使用 。感谢[Miquelsn](https://github.com/Miquelsn)。
13. CLI命令行擦料塔旋转角度功能暂改为不支持，等待后续优化 感谢 [andeplane](https://github.com/andeplane) 。
14. 修复发送打印页转化小语种失败问题 [#13122](https://github.com/bambulab/BambuStudio/issues/13122)。
15. 修复step文件时计算面片数目不可点击确认的问题 [#13113](https://github.com/bambulab/BambuStudio/issues/13113) [#13080](https://github.com/bambulab/BambuStudio/issues/13080) 。
16. 修复单色涂色对象收缩补偿被误禁用 [#13029](https://github.com/bambulab/BambuStudio/issues/13029) 。
17. 修复布尔运算闪退问题 [#13026](https://github.com/bambulab/BambuStudio/issues/13026)。
18. 修复首层后重复设置喷嘴温度覆盖手动调整的问题 [#13012](https://github.com/bambulab/BambuStudio/issues/13012)。
19. 修复H2C选择喷嘴不生效的问题。
20. 修复料塔无法移动至盘边缘的问题 [#12995](https://github.com/bambulab/BambuStudio/issues/12995)[#13146](https://github.com/bambulab/BambuStudio/issues/13146)。
21. 修复H2C左右喷嘴显示反了的问题 [#12933](https://github.com/bambulab/BambuStudio/issues/12933)。
22. 修复HMS不显示的问题 [#12935](https://github.com/bambulab/BambuStudio/issues/12935)。
23. 修复双击打开外部 3MF 时文件名始终显示 untitled 的问题 [#12943](https://github.com/bambulab/BambuStudio/issues/12943)。
24. 修复异常弹窗导致账号退出登录的问题 [#12746](https://github.com/bambulab/BambuStudio/issues/12746)。
25. 修复mac上无法删除高度范围修改器的问题 [#12739](https://github.com/bambulab/BambuStudio/issues/12739)。
26. 修复外挂料盘添加耗材管理器后余量显示为0的问题 [#13014](https://github.com/bambulab/BambuStudio/issues/13014)。
27. 修复网格布尔运算在共面输入时崩溃或卡死的问题。
28. 修复设备页 Liveview 偶发崩溃的问题。
29. 修复部分 3MF 因项目配置非法导致导入后模型几何丢失的问题。
30. 修复mac、linux与多显示器环境中页面一些兼容性问题。
31. 恢复零件导入时单位转换弹窗。 [#13280](https://github.com/bambulab/BambuStudio/issues/13280)、 [#12929](https://github.com/bambulab/BambuStudio/issues/12929)

## 已知问题

- 多口径混合打印仍在持续完善，部分组合下支撑与擦料塔的尺寸估算可能与实际打印结果存在偏差。
- H2D多口径下Helio功能暂不完善，Helio团队将会尽快支持H2D的多口径功能。
- P3C 选配烘干模块目前由固件判断电源适配器状态，软件侧尚未提供前置拦截，未接烘干适配器时发起烘干可能无响应。
- X2D 使用 ABS 耗材切片时，起始段 G-code 中的过滤风扇指令被误识别为辅助风扇指令，导致G-code预览中辅助风扇转速为被错误显示成 100%，此问题仅影响预览显示，不影响实际打印。将在后续通过预设文件更新解决。
- Windows 11 开启“智能应用控制（Smart App Control）”时，Bambu Studio 可能无法启动（v02.09.02.62）

  **现象**：更新到该版本后，部分 Windows 11 用户双击启动时会弹出 “bambu-studio.exe – Bad Image” 错误，提示文件为安装目录下的 libmpfr-4.dll，错误代码 0xC0E90002，程序无法打开。  
  **原因**：该版本随包分发的 libmpfr-4.dll、libgmp-10.dll 未进行数字签名。Windows 11 的智能应用控制（Smart App Control）处于“开启”或“评估”模式时，会阻止未签名 DLL 加载，从而出现上述报错。  
  **临时解决方案**：使用签名版本的 DLL 替换安装目录中的同名文件，操作步骤如下：

  > 1. 下载并解压缩 [signed\_dll.rar](https://wiki.bambulab.com/software/bambu-studio/release/release-note-2-9-2/signed_dll.rar)，将得到 libmpfr-4.dll 和 libgmp-10.dll 这两个文件。
  > 2. 关闭正在运行中的Bambu Studio软件，把上面两个文件拷贝到 studio 的安装目录下，默认是 C:\Program Files\Bambu Studio。若安装时修改过，可在桌面右键“Bambu Studio”，点击“打开文件所在的位置”即可。
  > 3. 提示是否替换同名文件，选择替换。替换后重新打开 Bambu Studio。

  后续版本将提供已签名的依赖库，届时无需再手动替换。
