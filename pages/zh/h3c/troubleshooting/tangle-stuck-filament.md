---
path: zh/h3c/troubleshooting/tangle-stuck-filament
title: "拓竹H3C 耗材缠料的处理办法"
description: ""
tags: []
created: 2026-11-03T12:09:02.530Z
updated: 2026-11-10T08:43:15.475Z
source: https://wiki.bambulab.com/zh/h3c/troubleshooting/tangle-stuck-filament
---

## 介绍

将缠结的耗材装入拓竹H3C 后，设备进料时可能出现"进料失败"等报错，或在打印过程中提示"挤出阻力异常"，“空打”等，此时需暂停打印，解开耗材缠结处后方可恢复正常工作。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-01.png)

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 方案一：直接解开

> 该方案适用于 AMS 2 Pro 或外挂料盘等场景。

请按住打结位置，固定打结部分后取出料盘。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-02.jpg)

卡住打结的耗材，同时从料盘中绕出，再解开缠绕。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-03.gif)

完成后将料盘放回 AMS，恢复打印。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-04.jpg)

当打印头回到吐料组件开始挤出时，需手动向内轻推耗材，直到感受到耗材被自动向内拉扯。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-05.png)

## 方案二：取下料盘解开

### AMS 3H

1. 拆下磁吸侧板。

|  |  |
| --- | --- |
| 图 | 图 |

2. 在屏幕上放置当前使用的打印头。若设备已放置打印头，请继续下一步。  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-08.png)
3. 从挂架上取下打印头，按住打印头刀柄切断耗材，再放回挂架；

> 注：此时热端温度较高，小心烫伤。

|  |  |
| --- | --- |
| 图 | 图 |

1. 切断耗材后再按压切刀下方，确保切刀回弹;  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-11.png)
2. 从 AMS 3 中抽回耗材, 理顺打结的缠料；  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-12.gif)
3. 将耗材插回 AMS 后，点击恢复打印，此时设备会自动完成送料、升温、挤出。  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-04.jpg)
4. 当打印头回到吐料组件开始挤出时，需手动向内轻推耗材，直到感受到耗材被自动向内拉扯。  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-05.png)

### AMS 2 Pro/AMS

从 AMS 中取下报错的耗材。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-15.png)

解开打结位置的缠料。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-12.gif)

将耗材插回 AMS 后，点击恢复打印，此时设备会自动完成送料、升温、挤出。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-17.png)

### 外挂料盘

1. 拆下磁吸侧板。

|  |  |
| --- | --- |
| 图 | 图 |

2. 在屏幕上放置当前使用的打印头。若设备已放置打印头，请继续下一步。  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-08.png)
3. 从挂架上取下打印头，按住打印头刀柄切断耗材，再放回挂架；

> 注：此时热端温度较高，小心烫伤。

|  |  |
| --- | --- |
| 图 | 图 |

1. 切断耗材后再按压切刀下方，确保切刀回弹;  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-11.png)
2. 从外挂料架上取下耗材, 理顺打结的缠料；  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-12.gif)
3. 完成后重新将耗材插入料管，并点击“恢复打印”。  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-25.png)
4. 从前侧观察打印头，确保耗材被完全推入。当耗材被成功送入打印头后，感受耗材是否会被自动向内拉。  
   ![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-26.png)

若耗材未被自动向内拉，请持续从进料处轻推耗材。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/tangle-stuck-filament/zh/07_h3c__________-27.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
