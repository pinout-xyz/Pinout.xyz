import json
import datetime
import os

try:
    import yaml
except ImportError:
    exit("This script requires the yaml module\nInstall with: sudo pip install PyYAML")

BUILD_ID = datetime.datetime.now().isoformat().replace(":","").replace("-", "").split(".")[0]
PINOUT_FILE = 'pinout.yaml'
FUNCTIONS_FILE = 'common/pin-functions.yaml'
SETTINGS_FILE = 'settings.yaml'
STRINGS_FILE = 'localised.yaml'

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

MODES = {
    '1wire': '1wire',
    '1-wire': '1wire',
    'chipselect': 'chipselect',
    'cs': 'chipselect',
    'eeprom_wp': 'eeprom_wp',
    'gpio': 'gpio',
    'i2c': 'i2c',
    'i2s': 'pcm',
    'input': 'input',
    'input/output': 'gpio',
    'output': 'output',
    'pcm': 'pcm',
    'pwm': 'pwm',
    'spi': 'spi',
    'uart': 'uart',
}

pins = None
pin_functions = None
settings = None

master_template = open(os.path.join(BASE_DIR, 'common/layout.html')).read()
twitter_template = open(os.path.join(BASE_DIR, 'common/opengraph.html')).read()


def sanitize_mode(mode):
    return MODES.get(str(mode).strip().lower())


def get_setting(setting, default=None):
    if setting in settings and settings[setting] is not None:
        return settings[setting]
    return default


def get_string(string, default=None):
    if string in strings and strings[string] is not None:
        return strings[string]
    return default


def render_html(*args, **kwargs):
    html = master_template
    html = html.replace('{{main_content}}', args[0])
    html = html.replace('{{footer}}', args[1])

    if "opengraph" in kwargs:
        if kwargs["opengraph"]:
            html = html.replace('{{opengraph}}', twitter_template)

    html = html.replace('{{opengraph}}', "")

    strings = args[2]

    for key in strings:
        if isinstance(strings[key], str):
            html = html.replace('{{strings:' + key + '}}', strings[key])

    settings = args[3]

    for key in settings:
        if isinstance(settings[key], str):
            html = html.replace('{{settings:' + key + '}}', settings[key])

    kwargs['v'] = BUILD_ID

    for key in kwargs:
        if type(kwargs[key]) == dict:
            for (d_key, d_value) in kwargs[key].items():
                html = html.replace('{{' + key + '_' + d_key + '}}', d_value)
        elif isinstance(kwargs[key], str):
            html = html.replace('{{' + key + '}}', kwargs[key])

    return html


def bcm_to_physical(pin):
    return physical_from(pin, 'bcm')


def wiringpi_to_physical(pin):
    return physical_from(pin, 'wiringpi')


def physical_from(pin, scheme='bcm'):
    if scheme in ['bcm', 'wiringpi']:
        for idx in pins:
            compare_pin = pins[idx]
            if 'scheme' in compare_pin:
                if scheme in compare_pin['scheme']:
                    if compare_pin['scheme'][scheme] == int(pin):
                        # print("Mapping {}{} to {}".format(scheme, pin, str(idx)))
                        return str(idx)
    elif scheme == 'physical':
        return pin
    return None


def physical_to_bcm(pin):
    return physical_to(pin, 'bcm')


def physical_to_wiringpi(pin):
    return physical_to(pin, 'wiringpi')


def physical_to(pin, scheme='bcm'):
    if scheme in ['bcm', 'wiringpi']:
        pin = pins[pin]
        if 'scheme' in pin:
            if scheme in pin['scheme']:
                return str(pin['scheme'][scheme])
    elif scheme == 'physical':
        return pin
    return None


def load(lang='en'):
    global pins, pin_functions, settings, strings

    settings_path = os.path.join(BASE_DIR, 'src/{}/{}'.format(lang, SETTINGS_FILE))
    strings_path = os.path.join(BASE_DIR, 'src/{}/template/{}'.format(lang, STRINGS_FILE))
    pinout_path = os.path.join(BASE_DIR, 'src/{}/template/{}'.format(lang, PINOUT_FILE))

    if SETTINGS_FILE.endswith('.yaml'):
        settings = yaml.safe_load(open(settings_path).read())
    else:
        settings = json.load(open(settings_path))

    if STRINGS_FILE.endswith('.yaml'):
        strings = yaml.safe_load(open(strings_path).read())
    else:
        strings = json.load(open(strings_path))

    if PINOUT_FILE.endswith('.yaml'):
        pinout = yaml.safe_load(open(pinout_path).read())
    else:
        pinout = json.load(open(pinout_path))

    site_url = get_setting('site_url') or ''
    settings['site_url'] = site_url
    settings['base_url'] = site_url + get_setting('base_url', '/pinout/')

    pin_functions = yaml.safe_load(open(os.path.join(BASE_DIR, FUNCTIONS_FILE)).read())

    pins = pinout['pins']
