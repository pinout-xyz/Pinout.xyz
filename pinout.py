import json
import time
import os

print(__file__)

try:
    import yaml
except ImportError:
    exit("This script requires the yaml module\nInstall with: sudo pip install PyYAML")

try:
    unicode('')
except NameError:
    unicode = str

BUILD_ID = str(int(time.time()))
PINOUT_FILE = 'pinout.yaml'
SETTINGS_FILE = 'settings.yaml'
STRINGS_FILE = 'localised.yaml'

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

pins = None
settings = None

master_template = open(os.path.join(BASE_DIR, 'common/layout.html')).read()
twitter_template = open(os.path.join(BASE_DIR, 'common/twittercard.html')).read()


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

    if "twittercard" in kwargs:
        if kwargs["twittercard"]:
            html = html.replace('{{twittercard}}', twitter_template)

    html = html.replace('{{twittercard}}', "")

    strings = args[2]

    for key in strings:
        if type(strings[key]) in [str, unicode]:
            html = html.replace('{{strings:' + key + '}}', strings[key])

    settings = args[3]

    for key in settings:
        if type(settings[key]) in [str, unicode]:
            html = html.replace('{{settings:' + key + '}}', settings[key])

    kwargs['v'] = BUILD_ID

    for key in kwargs:
        if type(kwargs[key]) == dict:
            for (d_key, d_value) in kwargs[key].items():
                html = html.replace('{{' + key + '_' + d_key + '}}', d_value)
        elif type(kwargs[key]) in [str, unicode]:
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
    global pins, settings, strings

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

    pins = pinout['pins']
