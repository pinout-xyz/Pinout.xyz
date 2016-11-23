<!--
---
name: DOTs
class: board
type: otro
formfactor: Otro
manufacturer: Raspberry Pi
description: Une los puntos para hacer un circuito
url: http://www.raspberrypi.org/dots/
github: https://github.com/raspberrypilearning/dots
buy: https://thepihut.com/products/raspberry-pi-dots-board
image: 'rpf-dots.png'
pincount: 40
eeprom: no
pin:
  bcm0:
    name: 'Color: Blue'
    direction: entrada
  bcm1:
    name: Dot 7
    direction: entrada
  bcm2:
    name: Dot 22
    direction: entrada
  bcm3:
    name: Dot 21
    direction: entrada
  bcm4:
    name: Dot 2
    direction: entrada
  bcm5:
    name: Dot 9
    direction: entrada
  bcm6:
    name: Dot 14
    direction: entrada
  bcm7:
    name: Dot 6
    direction: entrada
  bcm8:
    name: Dot 18
    direction: entrada
  bcm9:
    name: Dot 17
    direction: entrada
  bcm10:
    name: 'Color: Verde'
    direction: entrada
  bcm11:
    name: Dot 8
    direction: entrada
  bcm12:
    name: Dot 10
    direction: entrada
  bcm13:
    name: Cloud
    direction: entrada
  bcm14:
    name: Dot 1
    direction: entrada
  bcm15:
    name: Dot 3
    direction: entrada
  bcm16:
    name: Dot 13
    direction: entrada
  bcm17:
    name: Dot 4
    direction: entrada
  bcm18:
    name: Dot 20
    direction: entrada
  bcm19:
    name: 'Color: Naranja'
    direction: entrada
  bcm20:
    name: Bear
    direction: entrada
  bcm21:
    name: Dot 12
    direction: entrada
  bcm22:
    name: Dot 15
    direction: entrada
  bcm23:
    name: Dot 16
    direction: entrada
  bcm24:
    name: Dot 19
    direction: entrada
  bcm25:
    name: Dot 5
    direction: entrada
  bcm26:
    name: Dot 11
    direction: entrada
  bcm27:
    name: 'Color: Rojo'
    direction: entrada
-->
#Raspberry Pi Dots

###Dots es un HAT para Raspberry Pi que te permite unir los puntos con pintura conductiva BARE!

Cada punto en la placa Dots es un contacto de metal "flotante", esperando a ser conectado a tierra con una gota de pintura.

Para leer un punto, debes configurar el pin correspondiente como INPUT (entrada), y también el pull-up:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM )
GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
state = GPIO.entrada(dot_pin)
```

Es una buena práctica activar únicamente el pull-up cuando de verdad vas a leer el punto, así que se recomienda un método como este:

```python
def is_dot_connected(dot_pin):
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
    state = GPIO.entrada( dot_pin )
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_OFF)
    return state == 0
```
