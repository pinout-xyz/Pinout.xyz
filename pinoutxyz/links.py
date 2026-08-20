import concurrent.futures
import urllib.error
import urllib.parse
import urllib.request

from . import documents, overlays, settings

LINK_KEYS = ('url', 'buy', 'github', 'schematic', 'docs')
AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'
RETRY_HEAD = (400, 403, 405, 406, 501)
BLOCKED = (401, 403, 429)


def collect(root):
    found = {}

    for lang in settings.languages(root):
        for name, path in overlays.named(root, lang).items():
            data = documents.frontmatter(path) or {}
            for key in LINK_KEYS:
                value = data.get(key)
                if isinstance(value, str) and value.startswith(('http://', 'https://')):
                    found.setdefault(value.strip(), []).append('{}/{} {}'.format(lang, name, key))

    return found


def probe(url, timeout):
    for method in ('HEAD', 'GET'):
        request = urllib.request.Request(url, method=method, headers={'User-Agent': AGENT})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.status, response.geturl()
        except urllib.error.HTTPError as error:
            if method == 'HEAD' and error.code in RETRY_HEAD:
                continue
            return error.code, url
        except Exception as error:
            if method == 'HEAD':
                continue
            return type(error).__name__, url

    return 'Unreachable', url


def same_place(before, after):
    first, second = urllib.parse.urlsplit(before), urllib.parse.urlsplit(after)
    if first.netloc.lstrip('www.') != second.netloc.lstrip('www.'):
        return False
    return first.path.rstrip('/') == second.path.rstrip('/')


def report_check(root, timeout, workers):
    links = collect(root)
    references = sum(len(where) for where in links.values())
    print('Checking {} links from {} references across {} languages'.format(
        len(links), references, len(settings.languages(root))))
    print('This fetches every URL in the board data, so it is deliberately not part of CI.\n')

    broken, blocked, moved = [], [], []
    done = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        pending = {pool.submit(probe, url, timeout): url for url in sorted(links)}

        for future in concurrent.futures.as_completed(pending):
            url = pending[future]
            status, final = future.result()
            done += 1
            print('\r  {}/{}'.format(done, len(links)), end='', flush=True)

            if status in BLOCKED:
                blocked.append((url, status))
            elif not isinstance(status, int):
                broken.append((url, status))
            elif status >= 400:
                broken.append((url, status))
            elif not same_place(url, final):
                moved.append((url, final))

    print('\r  {0}/{0} checked\n'.format(len(links)))

    for title, rows in (('Broken', broken), ('Redirected', moved), ('Blocked, probably bot protection', blocked)):
        if not rows:
            continue
        print('{} ({}):'.format(title, len(rows)))
        for url, detail in sorted(rows):
            print('  {}\n    {}'.format(url, detail))
            for where in sorted(links[url]):
                print('      {}'.format(where))
        print()

    print('{} broken, {} redirected, {} blocked, {} fine'.format(
        len(broken), len(moved), len(blocked), len(links) - len(broken) - len(moved) - len(blocked)))

    return 1 if broken else 0
