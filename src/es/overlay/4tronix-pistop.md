<!--
---
name: Pi Stop
class: board
type: led
formfactor: Otro
manufacturer: 4tronix
description: LED Traffic Lights for Raspberry Pi
url: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=390
buy: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=390
image: '4tronix-pistop.png'
pincount: 4
eeprom: no
ground:
  '9':
pin:
  '11':
    name: Green
    mode: output
    active: high
  '13':
    name: Amber
    mode: output
    active: high
  '15':
    name: Red
    mode: output
    active: high
-->
#Pi Stop Traffic Lights

PiStop se conecta verticalmente a los pines GPIO y puede y puede colocarse en distintas posiciones. Sirve tanto para 26 pines como para 40.

PiStop sólo utiliza 3 pines GPIO, además de tierra, por lo que puedes conectar varios PiStops simultáneamente aunque no en cualquier posición ya que algunos pines se solaparían. Pese a que en el diagrama sólo se muestra una opción, cualquier sucesión de 3 pines GPIO cerca de tierra es susceptible de ser válida.  
