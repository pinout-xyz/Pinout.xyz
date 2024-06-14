<!--
---
name: Appliance HAT Mini
class: board
type: io, relay
formfactor: pHAT
manufacturer: PlasmaDan
description: Raspberry Pi pHAT I/O board with 2 quick connect 16A relays.
url: https://plasmadan.com/appliancehatmini
github: https://github.com/plasmadancom/Appliance-HAT-Mini
schematic: https://plasmadan.shop/appliance-hat-mini-v1-0-schematic/
buy: https://plasmadan.com/appliancehatmini
image: 'appliance-hat-mini.png'
pincount: 40
eeprom: no
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
# Appliance HAT Mini

The Appliance HAT Mini is a dual SPST relay I/O board based on the Microchip MCP23017 I2C expander. Ideally suited to switching of household appliances, industrial control or home automation applications.

## Features

* 2 opto-isolated quick connect power relays
* Up to 16A @ 250V AC
* Easy to use [interactive web GUI](https://io.plasmadan.com/appliancehatmini/)
* Based on the MCP23017 16-port GPIO expander
* Jumper selectable I2C address & GPIO voltage (3.3V / 5V)
* Can be used with 3.3V or 5V I2C host devices (eg, Arduino)

## Easy Installer

Our easy installer takes care of the setup process automatically.

```
sudo wget https://git.plasmadan.com/install.sh
sudo sh install.sh
```

Alternatively, you can install manually. See our [setup guide](https://github.com/plasmadancom/HAT-GUI#setup-guide).