<!--
---
name: Pi Cap
class: board
type: touch, capacitive, audio
formfactor: Custom
manufacturer: Bare Conductive
description: Add capacitive touch, distance sensing and high quality audio to the Raspberry Pi
url: https://www.bareconductive.com/shop/pi-cap/
buy: https://www.bareconductive.com/shop/pi-cap/
image: 'pi-cap.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '7':
    name: Button
    mode: input
    active: low
  '11':
    name: IRQ
    mode: input
    active: low
  '29':
    name: Green LED
    mode: output
    active: low
  '31':
    name: Red LED
    mode: output
    active: low
  '32':
    name: PWM0
    mode: output
    active: high
  '33':
    name: PWM1
    mode: output
    active: high
  '37':
    name: Blue LED
    mode: output
    active: low
i2c:
  '0x5C':
    name: MPR121
    device: MPR121
-->
# Pi Cap

Pi Cap añade botones capacitivos precisos, sensores de distancia y sonido de gran calidad a cualquier Raspberry Pi con un conector de 40 pines GPIO. Los 12 electrodos pueden ser conectados a cualquier cosa que conduzca electricidad para crear una interfaz táctil o de proximidad. Además, Pi Cap incluye un LED RGB programable y un botón multifunción.

El software de Pi Cap está en repositorio oficial de Raspbian, por lo tanto para instalarlo simplemente:

```bash
sudo apt-get update
sudo apt-get dist-upgrade
```

Reinicia la Raspberry Pi y:
```bash
sudo apt-get install picap
picap-setup
```

Pi Cap proporciona 7 pines digitales I/O, en el conector de 40 pines de Raspberry Pi. Los pines: 12, 13, 15, 16, 18, 22, 36.
El paquete de Pi Cap contiene muchos ejemplos de código escritos en: C++, Python y Node.js.
