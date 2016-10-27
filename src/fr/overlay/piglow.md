<!--
---
name: PiGlow
class: board
type: led
formfactor: Autre
manufacturer: Pimoroni
description: une spirale de LED contrôlable depuis Python.
url: http://shop.pimoroni.com/products/piglow
github: https://github.com/pimoroni/piglow
buy: http://shop.pimoroni.com/products/piglow
image: 'piglow.png'
pincount: 26
eeprom: no
power:
  '1':
  '2':
  '17':
ground:
  '14':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
-->
#PiGlow

La Piglow est une carte petit format pour la Raspberry Pi composée de 18 LEDs contrôlables individuellement.

Le circuit intégré responsable de la gestion des LEDs est le SN3218, un microchip PWM 8-bit à 18 canaux. Il communique avec la Raspi par le bus I2C, à l'adresse 0x54 plus précisément. Les LEDs peuvent se voir attribuer une valeur comprise entre 0 et 255.

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS get.pimoroni.com/piglow | bash
```
