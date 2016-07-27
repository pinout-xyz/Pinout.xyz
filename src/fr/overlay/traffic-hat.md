<!--
---
name: Traffic HAT
class: board
type: tous
manufacturer: Ryanteck LTD.
url: http://www.ryanteck.uk/store/traffichat
buy: http://www.ryanteck.uk/store/traffichat
description: carte multi-usage avec buzzer, LED et bouton
pincount: 40
pin:
  '15':
    name: LED1 / vert
    direction: output
    active: high
  '16':
    name: LED2 / orange
    direction: output
    active: high
  '18':
    name: LED3 / rouge
    direction: output
    active: high
  '22':
    name: bouton
    direction: input
    active: high
  '29':
    name: buzzer
    direction: output
    active: high
-->
#Traffic HAT

###Contrôler les broches GPIO du Traffic HAT depuis votre Raspberry Pi est aisé: 

```python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#LEDs
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

#Buzzer
GPIO.setup(5,GPIO.OUT)

#Bouton
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)
```