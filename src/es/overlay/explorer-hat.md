<!--
---
name: Explorer HAT
class: board
type: io,touch
formfactor: HAT
manufacturer: Pimoroni
description: Una placa completa, con luz, entradas, entradas táctiles y salidas.
url: http://shop.pimoroni.com/products/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
image: 'explorer-hat.png'
pincount: 40
eeprom: yes
power:
  '2':
  '17':
ground:
  '6':
  '9':
  '14':
  '25':
  '30':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: LED 1
    mode: output
    active: high
  '11':
    name: LED 2
    mode: output
    active: high
  '13':
    name: LED 3
    mode: output
    active: high
  '15':
    name: Entrada 2
    mode: input
    active: high
  '16':
    name: Entrada 1
    mode: input
    active: high
  '18':
    name: Entrada 3
    mode: input
    active: high
  '22':
    name: Entrada 4
    mode: input
    active: high
  '29':
    name: LED 4
    mode: output
    active: high
  '31':
    name: Salida 1
    mode: output
    active: high
  '32':
    name: Salida 2
    mode: output
    active: high
  '33':
    name: Salida 3
    mode: output
    active: high
  '36':
    name: Salida 4
    mode: output
    active: high
i2c:
  '0x28':
    name: Cap Touch
    device: cap1208
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'explorerhat'
  'python3':
    - 'explorerhat'
-->
# Explorer HAT

Entradas y salidas de 5V, paneles táctiles y LEDs componen el Explorer HAT.

Para preparar e instalar el HAT utiliza la siguiente línea:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import explorerhat
explorerhat.light.on()
```
