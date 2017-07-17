<!--
---
name: pi-top hub mk1
class: board
type: power, display, other
formfactor: Custom
manufacturer: pi-top
description: The pi-top's central board
url: https://pi-top.com/products/pi-top
buy: https://pi-top.com/products/pi-top
image: 'pi-top-hub-mk1.png'
pincount: 40
eeprom: no
pin:
  '3':
    name: SDA
    mode: i2c
  '5':
    name: SCL
    mode: i2c
  '26':
    name: CE1
    mode: spi
i2c:
  '0x0b':
    name: Smart Battery Management System
    device: bq40z60
install:
  'devices':
    - 'i2c'
    - 'spi'
  'apt':
    - 'pt-hub-controller'
    - 'pt-battery'
-->
#pi-top hub mk1

The pi-top hub mk1 is an integral component of all pi-top devices and an interface for other peripherals such as pi-topSPEAKER, pi-topPROTO and pi-topPULSE.

The hub is also responsible for managing the smart battery via I2C, as well as the connected display's brightness and power management control via SPI.