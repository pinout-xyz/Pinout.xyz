<!--
---
name: Automation pHAT
class: board
type: adc,io,motor,relay
formfactor: pHAT
manufacturer: Pimoroni
description: An all-in-one home automation and control board
url: http://shop.pimoroni.com/products/automation-phat
github: https://github.com/pimoroni/automation-hat
buy: http://shop.pimoroni.com/products/automation-phat
image: 'automation-phat.png'
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
  '36':
    name: Relay 1
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
# Automation pHAT

Automation pHAT sirva para monitorizar y domotizar el hogar con Raspberry Pi; cuenta con relés, canales analógicos, salidas con alimentación y entradas regulables. Todo capaz de funcionar con 24V.

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS https://get.pimoroni.com/automationhat | bash
```
Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import automationhat
automationhat.relay.one.on()
```
