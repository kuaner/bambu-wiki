---
path: zh/h2/manual/rotary-attachment-guide
title: "H2 系列激光旋转轴加工指南"
description: "本文介绍了如何使用激光旋转轴加工功能"
tags: []
created: 2026-01-22T02:30:28.157Z
updated: 2026-04-23T02:27:24.176Z
source: https://wiki.bambulab.com/zh/h2/manual/rotary-attachment-guide
---

## 激光旋转轴加工介绍

激光旋转轴加工是 H2 系列打印机的一项高级功能，需搭配旋转轴附件进行操作。该功能利用高精度激光模组、测高激光器以及旋转轴附件，实现在旋转体表面进行图案加工，常见应用于易拉罐、保温杯等各类回转体与环状物体的激光雕刻。

![20260127-121620.jpg](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/20260127-121620.jpg)

> 目前仅 H2DL 以及 H2SL 支持使用旋转轴组件，H2CL需等待后续固件更新。

## 激光旋转轴加工雕刻材料要求

在加工物体之前，请确保材料形状与材质符合以下要求：

### 表面特性

- 平滑曲面，不能有剧烈起伏（最大支持 15mm 高度差）；
- 物体轴线与物体中轴线夹角小于 40 度。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-10.png)

### 几何限制

- 材料不能有高度突变（例如阶跃超过 3mm 的阶梯状物体）；
- 尖角、内斜角区域较难加工。

### 材质限制

**不支持透明材质**（如普通玻璃、透明亚克力等）**和镜面材质**（如强反光金属、镜子等）。测高激光器在扫描透明或镜面材质物体时可能出现噪声或异常，如需加工此类物体，请谨慎确认扫描结果。**若扫描结果异常，请勿继续加工**，以免损坏材料。

## 激光旋转轴加工雕刻范围限制

- **加工物体最小 & 最大直径：57mm & 105mm**

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-8.png)

- **最大加工长度：220mm（H2D）**

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-9.png)

- **最大可调节加工角度：45°**

可通过打印机屏幕查看旋转轴角度。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image.png)

## 激光旋转轴加工模式

激光旋转轴加工包含两种模式，可根据加工件的外形特征选择对应的模式。

### 旋转体加工

适用于表面具有凹凸起伏的回转体，如圆台形杯体（杯口与杯底直径不同，呈一端大、一端小的锥台状结构）、花瓶等。该模式强依赖测量。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image_tips_revolve_shape.png)

### 圆柱加工

适用于圆柱型物体，如易拉罐等。该模式可通过手动输入半径、高度及长度进行加工，不强制依赖测量。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image_tips_cylinder.png)

## 激光旋转轴加工流程

### 加工前准备

为了获得更好的加工精度，加工前请点击屏幕**设置 > 工具箱**，进行俯视摄像头初始化以及激光模组初始化或者挂载校准操作。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-1.png)

### 开箱

- 取出旋转轴附件泡棉；

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-2.png)

- 依次将三个卡爪插入卡盘中，并扣紧卡扣；

|  |  |
| --- | --- |
|  |  |

- 撕下支撑组件胶带，取出泡棉。

|  |  |
| --- | --- |
|  |  |

### 加工件安装

- 取下杯盖；

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-7.png)

- 用卡爪夹住加工件较宽的一端，旋转卡盘调节环，调至与加工件适配的尺寸，将其固定；

|  |  |
| --- | --- |
|  |  |

> 注：必要时也可调节卡扣，以适应加工件的尺寸大小。
>
> ![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/%E8%B0%83%E8%8A%82%E5%8D%A1%E6%89%A3.webp)

- 旋转支撑组件上的固定旋钮，下降固定器；

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-15.png)

- 旋转高度调节旋钮，下降支撑滑轮；

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-16.png)

- 将右侧的球托拆卸，安装至支撑组件的上方位置；

|  |  |
| --- | --- |
|  |  |

