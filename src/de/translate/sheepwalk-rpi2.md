<!--
---
name: RPI2 1-Wire Adapter
class: board
type: com
formfactor: Custom
manufacturer: Sheepwalk
description: I2C to 1-Wire host adapter
url: http://www.sheepwalkelectronics.co.uk/RPI2.php
buy: http://www.sheepwalkelectronics.co.uk/product_info.php?products_id=30
image: 'sheepwalk-rpi2.png'
pincount: 10
eeprom: no
power:
  '2':
ground:
  '6':
  '9':
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
# RPI2 1-Wire Host Adapter

This module provides a way to connect 1-Wire devices to your Raspberry Pi without using up one of the USB ports. It is based around the DS2482-100 I2C to 1-Wire IC. 

Connection to your 1-Wire network is either by the RJ45 socket or the screw terminals. The RJ45 socket allows the assembly of a network using standard ethernet cables.

The jumpers on the RPI2 host adapter allow you to set the i2c address of the IC. This means that if you have multiple RPI2 adapters or you have other i2c devices on the bus you can change its address to avoid conflicts. By default the address is 0x18 but it can be set to 0x19, 0x1a or 0x1b.
