<!--
---
name: 1 Wire Pi Zero
class: board
type: com
formfactor: pHAT
manufacturer: AB Electronics
description: 1-Wire to I2C host interface
url: https://www.abelectronics.co.uk/p/76/1-Wire-Pi-Zero
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/76/1-Wire-Pi-Zero
image: 'ab-1-wire-pi-zero.png'
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
i2c:
  '0x18':
    name: DS2482
    device: DS2482-100
-->
#1 Wire Pi Zero

The 1 Wire Pi Zero from AB Electronics UK is a communication board supporting the 1-Wire® protocol designed for use on the Raspberry Pi Zero.  A 5V buffered I2C port is also provided on the board. 

The 1-Wire® port on the 1 Wire Pi Zero is based around a DS2482-100 I2C to 1-Wire® bridge device.  The DS2482-100 provides bi-directional protocol conversion between the I2C port on the Raspberry Pi and any attached 1-Wire® slave devices.  An ESD Protection Diode is used to protect the 1 Wire Pi Zero and Raspberry Pi from electrostatic spikes on the 1-Wire® port.  Connections to the 1-Wire® port can be made through the RJ-12 socket or the solder points on the PCB.

I2C address select solder jumpers give you the ability to set the I2C address of the 1 Wire Pi Zero allowing the board to be used with other I2C devices on the same bus.

[https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi](https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi "Configuring and using the 1-Wire® port on your Raspberry Pi")