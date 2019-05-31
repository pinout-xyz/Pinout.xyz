<!--
---
name: ModMyPi Christmas Tree Star
class: board
type: LED
formfactor: Custom
manufacturer: ModMyPi
description: A star shaped LED add-on board for the Raspberry Pi which can be used as a Christmas Tree topper.
url: https://www.modmypi.com/blog/christmas-tree-star-guide
github: https://github.com/modmypi/Programmable-Christmas-Star
buy: https://www.modmypi.com/raspberry-pi-christmas-tree-star
image: 'modmypi-star.png'
pincount: 40
eeprom: no
power:
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    name: LED Inner
    mode: output
    active: high
  '5':
    name: LED S
    mode: output
    active: high
  '7':
    name: LED R
    mode: output
    active: high
  '8':
    name: LED T
    mode: output
    active: high
  '10':
    name: LED W
    mode: output
    active: high
  '11':
    name: LED Q
    mode: output
    active: high
  '12':
    name: LED V
    mode: output
    active: high
  '13':
    name: LED P
    mode: output
    active: high
  '15':
    name: LED O
    mode: output
    active: high
  '16':
    name: LED U
    mode: output
    active: high
  '18':
    name: LED X
    mode: output
    active: high
  '19':
    name: LED N
    mode: output
    active: high
  '21':
    name: LED M
    mode: output
    active: high
  '22':
    name: LED Y
    mode: output
    active: high
  '23':
    name: LED L
    mode: output
    active: high
  '24':
    name: LED B
    mode: output
    active: high
  '26':
    name: LED A
    mode: output
    active: high
  '29':
    name: LED K
    mode: output
    active: high
  '31':
    name: LED J
    mode: output
    active: high
  '32':
    name: LED C
    mode: output
    active: high
  '33':
    name: LED I
    mode: output
    active: high
  '35':
    name: LED H
    mode: output
    active: high
  '36':
    name: LED F
    mode: output
    active: high
  '37':
    name: LED G
    mode: output
    active: high
  '38':
    name: LED E
    mode: output
    active: high
  '40':
    name: LED D
    mode: output
    active: high
-->
#ModMyPi Christmas Tree Star

The ModMy Pi Christmas Tree Star is an LED add-on board for the Raspberry Pi designed to go on top of your Christmas tree. There are 30 white LEDs controllable through a Python library which extends GPIO Zero and is available on GitHub.

```
from star import Star
from time import sleep

# Initialise the star
star = Star()

# Turn the star on and off.
star.on()
sleep(1)
star.off()

# Turn the inner and outer LEDs off.
star.outer.on()
sleep(1)
star.off()
star.inner.on()
sleep(1)
star.off()

# Turn on individual LEDs on the outer rim.
star.outer.A.on()
star.outer.F.on()
star.outer.P.on()
star.outer.X.on()
sleep(1)
star.off()
```