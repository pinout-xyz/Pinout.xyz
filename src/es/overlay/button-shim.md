<!--
---
name: Button SHIM
class: board
type: io
formfactor: Custom
manufacturer: Pimoroni
description: 5 tacile switches and one RGB LED for the Raspberry Pi
url: https://shop.pimoroni.com/products/button-shim
buy: https://shop.pimoroni.com/products/button-shim
image: 'button-shim.png'
pincount: 40
eeprom: no
power:
  '4':
  '17':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
-->
# Button SHIM

Button SHIM está diseñado para añadir 5 botones táctiles y un indicador LED RGB a tu proyecto con Raspberry Pi. Diseñado para ser soldado encima de los pines GPIO de tu Pi, es genial para añadir botones a un proyecto que use el Scroll pHAT o cualquier otro complemento de visualización.

Para instalar, ejecuta el instalador de una línea:

```bash
curl https://get.pimoroni.com/buttonshim | bash
```

Especificaciones:

* 5 botones táctiles
* Puede ser soldado directamente sobre los pines GPIO de Raspberry Pi
* LED de estado RGB
