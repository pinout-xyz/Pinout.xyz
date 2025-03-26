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
  '4':
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

## 5V Power

Blinkt! does not require *both* Physical Pin 2 and Physical Pin 4:

* Physical Pin 4 is used for 5v power on all Blinkt! boards since 2018
* Physical Pin 2 was used for 5v power on first run Blinkt! boards prior to 2018

If your Blinkt! doesn't work with one, try swapping over to the other or - if all else fails - wiring both.

## Installing

To get started you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/blinkt | bash
```

## Code

```python
from blinkt import set_pixel, show
from random import randint
from time import sleep

while True:
    for pixel in range(8):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        set_pixel(pixel, r, g, b)
        show()
        sleep(0.1)
```
