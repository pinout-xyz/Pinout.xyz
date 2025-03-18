<!--
---
name: Audio Z
class: board
type: audio
formfactor: pHAT
manufacturer: Fe-Pi
description: A complete audio solution for the Raspberry Pi
url: http://fe-pi.com/products/fe-pi-audio-z-v1
buy: http://fe-pi.com/products/fe-pi-audio-z-v1
image: 'fepi-audio-z.png'
pincount: 40
eeprom: no
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
  '12':
    name: BCLK (Bit Clock)
    mode: i2s
  '35':
    name: LRCLK (Left/Right Clock)
    mode: i2s
  '38':
    name: DIN (Data In)
    mode: i2s
  '40':
    name: DOUT (Data Out)
    mode: i2s
i2c:
  '0x0a':
    name: SGTL5000
    device: SGTL5000XNAA3/R2
-->
# Audio Z

Fe-Pi Audio Z está diseñado para ser una solución completa de sonido y bajo coste para Raspberry Pi 2, 3 y Zero, proporciona entrada y salida de línea, salida de auriculares/entrada de micrófono.

## Especificaciones ##

* Tamaño pequeño, como Raspberry Pi Zero
* Jack para auricuales/micrófono de 3.5 mm y 4 contactos (negro)
* Jack para salida de línea estéreo de 3.5 mm (verde) y entrada estéreo (rosa)
* ADC > 90 dB SNR y -72 dB THD+N
* Salida de línea > 100 dB SNR y-85 dB THD+N
* Salida HP > 100 dB SNR y -80 dB THD+N, 62.5 mW máximo en 16 ohm
* Controles de hardware para el  volúmen de auriculares, líneas de entrada y salida, soporte ALSA
* Conector femenino de 2.54mm y 2x20 pines, conector masculino de 40 pines incluido
