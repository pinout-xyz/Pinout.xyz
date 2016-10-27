<!--
---
name: Explorer HAT
class: board
type: cap.,e/s,multi
formfactor: HAT
manufacturer: Pimoroni
description: Un chapeau multi-usage avec entrées et sorties 5V
url: http://shop.pimoroni.com/products/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
image: 'explorer-hat.png'
pincount: 40
eeprom: yes
pin:
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
  '36':
    name: Sortie 4
    mode: output
    active: high
i2c:
  '0x28':
    name: Capteur tactile
    device: cap1208
-->
#Explorer HAT

L'Explorer HAT est un chapeau multi-usage avec entrées et sorties en 5V, LED et touches tactiles. Une extension utile pour tout prototype!

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS get.pimoroni.com/explorerhat | bash
```

Puis, sous Python, en guise de test que tout fonctionne bien:

```bash
import explorerhat
explorerhat.light.on()
```
