<!--
---
name: GPIO Button Adapter
class: board
type: io
formfactor: Custom
manufacturer: Indie
description: A simple way to add input button to your Raspberry Pi
url: http://frederickvandenbosch.be/?p=2462
image: 'vandenbosch-gpio-input.png'
pincount: 40
eeprom: no
ground:
  '6':
pin:
  '29':
    name: Button 1
    mode: input
  '31':
    name: Button 2
    mode: input
  '32':
    name: Button 3
    mode: input
  '33':
    name: Button 4
    mode: input
  '36':
    name: Button 5
    mode: input
  '37':
    name: Button 6
    mode: input
-->
# GPIO Button Adapter

The GPIO Button Adapter by Frederick Vandenbosch is a clean and easy way to add buttons to a Pi Zero alongside a pHAT (or HAT).

When a button is pressed, the GPIO gets connected to ground. The internal pull-up resistors on the Pi should be used so that the GPIO are HIGH when idle, LOW when the button is pressed.

Because the board is only 1mm thick, you can solder the GPIO adapter directly to the Pi header, leaving enough depth on the header pins to properly fit a pHAT on top of it, with good electrical connections.
