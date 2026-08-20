import json
import re

import markdown
import yaml

FRONTMATTER = re.compile(r'<!--(JSON:|\n---\n)(.*?)-->', re.DOTALL)
HEADING = re.compile(r'^#[^\#](.*)$', re.MULTILINE)
TABLE_SCROLL = ('<div class="table-scroll"><table', '</table></div>')


class Loader(yaml.SafeLoader):
    def __init__(self, stream):
        super().__init__(stream)
        self.duplicates = []


def construct_mapping(loader, node, deep=False):
    seen = set()

    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            loader.duplicates.append(key)
        seen.add(key)

    return yaml.SafeLoader.construct_mapping(loader, node, deep)


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def load_yaml(text, warn=None):
    loader = Loader(text)

    try:
        data = loader.get_single_data()
    finally:
        loader.dispose()

    if warn is not None:
        for key in loader.duplicates:
            warn('duplicate key {!r} in the frontmatter, only the last one is used'.format(key))

    return data


def to_html(text):
    html = markdown.markdown(text, extensions=['fenced_code'])
    return html.replace('<table', TABLE_SCROLL[0]).replace('</table>', TABLE_SCROLL[1])


def frontmatter(path, warn=None):
    return parse(open(path).read().replace('\r', ''), prefixed(path, warn))


def prefixed(path, warn):
    if warn is None:
        return None
    return lambda message: warn('{}: {}'.format(path, message))


def parse(text, warn=None):
    match = FRONTMATTER.search(text)
    heading = HEADING.search(text)
    if heading is not None:
        heading = heading.group(0).replace('#', '').strip()

    data = None

    if match is not None:
        block = match.group(0)
        if block[4:8].upper().strip() == 'JSON':
            data = json.loads(re.search(r'\{(.*)\}', block, re.DOTALL).group(0))
        else:
            data = load_yaml(re.search(r'\n(.*)\n', block, re.DOTALL).group(0), warn)
        data['title'] = heading
    elif heading is not None:
        data = {'title': heading}

    return data


def load(path, warn=None):
    text = open(path).read().replace('\r', '')
    return {'data': parse(text, prefixed(path, warn)), 'html': to_html(FRONTMATTER.sub('', text))}
