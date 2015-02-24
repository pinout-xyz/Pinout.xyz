#Pinout Overlays

A Pinout overlay describes the functions of the Raspberry Pi pins for a specific board.

An overlay is constructed from a JSON file and, optionally, a markdown file containing an extended long-description.

##JSON Format

The JSON overlay file must include a name, manufacturer name, URL, description 
( short description required, long is optional ) and a "pin" array.

The pin array must list each pin by its *physical* location, and include at least a "name" describing the function
of that pin.

Optionally each pin definition can include an "exclusive" flag, which marks this pin as being unavailable for other
use when it's occupied by this add-on.

Things like i2c/SPI wont normally be flagged as exclusive, but most general purpose GPIO pins would, for example.

Example:

```json
{
	"name": "Pibrella",
	"manufacturer": "Pimoroni",
	"url": "https://github.com/pimoroni/pibrella",
	"description": {
		"short": "An all-in-one light, sound, input and output add-on board.",
		"long": "pibrella.md"
	},
	"pin": {
		"7": {
			"name": "Green LED",
			"exclusive": "true"
		},
		"11": {
			"name": "Yellow LED",
			"exclusive": "true"
		}
	}
}
```
