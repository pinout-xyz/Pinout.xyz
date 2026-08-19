<!--
---
name: LetsTrust-TPM
class: board
type: other
formfactor: Custom
manufacturer: pi3g
collected: Other
description: Infineon SLB9670 TPM2.0 daughter board for the Raspberry PI
url: https://buyzero.de/products/letstrust-hardware-tpm-trusted-platform-module
schematic: http://www.letstrust.de/uploads/letstrust-v2.0.schematic.pdf
buy: https://buyzero.de/products/letstrust-hardware-tpm-trusted-platform-module
image: 'letstrust-tpm.png'
pincount: 10
eeprom: no
power:
  '17':
ground:
  '20':
  '25':
pin:
  '18':
    name: Reset
    mode: output
    active: low
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '22':
    name: PIRQ
    mode: input
    active: low
  '26':
    mode: spi
-->
# LetsTrust-TPM

LetsTrust-TPM is a TPM2.0 daughter board for the Raspberry Pi platform based on an Infineon SLB9670 chip.

It is compatible with all Raspberry Pi models and probably the smallest available addon board on the market.

The TPM can be used e.g. as a secure keystore or as an hardware random number generator.

In order to use it your kernel must have the following options enabled:
```kernelconfig
  CONFIG_HW_RANDOM_TPM=m
  CONFIG_TCG_TPM=m
  CONFIG_TCG_TIS_CORE=m
  CONFIG_TCG_TIS_SPI=m
  CONFIG_SECURITYFS=y
```		
and a suitable device tree overlay:
```dts
  slb9670: slb9670@0{
  	compatible = "infineon,slb9670";
  	reg = <1>;	/* CE1 */
  	#address-cells = <1>;
  	#size-cells = <0>;
  	spi-max-frequency = <32000000>;
  	status = "okay";
  };
```

Per default CE1 is used as chip select, CE0 can also be used by re-soldering a 0-ohm resistor.

A full dts overlay is available <a href="https://www.letstrust.de/uploads/letstrust-tpm-overlay.dts">here</a>,
or you can also find a pre-compiled image with TPM support and the complete build-instructions at <a href=https://www.letstrust.de>letstrust.de</a>.
