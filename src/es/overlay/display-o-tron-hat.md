<!--
---
name: Display-o-Tron HAT
class: board
type: todas
formfactor: HAT
manufacturer: Pimoroni
image: 'image.png'
url: https://github.com/pimoroni/dot3k
description: Una pantalla LCD de 3 líneas con luz RGB con 6 zonas y 6 botones táctiles
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '22':
    name: LCD CMD/DATA
    mode: salida
    active: alto (encendido)
  '19':
    mode: spi
  '22':
    name: Selector de Registro LCD
    mode: salida
  '23':
    mode: spi
  '24':
    name: Selector de Chip LCD
    mode: chipselect
    active: alto (encendido)
  '32':
    name: LCD Reset
    mode: salida
    active: low
-->
#Display-o-Tron HAT

El HAT Display-o-Tron usa tanto SPI como I2c para hacer funcionar la pantalla LCD, retroiluminación y botones táctiles.
Aún así ambos buses pueden ser compartidos con otros dispositivos

Puedes usar la siguiente línea para instalar, preparar y dejar listo para el uso el Display-o-Tron 3000:

```bash
curl -sS get.pimoroni.com/dot3k | bash
```

¡Y sigue las instrucciones!
