<!--
---
name: RS485 Pi
class: board
type: com
formfactor: pHAT
manufacturer: AB Electronics UK
description: UART to RS485 Converter
url: https://www.abelectronics.co.uk/p/77/rs485-pi
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/viewpdf/schematic-rs485pi
buy: https://www.abelectronics.co.uk/p/77/rs485-pi
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
# RS485 Pi

The RS485 Pi is a communication board supporting the RS-485 serial protocol, designed to work with the Raspberry Pi and other compatible single-board computers.

The RS485 port is connected to the UART port on the Raspberry Pi using a SN65HVD72 interface. The SN65HVD72 IC converts the 3.3V UART port to RS485 differential voltages allowing communication with RS485 compatible devices over a twisted pair cable. The RS485 port can be accessed through the DB9 port or the solder points on the PCB.

The RS485 Pi contains protection against voltage spikes in the form of a TVS Diode and two 10R, Pulse-Proof Thick-Film Resistors.  A 120R terminator resistor is included with the board.

## Features

- RS-485 Half Duplex Port.
- Up to 250 kbps transfer rate.
- Use the Raspberry Pi to control external RS-485 devices.
- Stackable with other Raspberry Pi accessory boards.
- Mounting holes for use with the AB Electronics UK mounting kits (sold separately)

[Serial Port setup in Raspberry Pi OS](https://www.abelectronics.co.uk/kb/article/1035/serial-port-setup-in-raspberry-pi-os)
