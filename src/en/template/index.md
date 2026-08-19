# Pinout!

## The Raspberry Pi GPIO pinout guide.

This GPIO Pinout is an interactive reference to the Raspberry Pi GPIO pins, and a guide to the Raspberry Pi's GPIO interfaces. Pinout also includes [hundreds of pinouts for Raspberry Pi add-on boards, HATs and pHATs](/boards).

## Other Pinouts

We've created Pinouts for the Raspberry Pi Pico range of boards, too, you can find them here:

* [Raspberry Pi Pico Pinout](https://pico.pinout.xyz)
* [Raspberry Pi Pico W Pinout](https://picow.pinout.xyz)
* [Raspberry Pi Pico 2 Pinout](https://pico2.pinout.xyz)
* [Raspberry Pi Pico 2 W Pinout](https://pico2w.pinout.xyz)

Plus chip planners for the RP2350A and RP2350B chips:

* [Raspberry Pi RP2350A QFN-60 Pinout](https://rp2350a.pinout.xyz)
* [Raspberry Pi RP2350B QFN-80 Pinout](https://rp2350b.pinout.xyz)

And some experimental pinouts, too:

* [Minimal Raspberry Pi 40-pin Pinout](https://pi.pinout.xyz)
* [Espressif ESP32 C5 DevKitC Pinout](https://esp32c5.pinout.xyz)
* [Espressif ESP32 C3 DevKitC Pinout](https://esp32c3.pinout.xyz)
* [PJRC Teensy 4.0 Pinout](https://teensy40.pinout.xyz)

## Explore HATs & pHATs

[Check out Pinout's board explorer](/boards)! Use it to find the pinout for your Raspberry Pi add-on board, or discover new boards. If you manufacture boards, we'd love to add yours too. [You can contribute to Pinout.xyz at GitHub.com](https://github.com/pinout-xyz/Pinout.xyz).

## What do these numbers mean?

* GPIO - General Purpose Input/Output, aka "BCM" or "Broadcom". These are the big numbers, e.g. "GPIO 22". You'll use these with RPi.GPIO and GPIO Zero.
* Physical - or "Board" correspond to the pin's physical location on the header. These are the small numbers next to the header, e.g. "Physical Pin 15".
* WiringPi - for Gordon Henderson's Wiring Pi library. These are shown as a tooltip when you mouseover a pin.
* Rev 1 Pi - alternate GPIO/BCM numbers for the original, 26-pin model "A" and "B" Pi. The 40-pin header is a superset of that 26-pin one: pins 1 to 26 carry the same signals, so a 26-pin board or wiring diagram still applies.
