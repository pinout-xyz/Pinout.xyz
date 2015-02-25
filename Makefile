all:
	./generate-html.py

serve:
	cd output && python -m SimpleHTTPServer
