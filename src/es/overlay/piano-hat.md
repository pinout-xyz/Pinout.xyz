<!--
---
name: Piano HAT
class: board
type: cap
formfactor: HAT
manufacturer: Pimoroni
description: Un mini Pi piano con 16 botones capacitivos
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
    name: Alerta A
    mode: entrada
  '11':
    name: Reset A
    mode: salida
  '13':
    name: Alerta B
    mode: entrada
  '15':
    name: Reset B
    mode: salida
i2c:
  '0x28':
    name: Cap Touch A
    device: cap1188
  '0x2b':
    name: Cap Touch B
    device: cap1188
-->
#Piano HAT

El Piano HAT tiene 16 botones capacitivos. 13 de estos se usan para una octava, y el resto para subir/bajar la octava y el selector de instrumento.

Usa dos CAP1188 chips de Microchip, con las direcciones i2c 0x28 y 0x2b

Puedes usar la siguiente línea para instalar y preparar el Piano HAT:

```bash
curl -sS get.pimoroni.com/pianohat | bash
```

¡Y sigue las instrucciones!
