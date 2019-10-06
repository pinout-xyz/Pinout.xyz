<!--
---
name: OnOff SHIM
class: board
type: power
formfactor: Custom
manufacturer: Pimoroni
description: A power switch for the Raspberry Pi
url: https://shop.pimoroni.com/products/onoff-shim
buy: https://shop.pimoroni.com/products/onoff-shim
image: 'onoff-shim.png'
pincount: 12
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
pin:
  '7':
    name: Shutdown
    mode: output
    active: low
  '11':
    name: Power Button
    mode: input
    active: low
-->
# OnOff SHIM

The OnOff SHIM is a convenient power switch for the Raspberry Pi. Designed to be soldered straight onto the GPIO pins of your Pi, you can use it alongside HATs and pHATs while retaining a very compact setup.

To setup the daemon responsible to initiate the clean shutdown, simply run:

```bash
curl https://get.pimoroni.com/onoffshim | bash
```

Features:

* 1mm thick PCB
* can be soldered right onto the Pi header
* corner-mounted push button for on/off
* micro-B connector for power supply
* red status LED
* optional breakout pins to connect an external momentary button
