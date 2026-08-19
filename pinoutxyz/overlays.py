import glob
import os

from . import documents
from .pins import sanitize_mode
from .slugs import slugify

SUBDIRS = ('overlay', 'translate')


def paths(root, lang):
    found = []
    for subdir in SUBDIRS:
        found += sorted(glob.glob(os.path.join(root, 'src', lang, subdir, '*.md')))
    return found


def duplicates(root, lang):
    seen = {}
    clashes = []
    for path in paths(root, lang):
        name = os.path.basename(path)
        if name in seen:
            clashes.append(name)
        seen[name] = path
    return sorted(clashes)


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


def load(path, warn=None):
    document = documents.load(path)
    data = document['data']

    data['source'] = path
    data['src'] = os.path.basename(path)[:-len('.md')]
    data['long_description'] = document['html']
    data['page_url'] = page_url(data)

    normalise_modes(data, path, warn)

    return data


def load_all(root, lang, warn=None):
    return [load(path, warn) for path in paths(root, lang)]
