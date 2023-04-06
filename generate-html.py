#!/usr/bin/env python3

import os
import re
import sys
import unicodedata
import glob

try:
    import markdown
except ImportError:
    exit("This script requires the Markdown module\nInstall with: sudo pip install Markdown")

import markjaml
import pinout
import urlmapper

try:
    reload(sys)
except NameError:
    from importlib import reload
    reload(sys)

try:
    sys.setdefaultencoding('utf8')
except AttributeError:  # Does not work in Python 3
    unicode = str


DEBUG_LEVEL = 1

# TODO: Why is this here and not loaded from pinout.yaml
GROUND_PINS = [6, 9, 14, 20, 25, 30, 34, 39]

lang = "en"
default_strings = {
    'home': 'Home',
    'boards': 'Boards',
    'details': 'Details',
    'pin_header': '{} pin header',
    'form_undefined': 'Undefined',
    'group_other': 'other',
    'type_hat': 'HAT form-factor',
    'type_phat': 'pHAT form-factor',
    'type_classic': 'Classic form-factor',
    'eeprom_detect': 'Uses VID/PID',
    'eeprom_setup': 'Uses EEPROM',
    'uses_5v_and_3v3': 'Needs 5v and 3v3 power',
    'uses_5v': 'Needs 5v power',
    'uses_3v3': 'Needs 3v3 power',
    'uses_i2c': 'Uses I2C',
    'uses_spi': 'Uses SPI',
    'uses_n_gpio_pins': 'Uses {} GPIO pins',
    'bcm_pin_rev1_pi': 'GPIO/BCM pin {} on Rev 1 ( very early ) Pi',
    'physical_pin_n': 'Physical/Board pin {}',
    'wiring_pi_pin': 'Wiring Pi pin {}',
    'made_by': 'Made by {manufacturer}',
    'more_information': 'More Information',
    'github_repository': 'GitHub Repository',
    'board_schematic': 'Schematic',
    'buy_now': 'Buy Now',
    'translate_msg': '<a href="https://github.com/pinout-xyz/Pinout.xyz">This page needs translating, can you help?</a><br><br>',
    'browse_addons': 'Browse more HATs, pHATs and add-ons',
    'return_home': 'Return to the Raspberry Pi GPIO Pinout',
    'boards_title': 'Raspberry Pi HATs, pHATs &amp; Add-ons',
    'boards_subtitle': 'Click on a HAT, pHAT or add-on for more details and to see which pins it uses!'
}
exclude_pincounts = ['3v3-power', '5v-power', 'ground', 'iface-jtag', 'i2c', 'iface-gpclk', 'wiringpi', 'spi', 'iface-1wire']


