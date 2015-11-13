#!/usr/bin/env python
from flask import Flask, send_from_directory
import sys
app = Flask(__name__)

lang = 'en'

@app.route('/')
def show_index():
	return send_from_directory(basedir,'index.html')

@app.route("/resources/<path:filename>")
def custom_static(filename):
	return send_from_directory(basedir + 'resources/', filename)

@app.route("/<path:page>")
def show_page(page):
	return send_from_directory(basedir,'{}.html'.format(page))

if __name__ == "__main__":

	if len(sys.argv) > 1:
		lang = sys.argv[1]

	basedir = 'output/{lang}/'.format(lang=lang)

	app.run(host='0.0.0.0', debug=True)
