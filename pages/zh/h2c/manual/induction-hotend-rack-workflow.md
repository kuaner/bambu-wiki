---
path: zh/h2c/manual/induction-hotend-rack-workflow
title: "感应热端挂架工作介绍"
description: "本文介绍了感应热端挂架的工作流程，包括感应热端切换，以及感应热端挂架粗回中和精回中。"
tags: []
created: 2025-11-18T12:39:38.396Z
updated: 2025-11-27T10:32:18.564Z
source: https://wiki.bambulab.com/zh/h2c/manual/induction-hotend-rack-workflow
---

## 概述

感应热端挂架是 H2C 打印机所搭载 Vortek 系统的核心组件之一，主要负责实现智能感应热端的自动切换与存储。它支持最多 6 个（工具头上 1 个 + 挂架上 5 个）感应热端的全自动更换，无需人工干预，显著降低了操作成本。同时，挂架集成了智能感应技术，可实时监测并反馈智能热端的位置与运行状态，确保打印过程稳定可靠。

![img_v3_02ra_e042f1e6-e688-4239-84d9-9a4397ec287g.png](https://public-cdn.bblmw.com/wiki/new/h2c/manual/induction-hotend-rack-workflow/img_v3_02ra_e042f1e6-e688-4239-84d9-9a4397ec287g.png)

## 感应热端挂架的组成

感应热端挂架主要由以下部件构成：步进电机、皮带、惰轮、感应热端拉柄解锁组件以及两排热端挂架。电机通过皮带驱动两排挂架进行升降运动；拉柄解锁组件则通过控制内部金属解锁轴的升降，实现对热端拉柄的锁定与解锁。

## 感应热端挂架工作流程

### 感应热端切换

系统通过电机与皮带控制两排热端挂架升降，同时拉柄解锁组件自动升降金属解锁轴，配合工具头的移动，可完成拉柄的拉出与推入动作，从而实现完整的热端切换流程：

1. 拉柄解锁
2. 放置当前工具头上的右热端（若有）：寻找空位进行放置（若存在多个空泊位，系统将优先选择编号最小、即最靠近工具头的空位，例如空位为 1、3、5 时，优先放置于 1 号位）
3. 安装新热端
4. 拉柄上锁

![switch_hotend.webp](https://public-cdn.bblmw.com/wiki/new/h2c/manual/induction-hotend-rack-workflow/switch_hotend.webp)

其中，拉柄解锁组件的金属轴升降动作由挂架本身的升降运动触发，动作如下：

![induction_hotend_latch_actuator.webp](https://public-cdn.bblmw.com/wiki/new/h2c/manual/induction-hotend-rack-workflow/induction_hotend_latch_actuator.webp)

### 感应热端挂架回中

#### **粗回中**

粗回中通过识别感应热端挂架上的软磁贴以确定中心点。

1. **自动回中**

- **工具头回中：**当 XY 电机重新上电后，因工具头位置尚未确定，在进行工具头回中之前，感应热端挂架会执行一次粗回中，避免工具头在回中过程中与热端挂架发生碰撞。
- **热床移动：**与工具头回中的逻辑相似。

2. **手动回中**

- **点击回中按钮：**当 A 排或 B 排挂架升起时，点击“热端 & 挂架”页面的回中按钮， 挂架会进行一次粗回中。

![coarse_homing.webp](https://public-cdn.bblmw.com/wiki/new/h2c/manual/induction-hotend-rack-workflow/coarse_homing.webp)

#### **精回中**

当需要在热端挂架上进行热端的取用或放置时，为精确定位挂架位置，系统会先执行一次精回中。精回中通过挂架撞击上下横梁限位，来确定上限位与下限位相对于零点的坐标位置。

![fine_homing.webp](https://public-cdn.bblmw.com/wiki/new/h2c/manual/induction-hotend-rack-workflow/fine_homing.webp)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