def debug(level, string):
    if level < DEBUG_LEVEL:
        return

    level_text = ['Notice', 'Warning', 'Error'][level]
    print("[{}] {}".format(level_text, string))


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
    data = markjaml.load(overlay)

    loaded = data['data']
    loaded['source'] = overlay
    loaded['long_description'] = data['html']

    filename = overlay.split('/')[-1].replace('.md', '')

    """
    try:
        data = markjaml.load('src/{}/overlay/{}.md'.format(lang, overlay))

        loaded = data['data']
        loaded['source'] = "src/{}/overlay/{}.md".format(lang, overlay)
        loaded['long_description'] = data['html']
    except IOError:
        try:
            data = markjaml.load('src/{}/translate/{}.md'.format(lang, overlay))


            loaded = data['data']
            loaded['source'] = "src/{}/translate/{}.md".format(lang, overlay)
            loaded['long_description'] = strings['translate_msg'] + data['html']
            loaded['type'] = strings['group_other']
            if 'formfactor' in loaded:
                if str(loaded['formfactor']) == 'Custom':
                    loaded['formfactor'] = strings['form_undefined']
        except IOError:
            print('overlay {} missing in lang {}'.format(overlay, lang))
            return None
    """

    debug(0, '>> Rendering: {src}'.format(src=loaded['source']))

    '''
    If this is not an info page, then build a collection of details and append them to long_description
    '''
    if 'type' not in loaded or loaded['type'] != 'info':
        details = []

        if 'type' not in loaded:
            loaded['type'] = strings['group_other']

        if 'manufacturer' in loaded:
            if 'collected' in loaded:
                details.append(strings['made_by'].format(manufacturer=loaded['manufacturer']))
            else:
                manu_link = '<a href="/boards#manufacturer={manufacturer}">{manufacturer}</a>'.format(manufacturer=loaded['manufacturer'])
                details.append(strings['made_by'].format(manufacturer=manu_link))

        if 'pincount' in loaded:
            '''
            Choose correct board type to be displayed based upon pincount and form factor.
            This could be a HAT, a pHAT or other...
            '''
            pincount = int(loaded['pincount'])
            if 'formfactor' in loaded:
                formfactor = str(loaded['formfactor'])
                if pincount == 40 and formfactor == 'HAT':
                    details.append(strings['type_hat'])
                elif pincount == 40 and formfactor == 'pHAT':
                    details.append(strings['type_phat'])
                elif pincount == 40 and formfactor == '40-way':
                    details.append(strings['pin_header'].format(pincount))
                else:
                    if filename not in exclude_pincounts:
                        details.append(strings['pin_header'].format(pincount))
            elif pincount == 40:
                details.append(strings['type_hat'])
            elif pincount == 26:
                details.append(strings['type_classic'])
            else:
                if filename not in exclude_pincounts:
                # if '3v3-power.md' not in overlay and '5v-power.md' not in overlay and 'ground.md' not in overlay:
                    details.append(strings['pin_header'].format(pincount))

        if 'eeprom' in loaded:
            eeprom = str(loaded['eeprom'])
            if eeprom == 'detect' or eeprom == 'True':
                details.append(strings['eeprom_detect'])
            if eeprom == 'setup':
                details.append(strings['eeprom_setup'])

        if 'power' not in loaded['type'] and 'power' in loaded:
            uses_5v = False
            uses_3v3 = False

            if loaded['power'] is None:
                loaded['power'] = {}

            for pin in loaded['power']:
                pin = str(pin)
                if pin.startswith('bcm'):
                    pin = pinout.bcm_to_physical(pin[3:])

                if pin in ['2', '4']:
                    uses_5v = True

                if pin in ['1', '17']:
                    uses_3v3 = True

            if uses_5v and uses_3v3:
                details.append(strings['uses_5v_and_3v3'])
            elif uses_5v:
                details.append(strings['uses_5v'])
            elif uses_3v3:
                details.append(strings['uses_3v3'])

        '''
        If the overlay includes a collection of pins then
        loop through them and count how many non-power pins are used
        '''
        if 'pin' in loaded:
            uses_i2c = False
            uses_spi = False

            uses = 0
            for pin in loaded['pin']:
                data = loaded['pin'][pin]
                pin = str(pin)
                if pin.startswith('bcm'):
                    pin = pinout.bcm_to_physical(pin[3:])

                if pin in pinout.pins:
                    actual_pin = pinout.pins[pin]

                    if actual_pin['type'] in ['+3v3', '+5v', 'GND'] and '3v3-power.md' not in overlay and '5v-power.md' not in overlay and 'ground.md' not in overlay:
                        raise Exception(
                            "{} includes a reference to a {} pin ({}), which isn't allowed".format(overlay, actual_pin['type'], pin))
                    else:
                        uses += 1

                if data is not None and 'mode' in data:
                    if pin in ['3', '5'] and data['mode'] == 'i2c':
                        uses_i2c = True
                    if pin in ['19', '21', '23'] and data['mode'] == 'spi':
                        uses_spi = True

            if filename not in exclude_pincounts:
                if uses > 0:
                    details.append(strings['uses_n_gpio_pins'].format(uses))

            if uses_spi:
                details.append(strings['uses_spi'])

            if uses_i2c:
                details.append(strings['uses_i2c'])

        if 'i2c' in loaded:
            for addr in loaded['i2c']:
                data = loaded['i2c'][addr]
                if type(addr) is int:
                    addr = "0x{:02x}".format(addr)
                dev = data['device']
                alt = None
                try:
                    alt = data['alternate']
                    if type(alt) is list:
                        alt = ", ".join(alt)
                except KeyError:
                    pass
                if data is not None and 'device' in data:
                    if alt is not None:
                        details.append('{address}: {device} (Alt: {alt})'.format(address=addr, device=dev, alt=alt))
                    else:
                        details.append('{address}: {device}'.format(address=addr, device=dev))

        # A URL to more information about the add-on board, could be a GitHub readme or an about page
        if 'url' in loaded:
            details.append('[{text}]({url})'.format(text=strings['more_information'], url=loaded['url']))

        # Should only ever be a URL to the github repository with code supporting the product
        if 'github' in loaded:
            details.append('[{text}]({url})'.format(text=strings['github_repository'], url=loaded['github']))

        # A URL referencing the add-on board schematic
        if 'schematic' in loaded:
            if loaded['schematic'] is not None:
                details.append('[{text}]({url})'.format(text=strings['board_schematic'], url=loaded['schematic']))
            else:
                debug(1, "schematic defined in {}, but missing a value.".format(loaded['source']))

        # A URL to a preferred place to buy the add-on board
        if 'buy' in loaded:
            details.append('[{text}]({url})'.format(text=strings['buy_now'], url=loaded['buy']))

        details_html = markdown.markdown('\n'.join(map(lambda d: '* ' + d, details)))

        details_image = ''

        if 'image' in loaded:
            details_image = "<img loading=\"lazy\" src=\"/resources/boards/{}\" alt=\"{}\" />".format(loaded['image'], loaded['name'])

        details_html = "<table class=\"details\"><tr><td><h2>{}</h2>{}</td><td>{}</td></tr></table>".format(strings['details'], details_html, details_image)

        if len(details) or len(details_image):
            loaded['long_description'] = '{}\n{}'.format(loaded['long_description'], details_html)
        else:
            loaded['long_description'] = '{}'.format(loaded['long_description'])

    # Automatically generate a page slug from the name if none is specified
    if 'page_url' not in loaded:
        loaded['page_url'] = slugify(loaded['name'])

    loaded['rendered_html'] = render_overlay_page(loaded)
    loaded['src'] = overlay
    pages[loaded['page_url']] = loaded
    navs[loaded['page_url']] = render_nav(loaded['page_url'], overlay=loaded)

    return loaded


