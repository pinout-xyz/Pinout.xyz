<!--
---
name: Breakout Garden HAT
class: board
type: io
formfactor: HAT
manufacturer: Pimoroni
description: Break out your i2c bus to 6 edge connectors.
url: https://shop.pimoroni.com/products/breakout-garden-hat
github: https://github.com/pimoroni/breakout-garden
buy: https://shop.pimoroni.com/products/breakout-garden-hat
image: 'breakout-garden-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
  '17':
ground:
  '9':
  '25':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Interrupt
    mode: input
  '36':
    name: EEPROM WP
    mode: output
    active: low
-->
# Breakout Garden HAT

Breakout Garden HAT breaks out your Pi's i2c (inter-integrated circuit) bus into 6 convenient edge connectors designed to accommodate Pimoroni breakout boards.

This means you can prototype your breakout-based designs with no soldering or connection hassles and write and test your code before assembling your final creation.

The top of Breakout Garden HAT is an unbroken ground plane, so if you're wiring it off your Pi you will only need one ground pin (pick from the ones marked). The 5v line is regulated to 3v3 for the breakouts, and either pin will do. The 3v3 pins are only used for the EEPROM so you can safely omit them.

For easy off-board wiring, or use with something like an Arduino you could use the SDA, SCL, INT, GND and 5V connections on the breakout header.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/breakoutgarden | bash
```

And follow the instructions!
