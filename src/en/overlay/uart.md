<!--
---
type: info
name: UART
description: Raspberry Pi UART pins
pincount: 2
pin:
  '8':
    name: TXD / Transmit
    direction: output
    active: high
  '10':
    name: RXD / Receive
    direction: input
    active: high
-->
#UART - Universal Asynchronous Receiver/Transmitter

###The 2 UART pins in WiringPi are: 15, 16

UART is a handy, straight forward way to interface an Arduino ( or bootloaded ATmega ) with your Pi. You must, however, be careful with logic-levels between the two devices: the Pi is 3.3v and the Arduino is 5v. Connect the two and you might conjure up some magic blue smoke.

Personally I'm a fan of building out a Arduino Bootloaded ATmega 328 circuit on a breadboard with a voltage regulator to take the Pi's 5v line and convert it to 3.3v. The ATmega 328 seems to run quite happily at 3.3v using a 16Mhz crystal and you'll then have an Arduino clone with 3.3v logic.

Assuming you have WiringPi2-Python installed, the following python example opens the Pi's UART at 9600baud and puts 'hello world'

```python
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
wiringpi.serialPuts(serial,'hello world!')
```