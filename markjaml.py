import json
import re
import unicodedata

try:
    import markdown
except ImportError:
    exit("This script requires the Markdown module\nInstall with: sudo pip install Markdown")

try:
    import yaml
except ImportError:
    exit("This script requires the yaml module\nInstall with: sudo pip install PyYAML")


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '-', value).strip().lower()
    return re.sub('[-\s]+', '-', value)


def load(file):
    '''
    Loads and parses JSON-embedded Markdown file, chopping out and
    parsing any JSON contained therein.

    Returns an object that includes the JSON data, and the parsed HTML.
    '''
    markson = open(file).read()
    markson = markson.replace('\r','')

    _data = re.search(re.compile(r'<!--(JSON:|\n---\n)(.*)-->', re.DOTALL), markson)

    _markdown = re.sub(re.compile(r'<!--(JSON:|\n---\n)(.*)-->', re.DOTALL), '', markson)
    _html = markdown.markdown(_markdown, extensions=['fenced_code'])

    # Scan for the Title in the Markdown file, this is always assumed
    # to be the first string starting with a single hash/pound ( # ) sign
    _title = re.search(re.compile(r'^#[^\#](.*)$', re.MULTILINE), markson)

    if _title != None:
        _title = _title.group(0).replace('#', '').strip()

    if _data != None:
        _type = _data.group(0)[4:8].upper().strip()

        if _type == 'JSON':
            _data = re.search('\{(.*)\}', _data.group(0), re.DOTALL).group(0)
            _data = json.loads(_data)
        elif _type == '---':
            _data = re.search('\n(.*)\n', _data.group(0), re.DOTALL).group(0)
            _data = yaml.load(_data)
        else:
            data = {}

        _data['title'] = _title

    elif _title != None:
        _data = {'title':_title}

    return {'data':_data, 'html':_html}