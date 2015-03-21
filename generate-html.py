#!/usr/bin/env python
import json
import markdown
import unicodedata
import re
import os
import time

base_url = '/pinout/'
resource_url = '/resources/'


overlays = [
	'spi',
	'uart',
	'i2c',
	'arduino-spi',
	'pibrella',
	'explorer-hat-pro',
	'explorer-hat',
	'display-o-tron'
	]

template = open('template/layout.html').read()

pages = {}
navs = {}
select_overlays = []

overlays_html = ''

try:
	os.mkdir('output/pinout')
except OSError:
	pass

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

	details = []

	if 'manufacturer' in loaded:
		details.append('* Made by ' + loaded['manufacturer'])

	if 'pincount' in loaded:
		pincount = int(loaded['pincount'])
		if pincount == 40:
			details.append('* HAT form-factor')
		elif pincount == 26:
			details.append('* Classic 26-pin')
		else:
			details.append('* {} pin header'.format(pincount))

	if 'pin' in loaded:
		uses = len(loaded['pin'])
		details.append('* Uses {} GPIO pins'.format(uses))

	if 'url' in loaded:
		details.append('* Resources: [{}]({})'.format(loaded['url'],loaded['url']))

	loaded['long_description'] = '{}\n{}'.format(loaded['long_description'],markdown.markdown('\n'.join(details)))

	loaded['page_url'] = slugify(loaded['name'])
	pages[loaded['page_url']] = render_overlay_page(loaded)
	navs[loaded['page_url']] = render_nav(loaded['page_url'], overlay=loaded)
	select_overlays.append((loaded['page_url'], loaded['name']))
 	return loaded

def load_md(filename):
	try:
		html = markdown.markdown(open(filename).read(), extensions=['fenced_code'])

		return html
		#return markdown.markdown(open(filename).read(), extensions=[gfm.HiddenHiliteExtension([]),'fenced_code'])
	except IOError:
		return ''

def render_pin_text(pin_num, pin_url, pin_name, pin_subtext):
	return '<article class="{}"><h1>{}</h1>{}{}</article>'.format(pin_url,pin_name,pin_subtext,load_md('description/pins/pin-{}.md'.format(pin_num)))

def render_overlay_page(overlay):
	if overlay == None:
		return ''
	return '<article class="page_{}">{}</article>'.format(slugify(overlay['name']),overlay['long_description'])

#pages += map(render_overlay_page,overlays)

def render_alternate(handle, name):
	handle = slugify(handle.lower())
	return '<span class="alternate legend_{}">{}</span>'.format(handle,name)

def render_pin_page(pin_num):
	pin = pins[str(pin_num)]
	pin_url = pin['name']
	pin_text_name = pin['name']

	pin_subtext = []


	pin_subtext.append('Physical pin {}'.format(pin_num))

	if 'scheme' in pin:
		if 'bcm' in pin['scheme']:
			bcm = pin['scheme']['bcm']
			pin_url = 'gpio{}'.format(bcm)
			pin_subname_text = ''
			pin_text_name = 'BCM {} {}'.format(bcm, pin_subname_text)
			if pin['name'] != '':
			    pin_subname_text = '({})'.format(pin['name'])
			pin_subtext.append('BCM pin {}'.format(bcm))
		if 'wiringpi' in pin['scheme']:
			wiringpi = pin['scheme']['wiringpi']
			pin_subtext.append('Wiring Pi pin {}'.format(wiringpi))
		if 'bcmAlt' in pin['scheme']:
			bcmAlt = pin['scheme']['bcmAlt']
			pin_subtext.append('BCM pin {} on Rev 1 ( very early ) Pi'.format(bcmAlt))


	pin_url = slugify('pin{}_{}'.format(pin_num,pin_url))

	pin_text = render_pin_text(pin_num,pin_url,pin_text_name,'<ul><li>{}</li></ul>'.format('</li><li>'.join(pin_subtext)))
	#if pin_text != None:
	return (pin_url, pin_text) #pages[pin_url] = pin_text


