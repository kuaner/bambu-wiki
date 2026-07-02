---
path: zh/x2d/troubleshooting/hotend-not-installed
title: "05FF-4094：X2D"
description: ""
tags: []
created: 2026-07-01T08:14:08.200Z
updated: 2026-07-02T02:41:26.284Z
source: https://wiki.bambulab.com/zh/x2d/troubleshooting/hotend-not-installed
---

## 故障描述

打印机在校准前会检查热端是否正确安装，热端未安装或安装不到位就会触发本告警。

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 排故措施：检查热端安装状态

### 移除工具头前盖组件

打开工具头前盖组件，断开连接线缆，移除工具头前盖组件。

![connector.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/connector.jpg)

### 移除热端硅胶套和热端

用手握住硅胶套的两侧，用力斜向下拉，取下硅胶套。  
![remove_right_sock.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/remove_right_sock.jpg)  
解锁热端卡扣，取下右热端。  
![unlock_right_click.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/unlock_right_click.jpg)

向右拨动升降拨杆，使堵嘴片移动到右侧位置。  
![ksnip_20260213-154847.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/ksnip_20260213-154847.jpg)  
用手握住硅胶套高温标识的两侧，用力斜向下拉，取下硅胶套。  
![left_sock.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/left_sock.jpg)  
解锁热端卡扣，取下左热端。。  
![unlock_left_click.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/unlock_left_click.jpg)

### 安装热端和热端硅胶套

确认热端卡扣处于完全打开状态，将热端安装到热端加热组件上  
![install_right_hotend.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/install_right_hotend.jpg)  
检查确认热端与底座完全的贴合，锁紧卡扣，  
![right_hotend_installed.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/right_hotend_installed.jpg)

向右拨动升降拨杆，使堵嘴片移动到右辅助热端位置。  
![move_block_2.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/move_block_2.jpg)  
确认热端卡扣处于完全打开状态，将热端安装到左热端加热组件上，  
![install_left_hotend.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/install_left_hotend.jpg)  
检查确认热端与底座完全的贴合，锁紧卡扣（先合上左侧金属板，再压紧右侧压环）。  
![left_hotend_installed.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/left_hotend_installed.jpg)

最后将硅胶套自下而上安装到热端上。

### 合上工具头前盖组件

连接工具头前盖，合上工具头前盖，注意工具头前盖组件是通过磁吸固定的，需要检查是否有明显的间隙，避免出来报错和打印过程中脱落。  
![install_front_cover.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/install_front_cover.jpg)

### 重新校准

完成以上排查步骤后，请在打印机屏幕上点击**重新校准**。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
