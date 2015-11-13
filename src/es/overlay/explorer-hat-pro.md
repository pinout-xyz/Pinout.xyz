<!--
---
name: Explorer HAT Pro
manufacturer: Pimoroni
url: https://github.com/pimoroni/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
description: Una placa completa, con luz, entradas, entradas táctiles y salidas.
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
  'examples': 'examples/'
pincount: 40
i2c:
  '0x28':
    name: Sensor capacitivo
    device: cap1208
  '0x48':
    name: Entrada Analógica
    device: ads1015
pin:
  '3': {}
  '5': {}
  '7':
    name: LED 1
    mode: salida
    active: alto (encendido)
  '8': {}
  '10': {}
  '11':
    name: LED 2
    mode: salida
    active: alto (encendido)
  '12': {}
  '13':
    name: LED 3
    mode: salida
    active: alto (encendido)
  '15':
    name: Entrada 2
    mode: entrada
    active: alto (encendido)
  '16':
    name: Entrada 1
    mode: entrada
    active: alto (encendido)
  '18':
    name: Entrada 3
    mode: entrada
    active: alto (encendido)
  '19': {}
  '21': {}
  '22':
    name: Entrada 4
    mode: entrada
    active: alto (encendido)
  '23': {}
  '24': {}
  '29':
    name: LED 4
    mode: salida
    active: alto (encendido)
  '31':
    name: Salida 1
    mode: salida
    active: alto (encendido)
  '32':
    name: Salida 2
    mode: salida
    active: alto (encendido)
  '33':
    name: Salida 3
    mode: salida
    active: alto (encendido)
  '35':
    name: Motor 1 +
    mode: salida
    active: alto (encendido)
  '36':
    name: Salida 4
    mode: salida
    active: alto (encendido)
  '37':
    name: Motor 2 -
    mode: salida
    active: alto (encendido)
  '38':
    name: Motor 1 -
    mode: salida
    active: alto (encendido)
  '40':
    name: Motor 2 +
    mode: salida
    active: alto (encendido)
-->
#Explorer HAT Pro

Entradas y salidas de 5V, paneles táctiles, LEDs, entradas analógicas y un Puente-H para controlar motores componen el Explorer HAT Pro.

Para preparar e instalar el HAT utiliza la siguiente línea:

```bash
curl -sS get.pimoroni.com/explorerhat
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import explorerhat
explorerhat.light.on()
```
