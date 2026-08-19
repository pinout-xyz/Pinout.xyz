<!--
---
description: Una maniera facile e veloce per imparare le basi del GPIO a basso prezzo. Tutto in un singolo HAT.
pin:
  '15':
    name: LED1 / verde
  '16':
    name: LED2 / ambra
  '18':
    name: LED3 / rosso
  '22':
    name: Bottone
  '29':
    name: Buzzer - cicalino
-->
# Traffic HAT

### Una maniera facile e veloce per imparare le basi del GPIO a basso prezzo. Tutto in un singolo HAT.

```python
import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BCM)

# Luci
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)

# Buzzer
IO.setup(5,IO.OUT)

# Bottone
IO.setup(25,IO.IN,pull_up_down=IO.PUD_UP)
```
