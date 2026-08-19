<!--
---
description: Una placa de control por joystick para el MeArm Pi
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
