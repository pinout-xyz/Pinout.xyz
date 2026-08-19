import os

from . import overlays, settings
from .pins import Pins
from .slugs import slugify


def pin_url(pins, number):
    pin = pins[str(number)]

    if number in pins.ground():
        return None

    name = pin['name']
    bcm = pins.bcm(number)
    if bcm is not None:
        name = 'gpio{}'.format(bcm)

    return slugify('pin{}_{}'.format(number, name))


def for_language(root, lang):
    conf = settings.load_settings(root, lang)
    pins = Pins(root, lang)

    site = 'https://{}'.format(conf.get('domain') or 'pinout.xyz')
    base_url = conf.get('base_url') or '/pinout/'
    site_url = conf.get('site_url') or ''

    found = {}

    for number in pins.numbers():
        url = pin_url(pins, number)
        if url is not None:
            found['pin{}'.format(number)] = site + base_url + url

    for path in overlays.paths(root, lang):
        data = overlays.load(path)
        found[data['src']] = site + base_url + data['page_url']

    found['index'] = site + site_url
    found['boards'] = '{}{}/boards'.format(site, site_url)

    return found


def alternates(root='.'):
    return {lang: for_language(root, lang) for lang in settings.languages(root)}
