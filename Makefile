LANG ?= en

LANG := $(subst -, ,$(LANG))
LANG := $(subst _, ,$(LANG))
LANG := $(firstword $(LANG))

.PHONY: resources

all:
	scss resources/pinout.scss > resources/pinout.scss.css
	./generate-html.py $(LANG)
	cp -r resources output/$(LANG)/

resources:
	cp -r resources output/$(LANG)/

clean:
	rm -rf output/$(LANG)/*

serve: all
	./serve.py $(LANG)
