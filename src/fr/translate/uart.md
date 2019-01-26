<!--
---
name: UART
class: interface
type: pinout
description: Raspberry Pi UART pins
url: http://elinux.org/RPi_Serial_Connection
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
---
###UART pins in BCM mode are: 14, 15
###UART pins in WiringPi are: 15, 16
---
UART is an asynchronous serial communication protocol, meaning that it takes bytes of data and transmits the individual bits in a sequential fashion.

Asynchronous transmission allows data to be transmitted without the sender having to send a clock signal to the receiver. Instead, the sender and receiver agree on timing parameters in advance and special bits called 'start bits' are added to each word and used to synchronize the sending and receiving units.

UART is commonly used on the Pi as a convenient way to control it over the GPIO, or access the kernel boot messages from the serial console (enabled by default).

It can also be used as a way to interface an Arduino, bootloaded ATmega, ESP8266, etc with your Pi. Be careful with logic-levels between the devices though, for example the Pi is 3.3v and the Arduino is 5v. Connect the two and you might conjure up some magic blue smoke.

Assuming you have WiringPi-Python installed, the following python example opens the Pi's UART at 9600baud and puts 'hello world'

```python
import wiringpi
wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
wiringpi.serialPuts(serial,'hello world!')
```
