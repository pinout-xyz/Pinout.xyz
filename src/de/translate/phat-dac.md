<!--
---
name: pHAT DAC
class: board
type: audio
formfactor: pHAT
manufacturer: Pimoroni
description: EIN I2S digital ZU analog audio Konverter
buy: https://shop.pimoroni.com/products/phat-dac
image: 'phat-dac.png'
pincount: 40
eeprom: nein
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

DER pHAT DAC verfügt über einen high-quality digital nach analog audio Konverter für den Raspberry Pi: 24-bits bei 192KHz über das I2S Interface mit dem 2x20 pin GPIO header. Er hat einen a 3.5mm stereo Klinkenstecker vormontiert. Optional kann ein RCA Klinkenstecker angelötet werden.

Obwohl der Formfaktor des pHAT dem des Raspberry Pi Zero entspricht ist er kompatible mit allen 40-pin GPIO Raspberry-Pi-Varianten (2/B+/A+/Zero).

Um den pHAT DAC aufzusetzen und sofort zuverwenden, nutzt man die one-line Produkt Installationsroutine:

```bash
curl -sS https://get.pimoroni.com/phatdac | bash
```
