<!--
---
name: LEDBorg
class: board
type: led
formfactor: Custom
manufacturer: PiBorg
description: A single RGB LED for your Raspberry Pi
url: https://www.piborg.org/ledborg-new/install
buy: https://www.piborg.org/ledborg
image: 'piborg-led-borg.png'
pincount: 26
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
pin:
  '11':
    name: Red LED
    direction: output
    active: high
    description: PiBorg Red LED
  '13':
    name: Green LED
    direction: input
    active: high
    description: PiBorg Green LED
  '15':
    name: Blue LED
    direction: output
    active: high
    description: PiBorg Blue LED
-->
# LedBorg

The PiBorg LedBorg is an ultra-bright RGB LED board for the Raspberry Pi.

```python
from gpiozero import LedBorg
from time import sleep

lb = LedBorg()

while True:
    r, g, b = 0, 0, 0
    for i in range(100):
        r = i / 100.0
        lb.value = (r, g, b)
        sleep(0.01)
    for i in range(100):
        g = i / 100.0
        sleep(0.01)
        lb.value = (r, g, b)
    for i in range(100):
        b = i / 100.0
        lb.value = (r, g, b)
        sleep(0.01)
```

[GPIO Zero docs](http://gpiozero.readthedocs.io/en/v1.3.1/api_boards.html#ledborg)
