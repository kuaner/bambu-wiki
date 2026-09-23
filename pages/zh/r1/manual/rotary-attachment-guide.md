---
path: zh/r1/manual/rotary-attachment-guide
title: "R1 旋转轴附件加工指南"
description: "本文介绍了如何在 R1 上使用旋转轴附件进行加工"
tags: []
created: 2026-09-22T13:29:39.181Z
updated: 2026-09-22T13:29:40.435Z
source: https://wiki.bambulab.com/zh/r1/manual/rotary-attachment-guide
---

## 介绍

激光旋转轴加工是 R1 系列激光切割机的一项高级功能，需搭配旋转轴附件进行操作。该功能可实现在旋转体表面进行图案加工，常见于易拉罐、保温杯等各类回转体与环状物体的激光雕刻。

|  |  |
| --- | --- |
| 001.png | 002.png |

为确保定位精度和加工质量，在 R1 系列中，旋转轴附件必须搭配官方**旋转轴附件安装支架**使用。使用其他方式固定旋转轴附件可能导致一键准备失效、加工质量下降等问题。

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/003.png)

## 加工物体要求

在加工前，请确保待加工物体满足以下要求：

### 材质要求

- 不支持加工**高反光材质**（如镜面、亮面金属杯等），高反光材质在加工时反射激光可能导致工具头损坏；
- **透明材料可能会影响测量结果和加工质量**，如需加工该类材料，请谨慎确定测量结果，以免损坏材料。

### 几何要求

- **平滑曲面：** 不能有高度突变，高度突变区域可能导致测量误差较大、工具头与工件发生碰撞、表面加工质量不统一等问题；
- **尖角内斜角较难加工：** 尖角区域和内斜角区域可能导致表面加工质量不统一；

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/004.png)

- 物体轴线与物体中轴线夹角小于 40 度。

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/005.png)

## 加工范围限制

1. **最大加工长度**：500 mm

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/006.png)

2. **加工物体最小 & 最大直径**：57 mm & 105 mm

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/007.png)

3. **放置高度要求：**

- 物体上表面与工具头外壳底部的距离须 **≤ 6–7 cm**；

![008.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/008.png)

- 放在第三层（右图）时通常会超出该距离（极厚特殊工件除外），因此**推荐放置于第二层（左图）**，测量更准确；

|  |  |
| --- | --- |
| 009.png | 010.png |

## 固件/软件版本要求：

- 固件版本：01.01.00.00 （**该版本仅支持圆柱加工，旋转体加工将在后续版本中支持**）
- 软件版本：

## 加工流程

### 开箱

- 取出旋转轴附件泡棉；

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/011.png)

- 依次将三个卡爪插入卡盘中，并扣紧卡扣；

|  |  |
| --- | --- |
| 012.png | 013.png |

- 撕下支撑组件胶带，取出泡棉。

|  |  |
| --- | --- |
| 014.png | 015.png |

### 加工件安装

- 取下杯盖；

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/016.png)

- 用卡爪夹住加工件较宽的一端，旋转卡盘调节环，调至与加工件适配的尺寸，将其固定；

|  |  |
| --- | --- |
| 017.png | 018.png |

> 注：必要时也可调节卡扣，以适应加工件的尺寸大小。  
> ![019.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/019.webp)

- 旋转支撑组件上的固定旋钮，下降固定器；

![020.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/020.png)

- 旋转高度调节旋钮，下降支撑滑轮；

![021.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/021.png)

- 将右侧的球托拆卸，安装至支撑组件的上方位置；

|  |  |
| --- | --- |
| 022.png | 023.png |

- 将支撑组件插入旋转轴附件；

> 注意：
>
> 1. **支撑组件非必需安装**，需根据加工件的规格进行判断；若加工件较长或较重，建议安装支撑组件，避免因一端重力过大导致卡爪夹持不稳。
> 2. 安装支撑组件时需注意以下两点：
>
> - 不干涉加工件；
> - 确保安装方向正确。

![024.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/024.png)

- 旋转固定旋钮，固定支撑组件；

![025.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/025.png)

- 转动加工件，检查其是否偏心；如果存在偏心接触，需重新调整高度调节旋钮。

![026.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/026.webp)

- 松开旋转轴附件的角度固定旋钮，放置水平仪；

|  |  |
| --- | --- |
| 027.png | 028.png |

- 微调支撑组件上的高度调节旋钮，直至水平仪气泡居中；

|  |  |
| --- | --- |
| 029.png | 030.png |

- 可根据加工件的夹持偏心情况，适当旋紧角度固定旋钮。

> 注意：如果未使用支撑组件，则必须旋紧角度固定旋钮。

![031.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/031.png)

### 旋转轴附件安装

- 用双手按压左右卡扣，打开增高架前门；

|  |  |
| --- | --- |
| 032.png | 033.png |

- 放置托盘；

![034.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/034.png)

- 将线缆 “L” 端插入旋转轴附件；

![035.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/035.png)

- 将旋转轴附件对准增高架左侧的 4 个支架孔位；

|  |  |
| --- | --- |
| 036.png | 037.png |

锁紧螺丝；

![038.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/038.png)

- 打开旋转轴支架扳手；

![039.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/039.png)

将旋转轴附件卡入支架中，夹角处应卡入到位，确保牢固无松动；

|  |  |
| --- | --- |
| 040.webp | 041.png |

