<!--
---
name: RASPIAUDIO AUDIO+ SPEAKERS+ MIC+
class: board
type: audio,io
formfactor: phat
manufacturer: RASPIAUDIO
description: An I2S digital to analog audio converter with 2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS and detachable ONBOARD I2S MICROPHONE
buy: https://raspiaudio.com
image: 'audioplus_speakerplus_micplus.png'
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
  '36':
    name: Google Driver
  '38':
    name: I2S D-In
  '40':
    name: I2S D-Out
install:
  'devices':
  - 'i2s'
-->
#Audio+ Speaker+ Microphone+
##2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS

* Experimenta con el asistente AIY de Google (compatible 100% pin a pin).

* Utiliza asistentes de código abierto como ADRIAN, proyecto SNIPS y otros

* Cambiador de voz

* Ideal para cualquier proyecto de radio portátil en el que necesite un altavoz integrado

* Enciende tu antiguo altavoz directamente

* No se requiere suministro de energía adicional

##Especificaciones:


1. Micrófono I2S Alta sensibilidad a bordo (se puede separar de la boad principal con el cable incluido)

2. Amplificador estéreo 2x5w y 2 altavoces integrados incluidos

3. Audio DAC I2 de 24 bits con calidad de muestreo de estudio

4. Conector de línea de 3,5 mm estéreo

5. Botón rojo incorporado, 1 estado led

6. Terminal de tornillo de extensión para altavoces externos (2 a 8 ohmios)

7. Terminal de tornillo de extensión para pulsador externo y led externo.

8. Cabezal hembra largo soldado 2x20 (NO se requiere soldadura) Compatible con Raspberry Pi 3, 2, B +, A + y Zero.

##Instalación:

Abre terminal y ejecuta los siguientes comandos:

```bash
sudo wget -O mic mic.raspiaudio.com

sudo bash mic
```
* Di sí para reiniciar
* En el próximo reinicio, debe ejecutar la prueba para finalizar la instalación (es una rareza de ALSA):

```bash
sudo wget -O test test.raspiaudio.com

sudo bash test
```


* Presione el botón de a bordo, debe escuchar "Delantero izquierdo" "Delantero derecho" luego la secuencia grabada por el micrófono.

* Si el volumen es demasiado bajo, puede ajustar la ganancia del micrófono reiniciando y escribiendo lo siguiente en un terminal:

```bash
alsamixer
```
