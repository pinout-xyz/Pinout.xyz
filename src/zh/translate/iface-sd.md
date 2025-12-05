<!--
---
name: SDIO
class: interface
type: pinout
description: 树莓派 SD0/SD1 接口
pin:
  'bcm22':
    name: CLK
  'bcm23':
    name: CMD
  'bcm24':
    name: DAT0
  'bcm25':
    name: DAT1
  'bcm26':
    name: DAT2
  'bcm27':
    name: DAT3
-->
# SDIO - SD 卡接口

SDIO 是 SD 主站或者 eMMC 的接口。SD 主站通常用于读写 microSD 卡槽。

这些引脚是复用功能 0 中的 “SD Host” 以及复用功能 3 中的“eMMC”。
