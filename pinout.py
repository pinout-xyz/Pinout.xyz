import json
import time
import markdown

DB_FILE = 'pi-pinout.json'
SETTINGS_FILE = 'settings.json'

pins = None
settings = None

def render_html(*args, **kwargs):
    html = args[0]
    kwargs['v'] = str(int(time.time()))
    for key in kwargs:
        html = html.replace('{{' + key + '}}', kwargs[key])
    return html

def bcm_to_physical(pin):
    for idx in pins:
        compare_pin = pins[idx]
        if 'scheme' in compare_pin:
            if 'bcm' in compare_pin['scheme']:
                if compare_pin['scheme']['bcm'] == int(pin):
                    #print("Mapping BCM{} to {}".format(pin, str(idx)))
                    return str(idx)

def physical_to_bcm(pin):
    pin = pins[pin]
    if 'scheme' in pin:
        if 'bcm' in pin['scheme']:
            return str(pin['scheme']['bcm'])
    return None

def physical_to_wiringpi(pin):
    pin = pins[pin]
    if 'scheme' in pin:
        if 'wiringpi' in pin['scheme']:
            return str(pin['scheme']['wiringpi'])
    return None

def physical_to(pin, scheme='bcm'):
    if scheme in ['bcm','wiringpi']:
        pin = pins[pin]
        if 'scheme' in pin:
            if scheme in pin['scheme']:
                return str(pin['scheme'][scheme])
    elif scheme == 'physical':
        return pin
    return None

def load(lang='en-GB'):
    global pins, settings
    db = json.load(open('src/{}/{}'.format(lang,DB_FILE)))
    settings = json.load(open('src/{}/{}'.format(lang,SETTINGS_FILE)))
    pins = db['pins']


