<!--
---
description: Ein schneller und einfacher Weg um die grundlegenden Fähigkeiten der GPIO-Ports zu erkunden.
pin:
  '15':
    name: LED1 / Grün
  '16':
    name: LED2 / Orange
  '18':
    name: LED3 / Rot
  '22':
    name: Taster
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
