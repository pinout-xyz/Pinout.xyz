<!--
---
name: Cananka
class: board
type: other
collected: Other
formfactor: HAT
manufacturer: Josip Medved
description: Cananka es un HAT para Raspberry Pi que permite la comunicación por bus CAN.
url: https://medo64.com/cananka/
github: https://github.com/medo64/cananka/
image: 'medo64-cananka.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
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
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: Interrupt
    mode: input
    active: low
  '23':
    mode: spi
  '24':
    mode: spi
-->
# Cananka

Cananka es un HAT para Raspberry Pi que permite la comunicación por bus CAN.

Entre sus características están una velocidad de bus de hasta 1Mbit/s (125 kbit/s por
defecto); aislamiento completo (1 kV); no necesita alimentación en el bus CAN
(convertidor CC-CC integrado); admite alimentar la Raspberry Pi desde el bus CAN
(hasta 24 V, 2 A); detección automática mediante la especificación HAT; y funciona
en la Raspberry Pi B+ y posteriores (incluida la Pi Zero).
