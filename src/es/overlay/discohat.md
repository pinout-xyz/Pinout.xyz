<!--
---
name: DiscoHAT
class: board
type: audio
formfactor: HAT
manufacturer: Kertatuote
description: Computer controlled DMX lights, sounds and special effects
url: http://discohat.com
buy: http://discohat.com/shop
image: 'discohat.png'
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
  '8':
    name: TXD
    active: high
    mode: output
    description: DMX out
  '13':
    name: Button1
    active: low
    mode: input
    description: Button 1
  '15':
    name: Button2
    active: low
    mode: input
    description: Button 2
  '22':
    name: Button3
    active: low
    mode: input
    description: Button 3
  '18':
    name: Button4
    active: low
    mode: input
    description: Button 4
  '16':
    name: Button5
    active: low
    mode: input
    description: Button 5
  '37':
    name: Button6
    active: low
    mode: input
    description: Button 6
  '32':
    name: Button7
    active: low
    mode: input
    description: Button 7
  '36':
    name: Button8
    active: low
    mode: input
    description: Button 8
  '19':
    name: MOSI
    mode: spi
    description: LED strip data
  '23':
    name: SCLK
    mode: spi
    description: LED strip clock
-->
#DiscoHAT

###DiscoHAT es una pequeña placa que permtie controlar por ordenador luces, sonidos y efectos especiales.

Es una pieza esencial para hacer sistemas de luz y sonido personalizados. Puedes crear fácilmente tu propia discoteca. Es también útil para pequeños grupos de teatro, grupos de música o proyectos escolares.

Con DiscoHAT puedes controlar equipos DMX y tiras LED. También tiene interfaz para hasta 8 botones que pueden configurarse para iniciar secuencias de luz y sonido.

DiscoHAT fue creado para utilizarse con QLC+ un sotware libre de control de luz y sonido que es increíble. Los botones pueden alternar entre luces fijas, luces siguiendo un patrón o luces sincronizadas con la música, sin necesidad de pantallas, teclados o ratón. Con una antena WiFi se pueden controlar las luces desde una tablet o smartphone.

Debido a su potencia, se recomiendan Raspberry Pi 2 modelo B o superior. También se puede utilizar con Raspberry Pi de 26 pines pero se pierde el formato HAT y 4 botoenes. Los conectores no están soldados, utiliza SMD a través de los pines.

DiscoHAT está siendo utilizado por su creador en sus funciones de teatro. La salida DMX y los botoenes están aislados ópticamente y protegidos por ESD para evitar descargas electrostáticas debidas a cables largos, aire caliente, superficies de plástico o ropa de nylon.
