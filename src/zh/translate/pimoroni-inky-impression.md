<!--
---
name: Inky Impression
class: board
type: display
formfactor: custom
manufacturer: Pimoroni
description: A 7-colour e-paper display for your Raspberry Pi
url: https://shop.pimoroni.com/products/inky-impression
github: https://github.com/pimoroni/inky
buy: https://shop.pimoroni.com/products/inky-impression
image: 'pimoroni-inky-impression.png'
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
  '11':
    name: Busy
    mode: input
  '13':
    name: Reset
    mode: output
    active: low
  '15':
    name: Data/Command
    mode: output
    active: high
  '19':
    mode: spi
  '23':
    mode: spi
  '24':
    name: Chip Select
    mode: chipselect
    active: high
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  0x50:
    device: Inky ID EEPROM
-->
# Inky Impression

Inky Impression is a big, beautiful, 5.7", 600 x 448 pixel 7 colour electronic paper (ePaper / eInk / EPD) display for Raspberry Pi.

The unit comes fully-assembled, with the display securely stuck down to the Inky Impression PCB and connected via a ribbon cable. Inky Impression is compatible with all 40-way Raspberry Pis.

To get Inky Impression up and running, you can use the one-line product installer:

```bash
curl https://get.pimoroni.com/inky | bash
```

And follow the instructions!
