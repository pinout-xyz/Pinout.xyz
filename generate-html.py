#!/usr/bin/env python
import json
import markdown
import unicodedata
import re
import os

resource_url = '/pinout2/resources/'
#resource_url = '/resources/'

overlays = ['pibrella','explorer-hat-pro']

template = open('template/layout.html').read()

pages = {}
navs = {}

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


	if overlay != None and str(pin_num) in overlay['pin']:
		pin_text_name = ''
		print(overlay)
		pin_name = overlay['pin'][str(pin_num)]['name']
		pin_used = True
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
		#if 'wiringpi' in pin['scheme']:
		#	wiringpi = pin['scheme']['wiringpi']
		#	alternates.append(render_alternate('wiringpi','Wiring Pi pin {}'.format(wiringpi)))

		#print(pin_type)

	pin_url = slugify('pin{}_{}'.format(pin_num,pin_url))

	#print(selected_url)
	selected = ''
	if selected_url == pin_url:
		selected = ' active'
	if pin_used:
		selected += ' overlay-pin'

	return '<li class="pin{} {}{}"><a href="{}.html"><span class="default"><span class="phys">{}</span> {}</span><span class="pin"></span></a></li>\n'.format(
		pin_num,
		' '.join(map(slugify,pin_type)),
		selected,
		pin_url,
		pin_num,
		pin_name
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


pages['index'] = render_overlay_page({'name':'Index','long_description':load_md('description/index.md')})
navs['index'] = render_nav('index')

print('Rendering pin pages...')

for pin in range(1,len(pins)+1):
	(pin_url, pin_html) = render_pin_page(pin)
	pin_nav = render_nav(pin_url)
	pin_html = template.replace('{{nav}}',pin_nav).replace('{{content}}',pin_html).replace('{{resource_url}}',resource_url)

	print('Outputting page {}'.format(pin_url))

	with open(os.path.join('output','{}.html'.format(pin_url)),'w') as f:
		f.write(pin_html)

#nav = render_nav()

print('Rendering overlay and index pages...')

for url in pages:
	content = pages[url]
	nav = navs[url]
	print('Outputting page {}'.format(url))
	html = template.replace('{{nav}}',nav).replace('{{content}}',content).replace('{{resource_url}}',resource_url)
	with open(os.path.join('output','{}.html'.format(url)),'w') as f:
		f.write(html)

