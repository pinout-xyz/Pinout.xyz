<!--
---
name: Pi-DigiAMP+
class: board
type: audio
formfactor: HAT
manufacturer: IQaudIO
description: A combined DAC and 35w amplifier board
url: http://www.iqaudio.co.uk/home/9-pi-digiamp-0712411999650.html
buy: http://www.iqaudio.co.uk
image: 'iqaudio-pi-digiamp.png'
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
  '12':
    name: I2S
  '15':
    name: Mute/Unmute
  '16':
    name: Rotary Encoder
    description: (optional)
  '18':
    name: Rotary Encoder
    description: (optional)
  '22':
    name: IR Sensor
    description: (optional)
  '35':
    name: I2S
  '38':
    name: I2S
  '40':
    name: I2S
install:
  'devices':
  - 'i2c'
-->
#Pi-DigiAMP+

Pi-DigiAMP+ es una placa adicional que incluye un conversor digital a anlógico (DAC) y un potente amplificador estéreo de 35w. Si quieres convertir tu Raspberry Pi en una minicadena con audio estéreo de Alta Fidelidad, simplemente añade altavoces.

Puedes utilizar GPIO25 para añadir un sensor infrarrojo y GPIO23/24 para un dial. Estas dos partes son opcionales pero están disponibles en Pi-DAC9 para un acceso fácil.
Nota: los pines reservados para el dia y el sensor infrarrojo se pueden utilizar para otros propósitos si estos dos componentes no se han añadido y activado mediante software.
