<!--
---
name: LedBorg
class: board
type: Tous
formfactor: Autre
manufacturer: PiBorg
description: une carte LED RGB pour la Raspberry Pi
url: https://www.piborg.org/ledborg-new/install
buy: https://www.piborg.org/ledborg
image: 'piborg-led-borg.png'
pincount: 26
eeprom: no
pin:
  '11':
    name: LED rouge
    direction: output
    active: high
    description: LED rouge de la PiBorg
  '13':
    name: LED verte
    direction: input
    active: high
    description: LED verte de la PiBorg
  '15':
    name: LED bleue
    direction: output
    active: high
    description: LED bleue de la PiBorg
-->
### PiBorg LedBorg

La carte PiBorg LedBorg ajoute une LED tricolore RGB à votre Raspberry Pi.

```python
from gpiozero import LedBorg
from time import sleep

lb = LedBorg()

while True:
    r, g, b = 0, 0, 0
    for i in range(100):
        r = i / 100
        lb.value = (r, g, b)
        sleep(0.01)
    for i in range(100):
        g = i / 100
        sleep(0.01)
        lb.value = (r, g, b)
    for i in range(100):
        b = i / 100
        lb.value = (r, g, b)
        sleep(0.01)
```

[GPIO Zero docs](http://gpiozero.readthedocs.io/en/v1.3.1/api_boards.html#ledborg)
