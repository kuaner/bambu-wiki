---
path: zh/software/bambu-studio/filament-manager
title: "耗材管理"
description: "本文介绍了如何使用 Bambu Studio 的耗材管理功能，包括如何添加、编辑、删除耗材信息，查询与更新耗材剩余重量，及云端同步至 Bambu Handy 耗材库等功能。"
tags: []
created: 2026-06-12T04:22:07.206Z
updated: 2026-06-12T09:30:50.939Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/filament-manager
---

## 耗材管理

**耗材管理** 是 Bambu Studio 中用于统一管理与记录**耗材信息**的页面，包括耗材**品牌、类型、颜色**和**剩余量**。耗材库信息可通过云端在 Bambu Studio 和 Bambu Handy 间自动同步。耗材管理的入口位于 Bambu Studio 上侧标签栏。

![filament_manager_page_zh.png](https://wiki.bambulab.com/bambu-studio/filament-manager/filament_manager_page_zh.png)

> **ℹ️ 说明：** 耗材管理无法对耗材的**打印参数**进行编辑。如需修改耗材打印参数，请在「准备 → 项目耗材列表 → ![](https://wiki.bambulab.com/bambu-studio/filament-manager/edit.jpg) → 编辑 → 耗材丝设置」中进行编辑。

> **⚠️ 注意：** 使用耗材管理功能需要将 Bambu Studio 更新至 `V2.6.1` 版本以上。低于此版本则无法使用该功能。

## 功能总览

耗材管理的主要功能如下：

- **耗材信息管理**：批量添加、删除耗材信息，记录耗材品牌、类型、颜色及余量。
- **耗材余量查询**：耗材余量精确到以克为单位。
- **筛选和分组**：可根据耗材品牌与类型对耗材进行筛选与分组。
- **云端自动同步**：所有耗材信息可通过 Bambu 云端在 Bambu Handy 与 Bambu Studio 之间自动同步。

## 界面与功能指南

### 顶部工具栏

![filament-manager-main-view.png](https://wiki.bambulab.com/bambu-studio/filament-manager/zh_filament-manager-main-view.png)

| 功能按钮 | 功能介绍 |
| --- | --- |
| 「**全部**」 | 展示所有耗材信息 |
| 「**AMS**」 | 仅展示当前所连接 AMS 中的所有耗材信息 |
| 「**品牌**」 | 按品牌筛选所显示的耗材 |
| 「**耗材类型**」 | 按耗材类别筛选 |
| 「**类型**」 | 按耗材二级类别筛选 |
| 「**搜索耗材**」 | 可根据耗材名称、材料或颜色进行搜索 |
| 「**分组**」 | 将耗材条目归类到可折叠的标题下，显示**品牌**、**耗材名称**、**耗材料盘总数**和**合计剩余重量** |
| refresh.jpg | 刷新 AMS 数据并同步至云端 |
| upload.jpg | 将最新修改同步云端 |
| history.jpg | 查看耗材条目的同步历史 |
| 「**+ 添加耗材**」 | 进入添加耗材窗口 |

### 添加耗材——从 AMS 读取

**「从 AMS 读取」** 是添加耗材最快捷的方式。它可以通过 AMS 批量识别并一键添加 AMS 中的耗材。

该功能仅适用于**带有 RFID 标签的 Bambu Lab 耗材**。第三方耗材不包含 RFID 数据，若须添加耗材，可以使用「手动添加」的方式。  
![](https://wiki.bambulab.com/bambu-studio/filament-manager/bambu_filament_rfid.png)

**操作步骤：**

![add-filaments-ams-steps.png](https://wiki.bambulab.com/bambu-studio/filament-manager/zh_add-filaments-ams-steps.png)

1. 点击「**+ 添加耗材**」。
2. 选择「**从 AMS 读取**」。
3. 从下拉菜单中选择您的「**打印机**」。如果列表中未显示您的打印机，请点击右侧的「**刷新**」（↻）按钮。
4. 选择机型后，将显示 AMS 的四个槽位及其对应的耗材信息，包括槽位标签（`A1–A4`）、颜色色块、耗材类型以及耗材余量。

![add-filaments-steps_2.png](https://wiki.bambulab.com/bambu-studio/filament-manager/zh_add-filaments-steps_2.png)

5. 选择想要添加的耗材：

   - 点击卡片可逐一选择。
   - 点击「**选择全部已识别**」可以全选 AMS 内识别到的所有耗材。
   - 点击「**取消选择**」将取消已选耗材。
6. 最后，点击「**批量添加**」即可添加所选中的耗材。

添加完成后，Bambu Studio 会将新的耗材信息自动同步至云端。屏幕右下角会弹出相关提示：**“已同步 N 个新增耗材到云端。”**

![confirmation-upload-to-cloud.png](https://wiki.bambulab.com/bambu-studio/filament-manager/zh_confirmation-upload-to-cloud.png)

> ✅ **提示**：`V2.7.1` 以上版本的 Bambu Studio 中，如果所添加的耗材的 RFID 标签是系统已识别过的，则会弹出提示询问是否覆盖现有耗材，以防止同一卷耗材从 AMS 取出又装回的情况下产生重复记录。
>
> ![confirmation_prompt.png](https://wiki.bambulab.com/bambu-studio/filament-manager/confirmation_prompt.png)

### 添加耗材——手动添加

非 Bambu Lab 耗材或不带 RFID 标签的耗材，可以选择手动添加耗材。

**操作步骤：**

![manual-filament-add-steps_1.png](https://wiki.bambulab.com/bambu-studio/filament-manager/zh_manual-filament-add-steps_1.png)

1. 点击「**+ 添加耗材**」
2. 点击「**手动添加**」
3. 选择「**品牌**」；若列表中没有对应的品牌，请选择 `Generic`。
4. 选择「**类型**」
5. 选择「**颜色**」：

   - **Bambu Lab 耗材**：自动显示官方色块、颜色名称、耗材代码和 HEX 色值（例如 `拓竹绿 · 10501 · #00AE42`）。
   - **其他品牌耗材**：点击「**+**」通过取色器或 HEX 色值设置自定义颜色。
6. 设置「**重量**」：

   - **当前净重**：料盘上目前剩余的耗材量。
   - **总净重**：耗材的初始重量（例如 `1000 g`）。

> **提示：** 若要手动添加已使用了一部分的耗材，则需要自行称重，计算当前净重。耗材与料盘的称重结果，减去空料盘的重量（`1kg` 料盘通常约重 `200g`），即为“**当前净重**”。

7. 添加「**备注**」。非必填，最多 50 个字符。
8. 如需批量添加多个完全相同的耗材，请在窗口左下角设置「**耗材盘数量**」。
9. 最后，点击「**添加**」。

### 编辑、复制和删除耗材

![edit-duplicate-delete.png](https://wiki.bambulab.com/bambu-studio/filament-manager/zh_edit-duplicate-delete.png)

每行耗材信息的最右侧都有三个小图标，它们的功能如下：

1. **编辑**：查看耗材详情，编辑耗材信息。
2. **复制**：创建一个预填充了相同信息的新耗材。当您有多卷相同品牌、材料和颜色的耗材时非常适用。
3. **删除**：永久删除该耗材信息并将删除操作同步至云端。

> **⚠️ 注意：** 删除操作会立即同步至云端且无法撤销，请谨慎操作。

### 耗材剩余重量

「**剩余**」列由具体数值和进度条展示每个耗材的当前余量。

剩余重量不会自动更新。它会在以下情况下更新：

1. 您添加、删除或修改耗材信息时。
2. 您手动点击右上角的「**↻**」刷新按钮时。

![spool-weight-remainder.png](https://wiki.bambulab.com/bambu-studio/filament-manager/zh_spool-weight-remainder.png)

**注意事项：**

- 剩余重量在打印过程中不会实时更新，而是在打印完成后更新。
- 耗材管理不具备耗材不足的通知功能。在长时间打印前，请自行检查剩余量是否满足需求。
- 云端同步需要有效的网络连接。

> **提示：** 为确保剩余重量记录长期保持准确，请定期重新称量用过的耗材，并通过“编辑”功能更新当前净重。因为打印失败、换料损耗等情况会影响软件对耗材余量的精确估算，使得时间久了记录会和实际重量产生偏差，因此需要定期手动称量校准。

### 网络连接要求

**⚠️ 注意：** 添加、编辑、删除和同步耗材信息**均需要联网**。断网时您仍可查看已有的耗材信息，但所做的任何改动要等重新联网后，才会同步到其他设备。

## 同步至 Bambu Handy

耗材信息与 Bambu 账户绑定，可以通过云端自动同步。

1. 在 Bambu Handy 中登录相同的 Bambu 账户。
2. 进入「**设备 → 耗材库**」，即可在手机上查看和管理耗材信息。

在 Bambu Handy 中所做的更改会同步至 Bambu Studio，反之亦然。

![](https://wiki.bambulab.com/bambu-studio/filament-manager/phone-handy-1_zh.png)
![](https://wiki.bambulab.com/bambu-studio/filament-manager/phone-handy-2_zh.png)

> **ℹ️ 说明：** 如果您的耗材信息未在 Bambu Handy 中显示，请退出并重新登录 Bambu 账户刷新重试。

---

## 故障排除

| 现象 | 解决方法 |
| --- | --- |
| 找不到耗材管理入口 | 将 Bambu Studio 更新至 `V2.6.1` 或更高版本 |
| 从 AMS 读取时，未显示任何槽位数据 | 确认已选择机型且打印机在线，可点击打印机下拉菜单旁的 ↻ 进行刷新 |
| 从 AMS 读取时，未显示耗材数据 | 该功能仅支持带 Bambu Lab RFID 标签的耗材，第三方耗材请手动添加耗材 |
| 颜色显示“无预定义颜色” | 对于非 Bambu Lab 耗材属正常现象，点击「**+**」添加自定义颜色 |
| 更改未保存 / 同步卡住 | 检查您的网络连接，保存与同步均需要联网 |
| RFID 重新扫描后出现重复耗材条目 | 在弹出的确认窗口选择确认覆盖替换现有条目（适用于 `V2.7.1` 以上版本） |
| 剩余重量未更新 | 点击 ↻ 刷新，或编辑耗材信息，手动修正当前净重 |
| Bambu Handy 中缺少添加过的耗材 | 确认两台设备登录的是同一个 Bambu 账户，尝试退出并重新登录 |

## 相关阅读

- [流量动态校准](calibration_pa.md)
- [流量校准](calibration_flow_rate.md)
- [创建自定义耗材配置文件](../../bambu-studio/create-filament.md)

---

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
