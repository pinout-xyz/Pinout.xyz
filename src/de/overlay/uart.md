<!--
---
name: UART
class: interface
type: pinout
description: Raspberry Pi UART Anschlüsse
url: http://elinux.org/RPi_Serial_Connection
pincount: 18
pin:
  '8':
    name: TXD / Senden
    direction: output
    active: high
  '10':
    name: RXD / Empfangen
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
# UART - Universal Asynchronous Receiver/Transmitter (serielle Schnittstelle)

### Die beiden UART Anschlüsse sind in WiringPi 15 und 16

UART ist eine einfache und nützliche Schnittstelle um einen Arduino (oder vorbereiteten ATmega) mit Deinem Pi zu verbinden.
Allerdings solltest Du auf die Spannungspegel der Anschlüsse zwischen den beiden Chips achten: der Pi hat 3,3 Volt, der Arduino 5 Volt.
Verbinde beide und die wirst magischen blauen Rauch aufsteigen sehen...

Persönlich nehme ich gerne einen ATmega 328 mit einem 3,3Volt Spannungsregulierer, der die 5 Volt Spannungsversorgung auf 3,3 Volt für den ATmega 328
runter reguliert. Der ATmega 328 läuft ganz gut mit 3,3 Volt und einem 15Mhz Quarz und so bekommt man einen Arduino-Klone mir 3,3 Volt Logik.
