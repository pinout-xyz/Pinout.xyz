<!--
---
name: UART
class: interface
type: pinout
description: Raspberry Pi UART pinleri
url: http://elinux.org/RPi_Serial_Connection
pincount: 18
pin:
  '8':
    name: TXD / Transmit
    direction: output
    active: high
  '10':
    name: RXD / Receive
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
# UART - Universal Asenkron Verici/Alcı

### WiringPi'deki 2 UART pini Pin 15 ve 16'dır

UART Arduino, veya bootload edilmiş bir ATmega ile kolayca iletişim kurmanızı sağlayacak bir arayüzdür. Yalnız bu iletişimi kurarken dikkat etmeniz gereken bazı hususlar var. Raspberry Pi 3.3v iken Arduino 5v'tur. Bunları akımları eşitlemeden bağlarsanız cihazlarınızdan dumanlar tütmeye başlayabilir

Örneğin Arduino bootload edilmiş ATmega 328 devresini breadboard'a kurup bir akım regülatörü ile Raspberry Pi'nin 5v yolunu 3.3 v'a dönüştürebilirsiniz. Bu sayede 3.3v logic'ine sahip bir Arduino klonunuz olacak.
