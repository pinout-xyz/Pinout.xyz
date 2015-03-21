#Pinout Overlays

A Pinout overlay describes the functions of the Raspberry Pi pins for a specific board.

An overlay is constructed from a JSON file and, optionally, a markdown file containing an extended long-description.

##JSON Format

The JSON overlay file must include a name, manufacturer name, URL, description and a "pin" array defining all the
pins that the board uses.

If a counterpart .md file is present in description/overlay it will be used for the long description.

The pin array must list each pin by its *physical* location, and include at least a "name" describing the function
of that pin.

Optionally each pin definition can include a "mode" flag, which defines the pin as an "input" or an "output".

A pin can also have an "active" value, which defines it as "high" or active "low".

I2C and SPI pins should be included if your board uses them, however they will generally be intepreted as being
shared and usable with muliple boards unless you explicitly define them as being an "input" or "output".

Example:

```json
{
	"name": "Explorer HAT",
	"manufacturer": "Pimoroni",
	"url": "https://github.com/pimoroni/pibrella",
	"description": "An all-in-one light, input and output add-on board.",
	"pin": {
		"7": {
			"name": "Green LED"
		},
		"11": {
			"name": "Yellow LED"
		}
	}
}
```
