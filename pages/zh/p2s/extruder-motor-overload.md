---
path: zh/p2s/extruder-motor-overload
title: "P2S 挤出电机过载排查指南"
description: "本文将指导您排查挤出电机过载的错误。"
tags: ["p2s"]
created: 2026-02-05T07:57:02.620Z
updated: 2026-02-26T04:30:18.061Z
source: https://wiki.bambulab.com/zh/p2s/extruder-motor-overload
---

## 故障描述

在打印过程中，P2S 的挤出电机会实时监测挤出力的变化。当检测到挤出力过大时，会报错并暂停打印任务，需要用户排除故障后才能继续打印。

相关报错：[HMS\_0300-0900-0002-0001：挤出电机过载，可能堵头或者有耗材卡在工具头内。](troubleshooting/hmscode/0300_0900_0002_0001.md)

## 故障原因

1. 加热组件未正确安装
2. 模型翘边
3. 挤出机堵塞
4. 喷嘴堵塞

## 故障排查

### 检查首层打印质量

如果设备此时正在打印首层，请观察打印件外观是否和下图相似。如果存在较大面积的褶皱，请取消打印进行后续操作。

![image12.jpg](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image12.jpg)

1. 摘掉硅胶套，观察夹扣的扣紧方式是否正确。

|  |  |
| --- | --- |
| image2.1.png | image3.1.png |

2. 拧紧加热组件的 3 个固定螺丝，确保加热组件不会晃动。

![image01.png](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image01.png)

3. 正确安装喷嘴并合上卡扣

![image13.webp](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image13.webp)

4. 进行一次校准中的热床调平。

![image6.jpeg](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image6.jpeg)

如果仍然在热床特定位置处过低剐蹭热床，建议进行一次手动热床调平。具体可以参考该链接：[P2S 热床手动调平](maintenance/manual-bed-tramming.md)

### 检查模型是否发生翘边

如果模型某个角落发生翘边，那么喷嘴移动到该位置时，会直接刮蹭翘起的模型。这会导致喷嘴口无法正常挤出耗材，进而引发挤出电机过载。  
您可以参考[模型翘边](../knowledge-sharing/printed-model-warping.md)指南解决该问题，再重新发起打印。

![image7.jpg](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image7.jpg)

### 检查挤出机是否堵塞

当环境温度过高（超过 30℃）时，打印机腔内热量无法及时散出。如果打印 PLA、PETG 等耗材，耗材可能提前软化（[热蠕变](../filament-acc/filament/heat-creep.md)），并卡在挤出机齿轮内，导致挤出电机转动受阻，最终触发电机过载报警。

1. 将工具头前盖卡在 X 轴以及拖链中；

![image8.jpg](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image8.jpg)

2. 按压切刀刀柄，剪断耗材；

![image9.png](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image9.png)

3. 压下气动接头顶部，缓慢拔出料管；

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/cold-pull-maintenance-hotend/010.webp)

4. 拧松挤出机压块螺丝，轻轻拔出耗材；

![image4.png](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image4.png)

如果能够非常轻易地拔出耗材，并且外观不存在变形，那么挤出机并未堵塞。请装回耗材直到无法进一步插入后，再拧紧压块螺丝，进行步骤 4 。

![image5.png](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image5.png)

如果耗材无法拔出，请停止打印并参考 [P2S 挤出机堵塞清理指南](maintenance/extruder-cleaning-guide.md) 清理挤出机。

### 检查喷嘴是否堵塞

请在打印机屏幕上点击重试或恢复打印，观察喷嘴能否挤出耗材。

![image14.webp](https://wiki.bambulab.com/p2s/troubleshooting/extruder-motor-overload/image14.webp)

#### 情况 1：耗材无法挤出或存在卡滞

若耗材无法顺利挤出，则确定喷嘴存在堵塞。  
请参考 [P2S 喷嘴堵塞清理指南](maintenance/cold-pull-maintenance-hotend.md) 疏通喷嘴，并进行**多次冷拔**，直到冷拔出的耗材**没有杂质残留**。

> 可参考下图对比冷拔结果。  
> ![](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/image.png)

#### 情况 2：耗材顺利挤出

若喷嘴可以正常挤出耗材，则报错原因可能为喷嘴轻微堵塞、进料阻力过大或最大体积速度设置过快。

- 请参考[P2S 喷嘴堵塞清理指南](maintenance/cold-pull-maintenance-hotend.md) 疏通喷嘴并进行**多次冷拔**带出内部杂质，直到冷拔出的耗材**没有杂质残留**。
- 检查外部阻力，比如耗材缠绕，料管弯折等。  
  PVA、TPU 耗材的进料路径需要重点排查。如果您打印的耗材种类是 TPU，推荐您查看 [P 系列机器打印 TPU 90A & 85A 的打印指南](../filament-acc/filament/tpu-85a-90a-printing-guide-for-p-series.md) 再进行操作。并且建议每次使用 TPU 材料前，先进行 [P2S 喷嘴堵塞清理指南](maintenance/cold-pull-maintenance-hotend.md) ，以清除热端内部残留的杂质。
- 检查最大体积速度是否与所使用的热端类型相匹配；  
  例如，标准流量热端打印 Bambu PLA Basic 预设的最大体积速度是 25 mm³/s，而高流量热端打印 Bambu PLA Basic 的预设是 35 mm³/s。如果使用标准流量热端去打印高流量热端的参数，则会报错挤出电机过载。  
  同理 Bambu PETG Basic 和 Bambu PETG HF（高流量）也不能混用。第三方耗材建议降低该数值进行打印。

|  |  |
| --- | --- |
| image10.1.png | image11.png |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
