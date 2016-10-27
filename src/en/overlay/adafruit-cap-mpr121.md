<!--
---
name: Capacitive Touch HAT
class: board
type: touch
formfactor: HAT
manufacturer: Adafruit
description: Create electronics that can react to human touch with up to 12 individual sensors
url: https://www.adafruit.com/products/2340
github: https://github.com/adafruit/Adafruit_Python_MPR121
buy: https://www.adafruit.com/products/2340
image: 'adafruit-cap-mpr121.png'
pincount: 40
eeprom: yes
power:
  '1':
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
i2c:
  '0x5A':
    name: Cap Touch
    device: mpr121
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
-->
# Capacitive Touch HAT

This Raspberry Pi add-on board provides 12 capacitive touch inputs and all the logic to read them over a simple I2C communication bus.

Baded on the MPR121 chip, this HAT allows you to create electronics that can react to human touch, with up to 12 individual sensors.

## Code

```python
from Adafruit_MPR121 import MPR121
from time import sleep

cap = MPR121.MPR121()

last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    for i in range(12):
        pin_bit = 1 << i
        if current_touched & pin_bit and not last_touched & pin_bit:
            print("{} touched!".format(i))
    last_touched = current_touched
    sleep(0.1)
```
