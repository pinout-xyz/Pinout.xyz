<!--
---
name: RS485 Pi
class: board
type: com
formfactor: pHAT
manufacturer: AB Electronics
description: UART to RS485 Converter
url: https://www.abelectronics.co.uk/p/77/RS485-Pi
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/77/RS485-Pi
image: 'ab-rs485-pi.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '8':
    mode: UART
  '10':
    mode: UART
-->
#RS485 Pi

The RS485 Pi is a UART to RS485 serial converter for the Raspberry Pi.

The RS485 port is connected to the UART port on the Raspberry Pi using a SN65HVD72 interface. The SN65HVD72 IC converts the 3.3V UART port to RS485 differential voltages allowing communication with RS485 compatible devices over a twisted pair cable. The RS485 port can be accessed through the DB9 port or the solder points on the PCB.

The RS485 Pi contains protection against voltage spikes in the form of a TVS Diode and two 10O, Pulse-Proof Thick-Film Resistors.  A 120O terminator resistor is included with the board.

##Features

- RS-485 Half Duplex Port.
- Up to 250 kbps transfer rate.
- Use the Raspberry Pi to control external RS-485 devices.
- Stackable with other Raspberry Pi accessory boards.
- Mounting holes for use with the AB Electronics UK mounting kits (sold separately)

[Configuring the UART communication on the Raspberry Pi](https://www.abelectronics.co.uk/kb/article/20/raspberry-pi-serial-port-usage)