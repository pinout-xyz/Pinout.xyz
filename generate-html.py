#!/usr/bin/env python
import json
import markdown
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

	loaded['long_description'] = load_md('description/overlay/{}.md'.format(overlay))
	return loaded

def load_md(filename):
	try:
		html = markdown.markdown(open(filename).read(), extensions=['fenced_code'])

		return html
		#return markdown.markdown(open(filename).read(), extensions=[gfm.HiddenHiliteExtension([]),'fenced_code'])
	except IOError:
		return None

def render_pin_text(pin_num, pin_url, pin_name, pin_subtext):
	return '<article class="{}"><h1>{}</h1>{}{}</article>'.format(pin_url,pin_name,pin_subtext,load_md('description/pins/pin-{}.md'.format(pin_num)))

def render_overlay_page(overlay):
	if overlay == None:
		return ''
	return '<article class="page_{}">{}</article>'.format(slugify(overlay['name']),overlay['long_description'])

db = json.load(open('pi-pinout.json'))

pins = db['pins']

html_odd = ''
html_even = ''

overlays = map(load_overlay,overlays)

pages = [render_overlay_page({'name':'Index','long_description':load_md('description/index.md')})]
pages += map(render_overlay_page,overlays)

def render_alternate(handle, name):
	handle = slugify(handle.lower())
	return '<span class="alternate legend_{}">{}</span>'.format(handle,name)

def render_pin(pin_num):
	pin = pins[str(pin_num)]
	pin_type = list([x.strip() for x in pin['type'].lower().split('/')])
	pin_url = pin['name']
	pin_name = pin['name']
	pin_text_name = pin['name']

	pin_subtext = []
	alternates = []


	pin_subtext.append('Physical pin {}'.format(pin_num))

	for overlay in overlays:
		if overlay != None:
			if str(pin_num) in overlay['pin']:
			    alternates.append(render_alternate(overlay['name'],overlay['pin'][str(pin_num)]['name']))

	if 'scheme' in pin:
		if 'bcm' in pin['scheme']:
			bcm = pin['scheme']['bcm']
			pin_subname = ''
			pin_subname_text = ''
			#if pin_url == '':
			pin_url = 'gpio{}'.format(bcm)
			if pin['name'] != '':
			    pin_subname = '<small>({})</small>'.format(pin['name'])
			    pin_subname_text = '({})'.format(pin['name'])
			pin_name = 'BCM {} {}'.format(bcm, pin_subname)
			pin_text_name = 'BCM {} {}'.format(bcm, pin_subname_text)
			pin_subtext.append('BCM pin {}'.format(bcm))
		if 'wiringpi' in pin['scheme']:
			wiringpi = pin['scheme']['wiringpi']
			pin_subtext.append('Wiring Pi pin {}'.format(wiringpi))
			alternates.append(render_alternate('wiringpi','Wiring Pi pin {}'.format(wiringpi)))

		if 'bcmAlt' in pin['scheme']:
			bcmAlt = pin['scheme']['bcmAlt']
			pin_subtext.append('BCM pin {} on Rev 1 ( very early ) Pi'.format(bcmAlt))

	#print(pin_type)

	pin_url = slugify('pin{}_{}'.format(pin_num,pin_url))

	pin_text = render_pin_text(pin_num,pin_url,pin_text_name,'<ul><li>{}</li></ul>'.format('</li><li>'.join(pin_subtext)))
	if pin_text != None:
		pages.append(pin_text)

	return '<li class="pin{} {}"><a href="/pindb/{}"><span class="default"><span class="phys">{}</span> {}</span><span class="pin"></span>\n{}</a></li>\n'.format(
		pin_num,
		' '.join(map(slugify,pin_type)),
		pin_url,
		pin_num,
		pin_name,
		'\n'.join(alternates)
		)

for odd in range(1,len(pins),2):
	html_odd += render_pin(odd)
	html_even += render_pin(odd+1)


html = '''<ul class="bottom">
{}</ul>
<ul class="top">
{}</ul>'''.format(html_odd, html_even)

html = template.replace('{{nav}}',html).replace('{{content}}','\n'.join(pages))

print(html)
