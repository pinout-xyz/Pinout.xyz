#!/usr/bin/env python
import json
import markdown, gfm
import unicodedata
import re

overlays = ['pibrella','explorerhat']

template = open('template/layout.html').read()

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
		loaded = json.load(open('overlay/{}.json'.format(overlay)))
	except IOError:
		return None

	loaded['long_description'] = load_text(overlay)
	return loaded

def load_text(overlay):
	try:
		return markdown.markdown(open('description/overlay/{}.md'.format(overlay)).read(), extensions=[gfm.HiddenHiliteExtension([]),'fenced_code'])
	except IOError:
		return None

def render_overlay_page(overlay):
	if overlay == None:
		return ''
	return '<article id="{}">{}</article>'.format(slugify(overlay['name']),overlay['long_description'])

db = json.load(open('pi-pinout.json'))

pins = db['pins']

html_odd = ''
html_even = ''

overlay_text = map(load_text,overlays)
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

pages = map(render_overlay_page,overlays)

html = '''<ul class="bottom">
{}</ul>
<ul class="top">
{}</ul>'''.format(html_odd, html_even)

html = template.replace('{{nav}}',html).replace('{{content}}','\n'.join(pages))

print(html)