def load_md(filename):
    filename = 'src/{}/{}'.format(lang, filename)
    try:
        html = markdown.markdown(open(filename).read(), extensions=['fenced_code'])
        # print(':) Loaded markdown from {}'.format(filename))
        return html
    except IOError:
        # print('!! Unable to load markdown from {}'.format(filename))
        return ''


def render_overlay_page(overlay):
    if overlay is None:
        return ''
    return '<article class="page_{}">{}</article>'.format(slugify(overlay['name']), overlay['long_description'])


def render_pin_page(pin_num):
    pin = pinout.pins[str(pin_num)]
    pin_url = pin['name']

    # Exclude pages for ground pins
    if pin_num in GROUND_PINS:
        return None, None, None

    pin_text_name = pin['name']

    pin_subtext = []

    pin_subtext.append(strings['physical_pin_n'].format(pin_num))

    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            bcm = pin['scheme']['bcm']
            pin_url = 'gpio{}'.format(bcm)

            pin_text_name = 'GPIO {}'.format(bcm)

            pin_subtext.append('GPIO/BCM pin {}'.format(bcm))
        if 'wiringpi' in pin['scheme']:
            wiringpi = pin['scheme']['wiringpi']
            pin_subtext.append('Wiring Pi pin {}'.format(wiringpi))
        if 'bcmAlt' in pin['scheme']:
            bcmAlt = pin['scheme']['bcmAlt']
            pin_subtext.append(strings['bcm_pin_rev1_pi'].format(bcmAlt))

    if 'description' in pin:
        pin_text_name = '{} ({})'.format(pin_text_name, pin['description'])

    fn_headings = []
    fn_functions = []
    pin_functions = ''
    if 'functions' in pin:
        for x in range(6):
            fn_headings.append('Alt' + str(x))

            function = ''
            if 'alt' + str(x) in pin['functions']:
                function = pin['functions']['alt' + str(x)]

            fn_functions.append(function)

        pin_functions = '''<table class="pin-functions">
        <thead>
            <tr>
                <th>{headings}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{functions}</td>
            </tr>
        </tbody>
        </table>'''.format(headings='</th><th>'.join(fn_headings), functions='</td><td>'.join(fn_functions))

    pin_url = slugify('pin{}_{}'.format(pin_num, pin_url))

    pin_text = '<article class="{pin_url}"><h1>{pin_name}</h1>{pin_functions}{pin_subtext}{pin_text}</article>'.format(
        pin_url=pin_url,
        pin_name=pin_text_name,
        pin_functions=pin_functions,
        pin_subtext='<ul><li>{}</li></ul>'.format('</li><li>'.join(pin_subtext)),
        pin_text=load_md('pin/pin-{}.md'.format(pin_num)))

    # if pin_text != None:
    return pin_url, pin_text, pin_text_name  # pages[pin_url] = pin_text


