<!--
---
name: PaPiRus Zero
class: board
type: display
formfactor: pHAT
manufacturer: Pi Supply
description: PaPiRus Zero is an ePaper / eInk screen pHAT module for the Pi Zero
url: https://www.kickstarter.com/projects/pisupply/papirus-the-epaper-screen-hat-for-your-raspberry-p
github: https://github.com/PiSupply/PaPiRus
buy: https://www.pi-supply.com/product/papirus-zero-epaper-screen-phat-pi-zero/
image: 'papirus-zero.png'
pincount: 40
eeprom: no
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
    name: Chip On Glass Reset
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: Chip On Glass Busy
  '23':
    mode: spi
  '24':
    mode: spi
  '26':
    mode: spi
  '35':
    name: SW4
    mode: input
    active: low
  '36':
    name: SW2
    mode: input
    active: low
  '37':
    name: SW5
    mode: input
    active: low  
  '38':
    name: SW3
    mode: input
    active: low
  '40':
    name: SW1
    mode: input
    active: low
  i2c:
    '0x48':
      name: Temperature Sensor
      device: LM75BD
-->
#PaPiRus Zero

The PaPiRus Zero is a versatile ePaper display for the Raspberry Pi Zero with screens ranging from 1.44" to 2.0" in size.

Unlike conventional displays, ePaper reflects light, and is capable of holding text and images indefinitely, even without electricity. The display does not require any power to keep the image and will stay 'on' without any power connection for many days before slowly fading. It's also daylight readable and is very high contrast.

* Interchangeable screen sizes (1.44" or 2.0")
* 32MBit Flash Memory
* Digital temperature sensor and thermal watchdog
* GPIO breakout solder pads
* 5 x optional slimline switches on top

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sSL https://goo.gl/i1Imel | sudo bash
```

Before using PaPiRus, do not forget to enable the SPI and I2C interfaces!
