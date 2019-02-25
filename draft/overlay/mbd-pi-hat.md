<!--
---
name: MDB HAT
class: board
type: alle
formfactor: HAT
manufacturer: Qibixx
description: Multi-Drop-Bus MDB Bus sniffer for the Raspberry Pi
url: https://qibixx.com
buy: https://qiba.pt/
image: 'mbd-pi-hat.png'
pincount: 40
eeprom: yes
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
    mode: uart
    name: TXD breakout
  '10':
    mode: uart
    name: RXD breakout
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
-->
# MDB HAT
The MDBHAT from [Qibixx](https://qibixx.com) is a Raspberry Pi HAT connecting the Pi with the MDB (Machine Data Bus), found in vending machines and peripherals such as Coin and Bill Acceptors. With its advanced architecture, the MDB Hat can support MDB Master, MDB Peripheral and MDB Sniffing applications without any jumper settings.

The firmware of the MDBHAT can be updated from the Pi.

For universal connectivity, the MDB HAT connects with the PI with either serial or SPI interface.
The MDB HAT is powered from the Pi, however, it can also provide up to 15W (5V, 3A) and backpower the Pi if MDB power is available. In most applications, the MDB HAT plus Pi and even other peripherals can be used without an additional power supply.

Full device documentation and protocol information is available [here](https://docs.qibixx.com).

General MDB information and a device family overview can be found [here](https://mdb.technology).