This pin doubles up as the UART receive pin, RX. It's also commonly known as "Serial" and, with a [suitable serial cable](https://elinux.org/RPi_Serial_Connection) and the serial port enabled in raspi-config, gives you a console you can use to control your Pi from the command line.

The UART pins can be useful for setting up a "headless" Pi (a Pi without a screen) and getting it connected to a network.

UART can also be used to talk to serial GPS modules or sensors such as the PMS5003, but you must disable the serial console in raspi-config first.

On the Pi 3, Pi 4, Pi Zero W and Pi Zero 2 W, Bluetooth has the full hardware UART and these pins are wired to the mini UART, whose baud rate follows the VPU core clock. Adding "enable_uart=1" to "/boot/firmware/config.txt" pins that clock, and "dtoverlay=miniuart-bt" swaps the two over so that these pins get the full UART, at the cost of a lower Bluetooth baud rate.

The Pi 5 has no mini UART. These pins carry a full PL011 UART, enabled with "dtoverlay=uart0-pi5", and the serial console lives on the dedicated three-pin debug header instead.

All UARTs are 3.3v only and damage will occur if they are connected to 5v systems.

[Learn more about UART](/pinout/uart)

[Raspberry Pi UART documentation](https://www.raspberrypi.com/documentation/computers/configuration.html#uarts)
