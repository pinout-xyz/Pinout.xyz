<!--
---
name: PiJack
class: board
type: network
formfactor: pHAT
manufacturer: Hot Glue
description: Add Ethernet to your Pi Zero
url: https://pijack.net
buy: https://pijack.net
image: 'pijack.png'
pincount: 40
eeprom: setup
power:
  '2':
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
  '22':
    name: INT
    mode: input
    description: Ethernet controller interrupt
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
-->
#PiJack

The easiest way to add Ethernet to your Rasberry Pi Zero. Simply plug the PiJack board on to your Pi and boot the latest Raspbian. PiJack will be autodetected by the Linux kernel, the correct driver will be loaded and the Ethernet interface will be ready to use.

By default, Raspbian will automatically configure the interface for DHCP so as soon as you connect PiJack to your network your Pi will request an address and be ready to go online!

Each PiJack board is programmed with a unique and persistent MAC address so each time your Pi boots the MAC address will remain the same. This allows you to set up your router to hand out the same IP address each time.

There are a couple of recent improvements to the Ethernet controller driver, so if you're not running the latest version of Raspbian on your Pi, either download it and reflash your microSD card again, or run
```bash
sudo apt-get update
sudo apt-get dist-upgrade
```


