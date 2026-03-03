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

* Alt5 on GPIOs 4, 5, 6, 12 and 13
* Alt4 on GPIOs 22, 23, 24, 25, 26 and 27