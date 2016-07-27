<!--
---
name: Skywriter HAT
class: board
type: alle
formfactor: HAT
manufacturer: Pimoroni
image: 'image.png'
url: https://github.com/pimoroni/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
description: Ein 3D Positions- und Gesten-Sensor.
install:
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'skywriter'
  'examples': 'python/examples/'
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

Skywriter HAT spürt die Position Deines Fingers über ihm in drei Dimensionen und gibt die somit die X-, Y- und Z-Koordinaten, welche Du in Deinen Python-Skripten verarbeiten kannst.

Er erkennt auch Gesten wie z.B. wischen und andere.

