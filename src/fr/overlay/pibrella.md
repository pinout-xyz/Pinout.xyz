<!--
---
description: carte multi-usage avec son, lumière, entrées et sorties
pin:
  '7':
    name: LED verte
  '11':
    name: LED jaune
  '12':
    name: buzzer piezo
  '13':
    name: LED rouge
  '15':
    name: sortie E
  '16':
    name: sortie F
  '18':
    name: sortie G
  '19':
    name: entrée D
  '21':
    name: entrée A
  '22':
    name: sortie H
  '23':
    name: bouton
  '24':
    name: entrée C
  '26':
    name: entrée B
-->
# Pibrella

La Pibrella est une carte à usage multiple avec son, lumière, entrées et sorties. Elle monopolise un nombre élevé de broches GPIO tout en laissant cependant les bus série, SPI et i2c libres.

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS https://get.pimoroni.com/pibrella | bash
```

Puis, sous Python, en guise de test que tout fonctionne bien:

```bash
import pibrella
pibrella.light.red.on()
```
