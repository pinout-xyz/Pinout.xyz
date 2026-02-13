<!--
---
name: Inky pHAT
class: board
type: display
formfactor: pHAT
manufacturer: Pimoroni
description: An e-paper display for your Raspberry Pi
url: https://shop.pimoroni.com/products/inky-phat
github: https://github.com/pimoroni/inky
buy: https://shop.pimoroni.com/products/inky-phat
image: 'inkyphat.png'
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
# Inky pHAT

Inky pHAT is a low-energy, red/black, red/black/white or yellow/black/white electronic paper display for the Raspberry Pi. Multi-colour EPD displays, like the one on Inky pHAT, use ingenious electrophoresis to pull coloured particles up and down on the display. The coloured particles reflect light, unlike most display types, so they're visible under bright lights.

The unit comes fully-assembled, with the display securely stuck down to the Inky pHAT PCB and connected via a ribbon cable. The Inky pHAT is compatible with all 40-way Raspberry Pis.

To get the pHAT up and running, you can use the one-line product installer:

```bash
curl https://get.pimoroni.com/inky | bash
```

And follow the instructions!

Note: For the old first edition Inky pHAT you should use:

```bash
curl https://get.pimoroni.com/inkyphat | bash
```
