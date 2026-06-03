---
path: zh/h2s/manual/laser-upgrade-kit
title: "H2S 激光升级指南"
description: "本文介绍如何将标准版 H2S 升级为激光版本。"
tags: []
created: 2025-11-27T04:14:59.315Z
updated: 2026-05-29T04:04:15.932Z
source: https://wiki.bambulab.com/zh/h2s/manual/laser-upgrade-kit
---

## H2S 激光升级

若需将 H2S 升级至 H2SL 版本，仅需购置 10W 激光升级套装，并严格遵循本指南所述步骤执行操作。

激光升级的安装流程较为复杂，操作前，请务必仔细阅读本指南，并观看激光升级套件教学视频，确保您已完全掌握安装方法。

> **注意：** 本指南中部分示意图采用 H2D 机型相关图示，其核心安装逻辑与 H2S 一致，不会影响升级更换流程。

## 所需的工具和材料

- 激光升级套装
- H2.0 内六角扳手
- 所需时长 1 h

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[请点击此处提交技术工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)，我们将及时回复并为您提供所需的帮助。

## 操作步骤

### 激光升级套装开箱

- 打开纸箱；

![image-5.png](https://wiki.bambulab.com/h2/laser/image-5.png)

- 取出所有泡棉；

![20251127-221758_compressed.jpg](https://wiki.bambulab.com/h2s/manual/20251127-221758_compressed.jpg)

- 取出纸箱中所有配件，请参考下图：

> 注意：俯视摄像头卡扣和螺丝未在下图中标注，但升级套装中已包含。

1. 激光垫板
2. 顶部防护盖
3. 激光防护窗（前）
4. 支撑条\*6
5. 俯视摄像头
6. 内六角扳手 H2.5
7. 排烟管
8. 气管
9. 气泵连接线
10. 10 W 激光模组
11. 卡箍
12. 急停按钮
13. 清洁刷
14. 气泵
15. 排烟管转接件
16. 压紧块\*4

![20251204-230000_compressed.jpg](https://wiki.bambulab.com/20251204-230000_compressed.jpg)

### 更换激光防护视窗（前）

#### 移除前门玻璃

- 移除前门玻璃的 4 颗螺丝；

> 注意：移除最后一颗螺丝时，注意用手扶住前门，防止跌落损坏。

![](https://wiki.bambulab.com/h2/laser/image-8.png)

![](https://wiki.bambulab.com/h2/laser/image-7.png)

- 取下前门玻璃。

> 注意：取下或放置前门玻璃时，请小心，避免任何坚硬物体撞击玻璃门，注意保护玻璃边缘。

![](https://wiki.bambulab.com/h2/laser/image-4.png)

#### 安装激光防护视窗（前）

- 撕掉激光防护视窗（前）的保护膜；

![](https://wiki.bambulab.com/h2/laser/image-10.png)

- 将激光防护视窗对准螺丝孔放置；

![](https://wiki.bambulab.com/h2/laser/image-9.png)

- 用手将激光防护视窗固定到位，并与螺丝孔对齐，然后拧紧顶部和底部各两颗螺丝。

> 螺丝应拧紧到位，但不要拧得过紧。

![](https://wiki.bambulab.com/h2/laser/image.png)

![](https://wiki.bambulab.com/h2/laser/image-14.png)

- 安装完成后，拉开激光防护视窗（前）检查是否安装到位。

![](https://wiki.bambulab.com/h2/laser/image-11.png)

### 安装俯视摄像头

> **隐私提示**：请确保摄像头已正确安装，使摄像头视野正确朝向打印机腔体，以避免对打印区域或喷嘴的检测出现问题。

#### 固定俯视摄像头

- 移除一颗 AP 板盖固定螺丝；

![](https://wiki.bambulab.com/h2/laser/image-44.png)

- 打开 AP 板盖；

![](https://wiki.bambulab.com/h2/laser/image-51.png)

- 用内六角扳手将 LED 排线轻轻往里塞，避免安装俯视摄像头时压坏线缆；

![](https://wiki.bambulab.com/h2/laser/image-58.png)

- 安装俯视摄像头，将摄像头外壳的左右两个卡扣对准打印机上的两个小凹槽；

![](https://wiki.bambulab.com/h2/laser/image-49.png)

- 向上稍用力按压摄像头外壳，听到“咔”的一声，即为安装到位。

|  |  |
| --- | --- |
|  |  |

- 用无纺布擦拭镜头，清除灰尘。

![](https://wiki.bambulab.com/h2/laser/image-45.png)

#### 连接俯视摄像头线缆

- 撕下连接线背胶；

![](https://wiki.bambulab.com/h2/laser/image-50.png)

- 粘贴连接线时，需避开腔温传感器和火焰传感器；

![](https://wiki.bambulab.com/h2/laser/image-47.png)

> 注意：粘贴时需持续施加适当压力（建议 30 秒），确保连接线粘牢。
>
> ![](https://wiki.bambulab.com/h2/laser/image-48.png)

- 打开 AP 板上的黑色卡扣；

![](https://wiki.bambulab.com/h2/laser/image-70.png)

- 将俯视摄像头连接线从其他线缆后面穿过，连接至 AP 板；

![](https://wiki.bambulab.com/h2/laser/image-72.png)

- 按下卡扣将其锁定。

![](https://wiki.bambulab.com/h2/laser/image-69.png)

- 盖上 AP 板盖；

![](https://wiki.bambulab.com/h2/laser/image-71.png)

- 拧紧一颗固定螺丝；

![](https://wiki.bambulab.com/h2/laser/image-65.png)

- 撕下卡扣贴纸；

![撕下卡扣贴纸.png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/%E6%92%95%E4%B8%8B%E5%8D%A1%E6%89%A3%E8%B4%B4%E7%BA%B8.png)

- 将卡扣对准上盖的螺丝孔粘贴；

|  |  |
| --- | --- |
|  |  |

> 注意：粘贴时需持续施加适当压力（建议 15 秒），确保卡扣粘牢。  
> ![持续施压.png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/%E6%8C%81%E7%BB%AD%E6%96%BD%E5%8E%8B.png)

- 将另一个卡扣安装在俯视摄像头和第一个卡扣中间，并按紧；

![粘贴第二个卡扣.png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/%E7%B2%98%E8%B4%B4%E7%AC%AC%E4%BA%8C%E4%B8%AA%E5%8D%A1%E6%89%A3.png)

- 锁紧卡扣固定螺丝。

![锁紧卡扣螺丝.png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/%E9%94%81%E7%B4%A7%E5%8D%A1%E6%89%A3%E8%9E%BA%E4%B8%9D.png)

> 注意：有版本机器上没有预留螺丝孔位，只需将两个卡扣按要求粘紧即可。

### 安装气泵

> 注意区分气管长短，长气管上有贴纸。  
> ![](https://wiki.bambulab.com/h2/laser/image-60.png)  
> ![](https://wiki.bambulab.com/h2/laser/image-61.png)

- 将短气管一端插入 TPU 进料口中；

![](https://wiki.bambulab.com/h2/laser/image-62.png)

- 将气管固定在两个卡扣中；

![](https://wiki.bambulab.com/h2/laser/image-63.png)

- 插上气泵连接线；

![](https://wiki.bambulab.com/h2/laser/image-64.png)

- 将气泵的 4pin 线插入打印机的接口中；

![](https://wiki.bambulab.com/h2/laser/image-73.png)

- 将气管连接至气泵接口；

![](https://wiki.bambulab.com/h2/laser/image-81.png)

- 插到位后，轻轻摇动气管，确认连接牢固；

![](https://wiki.bambulab.com/h2/laser/image-84.png)

- 将气泵平放在桌面上。

![](https://wiki.bambulab.com/h2/laser/image-75.png)

### 安装排烟管

- 将排烟管转接件放在打印机背面的腔体外排风扇上，并拧紧 4 颗螺丝。

|  |  |
| --- | --- |
|  |  |

- 在排烟管一端套上卡箍，并将排烟管安装至排烟管转接件上，使其完全套住转接件。顺时针拧紧卡箍，将其固定在排烟管与转接件连接的部分。

|  |  |
| --- | --- |
|  |  |

- 装好后可尝试往回拉，以确认排烟管已完全锁紧。

![](https://wiki.bambulab.com/h2/laser/image-79.png)

### 安装急停按键

- 检查急停按键上是否也插入安全钥匙。

![](https://wiki.bambulab.com/h2/laser/image-80.png)

- 抬起打印机，将急停按键放在打印机边缘下方位置。

![](https://wiki.bambulab.com/h2/laser/image-76.png)

![](https://wiki.bambulab.com/h2/laser/image-78.png)

- 拔出打印机背面的安全钥匙，插入急停按键线缆。

|  |  |
| --- | --- |
|  |  |

### 激光模组开箱

- 打开激光模组；

![image_(28).png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/image_(28).png)

- 取出说明书和备用窗口镜；

![依次取出说明书和窗口镜.png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/%E4%BE%9D%E6%AC%A1%E5%8F%96%E5%87%BA%E8%AF%B4%E6%98%8E%E4%B9%A6%E5%92%8C%E7%AA%97%E5%8F%A3%E9%95%9C.png)

- 拉出左侧卡纸；

![image_(29).png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/image_(29).png)

- 取出激光模组；

![image_(30).png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/image_(30).png)

- 撕下激光模组保护套；

![image_(31).png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/image_(31).png)

- 撕下表面透明贴纸。

![image_(32).png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/image_(32).png)

### 安装激光模组

捏住工具头前盖底部位置，向前拉出，移除前盖。

![yichu.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/installation-laser/yichu.webp)

接下来移除旋转指示轮。

![indicating.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/installation-laser/indicating.png)

对准对应的槽位，将激光模组沿槽滑入，并按下锁紧扣固定。

![anzhaung.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/installation-laser/anzhaung.webp)

将线缆连接至工具头顶部连接器。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/maintenance/replace-toolhead-enhanced-cooling-fan/image-8_019.png)

> 注意：打印前务必撕下激光保护膜，并确认机舱内无异物或打印碎屑，避免激光点燃造成安全隐患。

![simo.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/installation-laser/simo.webp)

将气管一端连接至激光模组，另一端连接至打印机后方的气动接头。

![pixpin_2025-08-08_16-24-37.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/installation-laser/pixpin_2025-08-08_16-24-37.png)

![pixpin_2025-08-08_16-29-31.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/installation-laser/pixpin_2025-08-08_16-29-31.png)

安装完成后如下图所示。

![pixpin_2025-08-08_17-04-45.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/installation-laser/pixpin_2025-08-08_17-04-45.png)

### 俯视摄像头初始化

- 确保热床上无任何异物遮挡，尤其是视觉识别用的校准标记；

![](https://wiki.bambulab.com/h2/manual/laser-module-lnstallation-guide/image-47.png)

- 从 HMS 页面或“设置-工具箱”进入俯视摄像头初始化。  
  ![](https://wiki.bambulab.com/h2/manual/laser-module-lnstallation-guide/image-48.png)

### 安装激光垫板

- 将支撑条两端分别按压至激光垫板槽位中，听到“咔哒”声表明安装到位。每隔 4 个卡槽放一根支撑条。

|  |  |
| --- | --- |
|  |  |

- 将激光垫板放在热床上，确保激光垫板的两个识别标识与热床的限位块贴合。

|  |  |
| --- | --- |
|  |  |

### 放置顶部防护板

- 撕下顶部防护板保护膜；

![](https://wiki.bambulab.com/h2/laser/image-90.png)

- 放置顶部防护板。

![](https://wiki.bambulab.com/h2/laser/image-89.png)

### 激光模组初始化

- 将激光焦距标定卡纸放置在激光垫板后方中间位置，如下图所示。

![](https://wiki.bambulab.com/h2/manual/laser-module-lnstallation-guide/image-57.png)

- 从 HMS 页面或“设置-工具箱”进入激光模组初始化页面；

![jiguangmozuchushihua.png](https://wiki.bambulab.com/h2/laser/laser-upgrade-kit/jiguangmozuchushihua.png)

- 激光模组校准完成后，打开前门，取出激光焦距标定卡纸。

![](https://wiki.bambulab.com/h2/manual/laser-module-lnstallation-guide/image-61.png)

关于激光焦点标定的详细内容，请参考[激光焦点标定介绍](../../h2/manual/laser-focus-calibration-intro.md)。

## 附录

- H2S 激光升级相关 FAQ，请参考[激光升级套装 FAQ](../../h2/laser/manual/laser-upgrade-kit-FAQ.md)。
- 激光模组安装指南，请参考[激光模组安装指南（以10W激光模组为例）](../../h2/manual/laser-module-lnstallation-guide.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
