<!--
---
name: WiringPi
class: interface
type: pinout
url: http://wiringpi.com
github: https://github.com/WiringPi/WiringPi2-Python
pincount: 40
pin:
  '3':
    name: WiringPi 8
  '5':
    name: WiringPi 9
  '7':
    name: WiringPi 7
  '8':
    name: WiringPi 15
  '10':
    name: WiringPi 16
  '11':
    name: WiringPi 0
  '12':
    name: WiringPi 1
  '13':
    name: WiringPi 2
  '15':
    name: WiringPi 3
  '16':
    name: WiringPi 4
  '18':
    name: WiringPi 5
  '19':
    name: WiringPi 12
  '21':
    name: WiringPi 13
  '22':
    name: WiringPi 6
  '23':
    name: WiringPi 14
  '24':
    name: WiringPi 10
  '26':
    name: WiringPi 11
  '29':
    name: WiringPi 21
  '31':
    name: WiringPi 22
  '32':
    name: WiringPi 26
  '33':
    name: WiringPi 23
  '35':
    name: WiringPi 24
  '36':
    name: WiringPi 27
  '37':
    name: WiringPi 25
  '38':
    name: WiringPi 28
  '40':
    name: WiringPi 29
-->
#WiFi Pants

WiFi Pants es una placa adicional para Raspberry Pi con WiFi y alimentación de 5V, basada en ESP-12F.

Encaja perfectamente con Pi Zero, pese a un pequeño saliente para la antena, y sólo necesita 6 puertos GPIO.

Se comunica a través de la interfaz SDIO para dar capacidades WiFi como alternativa a los adaptadores WiFi USB. Es útil para proyectos de poco ancho de banda, como la mayoría de los proyectos incrustados.

Lo más destacable, WiFI Pants añade WiFi a Pi Zero dejando libre el puerto USB y permite usar cualquier batería de hasta 3V ya que la aumenta a 5V y 2A para alimentar la Pi y otros periféricos.

Incluye un conector JST-PH compatible con las baterías de Sparkfun y Adafruit. Su mecanismo de seguridad evita la descarga más allá de 2.7V. Un interruptor permite a un microcontrolador encender o apagar la fuente de alimentación.

Además del interruptor, los 5 pines dan acceso al puerto serie de Raspberry Pi, ideal para proyectos IoT donde no hay pantalla pero es necesario acceso a terminal para la puesta a punto. Estos pines pueden conectarse a un cable FTDI USB-to-UART de 6 pines.

WiFi Pants también funciona perfectamente con Pi A+/B+/2.
