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
# SPI - Serial Peripheral Interface

* SPI0 pins are GPIO 7, GPIO 8, GPIO 9, GPIO 10, GPIO 11
* SPI1 pins are GPIO 16, GPIO 17, GPIO 18, GPIO 19, GPIO 20, GPIO 21

Known as the four-wire serial bus, SPI lets you attach multiple compatible devices to a single set of pins by assigning them different chip-select pins.

To talk to an SPI device, you assert its corresponding chip-select pin.

By default the Pi allows you to use SPI0 with chip select pins on CE0 on GPIO 8 and CE1 on GPIO 7.

## Enable via config.txt

You can enable SPI1 with a dtoverlay configured in "/boot/firmware/config.txt", for example:

```
dtoverlay=spi1-3cs
```

For full details of the SPI dtoverlays (and others) see [the Raspberry Pi dtoverlay README](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/overlays/README)