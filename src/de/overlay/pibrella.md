<!--
---
name: Pibrella
class: board
type: multi,io
formfactor: Custom
manufacturer: Cyntech
description: eine "Alles-in-Einem" Licht, Ton, Ein- und Ausgabe Erweiterungsplatine.
url: http://pibrella.com
github: https://github.com/pimoroni/pibrella
buy: https://shop.cyntech.co.uk/products/pibrella?variant=581387897
image: 'pibrella.png'
pincount: 26
eeprom: no
pin:
  '7':
    name: Green LED
    direction: output
    active: high
  '11':
    name: Yellow LED
    direction: output
    active: high
  '12':
    name: Buzzer
    direction: output
    active: high
  '13':
    name: Red LED
    direction: output
    active: high
  '15':
    name: Output A
    direction: output
    active: high
  '16':
    name: Output B
    direction: output
    active: high
  '18':
    name: Output C
    direction: output
    active: high
  '19':
    name: Input D
    direction: output
    active: high
  '21':
    name: Input A
    direction: input
    active: high
  '22':
    name: Output D
    direction: output
    active: high
  '23':
    name: Button
    direction: input
    active: high
  '24':
    name: Input C
    direction: input
    active: high
  '26':
    name: Input B
    direction: input
    active: high
-->
#Pibrella

Die "Alles-in-Einem" Licht, Ton, Ein- und Ausgabe Erweiterungsplatine von Pimoroni vs Cyntech 
benutzt jede Menge I/O Anschlüsse des Pi aber lässt die serielle Schnittstelle und den I2C-Bus noch frei und somit viel Raum für creative Erweiterungen!

Pibrella is einfach zu benutzen - einfach das entsprechende Modul über die Kommandozeile installieren:

```bash
sudo apt-get install python-pip
sudo pip install pibrella
```

... dann die Library in Dein Python-Skript importieren und anfangen zu basteln:

```bash
import pibrella
pibrella.light.red.on()
```