- 将支撑组件插入旋转轴附件；

> 注意：
>
> 1. **支撑组件非必需安装**，需根据加工件的规格进行判断；若加工件较长或较重，建议安装支撑组件，避免因一端重力过大导致卡爪夹持不稳。
> 2. 安装支撑组件时需注意以下两点：
>
> - 不干涉加工件；
> - 确保安装方向正确，**装反则会遮挡旋转轴附件定位标识**，进而引发后续报错。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-19.png)

- 旋转固定旋钮，固定支撑组件；

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-20.png)

- 转动加工件，检查其是否偏心；如果存在偏心接触，需重新调整高度调节旋钮。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/%E5%81%8F%E5%BF%83.webp)

- 松开旋转轴附件的角度固定旋钮，放置水平仪；

|  |  |
| --- | --- |
|  |  |

- 微调支撑组件上的高度调节旋钮，直至水平仪气泡居中；

|  |  |
| --- | --- |
|  |  |

- 可根据加工件的夹持偏心情况，适当旋紧角度固定旋钮。

> 注意：如果未使用支撑组件，则必须旋紧角度固定旋钮。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-25.png)

### 旋转轴附件放置

> 注意：安装旋转轴附件时需注意接线与安装位置，附件应安装在激光垫板的特定位置。

- 将线缆的“L”形插头插入旋转轴附件上；

|  |  |
| --- | --- |
|  |  |

- 将旋转轴附件放进打印机中，对准激光垫板固定销（旋转轴附件卡槽位置）放置，并且确保激光垫板无位移；

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-28.png)

确保附件卡入固定销位置并保持水平。

|  |  |
| --- | --- |
|  |  |

> **注意：**  
> **旋转轴附件必须卡在固定销位置，并与前门平行摆放。** 以下为错误摆放：
>
> ![错误摆放](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-30.png)
>
> 若摆放位置不正确或定位标识被遮挡，俯视摄像头将无法在特定范围内扫描到定位标识，系统则会显示相关报错。
>
> |  |  |
> | --- | --- |
> | 旋转轴附件定位标识 |  |

- 将旋转轴线缆另一侧插入图示接口处，并关闭前门和上盖。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-32.png)

### Bambu Suite 操作

#### 旋转体加工模式

- 在 Bambu Suite 中打开或者新建项目，可适当调整图案大小；

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-33.png)

- 点击右下角“准备制作”按钮，进入摆盘页面；

|  |  |
| --- | --- |
|  |  |

- 在“加工模式”中选择“旋转体加工”；

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-36.png)

- 选择对应材料后点击拍照按钮；**拍照过程中请确保电脑保持亮屏状态，否则可能引发电脑断网，导致软件无法接收设备指令，造成拍照超时。**

|  |  |
| --- | --- |
|  |  |

##### **拍照过程的注意事项**

1. 拍照测量时，前门必须保持关闭状态。
2. 拍照前系统会先检查旋转轴是否摆放正确，若确认位置无误，可直接跳过弹窗。
3. 拍摄后显示的图像为物体表面的平面展开效果，图中的中轴线对应加工件的正上方位置。

|  |  |
| --- | --- |
|  |  |

4. **拍照测量时，需确保旋转轴放置水平且与设备前门保持平行，并保证旋转轴俯仰角度接近 0°，以保障测量精度**。若未满足上述条件，会导致测量结果偏差，进而影响最终雕刻质量。若未将俯仰角调至水平，仅使加工件上表面保持水平，则针对圆台形加工件的测量会出现误差，设备会误将其识别为前后直径一致的圆柱体。

![通过角度固定旋钮调节旋转轴角度](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/img_v3_02u4_9d5dc138-7225-4d1e-9f17-1e222748320g.jpg)

可在屏幕控制界面查看俯仰角度数：

|  |  |
| --- | --- |
|  |  |

5. 当前，针对反光度较高或长度较短的物体进行拍照测量时，可能出现测量不稳定的情况。该问题将在后续软件版本中进行优化。

