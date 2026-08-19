<!--
---
description: Pines de UART de la Raspberry Pi
pin:
  '8':
    name: TXD / Transmitir
  '10':
    name: RXD / Recibir
-->
# UART - Universal Asynchronous Receiver/Transmitter (Receptor/Transmisor Universal Asíncrono)

### Los 2 pines de UART en WiringPi son: 15, 16

El UART es una útil y directa manera de comunicar un Arduino ( o un ATmega con bootloader) con tu Pi. Debes, sin embargo, tener cuidado con los niveles lógicos entre los dos aparatos: la Pi es de 3.3v y el Arduino de 5v. Conecta los dos y puede que invoques humo mágico azul.

Personalmente prefiero colocar en una placa de pruebas un ATmega 328 con el bootloader de Arduino, con un regulador de voltaje que tome de entrada la línea de 5v de la Pi y que saque 3.3v. El ATmega 328 parece bastante feliz a 3.3v y usando un cristal de 16Mhz, y además tendrás un clon de un Arduino con lógica de 3.3v.
