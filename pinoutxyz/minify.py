import os

MISSING = ('Minifying needs rcssmin and rjsmin:\n'
           '    python3 -m pip install -r requirements.txt')


def minifiers():
    try:
        import rcssmin
        import rjsmin
    except ImportError:
        raise SystemExit(MISSING)

    return {'.css': rcssmin.cssmin, '.js': rjsmin.jsmin}


def assets(root, suffixes):
    for path, _, names in os.walk(root):
        for name in sorted(names):
            if os.path.splitext(name)[1] in suffixes:
                yield os.path.join(path, name)


def run(root, report=None):
    minify = minifiers()
    before = after = 0

    for path in assets(root, minify):
        source = open(path).read()
        result = minify[os.path.splitext(path)[1]](source)

        if len(result) >= len(source):
            continue

        open(path, 'w').write(result)
        before += len(source)
        after += len(result)

        if report:
            report(os.path.relpath(path, root), len(source), len(result))

    return before, after
