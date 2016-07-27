<!--
---
name: "Pi-DAC+"
class: board
type: tous
manufacturer: IQaudIO
buy: http://www.iqaudio.co.uk
description: Convertisseur numérique-analogique pour la Raspberry Pi
install:
  'devices':
    - 'i2c'
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: I2S
  '15':
    name: silence
    description: pour le Pi-AMP+ (option) 
  '16':
    name: encodeur rotatif
    description: (option) 
  '18':
    name: encodeur rotatif
    description: (option)
  '22':
    name: capteur IR
    description: (option) 
  '35':
    name: I2S
  '38':
    name: I2S
  '40':
    name: I2S
-->
#IQaudIO Pi-DAC+

Le Pi-DAC+ permet de convertir le signal audio numérique I2S de la Raspi en analogique, à l'aide de son CDA Texas Instrument PCM5122 et sorties phono. Il comprend aussi un pre-ampli pour sortie casque Texas Instrument TPA6133A.

La broche GPIO22 peut être utilisée pour couper le volume de l'ampli optionnel Pi-AMP+ rapidement (fonction mute/silence).

De même la broche GPIO25 peut être utilisée pour la lecture d'un capteur IR, et les broches GPIO23/24 pour celle d'un encodeur rotatif. Ces composants sont des options à souder sur la carte en elle-même.

Note: Les broches réservées à ces options peuvent être utilisées pour d'autres applications du moment qu'elles n'ont pas été activées programmatiquement pour leur fonction Pi-DAC.