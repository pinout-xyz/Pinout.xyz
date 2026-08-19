<!--
---
description: carte multi-usage avec buzzer, LED et bouton
pin:
  '15':
    name: LED1 / vert
  '16':
    name: LED2 / orange
  '18':
    name: LED3 / rouge
  '22':
    name: bouton
  '29':
    name: buzzer
-->
# Traffic HAT

### Contrôler les broches GPIO du Traffic HAT depuis votre Raspberry Pi est aisé:

```python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# LEDs
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

# Buzzer
GPIO.setup(5,GPIO.OUT)

# Bouton
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)
```
