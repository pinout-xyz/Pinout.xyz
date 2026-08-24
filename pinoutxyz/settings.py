import glob
import os

import yaml

SETTINGS_FILE = 'src/{}/settings.yaml'
STRINGS_FILE = 'src/{}/template/localised.yaml'
SOURCE = 'en'

DEFAULTS = {
    'home': 'Home',
    'boards': 'Boards',
    'details': 'Details',
    'pin_header': '{} pin header',
    'form_undefined': 'Undefined',
    'group_other': 'other',
    'type_hat': 'HAT form-factor',
    'type_phat': 'pHAT form-factor',
    'type_classic': 'Classic form-factor',
    'eeprom_detect': 'Uses VID/PID',
    'eeprom_setup': 'Uses EEPROM',
    'overlay_in_config': 'Needs {} in /boot/firmware/config.txt',
    'uses_5v_and_3v3': 'Needs 5v and 3v3 power',
    'uses_5v': 'Needs 5v power',
    'uses_3v3': 'Needs 3v3 power',
    'uses_i2c': 'Uses I2C',
    'uses_spi': 'Uses SPI',
    'uses_n_gpio_pins': 'Uses {} GPIO pins',
    'bcm_pin_rev1_pi': 'GPIO/BCM pin {} on Rev 1 ( very early ) Pi',
    'supported_on': 'Supported on {}',
    'physical_pin_n': 'Physical/Board pin {}',
    'physical_pin_label': 'physical pin',
    'gpio_header': 'GPIO header',
    'pins_odd': 'Odd-numbered pins',
    'pins_even': 'Even-numbered pins',
    'skip_to_content': 'Skip to content',
    'wiring_pi_pin': 'Wiring Pi pin {}',
    'made_by': 'Made by {manufacturer}',
    'more_information': 'More Information',
    'github_repository': 'GitHub Repository',
    'board_schematic': 'Schematic',
    'buy_now': 'Buy Now',
    'translate_msg': 'This page needs translating, can you help?',
    'browse_addons': 'Browse more HATs, pHATs and add-ons',
    'mirror_pinout': 'Mirror the pinout, as seen from the underside of the board',
    'pin_functions': 'Alternate functions by model',
    'rotate_pinout': 'Rotate the pinout 180 degrees',
    'choose_language': 'Choose a language',
    'return_home': 'Return to the Raspberry Pi GPIO Pinout',
    'boards_title': 'Raspberry Pi HATs, pHATs &amp; Add-ons',
    'boards_subtitle': 'Click on a HAT, pHAT or add-on for more details and to see which pins it uses!'
}


def languages(root='.'):
    return sorted(os.path.basename(os.path.dirname(path))
                  for path in glob.glob(os.path.join(root, 'src/??/settings.yaml')))


def language_names(root='.'):
    names = {}
    for code in languages(root):
        loaded = load_settings(root, code)
        names[code] = (loaded.get('language', code), loaded.get('flag', code))
    return names


def resolve(root, template, lang):
    path = os.path.join(root, template.format(lang))
    if os.path.exists(path):
        return path
    return os.path.join(root, template.format(SOURCE))


def load_settings(root, lang):
    loaded = yaml.safe_load(open(os.path.join(root, SETTINGS_FILE.format(lang))).read())
    site_url = loaded.get('site_url') or ''
    loaded['site_url'] = site_url
    loaded['base_url'] = site_url + (loaded.get('base_url') or '/pinout/')
    return loaded


def load_strings(root, lang):
    loaded = yaml.safe_load(open(resolve(root, STRINGS_FILE, lang)).read())
    strings = loaded.get('strings', {})

    if isinstance(strings, list):
        strings = {key: value for item in strings for key, value in item.items()}

    for key, value in DEFAULTS.items():
        strings.setdefault(key, value)

    return strings
