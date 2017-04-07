<!--
---
name: Navio2 Autopilot
class: board
type: gps,motor,sensor
formfactor: HAT
manufacturer: Emlid
collected: Other
description: Full drone controller for Raspberry Pi
url: https://docs.emlid.com/navio2/
github: https://github.com/emlid/Navio2
buy: https://emlid.com/shop/navio2/
image: 'emlid-navio2.png'
pincount: 40
eeprom: setup
power:
  '1':
  '2':
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
    name: MS5611 Data
    mode: i2c
  '5':
    name: MS5611 Clock
    mode: i2c
  '7':
    name: Red LED
    mode: output
    active: high
  '13':
    name: Green LED
    mode: output
    active: high
  '15':
    name: LSM9DS1 Chip Select
    mode: chipselect
    active: high
  '16':
    name: MPU9250 Interrupt
    mode: output
    active: high
  '18':
    name: RCIO PC10
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: LSM9DS1 Chip Select
    mode: chipselect
    active: high
  '23':
    mode: spi
  '24':
  '26':
    name: MPU9250 Chip Select
    mode: chipselect
    active: high
  '29':
    name: RCIO PC11
  '31':
    name: Blue LED
    mode: output
    active: high
  '32':
    name: RCIO Clock
  '33':
    name: RCIO Data
  '35':
    name: RCIO MISO
    mode: spi
  '36':
    name: RCIO Chip Select
    mode: chipselect
    active: high
  '38':
    name: RCIO MOSI
    mode: spi
  '40':
    name: RCIO SCLK
    mode: spi
i2c:
  '0x77':
    name: Barometer
    device: MS5611
-->
# Navio2 Autopilot

The Navio2 Autopilot is designed both for your own custom robotic projects and as a platform for Linux version of APM (ArduPilot).

Navio2 eliminates the need for multiple on-board controllers making development easier and increasing robustness. It extends connectivity and allows control of all kinds of moving robots: cars, boats, multirotors, planes.

For accurate knowledge of position and orientation Navio2 is equipped with double IMU and GPS/Glonass/Beidou receiver. PWM, ADC, SBUS and PPM are integrated in Linux sysfs via the on-board RC I/O co-processor (communicating over SPI1 bus), allowing easy access from any programming language.

Features:

* MS5611 Barometer (I2C1)
* MPU9250 9DOF IMU (SPI0)
* LSM9DS1 9DOF IMU (SPI0)
* Ublox M8N Glonass/GPS/Beidou (SPI0)
* 14 PWM servo outputs (RCIO)
* PPM/S.Bus input (RCIO)
* 6-channel ADC (RCIO)
* Integrated RGB LED
* UART, I2C terminals for extensions
* Power module connector
* Triple redundant power supply
