<!--
---
description: créez un circuit avec de la peinture électrique
pin:
  bcm0:
    name: 'couleur: bleue'
  bcm1:
    name: point 7
  bcm2:
    name: point 22
  bcm3:
    name: point 21
  bcm4:
    name: point 2
  bcm5:
    name: point 9
  bcm6:
    name: point 14
  bcm7:
    name: point 6
  bcm8:
    name: point 18
  bcm9:
    name: point 17
  bcm10:
    name: 'couleur: vert'
  bcm11:
    name: point 8
  bcm12:
    name: point 10
  bcm13:
    name: 'forme: nuage'
  bcm14:
    name: point 1
  bcm15:
    name: point 3
  bcm16:
    name: point 13
  bcm17:
    name: point 4
  bcm18:
    name: point 20
  bcm19:
    name: 'couleur: orange'
  bcm20:
    name: 'forme: ours'
  bcm21:
    name: point 12
  bcm22:
    name: point 15
  bcm23:
    name: point 16
  bcm24:
    name: point 19
  bcm25:
    name: point 5
  bcm26:
    name: point 11
  bcm27:
    name: 'couleur: rouge'
-->
# Raspberry Pi Dots

### Dots est un project éducatif qui vous permet de créez un circuit en joignant les points représentés avec de la peinture électrique.

Les points du circuit sont des contacts métalliques que la peinture connectera à la masse, créant un effect de résistance de rappel.

Pour lire l'état d'un contact métallique, assurez vous de déclarer la broche correspondante en tant qu'entrée et en 'pull-up', comme ceci:


```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
state = GPIO.input(dot_pin)
```

Il est cependant recommandé de n'activer le 'pull-up' que lorsque nécessaire pour la requête, par l'intermédiaire d'une fonction telle que celle qui suit:

```python
def is_dot_connected(dot_pin):
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
    state = GPIO.input( dot_pin )
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_OFF)
    return state == 0
```
