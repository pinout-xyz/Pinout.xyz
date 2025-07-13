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
  '1':
  '2':
ground:
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '12':
    name: I2S
  '16':
    name: Data
    mode: output
    active: high
  '18':
    name: Clock
    mode: output
    active: high
  '29':
    name: Fast Forward
    mode: input
    active: low
  '31':
    name: Play/Pause
    mode: input
    active: low
  '32':
    name: On/Off
    mode: input
    active: low
  '33':
    name: Rewind
    mode: input
    active: low
  '35':
    name: I2S
  '36':
    name: Volume Up
    mode: input
    active: low
  '37':
    name: Volume Down
    mode: input
    active: low
  '40':
    name: I2S
install:
  'devices':
  - 'i2s'
-->
# pHAT BEAT

Para hacer funcionar el pHAT BEAT puedes utilizar nuestro instalador de una línea:

```bash
curl -sS https://get.pimoroni.com/phatbeat | bash
```
