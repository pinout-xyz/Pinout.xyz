<!--
---
name: GPIO I2C pHAT
class: board
type: io
formfactor: pHAT
manufacturer: PlasmaDan
description: 4 Extra I2C Buses for Raspberry Pi.
url: https://plasmadan.com/gpioi2c
github: https://github.com/plasmadancom/GPIO-I2C-pHAT
buy: https://plasmadan.com/gpioi2c
image: 'gpio-i2c-phat.png'
pincount: 40
eeprom: no
pin:
  '7':
    name: I2C3 SDA
    mode: i2c
    direction: both
    active: high
  '15':
    name: I2C6 SDA
    mode: i2c
    direction: both
    active: high
  '16':
    name: I2C6 SCL
    mode: i2c
    direction: both
    active: high
  '29':
    name: I2C3 SCL
    mode: i2c
    direction: both
    active: high
  '21':
    name: I2C4 SCL
    mode: i2c
    direction: both
    active: high
  '24':
    name: I2C4 SDA
    mode: i2c
    direction: both
    active: high
  '32':
    name: I2C5 SDA
    mode: i2c
    direction: both
    active: high
  '33':
    name: I2C5 SCL
    mode: i2c
    direction: both
    active: high
-->
# GPIO I2C pHAT

The GPIO I2C pHAT is an I2C switch which mounts under your HAT to remap its I2C pins (GPIO 2 & GPIO 3) to 1 of 4 additional I2C buses, without the need for a multiplexer or expander.

Makes use of the extra hardware I2C buses introduced on Raspberry Pi 4 (BCM2711) or software I2C (bit bang). Switching is controlled using a 4-position double-pole slide switch, which allows you to quickly switch between buses.

## Features

* Adds 4 additional I2C buses with breakout
* User selectable I2C GPIO pin remapping
* Hardware I2C compatible (Pi 4)
* Slide switch allows fast bus switching
* No-conflict solder jumpers
* Stackable design
* Immersion gold plated copper

## Usage

Add required dtoverlay parameter(s) to ```/boot/config.txt``` and reboot.

Mount the GPIO I2C pHAT board to your Pi, use the slide switch to select your preferred I2C bus and stack your I2C based HAT on top.

## Hardware I2C (Pi 4 Only)

```
dtoverlay=i2c3
dtoverlay=i2c4
dtoverlay=i2c5
dtoverlay=i2c6
```

## Software I2C (Bit Bang)

```
dtoverlay=i2c-gpio,bus=6,i2c_gpio_sda=22,i2c_gpio_scl=23
dtoverlay=i2c-gpio,bus=5,i2c_gpio_sda=12,i2c_gpio_scl=13
dtoverlay=i2c-gpio,bus=4,i2c_gpio_sda=8,i2c_gpio_scl=9
dtoverlay=i2c-gpio,bus=3,i2c_gpio_sda=4,i2c_gpio_scl=5
```

Note: When using multiple software I2C buses, it's best to add the parameters from highest to lowest, i.e., 6, 5, 4, 3.