---
path: zh/h2d/manual/cutting-upgrade-kit
title: "H2D 刀切升级套件使用指南"
description: ""
tags: []
created: 2025-08-21T07:12:05.900Z
updated: 2026-03-23T01:31:17.148Z
source: https://wiki.bambulab.com/zh/h2d/manual/cutting-upgrade-kit
---

> **特别说明：** 由于 H2D 及刀切升级套件均未配备俯视相机，因此在 Bambu Suite 中无法使用拍照功能；但这并不影响刀切和画笔功能的正常运行，仅会导致无法实现切割坐标与实际位置的精准对齐。  
> 对此，我们推荐您使用 Bambu Suite 中的 [“打印后刀切”](../../h2/manual/post-printing-cutting.md)工艺 —— 该方式可借助工具头摄像头与打印生成的 marker 定位图案进行精准定位，从而实现更高精度的切割效果。  
> ![](https://wiki.bambulab.com/h2/post-printing-cutting/image-3.png)  
> 若 H2D 已经加装了俯视相机，可在刀切模组下运行俯视相机校准功能。而 H2C 和 H2S 仍需在激光模组下，才能运行俯视相机校准功能。我们会在未来的固件更新中，实现刀切模组与俯视相机的适配支持。

## 刀切模组安装

### 1. 安装刀切垫板

取下纹理 PEI 打印板（若当前热床位置较高，可通过屏幕操作适当降低热床高度，以便取放打印板）。

|  |  |
| --- | --- |
|  |  |

根据所使用的耗材类型，选择对应的粘板面朝上并撕掉表面保护膜（与热床贴合一侧的保护膜请勿撕下）。将刀切垫板安装至热床上，确保其两个角与热床的限位块紧密贴合。

请妥善保管撕下的保护膜，在不使用刀切垫板时，可将保护膜贴回粘性面，以防止粘附杂物，保持垫板粘性。

![](https://wiki.bambulab.com/h2/manual/cutting-module-installation-guide/image-8.png)

|  |  |
| --- | --- |
|  |  |

### 3. 安装刀切模组

捏住工具头前盖的顶部2个角，向前拉出以移除工具头前盖。

|  |  |
| --- | --- |
|  |  |

沿着挤出机前盖槽位滑入刀切组件，

|  |  |
| --- | --- |
|  |  |

若无法下压锁扣，需用H2.0 扳手逆时针拧松螺丝半圈，使锁扣放松，再次下压确认，如仍然过紧，再放松半圈，直至顺利锁紧。

|  |  |
| --- | --- |
|  |  |

若锁扣出现晃动的，需用H2.0 扳手顺时针拧紧螺丝半圈，使锁扣压紧，再次晃动确认，如仍然过松，再拧紧半圈，直至顺利不再晃动。

|  |  |
| --- | --- |
|  |  |

取下刀架上的保护套，请小心操作避免受伤。同时，建议保存该保护套，用于拆装时包裹整个刀架。

![](https://wiki.bambulab.com/h2/manual/cutting-module-installation-guide/image-18.png)

打开工具头扩展接口处的防尘盖，将连接线插入接口。

![](https://wiki.bambulab.com/h2/manual/cutting-module-installation-guide/image-21.png)

### 4. 刀切模组挂载校准

插入刀切模组的线缆后，若出现固件升级提示，请先完成固件升级，再点击刀切模组进行挂载校准。

> 注意：在进行刀切模组挂载校准时，必须安装刀架和刀头，切勿安装画笔模组。

|  |  |
| --- | --- |
|  |  |

更多详细开箱安装使用教程可查看。[刀切/画笔主要部件和使用流程介绍](../../h2/manual/cutter-setup.md)

## 发起加工任务

您需要下载安装 [Bambu Suite](https://bambulab.cn/zh-cn/download/suite) ，并完成Bambu Suite与打印机的绑定，您可以通过扫码二维码或者使用局域网进行绑定。  
绑定完成后，您可以在此页面添加需要切割的图案。  
![zh4.png](https://wiki.bambulab.com/h2/cutting-upgrade-kit/zh3.png)  
接下来进入准备界面，选择相对应的材料，并进行预览。

> 由于缺少俯视相机及拍照功能，材料与待切割图案无法实现精准对齐，因此建议将待切割图案居中摆放。

![zh4.png](https://wiki.bambulab.com/h2/cutting-upgrade-kit/zh4.png)

确认切割路径无误后，点击“制作”即可进行加工任务。  
![zh5.png](https://wiki.bambulab.com/h2/cutting-upgrade-kit/zh5.png)

![20250821-162740.webp](https://wiki.bambulab.com/h2/cutting-upgrade-kit/20250821-162740.webp)

> 除了此种加工方式外我们还推荐您使用[“打印后刀切”](../../h2/manual/post-printing-cutting.md)。

## 安装画笔模组（如需使用绘画功能）

取下画笔转接件上的定高块，并安装至转接件的下方

|  |  |
| --- | --- |
|  |  |

逆时针拧松画笔锁定器，将画笔插入到底后，顺时针拧紧锁定器。

|  |  |
| --- | --- |
|  |  |

移除和安装工具取下刀架时，您可以使用3D打印的刀架和刀片辅助工具。如果您没有打印工具，取下刀架时，需握住刀架的圆形边缘,向下将其拔出。刀头十分锋利,请小心操作,避免受伤!

|  |  |
| --- | --- |
|  |  |

将画笔插入刀切模组。

![](https://wiki.bambulab.com/h2/manual/cutting-module-installation-guide/image-35.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
