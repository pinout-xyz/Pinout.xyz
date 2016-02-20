<!--
---
class: board
type: other
name: Propeller HAT
featured: true
image: 'propeller-hat.png'
manufacturer: Pimoroni
description: The 8-core Propeller Microcontroller in HAT form-factor
url: http://shop.pimoroni.com/products/propeller-hat
github: https://github.com/pimoroni/piano-hat
buy: https://shop.pimoroni.com/products/propeller-hat
formfactor: 'HAT'
pincount: 40
eeprom: yes
power:
  '2':
ground:
  '6':
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