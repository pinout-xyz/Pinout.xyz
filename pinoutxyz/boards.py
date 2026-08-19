TYPES = {
    'adc': 'ADC', 'audio': 'Audio', 'com': 'COM', 'dac': 'DAC', 'display': 'Display',
    'gesture': 'Gesture', 'gps': 'GPS', 'instrument': 'Instrument', 'io': 'IO', 'iot': 'IOT',
    'led': 'LED', 'lora': 'LoRa', 'mcu': 'MCU', 'motor': 'Motor', 'multi': 'Multi',
    'network': 'Network', 'other': 'Other', 'pinout': 'pinout', 'power': 'Power',
    'radio': 'Radio', 'relay': 'Relay', 'rtc': 'RTC', 'sensor': 'Sensor', 'touch': 'Touch',
    'usb': 'USB',
}

REMAPPED_TYPES = {'iot': 'radio'}

LOCALISED_TYPES = {
    'es': {'gesture': 'Gestos', 'other': 'Otro'},
}

FORMFACTORS = {'custom': 'Custom', 'hat': 'HAT', 'phat': 'PHAT', 'usb': 'USB'}


def type_names(lang):
    names = dict(TYPES)
    names.update(LOCALISED_TYPES.get(lang, {}))
    return names


def sanitize_type(names, value):
    handle = value.strip().lower()

    if handle in names:
        return names[handle]

    if handle in REMAPPED_TYPES:
        return names[REMAPPED_TYPES[handle]]

    return None


def types(site, overlay, warn):
    names = type_names(site.lang)
    found = []

    for value in overlay['type'].split(','):
        name = sanitize_type(names, value)
        if name is None:
            warn('Rejecting unsupported type: {} in overlay: {}'.format(value.strip(), overlay['name']))
            continue
        found.append(name)

    if len(found) > 1 and 'Multi' not in found:
        found.append('Multi')

    if not found:
        warn('No type(s) found in overlay: {}'.format(overlay['name']))
        found = [site.strings['group_other']]

    return ','.join(found)


def formfactor(site, overlay, warn):
    if 'formfactor' not in overlay:
        warn('{} missing formfactor'.format(overlay['name']))
        return site.strings['form_undefined']

    return FORMFACTORS.get(str(overlay['formfactor']).lower(), site.strings['form_undefined'])
