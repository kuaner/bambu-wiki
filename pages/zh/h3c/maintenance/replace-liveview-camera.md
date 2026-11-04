---
path: zh/h3c/maintenance/replace-liveview-camera
title: "实况摄像头更换指南"
description: ""
tags: []
created: 2026-11-03T12:42:52.209Z
updated: 2026-11-03T12:48:30.501Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-liveview-camera
---

## 实况摄像头

实况摄像头安装在打印机左前立柱的横梁上，通过实况摄像头在 Bambu Studio 和 Bambu Handy 中实时查看打印的过程，并实现多种智能检测功能。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-liveview-camera/zh/92___________liveview_camera_replacement_guide_d3cc4ab8e5.jpg)

## 何时更换

1. 成像画面异常，如模糊、色块等；
2. 实况摄像头报错，且已经过技术支持分析确认；
3. 明确的物理损坏。

## 工具和材料

- H2.0 内六角扳手
- 镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 1. 打印机侧板的拆装需要提前移除 AMS 3H，请参考 WIKI： [AMS 3H 拆除与安装指南](replace-ams3.md)，将 AMS 3H 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3H 的场景下进行。
> 2. 根据更换侧板的操作指南，在断电前，先将热床下降到底部。

## 移除实况摄像头

### 第 1 步 移除左侧板

请参考 WIKI：[左侧板更换指南](replace-side-panel-left.md)，移除左侧板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-liveview-camera/zh/60_________________auxiliary_part_cooling_fan_duct_left_replacement_guide_686a72b3d9.jpg)

### 第 2 步 移除实况摄像头

在 AP 板上揭开连接器盖子，将实况摄像头排线从连接器上松出。

|  |  |
| --- | --- |
| 图 | 图 |

沿着过线孔将排线退出，沿着排线的路径下拉至摄像头所在横梁的位置，将排线与框架分离。

|  |  |
| --- | --- |
| 图 | 图 |

在腔室内将手伸到摄像头背面的间隙处抠动摄像头，可解除摄像头的固定，移除摄像头。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装实况摄像头

### 第 1 步 安装实况摄像头

触点面朝上，将排线穿过横梁附近的过线孔，然后将摄像头向横梁边角推到底，安装到横梁上。

|  |  |
| --- | --- |
| 图 | 图 |

> 实况摄像头两端都配置有卡扣，用来卡住实况摄像头的同时，也可作为安装到位的判断标识。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-liveview-camera/zh/92___________liveview_camera_replacement_guide_cd0c091339.jpg)

以下两张图是安装前和安装后，在前立柱上的两个确认位置的外观差异。

|  |  |
| --- | --- |
| 图 | 图 |

将摄像头排线穿过上方的过线孔，注意在有缠绕胶带保护的位置再对排线调整方向，避免操作排线。

|  |  |
| --- | --- |
| 图 | 图 |

将排线连接到 AP 板连接器上，确认白线与连接器的边沿平齐，然后合上盖子。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 安装左侧板

请参考 WIKI: [左侧板更换指南](replace-side-panel-left.md)，安装好左侧板及玻璃前门。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-liveview-camera/zh/55___________chamber_temperature_sensor_replacement_guide_e33e1f35ef.jpg)

## 功能验证

启动打印机，通过 APP 或 Studio 连接打印机，打开实况画面，确认实时画面可见且无异常。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
