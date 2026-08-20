import copy
import glob
import os

from . import documents
from .pins import sanitize_mode
from .slugs import slugify

SOURCE = 'en'
OVERLAY_DIR = 'overlay'

OVERRIDE_KEYS = ('name', 'description', 'page_url', 'url', 'buy', 'github', 'schematic', 'docs')

EEPROM_PINS = {'27': 'EEPROM Data', '28': 'EEPROM Clock'}
OVERRIDE_MAPS = ('pin', 'i2c')
OVERRIDE_ENTRY_KEYS = ('name', 'description')


def paths(root, lang):
    return sorted(glob.glob(os.path.join(root, 'src', lang, OVERLAY_DIR, '*.md')))


def named(root, lang):
    found = {}
    for path in paths(root, lang):
        found[os.path.basename(path)] = path
    return found


def page_url(data):
    return data.get('page_url') or slugify(data['name'])


def normalise_modes(data, path, warn):
    for pin, pin_data in (data.get('pin') or {}).items():
        if not isinstance(pin_data, dict) or 'mode' not in pin_data:
            continue
        mode = sanitize_mode(pin_data['mode'])
        if mode is None and warn is not None:
            warn("{}: Unsupported mode '{}' on pin {}".format(path, pin_data['mode'], pin))
        pin_data['mode'] = mode


def add_eeprom_pins(data):
    if str(data.get('eeprom')) != 'setup':
        return

    pins = data.setdefault('pin', None) or {}
    data['pin'] = pins

    for pin, name in EEPROM_PINS.items():
        if pin not in pins and int(pin) not in pins:
            pins[pin] = {'name': name, 'mode': 'i2c'}


def describe(data, path, html):
    data['source'] = path
    data['src'] = os.path.basename(path)[:-len('.md')]
    data['long_description'] = html
    return data


def load(path, warn=None):
    document = documents.load(path, warn)
    data = describe(document['data'], path, document['html'])
    normalise_modes(data, path, warn)
    add_eeprom_pins(data)
    data['page_url'] = page_url(data)
    return data


def load_source(root, warn=None):
    source = {}
    for path in paths(root, SOURCE):
        document = documents.load(path, warn)
        data = describe(document['data'], path, document['html'])
        normalise_modes(data, path, warn)
        add_eeprom_pins(data)
        source[os.path.basename(path)] = data
    return source


def finalise(data, translated=True):
    data['page_url'] = page_url(data)
    data['translated'] = translated
    return data


def merge(base, override, path, warn=None):
    merged = copy.deepcopy(base)

    for key in OVERRIDE_KEYS:
        if key in override:
            merged[key] = override[key]

    for key in OVERRIDE_MAPS:
        for entry, values in (override.get(key) or {}).items():
            target = (merged.get(key) or {}).get(entry)
            if not isinstance(values, dict):
                continue
            if not isinstance(target, dict):
                if warn is not None:
                    warn('{}: {} {} is not in the English overlay'.format(path, key, entry))
                continue
            for inner in OVERRIDE_ENTRY_KEYS:
                if inner in values:
                    target[inner] = values[inner]

    return merged


def load_all(root, lang, source=None, warn=None):
    if source is None:
        source = load_source(root, warn)

    if lang == SOURCE:
        return [finalise(copy.deepcopy(base)) for base in source.values()]

    overrides = named(root, lang)
    loaded = []

    for name in sorted(overrides):
        if name not in source:
            warn('{} has no English counterpart'.format(overrides[name]))

    for name, base in source.items():
        path = overrides.get(name)

        if path is None:
            loaded.append(finalise(copy.deepcopy(base), False))
            continue

        document = documents.load(path, warn)
        merged = merge(base, document['data'] or {}, path, warn)
        merged['source'] = path

        html = document['html'].strip()
        if html:
            merged['long_description'] = document['html']

        loaded.append(finalise(merged, bool(html)))

    return loaded
