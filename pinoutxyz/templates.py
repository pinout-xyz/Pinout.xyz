import datetime
import os

LAYOUT_FILE = 'common/layout.html'
OPENGRAPH_FILE = 'common/opengraph.html'
PAGE_FILE = 'common/page.html'
BOARDS_FILE = 'common/boards.html'
FOOTER_FILE = 'src/{}/template/footer.html'

BUILD_ID = datetime.datetime.now().isoformat().replace(':', '').replace('-', '').split('.')[0]


class Templates:
    def __init__(self, root, lang):
        self.layout = read(root, LAYOUT_FILE)
        self.opengraph = read(root, OPENGRAPH_FILE)
        self.page = read(root, PAGE_FILE)
        self.boards = read(root, BOARDS_FILE)
        self.footer = read(root, FOOTER_FILE.format(lang))

    def render(self, main, strings, settings, opengraph=False, **kwargs):
        html = self.layout
        html = html.replace('{{main_content}}', main)
        html = html.replace('{{footer}}', self.footer)
        html = html.replace('{{opengraph}}', self.opengraph if opengraph else '')

        for key, value in strings.items():
            if isinstance(value, str):
                html = html.replace('{{strings:' + key + '}}', value)

        for key, value in settings.items():
            if isinstance(value, str):
                html = html.replace('{{settings:' + key + '}}', value)

        kwargs['v'] = BUILD_ID

        for key, value in kwargs.items():
            if isinstance(value, dict):
                for inner_key, inner_value in value.items():
                    html = html.replace('{{' + key + '_' + inner_key + '}}', inner_value)
            elif isinstance(value, str):
                html = html.replace('{{' + key + '}}', value)

        return html


def read(root, path):
    return open(os.path.join(root, path)).read()
