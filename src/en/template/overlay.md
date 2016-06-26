<!--
---
name: board name
class: category
type: application
image: board image
manufacturer: made by
description: what it is
url: https://myaddon.com
github: https://github.com/myaddonrepo.com
buy: http://shopformyaddon.com
formfactor: Custom
pincount: 26
eeprom: no
power: 3v3,5v
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x00':
    name: device display name
    device: chip name
-->
#my add-on board

Use this section to provide additional information such as fonctionality, technical parts, install requirements, etc  
The overlay itself uses the following fields, some of which are mandatory, as noted below:

MANDATORY  
name: the board name as it will appear in the board selection menu at pinout.xyz  
class: the class the overlay falls in, 'board' is the most common (use that if in doubt).  
type: the typical applications of the board, i.e 'lcd' (use 'other' if in doubt).  
If multiple types apply, use a comma separated list (for example, 'adc,motor').  
The keywords submitted will be used to filter boards at pinout.xyz so don't include anything but tags that are relevant to the key functionality of the board. 
manufacturer: the manufacturer's name.  
description: a short description of what the add-on board provides.  
url: the main URL for the product providing detailed technical information about the board.  
pin: an array of the pins used. Do not specify power or EEPROM pins as part of the array!  

DESIRABLE  
formfactor: the board's form factor. Valid values currently are 26-way, Custom, HAT and pHAT.  
pincount: the header pin count, typically 26 or 40 but shims/custom boards are acceptable.  
eeprom: whether the board includes an eeprom (required by 'HAT' specs!).  
power: the supply logic required by the board. Valid values are 3v3, 5v and 3v3,5v.  
i2c: if the board uses i2c, a list of the bus address(es) and device(s) identification.  

OPTIONAL  
image: a top-down image of the board as png with transparency (or placeholder).  
github: github repository address.  
buy: URL where the board can be purchased.  
