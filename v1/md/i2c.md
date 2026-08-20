<!--
---
name: I2C
class: interface
type: pinout
description: Raspberry Pi I2C pins
url: http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
pin:
  '3':
    name: Data
    direction: both
    active: high
  '5':
    name: Clock
    direction: both
    active: high
  '27':
    name: EEPROM Data
    direction: both
    active: high
  '28':
    name: EEPROM Clock
    direction: both
    active: high
  '7':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c3) and Pi 5 (i2c2)
  '29':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c3) and Pi 5 (i2c2)
  '31':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c4) and Pi 5 (i2c3)
  '26':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c4) and Pi 5 (i2c3)
  '24':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c4) and Pi 5 (i2c0)
  '21':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c4) and Pi 5 (i2c0)
  '19':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c5) and Pi 5 (i2c1)
  '23':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c5) and Pi 5 (i2c1)
  '32':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c5) and Pi 5 (i2c2)
  '33':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c5) and Pi 5 (i2c2)
  '15':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c6) and Pi 5 (i2c3)
  '16':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c6) and Pi 5 (i2c3)
  '8':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 5 (i2c3)
  '10':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 5 (i2c3)
-->
# I2C - Inter Integrated Circuit

GPIO 2 and GPIO 3 - the Raspberry Pi's I2C1 pins - allow for two-wire communication with a variety of external sensors and devices.

The I2C pins include a fixed 1.8 kΩ pull-up resistor to 3.3v. They are not suitable for use as general purpose IO where a pull-up might interfere.

I2C is a multi-drop bus, multiple devices can be connected to these same two pins. Each device has its own unique I2C address.

I2C is turned off on a stock Raspberry Pi OS image. Enable it with `raspi-config`, or by adding `dtparam=i2c_arm=on` to `/boot/firmware/config.txt`.

Once it's on, `i2cdetect -y 1` from the `i2c-tools` package lists the addresses responding on the bus.

GPIO 0 and GPIO 1 - I2C0 - can be used as an alternate I2C bus, but are typically used by the system to read the HAT EEPROM.

## More than one bus

i2c1 is the only bus available without an overlay. Pi 4 and Pi 5 both have several more, each on a pair of low-numbered GPIO pins, but the numbering differs between the two models:

| Pins | Pi 4 | Pi 5 | Notes |
| --- | --- | --- | --- |
| GPIO 0 and GPIO 1 | i2c0 or i2c6 | i2c0 | Usually left alone for the HAT EEPROM |
| GPIO 2 and GPIO 3 | i2c1 or i2c3 | i2c1 | |
| GPIO 4 and GPIO 5 | i2c3 | i2c2 | |
| GPIO 6 and GPIO 7 | i2c4 | i2c3 | |
| GPIO 8 and GPIO 9 | i2c4 | i2c0 | |
| GPIO 10 and GPIO 11 | i2c5 | i2c1 | |
| GPIO 12 and GPIO 13 | i2c5 | i2c2 | |
| GPIO 14 and GPIO 15 | | i2c3 | Also the UART pins |
| GPIO 22 and GPIO 23 | i2c6 | i2c3 | |

Each bus is enabled with a device tree overlay, and the pin pair is chosen with a parameter: `dtoverlay=i2c4,pins_6_7` on a Pi 4. On Pi 5 the overlays take a `-pi5` suffix, so the same pins are `dtoverlay=i2c3-pi5,pins_6_7`.

Only GPIO 2 and GPIO 3 have pull-up resistors fitted. Every other pair needs your own, typically 4.7 kΩ to 3.3v.
