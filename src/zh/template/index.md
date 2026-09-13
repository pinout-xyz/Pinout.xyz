# 引路派

## 树莓派引脚导航

本站是一个交互式的树莓派 GPIO 引脚参考工具和使用指南网站。本站还同时收录了 [数百种树莓派扩展板、HAT 和 pHAT 的引脚定义](/boards)。

## 其他相关板卡的引脚定义

我们也为树莓派 Pico 系列开发板制作了引脚定义导航，请点击查看：

* [树莓派 Pico 引脚定义](https://pico.pinout.xyz)
* [树莓派 Pico W 引脚定义](https://picow.pinout.xyz)
* [树莓派 Pico 2 引脚定义](https://pico2.pinout.xyz)
* [树莓派 Pico 2 W 引脚定义](https://pico2w.pinout.xyz)

此外，还有适用于 RP2350A 和 RP2350B 芯片的引脚规划工具：

* [RP2350A QFN-60 引脚定义](https://rp2350a.pinout.xyz)
* [RP2350B QFN-80 引脚定义](https://rp2350b.pinout.xyz)

还有一些实验性的引脚介绍站：

* [迷你版树莓派 40 针引脚定义](https://pi.pinout.xyz)
* [ESP32 C5 DevKitC 引脚定义](https://esp32c5.pinout.xyz)
* [ESP32 C3 DevKitC 引脚定义](https://esp32c3.pinout.xyz)
* [PJRC Teensy 4.0 引脚定义](https://teensy40.pinout.xyz)

## 查看 HATs & pHATs

[查看引路派提供的板卡浏览器](/boards)！你可以使用它查找树莓派扩展板的引脚定义，或探索新的扩展板。如果你是扩展板制造商，我们也很乐意收录你的产品。 [欢迎在 GitHub.com 上贡献代码](https://github.com/pinout-xyz/Pinout.xyz).

## 引脚编号的含义

* GPIO 编号 - 通用输入/输出（General Purpose Input/Output），也称为“BCM”或“博通”编号。它们的字体较大，例如“GPIO 22”。使用 RPi.GPIO 和 GPIO Zero 时应采用这种编号。
* 物理编号 - 也称为板级编号，对应引脚在排针上的实际物理位置。它们是排针旁标注的较小数字，例如“物理引脚 15”。
* WiringPi 编号 - 用于 Gordon Henderson 的 WiringPi 库。当鼠标悬停在引脚上时，这些编号会悬浮显示。
* 初代树莓派编号 - 初代 26 针 Model A 和 Model B 树莓派所使用的另一套 GPIO/BCM 编号。40 针排针兼容这套 26 针定义：1～26 号引脚承载相同的信号，因此仍然适用 26 针扩展板。
