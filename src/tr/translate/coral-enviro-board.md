<!--
---
name: Coral Environmental Sensor Board
class: board
type: adc,sensor
formfactor: pHAT
manufacturer: Google
description: An Environmental Sensor and Grove Breakout Board
url: https://coral.withgoogle.com/products/environmental
github: https://coral.googlesource.com/coral-cloud/
buy: https://coral.withgoogle.com/products/environmental
image: 'coral-enviro-board.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
  '17':
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
  '8':
    mode: uart
  '10':
    mode: uart
  '12':
    mode: pwm
  '13':
    name: OPT3002_INT
    mode: input
    active: low
  '16':
    name: Push Button
    mode: input
    active: low
  '18':
    name: OLED DC
    mode: output
    active: high
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: OLED RESET
    mode: output
    active: low
  '23':
    mode: spi
  '24':
    mode: spi
  '29':
    name: A71CH_RST_N
    mode: output
    active: low
  '33':
    mode: pwm
  '35':
    name: HDC2010_DRDY
    mode: input
    active: high
  '40':
    name: LED
    mode: output
    active: high
i2c:
  '0x30':
    name: Cyptographic Secure Element
    device: ECC608
  '0x40':
    name: Humidity/Temperature Sensor
    device: HDC2010
  '0x45':
    name: Wide Spectrum Ambient Light Sensor
    device: OPT3002
  '0x49':
    name: Single-Channel ADC
    device: TLA2021
  '0x76':
    name: Barometric Pressure Sensor
    device: BMP280

-->
# Coral Environmental Sensor Board

The Coral Environmental Sensor Board adds multiple environmental sensors and Grove connectors for external devices. It works with all 40-pin Rasperry Pi variants as well as the Coral Dev Board.

Features:

* 128x32 OLED Display (SSD1306-based SPI interface)  
* Ambient light sensor (OPT3002, 0x45 on i2c bus)  
* Barometric pressure sensor (BMP280, 0x76 on i2c bus)  
* Humidity / temperature sensor (HDC2010, 0x40 on i2c bus)  
* Cryptoprocessor with Google keys (ECC608, 0x30 on i2c bus)  
* Four Grove connectors:  
    1x UART  
    1x I2C  
    1x PWM  
    1x 3.3/5V analog (using TLA2022 ADC, 0x49 on i2c bus)
* General purpose button  
* General purpose LED  

