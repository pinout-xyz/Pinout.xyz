<!--
---
name: DPI
class: interface
type: pinout
description: Raspberry Pi DPI pins
url: https://www.raspberrypi.org/documentation/hardware/raspberrypi/dpi/
pin:
  'bcm0':
    name: CLK
  'bcm1':
    name: DEN
  'bcm2':
    name: V-SYNC
  'bcm3':
    name: H-SYNC
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
  'bcm10':
    name: Green 2
  'bcm11':
    name: Green 3
  'bcm12':
    name: Green 4
  'bcm13':
    name: Green 5
  'bcm14':
    name: Green 6
  'bcm15':
    name: Green 7
  'bcm16':
    name: Red 2
  'bcm17':
    name: Red 3
  'bcm18':
    name: Red 4
  'bcm19':
    name: Red 5
  'bcm20':
    name: Red 6
  'bcm21':
    name: Red 7
-->
#DPI - Display Parallel Interface

DPI (interfaz de muestra paralela) es una interfaz paralela de 24-bit con 28 relojes y señales de sincronización. La Pi utiliza una versión reducidad de 6-bit, 22 pines, omitiendo los bits de color R, G y B menos significantes.

DPI, combinada con un simple adaptador formado por 20 resitencias, permite añadir un conector VGA a la Raspberry Pi que soporta resoluciones desde 640 x 480 hasta 1920 x 1024 a 60fps y 6bits por canal.
