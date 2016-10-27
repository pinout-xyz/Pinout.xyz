<!--
---
name: WiFi Pants
class: board
type: power, iot
formfactor: pHAT
manufacturer: SLNGadget
description: WiFi and battery power for the Raspberry Pi
url: https://hackaday.io/project/8678-rpi-wifi
github: https://github.com/al177/esp_hat
buy: https://www.tindie.com/products/ajlitt/wifi-power-pants/
image: 'wifi-pants.png'
pincount: 40
eeprom: no
power:
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
  '13':
    name: ESP GPIO10
  '15':
    name: ESP SCLK
  '16':
    name: ESP CSO
  '18':
    name: ESP MISO
  '22':
    name: ESP MOSI
  '27':
    name: ESP CH_PD
  '37':
    name: ESP GPIO9
-->
#WiFi Pants

WiFi Pants es una placa adicional para Raspberry Pi con WiFi y alimentación de 5V, basada en ESP-12F.

Encaja perfectamente con Pi Zero, pese a un pequeño saliente para la antena, y sólo necesita 6 puertos GPIO.

Se comunica a través de la interfaz SDIO para dar capacidades WiFi como alternativa a los adaptadores WiFi USB. Es útil para proyectos de poco ancho de banda, como la mayoría de los proyectos incrustados.

Lo más destacable, WiFI Pants añade WiFi a Pi Zero dejando libre el puerto USB y permite usar cualquier batería de hasta 3V ya que la aumenta a 5V y 2A para alimentar la Pi y otros periféricos.

Incluye un conector JST-PH compatible con las baterías de Sparkfun y Adafruit. Su mecanismo de seguridad evita la descarga más allá de 2.7V. Un interruptor permite a un microcontrolador encender o apagar la fuente de alimentación.

Además del interruptor, los 5 pines dan acceso al puerto serie de Raspberry Pi, ideal para proyectos IoT donde no hay pantalla pero es necesario acceso a terminal para la puesta a punto. Estos pines pueden conectarse a un cable FTDI USB-to-UART de 6 pines.

WiFi Pants también funciona perfectamente con Pi A+/B+/2.
