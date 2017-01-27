<!--
---
name: Speaker pHAT
class: board
type: audio
formfactor: pHAT
manufacturer: Pimoroni
description: An I2S digital speaker and VU meter
buy: https://shop.pimoroni.com/products/speaker-phat
image: 'speaker-phat.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
install:
  'devices':
  - 'i2s'
  - 'i2c'
i2c:
  '0x54':
    name: LED driver
    device: sn3218
-->
#Speaker pHAT

Speaker pHAT crams an I2S DAC and mono amplifier, a tiny 8Ω 2W speaker, and a 10 LED bar graph all on a board no bigger than a Pi zero.

Though designed to match the format of the Raspberry Pi Zero it is compatible with all 40-pin GPIO Raspberry Pi variants (2/3/B+/A+/Zero).

To get the Speaker pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/speakerphat | bash
```
