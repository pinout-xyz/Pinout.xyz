<!--
---
name: High-Precision AD/DA Board
class: board
type: adc
formfactor: HAT
manufacturer: Waveshare
collected: Otro
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

La placa High-Precision AD/DA proporciona funciones de conversión analógica a digital y viceversa de gran precisión a Raspberry Pi.

##Características

- ADS1256, 8 canales 24 bit alta precisión ADC (4 canales de salida diferencial), 30ksps velocidad de sampleo
- DAC8532, 2 canales 16 bit alta precisión DAC8532
- Interfaz a través de los pines para conectar señal analógica
    - Los pines son compatibles con la interfaz estándar Waveshare, para conectar fácilmente distintos sensores
- Interfaz de entrada/salida a través de las conexiones analógica/digital
- Circuito de detección AD/DA para demostraciones sencillas

##Comienzo

- [Wiki oficial](http://www.waveshare.com/wiki/High-Precision_AD/DA_Board)
- [Libería Raspberry Pi AD/DA Board para Windows 10 IoT Core](https://www.hackster.io/laserbrain/raspberry-pi-ad-da-board-library-for-window-10-iot-core-c8cc34 "www.hackster.io")
