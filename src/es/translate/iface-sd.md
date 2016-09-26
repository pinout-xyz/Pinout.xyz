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
#SDIO - SD Card Interface

SDIO is the SD host/eMMC interface on the Raspberry Pi. SD host signals are normally used for the microSD slot.

These pins are "SD host" on Alt0 and "eMMC" on Alt3.