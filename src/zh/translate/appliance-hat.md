<!--
---
name: Appliance HAT
class: board
type: io, relay
formfactor: HAT
manufacturer: PlasmaDan
description: Raspberry Pi HAT I/O board with 6 quick connect 16A relays.
url: https://plasmadan.com/appliancehat
github: https://github.com/plasmadancom/Appliance-HAT
schematic: https://plasmadan.shop/appliance-hat-v1-1-schematic/
buy: https://plasmadan.com/appliancehat
image: 'appliance-hat.png'
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
    name: MCP23017
    device: MCP23017
-->
# Appliance HAT

The Appliance HAT is a 6 channel SPST relay I/O board based on the Microchip MCP23017 I2C expander. Ideally suited to switching of household appliances, industrial control or home automation applications.

## Features

* 6 opto-isolated quick connect power relays
* Up to 16A @ 250V AC
* Easy to use [interactive web GUI](https://io.plasmadan.com/appliancehat/)
* Based on the MCP23017 16-port GPIO expander
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