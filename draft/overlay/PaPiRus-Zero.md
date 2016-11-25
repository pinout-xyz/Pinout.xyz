<!--
---
name: PaPiRus Zero
class: board
type: display
formfactor: pHAT
manufacturer: Pi Supply
description: PaPiRus Zero is an ePaper / eInk screen pHAT module for the Pi Zero.
url: https://www.kickstarter.com/projects/pisupply/papirus-the-epaper-screen-hat-for-your-raspberry-p
github: https://github.com/PiSupply/PaPiRus
schematic:
buy: https://www.pi-supply.com/product/papirus-zero-epaper-screen-phat-pi-zero/
image: 'pisupply-papirus-zero.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    name: Border Control
  '10':
    name: Discharge
  '11':
    name: Temp Sens
  '16':
    name: Panel On
  '18':
    name: Reset COG (Chip On Glass) 
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: Busy COG (Chip On Glass)
  '23':
    mode: spi
  '24':
    mode: spi
  '26':
    mode: spi
  '35':
    name: Button 3
    mode: input
    active: low
  '36':
    name: Button 4
    mode: input
    active: low
  '37':
    name: Button 2
    mode: input
    active: low  
  '38':
    name: Button 1
    mode: input
    active: low
  '40':
    name: Button 5
    mode: input
    active: low
-->
#PaPiRus ePaper eInk display
* Raspberry Pi pHAT compliant design
* Interchangeable screen sizes (1.44" or 2.0")
* 32MBit Flash Memory
* Digital temperature sensor and thermal watchdog
* GPIO breakout solder pads
* 5 x optional slimline switches on top

Before using PaPiRus, do not forget to enable the SPI interface!
Also make sure to enable I2C for the temperature sensor.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sSL https://goo.gl/i1Imel | sudo bash
```
