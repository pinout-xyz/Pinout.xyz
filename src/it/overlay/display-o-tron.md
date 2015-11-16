<!--
---
name: Display-o-Tron 3000
manufacturer: Pimoroni
github: https://github.com/pimoroni/dot3k
url: https://github.com/pimoroni/dot3k
description: Un LCD da 3 righe di caratteri, RGB retroilluminato e un joystick
install:
  'devices':
    - 'i2c'
    - 'spi'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'dot3k'
  'examples': 'python/examples/'
pincount: 40
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
