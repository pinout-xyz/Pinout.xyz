<!--
---
name: Zero2Go
class: board
type: power
formfactor: pHAT
manufacturer: UUGear
description: Wide Input Range Power Supply for Raspberry Pi
url: http://www.uugear.com/product/zero2go/
buy: http://www.uugear.com/product/zero2go/
image: 'uugear-zero2go.png'
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
  '7':
    name: HALT
    mode: input
-->
# Zero2Go

Zero2Go es una fuente de alimentación de tamaño de Pi Zero que acepta entrada DC 5~26V y salida de 5V/2.6A máximo. Permite encender/apagar tu Raspberry Pi (Zero u otros modelos) con un solo toque.

Puede conectarse a Raspberry Pi Zero sin soldaduras, gracias a los pines pogo. Además, puede utilizarse con cualquier Raspberry Pi de 40 pines, incluyendo A+, B+, 2B y 3B.

Puedes utilizar estos dos comandos para instalar el software para Zero2Go:

```bash
wget http://www.uugear.com/repo/Zero2Go/installZero2Go.sh
sudo sh installZero2Go.sh
```

Tras la instalación, reinicia tu Raspberry Pi y tu Zero2Go estará listo.
