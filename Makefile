LANG ?= en

LANG := $(subst -, ,$(LANG))
LANG := $(subst _, ,$(LANG))
LANG := $(firstword $(LANG))

LANGS := $(notdir $(wildcard src/??))
SITE := output/site

.PHONY: resources site site-lang

all: html resources

deps:
	python3 -m pip install -r requirements.txt

html:
	./generate-html.py $(LANG)

resources:
	cp -r resources phatstack output/$(LANG)/

site-lang: html
	mkdir -p $(SITE)
	if [ $(LANG) = en ]; then cp -r output/$(LANG)/. $(SITE)/; \
	else mkdir -p $(SITE)/$(LANG) && cp -r output/$(LANG)/. $(SITE)/$(LANG)/; fi
	cp -r resources phatstack $(SITE)/

site:
	rm -rf $(SITE)
	for lang in $(LANGS); do $(MAKE) site-lang LANG=$$lang; done

devel: serve

clean:
	rm -rf output/$(LANG)/* $(SITE)

serve: site-lang
	./serve.py
