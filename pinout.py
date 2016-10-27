import json
import time

try:
    import yaml
except ImportError:
    exit("This script requires the yaml module\nInstall with: sudo pip install PyYAML")


DB_FILE = 'pi-pinout.yaml'
SETTINGS_FILE = 'settings.yaml'

pins = None
settings = None


def get_setting(setting, default = None):
    if setting in settings and settings[setting] != None:
        return settings[setting]
    return default


def render_html(*args, **kwargs):
    html = args[0]
    kwargs['v'] = str(int(time.time()))
    for key in kwargs:
        if type(kwargs[key]) == dict:
            for d_key, d_value in kwargs[key].iteritems():
                html = html.replace('{{' + key + '_' + d_key + '}}', d_value)
        elif type(kwargs[key]) == str:
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
    global pins, settings
    if DB_FILE.endswith('.yaml'):
        db = yaml.load(open('src/{}/{}'.format(lang, DB_FILE)).read())
    else:
        db = json.load(open('src/{}/{}'.format(lang, DB_FILE)))
    if SETTINGS_FILE.endswith('.yaml'):
        settings = yaml.load(open('src/{}/{}'.format(lang, SETTINGS_FILE)).read())
    else:
        settings = json.load(open('src/{}/{}'.format(lang, SETTINGS_FILE)))
    pins = db['pins']


