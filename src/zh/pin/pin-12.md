GPIO 18 属于 PCM 模块，用来向外部音频设备输出时钟信号，比如 DAC 芯片。

GPIO 18 的 PWM0 输出尤其有用。如果配合一些快速、直接内存访问的技巧，可以用于驱动一些有特殊时钟要求的设备。比如：[Unicorn HAT](/pinout/unicorn_hat) 上的 WS2812 LED 就用到了这一方案。
