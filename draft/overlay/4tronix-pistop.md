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
power:
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
  '3':
    name: Red_0
    mode: output
    active: high
  '5':
    name: Amber_0
    mode: output
    active: high
  '7':
    name: Green_0
    mode: output
    active: high
  '15':
    name: Red_1
    mode: output
    active: high
  '13':
    name: Amber_1
    mode: output
    active: high
  '11':
    name: Green_1
    mode: output
    active: high
  '19':
    name: Red_2
    mode: output
    active: high
  '21':
    name: Amber_2
    mode: output
    active: high
  '23':
    name: Green_2
    mode: output
    active: high
  '31':
    name: Red_3
    mode: output
    active: high
  '29':
    name: Amber_3
    mode: output
    active: high
  '27':
    name: Green_3
    mode: output
    active: high
  '33':
    name: Red_4
    mode: output
    active: high
  '35':
    name: Amber_4
    mode: output
    active: high
  '37':
    name: Green_4
    mode: output
    active: high
  '12':
    name: Red_5
    mode: output
    active: high
  '10':
    name: Amber_5
    mode: output
    active: high
  '8':
    name: Green_5
    mode: output
    active: high
  '26':
    name: Red_6
    mode: output
    active: high
  '24':
    name: Amber_6
    mode: output
    active: high
  '22':
    name: Green_6
    mode: output
    active: high
  '24':
    name: Red_7
    mode: output
    active: high
  '26':
    name: Amber_7
    mode: output
    active: high
  '28':
    name: Green_7
    mode: output
    active: high
  '40':
    name: Red_8
    mode: output
    active: high
  '38':
    name: Amber_8
    mode: output
    active: high
  '36':
    name: Green_8
    mode: output
    active: high
-->
#Pi Stop Traffic Lights

The PiStop is placed vertically into the GPIO connectors and can be fitted into several positions in the board. It can be fitted into 26-pin headers as well as 40-pin headers. It only uses 3 GPIO pins plus ground, but you can fit multiple PiStops into one header, although not all positions are possible simultaneously as some pins are shared across the options.