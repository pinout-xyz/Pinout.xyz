#!/usr/bin/env python

import glob
import os
import re
import sys
import unicodedata

import markjaml
import pinout


reload(sys)
sys.setdefaultencoding('utf8')


def url_slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '_', value)


def load_overlay_url(overlay, lang):
    loaded = None
    print("Info: Trying {}".format('src/{}/overlay/{}.md'.format(lang, overlay)))
    try:
        data = markjaml.load('src/{}/overlay/{}.md'.format(lang, overlay))

        loaded = data['data']
    except IOError:
        try:
            print("Warning: Falling back to {}".format('src/{}/translate/{}.md'.format(lang, overlay)))
            data = markjaml.load('src/{}/translate/{}.md'.format(lang, overlay))
            loaded = data['data']
        except IOError:
            return None

    if loaded is None:
        print("Fatal: Invalid overlay formatting.")
        sys.exit(0)

    if not 'page_url' in loaded:
        loaded['page_url'] = url_slugify(loaded['name'])

    return overlay, loaded['page_url']


def get_pin_url(pin_num, pinout):
    pin = pinout.pins[str(pin_num)]
    pin_url = pin['name']

    if pin_url == 'Ground':
        return None

    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            bcm = pin['scheme']['bcm']
            pin_url = 'gpio{}'.format(bcm)

    return url_slugify('pin{}_{}'.format(pin_num, pin_url))


def generate_for_lang(lang="en"):
    url_lookup = {}

    pinout.load(lang)

    overlays = pinout.settings['overlays']

    base_url = pinout.get_setting('base_url', '/pinout/')

    domain = pinout.get_setting('domain', 'pinout.xyz')

    overlays_html = ''

    overlays = map(lambda overlay: load_overlay_url(overlay, lang), overlays)

    for pin in range(1, len(pinout.pins)+1):
        pin_url = get_pin_url(pin, pinout)
        if pin_url is None:
            continue

        url_lookup['pin{}'.format(pin)] = '//{domain}{base_url}{url}'.format(domain=domain, base_url=base_url, url=pin_url)

    for url in overlays:
        if url is None:
            continue

        url_lookup['{}'.format(url[0])] = '//{domain}{base_url}{url}'.format(domain=domain, base_url=base_url, url=url[1])


    url_lookup['index'] = '//{}'.format(domain)

    url_lookup['boards'] = '//{}/boards'.format(domain)

    return url_lookup


def generate_urls(lang="en"):
    languages = [l.replace('src/', '') for l in glob.glob('src/??') if os.path.isdir(l)] #  if not l == 'src/'+lang
    urls = {}
    for lang in languages:
        urls[lang] = generate_for_lang(lang)
    return urls
