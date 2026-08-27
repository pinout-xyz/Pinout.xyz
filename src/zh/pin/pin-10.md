此引脚还兼作 UART 接收引脚 RX，通常也称为“串口”。使用 [合适的串口线](https://elinux.org/RPi_Serial_Connection)，并在 raspi-config 中启用串口后，即可通过命令行控制树莓派。

在配置“无头”树莓派（即未连接显示器的树莓派）时，UART 引脚非常有用。

UART 还可用于与串口 GPS 模块或 PMS5003 等传感器通信，但必须先在 raspi-config 中禁用串口控制台。

在树莓派 3、树莓派 4、树莓派 Zero W 和树莓派 Zero 2 W 上，蓝牙模块会占用此 UART。这些引脚连接至 mini UART，其波特率会随 VPU 核心时钟变化。在 `/boot/firmware/config.txt` 中添加 `enable_uart=1` 可固定该时钟；添加 `dtoverlay=miniuart-bt` 则会交换两个 UART，以便用户使用该UART，但这样会降低蓝牙的波特率。

树莓派 5 没有 mini UART。这些引脚连接的是完整的 PL011 UART，可通过 `dtoverlay=uart0-pi5` 启用；串口控制台则位于专用的三针调试排针上。

所有 UART 均仅支持 3.3V 电平，如果连接到 5V 电平上，会损坏树莓派。

[进一步了解 UART](/pinout/uart)

[树莓派 UART 文档](https://www.raspberrypi.com/documentation/computers/configuration.html#uarts)
