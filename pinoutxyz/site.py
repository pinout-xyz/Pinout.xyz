import os

from . import documents, overlays, settings, urls
from .pins import Pins
from .templates import Templates

LEGEND_URLS = (('url_gpio', 'gpio', 'gpio'),
               ('url_ground', 'ground', 'ground'),
               ('url_3v3', '3v3-power', '3v3_power'),
               ('url_5v', '5v-power', '5v_power'))


class Site:
    def __init__(self, root, lang, alternates=None, reporter=None, source=None):
        self.root = root
        self.lang = lang
        self.report = reporter if reporter is not None else Reporter()

        self.settings = settings.load_settings(root, lang)
        self.strings = settings.load_strings(root, lang)
        self.languages = settings.language_names(root)
        self.pins = Pins(root, lang)
        self.templates = Templates(root, lang)
        self.alternates = alternates if alternates is not None else urls.alternates(root)

        self.overlays = overlays.load_all(root, lang, source, self.report.warn)

        found = {overlay['src']: overlay['page_url'] for overlay in self.overlays}
        for key, src, default in LEGEND_URLS:
            self.settings[key] = found.get(src, default)

    @property
    def base_url(self):
        return self.settings['base_url']

    @property
    def resource_url(self):
        return self.settings.get('resource_url') or '/resources/'

    @property
    def url_suffix(self):
        return self.settings.get('url_suffix') or ''

    def markdown(self, path):
        try:
            return documents.to_html(open(os.path.join(self.root, 'src', self.lang, path.lstrip('/'))).read())
        except IOError:
            return ''


class Reporter:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.warnings = 0

    def notice(self, message):
        if self.verbose:
            print('[Notice] {}'.format(message))

    def warn(self, message):
        self.warnings += 1
        print('[Warning] {}'.format(message))

    def info(self, message):
        print(message)
