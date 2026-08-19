LANG ?= en

LANG := $(subst -, ,$(LANG))
LANG := $(subst _, ,$(LANG))
LANG := $(firstword $(LANG))

LANGS := $(notdir $(wildcard src/??))
SITE := output/site

.PHONY: resources site

all: html resources

deps:
	python3 -m pip install -r requirements.txt

html:
	./generate-html.py $(LANG)

resources:
	cp -r resources phatstack output/$(LANG)/

site:
	rm -rf $(SITE)
	for lang in $(LANGS); do ./generate-html.py $$lang; done
	mkdir -p $(SITE)
	cp -r output/en/. $(SITE)/
	for lang in $(LANGS); do \
		if [ $$lang != en ]; then mkdir -p $(SITE)/$$lang && cp -r output/$$lang/. $(SITE)/$$lang/; fi; \
	done
	cp -r resources phatstack $(SITE)/

devel: serve

clean:
	rm -rf output/$(LANG)/* $(SITE)

serve: site
	./serve.py
