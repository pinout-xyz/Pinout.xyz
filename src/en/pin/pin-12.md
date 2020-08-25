GPIO 18 is used by PCM to provide a clock signal to an external audio device such as a DAC chip.

The PWM0 output of GPIO 18 is particularly useful, in combination with some fast, direct memory access trickery, for driving devices with very specific timings. The WS2812 LEDs on the [Unicorn HAT](/pinout/unicorn_hat) are a good example of this in action.