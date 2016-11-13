<!--
---
name: PiShield
class: board
type: adc
formfactor: Custom
manufacturer: Infusion Systems
description: 5V Analog to Digital Converter and 5V I2C level shifter
url: https://infusionsystems.com/pishield/
github: https://github.com/I-CubeX/PythonExamples
schematic: https://infusionsystems.com/pishield/?page_id=137
buy: https://infusionsystems.com/pishield/?page_id=8
image: 'icubex-pishield.png'
pincount: 26
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '20':
pin:
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
install:
  'devices':
    - 'spi'

-->
# PiShield

PiShield fabricado por I-CubeX es una interfaz de sensores de 5V con 8 canales de 10-bit ADC a través de SPI, además de proporcionar 5V para dispositivos I2C. La conversión desde/hacia 5V es proporcionada tanto para sensores analógicos como digitales.

Especificaciones:

- Diseñado para [I-CubeX Sensors](http://infusionsystems.com/catalog/index.php/cPath/24), pero funciona con cualquier sensor analógico de 5V a través del conector de 3 pines (VCC, SIG, GND).
- ADC a través del chip MCP3008, funciona con las librerías y aplicaciones actuales (incluido wiringPi)
- Admite hasta 8 sensores analógicos a través del conector de 3 pines y 4 sensores digitales a través de los conectores de 2x3 pines.
- Deja espacio para conectar otro conector de 26 pines en la parte superior.
