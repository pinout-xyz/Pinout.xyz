<!--
---
name: Explorer HAT
description: An all-in-one light, input, touch and output add-on board.
pincount: 40
pin:
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
  '36':
    name: Output 4
    mode: output
    active: high
-->
#Explorer HAT and Explorer HAT Pro

5V inputs and outputs, touch pads, LEDs, analog inputs and an H-Bridge motor driver make up the Explorer HAT Pro- a jack of all trades prototyping side-kick for your Raspberry Pi.

```bash
sudo apt-get install python-pip
sudo pip install explorer-hat
```

Then import it into your Python script and start tinkering:

```bash
import explorerhat
explorerhat.light.on()
```
