<!--
---
name: Expander Pi
class: board
type: adc, dac, io, rtc
formfactor: Custom
manufacturer: AB Electronics UK
description: 8 ADC inputs, 2 DAC outputs, 16 IO channels and a Real-Time Clock
url: https://www.abelectronics.co.uk/p/50/expander-pi
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-expander_pi.pdf
buy: https://www.abelectronics.co.uk/p/50/expander-pi
image: 'ab-expander-pi.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
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
    mode: spi
  '21':
    mode: spi
  '22':
    name: LDAC
    mode: output
    active: high
  '23':
    mode: spi
  '24':
    mode: spi
  '26':
    mode: spi
i2c:
  '0x20':
    name: MCP23017
    device: MCP23017
  '0x68':
    name: DS1307
    device: DS1307

-->
#Expander Pi

Expander Pi is a versatile digital and analogue expansion board.  It allows you to connect your Raspberry Pi to switches, lights, sensors, and many other devices giving you a way to communicate with the outside world.

##Features  

8 channel MCP3208 12-bit ADC with a maximum sample rate of 100 ksps and includes a 4.096 volt precision voltage reference.  
2 channel MCP4822 12-bit DAC with an internal voltage reference.  
16 digital I/O channels, using an MCP23017 16-bit I/O expander with a maximum input of 5 volts on each channel.
A Real Time Clock using a DS1307 RTC and a CR2032 battery to maintain the date and time when the main system power is not available.

Python, C, C++, Node.js and Windows 10 IOT libraries are available on GitHub.