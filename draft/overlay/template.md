<!--
---
name: My Add-on Board
class: board
type: other
formfactor: Custom
manufacturer: Company
description: An add-on board for the Raspberry Pi
url: https://my-addon-board.com
github: https://github.com/my-addon-board-repo.com
schematic: https://my-addon-board-schematic.com
buy: http://buy-my-addon-board.com
image: 'image.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Enable
    mode: output
    active: high
i2c:
  '0x00':
    name: device display name
    device: chip name
-->
#my add-on board

Use this section to provide additional information such as features, technical parts, install requirements, etc. Please keep this section to the point and avoid copy/paste of marketing blurb - the board's extended description should be primarily neutral and technical.

The overlay itself uses the following fields, some of which are mandatory, as noted below:

MANDATORY
* name: the board name as it will appear at pinout.xyz
* class: the class the overlay falls in, 'board' is the most common (use that if in doubt).
* type: the typical applications of the board, i.e 'lcd' (use 'other' if in doubt). If multiple types apply, use a comma separated list (for example, 'adc,motor'). The keywords submitted will be used to filter boards on the site so don't include anything but tags that are relevant to the key functionality of the board.
* formfactor: the board's form factor. Valid values are Custom, HAT and pHAT. Note that an EEPROM is required for HAT specs, use Custom if that is not the case.
* manufacturer: the manufacturer's name.
* description: a description of what the add-on board provides.
* url: the main URL for the product providing detailed technical information about the board.
* pin: an array of the pins used. Do not specify power or EEPROM pins as part of the array!

DESIRABLE
* pincount: the header pin count, typically 26 or 40 but shims/custom boards are acceptable.
* eeprom: whether the board includes an eeprom (required by 'HAT' specs!).
* power: the supply logic required by the board. Valid values are 'external', '3v3', '5v' and '3v3,5v'.
* i2c: if the board uses i2c, a list of the bus address(es) and device(s) identification.

OPTIONAL
* image: a top-down image of the board as png with transparency or appropriate placeholder (see image template in board directory).
* github: github repository address.
* buy: URL where the board can be purchased.
