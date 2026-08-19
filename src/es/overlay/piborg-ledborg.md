<!--
---
description: Un único LED RGB para tu Raspberry Pi
-->
### PiBorg LedBorg

El LedBorg es una placa con un LED RGB ultra-brillante para la Rasberry Pi.

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
