---
path: zh/h3c/maintenance/replace-dock-alignment-sensor
title: "泊位标定传感器更换指南"
description: ""
tags: []
created: 2026-11-03T13:07:02.846Z
updated: 2026-11-03T13:07:03.898Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-dock-alignment-sensor
---

## 泊位标定传感器

用于检测打印头上的泊位标定磁铁，以此来精确标定每个打印头的泊位坐标。  
![img_c5d82b593260.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-dock-alignment-sensor/zh/img_c5d82b593260.jpg)

## 何时更换

- 泊位标定传感器的排线损坏。
- 经 Bambu Lab 技术支持分析需更换泊位标定传感器。

## 工具和材料

- H1.5 内六角扳手
- 镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除泊位标定传感器

### 第 1 步 移除工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，移除 工具头前盖和顶盖。  
![img_88cc28be87ee.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-dock-alignment-sensor/zh/img_88cc28be87ee.jpg)

### 第 2 步 松出连接线缆

将风扇线缆、裹头检测传感器线缆和工具识别传感器排线从接口板上断开，用镊子轻微掰开热端风扇的线缆卡扣。

|  |  |
| --- | --- |
| img_40edab626023.jpg | img_f4d825b1f6d1.jpg |

将热端风扇线缆从卡扣上松出，再将裹头检测传感器线缆从另一边的卡扣中松出。

|  |  |
| --- | --- |
| img_047e04bb9c74.jpg | img_5dfecf0445f9.jpg |

### 第 3 步 移除泊位标定传感器

从挤出接口板上打开连接器盖子，断开泊位标定传感器的连接线

|  |  |
| --- | --- |
| img_fdea821d5e14.jpg | img_e5524855e750.jpg |

用 H1.5 内六角扳手移除 2 颗螺丝，移除金属支架。

|  |  |
| --- | --- |
| img_1390c6991a7b.jpg | img_e245498d79d4.jpg |

用 H1.5 内六角扳手移除 1 颗螺丝，移除泊位标定传感器保护盖，然后用镊子将泊位标定传感器沿着线槽上撕下。

|  |  |
| --- | --- |
| img_0adf94ac343a.jpg | img_438d33fc0cb4.jpg |

## 安装泊位标定传感器

> 温馨提示：
>
> 1. 新的泊位标定传感器背面有保护胶纸，在安装前需要撕掉，露出背胶；
> 2. 新的泊位标定传感器在安装前可参考图中白线位置进行折弯，方便安装。
>
> |  |  |
> | --- | --- |
> | img_a7da3a7ea16f.jpg | img_b018911d66a5.jpg |

### 第 1 步 安装泊位标定传感器

将泊位标定传感器安装到支架上，对齐安装导向柱，装上保护盖，并锁入 1 颗螺丝固定。

|  |  |
| --- | --- |
| img_11a0fe179d00.jpg | img_4f1e94be04db.jpg |

将排线沿着线槽进行安装，然后将金属支架也安装到线槽中，注意泊位标定传感器在上部弯折的位置要塞到支架在该位置向下的卡扣中。

|  |  |
| --- | --- |
| img_72e92dbbb251.jpg | img_568ab9f350c3.jpg |

检查确认螺丝孔对齐，依次锁入 2 颗螺丝，固定金属支架。

|  |  |
| --- | --- |
| img_f19c131ae315.jpg | img_143a4c38e1fc.jpg |

将排线连接到挤出接口板的连接器上，通过白线检查确认排线插到位，合上盖子。

|  |  |
| --- | --- |
| img_1b6ace3d3699.jpg | img_fdea821d5e14.jpg |

### 第 2 步 连接线缆

将裹头检测传感器和热端风扇的线缆依次整理到金属支架上。

|  |  |
| --- | --- |
| img_83eae36f8c76.jpg | img_1eff7c5a3fc8.jpg |

用镊子调整拆装时撬开的卡扣，使线缆不能轻易松出。

|  |  |
| --- | --- |
| img_1e903c932813.jpg | img_5c0d7da1be51.jpg |

最后将线缆按图中序号依次连接到挤出接口板上，连接中单的排线时，也是通过白色标线来确认排线连接到位。

|  |  |
| --- | --- |
| img_fe2aa118b438.jpg | img_1513b2ae99bc.jpg |

### 第 3 步 安装工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，安装 工具头顶盖和前盖。  
![img_3f758f3bab87.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-dock-alignment-sensor/zh/img_3f758f3bab87.jpg)

## 功能验证

启动打印机，执行一次挂架对位校准，能正常完成却可。  
![img_d660e36ef043.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-dock-alignment-sensor/zh/img_d660e36ef043.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
