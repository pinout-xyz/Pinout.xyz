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

SDIO es la interfaz host de SD/eMMC para Raspberry Pi. Las señales SD host normalmente son utilizadas para la tarjeta microSD.

Estos pines son "SD host" en Alt0 y "eMMC" en Alt3.
