<!--
---
name: Touch pHAT
class: board
type: touch
formfactor: pHAT
manufacturer: Pimoroni
description: A 6 capacitive touch pads add-on for your Raspberry Pi
url: http://shop.pimoroni.com/products/touch-phat
github: https://github.com/pimoroni/touch-phat
buy: http://shop.pimoroni.com/products/touch-phat
image: 'touch-phat.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x2c':
    name: Cap Touch
    device: cap1166
-->
#Touch HAT

Touch pHAT has six capacitive touch buttons, each with a bright white LED, designed to be completely agnostic about what they're used for. You can even use a dry erase pen to write on the pads to label their function.

It uses the CAP1166 capacitive touch and LED driver chip. The LEDs have been under-mounted and shine through exposed sections of the PCB to give a pleasing yellow-green glow and a completely smooth top surface!

```bash
curl https://get.pimoroni.com/touchphat | bash
```

And follow the instructions!
