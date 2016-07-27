<!--
---
name: Piano HAT
class: board
type: Tutti
formfactor: HAT
manufacturer: Pimoroni
image: 'image.png'
url: https://github.com/pimoroni/piano-hat
description: Un piccolo Pi-piano con 16 tasti touch
pincount: 40
i2c:
  '0x28':
    name: Touch capacitivo A
    device: cap1188
    datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
  '0x2b':
    name: Touch capacitivo B
    device: cap1188
    datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Allarme A
    mode: input
  '11':
    name: Reset A
    mode: output
  '13':
    name: Allarme B
    mode: input
  '15':
    name: Reset B
    mode: output
-->
#Piano HAT

Il Piano HAT ha 16 tasti touch, 13 di questi sono singole ottave, gli altri ti danno 
le ottave superiori e inferiori e la selezione dello strumento.

Utilizza due Microchip CAP1188 con indirizzi i2c 0x28 e 0x2b.

Per preparare e impostare l'HAT puoi utilizzare l'installer fornito:

```bash
curl -sS get.pimoroni.com/pianohat | bash
```

&hellip;e seguire le istruzioni!
