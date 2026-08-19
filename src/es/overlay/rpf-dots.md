<!--
---
description: Une los puntos para hacer un circuito
pin:
  bcm10:
    name: 'Color: Verde'
  bcm19:
    name: 'Color: Naranja'
  bcm27:
    name: 'Color: Rojo'
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