- 拍照完成后，Suite 将显示展开图以及三维仿真图（右下角）。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-43.png)

> 注：材料上下方的空白区域即材料展开后的表面区域。  
> ![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-44.png)

- 可对图案执行旋转或缩放操作，将其拖动至目标加工区域；拖动右下角的仿真图，即可预览加工完成后的预期效果。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/%E4%B8%89%E7%BB%B4%E4%BB%BF%E7%9C%9F%E5%9B%BE.webp)

- 点击右下角“制作”按钮，确认激光模组、激光垫板及旋转轴均已安装到位后，点击“发送”，即可启动加工流程。

|  |  |
| --- | --- |
|  |  |

#### 圆柱加工模式

圆柱加工与旋转体加工模式类似，区别在于加工件右侧的直径、高度及长度可通过手动输入设定（也可选择拍照自动测量）。

![](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/image-47.png)

**如果需要以圆柱模式加工圆台，可通过调整俯仰角的方法快速启动加工流程**，请参考以下步骤：

- 松开角度固定旋钮。

![角度固定旋钮.jpg](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/%E8%A7%92%E5%BA%A6%E5%9B%BA%E5%AE%9A%E6%97%8B%E9%92%AE.jpg)

- 调节俯仰角，使圆台朝上的一侧与激光模组保持平行，以此保证加工面的均匀性与精度。

> 建议借助水平仪进行平行度的辅助检查。

|  |  |
| --- | --- |
| 调节前 | 调节后 |

- 点击屏幕"控制 > 旋转轴"，查看俯仰角度，**绿色代表最佳可加工俯仰角度，角度过大在拍照阶段可能会被拦截。** 然后轻旋角度固定旋钮固定。

> 注：离线加工模式下设备不触发拦截机制，仅在拍照阶段进行拦截。

|  |  |
| --- | --- |
|  |  |

在水平状态下，屏幕上的旋转轴角度通常显示为绿色；如果显示的角度呈红色或橙色（角度过大或过小），如下图：

![screenshot-20260202-164611.png](https://wiki.bambulab.com/h2/manual/rotary-attachment-guide/screenshot-20260202-164611.png)

请使用 H1.5 内六角扳手拧动旋转轴螺丝，并同步观察屏幕，直至角度变为绿色。

|  |  |
| --- | --- |
|  |  |

> 注意：非必要请勿拧动此螺丝，以免影响加工精度。

### 加工后操作

加工结束后，旋转卡盘调节环，即可取下加工件。

|  |  |
| --- | --- |
|  |  |

## 激光旋转轴加工注意事项

1. 若杯子带有可拆卸把手，为确保更好的加工效果，**请先将把手拆卸**；
2. 为了保证更好的加工效果，**建议不要将卡爪放置在加工件正上方**；
3. 完成拍照后，**请勿移动机箱内物体或者升降热床**；若出现以上操作，请先重新拍照再进行雕刻；
4. 不支持球体、戒指类小物体加工。

## 激光旋转轴加工异常排查

### 雕刻过程中线条抖动

1. 检查激光垫板是否平整、表面有无脏污；
2. 检查旋转轴附件底板表面是否粘附杂物；
3. 检查旋转轴附件底板脚垫是否齐全；
4. 检查旋转轴附件的摆放位置是否正确，确认摆放处无凹槽，放置单侧脚垫悬空；
5. 检查加工件的夹持状态，确认无偏心问题。

### 填充雕刻中图案出现重影或错位

1. 检查使用支撑组件时，角度固定旋钮是否处于松开状态；
2. 如果加工件带有不可拆卸把手，检查把手在加工过程中是否与激光模组发生碰撞；
3. 使用卡爪固定加工件时，检查卡爪是否将加工件顶紧，确认加工件转动时无摇晃、位移情况；
4. 确认加工环境周边无明显震动的设备。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
