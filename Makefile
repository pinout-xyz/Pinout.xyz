all:
	./generate-html.py en-GB
	cp -r resources output/en-GB/

clean:
	rm -r output/en-GB/*

serve:
	./serve.py en-GB
