<!--
---
name: Raspberry Pi Dots
description: créez un circuit avec de la peinture électrique
url: http://www.raspberrypi.org/dots/
github: https://github.com/raspberrypilearning/dots
pincount: 38
pin:
  bcm0:
    name: 'couleur: bleue'
    direction: input
  bcm1:
    name: point 7
    direction: input
  bcm2:
    name: point 22
    direction: input
  bcm3:
    name: point 21
    direction: input
  bcm4:
    name: point 2
    direction: input
  bcm5:
    name: point 9
    direction: input
  bcm6:
    name: point 14
    direction: input
  bcm7:
    name: point 6
    direction: input
  bcm8:
    name: point 18
    direction: input
  bcm9:
    name: point 17
    direction: input
  bcm10:
    name: 'couleur: vert'
    direction: input
  bcm11:
    name: point 8
    direction: input
  bcm12:
    name: point 10
    direction: input
  bcm13:
    name: 'forme: nuage'
    direction: input
  bcm14:
    name: point 1
    direction: input
  bcm15:
    name: point 3
    direction: input
  bcm16:
    name: point 13
    direction: input
  bcm17:
    name: point 4
    direction: input
  bcm18:
    name: point 20
    direction: input
  bcm19:
    name: 'couleur: orange'
    direction: input
  bcm20:
    name: 'forme: ours'
    direction: input
  bcm21:
    name: point 12
    direction: input
  bcm22:
    name: point 15
    direction: input
  bcm23:
    name: point 16
    direction: input
  bcm24:
    name: point 19
    direction: input
  bcm25:
    name: point 5
    direction: input
  bcm26:
    name: point 11
    direction: input
  bcm27:
    name: 'couleur: rouge'
    direction: input
-->
#Raspberry Pi Dots

###Dots est un project éducatif qui vous permet de créez un circuit en joignant les points représentés avec de la peinture électrique.

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