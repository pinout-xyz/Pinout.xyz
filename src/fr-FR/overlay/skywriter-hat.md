<!--
---
name: Skywriter HAT
manufacturer: Pimoroni
url: https://github.com/pimoroni/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
description: A 3D positional and gesture sensor.
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: Reset
  '13':
    name: Transfer
-->
#Skywriter HAT

Skywriter HAT senses your finger's position above it in 3 dimensions, outputting an X, Y, Z axis
which you can use in your Python scripts.

It also recognises gestures, including swipes and more.