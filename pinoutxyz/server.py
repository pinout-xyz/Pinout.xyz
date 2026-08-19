import os
import threading
import time

WATCH_DIRS = ('src', 'common', 'resources')
WATCH_INTERVAL = 1.0


def snapshot(root):
    seen = {}

    for watched in WATCH_DIRS:
        for base, dirs, files in os.walk(os.path.join(root, watched)):
            for name in files:
                path = os.path.join(base, name)
                try:
                    seen[path] = os.stat(path).st_mtime
                except OSError:
                    pass

    return seen


def changed_languages(root, changes, languages):
    prefix = os.path.join(root, 'src') + os.sep
    affected = set()

    for path in changes:
        if not path.startswith(prefix):
            return set(languages)
        lang = path[len(prefix):].split(os.sep)[0]
        if lang in languages:
            affected.add(lang)
        else:
            return set(languages)

    return affected


def watcher(root, languages, rebuild):
    previous = snapshot(root)

    while True:
        time.sleep(WATCH_INTERVAL)
        current = snapshot(root)

        changes = [path for path in current if previous.get(path) != current[path]]
        changes += [path for path in previous if path not in current]

        if not changes:
            continue

        affected = changed_languages(root, changes, languages)
        print('\nChanged: {}'.format(', '.join(sorted(os.path.relpath(path, root) for path in changes)[:5])))

        try:
            rebuild(sorted(affected))
        except Exception as error:
            print('Rebuild failed: {}'.format(error))

        previous = current


def serve(root, languages, port, watch):
    try:
        from flask import Flask, send_from_directory
    except ImportError:
        return 'This command requires Flask\nInstall with: pip install -r requirements.txt'

    from .cli import assemble, build_languages

    site = os.path.abspath(os.path.join(root, 'output', 'site'))
    app = Flask(__name__)

    @app.route('/')
    def index():
        return send_from_directory(site, 'index.html')

    @app.route('/<path:page>')
    def page(page):
        if os.path.isfile(os.path.join(site, page)):
            return send_from_directory(site, page)
        if os.path.isfile(os.path.join(site, '{}.html'.format(page))):
            return send_from_directory(site, '{}.html'.format(page))
        return send_from_directory(site, '{}/index.html'.format(page))

    if watch:
        def rebuild(affected):
            build_languages(root, affected or languages)
            assemble(root, languages)

        threading.Thread(target=watcher, args=(root, languages, rebuild), daemon=True).start()
        print('\nWatching {} for changes'.format(', '.join(WATCH_DIRS)))

    app.run(host='0.0.0.0', port=port)
    return 0
