<!--
---
name: GPCLK
class: interface
type: pinout
description: 树莓派通用时钟接口
pin:
  'bcm4':
    name: GPCLK0
  'bcm5':
    name: GPCLK1
  'bcm6':
    name: GPCLK2
-->
# GPCLK - 通用时钟

通用时钟可以在无需软件控制的情况下，输出固定频率的信号。

此接口默认支持以下时钟源：

```
0     0 Hz     接地
1     19.2 MHz 晶振
2     0 Hz     testdebug0
3     0 Hz     testdebug1
4     0 Hz     PLLA
5     1000 MHz PLLC (超频后，此数值会变化)
6     500 MHz  PLLD
7     216 MHz  HDMI 辅助
8-15  0 Hz     接地
```

你可以通过设置时钟分频以配置其他频率的时钟信号，格式为 `SOURCE/(DIV_I + DIV_F/4096)`。注意，[BCM2835 ARM 外设](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2835/BCM2835-ARM-Peripherals.pdf) 文档里面有一个错误，分频器的分母应该是 1024 而不是 4096。
