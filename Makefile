all:
	./generate-html.py en-GB
	cp -r resources output/en-GB/

clean:
	rm -r output/en-GB/*

serve:
	cd output && python -m SimpleHTTPServer
