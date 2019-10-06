<!--
---
name: Hyperpixel4
class: board
type: display
formfactor: Custom
manufacturer: Pimoroni
description: An 800x480 pixel 60FPS 4" TFT display for the Raspberry Pi
url: https://shop.pimoroni.com/products/hyperpixel
github: https://github.com/pimoroni/hyperpixel4
buy: https://shop.pimoroni.com/products/hyperpixel
image: 'hyperpixel4.png'
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
  'bcm0':
    name: DPI Clock
  'bcm1':
    name: DPI EN
  'bcm2':
    name: DPI V-Sync
  'bcm3':
    name: DPI H-Sync
  'bcm4':
    name: Blue 2
  'bcm5':
    name: Blue 3
  'bcm6':
    name: Blue 4
  'bcm7':
    name: Blue 5
  'bcm8':
    name: Blue 6
  'bcm9':
    name: Blue 7
  'bcm12':
    name: Green 2
  'bcm13':
    name: Green 3
  'bcm14':
    name: Green 4
  'bcm15':
    name: Green 5
  'bcm16':
    name: Green 6
  'bcm17':
    name: Green 7
  'bcm20':
    name: Red 2
  'bcm21':
    name: Red 3
  'bcm22':
    name: Red 4
  'bcm23':
    name: Red 5
  'bcm24':
    name: Red 6
  'bcm25':
    name: Red 7
  'bcm10':
    name: Touch Data
    mode: i2c
  'bcm11':
    name: Touch Clock
    mode: i2c
  'bcm18':
    name: LCD Chip Select
    mode: output
  'bcm19':
    name: Backlight Control
    mode: output
  'bcm26':
    name: LCD Program Data
    mode: output
  'bcm27':
    name: Touch Interrupt
    mode: output
-->
# HyperPixel 4

HyperPixel 4 is a 4" TFT display for the Raspberry Pi. Using a high-speed DPI interface, it boosts a 60 FPS frame rate and a resolution of approximately 270 pixels per inch (800x480).

The display is capable of displaying 18-bits of colour (6 bits per colour, DPI mode 6 - RGB666), and provides capacitive multi-touch capabilities, more sensitive and responsive to touch than a resistive touch display.

HyperPixel 4 is compatible with any 40-pin version of the Pi, including Pi Zero and Pi Zero W.

HyperPixel 4 is larger than a standard HAT to accomodate the
display and will overhang both the USB ports and over the
other end of the Pi. It requires an extension header (supplied)
to connect.

Because HyperPixel 4 uses every Raspberry Pi pin it's difficult
to use it in conjunction with other devices, but it does break
out the software I2C bus (i2c 3) which you can share with the
touchscreen controller.

To get the display set up, you can use the one-line product installer:

```bash
curl https://get.pimoroni.com/hyperpixel4 | bash
```

And follow the instructions!
