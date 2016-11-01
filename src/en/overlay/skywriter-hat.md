<!--
---
name: Skywriter HAT
class: board
type: 'gesture,touch'
formfactor: HAT
manufacturer: Pimoroni
description: A 3D positional and gesture sensor
url: http://shop.pimoroni.com/products/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
image: 'skywriter-hat.png'
pincount: 40
eeprom: yes
power:
  '17':
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
i2c:
  '0x42':
    name: Gesture sensor
    device: mgc3130
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
