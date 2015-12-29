<!--
---
type: board
name: Pibrella
manufacturer: Pimoroni Vs Cyntech
description: An all-in-one light, sound, input and output add-on board.
url: https://github.com/pimoroni/pibrella
formfactor: '26-way'
pincount: 26
eeprom: no
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
    name: Output E
    direction: output
    active: high
  '16':
    name: Output F
    direction: output
    active: high
  '18':
    name: Output G
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
    name: Output H
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
curl -sS get.pimoroni.com/pibrella | bash
```

Then import it into your Python script and start tinkering:

```bash
import pibrella
pibrella.light.red.on()
```
