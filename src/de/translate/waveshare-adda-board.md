<!--
---
name: High-Precision AD/DA Board
class: board
type: adc
formfactor: HAT
manufacturer: Waveshare
description: 8 channel Analogue to Digital Converter & 2 channel Digital to Analogue Converter
url: http://www.waveshare.com/High-Precision-AD-DA-Board.htm
schematic: http://www.waveshare.com/wiki/File:High-Precision-AD-DA--Schematic.pdf
buy: http://www.waveshare.com/High-Precision-AD-DA-Board.htm
image: 'waveshare-adda-board.png'
pincount: 40
eeprom: no
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
  '11':
    name: DRDY
    mode: output
    active: low
  '12':
    name: RESET
    mode: output
    active: high
  '13':
    name: PDWN
    mode: input
    active: low
  '15':
    name: CS0
    mode: output
    active: low
  '16':
    name: CS1
    mode: output
    active: low
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
-->
#High-Precision AD/DA Board

The High-Precision AD/DA Board allows you to add high-precision analog to digital and digital to analog functions to the Raspberry Pi.

##Features

- Onboard ADS1256, 8ch 24bit high-precision ADC (4ch differential input), 30ksps sampling rate
- Onboard DAC8532, 2ch 16bit high-precision DAC
- Onboard input interface via pinheaders, for connecting analog signal
    - the pinout is compatible with Waveshare sensor interface standard, easy to connect various analog sensor modules
- Onboard input/output interface via screw terminals, for connecting analog/digital signal
- Features AD/DA detect circuit, easy for signal demonstration

##Getting Started

- [Official Wiki page getting started on Linux](http://www.waveshare.com/wiki/High-Precision_AD/DA_Board)
- [Raspberry Pi AD/DA Board Library for Window 10 IoT Core](https://www.hackster.io/laserbrain/raspberry-pi-ad-da-board-library-for-window-10-iot-core-c8cc34 "www.hackster.io")
