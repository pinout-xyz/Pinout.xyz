<!--
---
name: Explorer pHAT
class: board
type: adc,io,motor
formfactor: pHAT
manufacturer: Pimoroni
description: An all-in-one input, output and motor add-on board
buy: https://shop.pimoroni.com/products/explorer-phat
github: https://github.com/pimoroni/explorer-hat
buy: https://shop.pimoroni.com/products/explorer-phat
image: 'explorer-phat.png'
pincount: 40
eeprom: no
power:
  '2':
  '17':
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
    mode: i2c
  '5':
    mode: i2c
  '15':
    name: Input 2
    mode: input
    active: high
  '16':
    name: Input 1
    mode: input
    active: high
  '18':
    name: Input 3
    mode: input
    active: high
  '22':
    name: Input 4
    mode: input
    active: high
  '31':
    name: Output 1
    mode: output
    active: high
  '32':
    name: Output 2
    mode: output
    active: high
  '33':
    name: Output 3
    mode: output
    active: high
  '35':
    name: Motor 1 +
    mode: output
    active: high
  '36':
    name: Output 4
    mode: output
    active: high
  '37':
    name: Motor 2 -
    mode: output
    active: high
  '38':
    name: Motor 1 -
    mode: output
    active: high
  '40':
    name: Motor 2 +
    mode: output
    active: high
i2c:
  '0x48':
    name: Analog Input
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
#Explorer pHAT

Entradas y salidas de 5V, entradas analógicas y un controlador de motores H-Bridge forman el Explorer pHAT; un complemento de prototipado multifuncional para Raspberry Pi. Perfecto para RPi Zero pero también funciona con A+/B+/2.

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS get.pimoroni.com/explorerhat | bash
```

Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import explorerhat
```
