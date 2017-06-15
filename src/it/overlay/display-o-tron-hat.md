<!--
---
name: Display-o-Tron HAT
class: board
type: Tutti
formfactor: HAT
manufacturer: Pimoroni
description: Un LCD da 3 righe di caratteri, RGB retroilluminato a 6 zone con 6 bottoni touch
url: https://shop.pimoroni.com/products/display-o-tron-hat
github: https://github.com/pimoroni/displayotron
buy: https://shop.pimoroni.com/products/display-o-tron-hat
image: 'display-o-tron-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '19':
    mode: spi
  '22':
    name: LCD Register Select
    mode: output
  '23':
    mode: spi
  '24':
    name: LCD Chip Select
    mode: chipselect
    active: high
  '32':
    name: LCD Reset
    mode: output
    active: low
-->
#Display-o-Tron HAT

Il Display-o-Tron HAT usa sia l'SPI che l'I2c per controllare il display LCD, la retroilluminazione e il touchscreen. 
Entrambi questi bus possono essere comunque condivisi con altre periferiche.

Per preparare e impostare l'HAT puoi utilizzare l'installer fornito:

```bash
curl -sS https://get.pimoroni.com/dot3k | bash
```

&hellip;e seguire le istruzioni!
