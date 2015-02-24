#!/usr/bin/env python
import json
import unicodedata
import re

overlays = ['pibrella','break']

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
	    return json.load(open('overlay/{}.json'.format(overlay)))
	except IOError:
		return None

db = json.load(open('pi-pinout.json'))

pins = db['pins']

html_odd = ''
html_even = ''

overlays = map(load_overlay,overlays)

def render_alternate(handle, name):
	handle = slugify(handle.lower())
	return '<span class="alternate legend_{}">{}</span>'.format(handle,name)

def render_pin(pin_num):
	pin = pins[str(pin_num)]
	pin_type = list([x.strip() for x in pin['type'].lower().split('/')])
	pin_url = pin['name']
	pin_name = pin['name']
	alternates = []

	for overlay in overlays:
		if overlay != None:
			if str(pin_num) in overlay['pin']:
			    alternates.append(render_alternate(overlay['name'],overlay['pin'][str(pin_num)]['name']))

	if 'scheme' in pin:
		if 'bcm' in pin['scheme']:
			bcm = pin['scheme']['bcm']
			pin_subname = ''
			#if pin_url == '':
			pin_url = 'gpio{}'.format(bcm)
			if pin['name'] != '':
			    pin_subname = '<small>({})</small>'.format(pin['name'])
			pin_name = 'GPIO {} {}'.format(bcm, pin_subname)
		if 'wiringpi' in pin['scheme']:
			wiringpi = pin['scheme']['wiringpi']
			alternates.append(render_alternate('wiringpi','Wiring Pi pin {}'.format(wiringpi)))

	#print(pin_type)

	return '<li class="pin{} {}"><a href="/pindb/pin{}_{}"><span class="default"><span class="phys">{}</span> {}</span><span class="pin"></span>\n{}</a></li>\n'.format(
		pin_num,
		' '.join(map(slugify,pin_type)),
		pin_num,
		slugify(pin_url),
		pin_num,
		pin_name,
		'\n'.join(alternates)
		)

for odd in range(1,len(pins),2):
	html_odd += render_pin(odd)
	html_even += render_pin(odd+1)

html = '<nav class="gpio" id="gpio">\n<ul class="bottom">\n{}</ul>\n<ul class="top">\n{}</ul>\n</nav>'.format(html_odd, html_even)

print(html)
