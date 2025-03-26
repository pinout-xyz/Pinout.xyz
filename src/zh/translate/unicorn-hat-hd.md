<!--
---
name: Unicorn HAT HD
class: board
type: display
formfactor: HAT
manufacturer: Pimoroni
description: A matrix of 256 RGB LED pixels for the Raspberry Pi
url: https://shop.pimoroni.com/products/unicorn-hat-hd
github: https://github.com/pimoroni/unicorn-hat-hd
buy: https://shop.pimoroni.com/products/unicorn-hat-hd
image: 'unicorn-hat-hd.png'
pincount: 40
eeprom: yes
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
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    name: Chip Select
    mode: chipselect
    active: high
-->
# Unicorn HAT HD

Unicorn HAT HD provides a matrix of 256 RGB LED pixels. It's ideal for writing messages, showing graphs, and drawing pictures.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/unicornhathd | bash
```

And follow the instructions!
