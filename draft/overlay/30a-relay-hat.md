<!--
---
name: 30A Relay HAT
class: board
type: io, relay
formfactor: HAT
manufacturer: PlasmaDan
description: Raspberry Pi HAT I/O board which offers an impressive 30A switching capability.
url: https://plasmadan.com/30arelayhat
github: https://github.com/plasmadancom/30A-Relay-HAT
buy: https://plasmadan.com/30arelayhat
image: '30a-relay-hat.png'
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
i2c:
  '0x20':
    alternate: [ '0x21', '0x22', '0x23', '0x24', '0x25', '0x26', '0x27' ]
    name: MCP23008
    device: MCP23008
-->
# 30A Relay HAT

A Raspberry Pi HAT I/O board which offers an impressive 30A switching capability. Ideally suited to automation or industrial control, switching of household appliances, industrial machinery or automotive applications.

## Features

* 2 opto-isolated SPDT power relays
* 30A / 15A @ 250V AC (NO / NC)
* Supports up to 6mm<sup>2</sup> / 10 AWG cable
* 2oz copper PCB ensures maximum current flow
* Easy to use [interactive web GUI](https://io.plasmadan.com/30arelayhat/)
* Based on the MCP23008 8-port GPIO expander
* Jumper selectable I2C address & GPIO voltage (3.3V / 5V)
* Can be used with 3.3V or 5V I2C host devices (eg, Arduino)
* Built-in user programmable ID EEPROM

## Easy Installer

Our easy installer takes care of the setup process automatically.

```
sudo wget https://git.plasmadan.com/install.sh
sudo sh install.sh
```

Alternatively, you can install manually. See our [setup guide](https://github.com/plasmadancom/HAT-GUI#setup-guide).