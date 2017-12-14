<!--
---
name: MDB2Pi HAT
class: board
type: IO,Power
formfactor: HAT
manufacturer: Abrantix
description: Multi-Drop-Bus MDB Converter Board for the Raspberry Pi
url: http://blog.abrantix.com/webshop/mdb-converter/
buy: http://blog.abrantix.com/webshop/product/mdb-to-raspberrypi
image: 'mdb2pi-hat.png'
pincount: 40
eeprom: yes
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    mode: UART
  '10':
    mode: UART
  '27':
    mode: i2c
  '28':
    mode: i2c
i2c:
  '0x50':
    name: HAT EEPROM on I2C0
    device: 24C32
  '0x51':
    name: RTC on I2C1
    device: PCF8563
-->
# MDB2Pi HAT

The MDB2Pi is a Raspberry Pi HAT which can serve as a MDB master (VMC), as MDB cashless peripheral, or as tracer for MDB Vending Machines. It takes care of the MDB specific 9-bit format, electrical and timing constraints. It forwards the MDB payload to the Raspberry Pi UART using a simple serial protocol. The MDB2Pi is powered through the MDB bus (10...42V regulated or unregulated supply) and back-powers the Raspberry Pi with up to 2.5A at 5V. Therefore, no separate power supply is required. Furthermore, the MDB2Pi contains a Real Time Clock (RTC), buffered by a super capacitor.

A housing for the MDB2Pi (and the MDB2Pi itself) is available at the Abrantix Web Shop: http://blog.abrantix.com/webshop/product/mdb-to-raspberrypi/. Alternatively, you can download a free 3D model here: http://www.thingiverse.com/thing:2209661

For Configuration and further information, please see http://blog.abrantix.com/webshop/mdb-to-raspberry-pi-configuration/
