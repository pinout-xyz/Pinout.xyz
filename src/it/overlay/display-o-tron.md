<!--
---
name: Display-o-Tron 3000
class: board
type: Tutti
formfactor: Altro
manufacturer: Pimoroni
description: Un LCD da 3 righe di caratteri, RGB retroilluminato e un joystick
url: https://shop.pimoroni.com/products/displayotron-3000
github: https://github.com/pimoroni/dot3k
buy: https://shop.pimoroni.com/products/displayotron-3000
image: 'display-o-tron.png'
pincount: 26
eeprom: no
power:
  '2':
  '17':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Bottone joystick
    mode: input
    active: low
  '11':
    name: Joystick sinistra
    mode: input
    active: low
  '13':
    name: Joystick su
    mode: input
    active: low
  '15':
    name: Joystick destra
    mode: input
    active: low
  '19':
    mode: spi
  '21':
    name: Joystick giù
    mode: input
    active: low
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '23':
    mode: spi
-->
#Display-o-Tron 3000

Il Display-o-Tron 3000 è un LCD da 3 righe di caratteri retroilluminato RGB e con un joystick.

Per preparare e impostare il modulo puoi utilizzare l'installer fornito:

```bash
curl -sS get.pimoroni.com/dot3k | bash
```

&hellip;e seguire le istruzioni!
