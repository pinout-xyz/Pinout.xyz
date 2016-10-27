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

Propeller HAT lleva el microcontrolador de 8-núcleos Parallax Propeler al factort de forma HAT. Comunícate a través del puerto serie utilizando Propeller IDE y siempre tendrás un coprocesador poderoso y de tiempo real para tu Pi.

Es como un pequeño programador lógico. Muy útil para IO en tiempo real, control de servos o sintetizar un chip SID.
