<!--
---
type: board
name: Explorer pHAT
manufacturer: Pimoroni
description: An all-in-one input, output and motor add-on board.
url: https://github.com/pimoroni/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: https://shop.pimoroni.com/products/explorer-phat
formfactor: 'pHAT'
pincount: 40
eeprom: no
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
  'examples': 'examples/'
-->
#Explorer pHAT

5V inputs and outputs, analog inputs and an H-Bridge motor driver make up the Explorer pHAT; a jack of all trades prototyping side-kick for your Raspberry Pi. Perfect for RPi Zero but works with A+/B+/2 too!

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/explorerhat | bash
```

Then import it into your Python script and start tinkering:

```bash
import explorerhat
```
