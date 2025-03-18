<!--
---
name: DPI TFT Kippah
class: board
type: display
formfactor: HAT
manufacturer: Adafruit
description: Run 40 pin TFT's of a Raspberry Pi
url: https://learn.adafruit.com/adafruit-dpi-display-kippah-ttl-tft
buy: https://www.adafruit.com/products/2453
image: adafruit-tft-kippah.png
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '9':
  '25':
  '39':
  '34':
  '30':
  '20':
  '14':
  '6':
pin:
  '3':
  '5':
  '7':
  '29':
  '31':
  '26':
  '24':
  '21':
  '19':
  '23':
  '32':
  '33':
  '8':
  '10':
  '36':
  '11':
  '12':
  '35':
  '38':
  '40':
-->
# DPI TFT Kippah

Esta placa parecida a un HAT permite, con una mínima configuración, conectar una pantalla TFT.

Lo negativo es que esta placa utiliza la mayoría de pines GPIO, del 2 al 21 incluidos. Por lo tanto, no podrás usar UART RX/TX (cable consola), I2C, I2C EEPROM o SPI hardware. Puedes usar los pines #22, #23, #24, #25, #26 and #27 y los puertos USB.

Otra desventaja es que sustituye la salida HDMI/NTSC, por lo que no podrás tener DPI y la salida HDMI al mismo tiempo, ni puedes cambiar entre ambas.

Además, PWM tampoco está disponible por lo que no tendrás un control preciso de la retroiluminación de la pantalla a menos que utilices un generador PWM externo con un 555 o algo similar.

Es el mismo diagrama de pines para la versión táctil y la no-táctil.

Para instalar sigue el tutorial de Adafruit.
