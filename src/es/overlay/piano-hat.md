<!--
---
name: Piano HAT
manufacturer: Pimoroni
url: https://github.com/pimoroni/piano-hat
description: Un mini Pi piano con 16 botones capacitivos
pincount: 40
i2c:
  '0x28':
    name: Cap Touch A
    device: cap1188
    datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
  '0x2b':
    name: Cap Touch B
    device: cap1188
    datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
pin:
  3:
    mode: i2c
  5:
    mode: i2c
  7:
    name: Alerta A
    mode: entrada
  11:
    name: Reset A
    mode: salida
  13:
    name: Alerta B
    mode: entrada
  15:
    name: Reset B
    mode: salida
-->
#Piano HAT

El Piano HAT tiene 16 botones capacitivos. 13 de estos se usan para una octava, y el resto para subir/bajar la octava y el selector de instrumento.

Usa dos CAP1188 chips de Microchip, con las direcciones i2c 0x28 y 0x2b

Puedes usar la siguiente línea para instalar y preparar el Piano HAT:

```bash
curl -sS get.pimoroni.com/pianohat | bash
```

¡Y sigue las instrucciones!
