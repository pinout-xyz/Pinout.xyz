import os
import unicodedata

from . import documents, overlays, settings

SOURCE = overlays.SOURCE
EEPROM_VALUES = {'True', 'False', 'None', 'detect', 'setup'}


def frontmatter(path):
    return documents.frontmatter(path) or {}


def body(path):
    text = open(path, encoding='utf-8', errors='replace').read().replace('\r\n', '\n')
    return documents.FRONTMATTER.sub('', text).strip()


def pad(value, width):
    wide = sum(1 for character in value if unicodedata.east_asian_width(character) in 'WF')
    return value + ' ' * max(0, width - len(value) - wide)


def check_source(path, data):
    findings = []

    if str(data.get('eeprom')) not in EEPROM_VALUES:
        findings.append((path, 'eeprom: unknown value {!r}'.format(data['eeprom'])))

    for token in str(data.get('type', '')).split(','):
        token = token.strip()
        if token and token != token.lower():
            findings.append((path, 'type: {!r} is not lower case'.format(token)))

    return findings


def check_override(path, data, base):
    findings = []

    for key in sorted(set(data) - set(overlays.OVERRIDE_KEYS) - set(overlays.OVERRIDE_MAPS) - {'title'}):
        findings.append((path, '{}: belongs to English, remove it'.format(key)))

    for key in overlays.OVERRIDE_MAPS:
        entries = data.get(key) or {}
        for entry in sorted(entries, key=str):
            values = entries[entry]
            if entry not in (base.get(key) or {}):
                findings.append((path, '{} {}: not in the English overlay'.format(key, entry)))
                continue
            if not isinstance(values, dict):
                findings.append((path, '{} {}: should be a mapping'.format(key, entry)))
                continue
            for inner in sorted(set(values) - set(overlays.OVERRIDE_ENTRY_KEYS)):
                findings.append((path, '{} {}: {} belongs to English, remove it'.format(key, entry, inner)))

    return findings


def check(root, lang, source):
    findings = []
    urls = {}

    for name, path in sorted(overlays.named(root, lang).items()):
        data = frontmatter(path)

        if lang == SOURCE:
            if not data.get('name'):
                findings.append((path, 'name: missing'))
            else:
                url = overlays.page_url(data)
                if url in urls:
                    findings.append((path, 'page_url {!r} collides with {}'.format(url, urls[url])))
                urls[url] = path
            findings += check_source(path, data)
            continue

        if name not in source:
            findings.append((path, 'no English counterpart'))
            continue

        findings += check_override(path, data, source[name])

        if not data and not body(path):
            findings.append((path, 'overrides nothing, remove it'))

    return findings


def coverage(root, lang, source):
    translated = []
    partial = []
    overrides = overlays.named(root, lang)

    for name in sorted(overrides):
        if name not in source:
            continue
        if body(overrides[name]):
            translated.append(name)
        else:
            partial.append(name)

    absent = sorted(set(source) - set(overrides))

    return translated, partial, absent


def report_check(root, languages):
    source = {name: frontmatter(path) for name, path in overlays.named(root, SOURCE).items()}
    findings = []

    print('Checking against {} English overlays'.format(len(source)))

    for lang in languages:
        found = check(root, lang, source)
        print('  {:4} {:4} overrides, {:4} findings'.format(
            lang, len(overlays.named(root, lang)) if lang != SOURCE else len(source), len(found)))
        findings += found

    findings.sort()

    for path, message in findings:
        print('{}\n  {}'.format(path, message))

    print('\n{} findings'.format(len(findings)))

    return 1 if findings else 0


def report_list(root, languages):
    source = overlays.named(root, SOURCE)
    names = settings.language_names(root)
    total = len(source)

    print('{} {} {:>12} {:>12} {:>10}'.format(
        pad('code', 6), pad('language', 12), 'translated', 'text only', 'English'))

    for lang in languages:
        if lang == SOURCE:
            continue
        translated, partial, absent = coverage(root, lang, source)
        print('{} {} {:>12} {:>12} {:>10}'.format(
            pad(lang, 6), pad(names.get(lang, (lang, lang))[0], 12),
            '{}/{}'.format(len(translated), total), len(partial), len(absent)))

    print('\ntext only overrides just a name, description or pin label; English pages fall back to src/en')

    return 0


def report_listing(root, lang, which):
    source = overlays.named(root, SOURCE)
    translated, partial, absent = coverage(root, lang, source)
    listing = {'outstanding': absent, 'partial': partial, 'translated': translated}[which]

    for name in listing:
        print(name)

    print('\n{} {} of {} overlays'.format(len(listing), which, len(source)))

    return 0
