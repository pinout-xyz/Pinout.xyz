<!--
---
name: Explorer HAT Pro
class: board
type: adc,io,motor,multi,touch
formfactor: HAT
manufacturer: Pimoroni
description: Una placa completa, con luz, entradas, entradas táctiles y salidas.
url: http://shop.pimoroni.com/products/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
image: 'explorer-hat-pro.png'
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
    active: alto (encendido)
  '11':
    name: LED 2
    mode: output
    active: alto (encendido)
  '13':
    name: LED 3
    mode: output
    active: alto (encendido)
  '15':
    name: Entrada 2
    mode: input
    active: alto (encendido)
  '16':
    name: Entrada 1
    mode: input
    active: alto (encendido)
  '18':
    name: Entrada 3
    mode: input
    active: alto (encendido)
  '22':
    name: Entrada 4
    mode: input
    active: alto (encendido)
  '29':
    name: LED 4
    mode: output
    active: alto (encendido)
  '31':
    name: Salida 1
    mode: output
    active: alto (encendido)
  '32':
    name: Salida 2
    mode: output
    active: alto (encendido)
  '33':
    name: Salida 3
    mode: output
    active: alto (encendido)
  '35':
    name: Motor 1 +
    mode: output
    active: alto (encendido)
  '36':
    name: Salida 4
    mode: output
    active: alto (encendido)
  '37':
    name: Motor 2 -
    mode: output
    active: alto (encendido)
  '38':
    name: Motor 1 -
    mode: output
    active: alto (encendido)
  '40':
    name: Motor 2 +
    mode: output
    active: alto (encendido)
i2c:
  '0x28':
    name: Sensor capacitivo
    device: cap1208
  '0x48':
    name: Entrada Analógica
    device: ads1015
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
# Explorer HAT Pro

Entradas y salidas de 5V, paneles táctiles, LEDs, entradas analógicas y un Puente-H para controlar motores componen el Explorer HAT Pro.

Para preparar e instalar el HAT utiliza la siguiente línea:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import explorerhat
explorerhat.light.on()
```
