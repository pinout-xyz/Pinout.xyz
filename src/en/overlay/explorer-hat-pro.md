<!--
---
name: Explorer HAT Pro
manufacturer: Pimoroni
url: https://github.com/pimoroni/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
description: An all-in-one light, input, motor, touch and output add-on board.
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
    name: Cap Touch
    device: cap1208
  '0x48':
    name: Analog Input
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
-->
#Explorer HAT Pro

5V inputs and outputs, touch pads, LEDs, analog inputs and an H-Bridge motor driver make up the Explorer HAT Pro- a jack of all trades prototyping side-kick for your Raspberry Pi.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/explorerhat | bash
```

Then import it into your Python script and start tinkering:

```bash
import explorerhat
explorerhat.light.on()
```
