<!--
---
name: pi-topHUB
class: board
type: power, display, other
formfactor: Custom
manufacturer: pi-top
description: pi-top/pi-topCEED compatible speaker add-on board
url: http://pi-top.com/products
buy: http://pi-top.com/products
image: 'pi-top-hub.png'
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
#pi-topHUB

The pi-topHUB is an integral component of all pi-top/pi-topCEED devices, and an interface for other peripherals, such as pi-topSPEAKER, pi-topPROTO and pi-topPULSE.

The pi-topHUB is responsible for providing access to the smart battery management system on pi-tops via I2C, as well as display brightness, device identification (for pi-tops and pi-topCEEDs) and power management control via SPI.