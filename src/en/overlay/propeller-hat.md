<!--
---
name: Propeller HAT
class: board
type: mcu,io,motor
formfactor: HAT
manufacturer: Pimoroni
description: The 8-core Propeller Microcontroller in HAT form-factor
url: http://shop.pimoroni.com/products/propeller-hat
github: https://github.com/pimoroni/piano-hat
buy: https://shop.pimoroni.com/products/propeller-hat
image: 'propeller-hat.png'
pincount: 40
eeprom: yes
power:
  '2':
ground:
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
    name: Reset
    active: low
  '29':
    name: EEPROM WP
    active: low
-->
#Propeller HAT

Propeller HAT brings the 8-core Parallax Propeller microcontroller to HAT form-factor. Program and talk to it over Serial using Propeller IDE and you'll have a powerful, realtime co-processor for your Pi.

It's like a little software programming logic device. Great for realtime IO, servo control and even convincingly synthesizing a SID chip.