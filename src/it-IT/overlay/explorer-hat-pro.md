<!--
---
name: Explorer HAT Pro
manufacturer: Pimoroni
url: https://github.com/pimoroni/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
description: All-in-one luce, input, motore, touch e add-on output board.
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
    name: Touch capacitivo
    device: cap1208
  '0x48':
    name: Input analogico
    device: ads1015
pin:
  '3': {}
  '5': {}
  '7':
    name: LED 1
    mode: output
    active: high
  '8': {}
  '10': {}
  '11':
    name: LED 2
    mode: output
    active: high
  '12': {}
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
  '19': {}
  '21': {}
  '22':
    name: Input 4
    mode: input
    active: high
  '23': {}
  '24': {}
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
-->
#Explorer HAT Pro

Input ed output a 5V, touch pad, LED, input analogici e un motore H-Bridge sono le caratteristiche dell'Explorer HAT Pro- un asso nella manica per il tuo Raspberry Pi.

Per preparare e impostare il modulo puoi utilizzare l'installer fornito:

```bash
curl -sS get.pimoroni.com/explorerhat
```

Importalo poi nel tuo script Python e inizia a smanettare:

```bash
import explorerhat
explorerhat.light.on()
```
