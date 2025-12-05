此引脚可被复用为 UART 接收引脚，即 RX 引脚。UART 引脚就是通常所说的“串口”，默认作为树莓派的终端输出。连上合适的串口线的话，可以通过这个串口终端使用命令行控制树莓派。

UART 引脚可以用来配置没有显示屏的树莓派，以进行联网等操作。

UART 还可以用来连接串行 GPS 模块或者 PM5003 之类的传感器，但得先确保在 raspi-config 中关闭了树莓派的串口终端。

在树莓派 3 和 4 上，UART 默认用来与蓝牙通信。为了稳定运行，最好在 "/boot/config.txt" 中添加 "dtoverlay=miniuart-bt" 这一配置。

[继续了解 UART](/pinout/uart)

[树莓派 UART 官方文档](https://www.raspberrypi.org/documentation/configuration/uart.md)
