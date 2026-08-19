<!--
---
name: DOTs
class: board
type: other
formfactor: HAT
manufacturer: Raspberry Pi
description: Une los puntos para hacer un circuito
url: http://www.raspberrypi.org/dots/
github: https://github.com/raspberrypilearning/dots
buy: https://thepihut.com/products/raspberry-pi-dots-board
image: 'rpf-dots.png'
pincount: 40
eeprom: no
power:
  '1':
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
    name: 'Color: Verde'
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
    name: 'Color: Naranja'
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
    name: 'Color: Rojo'
    direction: input
-->
# Raspberry Pi Dots

### Dots es un HAT para Raspberry Pi que te permite unir los puntos con pintura conductiva BARE!

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
