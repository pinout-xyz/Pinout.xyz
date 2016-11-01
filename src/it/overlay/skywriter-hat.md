<!--
---
name: Skywriter HAT
class: board
type: Tutti
formfactor: HAT
manufacturer: Pimoroni
description: Un sensore 3D posizionale per le dita.
url: http://shop.pimoroni.com/products/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
image: 'skywriter-hat.png'
pincount: 40
eeprom: yes
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: Reset
  '13':
    name: Transfer
i2c:
  '0x42':
    name: Gesture sensor
    device: mgc3130
-->
#Skywriter HAT

Skywriter HAT percepisce la posizione del tuo dito in 3 dimensioni, e restituisce un asse in X, Y, Z
che puoi usare nei tuoi script Python.

È anche in grado di riconoscere gesti, come ad esempio swipe ("scorrimento"), e molti altri.

Per preparare e impostare l'HAT puoi utilizzare l'installer fornito:

```bash
curl -sS get.pimoroni.com/skywriter | bash
```

&hellip;e seguire le istruzioni!
