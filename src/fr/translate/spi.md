<!--
---
name: SPI
class: interface
type: pinout
description: Raspberry Pi SPI pins
url: https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/
pincount: 5
pin:
  '11':
    name: SPI1 CE1
  '12':
    name: SPI1 CE0
  '19':
    name: SPI0 MOSI
    direction: output
    active: high
    description: Master Out / Slave In
  '21':
    name: SPI0 MISO
    direction: input
    active: high
    description: Master In / Slave Out
  '23':
    name: SPI0 SCLK
    direction: output
    active: high
    description: Clock
  '24':
    name: SPI0 CE0
    direction: output
    active: high
    description: Chip Select 0
  '26':
    name: SPI0 CE1
    direction: output
    active: high
    description: Chip Select 1
  '35':
    name: SPI1 MISO
  '36':
    name: SPI1 CE2
  '38':
    name: SPI1 MOSI
  '40':
    name: SPI1 SCLK
-->
#SPI - Serial Peripheral Interface
---
###SPI0 pins in BCM mode are: 9, 10, 11 + 7/8
###SPI0 pins in WiringPi are: 12, 13, 14 + 10/11
---
Known as the four-wire serial bus, SPI lets you daisy-chain multiple compatible devices off a single set of pins by assigning them different chip-select pins.

A useful example of an SPI peripheral is the MCP23S17 digital IO expander chip ( Note the S in place of the 0 found on the I2C version ). You can also use the SPI port to "Bit-Bang" an ATmega 328, loading Arduino sketches onto it with Gordon Hendersons' modified version of AVRDude.

To talk to an SPI device, you assert its corresponding chip-select pin. By default the Pi has CE0 and CE1.

```python
import spidev
spi = spidev.SpiDev()
spi.open(0, CHIP_SELECT_0_OR_1)
spi.max_speed_hz = 1000000
spi.xfer([value_8bit])
```
