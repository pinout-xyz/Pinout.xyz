<!--
---
name: Speaker pHAT
class: board
type: audio
formfactor: pHAT
manufacturer: Pimoroni
description: An I2S digital speaker and VU meter
buy: https://shop.pimoroni.com/products/speaker-phat
image: 'speaker-phat.png'
pincount: 40
eeprom: no
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
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
install:
  'devices':
  - 'i2s'
  - 'i2c'
i2c:
  '0x54':
    name: LED driver
    device: sn3218
-->
#Speaker pHAT

Speaker pHAT cuenta con I2S DAC, amplificador mono, un pequeño altavoz de 8Ω y 2W además de unas barras de 10 LED, todo en una placa del mismo tamaño que una Pi Zero.

Pese a ser diseñado para ser utilizado con Raspberry Pi Zero, es compatible con todas las Raspberry Pi de 40 pines GPIO (2/3/B+/A+/Zero)

Para poner el pHAT en funcionamiento, puedes utilizar nuestro instalador de una línea.

```bash
curl -sS https://get.pimoroni.com/speakerphat | bash
```
