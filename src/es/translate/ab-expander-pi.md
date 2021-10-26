<!--
---
name: Expander Pi
class: board
type: adc, dac, io, rtc
formfactor: HAT
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

Expander Pi es una placa de expansión digital y analógica versátil. Le permite conectar su Raspberry Pi a interruptores, luces, sensores y muchos otros dispositivos, lo que le permite comunicarse con el mundo exterior.

##Características

ADC de 8 bits MCP3208 de 12 bits con una frecuencia de muestreo máxima de 100 ksps e incluye una referencia de voltaje de precisión de 4.096 voltios.
2 canales MCP4822 DAC de 12 bits con una referencia de voltaje interno.
16 canales de E / S digitales, utilizando un expansor de E / S de 16 bits MCP23017 con una entrada máxima de 5 voltios en cada canal.
Un reloj de tiempo real que utiliza un RTC DS1307 y una batería CR2032 para mantener la fecha y la hora cuando la alimentación del sistema principal no está disponible.

Python, C, C ++, Node.js y las bibliotecas IOT de Windows 10 están disponibles en GitHub.