def render_pin(pin_num, selected_url, overlay=None):
    pin = pinout.pins[str(pin_num)]

    pin_type = list([x.strip() for x in pin['type'].lower().split('/')])
    pin_name = pin['name']
    pin_url = pin_name
    pin_ground = False
    pin_power = False
    pin_regular = False
    pin_link_title = []
    bcm_pin = None
    overlay_pin = {}

    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            bcm_pin = 'bcm' + str(pin['scheme']['bcm'])

    valid_pins = (pin_num, str(pin_num), bcm_pin)

    if overlay is not None:
        for try_pin in valid_pins:
            if try_pin in overlay.get('ground', {}):
                overlay_pin = overlay['ground'][try_pin]
                pin_ground = True
                break
            if try_pin in overlay.get('power', {}):
                overlay_pin = overlay['power'][try_pin]
                pin_power = True
                break
            if try_pin in overlay.get('pin', {}):
                overlay_pin = overlay['pin'][try_pin]
                pin_regular = True
                break

        if isinstance(overlay_pin, str):
            # source = ''
            # if 'source' in overlay:
            #     source = overlay['source']
            # TODO: What is this?
            debug(1, "{}: Overlay pin '{}' for pin {} is a string! Should be dict".format(overlay['source'], overlay_pin, pin_num))

        if overlay_pin is None:
            overlay_pin = {}

        if pin_regular:
            pin_name = overlay_pin.get('name', pin_name)

            if 'description' in overlay_pin:
                pin_link_title.append(overlay_pin['description'])

            if overlay_pin.get('mode') == "EEPROM_WP":
                pin_name = "EEPROM WP"

    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            bcm = pin['scheme']['bcm']
            pin_subname = ''

            pin_url = 'gpio{}'.format(bcm)
            if pin_name != '':
                pin_subname = ' <small>({})</small>'.format(pin_name)
            pin_name = '<span class="name">GPIO {}</span>{}'.format(bcm, pin_subname)

        if 'wiringpi' in pin['scheme']:
            wiringpi = pin['scheme']['wiringpi']
            pin_link_title.append(strings['wiring_pi_pin'].format(wiringpi))

    pin_url = base_url + slugify('pin{}_{}'.format(pin_num, pin_url))

    if pin['type'] in pinout.get_setting('urls'):
        pin_url = base_url + pinout.get_setting('urls')[pin['type']]

    selected = ''

    if base_url + selected_url == pin_url:
        selected = ' active'
    if pin_ground:
        selected += ' overlay-ground'
    if pin_power:
        selected += ' overlay-power'
    if pin_regular:
        selected += ' overlay-pin'

    pin_url = pin_url + url_suffix

    return '<li class="pin{pin_num} {pin_type}{pin_selected}"><a href="{pin_url}" title="{pin_title}"><span class="default"><span class="phys">{pin_num}</span> {pin_name}</span><span class="pin"></span></a></li>\n'.format(
        pin_num=pin_num,
        pin_type=' '.join(map(cssify, pin_type)),
        pin_selected=selected,
        pin_url=pin_url,
        pin_title=', '.join(pin_link_title),
        pin_name=pin_name,
        langcode=lang
    )


def render_nav(url, overlay=None):
    html_odd = ''
    html_even = ''
    for odd in range(1, len(pinout.pins), 2):
        html_odd += render_pin(odd, url, overlay)
        html_even += render_pin(odd + 1, url, overlay)

    return '''<ul class="bottom">
{}</ul>
<ul class="top">
{}</ul>'''.format(html_odd, html_even)


def get_hreflang_urls(src):
    hreflang = []
    for lang in sorted(alternate_urls):
        if src in alternate_urls[lang]:
            url = alternate_urls[lang][src]
            hreflang.append('<link rel="alternate" href="{url}" hreflang="{lang}"/>'.format(
                lang=lang,
                url=url
            ))
    return hreflang


