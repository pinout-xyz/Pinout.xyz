<!--
---
name: WiringPi
class: interface
type: pinout
url: http://wiringpi.com/
page_url: wiringpi
pin:
  '3':
    name: WiringPi 8
  '5':
    name: WiringPi 9
  '7':
    name: WiringPi 7
  '8':
    name: WiringPi 15
  '10':
    name: WiringPi 16
  '11':
    name: WiringPi 0
  '12':
    name: WiringPi 1
  '13':
    name: WiringPi 2
  '15':
    name: WiringPi 3
  '16':
    name: WiringPi 4
  '18':
    name: WiringPi 5
  '19':
    name: WiringPi 12
  '21':
    name: WiringPi 13
  '22':
    name: WiringPi 6
  '23':
    name: WiringPi 14
  '24':
    name: WiringPi 10
  '26':
    name: WiringPi 11
  '29':
    name: WiringPi 21
  '31':
    name: WiringPi 22
  '32':
    name: WiringPi 26
  '33':
    name: WiringPi 23
  '35':
    name: WiringPi 24
  '36':
    name: WiringPi 27
  '37':
    name: WiringPi 25
  '38':
    name: WiringPi 28
  '40':
    name: WiringPi 29
-->
#WiringPi Bibliothek

###WiringPi is der Versuch die Einfachheit der VErdrahtung des Arduino auf den Raspberry Pi zu bringen.

Das Ziel dieser Bibliothek ist es, eine einzige gemeinsame Plattform und Programmierschnistelle für den Zugriff auf die
GPIOs des Rapsberry Pi für verschiedene Programmiersprachen zur VErfügung zu stellen.
Im Kern ist WiringPi eine C-Bibliothek, aber sie steht auch in Ruby und Python per "gem install wiringpi" bzw. "pip install wiringpi2" zur Verfügung.

Bei Python muss man auf die "2" am Ende achten - das ist die WiringPi2-Python Bibliothek, die momentan die aktuelle Version ist.

Mehr Informationen findest Du auf der offiziellen WiringPi-Webseite.

##Erste Schritte mit WiringPi

WiringPi benutzt seine eigene Nummerierung der Anschlüsse am Pi. Links siehst Du die entsprechende Nummerierung.
