LANG ?= en-GB

all:
	./generate-html.py $(LANG)
	cp -r resources output/$(LANG)/

clean:
	rm -r output/$(LANG)/*

serve:
	./serve.py $(LANG)