def get_lang_urls(src):
    urls = []
    for url_lang in sorted(alternate_urls):
        if src in alternate_urls[url_lang]:
            img_css = ''
            if url_lang == lang:
                img_css = ' class="grayscale"'
            url = alternate_urls[url_lang][src]
            urls.append(
                '<a href="{url}" rel="alternate" hreflang="{lang}"><img{css} src="{resource_url}{lang}.png" width="16" height="11" /></a>'.format(
                    lang=url_lang,
                    url=url,
                    resource_url=resource_url,
                    css=img_css
                ))
    return urls


'''
Main Program Flow
'''

if len(sys.argv) > 1:
    lang = sys.argv[1]

alternate_urls = urlmapper.generate_urls(lang)

pinout.load(lang)

overlays = glob.glob("src/{}/overlay/*.md".format(lang)) + glob.glob("src/{}/translate/*.md".format(lang))

strings = pinout.get_string('strings', {})

if type(strings) == list:
    _strings = {}
    for item in strings:
        _strings[list(item.keys())[0]] = list(item.values())[0]
    strings = _strings

for key, val in default_strings.items():
    if key not in strings:
        strings[key] = val

base_url = pinout.get_setting('base_url', '/pinout/')             # eg: '/pinout-tr/pinout/'
resource_url = pinout.get_setting('resource_url', '/resources/')  # eg: '/pinout-tr/resources/'
url_suffix = pinout.get_setting('url_suffix', '')                 # eg: '.html'

template_main = open('common/page.html'.format(lang)).read()
template_boards = open('common/boards.html'.format(lang)).read()
template_footer = open('src/{}/template/footer.html'.format(lang)).read()
template_footer = open('src/{}/template/footer.html'.format(lang)).read()

pages = {}
navs = {}

overlays_html = []

nav_html = {}

if not os.path.isdir('output'):
    try:
        os.mkdir('output')
    except OSError:
        exit('Failed to create output dir')
if not os.path.isdir('output/{}'.format(lang)):
    try:
        os.mkdir('output/{}'.format(lang))
    except OSError:
        exit('Failed to create output/{} dir'.format(lang))
if not os.path.isdir('output/{}/pinout'.format(lang)):
    try:
        os.mkdir('output/{}/pinout'.format(lang))
    except OSError:
        exit('Failed to create output/{}/pinout dir'.format(lang))

print("\nRendering overlay pages...")
overlays = list(map(load_overlay, overlays))
overlay_subnav = ['featured']
featured_boards_count = 0
featured_boards_html = ''

boards_page = []
boards_manufacturers = []

