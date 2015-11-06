<!--
---
name: Pibrella
manufacturer: Pimoroni Vs Cyntech
url: https://github.com/pimoroni/pibrella
description: An all-in-one light, sound, input and output add-on board.
pincount: 26
pin:
  '7':
    name: Green LED
    direction: output
    active: high
  '11':
    name: Yellow LED
    direction: output
    active: high
  '12':
    name: Buzzer
    direction: output
    active: high
  '13':
    name: Red LED
    direction: output
    active: high
  '15':
    name: Output A
    direction: output
    active: high
  '16':
    name: Output B
    direction: output
    active: high
  '18':
    name: Output C
    direction: output
    active: high
  '19':
    name: Input D
    direction: output
    active: high
  '21':
    name: Input A
    direction: input
    active: high
  '22':
    name: Output D
    direction: output
    active: high
  '23':
    name: Button
    direction: input
    active: high
  '24':
    name: Input C
    direction: input
    active: high
  '26':
    name: Input B
    direction: input
    active: high
-->
#Pibrella

The all-in-one light, sound, input and output add-on board from Pimoroni vs Cyntech uses lots of IO on the Pi but leaves both Serial and I2C free leaving plenty of room for expansion if you get creative.

Pibrella is easy to use, first you should install the module using LXTerminal/Command Line:

```bash
sudo apt-get install python-pip
sudo pip install pibrella
```

Then import it into your Python script and start tinkering:

```bash
import pibrella
pibrella.light.red.on()
```