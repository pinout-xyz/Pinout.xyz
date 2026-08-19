LANG ?= en

LANG := $(subst -, ,$(LANG))
LANG := $(subst _, ,$(LANG))
LANG := $(firstword $(LANG))

.PHONY: resources

all: html resources

deps:
	python3 -m pip install -r requirements.txt

html:
	./generate-html.py $(LANG)

resources:
	cp -r resources phatstack output/$(LANG)/

devel: all resources
	./serve.py ${LANG}

clean:
	rm -rf output/$(LANG)/*

serve: all
	./serve.py $(LANG)
