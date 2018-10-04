<!--
---
name: TroPi
class: board
type: LED
formfactor: Custom
manufacturer: PiBorg
description: A five LED add on board.
url: https://www.piborg.org/tropi
github: https://www.github.com/piborg/tropi
buy: https://www.piborg.org/tropi
image: 'piborg-tropi.png'
pincount: 40
eeprom: no
power:
  '2':
ground:
  '6':
  '20':
  '25':
  '30':
pin:
  '16':
    name: Clock
    mode: output
    active: low
  '18':
    name: Data
    mode: output
    active: low
-->
#TroPi

The TroPi is an RGB LED board with 5 APA102C LEDs which are individually controllable from a Raspberry Pi.
