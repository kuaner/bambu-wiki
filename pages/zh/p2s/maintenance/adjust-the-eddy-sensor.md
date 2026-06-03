---
path: zh/p2s/maintenance/adjust-the-eddy-sensor
title: "P2S 涡流线圈调整"
description: "本文将详细为您介绍 P2S 涡流线圈与热端距离调整方法。"
tags: []
created: 2025-10-14T13:14:31.014Z
updated: 2025-10-14T13:14:32.383Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/adjust-the-eddy-sensor
---

工具头上的涡流线圈参与Z方向归零、热床调平和动态流量校准，当涡流线圈和喷嘴之间的距离过近或过远，以上这几个功能都会受到影响。因此拆装涡流传感器后还需要对间距进行调整，该WIKI提供了一种最为简单的操作方法。

## 调整步骤

### 第1步 移除工具头前盖

打开工具头前盖组件，并将其挂到工具头顶部。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/009.png)

### 第2步 释放切刀刀柄

拧下切刀螺丝，并使用镊子小心取下切刀刀片。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/008.png)

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/007.png)

### 第3步 粗验涡流线圈距离

裁剪一段4mm\*60mm的A4纸片，对折一次后插入到喷嘴和涡流线圈之间。当来回抽拉时，能感受到一定的摩擦阻力，但纸张仍可自由移动。这就说明热端和涡流线圈大致间隙为0.2-0.3mm。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/001.webp)

### 第4步 重装涡流线圈

若双层A4纸非常难插入或者没有感受到摩擦力，则需要取下喷嘴，重新安装涡流传感器。以下是具体操作过程。

1. 取下硅胶套并拨开卡扣，然后将喷嘴取下。

![019.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/019.webp)

2. 同时拧松两个涡流线圈固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/010.png)

3. 重新拧紧固定螺丝。锁螺丝时，请先轻轻预锁一颗，锁紧另一颗后再次拧紧第一颗螺丝，以保证涡流线圈装好后呈水平状态（重要）。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/013.webp)

4. 安装喷嘴组件。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/012.webp)

5. 再次使用 A4 纸测试操作。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/002.webp)

### 第5步 装回切刀

使用镊子等工具小心装回切刀刀片。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/003.png)

将刀片引入挤出机侧面的刀槽。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/004.png)

用内六角扳手锁紧刀柄螺丝。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/005.png)

### 第6步 安装工具头前盖

工具头前盖组件是通过磁吸固定的，直接合上即可。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adjust-the-eddy-sensor/006.png)

## 功能验证

为确保一切正常，请开机进行一次回零和热床调平校准，若无出现回零或调平失败报错，表示上方操作均正确。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
