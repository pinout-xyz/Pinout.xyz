<!--
---
name: Automation HAT
class: board
type: adc,io,motor
formfactor: HAT
manufacturer: Pimoroni
description: An all-in-one home automation and control board
url: http://shop.pimoroni.com/products/automation-hat
github: https://github.com/pimoroni/automation-hat
buy: http://shop.pimoroni.com/products/automation-hat
image: 'automation-hat.png'
pincount: 40
eeprom: yes
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
  '29':
    name: Output 1
    mode: output
    active: high
  '31':
    name: Output 3
    mode: output
    active: high
  '32':
    name: Output 2
    mode: output
    active: high
  '33':
    name: Relay 1
    mode: output
    active: high
  '35':
    name: Relay 2
    mode: output
    active: high
  '36':
    name: Relay 3
    mode: output
    active: high
  '37':
    name: Input 1
    mode: input
    active: high
  '38':
    name: Input 2
    mode: input
    active: high
  '40':
    name: Input 3
    mode: input
    active: high
i2c:
  '0x54':
    name: LED Driver
    device: sn3218
  '0x48':
    name: Analog Input
    device: ads1015
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
  'python':
    - 'automationhat'
  'python3':
    - 'automationhat'
-->
#Automation HAT

Automatian HAT es una placa adicional de domótica para Raspberry Pi; con relés, canales analógicos, salidas alimentadas y entradas regulables. Todos con tolerancia hasta 24V.

Para configurar el HAT puedes utilizar el instalador online de una línea.

```bash
curl -sS https://get.pimoroni.com/automationhat | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import automationhat
automationhat.relay.one.on()
```
