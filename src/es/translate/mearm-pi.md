<!--
---
name: MeArm Pi
class: board
type: other
formfactor: HAT
manufacturer: Mime Industries
collected: Other
description: Una placa de control por joystick para el MeArm Pi
url: https://mime.co.uk
github: https://github.com/mimeindustries/mearm-pi-hat-pcb
schematic: http://learn.mime.co.uk/assets/mearm-pi-hat-schematic-v1.4.pdf
buy: https://shop.mime.co.uk
image: 'mearm-pi.png'
pincount: 40
eeprom: yes
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
  '7':
    name: Base Servo
    mode: output
    active: high
  '11':
    name: Right Servo
    mode: output
    active: high
  '15':
    name: Left Servo
    mode: output
    active: high
  '19':
    name: Grip Servo
    mode: output
    active: high
  '23':
    name: RGB LED - green
    mode: output
    active: high
  '24':
    name: RGB LED - red
    mode: output
    active: high
  '26':
    name: RGB LED - blue
    mode: output
    active: high
  '29':
    name: Button 1
    mode: input
    active: high
  '31':
    name: Button 2
    mode: input
    active: high
i2c:
  '0x48':
    name: Joysticks
    device: PCF8591 ADC
-->
# MeArm Pi HAT

### El MeArm Pi HAT es una placa controladora de joystick para el kit de brazo robótico MeArm Pi

El MeArm Pi HAT proporciona lo siguiente:

 * Un ADC I2C de 8 bits (dirección 0x48) conectado a dos joysticks analógicos
 * Acceso a los pulsadores de los joysticks en el GPIO
 * Un LED RGB para salida
 * Un puerto de 6 pines para conectar los servos del brazo

La alimentación se puede suministrar a la Pi a través del HAT o directamente a la Pi, pero los servos solo se alimentan a través del HAT para no sobrecargar la fuente de alimentación de la Pi.

El pinout del conector de 6 pines es:

<table>
  <tr>
    <td>+5v</td>
    <td>Servo izquierdo</td>
    <td>Servo de la pinza</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>Servo de la base</td>
    <td>Servo derecho</td>
  </tr>
</table>

Además, las líneas I2C y de alimentación se llevan a un conector para facilitar la expansión, con el siguiente pinout de arriba a abajo:

1. SDA
2. 3V3
3. SCL
4. GND
