<!--
---
name: pHAT BEAT
class: board
type: audio
formfactor: pHAT
manufacturer: Pimoroni
description: Stereo I2S DAC, AMP and VU meter
buy: https://shop.pimoroni.com/products/phat-beat
github: https://github.com/pimoroni/phat-beat
buy: https://shop.pimoroni.com/products/phat-beat
image: 'phat-beat.png'
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
  '16':
    name: Data
    mode: output
    active: high
  '18':
    name: Clock
    mode: output
    active: high
install:
  'devices':
  - 'i2s'
  - 'i2c'
i2c:
  '0x54':
    name: LED driver
    device: sn3218
-->
#pHAT BEAT

To get the pHAT BEAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/phatbeat | bash
```