'''
Build up the navigation between overlays. This needs to be done before rendering pages
as it's used in every single page.

overlays_html is generated with all types for legacy reasons
'''
for overlay in overlays:

    link = (overlay['page_url'], overlay['name'])

    overlays_html += [link]

    if overlay['src'] in pinout.settings['featured'] and 'image' in overlay and featured_boards_count < 4:
        featured_boards_count += 1
        featured_boards_html += '<div class="board"><a href="{base_url}{page_url}"><img loading=\"lazy\"" alt="{name}" src="{resource_url}boards/{image}" /><strong>{name}</strong><span>{description}</span></a></div>'.format(
            image=overlay['image'],
            name=overlay['name'],
            page_url=overlay['page_url'],
            base_url=base_url,
            resource_url=resource_url,
            description=overlay['description']
        )

    if 'class' in overlay and 'type' in overlay:
        o_class = overlay['class']

        o_type = overlay['type']

        def sanitize_type(t):
            allowed_types = {
                'adc': 'ADC', 'audio': 'Audio', 'com': 'COM', 'dac': 'DAC', 'display': 'Display', 'gesture': 'Gesture', 'gps': 'GPS', 'instrument': 'Instrument',
                'io': 'IO', 'iot': 'IOT', 'led': 'LED', 'mcu': 'MCU', 'motor': 'Motor', 'multi': 'Multi', 'network': 'Network', 'other': 'Other', 'power': 'Power', 'radio': 'Radio',
                'relay': 'Relay', 'rtc': 'RTC', 'sensor': 'Sensor', 'touch': 'Touch', 'usb': 'USB', 'pinout': 'pinout',

                'lora': 'LoRa',
                'otro': 'Otro',
                'gestos': 'Gestos',
                'cap': 'Cap',
                'lcd': 'LCD'}

            # TODO: maybe find a better way to handle type translations
            if lang == 'es':
                allowed_types['gesture'] = 'Gestos'
                allowed_types['other'] = 'Otro'

            remapped_types = {'iot': 'radio'}
            t = t.strip()
            t_handle = t.lower()
            if t_handle in allowed_types:
                return allowed_types[t_handle]

            for remap_src, remap_target in remapped_types.iteritems():
                if t_handle == remap_src:
                    return allowed_types[remap_target]

            print("Rejecting unsupported type: {} in overlay: {}".format(t, overlay['name']))
            return None

        o_types = [sanitize_type(t) for t in o_type.split(',') if sanitize_type(t) is not None]

        if len(o_types) > 1 and 'Multi' not in o_types:
            o_types.append('Multi')

        if len(o_types) == 0:
            print(" No type(s) found in overlay: {}".format(overlay['name']))
            o_types = [strings['group_other']]

        o_type = ','.join(o_types)

        if o_class not in nav_html:
            nav_html[o_class] = ''

        nav_html[o_class] += '<li><a href="{}{}">{}</a></li>'.format(base_url, overlay['page_url'], overlay['name'])

        if o_class == 'board':
            image = overlay['image'] if 'image' in overlay else 'no-image.png'

            if 'formfactor' not in overlay:
                print('Warning! -> {name} missing formfactor'.format(name=overlay['name']))

            o_formfactor = strings['form_undefined']

            allowed_formfactors = {'custom': 'Custom', 'hat': 'HAT', 'phat': 'PHAT', 'usb': 'USB'}

            if 'formfactor' in overlay:
                o_formfactor = overlay['formfactor']

                if o_formfactor.lower() in allowed_formfactors:
                    o_formfactor = allowed_formfactors[o_formfactor.lower()]
                else:
                    o_formfactor = strings['form_undefined']

            boards_page.append({
                'name': overlay['name'],
                'html': '<li class="board" data-type="{type}" data-manufacturer="{manufacturer}" data-form-factor="{formfactor}"><a href="{base_url}{page_url}"><img loading=\"lazy\" src="{resource_url}boards/{image}" /><strong>{name}</strong></a></li>'.format(
                    image=image,
                    name=overlay['name'],
                    page_url=overlay['page_url'],
                    base_url=base_url,
                    type=o_type,
                    formfactor=o_formfactor,
                    manufacturer=overlay.get('collected', overlay['manufacturer']),
                    resource_url=resource_url)
            })


def interfaces_menu(current):
    interfaces = [overlay for overlay in overlays if overlay['class'] == 'interface']

    html = ''

    for interface in interfaces:
        sel = ''
        if current is not None and 'name' in current and interface['name'] == current['name']:
            sel = ' class="selected"'

        html += '<li{}><a href="{}{}">{}</a></li>'.format(sel, base_url, interface['page_url'], interface['name'])

    return html


boards_page = [x['html'] for x in sorted(boards_page, key=lambda k: k['name'].lower())]
pages['boards'] = {'rendered_html': ''.join(boards_page)}

'''
Manually add the index page as 'pinout', this is due to how the
website is currently structured with /pinout as the index
and all other pages in /pinout/

serve.py will mirror this structure for testing.
'''

pages['index'] = {}
pages['index']['rendered_html'] = render_overlay_page({'name': 'Index', 'long_description': load_md('/template/index.md')})

default_nav = render_nav('pinout')

navs['index'] = default_nav

'''
Add the 404 page if 404.md is present.
'''
page404 = load_md('/template/404.md')
if page404 is not None:
    pages['404'] = {}
    pages['404']['rendered_html'] = render_overlay_page({'name': '404', 'long_description': page404})
    navs['404'] = default_nav


crumbtrail = '<div id="crumbtrail"><p><a class="more" href="/boards">' + strings['browse_addons'] + ' &raquo;</a></p></div>'

navs['boards'] = default_nav

print('\nRendering pin pages...')

interfaces = interfaces_menu(None)

