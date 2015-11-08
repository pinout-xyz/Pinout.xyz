#!/usr/bin/env python
import json
import unicodedata
import re
import os
import time
import sys
import pinout
import yaml
import markjaml
import glob

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
	try:
		data = markjaml.load('src/{}/overlay/{}.md'.format(lang,overlay))

		loaded = data['data']
	except IOError:
		return None

	if not 'page_url' in loaded:
		loaded['page_url'] = url_slugify(loaded['name'])

	return overlay, loaded['page_url']

def get_pin_url(pin_num,pinout):
	pin = pinout.pins[str(pin_num)]
	pin_url = pin['name']

	if pin_url == 'Ground':
		return None

	if 'scheme' in pin:
		if 'bcm' in pin['scheme']:
			bcm = pin['scheme']['bcm']
			pin_url = 'gpio{}'.format(bcm)

	return url_slugify('pin{}_{}'.format(pin_num,pin_url))

def generate_for_lang(lang="en-GB"):
	url_lookup = {}

	pinout.load(lang)

	overlays = pinout.settings['overlays']

	overlays_html = ''

	overlays = map(lambda overlay: load_overlay_url(overlay, lang),overlays)

	for pin in range(1,len(pinout.pins)+1):
		pin_url = get_pin_url(pin,pinout)
		if pin_url is None:
			continue

		url_lookup['pin{}'.format(pin)] = '{}'.format(pin_url)

	for url in overlays:
		if url is None:
			continue

		url_lookup['{}'.format(url[0])] = '{}'.format(url[1])

	return url_lookup

def generate_urls(lang="en-GB"):
	languages = [l.replace('src/','') for l in glob.glob('src/*')] #  if not l == 'src/'+lang
	urls = {}
	for lang in languages:
		urls[lang] = generate_for_lang(lang)
	return urls