安装到位后，用力锁紧旋转轴支架扳手；

![042.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/042.png)

确认旋转轴附件是否安装牢固；

![043.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/043.png)

- 将旋转轴线缆另一侧插入图示接口处；

![044.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/044.png)

- 拆下工具头上的气嘴；

![045.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/045.png)

> **注意**：
>
> - 此步骤的目的是**为了增大加工范围，并防止气嘴在加工过程中碰撞旋转轴附件夹爪**；此外，也可将夹爪伸入杯内撑住杯子，同样可以避免夹爪碰撞气嘴。请参考下图：  
>   ![046.jpg](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/046.jpg)
> - 长期拆下气嘴加工可能导致聚焦镜脏污，注意及时清洁聚焦镜，请参考 wiki：[聚焦镜维护指南](focusing-lens-guide.md)。

- 关闭上盖。

![047.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/047.png)

### Bambu Suite 操作

- 在 Bambu Suite 中打开或者新建项目，在左上角选择工艺类型；

|  |  |
| --- | --- |
| 048.png | 049.png |

- 点击右下角“准备制作”按钮，进入摆盘页面；

![050.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/050.png)

- 根据物体实际形状，在“加工模式”中选择“圆柱体加工”；

> **注意**：“圆柱体加工”仅支持加工前后直径相同的圆柱体，非圆柱体可能影响加工质量和图案放缩比例。

![051.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/051.png)

- 选择对应材料后点击**一键准备**按钮；

![052.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/052.png)

机器将开启自动拍照测量；

> **注意**：
>
> - 确保上盖完全打开，旋转轴上方无遮挡；
> - 请确保电脑网络连接通畅，避免息屏或网络连接断开导致一键准备超时或展开图下载失败。

|  |  |
| --- | --- |
| 053.png | 054.png |

一键准备结束后，suite 画布上将会显示物体表面的平面展开效果，右下角会显示仿真图；

![055.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/055.png)

> **注意：一键准备时，需确保旋转轴放置水平，** 系统会自动检测旋转轴角度，屏幕上的旋转轴角度通常显示为绿色。如果显示的角度呈红色或橙色（角度过大或过小），则需及时调整；
>
> ![056.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/056.png)  
> 请使用 H1.5 内六角扳手拧动旋转轴螺丝，并同步观察屏幕，直至角度变为绿色。  
> ![057.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/057.png)

也可再次进行测距和测长操作；

- **测距**（快速测距）：

![058.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/058.png)

点击“快速测距”，机器将开始自动测距；

![059.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/059.webp)

- **测长**（手拖工具头测长）：

![revolve-measure.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/revolve-measure.png)

点击“手拖工具头长度测量”后，手拖工具头依次选中两个点：物体起始点和结束点；

> 注意：起始点和结束点均需对准杯子的边缘位置，才能获得准确的展开图。

![061.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/en/061.webp)

机器会自动测量出选中的长度，确认后将自动填写至 suite 中；

![060.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/060.png)

- 可对图案执行旋转或缩放操作，将其拖动至目标加工区域；拖动右下角的仿真图，即可预览加工完成后的预期效果；

![063.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/063.webp)

- 在右侧选择加工材料类型；

![choose-material.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/choose-material.png)

- 屏幕右下角有“预览”和“走边框”按钮；

![065.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/065.png)

点击“**预览**”按钮，可预览加工路径；

![064.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/064.png)

点击“**走边框**”按钮，工具头将自动进行走边框预演；

![067.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/en/067.webp)

- 点击右下角“**制作**”按钮，确认旋转轴安装到位、气嘴已拆卸后，点击“**发送**”，即可启动加工流程。

![066.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/066.png)

- 等待制作完成。

![069.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/069.webp)

### 加工后操作

- 加工结束后，旋转卡盘调节环，即可取下加工件；

![070.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/en/070.png)

- 可用纸巾擦拭加工物表面灰尘。

|  |  |
| --- | --- |
| 071.png | 072.png |

## 注意事项

1. 若杯子带有可拆卸把手，为确保更好的加工效果，**请先将把手拆卸**；
2. 为了保证更好的加工效果，**建议不要将卡爪放置在加工件正上方**，防止碰撞；
3. 完成拍照后，**请勿移动旋转轴附件或工件**；若出现以上操作，请重新拍照再进行加工；
4. 不支持球体、戒指类小物体加工。

## 异常排查

> **注意**：请确认使用官方**旋转轴附件安装支架固定旋转轴附件，并夹持到位。**

### 雕刻过程中线条抖动

1. 检查旋转轴安装是否牢固，工件夹持是否牢固；
2. 检查旋转轴附件底板表面是否粘附杂物；
3. 检查旋转轴附件底板脚垫是否齐全；
4. 检查加工参数设置，对于较重的工件，可以适当调小 U 轴加速度以及加工速度。

### 填充雕刻中图案出现重影或错位

1. 如果是手动设置参数，检查参数是否设置正确，推荐采用一键准备进行参数测量；
2. 检查使用支撑附件时，角度固定旋钮是否处于松开状态；
3. 如果加工件带有不可拆卸把手，检查把手在加工过程中是否与激光模组发生碰撞；
4. 使用卡爪固定加工件时，检查卡爪是否将加工件顶紧，确认加工件转动时无摇晃、位移情况；
5. 确认加工环境周边无明显震动的设备。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
