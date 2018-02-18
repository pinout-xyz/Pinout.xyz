<!--
---
name: RGB Matrix Bonnet
class: board
type: led
formfactor: pHAT
manufacturer: Adafruit
description: Easily control large matrices
url: https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/overview
github: https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/blob/master/rgb-matrix.sh
schematic: https://cdn-learn.adafruit.com/assets/assets/000/051/031/original/adafruit_products_schem.png?1518648935
buy: https://www.adafruit.com/product/3211
image: 'adafruit_matrix_bonnet.png'
pincount: 40
eeprom: no
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
  '29':
    name: 'Matrix R1'
  '33':
    name: 'Matrix G1'
  '31':
    name: 'Matrix B1'
  '32':
    name: 'Matrix R2'
  '36':
    name: 'Matrix G2'
  '16':
    name: 'Matrix B2'
  '7':
    name: 'Matrix OE'
  '11':
    name: 'Matrix CLK'
  '40':
    name: 'Matrix LAT'
  '15':
    name: 'Matrix A'
  '37':
    name: 'Matrix B'
  '13':
    name: 'Matrix C'
  '38':
    name: 'Matrix D'
  '18':
    name: 'Matrix E'



-->
#RGB Matrix Bonnet

This HAT plugs into your Pi and makes it super easy to control RGB matrices, such as those you see in the likes of Times square, enabling you to create a colorful scrolling display or mini LED wall.

* A 5V power supply is also required for powering the matrix itself.
* To calculate the max current of your matrix set up, multiply the width of all the chained matrix by 0.12 : A 32 pixel wide matrix needs 32*0.12 = 3.85A so pick up a 5V 4A power supply.
* This HAT is only for use with HUB75 type RGB Matrices. Not for use with NeoPixel, DotStar, or other 'addressable' LEDs.

Features:

* Simple design - plug in power, plug in IDC cable, code.
* Power protection circuitry - you can plug a 5V 4A wall adapter into the HAT and it will automatically protect against negative, over or under-voltages.
* Onboard level shifters - these convert the RasPi's 3.3V to 5.0V logic for clean and glitch free matrix driving

This bonnet is compatible with any Pi that has a 2x20 header.

To install:

```bash
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh
sudo bash rgb-matrix.sh
```
