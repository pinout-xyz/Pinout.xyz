#!/usr/bin/env python3

import glob
import os
import sys
import urllib.parse

from pinoutxyz import documents, overlays

TRANSLATABLE = {'name', 'description', 'title', 'page_url', 'docs'}
LOCALISED = {'url', 'buy', 'github', 'schematic'}
PIN_MAPS = {'pin', 'power', 'ground', 'i2c'}
EEPROM_VALUES = {'True', 'False', 'None', 'detect', 'setup'}


def load(path):
    return documents.load(path)['data'] or {}


def sources(lang):
    found = {}
    duplicates = []

    for subdir in ('overlay', 'translate'):
        for path in sorted(glob.glob('src/{}/{}/*.md'.format(lang, subdir))):
            name = os.path.basename(path)
            if name in found:
                duplicates.append((path, found[name]))
            found[name] = path

    return found, duplicates


def structure(value):
    if isinstance(value, dict):
        return {str(key): structure(inner) for key, inner in value.items() if key != 'name'}
    return value


def same_host(one, other):
    try:
        return urllib.parse.urlparse(one).netloc == urllib.parse.urlparse(other).netloc
    except (AttributeError, ValueError):
        return False


def check_english(path, data):
    findings = []

    if str(data.get('eeprom')) not in EEPROM_VALUES:
        findings.append((path, "eeprom: unknown value {!r}".format(data['eeprom'])))

    for token in str(data.get('type', '')).split(','):
        token = token.strip()
        if token and token != token.lower():
            findings.append((path, "type: {!r} is not lower case".format(token)))

    return findings


def check(lang, english):
    findings = []
    found, duplicates = sources(lang)

    for path, shadowed in duplicates:
        findings.append((path, "also exists as {}, only one will be built".format(shadowed)))

    for name in sorted(set(english) - set(found)):
        findings.append(('src/{}'.format(lang), "nothing translates {}".format(name)))

    urls = {}

    for name, path in sorted(found.items()):
        data = load(path)

        if not data.get('name'):
            findings.append((path, "name: missing"))
        else:
            url = overlays.page_url(data)
            if url in urls:
                findings.append((path, "page_url {!r} collides with {}".format(url, urls[url])))
            urls[url] = path

        if lang == 'en':
            findings += check_english(path, data)
            continue

        if name not in english:
            findings.append((path, "no English counterpart"))
            continue

        source = english[name]

        for key in sorted((set(source) - set(data)) - TRANSLATABLE):
            findings.append((path, "{}: missing, English has {!r}".format(key, source[key])))

        for key in sorted((set(data) - set(source)) - TRANSLATABLE):
            findings.append((path, "{}: not in English".format(key)))

        for key in sorted((set(source) & set(data)) - TRANSLATABLE):
            theirs, ours = structure(data[key]), structure(source[key])

            if theirs == ours:
                continue

            if key in LOCALISED and same_host(theirs, ours):
                continue

            if isinstance(theirs, dict) and isinstance(ours, dict) and key in PIN_MAPS:
                differs = set(theirs) ^ set(ours)
                differs |= {k for k in set(theirs) & set(ours) if theirs[k] != ours[k]}
                findings.append((path, "{}: differs at {}".format(key, ', '.join(sorted(differs)))))
            else:
                findings.append((path, "{}: {!r}, English has {!r}".format(key, data[key], source[key])))

    return findings


available = sorted(os.path.basename(d) for d in glob.glob('src/??') if os.path.isdir(d))

languages = sys.argv[1:] or available

for language in languages:
    if language not in available:
        sys.exit("No such language '{}', expected one of: {}".format(language, ', '.join(available)))

english = {os.path.basename(path): load(path) for path in glob.glob('src/en/overlay/*.md')}

findings = []

for language in languages:
    findings += check(language, english)

findings.sort()

previous = None

for path, message in findings:
    if path != previous:
        print(path)
        previous = path
    print("  {}".format(message))

print("\n{} findings".format(len(findings)))

sys.exit(1 if findings else 0)
