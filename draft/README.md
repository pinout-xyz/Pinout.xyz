# Pinout Overlays

A Pinout overlay describes the functions of the Raspberry Pi pins for a specific board.
An overlay is specified by a Markdown file containing mandatory and optional fields as well as an extended long-description.

The Markdown overlay file must include as a minimum a name, class, type, formfactor, manufacturer, (short) description, product url, and last but not least an array defining all the pins that the board uses.

A long description is also highly desirable so that visitors to the site can get an introduction to the add-on boards featured on the site if they are not familar with them.

Note that the pin array must list each pin by its *physical* location, and include at least a 'name' describing the function of that pin.

Optionally each pin definition can include a 'direction', which defines the pin as an input or an output. A pin can also have an 'active' value, which defines it as active high or active low.

I2C and SPI pins should be included if your board uses them, however they will generally be intepreted as being shared and usable with muliple boards unless you explicitly define them as being an input or output.

Power pins and EEPROM should specifically be excluded, but specifying the power and eeprom fields are highly recommended if that info is known.

All of the above is further expended in the overlay template.md. We recommend you use this template as a starting point for any new add-on board submission and add or remove fields as required.