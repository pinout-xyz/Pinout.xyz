<!--
---
name: Display-o-Tron 3000
class: board
type: lcd
formfactor: Autre
manufacturer: Pimoroni
description: Un écran LCD 3 lignes avec rétro-éclairage et joystick
url: https://shop.pimoroni.com/products/displayotron-3000
github: https://github.com/pimoroni/dot3k
buy: https://shop.pimoroni.com/products/displayotron-3000
image: 'display-o-tron.png'
pincount: 26
eeprom: no
power:
  '2':
  '17':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: bouton Joystick
    mode: input
    active: low
  '11':
    name: Joystick gauche
    mode: input
    active: low
  '13':
    name: Joystick haut
    mode: input
    active: low
  '15':
    name: Joystick droit
    mode: input
    active: low
  '19':
    mode: spi
  '21':
    name: Joystick bas
    mode: input
    active: low
  '22':
    name: Données/Commandes LCD
    mode: output
    active: high
  '23':
    mode: spi
-->
# Display-o-Tron 3000

Le Display-o-Tron 3000 est un écran LCD avec 3 lignes, rétro-éclairage et joystick

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS https://get.pimoroni.com/dot3k | bash
```
