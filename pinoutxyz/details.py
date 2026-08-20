import markdown

EXCLUDE_PINCOUNTS = ('3v3-power', '5v-power', 'ground', 'iface-jtag', 'i2c',
                     'iface-gpclk', 'wiringpi', 'spi', 'iface-1wire')

POWER_PINS_5V = ('2', '4')
POWER_PINS_3V3 = ('1', '17')
I2C_PINS = ('3', '5')
SPI_PINS = ('19', '21', '23')
POWER_OVERLAYS = ('3v3-power', '5v-power', 'ground')

LINK_KEYS = (('url', 'more_information'),
             ('github', 'github_repository'),
             ('schematic', 'board_schematic'),
             ('buy', 'buy_now'))


def manufacturer(site, overlay):
    if 'manufacturer' not in overlay:
        return None

    if 'collected' in overlay:
        return site.strings['made_by'].format(manufacturer=overlay['manufacturer'])

    link = '<a href="{site_url}/boards#manufacturer={manufacturer}">{manufacturer}</a>'.format(
        site_url=site.settings['site_url'], manufacturer=overlay['manufacturer'])
    return site.strings['made_by'].format(manufacturer=link)


def form_factor(site, overlay):
    strings = site.strings
    pincount = int(overlay['pincount'])
    header = strings['pin_header'].format(pincount)
    excluded = overlay['src'] in EXCLUDE_PINCOUNTS

    if 'formfactor' in overlay:
        formfactor = str(overlay['formfactor']).lower()
        if pincount == 40 and formfactor == 'hat':
            return strings['type_hat']
        if pincount == 40 and formfactor == 'phat':
            return strings['type_phat']
        if pincount == 40 and formfactor == '40-way':
            return header
        return None if excluded else header

    if pincount == 40:
        return strings['type_hat']
    if pincount == 26:
        return strings['type_classic']
    return None if excluded else header


def eeprom(site, overlay):
    value = str(overlay['eeprom'])
    if value in ('detect', 'True'):
        return site.strings['eeprom_detect']
    if value == 'setup':
        return site.strings['eeprom_setup']
    return None


def power(site, overlay):
    uses_5v = False
    uses_3v3 = False

    for pin in overlay['power']:
        pin = str(pin)
        if pin.startswith('bcm'):
            pin = site.pins.bcm_to_physical(pin[3:])
        if pin in POWER_PINS_5V:
            uses_5v = True
        if pin in POWER_PINS_3V3:
            uses_3v3 = True

    if uses_5v and uses_3v3:
        return site.strings['uses_5v_and_3v3']
    if uses_5v:
        return site.strings['uses_5v']
    if uses_3v3:
        return site.strings['uses_3v3']
    return None


def pin_usage(site, overlay):
    found = []
    uses_i2c = False
    uses_spi = False
    uses = 0

    for pin, data in overlay['pin'].items():
        pin = str(pin)
        if pin.startswith('bcm'):
            pin = site.pins.bcm_to_physical(pin[3:])

        if pin in site.pins:
            actual = site.pins[pin]
            if actual['type'] in ('+3v3', '+5v', 'GND') and overlay['src'] not in POWER_OVERLAYS:
                raise Exception("{} includes a reference to a {} pin ({}), which isn't allowed".format(
                    overlay['source'], actual['type'], pin))
            uses += 1

        if data is not None and 'mode' in data:
            if pin in I2C_PINS and data['mode'] == 'i2c':
                uses_i2c = True
            if pin in SPI_PINS and data['mode'] == 'spi':
                uses_spi = True

    if uses > 0 and overlay['src'] not in EXCLUDE_PINCOUNTS:
        found.append(site.strings['uses_n_gpio_pins'].format(uses))
    if uses_spi:
        found.append(site.strings['uses_spi'])
    if uses_i2c:
        found.append(site.strings['uses_i2c'])

    return found


def i2c_devices(overlay):
    found = []

    for address, data in overlay['i2c'].items():
        if data is None or 'device' not in data:
            continue

        alternate = data.get('alternate')
        if isinstance(alternate, list):
            alternate = ', '.join(alternate)

        if alternate is not None:
            found.append('{}: {} (Alt: {})'.format(address, data['device'], alternate))
        else:
            found.append('{}: {}'.format(address, data['device']))

    return found


def links(site, overlay, warn):
    found = []

    for key, string in LINK_KEYS:
        if key not in overlay:
            continue
        if overlay[key] is None:
            warn("{} defined in {}, but missing a value.".format(key, overlay['source']))
            continue
        found.append('[{}]({})'.format(site.strings[string], overlay[key]))

    return found


def describe(site, overlay, warn):
    if overlay.get('type') == 'info':
        return overlay['long_description']

    if 'type' not in overlay:
        overlay['type'] = site.strings['group_other']

    if overlay.get('power') is None and 'power' in overlay:
        overlay['power'] = {}

    found = []

    for value in (manufacturer(site, overlay),
                  form_factor(site, overlay) if 'pincount' in overlay else None,
                  eeprom(site, overlay) if 'eeprom' in overlay else None,
                  power(site, overlay) if 'power' in overlay and 'power' not in overlay['type'] else None):
        if value is not None:
            found.append(value)

    if 'pin' in overlay:
        found += pin_usage(site, overlay)

    if 'i2c' in overlay:
        found += i2c_devices(overlay)

    found += links(site, overlay, warn)

    image = ''
    if 'image' in overlay:
        image = '<img loading="lazy" src="/resources/boards/{}" alt="{}" />'.format(
            overlay['image'], overlay['name'])

    if not found and not image:
        return overlay['long_description']

    details = '<div class="details"><h2>{}</h2>{}{}</div>'.format(
        site.strings['details'],
        markdown.markdown('\n'.join('* ' + item for item in found)),
        image)

    return '{}\n{}'.format(overlay['long_description'], details)
