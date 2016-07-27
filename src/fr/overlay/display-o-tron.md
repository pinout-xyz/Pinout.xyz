<!--
---
name: Display-o-Tron 3000
class: board
type: Tous
formfactor: Autre
manufacturer: Pimoroni
image: 'image.png'
github: https://github.com/pimoroni/dot3k
url: https://github.com/pimoroni/dot3k
description: Un écran LCD 3 lignes avec rétro-éclairage et joystick
install:
  'devices':
    - 'i2c'
    - 'spi'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'dot3k'
  'examples': 'python/examples/'
pincount: 26
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
#Display-o-Tron 3000

Le Display-o-Tron 3000 est un écran LCD avec 3 lignes, rétro-éclairage et joystick

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS get.pimoroni.com/dot3k | bash
```