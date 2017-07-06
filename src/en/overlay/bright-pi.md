<!--
---
name: My Add-on Board
class: board
type: led
formfactor: Custom
manufacturer: Pi Supply
description: The Bright Pi adds both visible bright white light and infrared illumination to the Raspberry Pi camera.
url: https://www.kickstarter.com/projects/pisupply/bright-pi-bright-white-and-ir-camera-light-for-ras
github: https://github.com/PiSupply/BrighPi
buy: https://www.pi-supply.com/product/bright-pi-bright-white-ir-camera-light-raspberry-pi/
image: 'bright-pi.png'
pincount: 4
eeprom: no
power: 5v
  '1':
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
  '4':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x70':
    name: LED Driver
    device: SC620
-->
#Bright Pi

The Bright Pi is a breakout/add on board for the Raspberry Pi (can be used with other I2C devices too – Arduino etc.) which adds both visible bright white light and infrared illumination to the Raspberry Pi, for use with the Raspberry Pi camera module, the Pi NoIR camera module or for any other project which requires bright LEDs.
