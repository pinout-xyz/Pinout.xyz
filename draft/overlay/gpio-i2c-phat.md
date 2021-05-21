<!--
---
name: GPIO I2C pHAT
class: board
type: io
formfactor: pHAT
manufacturer: PlasmaDan
description: 4 Extra I2C Buses for Raspberry Pi.
github: https://github.com/plasmadancom/GPIO-I2C-pHAT
buy: https://plasmadan.com/gpioi2c
image: 'gpio-i2c-phat.png'
pincount: 40
eeprom: no
power:
ground:
pin:
  '4':
    name: I2C3 SDA
    mode: i2c
  '15':
    name: I2C6 SDA
    mode: i2c
  '16':
    name: I2C6 SCL
    mode: i2c
  '29':
    name: I2C3 SCL
    mode: i2c
  '21':
    name: I2C4 SCL
    mode: i2c
  '24':
    name: I2C4 SDA
    mode: i2c
  '32':
    name: I2C5 SDA
    mode: i2c
  '33':
    name: I2C5 SCL
    mode: i2c
-->
# GPIO I2C pHAT

The GPIO I2C pHAT is an I2C switch for Raspberry Pi which remaps the I2C bus (pins 3 & 5) to 1 of 4 additional buses, allowing any I2C based add-on board to use an alternative I2C bus, without the need for multiplexers or expanders.

Makes use of the extra hardware I2C buses introduced on Raspberry Pi 4 (BCM2711) or software I2C (bit bang). Multiple GPIO I2C boards can be stacked along with other HATs or pHATs. Switching is controlled using a 4-position double-pole slide switch, which allows you to quickly switch between buses.

Includes a breakout header for the 4 extra I2C buses. These are always connected to the associated GPIO pins so can be used regardless of the switch position. Note: external pull-up resistors to 3.3V required.

## Features

* Adds 4 additional I2C buses with breakout
* User selectable I2C GPIO pin remapping
* Slide switch allows fast bus switching
* No-conflict solder jumpers
* Stackable design
* Immersion gold plated copper

## Usage

Add required dtoverlay parameter(s) to ```/boot/config.txt``` and reboot.

| Switch Position | Hardware I2C (Pi 4) | Software I2C (Bit Bang) | GPIO |
| :---: | :---: | :---: | :---: |
| I2C3 | dtoverlay=i2c3 | dtoverlay=i2c-gpio,bus=3,i2c_gpio_sda=4,i2c_gpio_scl=5 | 4 5 |
| I2C4 | dtoverlay=i2c4 | dtoverlay=i2c-gpio,bus=4,i2c_gpio_sda=8,i2c_gpio_scl=9 | 8 9 |
| I2C5 | dtoverlay=i2c5 | dtoverlay=i2c-gpio,bus=5,i2c_gpio_sda=12,i2c_gpio_scl=13 | 12 13 |
| I2C6 | dtoverlay=i2c6 | dtoverlay=i2c-gpio,bus=6,i2c_gpio_sda=22,i2c_gpio_scl=23 | 22 23 |

Note: When using multiple software I2C buses, add the parameters from highest to lowest, i.e., 6, 5, 4, 3.