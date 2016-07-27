<!--
---
name: Piano HAT
class: board
type: Tous
formfactor: HAT
manufacturer: Pimoroni
image: 'image.png'
url: https://github.com/pimoroni/piano-hat
description: Un mini-piano avec 16 touches tactiles
pincount: 40
i2c:
  '0x28':
    name: Capteur tactile A
    device: cap1188
    datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
  '0x2b':
    name: Capteur tactile B
    device: cap1188
    datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Alerte A
    mode: input
  '11':
    name: Reset A
    mode: output
  '13':
    name: Alerte B
    mode: input
  '15':
    name: Reset B
    mode: output
-->
#Piano HAT

Le Piano HAT est un mini-piano pour la RasPi muni de 16 touches tactiles. 13 d'entre elles forment le clavier en lui-même, s'étendant sur une octave. Les autres quant à elles servent à déplacer l'octave vers le haut ou le bas, ainsi que la sélection d'instrument.

Les microchips responsables de la gestion des touches tactiles sont deux CAP1188, communiquant par l'interface i2c, aux adresses 0x28 et 0x2b.

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS get.pimoroni.com/pianohat | bash
```
