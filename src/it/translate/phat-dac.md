<!--
---
name: pHAT DAC
class: board
type: audio
formfactor: pHAT
manufacturer: Pimoroni
description: An I2S digital to analog audio converter
buy: https://shop.pimoroni.com/products/phat-dac
image: 'phat-dac.png'
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
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
install:
  'devices':
  - 'i2s'
-->
#pHAT DAC

The pHAT DAC provides a high-quality digital to analog audio converter for the Raspberry Pi: 24-bits at 192KHz via the I2S interface on the 2x20 pin GPIO header. It has a 3.5mm stereo jack pre-assembled and can accommodate an optional RCA phono connector.

Though designed to match the format of the Raspberry Pi Zero it is compatible with all 40-pin GPIO Raspberry Pi variants (2/B+/A+/Zero).

To get the pHAT DAC set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/phatdac | bash
```
