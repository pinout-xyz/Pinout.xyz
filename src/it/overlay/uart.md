<!--
---
name: UART
class: interface
type: pinout
description: Pin UART del Raspberry
url: http://elinux.org/RPi_Serial_Connection
pincount: 18
pin:
  '8':
    name: TXD / Trasmissione
    direction: output
    active: high
  '10':
    name: RXD / Ricezione
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
# UART - Universal Asynchronous Receiver/Transmitter

### I due pin UART in WiringPi sono il 15 e il 16.

UART è una maniera facile e semplice per collegare un Arduino (o un ATmega bootloaded) con il tuo Raspberry. Devi, tuttavia, 
fare attenzione alla differenza di tensione tra le due periferiche: il Raspberry è a 3.3V, e l'Arduino invece a 5V. Se 
li colleghi rischi di evocare del magico fumo blu.

Personalmente preferisco costruire un circuito con un Arduino Bootloaded ATmega 328 su una breadboard con un regolatore di tensione 
per prendere la linea a 5V del Raspberry e convertirla in 3.3V. L'ATmega 328 sembra piuttosto soddisfatto di funzionare a 3.3V con un 
cristallo a 16Mhz, e così ottieni un clone di Arduino con una logica a 3.3V.
