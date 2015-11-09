Dieser Anschluss kann auch als [UART](https://de.wikipedia.org/wiki/Universal_Asynchronous_Receiver_Transmitter) Sendeleitung genutzt werden. Senden heisst im
englischen 'transmit' - daher die Bezeichnung TXD. 
This pin doubles up as the UART transmit pin, thus the name TXD. It's also commonly 
known as "Serial" and, by default, will output a Console from your Pi that, with a 
suitable Serial cable, you can use to control your Pi via the command-line.

UART is also extremely useful if you want to talk to Arduino or Propeller boards from 
your Pi, but you must make sure you disable the Serial Console in raspi-config first.

[Learn more about UART](/pinout/uart)