# PiShield

PiShield fabricado por I-CubeX es una interfaz de sensores de 5V con 8 canales de 10-bit ADC a través de SPI, además de proporcionar 5V para dispositivos I2C. La conversión desde/hacia 5V es proporcionada tanto para sensores analógicos como digitales.

Especificaciones:

- Diseñado para [I-CubeX Sensors](http://infusionsystems.com/catalog/index.php/cPath/24), pero funciona con cualquier sensor analógico de 5V a través del conector de 3 pines (VCC, SIG, GND).
- ADC a través del chip MCP3008, funciona con las librerías y aplicaciones actuales (incluido wiringPi)
- Admite hasta 8 sensores analógicos a través del conector de 3 pines y 4 sensores digitales a través de los conectores de 2x3 pines.
- Deja espacio para conectar otro conector de 26 pines en la parte superior.
