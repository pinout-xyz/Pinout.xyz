<!--
---
name: Traffic HAT
class: board
type: multi
formfactor: HAT
manufacturer: Ryanteck
description: Ein schneller und einfacher Weg um die grundlegenden Fähigkeiten der GPIO-Ports zu erkunden.
github: https://github.com/PiSupply/Ryanteck/tree/master/RTK%20Traffic%20HAT
buy: https://uk.pi-supply.com/products/traffic-hat-for-raspberry-pi
image: 'traffic-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
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
  '15':
    name: LED1 / Grün
    direction: output
    active: high
  '16':
    name: LED2 / Orange
    direction: output
    active: high
  '18':
    name: LED3 / Rot
    direction: output
    active: high
  '22':
    name: Taster
    direction: input
    active: high
  '29':
    name: Buzzer
    direction: output
    active: high
-->
# Traffic HAT

### Ein schneller und einfacher Weg um die grundlegenden Fähigkeiten der GPIO-Ports zu erkunden.

```python
import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BCM)

# Lights
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)

# Buzzer
IO.setup(5,IO.OUT)

# Button
IO.setup(25,IO.IN,pull_up_down=IO.PUD_UP)
```
