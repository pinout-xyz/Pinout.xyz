<!--
---
description: Un mini-piano avec 16 touches tactiles
pin:
  '7':
    name: Alerte A
  '13':
    name: Alerte B
i2c:
  '0x28':
    name: Capteur tactile A
  '0x2b':
    name: Capteur tactile B
-->
# Piano HAT

Le Piano HAT est un mini-piano pour la RasPi muni de 16 touches tactiles. 13 d'entre elles forment le clavier en lui-même, s'étendant sur une octave. Les autres quant à elles servent à déplacer l'octave vers le haut ou le bas, ainsi que la sélection d'instrument.

Les microchips responsables de la gestion des touches tactiles sont deux CAP1188, communiquant par l'interface i2c, aux adresses 0x28 et 0x2b.

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS https://get.pimoroni.com/pianohat | bash
```
