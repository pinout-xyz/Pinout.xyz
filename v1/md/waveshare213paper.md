<!--
---
name: 2.13 Inch E-Paper pHAT
class: board
type: display
formfactor: pHAT
manufacturer: Waveshare
description: an E-Ink display pHAT for with embedded controller, communicating via SPI interface.
url: http://www.waveshare.com/wiki/2.13inch_e-Paper_HAT
buy: https://www.waveshare.com/product/2.13inch-e-paper-hat.htm
image: 'waveshare213paper.png'
pincount: 40
eeprom: no
power:
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
  '11':
    name: RST
  '19':
    name: DIN
  '23':
    name: CLK
  '18':
    name: BUSY
  '22':
    name: DC
  '24':
    name: CS
-->
# 2.13 Inch E-Ink Display pHAT

This is an E-Ink display HAT for Raspberry Pi, 2.13inch, 250x122 resolution, with embedded controller, communicating via SPI interface, supports partial refresh.

Due to the advantages like ultra low power consumption, wide viewing angle, clear display without electricity, it is an ideal choice for applications such as shelf label, industrial instrument, and so on.

This pHAT is powered from 5v, not 3v3, and regulates its own 3.3v rail on board. That regulator is switched rather than always on, so the display's supply can be cut to save power.

## Features

* 250x122 resolution
* SPI interface
* Support for partial refresh
* Low power consumption
