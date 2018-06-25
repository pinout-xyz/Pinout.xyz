<!--
---
name: Fe-Pi Digital Audio Z V1
class: board
type: audio
formfactor: pHAT
manufacturer: Fe-Pi
description: S/PDIF audio solution for the Raspberry Pi
url: https://fe-pi.com/products/fe-pi-digital-audio-z-v1
buy: https://fe-pi.com/products/fe-pi-digital-audio-z-v1
image: 'fepi-digital-audio-z-V1.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: BCLK (Bit Clock)
    mode: i2s
  '35':
    name: LRCLK (Left/Right Clock)
    mode: i2s
  '38':
    name: DIN (Data In)
    mode: i2s
  '40':
    name: DOUT (Data Out)
    mode: i2s
i2c:
  '0x3B':
    name: S/PDIF Digital Interface Transceiver
    device: WM8804G
-->
#Fe-Pi Digital Audio Z V1

The Fe-Pi Digital Audio Z V1 is designed to provide a complete low cost audio solution for Raspberry Pi 2, 3, and Zero, needing S/PDIF output.

## Features ##

* Small Raspberry Pi Zero PCB footprint.
* Cirrus Logic WM8804 S/PDIF Digital Interface Transceiver.
* RCA and optical TOSLINK Output jacks.
* 2x20pin 2.54mm female header and 40pin male breakable header included!
