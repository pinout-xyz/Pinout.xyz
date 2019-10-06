<!--
---
name: LED SHIM
class: board
type: display, led
formfactor: Custom
manufacturer: Pimoroni
description: 28 RGB LEDs
url: https://github.com/pimoroni/led-shim
github: https://github.com/pimoroni/led-shim
buy: https://shop.pimoroni.com/products/led-shim
image: 'pimoroni-led-shim.png'
pincount: 40
eeprom: no
power:
  '4':
ground:
  '6':
  '20':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x75':
    name: Matrix LED driver
    device: IS31FL3731
-->
#LED SHIM

LED SHIM packs 28 RGB LEDs into a tiiiinnny SHIM. It uses i2c and a friction-fit header so you can stuff it under most HATs or pHATs to add LED status indicators without any need to solder.

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/ledshim | bash
```

Then import it into your Python script and start tinkering:

```bash
import ledshim
```
