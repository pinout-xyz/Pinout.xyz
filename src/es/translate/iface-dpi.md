<!--
---
name: DPI
class: interface
type: pinout
description: Raspberry Pi DPI pins
url: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#display-parallel-interface-dpi
pin:
  'bcm0':
    name: CLK
  'bcm1':
    name: DEN
  'bcm2':
    name: V-SYNC
  'bcm3':
    name: H-SYNC
  'bcm4':
    name: Blue 0
  'bcm5':
    name: Blue 1
  'bcm6':
    name: Blue 2
  'bcm7':
    name: Blue 3
  'bcm8':
    name: Blue 4
  'bcm9':
    name: Blue 5
  'bcm10':
    name: Blue 6
  'bcm11':
    name: Blue 7
  'bcm12':
    name: Green 0
  'bcm13':
    name: Green 1
  'bcm14':
    name: Green 2
  'bcm15':
    name: Green 3
  'bcm16':
    name: Green 4
  'bcm17':
    name: Green 5
  'bcm18':
    name: Green 6
  'bcm19':
    name: Green 7
  'bcm20':
    name: Red 0
  'bcm21':
    name: Red 1
  'bcm22':
    name: Red 2
  'bcm23':
    name: Red 3
  'bcm24':
    name: Red 4
  'bcm25':
    name: Red 5
  'bcm26':
    name: Red 6
  'bcm27':
    name: Red 7
-->
# DPI - Display Parallel Interface

One of the alternate functions selectable on bank 0 of the Raspberry Pi GPIO is DPI. DPI (Display Parallel Interface) is a 28-pin parallel interface, with 24 data signals plus a clock, a data enable and horizontal and vertical sync.

This interface allows parallel RGB displays to be attached to the Raspberry Pi GPIO in RGB888 (8 bits for red, green and blue), RGB666 (6 bits per colour) or RGB565 (5 bits red, 6 green, and 5 blue). It's alternate function 2 (ALT2) on Pi 1 to Pi 4, and function 1 (F1) on Pi 5.

The pinout here is RGB888, which takes all 28 pins and leaves nothing else on bank 0.

## Colour depth modes

A narrower colour depth needs fewer data pins. The padded modes align each colour to the top of its byte, so the pins they free up are scattered through the bank rather than gathered at the top:

* 565 on GPIO 0-19, leaving GPIO 20-27. Mode 2, or `rgb565`.
* 565 on GPIO 0-8, 12-17 and 20-24, leaving GPIO 9-11, 18, 19 and 25-27. Mode 3, or `rgb565-padhi`.
* 565 on GPIO 0-3, 5-9, 12-17 and 21-25, leaving GPIO 4, 10, 11, 18-20, 26 and 27. Mode 4 only, there's no overlay parameter for this one.
* 666 on GPIO 0-21, leaving GPIO 22-27. Mode 5, the default, or `dtoverlay=dpi18`.
* 666 on GPIO 0-9, 12-17 and 20-25, leaving GPIO 10, 11, 18, 19, 26 and 27. Mode 6, or `rgb666-padhi`, or `dtoverlay=dpi18cpadhi`.
* 888 on GPIO 0-27, leaving nothing. Mode 7, or `rgb888`, or `dtoverlay=dpi24`.

Each of the 666 and 888 modes also has a `bgr` form, such as `bgr666-padhi`, which swaps the red and blue channels over but uses the same pins.

The parameter names belong to `vc4-kms-dpi-generic`, which is how a DPI display is set up from Raspberry Pi OS Bookworm onward. The mode numbers are the `output_format` field of the `dpi_output_format` setting it replaced. `dtoverlay=vga666` is a fixed setup for the Fen Logic VGA666 board and uses GPIO 2-21.

Whichever mode you pick, DPI takes GPIO 0 to GPIO 3 for its clock and sync signals, so the HAT EEPROM pins and I2C1 are always gone. Any I2C or SPI overlay that overlaps has to be turned off too, with `dtparam=i2c_arm=off` and `dtparam=spi=off`.

A padded 666 mode is the usual choice when you need pins back, freeing GPIO 10, 11, 18 and 19 in the middle of the bank as well as 26 and 27 at the top. GPIO 10 and GPIO 11 can carry [one of the extra I2C buses](/pinout/i2c), i2c5 on Pi 4 or i2c1 on Pi 5, which is enough for a touch controller alongside the display.
