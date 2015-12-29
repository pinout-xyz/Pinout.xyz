<!--
---
type: board
name: PiGlow
manufacturer: Pimoroni
description: Simply 18 LEDs in a spiral pattern controllable in Python.
url: https://github.com/pimoroni/piglow
github: https://github.com/pimoroni/piglow
buy: http://shop.pimoroni.com/products/piglow
formfactor: '26-way'
pincount: 26
eeprom: no
power: 3v3,5v
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
-->
#PiGlow

The PiGlow is a small add-on board for the Raspberry Pi that provides 18 individually controllable LEDs.

The board uses the SN3218 8-bit 18-channel PWM chip to drive surface mount LEDs. Communication is done via I2C over the GPIO header with a bus address of 0x54. Each LED can be set to a PWM value of between 0 and 255.

To get the module set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/piglow | bash
```

And follow the instructions!
