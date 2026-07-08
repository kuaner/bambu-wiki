---
path: zh/p2s/maintenance/replace-filament-buffer
title: "更换 P2S 缓冲器"
description: "本文介绍了如何更换 P2S 缓冲器"
tags: ["缓冲器"]
created: 2025-10-14T12:50:21.570Z
updated: 2026-06-22T09:59:27.384Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-filament-buffer
---

## 缓冲器

缓冲器是安装在打印机背面，用于缓解进料过程中的张力波动，确保进料顺畅的专用配件。  
![sa011.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/sa011.jpg)

## 何时更换

- 缓冲器元器件或结构件出现明显损坏，并导致功能失效；
- 经过技术支持的分析确认，需要更换缓冲器。

## 所需的工具和材料

- 新的缓冲器
- H2.0 内六角扳手

## 移除缓冲器

### 第1步：移除铁氟龙管

按压左侧料管接头，移除进料铁氟龙管。  
![remove_ptfe_tube_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/filament_buffer/remove_ptfe_tube_001.png)  
向出料方向推动缓冲滑块，露出料管接头，按压接头，移除出料铁氟龙管。  
![remove_ptfe_tube_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/filament_buffer/remove_ptfe_tube_002.png)

> 如果您感觉到操作困难，可以打印[辅助工具](https://makerworld.com.cn/zh/models/2037378-p2s-huan-chong-qi-chu-liao-tie-fu-long-guan-fu-zhu#profileId-2273508)，这会更加方便拆卸右侧的料管。  
> ![p2s-buffer-tool.webp](https://wiki.bambulab.com/p2s/maintenance/buffer-cleaning/p2s-buffer-tool.webp)

### 第2步：移除缓冲器

用内六角扳手移除2颗螺丝。  
![2_screws_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/filament_buffer/2_screws_005.png)  
将缓冲器翻转过来，露出连接线，用手按压连接器锁扣，拔出连线电缆，取下缓冲器。  
![filament_buffer_cable_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/filament_buffer/filament_buffer_cable_006.png)

## 安装缓冲器

> ℹ️ 若缓冲器安装的位置有硅胶塞，请先移除硅胶塞，可使用内六角扳手辅助操作。
>
> |  |  |
> | --- | --- |
> |  |  |

### 第1步：安装缓冲器

将连接线连接到缓冲器的连接器上，注意确认锁扣的方向。  
![connect_cable_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/filament_buffer/connect_cable_007.png)  
将缓冲器扣到背板安装孔上，用内六角扳手锁上2颗螺丝。  
![install_filament_buffer_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/filament_buffer/install_filament_buffer_008.png)

### 第2步：连接铁氟龙管

重新连接缓冲器两侧的铁氟龙管。  
![connect_petf_tube_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/filament_buffer/connect_petf_tube_004.png)  
![connect_ptfe_rube_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/filament_buffer/connect_ptfe_rube_003.png)

## 如何验证完成/成功

启动打印机，使用 AMS 发起一次上料操作，如果可以正常完成上料流程，则更换成功。  
否则，请检查缓冲器的连接线与铁氟龙管是否连接正确，然后重试。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（工作日 9:00-21:00；节假日 9:00-18:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
