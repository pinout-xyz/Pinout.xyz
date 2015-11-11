<!--
---
name: Display-o-Tron 3000
manufacturer: Pimoroni
github: https://github.com/pimoroni/dot3k
url: https://github.com/pimoroni/dot3k
description: A 3-line character LCD with an RGB backlight and joystick
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
pincount: 40
pin:
  3:
    mode: i2c
  5:
    mode: i2c
  7:
    name: Joystick Button
    mode: input
    active: low
  11:
    name: Joystick Left
    mode: input
    active: low
  13:
    name: Joystick Up
    mode: input
    active: low
  15:
    name: Joystick Right
    mode: input
    active: low
  19:
    mode: spi
  21:
    name: Joystick Down
    mode: input
    active: low
  22:
    name: LCD CMD/DATA
    mode: output
    active: high
  23:
    mode: spi
-->
#Display-o-Tron 3000

The Display-o-Tron 3000 is a 3-line character LCD with an RGB backlight and joystick

To get the module set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/dot3k | bash
```

And follow the instructions!
