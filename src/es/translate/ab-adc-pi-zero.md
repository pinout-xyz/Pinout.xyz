<!--
---
name: ADC Pi Zero
class: board
type: adc
formfactor: pHAT
manufacturer: AB Electronics
description: 8 channel Analogue to Digital Converter
url: https://www.abelectronics.co.uk/p/69/ADC-Pi-Zero-Raspberry-Pi-Analogue-to-Digital-converter
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/69/ADC-Pi-Zero-Raspberry-Pi-Analogue-to-Digital-converter
image: 'ab-adc-pi-zero.png'
pincount: 40
eeprom: no
power: 3v3,5v
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x68':
    name: MCP3424
    device: MCP3424
  '0x69':
    name: MCP3424
    device: MCP3424
-->
#ADC Pi Zero

ADC Pi Zero es un conversor de 17 bit analógico a digital de 8 canales, diseñado para funcionar con Raspberry Pi Zero. ADC Differential Pi está basado en dos microchip conversores MCP3424 A/D, cada uno de ellos con 4 entradas analógicas. MCP3424 es un conversor A/D delta-sigma con entradas con bajo ruido diferencial.

##Especifiaciones

- 8 x 17-bit entradas únicas de 0 a 5 V
- Control mediante el puerto I2C de Raspberry Pi
- Acopla hasta cuatro placas en una sola Raspberry Pi
- Selección de dirección I2C
- Puerto I2C de 5V regulable
- Basado en MCP3424 de Microchip Technologies Inc
- Rango único de 5 V
- Voltaje de refrencia 2.048V (Precisión  ± 0.05%, Desvío: 15 ppm/°C)
- Amplificador de ganancia programable (PGA): ganancia de 1, 2, 4 or 8
- Velocidad de datos programable:
   - 3.75 SPS (17 bits)
   - 15 SPS (15 bits)
   - 60 SPS (13 bits)
   - 240 SPS (11 bits)
- Conversión única o continua

Librerías Arduino, C, Windows 10 IOT, Python 2 and Python 3 disponibles en GitHub.
