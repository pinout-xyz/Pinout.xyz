<!--
---
name: Skywriter HAT
class: board
type: gesture,touch
formfactor: HAT
manufacturer: Pimoroni
description: Ein 3D Positions- und Gesten-Sensor.
url: http://shop.pimoroni.com/products/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
image: 'skywriter-hat.png'
pincount: 40
eeprom: yes
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: Reset
  '13':
    name: Transfer
i2c:
  '0x42':
    name: Gesture sensor
    device: mgc3130
-->
# Skywriter HAT

Skywriter HAT spürt die Position Deines Fingers über ihm in drei Dimensionen und gibt die somit die X-, Y- und Z-Koordinaten, welche Du in Deinen Python-Skripten verarbeiten kannst.

Er erkennt auch Gesten wie z.B. wischen und andere.

