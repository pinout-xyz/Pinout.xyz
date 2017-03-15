<!--
---
name: Picade HAT
class: board
type: io
formfactor: HAT
manufacturer: Pimoroni
description: Arcade inputs & digital amp
buy: https://shop.pimoroni.com/products/picade-hat
github: https://github.com/pimoroni/picade-hat
image: 'picade-hat.png'
pincount: 40
eeprom: setup
power:
  '1':
  '2':
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
  '7':
    name: Shutdown
    mode: output
    active: low
  '11':
    name: Power Button
    mode: input
    active: low
  '12':
    name: I2S Clock
  '13':
    name: Enter
    mode: input
    active: low
  '15':
    name: Escape
    mode: input
    active: low
  '16':
    name: Coin
    mode: input
    active: low
  '18':
    name: Start
    mode: input
    active: low
  '19':
    name: 'Button 6'
    mode: input
    active: low
  '21':
    name: 'Button 5'
    mode: input
    active: low
  '22':
    name: 'Button 4'
    mode: input
    active: low
  '23':
    name: 'Button 2'
    mode: input
    active: low
  '24':
    name: 'Button 3'
    mode: input
    active: low
  '29':
    name: 'Button 1'
    mode: input
    active: low
  '31':
    name: Down
    mode: input
    active: low
  '32':
    name: Up
    mode: input
    active: low
  '35':
    name: I2S WS
  '36':
    name: Right
    mode: input
    active: low
  '38':
    name: Left
    mode: input
    active: low
  '40':
    name: I2S Data
install:
  'devices':
  - 'i2s'
-->
#Picade HAT

Picade HAT proporciona conexión para 10 botones arcade y un joystick. Además incluye un conversor de audio digital a analógico y un amplificador con salida hacia un altavoz. p

Todos los botones deben ser configurados con su pull-up interno. Los botones deben ser conectados en entrada y tierra.

* Conexión para 10 botones
* 4 entradas para un joystick
* Sonido estéreo en un solo altavoz
* Soporte para un botón externo

Para poner el HAT en funcionamiento, puedes utilizar nuestro de una línea:

```bash
curl -sS https://get.pimoroni.com/picadehat | bash
```
