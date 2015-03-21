all:
	./generate-html.py
	cp -r resources output/

clean:
	rm -r output/*

serve:
	cd output && python -m SimpleHTTPServer
