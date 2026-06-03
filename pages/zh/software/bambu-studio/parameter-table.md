---
path: zh/software/bambu-studio/parameter-table
title: "切片参数表格"
description: ""
tags: []
created: 2023-08-28T07:46:55.476Z
updated: 2024-05-28T10:54:56.883Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter-table
---

切片参数表提供了一个表格供用户可以同时修改各个对象/零件的参数，您可以在表格中修改的经常修改的参数，并在右侧修改其他参数。（对象与零件的区别，请参考[拆分为对象/零件](split-to-objects-parts.md)）

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/object_view1.png)

通过这个表格，您可以提高拥有大量对象的项目的使用效率。

# 如何使用？

## 打开/关闭表格

您可以通过点击“准备”页面左侧的“表格”图标来打开表格，点击“关闭”图标可以关闭表格。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/open_close1.gif)

## 修改表格中的参数值

您可以直接在表格中，修改各对象/零件的以下参数值：

- 可打印状态；
- 名称;
- 耗材丝;
- 层高；
- 墙层数；
- 填充密度(%)；
- 支撑;
- Brim；
- 外墙速度；

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/modify_value_cn.gif)

注意，在此处无法修改“盘”的值。

您还可以通过单击单元格右侧的橙色图标，恢复为该参数的默认值。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/resume_value_cn.gif)

## 修改右侧的值

当单击下列单元格的值时，右侧将显示与它同一组中的所有参数。

|  |  |
| --- | --- |
| **列** | **组** |
| 层高 | 质量 |
| 墙层数 | 强度 |
| 填充密度 | 强度 |
| 支撑 | 支撑 |
| Brim | 支撑 |
| 外墙速度 | 速度 |

当您点击“可打印状态/盘/名称”时，右侧将列举该对象或零件已经修改了的所有参数。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/printable_plate_name_cn.gif)

您也可以在右侧修改参数值，比如：

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/right_value_cn.gif)

## 快捷方式

### **通过“空格键”切换布尔值**

选择“可打印状态/支撑”单元格时，您可以通过键盘上的“快捷键”来切换这些布尔值。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/bool_space_cn.gif)

### 通过“数字键”选择耗材丝

选择“耗材丝”单元格后，我们可以直接使用键盘上的“数字键”选择不同的耗材丝。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/filament_color_cn.gif)

### 复制同一列的参数

对于大多数列（"盘"除外），我们可以使用 "Ctrl-C/Command-C "和 "Ctrl-V/Command-V "复制同一列中的值。选择一个单元格值后，使用 "Ctrl-C/Command-C "将其复制到剪贴板，然后在同一列中选择一个或多个单元格，使用 "Ctrl-V/Command-V "将这些值粘贴到这些单元格中。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/copy_cn.gif)

## 排序

Bambu Studio提供了三种排序方式。

### 按名字排序

您可以单击“名称”列，按对象名称对所有对象进行排序。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/name_sort_cn.gif)

### 按“盘”序号排序

您可以单击“盘”列，按照盘的序列号对所有对象进行排序。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/plate_sort_cn.gif)

### 按“耗材丝”序号排序

您可以单击“耗材丝”列，按照耗材丝序列号对所有对象进行排序。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-parameter-table/filament_color_sort_cn.gif)
