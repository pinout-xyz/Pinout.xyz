#!/usr/bin/env python3

import json
import sys

sys.path.insert(0, '..')

from pinoutxyz import documents, overlays

BASE_DIR = '..'

lang = sys.argv[1] if len(sys.argv) > 1 else 'en'

index = []

for path in overlays.paths(BASE_DIR, lang):
    data = documents.load(path)['data']
    slug = overlays.page_url(data)

    index.append({
        'name': data['name'],
        'class': data['class'],
        'detail': '/v1/detail/{}.json'.format(slug),
        'url': '/pinout/{}'.format(slug),
    })

print(json.dumps(index, sort_keys=True))
