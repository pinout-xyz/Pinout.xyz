<!--
---
name: Grow HAT Mini
class: board
type: multi
formfactor: pHAT
manufacturer: Pimoroni
description: Plant-monitoring and watering
url: http://shop.pimoroni.com/products/grow
github: https://github.com/pimoroni/grow-python
buy: http://shop.pimoroni.com/products/grow
image: 'pimoroni-grow-hat-mini.png'
pincount: 40
eeprom: no
power:
  '2':
  '17':
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
  '16':
    name: Moisture 1
  '24':
    name: Moisture 2
  '22':
    name: Moisture 3
  '7':
    name: Moisture Int
  '11':
    name: Pump 1
  '13':
    name: Pump 2
  '15':
    name: Pump 3
  '33':
    name: Piezo
  '26':
    mode: SPI
    name: Chip-select
  '32':
    name: Backlight
  '21':
    name: Data/Command
  '19':
    mode: SPI
  '23':
    mode: SPI
  '29':
    name: Button A
  '31':
    name: Button B
  '36':
    name: Button X
  '18':
    name: Button Y
i2c:
  0x23:
    device: LTR559
-->
# Grow HAT Mini

A compact Raspberry Pi powered monitoring system designed to help you take the best possible care of your plants. It will tell you how well they're hydrated, attract your attention when they need water and, if you want to go a step further, even give them water!

To get Grow HAT Mini set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/grow | bash
```
