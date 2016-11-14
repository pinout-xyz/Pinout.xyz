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
eeprom: yes
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

The display uses the hardware SPI pins (SCK, MOSI, MISO, CE0, CE1) as well as GPIO #25 and #24. GPIO #18 can be used to PWM dim the backlight if you like. All other GPIO are unused. There's a 2x16 'classic Pi' connection GPIO header on the bottom, you can connect a 26-pin Pi GPIO cable to it to use any of the other pins as you like. The other GPIO are broken out into solder pads at the bottom, in case you want to use more of the GPIO.

Best of all, it comes fully assembled and ready to plug into your Pi! You can use this as a display for running the X interface, or pygame. You can also have an HDMI display seperately connected. There's four mounting ears that can be used to attach the display & Pi to a bezel, or snap them off with pliers (they're perforated) for a slick exactly-the-same-size-as-a-Pi look.
