<!--
---
name: Hyperpixel
class: board
type: display
formfactor: Custom
manufacturer: Pimoroni
description: A high-resolution 3.5" TFT display for the Raspberry Pi
url: https://shop.pimoroni.com/products/hyperpixel
github: https://github.com/pimoroni/hyperpixel
buy: https://shop.pimoroni.com/products/hyperpixel
image: 'hyperpixel.png'
pincount: 40
eeprom: no
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
  'bcm0':
    name: DPI Clock
  'bcm1':
    name: DPI EN
  'bcm2':
    name: DPI V-Sync
  'bcm3':
    name: DPI H-Sync
  'bcm4':
    name: Blue 2
  'bcm5':
    name: Blue 3
  'bcm6':
    name: Blue 4
  'bcm7':
    name: Blue 5
  'bcm8':
    name: Blue 6
  'bcm9':
    name: Blue 7
  'bcm12':
    name: Green 2
  'bcm13':
    name: Green 3
  'bcm14':
    name: Green 4
  'bcm15':
    name: Green 5
  'bcm16':
    name: Green 6
  'bcm17':
    name: Green 7
  'bcm20':
    name: Red 2
  'bcm21':
    name: Red 3
  'bcm22':
    name: Red 4
  'bcm23':
    name: Red 5
  'bcm24':
    name: Red 6
  'bcm25':
    name: Red 7
  'bcm10':
    name: Touch Data
    mode: i2c
  'bcm11':
    name: Touch Clock
    mode: i2c
  'bcm18':
    name: LCD Chip Select
    mode: output
  'bcm19':
    name: Backlight Control
    mode: output
  'bcm26':
    name: LCD Program Data
    mode: output
  'bcm27':
    name: Touch Interrupt
    mode: output
-->
# HyperPixel

HyperPixel es una pantalla 3.5" TFT de alta resolución para Raspberry Pi. Utiliza una interfaz DPI de alta velocidad, muestra imágenes a 60 FPS con una resolución de 270 píxeles por pulgada (800x480).

La pantalla es capaz de mostrar 18-bits de color (6 bits por color, modo DPI 6 - RGB666) y cuenta con capacidad multitáctil, más sensible que una pantalla resistiva.

HyperPixel es compatible con cualquier versión de 40 pines, incluyendo Pi Zero y Pi Zero W.
Dimensiones: 56.5x86x10mm (ancho-alto-profundidad, pines y pantalla incluidos).

Para poner a punto la pantalla puedes utilizar el instalador de una línea:

```bash
curl https://get.pimoroni.com/hyperpixel | bash
```

¡Y sigue las instrucciones!
