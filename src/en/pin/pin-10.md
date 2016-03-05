This pin doubles up as the UART recieve pin, RXD. It's also commonly known as "Serial" and, by default, will output a Console from your Pi that, with a suitable Serial cable, you can use to control your Pi via the command-line.

Thus, The UART pins are useful for setting up a "headless" Pi (a Pi without a screen) and getting it connected to a network.

UART can also be extremely useful if you want to talk to Arduino or Propeller boards from your Pi, but you must make sure you disable the Serial Console in raspi-config first.

[Learn more about UART](/pinout/uart)