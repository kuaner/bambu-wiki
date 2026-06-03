---
path: zh/a2l/manual/a2l-firmware-release-history
title: "A2L 固件发布记录"
description: ""
tags: []
created: 2026-06-01T13:03:14.734Z
updated: 2026-06-01T13:03:17.750Z
source: https://wiki.bambulab.com/zh/a2l/manual/a2l-firmware-release-history
---

## 01.01.00.00（20260601）

### 新增功能

1. **新增自适应振动补偿功能**

新增自适应逻辑，进一步优化运动稳定性和打印精度。

2. **新增快速冲刷模式**

可在 Bambu Studio（版本号：2.7.1）中切换冲刷模式，默认标准模式，可根据项目需求自由选择。

- 标准模式：带有变速与变温的冲刷逻辑，冲刷更彻底，可在追求极致打印质量时使用。
- 快速模式：使用调优过的冲刷温度、倍率与更快的冲刷挤出，来缩短冲刷时长，可能会在某些极端情况产生轻微混色。

![2-cn.png](https://public-cdn.bblmw.com/wiki/new/a2l/release-note/u1/2-cn.png)

3. **支持通过 Bambu Handy 端（版本号：3.21.0）对 2D 加工的耗材位置进行拍照转正**

![handy-2dphoto.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/release-note/u1/handy-2dphoto.jpg)

4. **支持首层质量校准功能**

- 支持微调首层打印时喷嘴与热床间的距离，从而提升首层附着力与表面平整度。
- 注意：该功能是为了满足专业用户不同场景差异化的调参需求，一般情况无需用到，建议按需使用。

![4-cn.png](https://public-cdn.bblmw.com/wiki/new/a2l/release-note/u1/4-cn.png)

5. **新增使用外挂料进行手动多色打印功能**  
   使用外挂料时，新增加多色打印的按钮，以便在使用外部料盘时简化多色打印流程。开启后可以手动更换耗材，确保在没有AMS的情况下实现更顺畅的耗材切换。
6. **新增支持AMS与外挂料盘混合使用打印多色**
7. **支持边烘边打**  
   需要注意功率限制和烘干温度不能高于材料的软化温度。注意：运行该功能需要额外购买 AMS 外接电源。
8. **支持远程开启烘干功能**
9. **支持曲线规划增强功能**  
   优化了曲线规划，改善某些场景下的打印质量。
10. **新增智能高温堵头风险提示**
11. **新增耗材 SN 码显示**

![11-cn.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/release-note/u1/11-cn.jpg)

### 功能优化

1. 优化电机降噪算法
2. 优化静音模式下的风扇噪音
3. 优化全高精度校准触发逻辑
4. 优化智能裹头检测逻辑
5. 优化开机提示音
6. 优化部分场景下异常重启的问题
7. 优化热失控保护逻辑

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
