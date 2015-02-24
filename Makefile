all:
	./generate-html.py > output/test.html

serve:
	cd output && python -m SimpleHTTPServer
