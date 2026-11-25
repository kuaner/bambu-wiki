---
path: zh/p3c/manual/screen-operation-guide
title: "P3C 屏幕操作指南"
description: "本文介绍 P3C 屏幕各页面的功能与操作。"
tags: ["manual", "p3c"]
created: 2026-11-24T14:02:17.629Z
updated: 2026-11-24T14:02:17.629Z
source: https://wiki.bambulab.com/zh/p3c/manual/screen-operation-guide
---

## 介绍

本指南旨在介绍 P3C 打印机屏幕按键及功能。

## 主页

主页左侧为屏幕菜单栏，包括主页、耗材、控制、设置和助手；主页可使用 Bambu Handy 扫码登录，并可通过文件、耗材和工具进入对应界面。

![01.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/01.png)

点击“文件”，可显示项目。其中，项目包括机内存储、历史记录和外部存储；

- **机内存储**：缓存在打印机本地的模型文件；
- **历史记录**：显示打印机缓存空间内的模型列表；
- **外部存储**：缓存在打印机上 U 盘内的模型文件；

|  |  |
| --- | --- |
| 02.png | 03.png |
| 04.png |

## 耗材

![05.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/05.png)

1. **编辑**：如果 AMS 已识别该料盘信息，可在此处查看料盘信息，但无法修改耗材参数；如果未读取信息，则可在此处修改耗材信息。

![06.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/06.png)

- **进料/退料**：点击按钮，AMS 会进行进料/退料流程，并需手动插入或抽回耗材；

![07.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/07.png)

- **重读**：点击按钮，AMS 会重新读取该槽位的信息。
- **烘干/湿度：**显示 AMS 内部湿度和烘干状态，也可自购烘干模块进行烘干，具体请参考 wiki：[烘干模块安装指南](../maintenance/replace-optional-filament-dryer.md)。
- **全部重读**：可重读 AMS 内所有耗材。
- **AMS 进料**：可对 AMS 内耗材进行统一进料。

![08.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/08.png)

- **退料**：可对 AMS 内已进料的耗材进行批量退料。

![09.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/09.png)

- **工具**：共有外挂进料、自动续料和操作指南三种工具。

![10.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/10.png)

- **外挂进料**：可进行外挂进料或从 AMS 直通口进料。具体步骤请参考 wiki：[外挂进料指南](print-with-external-spool.md)。

![11.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/11.png)

- **自动续料**：当前耗材用尽时，系统将自动使用相同品牌、类型和颜色的耗材继续打印。同时支持手动编辑续料关系，相同类型的不同颜色耗材也可用于续料。具体信息请参考 wiki：[AMS 自动续料功能介绍](../../ams3/manual/auto-refill.md)。

![12.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/12.png)

- **操作指南**：对耗材页面和耗材进料进行教学。

![13.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/13.png)

## 控制

![14.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/14.png)

### 空调系统

可根据耗材的不同选择合适的空调系统。

- **冷却模式**：适合打印 PLA/TPU 等耐热性较低的耗材；腔体降温时，系统会自动切换至冷却模式。

![15.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/15.png)

- **腔温保持模式**：适合打印 ABS/ASA/PC/PA 等具备高耐热性的耗材。腔体加热时，系统会自动切换至腔温保持模式。

![16.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/16.png)

- **部件冷却风扇**：位于工具头上，用于确保在打印过程中充分冷却打印层，有助于在挤出时快速冷却耗材，使每一层都能在下一层沉积之前凝固并保持原始形状。

![17.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/17.png)

- **左/右部件辅助冷却风扇**：位于腔体两侧，能为高速打印提供更好的冷却条件。

|  |  |
| --- | --- |
| 18.png | 19.png |

- **外排风扇**：位于腔体后背板；打印 PLA 等低温耗材时，可实现打印气体外排，并联动自适应空气循环系统强化散热；打印高温耗材时，通过在屏幕开启“打印结束时净化空气”功能，可在打印完成后自动排出机箱残留气体。

![20.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/20.png)

- **腔体过滤风扇**：位于腔体后背板，用于气体过滤。腔温保持模式下，空调系统中的“外排”会切换为“过滤器”。

![21.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/21.png)

### 运动

![22.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/22.png)

- **工具头**：点击 1 格或 10 格的移动按钮，控制工具头在 X 轴和 Y 轴上移动。
- **热床**：点击 1 格或 10 格的移动按钮，升降热床。
- **挂架**：点击“上升”、“回中”或“下降”，可控制挂架的高度状态。

### 照明

点击此按钮可控制机箱内部 LED 补光灯。

### 工具与挤出机

![23.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/23.png)

1. **喷嘴温度**：挂架上喷嘴的温度；输入数值，可设置喷嘴温度，最高 300 ℃。

