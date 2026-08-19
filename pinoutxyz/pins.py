import os

import yaml

FUNCTIONS_FILE = 'common/pin-functions.yaml'
PINOUT_FILE = 'src/{}/template/pinout.yaml'

MODES = {
    '1wire': '1wire',
    '1-wire': '1wire',
    'chipselect': 'chipselect',
    'cs': 'chipselect',
    'eeprom_wp': 'eeprom_wp',
    'gpio': 'gpio',
    'i2c': 'i2c',
    'i2s': 'pcm',
    'input': 'input',
    'input/output': 'gpio',
    'output': 'output',
    'pcm': 'pcm',
    'pwm': 'pwm',
    'spi': 'spi',
    'uart': 'uart',
}


def sanitize_mode(mode):
    return MODES.get(str(mode).strip().lower())


class Pins:
    def __init__(self, root, lang):
        self._pins = yaml.safe_load(open(os.path.join(root, PINOUT_FILE.format(lang))).read())['pins']
        self.functions = yaml.safe_load(open(os.path.join(root, FUNCTIONS_FILE)).read())

    def __len__(self):
        return len(self._pins)

    def __iter__(self):
        return iter(self._pins)

    def __contains__(self, pin):
        return pin in self._pins

    def __getitem__(self, pin):
        return self._pins[pin]

    def numbers(self):
        return range(1, len(self._pins) + 1)

    def ground(self):
        return [int(number) for number in self._pins if self._pins[number]['type'] == 'GND']

    def bcm(self, pin):
        return self[str(pin)].get('scheme', {}).get('bcm')

    def physical_from(self, pin, scheme='bcm'):
        if scheme == 'physical':
            return pin
        if scheme not in ('bcm', 'wiringpi'):
            return None
        for number in self._pins:
            schemes = self._pins[number].get('scheme', {})
            if schemes.get(scheme) == int(pin):
                return str(number)
        return None

    def physical_to(self, pin, scheme='bcm'):
        if scheme == 'physical':
            return pin
        if scheme not in ('bcm', 'wiringpi'):
            return None
        value = self[pin].get('scheme', {}).get(scheme)
        return None if value is None else str(value)

    def bcm_to_physical(self, pin):
        return self.physical_from(pin, 'bcm')

    def wiringpi_to_physical(self, pin):
        return self.physical_from(pin, 'wiringpi')

    def physical_to_bcm(self, pin):
        return self.physical_to(pin, 'bcm')

    def physical_to_wiringpi(self, pin):
        return self.physical_to(pin, 'wiringpi')
