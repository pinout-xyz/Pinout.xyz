<!--
---
name: AIY Voice Bonnet
class: board
type: audio,sensor
formfactor: pHAT
manufacturer: Google
description: A pHAT that helps you build an intelligent speaker with voice recognition that connects to the Google Assistant
url: https://aiyprojects.withgoogle.com/voice
github: https://github.com/google/aiyprojects-raspbian
image: 'aiy-voice-bonnet.png'
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
  '8':
    mode: uart
    name: TXD breakout
  '10':
    mode: uart
    name: RXD breakout
  '12':
    mode: i2s
    name: I2S BCLK
  '16':
    mode: gpio
    name: Button
  '33':
    mode: i2s
    name: I2S LRCLK
  '38':
    mode: i2s
    name: I2S SDIN
  '40':
    mode: i2s
    name: I2S SDOUT
-->
# AIY Voice Bonnet

El AIY Voice Bonnet biene con el kit de voz AIY V2 de Google para hacer un altavoz inteligente al conectarse a la Raspberry Pi. Puede crearse un procesar de lenguaje natural que responda a tu voz y se conecte al Asistente de Google.

El bonnet incluye hardware para facilitar la captura y reproducción de audio, conexiones de audio estéreo, un conector de auriculares jack, un conector de botones de 8 pines, pines UART y 4 GPIO únicos llamados `PIN_A`, `PIN_B`, `PIN_C`, y `PIN_D`.

**Nota:** si tienes la versión V1 ve: [Voice Hat](/pinout/voice_hat), que es la versión de tamaño completo.
