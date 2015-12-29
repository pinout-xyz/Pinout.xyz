<!--
---
name: Traffic HAT
description: Una maniera facile e veloce per imparare le basi del GPIO a basso prezzo. Tutto in un singolo HAT.
pincount: 40
pin:
  '15':
    name: LED1 / verde
    direction: output
    active: high
  '16':
    name: LED2 / ambra
    direction: output
    active: high
  '18':
    name: LED3 / rosso
    direction: output
    active: high
  '22':
    name: Bottone
    direction: input
    active: high
  '29':
    name: Buzzer - cicalino
    direction: output
    active: high
-->
#Traffic HAT

###Una maniera facile e veloce per imparare le basi del GPIO a basso prezzo. Tutto in un singolo HAT.

```python
import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BCM)

#Luci
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)

#Buzzer
IO.setup(5,IO.OUT)

#Bottone
IO.setup(25,IO.IN,pull_up_down=IO.PUD_UP)
```