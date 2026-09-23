---
path: zh/r1/manual/offline-processing-guide
title: "R1 离线加工指南"
description: "本文介绍了 R1 离线加工步骤"
tags: []
created: 2026-09-22T12:48:59.017Z
updated: 2026-09-22T12:49:00.228Z
source: https://wiki.bambulab.com/zh/r1/manual/offline-processing-guide
---

## 离线加工功能介绍

离线加工不依赖网络，可直接从**设备内部存储**中发起加工任务，也可通过局域网或线缆，从 Bambu Suite 端发起加工。

在离线加工场景下，大量信息被固化在加工文件中，用户可调范围小，因此通常只能针对**完全相同****的****材料、在完全相同的位置、用完全相同的激光参数**进行加工，灵活度大大折扣，体验往往不佳。R1 通过提供走边框、手动调整等功能，显著提升了离线加工在**离线加工位置优化**方面的灵活性。

## 从软件端发起加工

### 步骤 1：连接机器

**方法一：** 通过 **USB 线缆**连接机器的 USB-C 接口与电脑，即可在未联网的情况下发起加工任务；

> 注意：如果使用未通过 USB‑IF 认证的线缆，可能导致设备无法识别。

|  |  |
| --- | --- |
| 001.png | 002.png |

**方法二：** 在机器屏幕点击 **“设置 > 仅局域网”**，开启局域网模式；

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/003.png)

打开 Bambu Suite，使用 PIN 码或 IP 和访问码连接机器。

|  |  |  |
| --- | --- | --- |
| 004.png | 005.png | 006.png |

### 步骤 2：开启加工

此时可正常开启加工：导入或选择需要加工的内容，一键准备，选择模式和材料，确认参数后即可进行加工。

|  |  |
| --- | --- |
| 007.png | 008.png |

## 从屏幕端发起加工

### **步骤 1：选择离线文件**

- 在首页左侧点击“**文件”** 图标，进入历史缓存页面；

> 注意：“文件”中均为历史加工任务。

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/009.png)

- 此页面将列出所有已下载到本地的离线任务（不论加工成功与否），点击想要加工的文件；

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/010.png)

- 屏幕会显示该加工文件详细信息，确认后点击“**下一步”** 进入调整页面。

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/011.png)

> 注意：无法查看第三方文件（从 Bambu Suite 中发送的 `.gcode` 文件）的加工信息，仅能直接发起离线加工。
>
> ![012.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/012.png)

### **步骤 2：调整加工位置/走边框预演（可选****步骤****）**

#### **平面加工模式**

如果加工模式为平面加工，左下角的“手动调整功能”将**默认开启**，按钮呈绿色，且光标会出现红十字。

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/013.png)

- 如果需要调整加工位置，则需手拖工具头来确定；拖动时，可根据红十字光标的投影确认加工对象的具体位置；

![014.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/014.webp)

> 注意：如果加工区域置红且右上角 **“制作”** 按钮置灰，则表示物体超出加工区域，无法进行加工。
>
> ![015.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/015.png)

确定后，建议点击 **“走边框”** 进行预演，系统将以工具头坐标位置为中心点，沿预设的走边框路径移动，红十字光标随之投射出完整的轨迹；

|  |  |
| --- | --- |
| 016.png | 017.webp |

观察投影路径是否在材料的预加工范围内；若需微调，可继续移动工具头后再次进行走边框。

![018.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/018.png)

- 如果无需调整，可直接按照加工文件的位置发起加工，则需**关闭“手动调整功能”**，否则**机器默认在工具头位置加工**；

|  |  |
| --- | --- |
| 019.png | 020.png |

关闭“手动调整功能”后，红色十字光标将消失，走边框区域和加工区域都会回到加工文件原本位置，不受工具头位置影响。

|  |  |
| --- | --- |
| 021.png | 022.webp |

#### 其他加工模式

由于**其他加工模式不支持“手动调整功能”**，因此，进入“预览加工位置”页面后，只能在**加工文件原位置**进行走边框预演或直接进行加工。

![023.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/023.png)

建议点击 **“走边框”** 按钮进行预演，然后根据工具头位置摆放材料。

![024.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/024.webp)

放置耗材后，进行二次走边框，检查投影路径是否在材料的预加工范围内。

![025.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/025.webp)

### **步骤 3：发起离线加工**

确认加工位置后，点击“\*\*制作”\*\*按钮，开启加工。

![026.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/026.png)

## **加工与走边框的范围限制**

由于气嘴和选点激光在工具头上的位置不同，走边框的检测范围与实际加工的可达范围并不完全相同；此外，选点激光光路并非垂直向下，会使偏移量随材料高度产生额外波动，所以**实际的可加工区域**和\*\*红十字激光可达区域（可走边框区域）\*\*并不完全相同，两者之间存在`[24.5 mm, ‑7.7 mm]`的固定偏移，可参考以下示意图：**①** 为激光可加工区域，**②** 为红十字激光可达区域。

![027.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/027.png)

因此，预览加工位置时可能出现以下两种异常，对应的界面表现如下：

- **无法加工**：加工区域边框变红，右上角\*\*“制作”\*\*按钮置灰；

![028.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/028.png)

- **无法走边框**：点击 **“走边框”** 按钮后屏幕报错，提示有工具头碰撞风险。

![029.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/029.png)

> **注意：** 以上判断仅在 **开启“手动调整功能”** 时生效。若未开启该功能，只要文件已成功下载到本地，点击 “**制作”** 时，系统不会检查坐标是否超出加工区域，工具头会移动到历史加工位置进行加工，因此文件必然可以直接启动加工。

由于两块区域范围不同，开启手动调整功能后，机器可能处于以下四种状态：

| **工具头是否在加工区域内** | **工具头是否在红十字激光可达区域内** | **结果** | **示意图** |
| --- | --- | --- | --- |
| 是 | 是 | 加工✔，走边框✔ | Image |
| 是 | 否 | 加工✔，走边框❌ | Image |
| 否 | 是 | 加工❌，走边框✔ | Image |
| 否 | 否 | 加工❌，走边框❌ | Image |

三种异常本质相同，建议**将工具头向中心区域方向移动尝试，**这是因为两类超限仅出现在加工区域**边缘的 10 mm ~ 25 mm** 范围内，只要工具头远离边缘，就能同时落在加工区域和红十字可达区域之内。

![034.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/034.png)

若不想手动调整光标，也可直接**关闭"手动调整"功能**，使用文件原始坐标发起加工；此时走边框不再使用红十字投射，不会触发报错。

![035.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/035.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
