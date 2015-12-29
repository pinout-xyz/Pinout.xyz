<!--
---
type: board
name: Display-o-Tron 3000
manufacturer: Pimoroni
description: A 3-line character LCD with an RGB backlight and joystick
url: https://github.com/pimoroni/dot3k
github: https://github.com/pimoroni/dot3k
buy: https://shop.pimoroni.com/products/displayotron-3000
formfactor: '26-way'
pincount: 26
eeprom: no
power: 3v3,5v
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Joystick Button
    mode: input
    active: low
  '11':
    name: Joystick Left
    mode: input
    active: low
  '13':
    name: Joystick Up
    mode: input
    active: low
  '15':
    name: Joystick Right
    mode: input
    active: low
  '19':
    mode: spi
  '21':
    name: Joystick Down
    mode: input
    active: low
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '23':
    mode: spi
install:
  'devices':
    - 'i2c'
    - 'spi'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'dot3k'
  'examples': 'python/examples/'
-->
#Display-o-Tron 3000

The Display-o-Tron 3000 is a 3-line character LCD with an RGB backlight and joystick

To get the module set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/displayotron | bash
```

And follow the instructions!
