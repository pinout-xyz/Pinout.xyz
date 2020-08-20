#!/usr/bin/env python

import json
import re
import sys
import unicodedata
import glob
import markdown

sys.path.insert(0, "../")
BASE_DIR = "../"

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


def load_overlay(overlay):
    try:
        data = markjaml.load(overlay) 
        slug = slugify(data['data']['name'])

        filename = 'v1/detail/{}.json'.format(slug)
        web_url = "https://pinout.xyz/pinout/{}".format(slug),

        data['api_output_file'] = filename
        data['data']['pinout_url'] = web_url

        loaded = data
    except IOError:
        return None

    return loaded

overlays = map(load_overlay, overlays)

for overlay in overlays:
    for t in ['power', 'ground']:
        try:
            overlay['data'][t] = overlay['data'][t].keys()
        except (KeyError, AttributeError):
            pass
    filename = overlay['api_output_file']
    data = json.dumps(overlay['data'], sort_keys=True)
    
    #print("Writing: {}".format(filename))
    #print(data)
    f = open(filename, 'w')
    f.write(data)
    f.close()
