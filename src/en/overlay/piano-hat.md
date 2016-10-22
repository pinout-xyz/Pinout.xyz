<!--
---
name: Piano HAT
class: board
type: instrument,touch
formfactor: HAT
manufacturer: Pimoroni
description: A tiny Pi piano with 16 touch-sensitive buttons
url: https://shop.pimoroni.com/products/piano-hat
github: https://github.com/pimoroni/piano-hat
buy: https://shop.pimoroni.com/products/piano-hat
image: 'piano-hat.png'
pincount: 40
eeprom: yes
power:
  '2':
  '17':
ground:
  '9':
  '30':
  '34':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Alert A
    mode: input
  '11':
    name: Reset A
    mode: output
  '13':
    name: Alert B
    mode: input
  '15':
    name: Reset B
    mode: output
i2c:
  '0x28':
    name: Cap Touch A
    device: cap1188
  '0x2b':
    name: Cap Touch B
    device: cap1188
-->
#Piano HAT

Piano HAT has 16 touch-sensitive buttons. 13 of these are a single Piano octave, the rest give you octave up/down and instrument select functionality.

It uses two Microchip CAP1188 chips with the i2c addresses 0x28 and 0x2b.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/pianohat | bash
```

And follow the instructions!
