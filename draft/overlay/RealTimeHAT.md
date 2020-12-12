<!--
---
name: Real-Time HAT
class: board
type: multi
formfactor: HAT
manufacturer: InnoRoute GmbH
description: The Real-Time HAT extends the Gigabit-Ethernet interface of the Raspberry Pi by professional networking functions.
github: https://github.com/InnoRoute/RealtimeHAT
image: 'RealTimeHAT.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
ground:
  '6':
  '9':
  '14':
  '17':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: PHY_MDC
  '11':
    name: PHY_MDIO
  '13':
    name: FPGA_Interrupt
    direction: Input
  '15':
    name: Buffer_Full
    direction: Input
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '26':
    mode: spi
  '27':
    mode: i2c
  '28':
    mode: i2c
i2c:
  '0x50':
    name: ID EEPROM
    device: I2C0 - ID EEPROM
  '0x24':
    name: PMIC
    device: I2C1 - PMIC
  '0x43':
    name: IO Expender
    device: I2C1 - IO Expander
-->
# Real-Time HAT

The Real-Time HAT extends the Gigabit-Ethernet interface of the Raspberry Pi by professional networking functions.
Typical applications are **industrial real-time communication** and **network monitoring**.

The HAT provides **3 Gigabit-Ethernet ports**, one of which connecting to the Raspberry Pi's Ethernet port.
Connection to the Raspberry Pi is realized via the GPIO connector and via a (short) Ethernet cable. Interface SPI0 is for main configuration, using either CE0# or CE1#. 
Additional information on use cases, programming interfaces etc. can be found on [InnoRoute's website](https://innoroute.com/realtimehat/)., e.g., on using the HAT as an **endpoint in Time-Sensitive Networks**, as a **3-port Ethernet switch**, or to **measure and monitor** any kind of the traffic forwarded through the HAT.

To install the necessary software, use the following commands:

```bash
git clone https://github.com/InnoRoute/RealtimeHAT
cd RealtimeHAT
./install.sh
```
