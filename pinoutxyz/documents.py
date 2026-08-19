import json
import re

import markdown
import yaml

FRONTMATTER = re.compile(r'<!--(JSON:|\n---\n)(.*?)-->', re.DOTALL)
HEADING = re.compile(r'^#[^\#](.*)$', re.MULTILINE)
TABLE_SCROLL = ('<div class="table-scroll"><table', '</table></div>')


def to_html(text):
    html = markdown.markdown(text, extensions=['fenced_code'])
    return html.replace('<table', TABLE_SCROLL[0]).replace('</table>', TABLE_SCROLL[1])


def load(path):
    text = open(path).read().replace('\r', '')

    match = FRONTMATTER.search(text)
    html = to_html(FRONTMATTER.sub('', text))

    heading = HEADING.search(text)
    if heading is not None:
        heading = heading.group(0).replace('#', '').strip()

    data = None

    if match is not None:
        block = match.group(0)
        if block[4:8].upper().strip() == 'JSON':
            data = json.loads(re.search(r'\{(.*)\}', block, re.DOTALL).group(0))
        else:
            data = yaml.safe_load(re.search(r'\n(.*)\n', block, re.DOTALL).group(0))
        data['title'] = heading
    elif heading is not None:
        data = {'title': heading}

    return {'data': data, 'html': html}
