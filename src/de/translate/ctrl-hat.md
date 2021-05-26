<!--
---
name: CTRL HAT
class: board
type: io, relay, motor
formfactor: HAT
manufacturer: PlasmaDan
description: SIP style solid state relay (SSR) home automation and industrial control HAT for Raspberry Pi.
url: https://plasmadan.com/ctrlhat
github: https://github.com/plasmadancom/CTRL-HAT
schematic: https://plasmadan.shop/ctrl-hat-v1-2-schematic/
buy: https://plasmadan.com/ctrlhat
image: 'ctrl-hat.png'
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
# CTRL HAT

The CTRL HAT is a 4 channel solid state power relay controller board based on the Microchip MCP23017 I2C expander. Designed for switching high power loads without the need for costly extra hardware such as SSR modules or contactors.

Ideally suited to automation or industrial control applications requiring high-speed switching, or switching of loads not suitable for regular mechanical relays, such as motors, power supplies, or noise sensitive equipment such as amplifiers.

## Features

* Support 4 industry standard SIP type solid state relays
* Up to 10A @ 250V / 16A @ 250V (forced air cooled)
* Huge range of compatible solid state relays ([known list](https://github.com/plasmadancom/CTRL-HAT#known-compatible-solid-state-relays))
* Easy to use [interactive web GUI](https://io.plasmadan.com/ctrlhat)
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