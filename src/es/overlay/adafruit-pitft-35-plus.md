<!--
---
name: PiTFT Plus 3.5"
class: board
type: display
formfactor: Custom
manufacturer: Adafruit
description: A TFT Display for the Raspberry Pi
url: https://learn.adafruit.com/adafruit-pitft-3-dot-5-touch-screen-for-raspberry-pi
github: https://github.com/adafruit/Adafruit-PiTFT-3.5-Plus-PCB
schematic: https://learn.adafruit.com/assets/26348
buy: https://www.adafruit.com/products/2441
image: 'adafruit-pitft-35-plus.png'
pincount: 40
eeprom: setup
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
    name: Backlight Control
    mode: output
  '18':
    name: RT Interrupt
    mode: input
  '22':
    name: TFT Data/Command
    mode: output
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    name: TFT Chip Select
    mode: chipselect
  '26':
    name: RT Chip Select
    mode: chipselect
-->
#PiTFT Plus 3.5"

PiTFT+ cuenta con una pantalla de 3.5" y 480x320, pixel de colores de 16-bit e interfaz resistiva, creada específicamente para la Raspberry Pi 3, 2 y A+/B+.

La pantalla usa los pines SPI además de los GPIO #25 y #24, GPIO #18 puede ser utilizado para controlar la iluminación mediante PWM. Un conector GPIO clásico de 2x13 permite utilizar el resto de pines.

PiTFT+ puede utilizarse como pantalla para la interfaz X o el terminal. Además, permite conectar otra pantalla HDMI teniendo en cuenta que sólo una sesión X puede utilizarse de manera simultánea por lo que tendrás que elegir en qué pantalla. 
