<!--
---
name: Pi Stop
class: board
type: led
formfactor: Custom
manufacturer: 4tronix
description: LED Traffic Lights for Raspberry Pi
url: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=390
buy: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=390
image: '4tronix-pistop.png'
pincount: 4
eeprom: no
ground:
  '9':
pin:
  '11':
    name: Green
    mode: output
    active: high
  '13':
    name: Amber
    mode: output
    active: high
  '15':
    name: Red
    mode: output
    active: high
-->
#Pi Stop Traffic Lights

The PiStop is placed vertically into the GPIO connectors and can be fitted into several positions in the board. It can be fitted into 26-pin headers as well as 40-pin headers.

PiStop only uses 3 GPIO pins plus ground, but you can fit multiple PiStops into one header, although not all positions are possible simultaneously as some pins are shared across the options. Note that only one position is illustrated in the pinout, but any succession of 3 GPIO next to a ground pin is suitable.