def render_pin(pin_num, selected_url, overlay=None):
	pin = pins[str(pin_num)]


	pin_type = list([x.strip() for x in pin['type'].lower().split('/')])
	pin_url = pin['name']
	pin_name = pin['name']
	pin_text_name = pin['name']
	pin_used = False
	pin_link_title = []


	if overlay != None and str(pin_num) in overlay['pin']:
		overlay_pin = overlay['pin'][str(pin_num)]
		pin_text_name = ''
		#print(overlay)
		pin_name = overlay_pin['name']
		pin_used = True

		if 'description' in overlay_pin:
			pin_link_title.append(overlay_pin['description'])
		#alternates = []

		#for overlay in overlays:
		#	if overlay != None:
		#		if str(pin_num) in overlay['pin']:
		#		    alternates.append(render_alternate(overlay['name'],overlay['pin'][str(pin_num)]['name']))

	if 'scheme' in pin:
		if 'bcm' in pin['scheme']:
			bcm = pin['scheme']['bcm']
			pin_subname = ''
			#pin_subname_text = ''
			#if pin_url == '':
			pin_url = 'gpio{}'.format(bcm)
			if pin_name != '': #pin['name'] != '':
			    pin_subname = '<small>({})</small>'.format(pin_name) #pin['name'])
		#	    pin_subname_text = '({})'.format(pin['name'])
			pin_name = 'BCM {} {}'.format(bcm, pin_subname)
		#	pin_text_name = 'BCM {} {}'.format(bcm, pin_subname_text)
		if 'wiringpi' in pin['scheme']:
			wiringpi = pin['scheme']['wiringpi']
			pin_link_title.append('Wiring Pi pin {}'.format(wiringpi))
		#	alternates.append(render_alternate('wiringpi','Wiring Pi pin {}'.format(wiringpi)))

		#print(pin_type)

	pin_url = base_url + slugify('pin{}_{}'.format(pin_num,pin_url))

	#print(selected_url)
	selected = ''

	if base_url + selected_url == pin_url:
		selected = ' active'
	if pin_used:
		selected += ' overlay-pin'

	return '<li class="pin{pin_num} {pin_type}{pin_selected}"><a href="{pin_url}" title="{pin_title}"><span class="default"><span class="phys">{pin_num}</span> {pin_name}</span><span class="pin"></span></a></li>\n'.format(
		pin_num = pin_num,
		pin_type = ' '.join(map(slugify,pin_type)),
		pin_selected = selected,
		pin_url = pin_url,
		pin_title = ', '.join(pin_link_title),
		pin_name = pin_name
		)

def render_nav(url, overlay=None):
	html_odd = ''
	html_even = ''
	for odd in range(1,len(pins),2):
		html_odd  += render_pin(odd,  url,overlay)
		html_even += render_pin(odd+1,url,overlay)

	return '''<ul class="bottom">
{}</ul>
<ul class="top">
{}</ul>'''.format(html_odd, html_even)




db = json.load(open('pi-pinout.json'))

pins = db['pins']

overlays = map(load_overlay,overlays)

for url, name in select_overlays:
	overlays_html += '<option value="{}">{}</option>'.format(url, name)


pages['pinout'] = render_overlay_page({'name':'Index','long_description':load_md('description/index.md')})
navs['pinout'] = render_nav('pinout')

print('Rendering pin pages...')

for pin in range(1,len(pins)+1):
	(pin_url, pin_html) = render_pin_page(pin)
	pin_nav = render_nav(pin_url)
	pin_html = template.replace('{{nav}}',pin_nav).replace('{{content}}',pin_html).replace('{{resource_url}}',resource_url).replace('{{overlays}}',overlays_html).replace('{{v}}',str(int(time.time())))

	print('Outputting page {}'.format(pin_url))

	with open(os.path.join('output/pinout','{}.html'.format(pin_url)),'w') as f:
		f.write(pin_html)

#nav = render_nav()

print('Rendering overlay and index pages...')

for url in pages:
	content = pages[url]
	nav = navs[url]
	print('Outputting page {}'.format(url))
	html = template.replace('{{nav}}',nav).replace('{{content}}',content).replace('{{resource_url}}',resource_url).replace('{{overlays}}',overlays_html).replace('{{v}}',str(int(time.time())))
	
	if url != 'pinout':
		url = os.path.join('pinout',url)

	with open(os.path.join('output','{}.html'.format(url)),'w') as f:
		f.write(html)

