<!--
---
name: SDIO
class: interface
type: pinout
description: Raspberry Pi SD0/SD1 pins
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
# SDIO - SD Card Interface

SDIO is the SD host/eMMC interface on the Raspberry Pi. SD host signals are normally used for the microSD slot.

These pins are "SD host" on Alt0 and "eMMC" on Alt3.

## Enable via config.txt

`dtoverlay=sdio` adds a second, four-bit SD interface on GPIO 22 to GPIO 27, and moves the microSD slot onto the bcm2835-sdhost driver. A one-bit interface uses GPIO 22 to GPIO 25 instead, leaving GPIO 26 and GPIO 27 free:

```
dtoverlay=sdio,bus_width=1,gpios_22_25
```

The older `sdio-1bit` overlay does the same thing and is deprecated.

Pi 5 has its own version, `dtoverlay=sdio-pi5`, which uses the same six pins.
