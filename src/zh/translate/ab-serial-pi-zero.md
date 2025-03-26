<!--
---
name: Serial Pi Zero
class: board
type: com
formfactor: pHAT
manufacturer: AB Electronics UK
description: UART to RS232 Converter
url: https://www.abelectronics.co.uk/p/75/serial-pi-zero
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-serialpizero.pdf
buy: https://www.abelectronics.co.uk/p/75/serial-pi-zero
image: 'ab-serial-pi-zero.png'
pincount: 40
eeprom: no
power:
  '1':
ground:
  '6':
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
# Serial Pi Zero

The Serial Pi Zero is a UART to RS232 serial converter for the Raspberry Pi Zero.

The RS232 port is connected to the UART port on the Raspberry Pi using a MAX3232 interface. The MAX3232 IC converts the 3.3V UART port to RS232 voltages allowing communication with RS232 compatible devices over a DB9 serial cable or with the use of a null-modem cable the board allows terminal access with linux on the Raspberry Pi using a terminal application. The RS232 port can be accessed through the DB9 port or the solder points on the PCB.

## Features

- RS232 Master Port.
- Control the Raspberry Pi over RS232 or connect to external serial accessories.
- Stackable with other Raspberry Pi accessory boards.
- Mounting holes for use with the AB Electronics UK mounting kits (sold separately)

[Configuring the RS232 communication on the Raspberry Pi](https://www.abelectronics.co.uk/kb/article/20/raspberry-pi-serial-port-usage)
