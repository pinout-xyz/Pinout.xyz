LANG ?= en

LANG := $(subst -, ,$(LANG))
LANG := $(subst _, ,$(LANG))
LANG := $(firstword $(LANG))

all:
	./generate-html.py $(LANG)
	cp -r resources output/$(LANG)/

clean:
	rm -rf output/$(LANG)/*

serve: all
	./serve.py $(LANG)
