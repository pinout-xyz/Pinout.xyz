<!--
---
name: Pi-LITE-r
class: board
type: led
formfactor: Otro
manufacturer: Ciseco
description: An 8 LED strip for the Raspberry Pi
url: http://gpiozero.readthedocs.io/en/v1.3.1/api_boards.html#piliter
buy: http://cpc.farnell.com/wirelessthings/pi-liter/pi-lite-junior-led-io-board-for/dp/SC13293
image: 'pi-liter.png'
pincount: 26
eeprom: no
power:
  '1':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
pin:
  '7':
    name: LED1
    direction: output
    active: high
  '11':
    name: LED2
    direction: output
    active: high
  '12':
    name: LED4
    direction: output
    active: high
  '13':
    name: LED3
    direction: output
    active: high
  '15':
    name: LED5
    direction: output
    active: high
  '16':
    name: LED6
    direction: output
    active: high
  '18':
    name: LED7
    direction: output
    active: high
  '22':
    name: LED8
    direction: output
    active: high
-->
#Pi-LITE-r

Pi-LITE-r es una placa adicional completa para Raspberry Pi. Cuenta con 8 LEDs blanco ultra-brillantes y se conecta directamente a los GPIO. Puede utilizarse en proyectos I/O para dar información del estado. Iluminar los 8 LEDs consume poca corriente, menos que un sólo LED (20 mA nominales, 14.4 mA para Pi-LITE-r)

Aplicaciones:

* Monitor de estado I/O
* Gráficos de barras
* Control de luz
* Indicador de actividad
* Efectos de luz

```python
from gpiozero import PiLiter
from time import sleep

lite = PiLiter()

for led in lite:
    led.on()
    sleep(0.1)
    led.off()

lite.on()
sleep(5)
```