![24.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/24.png)

- **取用**：点击“取用”工具，工具头将自动夹持所选打印头。

![25.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/25.png)

- **编辑**：可查看或编辑打印头的工具类型。

![26.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/26.png)

- **刷新**：机器将自动刷新该工具类型信息。
- **挤出机**：点击上下按钮，手动挤出或退出 1 cm 耗材。
- **温度**：工具头所夹持的打印头热端温度；输入数值，可设置喷嘴温度，最高 300 ℃。
- **放置**：点击“放置”按钮，可将工具头上的打印头重新放到挂架上。
- **...**：包含“工具信息”和“刷新全部”按钮。

![27.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/27.png)

- **工具信息**：点击此处，可查看打印机上所有工具的信息。
- **刷新全部**：点击此处，可刷新所有打印头的信息。

### 腔体

显示打印机腔体内的温度。

### 热床

输入数值，设置热床温度，最高 110℃。

![28.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/28.png)

## 设置

![29.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/29.png)

### 账号

用 Bambu Handy 扫描二维码，即可登录账号。

![30.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/30.png)

### Wi-Fi

可设置打印机网络，测试网络连接，查看当前网络，或查看和添加其他网络。

![31.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/31.png)

### USB 存储

- **存储**：显示 U 盘已使用容量和该 U 盘的最大容量；
- **弹出**：点击“弹出”，可将 U 盘安全弹出；
- **格式化外部存储**：可将 U 盘存储格式化。一旦重设，存储将无法恢复。

![32.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/32.png)

### 固件

查看设备当前版本和历史版本，或进行离线升级。如固件需更新时，右上角“更新”按钮会变亮。

![33.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/33.png)

### 校准

校准包括打印校准、挂架对位校准、平面加工偏移校准和平面加工调节（平面工艺校准），以及首层质量校准。

![34.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/34.png)

**打印校准**

![35.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/35.png)

- **电机降噪**：减少打印过程中电机产生的噪音，特别是在进行长时间或高速打印时。通过优化电机的运行算法和控制策略，不仅能降低噪音，还能提升打印表面的光滑度，从而改善最终打印效果。
- **振动补偿**：在打印中实时监测并检测到任何震动时，可自动调整工具头位置，以确保打印的精确度。尤其在打印复杂或细致模型时，通过此校准能够有效防止因震动引起的误差，确保每层都准确无误地完成。
- **自动热床调平**：通过智能算法调整喷嘴与打印板之间的距离，确保每个角落的间隙一致，能够有效避免因热床不平整导致的打印缺陷，从而提高打印精度。
- **喷嘴偏移校准**：如果两个喷嘴的定位出现偏移，则可能导致打印过程中模型出现错位或层移现象。在打印过程中发现切换喷嘴后模型出现明显的层移时，建议进行一次喷嘴偏移校准。此过程利用工具头内的涡流传感器和热床后面的喷嘴偏移校准传感器，确保喷嘴位置的准确性，以提高打印质量和精确度。通过有效的校准，可以减少打印错误，确保每个层次的完美对齐。

**挂架对位校准**

当挂架运动异常进而影响打印过程时，可进行挂架对位校准。系统将通过在预设坐标附近搜索磁铁记录其精确三维坐标，并在初步标定与取放测试后进行二次标定对比：差值在阈值内则判定标定可靠，超出阈值则识别出人工放置不正导致的异常并判定为不可靠。

![36.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/36.png)

**平面加工偏移校准**

当多刀具的实际位置与理论位置存在偏差时，用于校准各刀具之间的偏置。

![37.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/37.png)

**平面加工调平**

用于提高切割均匀性，避免出现局部切不穿或局部线条过深的情况。

> 注意：安装画笔头时，只可进行平面加工偏移校准；如需进行平面加工调节，请**安装刀切头**。

![38.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/38.png)

**首层质量校准**

支持微调首层打印时喷嘴与热床间的距离，从而提升首层附着力与表面平整度，有效解决首层偏高或偏低导致的打印质量问题。

> 注意：该功能是为了满足用户不同场景差异化的调参需求，一般情况无需用到，建议按需使用。

![39.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/39.png)

### 工具箱

![40.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/40.png)

- **腔体烘干**：可将需要烘干的耗材放置在热床上，用简易罩盖覆盖，并设置对应的温度，对耗材进行烘干处理。

![41.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/41.png)

- **XYZ 轴清洁**：光杆和线轨的定期清洁可防止碎屑积累，确保设备正常运作并延长使用寿命。屏幕左侧进度条长度会随光杆和线轨的清洁程度减少；如果进度条变为红色，则需进行清洁，具体教程可通过右侧二维码获取。

![42.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/42.png)

- **丝杆润滑**：丝杆需要定期润滑，以确保热床上下移动运行平稳。

