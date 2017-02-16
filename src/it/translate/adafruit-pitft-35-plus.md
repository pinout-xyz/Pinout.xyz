<!--
---
name: PiTFT Plus 3.5"
class: board
type: display
formfactor: Custom
manufacturer: Adafruit
description: A TFT Display for the Raspberry Pi
url: https://learn.adafruit.com/adafruit-pitft-3-dot-5-touch-screen-for-raspberry-pi
github: https://github.com/adafruit/Adafruit-PiTFT-3.5-Plus-PCB
schematic: https://learn.adafruit.com/assets/26348
buy: https://www.adafruit.com/products/2441
image: 'adafruit-pitft-35-plus.png'
pincount: 40
eeprom: setup
power:
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
  '12':
    name: Backlight Control
    mode: output
  '18':
    name: RT Interrupt
    mode: input
  '22':
    name: TFT Data/Command
    mode: output
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    name: TFT Chip Select
    mode: chipselect
  '26':
    name: RT Chip Select
    mode: chipselect
-->
#PiTFT Plus 3.5"

The PiTFT+ features a 3.5" display with 480x320 16-bit color pixels and a resistive touch overlay and is engineered specifically to work with the Raspberry Pi 3, 2 and the Model A+/B+.

The display uses the hardware SPI pins as well as GPIO #25 and #24. GPIO #18 can be used to PWM dim the backlight. A 2x13 'classic' GPIO header on the bottom, with additional GPIO pins broken out into solder pads, allows you to use more of the GPIO.

The PiTFT+ can be used as a display for running the X interface, or the console. You can also have an HDMI display separately connected to complement the setup, keeping in mind that there can only be one X session running (so you'll need to choose where X should be output, on the HDMI or the PiTFT+).
