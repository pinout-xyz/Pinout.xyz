<!--
---
name: Explorer HAT Pro
class: board
type: adc,io,motor,multi,touch
formfactor: HAT
manufacturer: Pimoroni
description: All-in-one luce, input, motore, touch e add-on output board.
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
  '29':
    name: LED 4
    mode: output
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
    name: Motore 2 -
    mode: output
    active: high
  '38':
    name: Motore 1 -
    mode: output
    active: high
  '40':
    name: Motore 2 +
    mode: output
    active: high
i2c:
  '0x28':
    name: Touch capacitivo
    device: cap1208
  '0x48':
    name: Input analogico
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

Input ed output a 5V, touch pad, LED, input analogici e un motore H-Bridge sono le caratteristiche dell'Explorer HAT Pro--un asso nella manica per il tuo Raspberry Pi.

Per preparare e impostare il modulo puoi utilizzare l'installer fornito:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Importalo poi nel tuo script Python e inizia a smanettare:

```bash
import explorerhat
explorerhat.light.on()
```
