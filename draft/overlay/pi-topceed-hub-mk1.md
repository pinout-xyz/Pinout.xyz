<!--
---
name: pi-topCEED hub mk1
class: board
type: power, display, other
formfactor: Custom
manufacturer: pi-top
description: The pi-top's central board
url: https://pi-top.com/products/ceed
buy: https://pi-top.com/products/ceed
image: 'pi-topceed-hub-mk1.png'
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
install:
  'devices':
    - 'spi'
  'apt':
    - 'pt-hub-controller'
    - 'pt-battery'
-->
#pi-topCEED hub mk1

The pi-topCEED hub mk1 is an integral component of all pi-topCEED devices and an interface for other peripherals such as pi-topSPEAKER, pi-topPROTO and pi-topPULSE.

The hub is also responsible for managing the connected display's brightness and power management control via SPI.