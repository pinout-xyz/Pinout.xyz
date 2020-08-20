#!/usr/bin/env python

import json
import re
import sys
import os
import glob
import unicodedata
from PIL import Image, ImageFont, ImageDraw


sys.path.insert(0,"../")
BASE_DIR = "../"

SOL_BLUE = (38, 139, 210)
SOL_PINK = (195, 38, 114)
SOL_PURPLE = (108, 113, 196)
SOL_YELLOW = (181, 137, 0)
SOL_GREEN = (133, 153, 0)
SOL_RED = (220, 50, 47)
SOL_BG = (0xcc, 0xcc, 0xcc) #586e75

SOL_BG = tuple([int(x * 1.2) for x in SOL_BG])

LOGO_PALETTE = [
    (51, 51, 51),
    (98, 221, 20),
    (58, 130, 12),
    (229, 4, 56),
    (171, 3, 42),
    (204, 6, 52),
]

LOGO_TEXT = "Pinout.xyz"

LOGO = [0,0,1,0,
        3,5,2,1,
        5,5,5,0,
        4,4,4,0]

LOGO_FONT = ImageFont.truetype("Lato-Semibold.ttf", 21)
TEXT_FONT = ImageFont.truetype("Lato-Medium.ttf", 16)

try:
    import markdown
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install Markdown")

import markjaml
import pinout

output_dir = "v1/img"

reload(sys)
sys.setdefaultencoding('utf8')

lang = "en"

if len(sys.argv) > 1:
    lang  = sys.argv[1]

pinout.load(lang)

overlays = glob.glob("{}src/{}/overlay/*.md".format(BASE_DIR, lang))

pages = {}


def cssify(value):
    value = slugify(value)
    if value[0] == '3' or value[0] == '5':
        value = 'pow' + value

    return value


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '_', value)


def load_overlay(overlay):
    try:
        data = markjaml.load(overlay)['data']
        slug = slugify(data['name'])
        data['slug'] = slug

        if "pin" in data:
            for pin in data["pin"].keys():
                if str(pin).startswith("bcm"):
                    data["pin"][pinout.bcm_to_physical(str(pin).replace("bcm",""))] = data["pin"][pin]

        return data
    except IOError:
        print('Not found: {}/src/{}/overlay/{}.md'.format(BASE_DIR, lang, overlay))
        return None


def load_md(filename):
    filename = 'src/{}/{}'.format(lang, filename)
    try:
        html = markdown.markdown(open(filename).read(), extensions=['fenced_code'])

        return html
    except IOError:
        print('Unable to load markdown from {}'.format(filename))
        return ''


overlays = map(load_overlay, overlays)

uses = {}

logo = Image.new("RGBA", (4, 4), (0, 0, 0, 0))
for x in range(4):
    for y in range(4):
        idx = (y*4) + x
        idx = LOGO[idx]
        col = LOGO_PALETTE[idx]
        logo.putpixel((x, y), col)

for overlay in overlays:
    if not overlay['class'] == "board" or "pin" not in overlay:
        continue
    img = Image.new("RGBA", (20, 7), (255, 255, 255, 255))
    slug = overlay['slug']
    pins = overlay['pin']
    name = overlay['name']
    power = []
    ground = []
    i2c = ""

    if "power" in overlay and overlay["power"] is not None:
        power = overlay["power"]

    if "ground" in overlay:
        ground = overlay["ground"]

    if "i2c" in overlay:
        i2c = ", ".join(overlay["i2c"].keys())

    print("Processing: {}".format(name))
    for pin_number in range(1,41):
        if str(pin_number) not in uses:
            uses[str(pin_number)] = 0

        y = 1 - ((pin_number-1) % 2)
        x = (pin_number-1) // 2
        
        if pin_number in [6, 9, 14, 20, 25, 30, 34, 39]:
            if str(pin_number) in ground:
                img.putpixel((x, y), (0, 0, 0, 255))
            else:
                img.putpixel((x, y), (196, 196, 128, 255))

        elif pin_number in [1, 17] and str(pin_number) in power: # 3v3
            img.putpixel((x, y), SOL_YELLOW)

        elif pin_number in [2, 4] and str(pin_number) in power:  # 5v
            img.putpixel((x, y), SOL_RED)

        elif pin_number in [14, 15] and str(pin_number) in pins: # TX / RX
            img.putpixel((x, y), SOL_PURPLE)
            uses[str(pin_number)] += 1

        elif pin_number in [3, 5, 27, 28] and str(pin_number) in pins: # SDA/SCL for i2c0/1
            img.putpixel((x, y), SOL_BLUE)
            uses[str(pin_number)] += 1

        elif pin_number in [19, 21, 23, 24, 26, 35, 38, 40] and str(pin_number) in pins: # SPI
            img.putpixel((x, y), SOL_PINK)
            uses[str(pin_number)] += 1

        elif str(pin_number) in pins:
            img.putpixel((x, y), SOL_GREEN)
            uses[str(pin_number)] += 1

        else:
            img.putpixel((x, y), SOL_BG)

    #pinout = img.rotate(90, expand=True)
    #img = img.crop((1, 1, 21, 3))
    #img = Image.new("RGBA", (20, 7), (0, 0, 0, 0))
    #img.paste(pinout, (0, 0, 21, 3))
    img.paste(logo, (0, 3))
    img = img.resize((400,140), Image.NEAREST)
    draw = ImageDraw.Draw(img)
    
    o_y = 60
    draw.text((100, o_y), name, (60, 60, 60), font=LOGO_FONT)
    o_y += 25
    if i2c != "":
        draw.text((100, o_y), i2c, (60, 60, 60), font=TEXT_FONT)
        o_y += 20
    draw.text((100, o_y), LOGO_TEXT, (60, 60, 60), font=TEXT_FONT)
    img.save(os.path.join(output_dir, slug + ".png"), "png", transparent=0)

#print(uses)
maxuses = 0
for pin in uses.keys():
    count = uses[pin]
    if count > maxuses:
        maxuses = count

maxuses = float(maxuses)
for pin in uses.keys():
    uses[pin] /= maxuses
    uses[pin] *= 255
    uses[pin] = int(uses[pin])

imguses = Image.new("RGBA", (20, 7), (255, 255, 255, 255))

for pin_number in range(1,41):
    y = 1 - (pin_number-1) % 2
    x = (pin_number-1) // 2
    use = uses[str(pin_number)]
    if pin_number in [6, 9, 14, 20, 25, 30, 34, 39]:
        imguses.putpixel((x, y), (0, 0, 0, 255))
    else:
        imguses.putpixel((x, y), (use, 0, 255-use, 255))

imguses.paste(logo, (0, 3))
imguses = imguses.resize((400,140), Image.NEAREST)
draw = ImageDraw.Draw(imguses)

o_y = 60
draw.text((100, o_y), "Raspberry Pi GPIO Heatmap", (60, 60, 60), font=LOGO_FONT)
o_y += 25
draw.text((100, o_y), LOGO_TEXT, (60, 60, 60), font=TEXT_FONT)

imguses.save(os.path.join(output_dir, "pinout_heatmap.png"), "png")