#!/usr/bin/env python

import json
import re
import sys
import unicodedata

try:
    import markdown
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install Markdown")

import markjaml
import pinout


reload(sys)
sys.setdefaultencoding('utf8')

lang = "en"

if len(sys.argv) > 1:
    lang  = sys.argv[1]

pinout.load(lang)

overlays = pinout.settings['overlays']

pages = {}


def cssify(value):
    value = slugify(value);
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
        data = markjaml.load('src/{}/overlay/{}.md'.format(lang, overlay))

        loaded = data['data']
    except IOError:
        return None


    details = []

    if 'manufacturer' in loaded:
        details.append('* Made by ' + loaded['manufacturer'])

    if 'pincount' in loaded:
        pincount = int(loaded['pincount'])
        if pincount == 40:
            details.append('* HAT form-factor')
        elif pincount == 38:
            details.append('* pHAT form-factor')
        elif pincount == 26:
            details.append('* Classic 26-pin')
        else:
            details.append('* {} pin header'.format(pincount))

    if 'pin' in loaded:
        uses_5v = False
        uses_3v = False
        uses = 0
        for pin in loaded['pin']:
            pin = str(pin)
            if pin.startswith('bcm'):
                pin = pinout.bcm_to_physical(pin[3:])

            if pin in pinout.pins:
                actual_pin = pinout.pins[pin]

                if actual_pin['type'] in ['+3v3', '+5v', 'GND']:
                    if actual_pin['type'] == '+3v3':
                        uses_3v = True
                    if actual_pin['type'] == '+5v':
                        uses_5v = True
                else:
                    uses += 1

        if uses > 0:
            details.append('* Uses {} GPIO pins'.format(uses))

        if '3' in loaded['pin'] and '5' in loaded['pin']:
            pin_3 = loaded['pin']['3']
            pin_5 = loaded['pin']['5']
            if 'mode' in pin_3 and 'mode' in pin_5:
                if pin_3['mode'] == 'i2c' and pin_5['mode'] == 'i2c':
                    details.append('* Uses I2C')

    if 'url' in loaded:
        details.append('* [More Information]({url})'.format(url=loaded['url']))

    if 'github' in loaded:
        details.append('* [GitHub Repository]({url})'.format(url=loaded['github']))

    if 'buy' in loaded:
        details.append('* [Buy Now]({url})'.format(url=loaded['buy']))

    if not 'page_url' in loaded:
        loaded['page_url'] = slugify(loaded['name'])

    pages[loaded['page_url']] = loaded
    return loaded


def load_md(filename):
    filename = 'src/{}/{}'.format(lang, filename)
    try:
        html = markdown.markdown(open(filename).read(), extensions=['fenced_code'])

        return html
    except IOError:
        print('Unable to load markdown from {}'.format(filename))
        return ''


overlays = map(load_overlay, overlays)

print(json.dumps(overlays))
