<!--
---
name: Fe-Pi Audio Z V2
class: board
type: audio
formfactor: pHAT
manufacturer: Fe-Pi
description: A complete audio solution for the Raspberry Pi
url: https://fe-pi.com/products/fe-pi-audio-z-v2
buy: https://fe-pi.com/products/fe-pi-audio-z-v2
image: 'fepi-audio-z-V2.png'
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
#Fe-Pi Audio Z V2

Fe-Pi Audio Z V2 está diseñado para proporcionar una solución de audio completa de bajo coste para Raspberry Pi 2, 3 y Zero, que necesitan altavoces de entrada de línea, salida de línea, salida de auriculares / entrada de micrófono y estéreo.

## Características ##

* Tamaño Raspberry Pi Zero
* Codec estéreo de baja potencia SGTL5000.
* 3.5 mm, 4 contactos, conector para auriculares / micrófono (negro).
* Jack de 3.5 mm para Line Out estéreo (verde), y Line Line estéreo (rosa).
* ADC> 90 dB SNR y -72 dB THD + N
* Salida de línea> 100 dB SNR y -85 dB THD + N
* Salida de HP> 100 dB SNR y -80 dB THD + N, 62.5 mW máx. A 16 ohmios.
* Controles de nivel de hardware para volumen de auriculares, entrada de línea, salida de línea. Apoyo ALSA.
* Incluye 2x20pin 2.54mm de cabecera hembra y 40pin de cabeza rompible masculina.
* Conexión RCA opcional para salida de video compuesto cuando se usa con Raspberry Pi Zero.
