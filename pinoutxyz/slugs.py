import re
import unicodedata


def slugify(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '_', value)


def cssify(value):
    value = slugify(value)
    if value[0] in ('3', '5'):
        return 'pow' + value
    return value
