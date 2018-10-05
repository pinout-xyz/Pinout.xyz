<!--
---
name: Fe-Pi Audio Card
class: board
type: audio
formfactor: HAT
manufacturer: Fe-Pi
description: A complete audio solution for the Raspberry Pi
url: https://fe-pi.com/products/fe-pi-audio-v1
buy: https://fe-pi.com/products/fe-pi-audio-v1
image: 'fepi-audio.png'
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
#Audio Z

Fe-Pi Audio está diseñado para proporcionar una solución de audio completa de bajo costo para Raspberry Pi 2, 3 y Zero, que necesitan altavoces de entrada de línea, salida de línea, salida de auriculares / entrada de micrófono y estéreo.

## Características ##

* Los pads SPI, UART e I2C de 2.54 mm (.100) están disponibles para uso externo.
* Tamaño Raspberry Pi 2, 3.
* Codec estéreo de baja potencia SGTL5000.
* 3.5 mm, 4 contactos, conector para auriculares / micrófono (negro).
* Conectores RCA para entrada de línea estéreo y salida de línea.
* Terminal de tornillo de 4 pines para salida de altavoz.
* Como mínimo, se recomienda una fuente de alimentación de 3 amperios para la Raspberry Pi, si se utilizan altavoces.
* ADC> 90 dB SNR y -72 dB THD + N
* Salida de línea> 100 dB SNR y -85 dB THD + N
* Salida de HP> 100 dB SNR y -80 dB THD + N, 62.5 mW máx. A 16 ohmios.
* Salida de altavoz> 1.4W por canal, en 8 ohms.
* Controles de nivel de hardware para volumen de auriculares, entrada de línea, salida de línea. Apoyo ALSA.
* 2x20pin 2.54mm conector hembra incluído.
