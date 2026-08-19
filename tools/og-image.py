#!/usr/bin/env python3

import functools
import os
import subprocess
import shutil
import tempfile
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

try:
    from PIL import Image
except ImportError:
    exit("This script requires the Pillow module\nInstall with: pip install Pillow")

WIDTH, HEIGHT = 1200, 630
SITE = 'output/site'
OUTPUT = 'api/index.png'
TIMEOUT = 60

CHROME = [
    os.environ.get('CHROME'),
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    'google-chrome',
    'chromium',
]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def find_chrome():
    for candidate in CHROME:
        if candidate and (os.path.isfile(candidate) or shutil.which(candidate)):
            return candidate
    exit("Unable to find Chrome, set CHROME to its path")


def serve(directory):
    handler = functools.partial(QuietHandler, directory=directory)
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    Thread(target=server.serve_forever, daemon=True).start()
    return server


def screenshot(chrome, url, path, profile):
    process = subprocess.Popen([
        chrome,
        '--headless',
        '--disable-gpu',
        '--hide-scrollbars',
        '--force-color-profile=srgb',
        '--no-first-run',
        '--no-default-browser-check',
        '--user-data-dir=' + profile,
        '--window-size={},{}'.format(WIDTH, HEIGHT),
        '--screenshot=' + path,
        url,
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Chrome writes the screenshot but will not reliably exit, so wait for the
    # file to stop growing and stop it ourselves.
    previous_size = 0
    deadline = time.time() + TIMEOUT
    while time.time() < deadline:
        time.sleep(0.5)
        if os.path.exists(path):
            size = os.path.getsize(path)
            if size > 0 and size == previous_size:
                break
            previous_size = size
        elif process.poll() is not None:
            exit("Chrome exited without taking a screenshot")

    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()

    if not os.path.exists(path):
        exit("Timed out waiting for a screenshot")


if not os.path.isdir(SITE):
    exit("No {} to shoot, run: make site-lang LANG=en".format(SITE))

chrome = find_chrome()
server = serve(SITE)
url = 'http://127.0.0.1:{}/index.html'.format(server.server_port)

with tempfile.TemporaryDirectory() as tmp:
    shot = os.path.join(tmp, 'shot.png')
    screenshot(chrome, url, shot, os.path.join(tmp, 'profile'))

    image = Image.open(shot).convert('RGB')
    if image.size != (WIDTH, HEIGHT):
        exit("Expected {}x{}, got {}x{}".format(WIDTH, HEIGHT, *image.size))
    image.convert('P', palette=Image.ADAPTIVE, colors=256).save(OUTPUT, optimize=True)

server.shutdown()

print("Saved {} ({}x{}, {} bytes)".format(OUTPUT, WIDTH, HEIGHT, os.path.getsize(OUTPUT)))
