<!--
---
name: Four Letter pHAT
class: board
type: display
formfactor: pHAT
manufacturer: Pimoroni
description: A four 14-segment displays for the Raspberry Pi
url: https://shop.pimoroni.com/products/four-letter-phat
github: https://github.com/pimoroni/fourletter-phat
buy: https://shop.pimoroni.com/products/four-letter-phat
image: 'fourletter-phat.png'
pincount: 40
eeprom: yes
power:
  '2':
  '17':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x70':
    name: Matrix Driver
    device: HT16K33
-->
# Four Letter pHAT

For Letter pHAT es una pantalla formada por 4 módulos de 14 segmentos que se puede utilizar para mostrar texto, números y otros caracteres. Sus matrices son de estilo retro vede, similares a la de los viejos despertadores digitales y son controladas por el chip HT16K33 vía I2C.

Especificaciones:

* Cuatro matrices de 14 segmentos
* Chip controlador HT16K33
* Compatible con Raspberry Pi A+/B+, 2, 3 y Zero/Zero W

Para configurar el pHAT y dejarlo listo para su funcionamiento puedes utilizar el instalador de una línea:

```bash
curl https://get.pimoroni.com/fourletterphat | bash
```
