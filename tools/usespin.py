#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

from pinoutxyz import documents, overlays
from pinoutxyz.pins import Pins

if len(sys.argv) < 2:
    sys.exit("Usage {} <physical pin>".format(sys.argv[0]))

pins = Pins('.', 'en')

pin_physical = str(sys.argv[1])
pin_bcm = "bcm{}".format(pins.physical_to_bcm(pin_physical))

message = "Searching for pin: {physical}, {bcm}".format(physical=pin_physical, bcm=pin_bcm)
print(message)
print('-' * len(message))

count = 0

for path in overlays.paths('.', 'en'):
    loaded = documents.load(path)['data']

    for key in ('pin', 'power', 'ground'):
        entries = loaded.get(key) or {}
        for candidate in (pin_physical, int(pin_physical), pin_bcm):
            if candidate not in entries:
                continue
            pin = entries[candidate] or {}
            count += 1
            print("{type}: {name}: {desc} (dir:{direction} pol:{active})".format(
                type=key,
                name=loaded['name'],
                desc=pin.get('name', ''),
                direction=pin.get('direction', 'unknown'),
                active=pin.get('active', 'unknown')))
            break

print()
print("Found {} boards using this pin".format(count))
