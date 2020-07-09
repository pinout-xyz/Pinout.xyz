<!--
---
name: MDB HAT
class: board
type: io
formfactor: HAT
manufacturer: Qibixx
collected: Other
description: MDB (Machine Data Bus) Bus Interface
url: https://qibixx.com
buy: https://qiba.pt/
image: 'mdb-pi-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
  '17':
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
    name: TxD
    mode: UART
    description: Serial TX > MDB Controller
  '10':
    name: RxD
    mode: UART
    description: Serial RX < MDB Controller
  '19':
    name: SPI_SDO
    mode: spi
    description: MDB Controller - SDO
  '21':
    name: SPI_SDI
    mode: spi
    description: MDB Controller – SDI
  '23':
    name: SPI_SCLK
    mode: spi
    description: MDB Controller - SCLK
  '24':
    name: SPI_CE0
    mode: spi
    description: MDB Controller – CS
  '27':
    name: ID_SD
    mode: I2C
    description: ID EEPROM DTA
  '28':
    name: ID_SC
    mode: I2C
    description: ID EEPROM CLK
  '29':
    name: IO2RPI
    mode: output
    description: IO MDB>RPi
  '31':
    name: MDB_RES
    mode: input
    description: MDB Contoller Reset
  '33':
    name: IOfromRPi
    mode: input
    description: IO RPi>MDB
-->
# MDB HAT
The MDBHAT from [Qibixx](https://qibixx.com) is a Raspberry Pi HAT connecting the Pi with the MDB (Machine Data Bus), found in vending machines and peripherals such as Coin and Bill Acceptors. With its advanced architecture, the MDB Hat can support MDB Master, MDB Peripheral and MDB Sniffing applications without any jumper settings.

The firmware of the MDBHAT can be updated from the Pi.

For universal connectivity, the MDB HAT connects with the PI with either serial or SPI interface.
The MDB HAT is powered from the Pi, however, it can also provide up to 15W (5V, 3A) and backpower the Pi if MDB power is available. In most applications, the MDB HAT plus Pi and even other peripherals can be used without an additional power supply.

Full device documentation and protocol information is available [here](https://docs.qibixx.com).

General MDB information and a device family overview can be found [here](https://mdb.technology).
