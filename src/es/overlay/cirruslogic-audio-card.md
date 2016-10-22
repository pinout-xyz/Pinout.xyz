<!--
---
name: Cirrus Logic Audio Card
class: board
type: audio
formfactor: HAT
manufacturer: Element14
description: Audio Card with unprecedented level of features and performance for Raspberry Pi
url: http://www.element14.com/community/community/raspberry-pi/raspberry-pi-accessories/cirrus_logic_audio_card
buy: http://www.element14.com/community/community/raspberry-pi/raspberry-pi-accessories/cirrus_logic_audio_card
image: 'cirruslogic-audio-card.png'
pincount: 40
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
    name: SDA1
    mode: i2c
    description: WM8804 I2C - SDA
  '5':
    name: SCL1
    mode: i2c
    description: WM8804 I2C - SCLK
  '11':
    name: GPIO_GEN0
    mode: input
    description: WM5102 RST
  '12':
    name: PCM_CLK
    mode: input
    description: WM5102 AIF PCM - BCLK
  '15':
    name: GPIO_GEN3
    mode: input
    description: WM5102 LDO Enable
  '16':
    name: GPIO_GEN4
    mode: input
    description: WM8804 Control I/F Config
  '19':
    name: SPI_MOSI
    mode: spi
    description: WM5102 SPI - MOSI
  '21':
    name: SPI_MISO
    mode: spi
    description: WM5102 SPI - MISO
  '23':
    name: SPI_SCLK
    mode: spi
    description: WM5102 SPI - SCLK1
  '24':
    name: SPI_CE0_N
    mode: input
    description: WM8804 RST
  '26':
    name: SPI_CE1_N
    mode: input
    description: WM5102 SPI - CE
  '35':
    name: PCM_FS
    mode: input
    description: WM5102 AIF PCM - FS
  '38':
    name: PCM_DIN
    mode: input
    description: WM5102 AIF PCM - DIN
  '40':
    name: PCM_DOUT
    mode: input
    description: WM5102 AIF PCM - DOUT
-->
#Cirrus Logic Audio Card

###Ofrece una gran variedad de especificaciones, perfecta para los audiófilos más entusiastas que quieren utilizar su Raspberry Pi para aplicaciones de audio.

* Capaz de reproducir audio de alta definición (HD), a 24-bit, 192khz
* Puerto jack de 4 polos y 3.5 mm para conectar un conjunto de auriculares/micrófono para jugar o VoIP
* Incluye dos micrófonos DMIC para grabar audio estéreo
* Jack de 3.5 mm para conectar una entrada estéreo que permita grabar audio de gran calidad
* Jack de 3.5 mm para conectar una salida estéreo como altavoces o amplificadores
* Entrada y salida estéreo digital (SPDIF)