for pin in range(1, len(pinout.pins) + 1):
    (pin_url, pin_html, pin_title) = render_pin_page(pin)
    if pin_url is None:
        continue

    hreflang = get_hreflang_urls('pin{}'.format(pin))
    langlinks = get_lang_urls('pin{}'.format(pin))

    pin_nav = render_nav(pin_url)
    pin_html = pinout.render_html(template_main,
                                  template_footer,
                                  strings,
                                  pinout.settings,
                                  lang_links="\n\t\t".join(langlinks),
                                  hreflang="\n\t\t".join(hreflang),
                                  nav=pin_nav,
                                  content=pin_html,
                                  resource_url=resource_url,
                                  overlays=overlays_html,
                                  description=strings['default_desc'],
                                  title=pin_title + strings['title_suffix'],
                                  featured_boards=featured_boards_html,
                                  langcode=lang,
                                  nav_html=nav_html,
                                  interfaces=interfaces,
                                  body_class='pin',
                                  crumbtrail=crumbtrail
                                  )

    debug(0, '>> Saving: pinout/{}.html'.format(pin_url))

    with open(os.path.join('output', lang, 'pinout', '{}.html'.format(pin_url)), 'w') as f:
        f.write(pin_html)


print('\nSaving overlay and index pages...')

for url in pages:
    content = pages[url]['rendered_html']
    nav = navs[url]
    hreflang = []
    langlinks = []

    # Select the appropriate template for this page
    template = template_boards if url == 'boards' else template_main

    if url == 'index' or url == 'boards':
        src = url
        hreflang = get_hreflang_urls(src)
        langlinks = get_lang_urls(src)

    if 'src' in pages[url]:
        src = pages[url]['src']
        hreflang = get_hreflang_urls(src)
        langlinks = get_lang_urls(src)

    if 'description' not in pages[url]:
        pages[url]['description'] = strings['default_desc']

    name = strings['default_title']

    if 'name' in pages[url]:
        name = pages[url]['name'] + strings['title_suffix']

    feat_boards_html = featured_boards_html

    body_class = ''

    crumbtrail = '<div id="crumbtrail"><p><a class="more" href="/boards">' + strings['browse_addons'] + ' &raquo;</a></p></div>'

    if 'class' in pages[url] and pages[url]['class'] == 'board':
        feat_boards_html = ''
        body_class = 'board'
        if 'collected' not in pages[url]:
            crumbtrail = '<div id="crumbtrail"><p><a href="/">{home}</a> &raquo; <a href="/boards">{boards}</a> &raquo; <a href="/boards#manufacturer={manufacturer}">{manufacturer}</a></p></div>'.format(
                title=pages[url]['name'],
                manufacturer=pages[url]['manufacturer'],
                home=strings['home'],
                boards=strings['boards']
            )
        else:
            crumbtrail = '<div id="crumbtrail"><p><a href="/">{home}</a> &raquo; <a href="/boards">{boards}</a> &raquo; <a href="/boards#manufacturer={manufacturer}">{manufacturer}</a></p></div>'.format(
                title=pages[url]['name'],
                manufacturer=pages[url]['collected'],
                home=strings['home'],
                boards=strings['boards']
            )

    if url == 'boards':
        body_class = 'boards-page'

    html = pinout.render_html(template,
                              template_footer,
                              strings,
                              pinout.settings,
                              twittercard=True,
                              lang_links="\n\t\t".join(langlinks),
                              hreflang="\n\t\t".join(hreflang),
                              nav=nav,
                              content=content,
                              overlays=overlays_html,
                              resource_url=resource_url,
                              description=pages[url]['description'],
                              title=name,
                              featured_boards=feat_boards_html,
                              langcode=lang,
                              nav_html=nav_html,
                              interfaces=interfaces_menu(pages[url]),
                              body_class=body_class,
                              crumbtrail=crumbtrail,
                              api_image="https://api.pinout.xyz/v1/img/{url}.png".format(url=url)
                              )

    key = url

    if url not in ['index', '404', 'boards']:
        url = os.path.join('pinout', url)

    if 'source' in pages[key]:
        debug(0, '>> Saving: {src} => {url}.html'.format(url=url, src=pages[key]['source']))

    with open(os.path.join('output', lang, '{}.html'.format(url)), 'w') as f:
        f.write(html)

print('\nAll done!')
