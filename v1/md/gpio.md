<!--
---
name: GPIO
class: interface
type: pinout
description: Raspberry Pi general purpose IO pins
url: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio
pin:
  '3':
  '5':
  '7':
  '8':
  '10':
  '11':
  '12':
  '13':
  '15':
  '16':
  '18':
  '19':
  '21':
  '22':
  '23':
  '24':
  '26':
  '27':
  '28':
  '29':
  '31':
  '32':
  '33':
  '35':
  '36':
  '37':
  '38':
  '40':
-->
# GPIO - General Purpose Input/Output

A GPIO pin can be read as an input, driven as an output, or switched to one of its alternate functions, connecting it to a peripheral inside the chip.

## Logic levels

GPIO pins are 3.3v. The Pi's GPIO are not 5v tolerant and could be damaged by 5v devices- use an appropriate level shifter or divider.

An input doesn't need a full 3.3v to read high, and the thresholds differ by model:

| Model | Reads low below | Reads high above |
| --- | --- | --- |
| Pi 1-3, Zero | 0.9v | 1.6v |
| Pi 4, 400, CM4 | 0.8v | 2.0v |

If you can find equivalent figures for the Pi 5's RP1, let me know!

## Drive strength

Drive strength is configurable. Both the default and the maximum differ by model:

| Model | Default | Maximum |
| --- | --- | --- |
| Pi 1-3, Zero | 8mA | 16mA |
| Pi 4, 400, CM4 | 4mA | 8mA |

These are drive strength settings rather than a rating for how much current a pin can safely supply. [Raspberry Pi's GPIO documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio) gives no per-pin or total limit for the header. Treat an output as a control signal: anything that needs powering should be fed from the [3v3](/pinout/3v3_power) or [5v](/pinout/5v_power) pins, or from its own supply.

## Pull-ups and pull-downs

Every GPIO pin has an internal pull-up and pull-down resistor that can be enabled in software:

| Model | Internal pull |
| --- | --- |
| Pi 1-3, Zero | 50 to 65 kΩ |
| Pi 4, 400, CM4 | 33 to 73 kΩ |

[GPIO 2 and GPIO 3](/pinout/i2c) are the exception, with fixed 1.8 kΩ pull-ups fitted to the board.

Every pin is an input at power-on, and most have a default pull applied. The defaults are listed in the alternate function table in the Arm peripherals datasheet.

## Alternate functions

Pi 4 and earlier have six alternate functions per pin, Alt0 to Alt5. Pi 5's RP1 has nine, F0 to F8, in a different order. Each pin's page lists them for all three generations.

Overlays written before Pi 5 still work; the RP1 driver translates the old function numbers to the closest matching RP1 function. Asking for function 2 (Alt5 on the older chips) gets you F3 on a Pi 5.

## Setting a pin from config.txt

A `gpio=` line in /boot/firmware/config.txt sets a pin's direction, level, pull or function at boot:

```
gpio=12=op,dh
gpio=0-27=a2
```

The first line makes GPIO 12 an output driven high. The second line puts every pin in bank 0 on alternate function 2 ([DPI](/pinout/dpi)). The attributes are:

| Attribute | Sets |
| --- | --- |
| `ip`, `op` | Input or output |
| `a0` to `a5` | One of the alternate functions |
| `dh`, `dl` | Drive an output high or low |
| `pu`, `pd`, `pn` | Pull up, pull down or no pull |

These settings take a few seconds to apply after power is connected, and longer when booting from the network or from USB storage. Anything set up later by an overlay or the `pinctrl` tool overrides them.
