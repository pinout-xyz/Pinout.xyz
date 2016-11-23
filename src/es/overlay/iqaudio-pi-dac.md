<!--
---
name: "Pi-DAC+"
class: board
type: audio
formfactor: HAT
manufacturer: IQaudIO
description: Un HAT I2S conversor de audio digital a analógico
url: http://www.iqaudio.co.uk/audio/8-pi-dac-0712411999650.html
buy: http://www.iqaudio.co.uk
image: 'iqaudio-pi-dac.png'
pincount: 40
eeprom: yes
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: I2S
  '15':
    name: Mutear/Desmutear
    description: Solo Pi-AMP+ (opcional)
  '16':
    name: Codificador rotatorio
    description: (opcional)
  '18':
    name: Codificador rotatorio
    description: (opcional)
  '22':
    name: Sensor de infrarrojos
    description: (opcional)
  '35':
    name: I2S
  '38':
    name: I2S
  '40':
    name: I2S
-->
#IQaudIO Pi-DAC+

El Pi-DAC+ coge las señales de audio digital (I2S) de la Raspberry Pi y a través del
DAC PCM5122 de Texas Instruments proporciona una salida variable (control de volumen por hardware)
de audio analógico a los conectores Phono del Pi-DAC+. Además, el Pi-DAC+, por medio del
amplificador de auriculares TPA6133A, soporta el uso directo de cascos o auriculares por medio
de la toma jack de 3.5mm.

El Pi-DAC+ usa el GPIO 22 para mutear/desmutear el Pi-AMP+.

Puedes usar el GPIO 25 para conectar un sensor de infrarrojos y los GPIO's 23 y 24 para un
codificador rotatorio. Ambas piezas son opcionales.

Nota: los pines marcados como opcionales pueden usarse con propósito general si esos add-ons no están
habilitados por software.
