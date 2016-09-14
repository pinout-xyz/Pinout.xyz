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

The ESP IoT pHAT is an ESP8266 based add-on for the Raspberry Pi. It provides some GPIO and one ADC channel, broken out to use alongside a small prototyping area. Perfect for RPi Zero but works with A+/B+/2 too!

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/iotphat | bash
```
