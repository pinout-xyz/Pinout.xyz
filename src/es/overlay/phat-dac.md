<!--
---
name: pHAT DAC
class: board
type: audio
formfactor: pHAT
manufacturer: Pimoroni
description: An I2S digital to analog audio converter
buy: https://shop.pimoroni.com/products/phat-dac
image: 'phat-dac.png'
pincount: 40
eeprom: no
power:
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
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
install:
  'devices':
  - 'i2s'
-->
#pHAT DAC

pHAT DAC es un conversor de sonido digital a analógico de alta calidad para Raspberry Pi: 24-bits a 192KHz a través de la interfaz I2S en el conector GPIO de 2x20 pines. Tiene un jack estéreo de 3.5 mm y se puede conectar, opcional, un RCA.

Pese a ser diseñado para Raspberry Pi Zero es compatible con todas las Raspberry Pi de 40 pines (2/B+/A+/Zero)

Para configurar pHAT DAC puedes utilizar el instalador online de una línea.

```bash
curl -sS get.pimoroni.com/phatdac | bash
```
