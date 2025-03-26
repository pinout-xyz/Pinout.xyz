<!--
---
name: PiGlow
class: board
type: led
formfactor: Custom
manufacturer: Pimoroni
description: Simply 18 LEDs in a spiral pattern controllable in Python
url: http://shop.pimoroni.com/products/piglow
github: https://github.com/pimoroni/piglow
buy: http://shop.pimoroni.com/products/piglow
image: 'piglow.png'
pincount: 26
eeprom: no
power:
  '1':
  '2':
  '17':
ground:
  '14':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
install:
  'devices':
  - 'i2c'
i2c:
  '0x54':
    name: LED driver
    device: sn3218
-->
# PiGlow

The PiGlow is a small add-on board for the Raspberry Pi that provides 18 individually controllable LEDs.

The board uses the SN3218 8-bit 18-channel PWM chip to drive surface mount LEDs. Communication is done via I2C over the GPIO header with a bus address of 0x54. Each LED can be set to a PWM value of between 0 and 255.

To get the module set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/piglow | bash
```

And follow the instructions!
