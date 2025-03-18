<!--
---
name: Piano HAT
class: board
type: Tutti
formfactor: HAT
manufacturer: Pimoroni
description: Un piccolo Pi-piano con 16 tasti touch
url: https://shop.pimoroni.com/products/piano-hat
github: https://github.com/pimoroni/piano-hat
buy: https://shop.pimoroni.com/products/piano-hat
image: 'piano-hat.png'
pincount: 40
eeprom: yes
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
i2c:
  '0x28':
    name: Touch capacitivo A
    device: cap1188
  '0x2b':
    name: Touch capacitivo B
    device: cap1188
-->
# Piano HAT

Il Piano HAT ha 16 tasti touch, 13 di questi sono singole ottave, gli altri ti danno 
le ottave superiori e inferiori e la selezione dello strumento.

Utilizza due Microchip CAP1188 con indirizzi i2c 0x28 e 0x2b.

Per preparare e impostare l'HAT puoi utilizzare l'installer fornito:

```bash
curl -sS https://get.pimoroni.com/pianohat | bash
```

&hellip;e seguire le istruzioni!
