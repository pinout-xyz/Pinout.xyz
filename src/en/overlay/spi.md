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
  '27':
    name: SPI CE0
    supported: Pi 4 (spi3) and Pi 5 (spi2)
  '28':
    name: SPI MISO
    supported: Pi 4 (spi3) and Pi 5 (spi2)
  '3':
    name: SPI MOSI
    supported: Pi 4 (spi3) and Pi 5 (spi2)
  '5':
    name: SPI SCLK
    supported: Pi 4 (spi3) and Pi 5 (spi2)
  '7':
    name: SPI CE0
    supported: Pi 4 (spi4) and Pi 5 (spi3)
  '29':
    name: SPI MISO
    supported: Pi 4 (spi4) and Pi 5 (spi3)
  '31':
    name: SPI MOSI
    supported: Pi 4 (spi4) and Pi 5 (spi3)
  '32':
    name: SPI CE0
    supported: Pi 4 and Pi 5 (spi5)
  '33':
    name: SPI MISO
    supported: Pi 4 and Pi 5 (spi5)
  '8':
    name: SPI MOSI
    supported: Pi 4 and Pi 5 (spi5)
  '10':
    name: SPI SCLK
    supported: Pi 4 and Pi 5 (spi5)
-->
# SPI - Serial Peripheral Interface

* SPI0 pins are GPIO 7, GPIO 8, GPIO 9, GPIO 10, GPIO 11
* SPI1 pins are GPIO 16, GPIO 17, GPIO 18, GPIO 19, GPIO 20, GPIO 21

Known as the four-wire serial bus, SPI lets you attach multiple compatible devices to a single set of pins by assigning them different chip-select pins.

To talk to an SPI device, you assert its corresponding chip-select pin.

By default the Pi allows you to use SPI0 with chip select pins on CE0 on GPIO 8 and CE1 on GPIO 7.

## Enable via config.txt

You can enable SPI1 with a dtoverlay configured in "/boot/firmware/config.txt", for example:

```
dtoverlay=spi1-3cs
```

For full details of the SPI dtoverlays (and others) see [the Raspberry Pi dtoverlay README](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/overlays/README)

## More than two buses

Pi 4 and Pi 5 both have extra SPI controllers on the low-numbered GPIO pins, numbered differently between the two models. Each group runs CE0, MISO, MOSI then SCLK in ascending pin order:

| Pins | Pi 4 | Pi 5 | Notes |
| --- | --- | --- | --- |
| GPIO 0 to GPIO 3 | spi3 | spi2 | |
| GPIO 4 to GPIO 7 | spi4 | spi3 | GPIO 7 is SPI0's CE1, so the two cannot both be in use |
| GPIO 12 to GPIO 15 | spi5 | spi5 | GPIO 14 and GPIO 15 are also the UART pins |
| GPIO 18 to GPIO 21 | spi6 | | Shares SPI1's pins, with CE0 on GPIO 18 |

Enable one with the matching overlay, in a `1cs` or `2cs` form for the number of chip selects you need: `dtoverlay=spi4-1cs` on a Pi 4, `dtoverlay=spi3-1cs-pi5` on a Pi 5. The `cs0_pin` parameter moves the chip select if the default clashes with something.

The `spi2` overlay without a `-pi5` suffix is a different thing entirely: spi2 on GPIO 40 to GPIO 42, which only exists on Compute Modules.

Raspberry Pi 5 documentation calls MISO and MOSI SIO1 and SIO0, since RP1's SPI blocks can run in modes where the data lines change direction.
