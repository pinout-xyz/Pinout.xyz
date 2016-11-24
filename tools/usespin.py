import sys
sys.path.insert(0,".")
import os
os.chdir("../")

import markjaml
import glob
import pinout

reload(sys)
sys.setdefaultencoding('utf-8')


pinout.load()

if len(sys.argv) < 2:
    print("Usage {} <physical pin>".format(sys.argv[0]))
    sys.exit(1)

find_pin = sys.argv[1]

files = glob.glob("src/en/overlay/*.md")

pin_physical = str(find_pin)
pin_bcm = "bcm{}".format(pinout.physical_to_bcm(pin_physical))

msg = "Searching for pin: {physical}, {bcm}".format(physical=pin_physical, bcm=pin_bcm)
print(msg)
print(''.join('-' for x in msg))

count = 0

for file in files:
    #print("Loading: {}".format(file))
    loaded = markjaml.load(file)

    if "data" not in loaded:
        continue

    data = loaded["data"]

    if "class" not in data or "pin" not in data:
        continue  
  
    if data["class"] in ["board", "interface"]:
        pin = None

        if pin_bcm in data["pin"]:
            pin = data["pin"][pin_bcm]

        if pin_physical in data["pin"]:
            pin = data["pin"][pin_physical]

        if pin is not None:
            print("{type}: {name}: {desc} (dir:{direction} pol:{active})".format(
                type=data["class"],
                name=data["name"],
                desc=pin["name"],
                direction=pin["direction"] if "direction" in pin else "unknown",
                active="active {}".format(pin["active"]) if "active" in pin else "unknown"
                ))

            count += 1

print(''.join('-' for x in msg))

if count > 0:
    print("Found {count} boards using physical pin: {physical}".format(count=count, physical=pin_physical))
else:
    print("No boards use this pin!")
