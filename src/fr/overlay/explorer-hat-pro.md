<!--
---
name: Explorer HAT Pro
class: board
type: a/n,cap.,e/s,moteur
formfactor: HAT
manufacturer: Pimoroni
description: Un chapeau multi-usage avec entrées analogiques et contrôle moteurs
url: http://shop.pimoroni.com/products/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
image: 'explorer-hat-pro.png'
pincount: 40
eeprom: yes
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: LED 1
    mode: output
    active: high
  '11':
    name: LED 2
    mode: output
    active: high
  '13':
    name: LED 3
    mode: output
    active: high
  '15':
    name: Entrée 2
    mode: input
    active: high
  '16':
    name: Entrée 1
    mode: input
    active: high
  '18':
    name: Entrée 3
    mode: input
    active: high
  '22':
    name: Entrée 4
    mode: input
    active: high
  '29':
    name: LED 4
    mode: output
    active: high
  '31':
    name: Sortie 1
    mode: output
    active: high
  '32':
    name: Sortie 2
    mode: output
    active: high
  '33':
    name: Sortie 3
    mode: output
    active: high
  '35':
    name: Moteur 1 +
    mode: output
    active: high
  '36':
    name: Sortie 4
    mode: output
    active: high
  '37':
    name: Moteur 2 -
    mode: output
    active: high
  '38':
    name: Moteur 1 -
    mode: output
    active: high
  '40':
    name: Moteur 2 +
    mode: output
    active: high
i2c:
  '0x28':
    name: Capteur tactile
    device: cap1208
  '0x48':
    name: Entrées analogiques
    device: ads1015
-->
#Explorer HAT Pro

L'Explorer HAT pro est un chapeau à usage multiple avec entrées et sorties en 5V, entrées analogiques et contrôle moteurs. Tout cela agrémenté de LED et touches tactiles. C'est donc d'un véritable couteau Suisse dont il s'agit!

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS get.pimoroni.com/explorerhat | bash
```

Puis, sous Python, en guise de test que tout fonctionne bien:

```bash
import explorerhat
explorerhat.light.on()
```
