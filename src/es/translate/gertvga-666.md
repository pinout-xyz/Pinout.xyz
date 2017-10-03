<!--
---
name: GertVGA 666
class: board
type: other
formfactor: Custom
manufacturer: Pi Supply
description: The Gert VGA 666 is a breakout/add on board for the Raspberry Pi for using a VGA monitor.
url: https://www.kickstarter.com/projects/pisupply/gert-vga-666-kit-hardware-vga-for-raspberry-pi
github: https://github.com/PiSupply/Gert-VGA-666
schematic: https://github.com/fenlogic/vga666/blob/master/documents/vga_manual.pdf
buy: https://www.pi-supply.com/product/gert-vga-666-hardware-vga-raspberry-pi/
image: 'gertvga-666.png'
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
  '3':
    name: V-SYNC
  '5':
    name: H-SYNC
  '7':
    name: Blue 2
  '8':
    name: Green 6
  '10':
    name: Green 7
  '11':
    name: Red 3
  '12':
    name: Red 4
  '19':
    name: Green 2
  '21':
    name: Blue 7
  '23':
    name: Green 3
  '24':
    name: Blue 6
  '26':
    name: Blue 5
  '29':
    name: Blue 3
  '31':
    name: Blue 4
  '32':
    name: Green 4
  '33':
    name: Green 5
  '35':
    name: Red 5
  '36':
    name: Red 2
  '38':
    name: Red 6
  '40':
    name: Red 7
-->
# GertVGA 666

Gert VGA 666 (6 bits por canal de color, por lo tanto 666) es una placa añadida para Raspberry Pi. El diseño es abierto, publicado por Gert van Loo.

Es una solución para utilizar una pantalla VGA con tu Raspberry Pi y es bastante más barata  que un adaptador HDMI a VGA. La conexión VGA es controlada de manera nativa a través de los pines GPIO (interfaz paralela) y utiliza aproximadamente la misma carga de CPU que la conexión HDMI de Raspberry Pi. Es capaz de mostrar video 1080p60 sin carga de CPU. 
