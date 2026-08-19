#!/usr/bin/env python3

import json
import os
import sys

sys.path.insert(0, '..')

from pinoutxyz import documents, overlays

BASE_DIR = '..'
OUTPUT_DIR = 'v1/detail'

lang = sys.argv[1] if len(sys.argv) > 1 else 'en'

for path in overlays.paths(BASE_DIR, lang):
    data = documents.load(path)['data']
    slug = overlays.page_url(data)

    data['pinout_url'] = 'https://pinout.xyz/pinout/{}'.format(slug)

    for key in ('power', 'ground'):
        if isinstance(data.get(key), dict):
            data[key] = list(data[key].keys())

    with open(os.path.join(OUTPUT_DIR, '{}.json'.format(slug)), 'w') as handle:
        handle.write(json.dumps(data))
