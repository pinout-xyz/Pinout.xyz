<!--
---
name: UART
class: interface
type: pinout
description: Raspberry Pi UART Anschlüsse
url: http://elinux.org/RPi_Serial_Connection
pin:
  '8':
    name: TXD / Senden
    direction: output
    active: high
  '10':
    name: RXD / Empfangen
    direction: input
    active: high
-->
#UART - Universal Asynchronous Receiver/Transmitter (serielle Schnittstelle)

###Die beiden UART Anschlüsse sind in WiringPi 15 und 16

UART ist eine einfache und nützliche Schnittstelle um einen Arduino (oder vorbereiteten ATmega) mit Deinem Pi zu verbinden.
Allerdings solltest Du auf die Spannungspegel der Anschlüsse zwischen den beiden Chips achten: der Pi hat 3,3 Volt, der Arduino 5 Volt.
Verbinde beide und die wirst magischen blauen Rauch aufsteigen sehen...

Persönlich nehme ich gerne einen ATmega 328 mit einem 3,3Volt Spannungsregulierer, der die 5 Volt Spannungsversorgung auf 3,3 Volt für den ATmega 328
runter reguliert. Der ATmega 328 läuft ganz gut mit 3,3 Volt und einem 15Mhz Quarz und so bekommt man einen Arduino-Klone mir 3,3 Volt Logik.

Wenn Du die WiringPi-Python-Bibliothek installiert hast, öffnet das folgende Beispiel die serielle Schnittstelle mit
einer Übertragungsgeschwindigkeit von 9600baud und gibt 'hello world' aus:

```python
import wiringpi
wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
wiringpi.serialPuts(serial,'hello world!')
```
