<!--
---
type: board
name: Traffic HAT
manufacturer: Ryanteck LTD.
description: A quick and easy way to learn the basics of GPIO on a budget. All in a nice HAT.
url: http://www.ryanteck.uk/store/traffichat
buy: http://www.ryanteck.uk/store/traffichat
formfactor: 'HAT'
pincount: 40
eeprom: yes
pin:
  '15':
    name: LED1 / Green
    direction: output
    active: high
  '16':
    name: LED2 / Amber
    direction: output
    active: high
  '18':
    name: LED3 / Red
    direction: output
    active: high
  '22':
    name: Button
    direction: input
    active: high
  '29':
    name: Buzzer
    direction: output
    active: high
-->
#Traffic HAT

###A quick and easy way to learn the basics of GPIO on a budget. All in a nice HAT.

```python
import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BCM)

#Lights
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)

#Buzzer
IO.setup(5,IO.OUT)

#Button
IO.setup(25,IO.IN,pull_up_down=IO.PUD_UP)
```