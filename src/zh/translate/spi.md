<!--
---
name: SPI
class: interface
type: pinout
description: Raspberry Pi SPI pins
url: https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/
pincount: 5
pin:
  '11':
    name: SPI1 CE1
  '12':
    name: SPI1 CE0
  '19':
    name: SPI0 MOSI
    direction: output
    active: high
    description: Master Out / Slave In
  '21':
    name: SPI0 MISO
    direction: input
    active: high
    description: Master In / Slave Out
  '23':
    name: SPI0 SCLK
    direction: output
    active: high
    description: Clock
  '24':
    name: SPI0 CE0
    direction: output
    active: high
    description: Chip Select 0
  '26':
    name: SPI0 CE1
    direction: output
    active: high
    description: Chip Select 1
  '35':
    name: SPI1 MISO
  '36':
    name: SPI1 CE2
  '38':
    name: SPI1 MOSI
  '40':
    name: SPI1 SCLK
-->
# SPI - 串行外设接口

---
### SPI0 的引脚是 GPIO 7, 8, 9, 10, 11
### SPI1 的引脚是 GPIO 16, 17, 18, 19, 20, 21
---

SPI 是一个四线制的总线，通过切换片选引脚，可以用同一套数据引脚来访问多个不同的外设。

默认情况下，树莓派允许用户使用 SPI0 及其片选引脚 CE0（GPIO 8）和 CE1（GPIO 7）。

如果要启用 SPI，你需要在 `/boot/config.txt` 中加一行 dtoverlay 的配置，比如：

```
dtoverlay=spi1-3cs
```

关于树莓派 SPI dtoverlays 的详情，请访问 [树莓派 dtoverlay 介绍](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/overlays/README)
