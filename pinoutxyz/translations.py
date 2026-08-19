import os
import urllib.parse

from . import documents, overlays, settings

TRANSLATABLE = {'name', 'description', 'title', 'page_url', 'docs'}
LOCALISED = {'url', 'buy', 'github', 'schematic'}
PIN_MAPS = {'pin', 'power', 'ground', 'i2c'}
EEPROM_VALUES = {'True', 'False', 'None', 'detect', 'setup'}

SOURCE = 'en'


def frontmatter(path):
    return documents.frontmatter(path) or {}


def body(path):
    text = open(path, encoding='utf-8', errors='replace').read().replace('\r\n', '\n')
    return documents.FRONTMATTER.sub('', text).strip()


def source_overlays(root):
    return {os.path.basename(path): path for path in overlays.paths(root, SOURCE)}


def source_frontmatter(root):
    return {name: frontmatter(path) for name, path in source_overlays(root).items()}


def sources(root, lang):
    found = {}
    clashes = []

    for path in overlays.paths(root, lang):
        name = os.path.basename(path)
        if name in found:
            clashes.append((path, found[name]))
        found[name] = path

    return found, clashes


def structure(value):
    if isinstance(value, dict):
        return {str(key): structure(inner) for key, inner in value.items() if key != 'name'}
    return value


def same_host(one, other):
    try:
        return urllib.parse.urlparse(one).netloc == urllib.parse.urlparse(other).netloc
    except (AttributeError, ValueError):
        return False


def check_source(path, data):
    findings = []

    if str(data.get('eeprom')) not in EEPROM_VALUES:
        findings.append((path, 'eeprom: unknown value {!r}'.format(data['eeprom'])))

    for token in str(data.get('type', '')).split(','):
        token = token.strip()
        if token and token != token.lower():
            findings.append((path, 'type: {!r} is not lower case'.format(token)))

    return findings


def compare(path, data, source):
    findings = []

    for key in sorted((set(source) - set(data)) - TRANSLATABLE):
        findings.append((path, '{}: missing, English has {!r}'.format(key, source[key])))

    for key in sorted((set(data) - set(source)) - TRANSLATABLE):
        findings.append((path, '{}: not in English'.format(key)))

    for key in sorted((set(source) & set(data)) - TRANSLATABLE):
        theirs, ours = structure(data[key]), structure(source[key])

        if theirs == ours:
            continue

        if key in LOCALISED and same_host(theirs, ours):
            continue

        if isinstance(theirs, dict) and isinstance(ours, dict) and key in PIN_MAPS:
            differs = set(theirs) ^ set(ours)
            differs |= {key for key in set(theirs) & set(ours) if theirs[key] != ours[key]}
            findings.append((path, '{}: differs at {}'.format(key, ', '.join(sorted(differs)))))
        else:
            findings.append((path, '{}: {!r}, English has {!r}'.format(key, data[key], source[key])))

    return findings


def check(root, lang, english, source, discovered):
    findings = []
    found, clashes = discovered

    for path, shadowed in clashes:
        findings.append((path, 'also exists as {}, only one will be built'.format(shadowed)))

    for name in sorted(set(english) - set(found)):
        findings.append((os.path.join(root, 'src', lang), 'nothing translates {}'.format(name)))

    urls = {}

    for name, path in sorted(found.items()):
        data = frontmatter(path)

        if not data.get('name'):
            findings.append((path, 'name: missing'))
        else:
            url = overlays.page_url(data)
            if url in urls:
                findings.append((path, 'page_url {!r} collides with {}'.format(url, urls[url])))
            urls[url] = path

        if lang == SOURCE:
            findings += check_source(path, data)
            continue

        if name not in english:
            findings.append((path, 'no English counterpart'))
            continue

        findings += compare(path, data, source[name])

    return findings


def coverage(root, lang, english):
    translated = []
    outstanding = []
    stale = []

    for name, path in sorted(sources(root, lang)[0].items()):
        if name not in english:
            continue
        if os.sep + 'overlay' + os.sep in path:
            translated.append(name)
        elif body(path) == body(english[name]):
            outstanding.append(name)
        else:
            stale.append(name)

    return translated, outstanding, stale


def report_check(root, languages):
    english = source_overlays(root)
    source = source_frontmatter(root)
    findings = []

    print('Checking {} overlays against src/{}'.format(len(english), SOURCE))

    for lang in languages:
        discovered = sources(root, lang)
        found = check(root, lang, english, source, discovered)
        print('  {:4} {:4} overlays, {:4} findings'.format(lang, len(discovered[0]), len(found)))
        findings += found

    findings.sort()
    previous = None

    for path, message in findings:
        if path != previous:
            print(path)
            previous = path
        print('  {}'.format(message))

    print('\n{} findings'.format(len(findings)))

    return 1 if findings else 0


def report_list(root, languages):
    english = source_overlays(root)
    names = settings.language_names(root)
    total = len(english)

    print('{:6} {:12} {:>12} {:>12} {:>8}'.format('code', 'language', 'translated', 'outstanding', 'stale'))

    for lang in languages:
        if lang == SOURCE:
            continue
        translated, outstanding, stale = coverage(root, lang, english)
        print('{:6} {:12} {:>12} {:>12} {:>8}'.format(
            lang, names.get(lang, (lang, lang))[0],
            '{}/{}'.format(len(translated), total), len(outstanding), len(stale)))

    print('\nstale counts English copies in translate/ that no longer match src/en')

    return 0


def report_outstanding(root, lang, which='outstanding'):
    english = source_overlays(root)
    translated, outstanding, stale = coverage(root, lang, english)
    listing = {'outstanding': outstanding, 'stale': stale, 'translated': translated}[which]

    for name in listing:
        print(name)

    print('\n{} {} of {} overlays'.format(len(listing), which, len(english)))

    return 0
