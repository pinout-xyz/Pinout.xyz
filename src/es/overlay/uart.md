<!--
---
name: UART
class: interface
type: pinout
description: Pines de UART de la Raspberry Pi
url: http://elinux.org/RPi_Serial_Connection
pincount: 18
pin:
  '8':
    name: TXD / Transmitir
    direction: output
    active: high
  '10':
    name: RXD / Recibir
    direction: input
    active: high
  '36':
    name: UART0 CTS
    direction: both
    active: high
  '11':
    name: UART0 RTS
    direction: both
    active: high
  '27':
    name: UART2 TXD
    direction: output
    active: high
    supported: Pi 4 (UART2) and Pi 5 (UART1)
  '28':
    name: UART2 RXD
    direction: input
    active: high
    supported: Pi 4 (UART2) and Pi 5 (UART1)
  '3':
    name: UART2 CTS
    direction: both
    active: high
    supported: Pi 4 (UART2) and Pi 5 (UART1)
  '5':
    name: UART2 RTS
    direction: both
    active: high
    supported: Pi 4 (UART2) and Pi 5 (UART1)
  '7':
    name: UART3 TXD
    direction: output
    active: high
    supported: Pi 4 (UART3) and Pi 5 (UART2)
  '29':
    name: UART3 RXD
    direction: input
    active: high
    supported: Pi 4 (UART3) and Pi 5 (UART2)
  '31':
    name: UART3 CTS
    direction: both
    active: high
    supported: Pi 4 (UART3) and Pi 5 (UART2)
  '26':
    name: UART3 RTS
    direction: both
    active: high
    supported: Pi 4 (UART3) and Pi 5 (UART2)
  '24':
    name: UART4 TXD
    direction: output
    active: high
    supported: Pi 4 (UART4) and Pi 5 (UART3)
  '21':
    name: UART4 RXD
    direction: input
    active: high
    supported: Pi 4 (UART4) and Pi 5 (UART3)
  '19':
    name: UART4 CTS
    direction: both
    active: high
    supported: Pi 4 (UART4) and Pi 5 (UART3)
  '23':
    name: UART4 RTS
    direction: both
    active: high
    supported: Pi 4 (UART4) and Pi 5 (UART3)
  '32':
    name: UART5 TXD
    direction: output
    active: high
    supported: Pi 4 (UART5) and Pi 5 (UART4)
  '33':
    name: UART5 RXD
    direction: input
    active: high
    supported: Pi 4 (UART5) and Pi 5 (UART4)
-->
# UART - Universal Asynchronous Receiver/Transmitter (Receptor/Transmisor Universal Asíncrono)

### Los 2 pines de UART en WiringPi son: 15, 16

El UART es una útil y directa manera de comunicar un Arduino ( o un ATmega con bootloader) con tu Pi. Debes, sin embargo, tener cuidado con los niveles lógicos entre los dos aparatos: la Pi es de 3.3v y el Arduino de 5v. Conecta los dos y puede que invoques humo mágico azul.

Personalmente prefiero colocar en una placa de pruebas un ATmega 328 con el bootloader de Arduino, con un regulador de voltaje que tome de entrada la línea de 5v de la Pi y que saque 3.3v. El ATmega 328 parece bastante feliz a 3.3v y usando un cristal de 16Mhz, y además tendrás un clon de un Arduino con lógica de 3.3v.
