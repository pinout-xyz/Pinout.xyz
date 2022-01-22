<!--
---
name: 1-WIRE 单线接口
class: interface
type: pinout
description: 树莓派单线数据接口
url: https://www.kernel.org/doc/Documentation/w1/w1.generic
pin:
  'bcm4':
    name: Data
-->
# W1-GPIO - 单线数据接口

树莓派的单线数据接口是只需要一根线就能通讯的总线，通常用来与某些传感器通讯。

树莓派支持在任何引脚上启用单线数据接口，但默认使用 GPIO 4。

要启用单线数据接口，你需要编辑 `/boot/config.txt` 并添加以下信息，然后重启树莓派：

```
dtoverlay=w1-gpio
```

或者，如果你想用除了 GPIO 4 以外的其他引脚：

```
dtoverlay=w1-gpio,gpiopin=x
```

你也可以用 `raspi-config` 命令来配置单线数据接口，或者以下命令：

```
sudo modprobe w1-gpio
```

4.9.28 以后的内核版本可以动态加载引脚配置，还可以同时创建多个单线数据接口：

```
sudo dtoverlay w1-gpio gpiopin=4 pullup=0  # header pin 7
sudo dtoverlay w1-gpio gpiopin=17 pullup=0 # header pin 11
sudo dtoverlay w1-gpio gpiopin=27 pullup=0 # header pin 13
```

执行了以上任意一种配置步骤后，即可用下面的命令查看树莓派已经识别的所有单线数据接口：

```
ls /sys/bus/w1/devices/
```

通常情况下，使用单线数据接口时，需要添加一个 4.7kΩ 的上拉电阻，上拉到 3.3V（比如引脚 1 或者 17）。你也可以通过其他方法把单线数据接口的传感器连到树莓派上，比如用一个 I2C 转单线的转接板。
