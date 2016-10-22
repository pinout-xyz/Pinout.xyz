<!--
---
name: 'Blinkt!'
class: board
type: led
formfactor: Custom
manufacturer: Pimoroni
description: Slimline board with 8 super-bright RGB LED indicators
url: http://blog.pimoroni.com/blinkt/
github: https://github.com/pimoroni/blinkt
buy: https://shop.pimoroni.com/products/blinkt
image: 'blinkt.png'
pincount: 40
eeprom: no
power:
  '2':
ground:
  '6':
pin:
  '16':
    name: Data
    mode: output
    active: high
  '18':
    name: Clock
    mode: output
    active: high
-->
# Blinkt!

Blinkt! is a super slimline Raspberry Pi Add-on board with 8 APA-102 LEDs.

## Code

```python
from blinkt import set_pixel, show
from random import randint
from time import sleep

while True:
    for pixel in range(8):
        r = randint(255)
        g = randint(255)
        b = randint(255)
        set_pixel(pixel, r, g, b)
        show()
        sleep(0.1)
```
