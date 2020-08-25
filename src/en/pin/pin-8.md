This pin doubles up as the UART transmit pin, TX. It's also commonly known as "Serial" and, by default, will output a Console from your Pi that, with a suitable Serial cable, you can use to control your Pi via the command-line.

The UART pins are useful for setting up a "headless" Pi (a Pi without a screen) and getting it connected to a network.

UART can be used to talk to Serial GPS modules or sensors such as the PM5003, but you must make sure you disable the Serial Console in raspi-config first.

On the Pi 3 and 4 the UART is, by default, used for Bluetooth and you may need to add "dtoverlay=miniuart-bt" to "/boot/config.txt" to achieve a stable.

[Learn more about UART](/pinout/uart)

[Raspberry Pi UART documentation](https://www.raspberrypi.org/documentation/configuration/uart.md)