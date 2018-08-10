<!--
---
name: cube:bit Base
class: board
type: other
formfactor: Custom
manufacturer: 4tronix
description:  Base for your Cube:Bit allowing easy connection of power and signal and directly able to plug in a Raspberry Pi Zero.
url: https://shop.4tronix.co.uk/products/cube-bit-base-for-power-microbit-and-raspberry-pi-cubebit
buy: https://shop.4tronix.co.uk/products/cube-bit-base-for-power-microbit-and-raspberry-pi-cubebit
image: 'cube-bit-base.png'
pincount: 40
eeprom: no

pin:

power:
  '2':

pin:
  '12':
    name: Data
    direction: output
    mode: pwm
    description: WS2812 Data

-->
# cube:bit Base

Base for your Cube:Bit allowing easy connection of power and signal and directly able to plug in a Raspberry Pi Zero.

There is a 40pin GPIO header that you can plug a Raspberry Pi Zero into and it will be powered from the 5V and connect on GPIO 12 (pin 18) to the neopixel array. This is the standard pin for driving neopixels on the Raspberry Pi. Note that there isn't room to fit a full-size Raspberry Pi (though with a GPIO cable you could do that as well)

