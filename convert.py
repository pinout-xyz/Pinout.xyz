import json, sys

db = json.load(open('pi-pinout.db'))


def from_phys(phys, mode="bcm"):
    pin = db['pins'][str(phys)]
    if 'scheme' in pin:
        if mode in pin['scheme']:
            return int(pin['scheme'][mode])
    return None


def to_phys(pin, mode="bcm"):
    for pin in db['pins']:
        if 'scheme' in db['pins'][pin]:
            if mode in db['pins'][pin]['scheme']:
                return int(pin)
    return None


pin = int(sys.argv[1])

mode = 'bcm'

if len(sys.argv) > 2:
    mode = sys.argv[2]

print("Pin {} is {}: {}".format(pin, mode.upper(), from_phys(pin, mode)))

