<!--
---
name: RPi-Spark
class: board
type: other, display, audio, multi, sensor, IO
formfactor: pHAT
manufacturer: mobiNRG
description: RPi-Spark pHAT and SDK let you quickly and easily bulid the application of the Raspberry Pi GPIO.
url: https://www.mobinrg.com
github: https://github.com/mobinrg/rpi_spark_foundations
buy: https://www.mobinrg.com/pages/products/rpi_spark
image: 'rpi-spark.png'
pincount: 19
eeprom: no
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
    mode: i2c
  '5':
    mode: i2c
  '19':
    name: DSP_MOSI
    mode: spi
  '21':
    name: DSP_DC
    mode: spi
  '23':
    name: DSP_CLK
    mode: spi
  '24':
    name: DSP_CS
    mode: spi
  '22':
    name: MOTION_INT
    mode: input
  '13':
    name: JOY_R
    mode: input
    active: low
  '18':
    name: JOY_C
    mode: input
    active: low
  '29':
    name: JOY_U
    mode: input
    active: low
  '31':
    name: JOY_D
    mode: input
    active: low
  '37':
    name: JOY_L
    mode: input
    active: low
  '15':
    name: SW_A
    mode: input
    active: low
  '16':
    name: SW_B
    mode: input
    active: low
  '33':
    name: AUDIO_R/SPK
    mode: output
  '32':
    name: AUDIO_L
    mode: output
i2c:
  '0x68':
    name: accelerometers, gyroscopes
    device: RPISpark
-->
# RPi-Spark

RPi-Spark pHAT and SDK let you quickly and easily bulid the application of the Raspberry Pi GPIO.
For example: games, remote control car, balance car, sports pedometer, server monitor and other applications.

### Key Features

#### Hardware
* 128x64 monochrome OLED
* Accelerometers
* Gyroscopes
* Temperature
* 5-way joystick
* 2 action buttons
* 3.5mm stereo headphone jack
* 1W speaker
* 19 extended GPIOs

#### SDK
* Drives - RPi-Spark hardware driver library, You can use them directly to build applications and be used with other open source libraries
* Skeletons - Let you can easy and fast development
* CLI interface - Let you can use your favorite languages, like Bash Script, Node.js, Java, PHP, C/C++, Pascal, Basic and so all.



### Supported
* Raspberry Pi 2/3/3+/Zero/Zero W



#### Requirements:

* Raspbian Linux
* Python 2.7 or Python 3.x
