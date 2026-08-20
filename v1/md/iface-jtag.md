<!--
---
name: JTAG
class: interface
type: pinout
description: Raspberry Pi JTAG pins
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
# JTAG - Joint Test Action Group

JTAG is a standardised interface for debugging integrated circuits which you can use to debug your Raspberry Pi.

There are two separate JTAG interfaces available on the Pi:

| Signal | Alt4 | Alt5 |
| --- | --- | --- |
| TRST | GPIO 22 | |
| RTCK | GPIO 23 | GPIO 6 |
| TDO | GPIO 24 | GPIO 5 |
| TCK | GPIO 25 | GPIO 13 |
| TDI | GPIO 26 | GPIO 4 |
| TMS | GPIO 27 | GPIO 12 |

Alt4 also brings out TRST, which Alt5 has no pin for.

## Using a Pi as the debug probe

A Pi can also be the debugger rather than the target. OpenOCD bit-bangs JTAG or SWD over the GPIO pins, on a pinout of its own which has nothing to do with the Alt4 and Alt5 modes above:

| Signal | GPIO | Header |
| --- | --- | --- |
| TCK / SWCLK | GPIO 11 | Physical Pin 23 |
| TMS / SWDIO | GPIO 8 | Physical Pin 24 |
| TDI | GPIO 10 | Physical Pin 19 |
| TDO | GPIO 9 | Physical Pin 21 |
| TRST | GPIO 7 | Physical Pin 26 |
| SRST | GPIO 24 | Physical Pin 18 |

SWD needs only SWCLK and SWDIO. TRST and SRST are optional and are commented out in the shipped config, since they need a matching `reset_config`. You also need a ground connection, and Physical Pin 20 is conveniently in amongst the signals.

These are the SPI0 pins, so SPI0 and OpenOCD cannot both be in use.

TMS/SWDIO used to be GPIO 25, Physical Pin 22. It moved because GPIO 25 is pulled low at boot and both JTAG and SWD expect a pull-up at the target, whereas GPIO 8 is pulled high. OpenOCD warns about the change on startup. The SWD-only `interface/raspberrypi-swd.cfg` keeps an older arrangement of its own, with SWCLK on GPIO 25 and SWDIO on GPIO 24, which is what Raspberry Pi's Pico debugging guides wire up.

Which config to pass depends on the model:

| Model | Config |
| --- | --- |
| Pi 4 and earlier, including Zero, Zero W and Zero 2 W | `interface/raspberrypi-native.cfg` |
| Pi 5 | `interface/raspberrypi5-gpiod.cfg` |

Pi 5 needs its own file because the GPIO pins hang off the RP1 chip across PCIe, out of reach of the native bit-bang driver. It falls back to the generic Linux gpiod driver, which is slower and has no adjustable clock speed.