<!--
---
name: Pi-mote
class: board
type: com
formfactor: Custom
manufacturer: Energenie
collected: Other
description: Add-on that allows control of Energenie smart plugs from a Raspberry Pi
url: https://energenie4u.co.uk/res/pdfs/ENER314%20UM.pdf
buy: https://energenie4u.co.uk/catalogue/product/ENER314
image: 'energenie-pi-mote.png' 
pincount: 26
eeprom: no
power:
  '1':
ground:
  '6':
pin:
  '11':
    name: D0 Encoder
    mode: output
    active: high
  '13':
    name: D3 Encoder
    mode: output
    active: high
  '15':
    name: D1 Encoder
    mode: output
    active: high
  '16':
    name: D2 Encoder
    mode: output
    active: high
  '18':
    name: Mode Select
    mode: output
    active: high
  '22':
    name: Modulator CE
    mode: output
    active: high
-->
# Pi-mote

The Pi-mote is a RF transmitter add-on board that allows control of up to 4 Energenie radio controlled sockets independently using Python.

With it you will be able to control your electrical sockets within a range of up to 30 metres, through doors, walls and ceilings.
