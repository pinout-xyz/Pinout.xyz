<!--
---
name: Pibrella
class: board
type: e/s,multi
formfactor: Autre
manufacturer: Cyntech
description: carte multi-usage avec son, lumière, entrées et sorties
url: http://pibrella.com
github: https://github.com/pimoroni/pibrella
buy: https://shop.cyntech.co.uk/products/pibrella?variant=581387897
image: 'pibrella.png'
pincount: 26
eeprom: no
pin:
  '7':
    name: LED verte
    direction: output
    active: high
  '11':
    name: LED jaune
    direction: output
    active: high
  '12':
    name: buzzer piezo
    direction: output
    active: high
  '13':
    name: LED rouge
    direction: output
    active: high
  '15':
    name: sortie A
    direction: output
    active: high
  '16':
    name: sortie B
    direction: output
    active: high
  '18':
    name: sortie C
    direction: output
    active: high
  '19':
    name: sortie D
    direction: output
    active: high
  '21':
    name: entrée A
    direction: input
    active: high
  '22':
    name: entrée D
    direction: output
    active: high
  '23':
    name: bouton
    direction: input
    active: high
  '24':
    name: entrée C
    direction: input
    active: high
  '26':
    name: entrée B
    direction: input
    active: high
-->
#Pibrella

La Pibrella est une carte à usage multiple avec son, lumière, entrées et sorties. Elle monopolise un nombre élevé de broches GPIO tout en laissant cependant les bus série, SPI et i2c libres.

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS get.pimoroni.com/pibrella | bash
```

Puis, sous Python, en guise de test que tout fonctionne bien:

```bash
import pibrella
pibrella.light.red.on()
```
