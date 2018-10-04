<!--
---
name: RASPIAUDIO AUDIO+ SPEAKERS+
class: board
type: audio,io
formfactor: phat
manufacturer: RASPIAUDIO
description: An I2S digital to analog audio converter with 2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS
buy: https://raspiaudio.com
image: 'audioplus_speakerplus.png'
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
  '12':
    name: I2S Clock
  '16':
    name: Button
    mode: input
    active: low
  '22':
    name: LED
    mode: output
    active: high
  '35':
    name: I2S WS
  '40':
    name: I2S Data
install:
  'devices':
  - 'i2s'
-->
#Audio+ Speaker+
##2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS


* Ideal para cualquier proyecto de radio portátil donde necesite un altavoz integrado

* Potencia tu antiguo altavoz directamente

* No requiere fuente de alimentación adicional

##Especificaciones:


(No hay micrófono en esta placa, para un micrófono vea nuestro otro modelo MIC +)

1. Altavoz a bordo 2x5w Stereo Amplification 2 incluido

2. Audio DAC I2s de 24 bits con calidad de muestreo de estudio

3. Salida de línea estéreo de 3,5 mm

4. Botón rojo a bordo, 1 estado llevado

5. Terminal de tornillo de extensión para altavoces externos (2 a 8 ohmios)

6. Terminal de tornillo de extensión para pulsador externo, led externo.

7. Cabezal hembra larga soldada 2x20 (no se requiere soldadura) Compatible con Raspberry Pi 3, 2, B +, A + y Zero

##Instalación para usuarios de Raspbian:

* Abre terminal y ejecuta los siguientes comandos:

```bash
sudo wget -O - script.raspiaudio.com | bash
```


* Di sí al reinicio

* En el próximo reinicio tienes que ejecutar la prueba para finalizar la instalación (es una rareza de ALSA):

```bash
sudo speaker-test -l5 -c2 -t wav
```

* Reinicie nuevamente y podrá controlar el volumen desde su escritorio o mediante la herramienta de línea de comandos `alsamixer`
