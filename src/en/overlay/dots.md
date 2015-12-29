<!--
---
type: board
name: Raspberry Pi Dots
manufacturer: Raspberry Pi Foundation
description: Join the dots to make a circuit
url: http://www.raspberrypi.org/dots/
github: https://github.com/raspberrypilearning/dots
formfactor: '40-way'
pincount: 40
eeprom: no
pin:
  bcm0:
    name: 'Color: Blue'
    direction: input
  bcm1:
    name: Dot 7
    direction: input
  bcm2:
    name: Dot 22
    direction: input
  bcm3:
    name: Dot 21
    direction: input
  bcm4:
    name: Dot 2
    direction: input
  bcm5:
    name: Dot 9
    direction: input
  bcm6:
    name: Dot 14
    direction: input
  bcm7:
    name: Dot 6
    direction: input
  bcm8:
    name: Dot 18
    direction: input
  bcm9:
    name: Dot 17
    direction: input
  bcm10:
    name: 'Color: Green'
    direction: input
  bcm11:
    name: Dot 8
    direction: input
  bcm12:
    name: Dot 10
    direction: input
  bcm13:
    name: Cloud
    direction: input
  bcm14:
    name: Dot 1
    direction: input
  bcm15:
    name: Dot 3
    direction: input
  bcm16:
    name: Dot 13
    direction: input
  bcm17:
    name: Dot 4
    direction: input
  bcm18:
    name: Dot 20
    direction: input
  bcm19:
    name: 'Color: Orange'
    direction: input
  bcm20:
    name: Bear
    direction: input
  bcm21:
    name: Dot 12
    direction: input
  bcm22:
    name: Dot 15
    direction: input
  bcm23:
    name: Dot 16
    direction: input
  bcm24:
    name: Dot 19
    direction: input
  bcm25:
    name: Dot 5
    direction: input
  bcm26:
    name: Dot 11
    direction: input
  bcm27:
    name: 'Color: Red'
    direction: input
-->
#Raspberry Pi Dots

###Dots is a Dot to Dot board for the Raspberry Pi that lets you join-the-dots with BARE Conductive Paint!

Every Dot on the Dots board is a "floating" metal contact just waiting to be pulled down to ground with a dab of paint.

To read a Dot you should set its corresponding pin as an INPUT and make sure it's pulled up like so:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
state = GPIO.input(dot_pin)
```

It's good practice to only turn on the PULLUP when you actually want to read the Dot, so a method like this is recommended for reading:

```python
def is_dot_connected(dot_pin):
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
    state = GPIO.input( dot_pin )
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_OFF)
    return state == 0
```
