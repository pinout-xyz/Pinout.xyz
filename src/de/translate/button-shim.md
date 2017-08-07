<!--
---
name: Button SHIM
class: board
type: io
formfactor: Custom
manufacturer: Pimoroni
description: 5 tacile switches and one RGB LED for the Raspberry Pi
url: https://shop.pimoroni.com/products/button-shim
buy: https://shop.pimoroni.com/products/button-shim
image: 'button-shim.png'
pincount: 40
eeprom: no
power:
  '4':
  '17':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
-->
# Button SHIM

Button SHIM is designed to add 5 tactile push buttons and a single RGB indicator LED to your Raspberry Pi project. Designed to be soldered right onto the GPIO pins of your Pi, it's great for adding buttons to a project using Scroll pHAT or another display add-on.

To install the library, run the one-line installer like so:

```bash
curl https://get.pimoroni.com/buttonshim | bash
```

Features:

* 5 tactile push buttons
* can be soldered right onto the Pi header
* RGB status LED
