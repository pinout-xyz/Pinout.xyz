#!/usr/bin/env python

import json
import os
import re
import sys
import time
import unicodedata

try:
    import markdown
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install Markdown")


lang = 'en'

pins = None

key_template = {
    'python': '{board_name}_{name}',
    'ruby':   '{board_name}_{name}',
    'spin':   '    {board_name}_{name}',
    'c':      '#define {board_name}_{name}'
}

value_template = {
    'python': ' = {value}',
    'ruby':   ' = {value}',
    'spin':   ' = {value}',
    'c':      ' {value}'
}

comment_prefix = {
    'python': '#',
    'ruby':   '',
    'spin':   '\'',
    'c':      '//'
}


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = value.replace('+', 'PLUS')
    value = value.replace('-', 'MINUS')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '_', value)


def bcm_to_physical(pin):
    pin = pin[3:]
    for idx in pins:
        compare_pin = pins[idx]
        if 'scheme' in compare_pin:
            if 'bcm' in compare_pin['scheme']:
                if compare_pin['scheme']['bcm'] == int(pin):
                    print("Mapping BCM{} to {}".format(pin, str(idx)))
                    return str(idx)


def physical_to_bcm(pin):
    pin = pins[pin]
    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            return str(pin['scheme']['bcm'])
    return None


def physical_to_wiringpi(pin):
    pin = pins[pin]
    if 'scheme' in pin:
        if 'wiringpi' in pin['scheme']:
            return str(pin['scheme']['wiringpi'])
    return None


def physical_to(pin, scheme='bcm'):
    if scheme in ['bcm', 'wiringpi']:
        pin = pins[pin]
        if 'scheme' in pin:
            if scheme in pin['scheme']:
                return str(pin['scheme'][scheme])
    elif scheme == 'physical':
        return pin
    return None


def add_define(key, value):
    global keys, define
    keys.append(key)
    define[key] = value


db = json.load(open('../src/{}/pi-pinout.json'.format(lang)))
pins = db['pins']

define = {}
keys = []

if len(sys.argv) >= 3:

    overlay_file = sys.argv[1]
    pin_scheme   = sys.argv[2]
    output_lang  = sys.argv[3]

    overlay = json.load(open('../src/{}/overlay/{}.json'.format(lang, overlay_file)))

    if 'i2c' in overlay:
        for addr in overlay['i2c']:
            info = overlay['i2c'][addr]

            add_define('ADDR_' + slugify(info['name']).upper(), addr)

    if 'pin' in overlay:
        for pin in overlay['pin']:
            info = overlay['pin'][pin]
            if str(pin).startswith('bcm'):
                pin = bcm_to_physical(pin)


            if 'name' in info:
                name = slugify(info['name']).upper()
            else:
                name = slugify(pins[pin]['name']).upper()

            add_define(name, physical_to(pin, pin_scheme))

    board_name = slugify(overlay['name']).upper()

    print(comment_prefix[output_lang] + ' Pin definitions for ' + overlay['name'])
    print(comment_prefix[output_lang] + ' Using the {} pin numbering scheme'.format(pin_scheme))

    row_length = 0

    for name in define:
        key = key_template[output_lang].format(
            board_name = board_name,
            name = name
        )
        row_length = max(len(key), row_length)


    for name in keys:
        key = key_template[output_lang].format(
            board_name = board_name,
            name = name
        )

        value = value_template[output_lang].format(value = define[name])

        value = value.rjust(row_length - len(key) + len(value), ' ')

        print(key+value)
