#!/usr/bin/env python

import json
import re
import sys
import glob
import unicodedata

sys.path.insert(0, "../")
BASE_DIR = "../"

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

def pimoroni_get_shop_handle(slug):
    """Maps a Pinout.xyz slug to a Pimoroni shop handle
    
    This is a customisation for shop.pimoroni.com which probably
    wont be of use in any other context.
    """
    pimoroni_shop_handles = {
        'unicorn_hat': 'unicorn-hat'
    }
    if slug in pimoroni_shop_handles:
        return pimoroni_shop_handles[slug]
    return None

def load_overlay(overlay):
    try:
        data = markjaml.load(overlay)['data']
        slug = slugify(data['name'])
        return {
            'name': data['name'],
            'class': data['class'],
            'detail': "/v1/detail/{}.json".format(slug),
            'url': "/pinout/{}".format(slug),
            #'pimoroni.shop-handle': pimoroni_get_shop_handle(slug)
        }
    except IOError:
        return None


def load_md(filename):
    filename = '../src/{}/{}'.format(lang, filename)
    try:
        html = markdown.markdown(open(filename).read(), extensions=['fenced_code'])

        return html
    except IOError:
        print('Unable to load markdown from {}'.format(filename))
        return ''


overlays = map(load_overlay, overlays)

print(json.dumps(overlays, sort_keys=True))
