<!--
---
type: board
name: Skywriter HAT
manufacturer: Pimoroni
description: A 3D positional and gesture sensor.
url: https://github.com/pimoroni/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
formfactor: 'HAT'
pincount: 40
eeprom: yes
power: 3v3
i2c:
  '0x42':
    name: Gesture sensor
    device: MGC3130
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: Reset
  '13':
    name: Transfer
install:
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'skywriter'
  'examples': 'python/examples/'
-->
#Skywriter HAT

Skywriter HAT senses your finger's position above it in 3 dimensions, outputting an X, Y, Z axis
which you can use in your Python scripts.

It also recognises gestures, including swipes and more.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/skywriter | bash
```

And follow the instructions!
