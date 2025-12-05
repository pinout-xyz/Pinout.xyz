<!--
---
name: UART
class: interface
type: pinout
description: Raspberry Pi UART pins
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
    name: CTS / Clear to Send
    direction: both
    active: high
  '11':
    name: RTS / Request to Send
    direction: both
    active: high
  '27':
    name: TXD / Transmit
    direction: output
    active: high
  '28':
    name: RXD / Receive
    direction: input
    active: high
  '3':
    name: CTS / Clear to Send
    direction: both
    active: high
  '5':
    name: RTS / Request to Send
    direction: both
    active: high
  '7':
    name: TXD / Transmit
    direction: output
    active: high
  '29':
    name: RXD / Receive
    direction: input
    active: high
  '31':
    name: CTS / Clear to Send
    direction: both
    active: high
  '26':
    name: RTS / Request to Send
    direction: both
    active: high
  '24':
    name: TXD / Transmit
    direction: output
    active: high
  '21':
    name: RXD / Receive
    direction: input
    active: high
  '19':
    name: CTS / Clear to Send
    direction: both
    active: high
  '23':
    name: RTS / Request to Send
    direction: both
    active: high
  '32':
    name: TXD / Transmit
    direction: output
    active: high
  '33':
    name: RXD / Receive
    direction: input
    active: high
-->
# UART - 通用异步收发器
---
### BCM 模式下的 UART 引脚: 14, 15
### Wiring Pi 模式下的 UART 引脚: 15, 16
---

UART 是一个异步的串行通讯协议，也就是说，它按顺序一个一个地发送或接受比特位。

异步通信意味着无需独立的时钟同步线，发送方即可发送数据给接收方。二者需要使用相同的时钟参数（波特率），并且发送方需要在每个字节前添加一个特殊的“起始位”，这样才能实现通讯。

通常，我们可以通过 UART 串口终端来直接控制树莓派，或者读取内核启动信息，而且这个功能是默认开启的。

UART 同样可以与 Arduino、ESP866 等其他单片机设备进行通讯，但要注意双方的 UART 逻辑电平高低。比如，树莓派 UART 是 3.3V 的，而传统 Arduino 是 5V 的，如果把两者的 UART 直接连在一起，说不定你的树莓派就要冒烟了。

树莓派 2 代和 3 代有两个 UART，分别是 UART0 和 UART1。树莓派 4 有四个额外的 UART 接口，但只有 UART0 和 UART1 是默认启用的（GPIO 引脚 14 和 15）。其他的 UART 可以通过修改设备描述树启用。

如果你安装了 WiringPi-Python，可以参考下列 python 代码。它以 9600 的波特率打开了树莓派的 UART，并输出 `hello world`。

```python
import wiringpi
wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
wiringpi.serialPuts(serial,'hello world!')
```
