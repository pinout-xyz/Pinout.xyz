<!--
---
name: UART
class: interface
type: pinout
description: Raspberry Pi UART pins
url: http://elinux.org/RPi_Serial_Connection
pincount: 18
pin:
  '8':
    name: TXD / Transmit
    direction: output
    active: high
  '10':
    name: RXD / Receive
    direction: input
    active: high
  '36':
    name: UART0 CTS
    direction: both
    active: high
  '11':
    name: UART0 RTS
    direction: both
    active: high
  '27':
    name: UART2 TXD
    direction: output
    active: high
    supported: Pi 4 (UART2) and Pi 5 (UART1)
  '28':
    name: UART2 RXD
    direction: input
    active: high
    supported: Pi 4 (UART2) and Pi 5 (UART1)
  '3':
    name: UART2 CTS
    direction: both
    active: high
    supported: Pi 4 (UART2) and Pi 5 (UART1)
  '5':
    name: UART2 RTS
    direction: both
    active: high
    supported: Pi 4 (UART2) and Pi 5 (UART1)
  '7':
    name: UART3 TXD
    direction: output
    active: high
    supported: Pi 4 (UART3) and Pi 5 (UART2)
  '29':
    name: UART3 RXD
    direction: input
    active: high
    supported: Pi 4 (UART3) and Pi 5 (UART2)
  '31':
    name: UART3 CTS
    direction: both
    active: high
    supported: Pi 4 (UART3) and Pi 5 (UART2)
  '26':
    name: UART3 RTS
    direction: both
    active: high
    supported: Pi 4 (UART3) and Pi 5 (UART2)
  '24':
    name: UART4 TXD
    direction: output
    active: high
    supported: Pi 4 (UART4) and Pi 5 (UART3)
  '21':
    name: UART4 RXD
    direction: input
    active: high
    supported: Pi 4 (UART4) and Pi 5 (UART3)
  '19':
    name: UART4 CTS
    direction: both
    active: high
    supported: Pi 4 (UART4) and Pi 5 (UART3)
  '23':
    name: UART4 RTS
    direction: both
    active: high
    supported: Pi 4 (UART4) and Pi 5 (UART3)
  '32':
    name: UART5 TXD
    direction: output
    active: high
    supported: Pi 4 (UART5) and Pi 5 (UART4)
  '33':
    name: UART5 RXD
    direction: input
    active: high
    supported: Pi 4 (UART5) and Pi 5 (UART4)
-->
# UART - Universal Asynchronous Receiver/Transmitter
---
### UART pins in BCM mode are: 14, 15
### UART pins in WiringPi are: 15, 16
---
UART is an asynchronous serial communication protocol, meaning that it takes bytes of data and transmits the individual bits in a sequential fashion.

Asynchronous transmission allows data to be transmitted without the sender having to send a clock signal to the receiver. Instead, the sender and receiver agree on timing parameters in advance and special bits called 'start bits' are added to each word and used to synchronize the sending and receiving units.

UART is commonly used on the Pi as a convenient way to control it over the GPIO, or access the kernel boot messages from the serial console (enabled by default).

It can also be used as a way to interface an Arduino, bootloaded ATmega, ESP8266, etc with your Pi. Be careful with logic-levels between the devices though, for example the Pi is 3.3v and the Arduino is 5v. Connect the two and you might conjure up some magic blue smoke.