![43.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/43.png)

- **打印头 & 挂架维护**：打印头与挂架在长期使用过程中，容易积累灰尘，这些灰尘会影响挂架对打印头的锁紧效果。通过对打印头与挂架进行润滑保养，可以减少部件磨损概率，延长使用寿命。

![44.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/44.png)

- **喷嘴冷拔维护**：当挤出电机在常规打印流量下频繁出现过载报错，则表示喷嘴阻力过大，急需清理；同时，由于 TPU 对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，建议在打印 TPU 前对喷嘴进行冷拔清理，以保证打印顺畅。

![45.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/45.png)

### 更多设置

|  |  |
| --- | --- |
| 46.png | 47.png |
| 48.png |

1. **打印选项**

- **炒面检测**：在打印过程中检测炒面问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。
- **堆料检测**：在打印过程中检测废料槽堆积问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。
- **裹头检测**：在打印过程中检测裹头问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。
- **异物检测**：发起打印任务后，实况摄像头会检查打印平台是否存在异物；若检测到异物，则无法开启打印。

|  |  |
| --- | --- |
| 49.png | 50.png |

- **类型检测**：若实际使用的打印板与切片文件中的打印板不匹配，则及时停止打印，避免打印失败。
- **偏移检测**：若打印板的标记未处于预定义范围内，打印机将自动停止打印，以避免打印板未放置或放置不当导致的打印异常。
- **空打检测**：若检测到喷嘴堵塞、耗材缠料或磨损导致的空打现象，打印机将自动停止打印。

![51.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/51.png)

- **丢步自动恢复**：当电机检测到位置偏移（丢步）时，X、Y 和 Z 轴会重新定位，并回到偏移前的位置继续执行未完成的 G-code，以保证打印质量。
- **开门检测**：开启后，打印机将检测前玻璃门是否打开，可选择在门打开时触发通知或暂停打印。
- **缓存远程打印文件到外部存储中**：通过云端发起的打印，打印文件将缓存到外部存储中。

![52.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/52.png)

- **运动精度增强**：专为对打印质量有高要求的用户设计，旨在解决 3D 打印过程中的绝对定位问题，从而提高打印精度，尤其是大尺寸打印的精度。通过这一过程，可以显著抑制运动迟滞和运动畸变，确保打印结果更加精准。
- **打印结束时净化空气**：安装外排风扇后，打开该按钮，支持结束打印后自动开始净化腔内气体，通过外排风扇排出机箱残留气体。
- **外接净化器自动模式参数设置**：可按耗材类型自定义自动模式下的净化强度和延时关闭的时长。
- **打印状态快照**：打印任务完成后，打印机会自动拍摄打印件照片并上传至云端，该照片将同步显示在 Bambu Handy 的打印完成弹窗中。

![53.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/53.png)

- **AMS 选项**

拓竹官方耗材均可自动读取，自动读取的耗材信息不支持修改。

- **自动读取未进料耗材**：当 AMS 中放置了官方耗材，在进入耗材页面时，机器将自动读取耗材类型。为避免频繁操作，自动读取间隔不小于 10 分钟。
- **AMS 自动续料**：当前耗材用尽时，系统将自动使用相同品牌、类型和颜色的耗材继续打印。同时支持手动编辑续料关系，相同类型的不同颜色耗材也可用于续料。

![54.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/54.png)

- **录像**：可选择开启实况摄像头或俯视摄像头。

![55.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/55.png)

- **声音**：如果开启声音选项，打印机在开机、打印开始和打印结束时都会发出提示音。
- **状态指示灯**：用于提示打印机健康状态和打印任务状态。
- **腔体灯模式**：可根据实际的使用需要选择手动模式或节能模式。

![56.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/56.png)

- **低功率模式**：在打印机供电功率受限的情况下，可通过延长热床升温时间，降低最大功率。

![57.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/57.png)

- **自动休眠**：选择打印机自动休眠的时长。

![58.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/58.png)

- **语言**：选择打印机屏幕的显示语言。

![59.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/59.png)

- **设备和序列号**：查看打印机设备名、设备使用时间和序列号。

![60.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/60.png)

- **仅局域网**：开启仅局域网模式后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。如果多个设备通过同一局域网连接，可进行视频直播或数据共享。

![61.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/61.png)

- **导出日志到外部存储**：可根据需求，选择是否导出所有打印日志、关键照片（判断炒面等问题）和 G-code（判断打印质量问题）。

![62.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/62.png)

- **恢复出厂设置**：将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![63.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/63.png)

- **认证信息**：可在此处查看机器的认证信息电子标签页。

![64.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/64.png)

## 助手

如果打印机出现故障，此处将会显示报错信息，可扫码查看详情。

![65.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/screen-operation-guide/zh/65.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
