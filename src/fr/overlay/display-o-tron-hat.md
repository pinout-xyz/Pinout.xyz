<!--
---
name: Display-o-Tron HAT
class: board
type: lcd
formfactor: HAT
manufacturer: Pimoroni
description: Un LCD 3x16 avec rétro-éclairage sur 6 zones RGB et buttons tactiles
url: https://shop.pimoroni.com/products/display-o-tron-hat
github: https://github.com/pimoroni/displayotron
buy: https://shop.pimoroni.com/products/display-o-tron-hat
image: 'display-o-tron-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '19':
    mode: spi
  '22':
    name: Selection Registre LCD
    mode: output
  '23':
    mode: spi
  '24':
    name: Selection Puce LCD
    mode: chipselect
    active: high
  '32':
    name: Reset LCD
    mode: output
    active: low
-->
# Display-o-Tron HAT

Le chapeau Display-o-Tron est un LCD 3x16 caractères avec rétro-éclairage sur 6 zones RGB et buttons tactiles. Il communique avec la Raspberry Pi par l'intermédiaire des bus SPI et I2C.

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS https://get.pimoroni.com/dot3k | bash
```
