<!--
---
name: ZeroBorg
class: board
type: motor
formfactor: Custom
manufacturer: PiBorg
description: A PiZero robot controller
url: https://www.piborg.org/zeroborg
buy: https://www.piborg.org/zeroborg
image: 'piborg-zeroborg.png'
pincount: 6
eeprom: no
power:
  '1':
  '2':
  '4':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
-->
#ZeroBorg

ZeroBorg fabricado por PiBorg es un controlador de motores de 4 canales para Raspberry Pi Zero.

Compatible con direcciones i2c esclavas configurables desde 3 (0x03) a 119 (0x77), por lo que aunque use i2c puede utilizarse con otras placas i2c. Echa un vistazo a la sección "Multiple Boards" de la guía de instalación de ZeroBorg para más detalles.

* 4 H-Brige completos
* Controla 4 motores o 2 motores paso a paso
* Picos de 2A o 1.5A RMS por brige
* Fusible de 5A
* Diseñada para funcionar con 9V
* 2 entradas analógicas
* Comunicación i2c
