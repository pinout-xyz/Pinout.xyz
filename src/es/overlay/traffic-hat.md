<!--
---
name: Traffic HAT
class: board
type: multi
formfactor: HAT
manufacturer: Ryanteck
description: Una manera rápida de aprender lo básico del GPIO con un bajo presupuesto. Todo en un bonito HAT.
github: https://github.com/PiSupply/Ryanteck/tree/master/RTK%20Traffic%20HAT
buy: https://uk.pi-supply.com/products/traffic-hat-for-raspberry-pi
image: 'traffic-hat.png'
pincount: 40
eeprom: yes
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
  '15':
    name: LED1 / Verde
    direction: salida
    active: alto (encendido)
  '16':
    name: LED2 / Amarillo
    direction: salida
    active: alto (encendido)
  '18':
    name: LED3 / Rojo
    direction: salida
    active: alto (encendido)
  '22':
    name: Botón
    direction: entrada
    active: alto (encendido)
  '29':
    name: Zumbador
    direction: salida
    active: alto (encendido)
-->
# Traffic HAT

### Una manera rápida de aprender lo básico del GPIO con un bajo presupuesto. Todo en un bonito HAT.

```python
import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BCM)

# Luces
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)

# Zumbador
IO.setup(5,IO.OUT)

# Botón
IO.setup(25,IO.IN,pull_up_down=IO.PUD_UP)
```
