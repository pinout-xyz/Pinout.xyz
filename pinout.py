import json
import time

try:
    import yaml
except ImportError:
    exit("This script requires the yaml module\nInstall with: sudo pip install PyYAML")


PINOUT_FILE = 'pinout.yaml'
SETTINGS_FILE = 'settings.yaml'
STRINGS_FILE = 'localised.yaml'

pins = None
settings = None

master_template = open('common/layout.html').read()


def get_setting(setting, default = None):
    if setting in settings and settings[setting] != None:
        return settings[setting]
    return default

def get_string(string, default = None):
    if string in strings and strings[string] != None:
        return strings[string]
    return default


def render_html(*args, **kwargs):
    html = master_template
    html = html.replace('{{main_content}}',args[0])
    html = html.replace('{{footer}}',args[1])

    strings = args[2]

    for key in strings:
        if type(strings[key]) in [str, unicode]:
            html = html.replace('{{strings:' + key + '}}', strings[key])

    settings = args[3]

    for key in settings:
        if type(settings[key]) in [str, unicode]:
            html = html.replace('{{settings:' + key + '}}', settings[key])

    kwargs['v'] = str(int(time.time()))

    for key in kwargs:
        if type(kwargs[key]) == dict:
            for d_key, d_value in kwargs[key].iteritems():
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
                        #print("Mapping {}{} to {}".format(scheme, pin, str(idx)))
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
    if SETTINGS_FILE.endswith('.yaml'):
        settings = yaml.load(open('src/{}/{}'.format(lang, SETTINGS_FILE)).read())
    else:
        settings = json.load(open('src/{}/{}'.format(lang, SETTINGS_FILE)))
    if STRINGS_FILE.endswith('.yaml'):
        strings = yaml.load(open('src/{}/template/{}'.format(lang, STRINGS_FILE)).read())
    else:
        strings = json.load(open('src/{}/template/{}'.format(lang, STRINGS_FILE)))
    if PINOUT_FILE.endswith('.yaml'):
        pinout = yaml.load(open('src/{}/template/{}'.format(lang, PINOUT_FILE)).read())
    else:
        pinout = json.load(open('src/{}/template/{}'.format(lang, PINOUT_FILE)))
    pins = pinout['pins']
