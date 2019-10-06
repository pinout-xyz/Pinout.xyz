<!--
---
name: Piano HAT
class: board
type: instrument,touch
formfactor: HAT
manufacturer: Pimoroni
description: Ein kleines Pi Piano mit 16 berührungsempfindlichen Tasten
url: https://shop.pimoroni.com/products/piano-hat
github: https://github.com/pimoroni/piano-hat
buy: https://shop.pimoroni.com/products/piano-hat
image: 'piano-hat.png'
pincount: 40
eeprom: yes
pin:
  3:
    mode: i2c
  5:
    mode: i2c
  7:
    name: Alert A
    mode: input
  11:
    name: Reset A
    mode: output
  13:
    name: Alert B
    mode: input
  15:
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

Piano HAT hat 16 berührungsempfindliche Tasten. 13 dieser Tasten bilden eine Piano-Oktave, die anderen lassen die die Oktave hoch oder runter schalten und Instrumente auswählen.

Der HAT benutzt zwei Microchip CAP1188 ICs mit den I2C Adressen 0x28 und 0x2b.

Mit folgendem Einzeiler installierst Du die nötige Software:

```bash
curl -sS https://get.pimoroni.com/pianohat | bash
```

Den Rest findest Du in der Anleitung!
