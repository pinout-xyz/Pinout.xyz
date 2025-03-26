<!--
---
name: DPI TFT Kippah
class: board
type: display
formfactor: HAT
manufacturer: Adafruit
description: Run 40 pin TFT's of a Raspberry Pi
url: https://learn.adafruit.com/adafruit-dpi-display-kippah-ttl-tft
buy: https://www.adafruit.com/products/2453
image: adafruit-tft-kippah.png 
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '9':
  '25':
  '39':
  '34':
  '30':
  '20':
  '14':
  '6': 
pin:
  '3':
  '5':
  '7': 
  '29':
  '31':
  '26':
  '24':
  '21':
  '19':
  '23': 
  '32':
  '33':
  '8':
  '10':
  '36':
  '11':
  '12':
  '35':
  '38':
  '40':
-->
# DPI TFT Kippah
 
A TFT panel connected to a Raspberry Pi without the use of an HDMI decoder? What is this sorcery??? It's the DPI Kippah from Adafruit! This HAT-like* board snaps onto a Raspberry Pi B+, A+, Pi 2, Pi 3 or Zero and with a little software configuration, allows you to have what normally would go out the HDMI port come up on a nice little flat screen.

The catch is this add on board uses nearly every pin available on the Raspberry Pi and those pins are hardcoded, they cannot be moved or rearranged. The pins used are GPIO 2 through 21 inclusive. That means you don't get the UART RX/TX pins (no console cable) and you don't get the standard user I2C pins, the EEPROM I2C pins, or hardware SPI pins. You do get to use pins #22, #23, #24, #25, #26 and #27, and the USB ports are fine to use too.

The other catch is that this display replaces the HDMI/NTSC output, so you can't have the DPI HAT and HDMI working at once, nor can you 'flip' between the two.

Also, there's no PWM's available so you can't have precision backlight control unless you somehow rig up an external PWM generator with a 555 or something.

Please note it is the same pinout for the touchscreen and none touchscreen version of the board.
 
For installation instructions please follow Adafruit's tutorial linked below
