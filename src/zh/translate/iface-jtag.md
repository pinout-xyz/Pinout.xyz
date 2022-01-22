<!--
---
name: JTAG
class: interface
type: pinout
description: 树莓派 JTAG 接口
pin:
  'bcm4':
    name: TDI (Alt5)
  'bcm5':
    name: TDO (Alt5)
  'bcm6':
    name: RTCK (Alt5)
  'bcm12':
    name: TMS (Alt5)
  'bcm13':
    name: TCK (Alt5)
  'bcm22':
    name: TRST (Alt4)
  'bcm23':
    name: RTCK (Alt4)
  'bcm24':
    name: TDO (Alt4)
  'bcm25':
    name: TCK (Alt4)
  'bcm26':
    name: TDI (Alt4)
  'bcm27':
    name: TMS (Alt4)
-->
# JTAG

JTAG 是一个标准化的、用于测试集成电路的接口，可以用来调试树莓派。

树莓派上有两个独立的 JTAG 接口：

* 复用功能5：GPIOs 4, 5, 6, 12, 13
* 复用功能4：GPIOs 22, 23, 24, 25, 26, 27
