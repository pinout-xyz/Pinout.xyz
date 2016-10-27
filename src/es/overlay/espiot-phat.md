<!--
---
name: ESP IoT pHAT
class: board
type: mcu,io,iot
formfactor: pHAT
manufacturer: Pimoroni
description: an ESP8266 module programmable from your Pi
url: https://shop.pimoroni.com/products/esp8266-phat
buy: https://shop.pimoroni.com/products/esp8266-phat
image: 'esp8266-phat.png'
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
  '8':
    name: TXD / Transmit
    direction: output
    active: high
  '10':
    name: RXD / Receive
    direction: input
    active: high
  '11':
    name: Chip Reset
    active: low
  '13':
    name: Chip Program
    active: low
-->
#ESP IoT pHAT

ESP IoT pHAT es una placa adicional para Raspberry Pi basada en ESP8266. Cuenta con varios GPIO y un canal ADC, junto a un pequeño área de prototipado. Perfecto para RPi Zero pero también funciona con A+/B+/2.

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS get.pimoroni.com/iotphat | bash
```
